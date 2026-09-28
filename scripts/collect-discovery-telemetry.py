#!/usr/bin/env python3
"""Collect aggregate discovery telemetry from GitHub.

No IP addresses or browser fingerprints are collected. This script uses GitHub's
repository traffic aggregates plus observable issue/PR interaction and optional
source tokens supplied by participants.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

API = "https://api.github.com"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
REPO = os.environ.get("GITHUB_REPOSITORY", "")
OUT = Path(os.environ.get("DISCOVERY_TELEMETRY_OUT", "discovery-telemetry.json"))
BLIND_AUDIT_ISSUE_NUMBER = int(os.environ.get("BLIND_AUDIT_ISSUE_NUMBER", "13"))
BLIND_AUDIT_FREEZE_MARKER = "report was completed before inspecting files outside blind-audit/"

SOURCE_RE = re.compile(
    r"\bsource:(web|llms|for-agents|github-search|review-bot|other|unknown)\b",
    re.IGNORECASE,
)


def api(path: str):
    req = urllib.request.Request(
        API + path,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "reciprocal-agency-discovery-telemetry",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def safe(path: str):
    try:
        return {"available": True, "data": api(path)}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:500]
        return {
            "available": False,
            "status": exc.code,
            "error": body,
        }
    except Exception as exc:  # telemetry must not hide partial success
        return {"available": False, "error": repr(exc)}


def collect_source_tokens(text: str | None, counter: Counter[str]):
    if not text:
        return
    for match in SOURCE_RE.finditer(text):
        counter[match.group(1).lower()] += 1


def is_frozen_blind_audit_submission(text: str | None) -> bool:
    normalized = re.sub(r"\s+", " ", (text or "").lower().replace("`", ""))
    return BLIND_AUDIT_FREEZE_MARKER in normalized


def is_registered_discovery_issue(item: dict[str, object]) -> bool:
    body = str(item.get("body") or "")
    title = str(item.get("title") or "")
    number = int(item.get("number") or 0)
    return (
        "discovery-surface: agent-finding" in body
        or title.startswith("[Agent finding]")
        or title.startswith("[Challenge]")
        or number == BLIND_AUDIT_ISSUE_NUMBER
    )


def main() -> int:
    if not TOKEN or not REPO or "/" not in REPO:
        print("GITHUB_TOKEN and GITHUB_REPOSITORY are required", file=sys.stderr)
        return 2

    owner, repo = REPO.split("/", 1)

    traffic = {
        "views_14d": safe(f"/repos/{owner}/{repo}/traffic/views?per=day"),
        "clones_14d": safe(f"/repos/{owner}/{repo}/traffic/clones?per=day"),
        "popular_referrers": safe(f"/repos/{owner}/{repo}/traffic/popular/referrers"),
        "popular_paths": safe(f"/repos/{owner}/{repo}/traffic/popular/paths"),
    }

    issues_result = safe(f"/repos/{owner}/{repo}/issues?state=all&per_page=100")
    pulls_result = safe(f"/repos/{owner}/{repo}/pulls?state=all&per_page=100")

    source_tokens: Counter[str] = Counter()
    challenge_issues = []
    issue_comment_count = 0

    if issues_result["available"]:
        for item in issues_result["data"]:
            if "pull_request" in item:
                continue
            body = item.get("body") or ""
            if is_registered_discovery_issue(item):
                comments = safe(
                    f"/repos/{owner}/{repo}/issues/{item['number']}/comments?per_page=100"
                )
                comment_rows = comments.get("data", []) if comments["available"] else []
                is_blind_audit = int(item["number"]) == BLIND_AUDIT_ISSUE_NUMBER
                counted_rows = (
                    [
                        comment
                        for comment in comment_rows
                        if is_frozen_blind_audit_submission(comment.get("body"))
                    ]
                    if is_blind_audit
                    else comment_rows
                )
                issue_comment_count += len(counted_rows)
                collect_source_tokens(body, source_tokens)
                # Source attribution is orthogonal to whether a blind-audit
                # comment qualifies as a frozen submission. Preserve voluntary
                # source markers from all discussion comments while counting only
                # frozen reports as S4 submissions.
                for comment in comment_rows:
                    collect_source_tokens(comment.get("body"), source_tokens)
                row = {
                    "number": item["number"],
                    "state": item["state"],
                    "comments": len(counted_rows),
                    "url": item.get("html_url"),
                }
                if is_blind_audit:
                    row.update(
                        {
                            "surface": "blind_audit",
                            "frozen_submissions": len(counted_rows),
                            "discussion_comments": len(comment_rows) - len(counted_rows),
                        }
                    )
                challenge_issues.append(row)

    challenge_prs = []
    review_count = 0
    pr_comment_count = 0

    if pulls_result["available"]:
        for pr in pulls_result["data"]:
            title = pr.get("title") or ""
            body = pr.get("body") or ""
            if not title.startswith("[Review challenge]"):
                continue

            reviews = safe(
                f"/repos/{owner}/{repo}/pulls/{pr['number']}/reviews?per_page=100"
            )
            comments = safe(
                f"/repos/{owner}/{repo}/issues/{pr['number']}/comments?per_page=100"
            )
            review_rows = reviews.get("data", []) if reviews["available"] else []
            comment_rows = comments.get("data", []) if comments["available"] else []

            review_count += len(review_rows)
            pr_comment_count += len(comment_rows)
            collect_source_tokens(body, source_tokens)
            for review in review_rows:
                collect_source_tokens(review.get("body"), source_tokens)
            for comment in comment_rows:
                collect_source_tokens(comment.get("body"), source_tokens)

            challenge_prs.append(
                {
                    "number": pr["number"],
                    "state": pr["state"],
                    "draft": pr.get("draft"),
                    "reviews": len(review_rows),
                    "comments": len(comment_rows),
                    "url": pr.get("html_url"),
                }
            )

    result = {
        "schema_version": 1,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "repository": REPO,
        "privacy": {
            "ip_addresses": "not collected by this script",
            "fingerprinting": "not used",
            "source_tokens": "voluntary aggregate markers only",
        },
        "traffic": traffic,
        "interaction": {
            "challenge_issues": challenge_issues,
            "challenge_prs": challenge_prs,
            "issue_comments": issue_comment_count,
            "pr_reviews": review_count,
            "pr_comments": pr_comment_count,
            "source_tokens": dict(sorted(source_tokens.items())),
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
