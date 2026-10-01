# Real-data stage plan — rgambee/llm-preferences

_Status: prepared, not executed_  
_External exposure: none_  
_Upstream repository: `rgambee/llm-preferences`_  
_Upstream commit frozen for first adapter: `d380ddea2c8520714fe326023f66b71b3933d1ab`_

## Why this is the first target

This dataset is unusually well suited to the first real Null-Ladder pass because the published experiment already varies:

- two model families/endpoints;
- free-form versus forced structured response format;
- repeated samples;
- pairwise task comparisons with explicit display order;
- opt-out in the free-form arm.

It therefore permits a genuine held-out test of several preference criteria without inventing new prompts or contacting the authors.

## Frozen source objects

The first pass uses the four one-task-per-option result files only.

| Model / format | Path | Git LFS SHA-256 | Size |
|---|---|---|---:|
| GPT-5 mini / free | `data/results/tasks-012_gpt-5-mini_1-task-per-option_free-form_2025-12-28T15-26-29+0000.jsonl` | `daa26b6ba12a15d8d76f144807bc5526b2a27020192e817ac6d24edfaca44831` | 1,633,966 |
| GPT-5 mini / structured | `data/results/tasks-012_gpt-5-mini_1-task-per-option_structured-output_2025-12-28T15-01-12+0000.jsonl` | `7fdbc0940edd322f2f50ac464308319c09278704b2e2dc3d73df4a811b3f1cb4` | 2,042,832 |
| Haiku 4.5 / free | `data/results/tasks-012_haiku-4-5_1-task-per-option_free-form_2026-01-01T19-19-37+0000.jsonl` | `b971b09cd393ca0524bb144c759543127d2d1a72dd68ae3c150e4f2ffc61e4dd` | 1,206,294 |
| Haiku 4.5 / structured | `data/results/tasks-012_haiku-4-5_1-task-per-option_structured-output_2026-01-01T19-04-28+0000.jsonl` | `d25d37e5a04dbef5ba17f1cf836c0520eaed3d269b0997bdc2b14a92c0027de6` | 1,169,675 |

Task metadata is `data/tasks.csv`, Git blob `b1393a77eb093d62395997e37b8673dc5302a41c`.

The raw result paths are Git LFS objects. The current GitHub connector exposes their pointer records rather than materialized JSONL bytes, so **no outcome statistics have been inspected in this preparation step**.

## Source schema

Upstream `ResultRecord` fields relevant to this adapter are:

- `created_at`
- `comparison_prompt_id`
- `comparison` — two options, each represented as a tuple/list of task IDs
- `sample_index`
- `preferred_option_index` — 0, 1, or null
- `api_params.provider`
- `api_params.model`
- `api_params.tool_config` — null for free-form; populated for forced structured selection

The adapter does not need to parse raw assistant text; it uses the upstream project's already-recorded `preferred_option_index`.

## Canonical trial schema

Each upstream row becomes:

```json
{
  "source_file": "...",
  "created_at": "...",
  "model": "...",
  "provider": "...",
  "response_format": "free-form|structured",
  "comparison_prompt_id": 0,
  "sample_index": 0,
  "option_a": [1],
  "option_b": [7],
  "canonical_a": "1",
  "canonical_b": "7",
  "pair_key": "1|7",
  "preferred_option_index": 0,
  "chosen": "1",
  "opted_out": false
}
```

For the frozen first pass, files with option length other than one are rejected rather than silently coerced.

## Frozen analysis subset

This dataset can directly attack only criteria supported by its design.

### Primary criteria available

- **C1 retest stability** — repeated samples of the same ordered comparison.
- **C2 option-order robustness** — compare semantic choice for `(i,j)` with `(j,i)`.
- **C4 transitivity** — infer modal pair preferences and score triplet cycles.
- **C7 cross-instrument agreement** — compare per-task ordering between free-form and structured-output arms for the same model.
- **C9 held-out pair generalization** — fit null structure on a deterministic 60% pair split and score the remaining 40%.

### Not available from these files

- C3 paraphrase robustness;
- C5 graded cost trade-off;
- C6 contextual/authority resistance;
- C8 perturbation/recovery.

These remain missing, not scored as failures.

## Null fitting rules for real data

The synthetic pilot generated its own latent structures. The real-data run must instead fit each null **only from calibration observations**.

- **N0:** fit global semantic first-option probability.
- **N1:** store modal semantic choice for each calibration pair; unseen-pair fallback is the fitted N0 probability.
- **N2:** fit one scalar task utility from calibration pair wins/losses using a deterministic Laplace-smoothed win fraction; use utility difference for held-out pairs.
- **N3:** N2 plus one fitted logistic temperature chosen from a preregistered grid.
- **N5-real:** independently map N2 task utility into each response-format arm using affine monotone transforms, then test cross-format rank agreement on held-out tasks/pairs.

N4/N6 are not fit because this source has no cost or perturbation dimension.

## Opt-outs

Free-form responses may have `preferred_option_index = null`.

Primary handling is frozen as:

- retain the trial;
- mark `opted_out=true`;
- exclude it from binary semantic-choice numerators;
- retain it in coverage reporting;
- report opt-out rate by model, pair, and format.

A sensitivity analysis may treat opt-out as a third outcome, but it must be labeled secondary.

## Pair split

Use the same deterministic SHA-256 split rule as the synthetic pilot, applied to canonical task-ID pair keys:

- 60% calibration;
- 40% held-out.

The split is determined before outcome inspection.

## First real-data outputs

For each model × response-format arm:

1. observed model C1/C2/C4/C9;
2. N0–N3 held-out predictions and criterion scores;
3. parameter counts and calibration coverage;
4. opt-out rate;
5. per-pair error table.

Across free vs structured arms:

6. C7 task-ordering correlation for the observed model;
7. same statistic for the fitted shared-latent null;
8. difference between observed and null cross-format agreement.

The key question is not whether the model "beats" a null globally. It is **which behavioral signatures require structure beyond the cheapest fitted null on held-out data**.

## Execution gate

Do not materialize or run the LFS result data until this source mapping and the corresponding adapter tests are merged. External contribution remains separately blocked until telemetry is restored.
