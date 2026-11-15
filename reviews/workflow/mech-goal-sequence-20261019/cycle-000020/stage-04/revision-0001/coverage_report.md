# Cycle 20 Stage 4 Record Review Coverage Report

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle:** `20`
- **Stage:** `4` (`record_review`)
- **Revision:** `revision-0001`
- **Source Revision:** `24d76baa823d7fd07e8ea2596f0cca50e66392e2`

## Corpus Coverage

| Surface | Current Count | Coverage |
| --- | ---: | --- |
| `data/ingredients/mapped/*.yaml` | `2,681` | All current mapped directory records are present in native structured review `targets:` across `reviews/structured/`. |
| `data/ingredients/unmapped/*.yaml` | `275` | All current unmapped directory records are present in native structured review `targets:` across `reviews/structured/`. |
| **`data/ingredients/**/*.yaml`** | **`2,956`** | **`2,956 / 2,956` current individual records are covered and source-hash verified by `scripts/record_review.py --repo-root . check`.** |
| `data/curated/*.yaml` | `7` | Aggregate and generated unmapped-slice collections are retained as checked review context. |
| `reviews/structured/*/review.yaml` | `1,016` | All native structured review bundles have a matching generated `review.md`. |

## Native Review Bundle Coverage

| Review Kind | Bundle Count | Notes |
| --- | ---: | --- |
| `record` | `965` | Per-record review observations, including successor reassessments. |
| `category` | `1` | Carnitine hydrochloride cohort review. |
| `batch` | `33` | Existing corpus/source/SSSOM review batches plus `20261111T061500Z-cas-chebi-grounding-and-polysalt-audit`. |
| `repository` | `17` | Repository-level review and SSSOM diagnostic bundles. |
| **Total** | **`1,016`** | **`2,032` retained files.** |

## Delta Since Cycle 19 Stage 4

The Cycle 19 Stage 4 source revision was
`c8f1be257770608369be85769f5e572662a7ef1e`. Cycle 20 Stage 4 rechecked the
review surfaces at `24d76baa823d7fd07e8ea2596f0cca50e66392e2`:

| Surface | Delta |
| --- | --- |
| `data/ingredients/` | `0` files changed |
| `data/curated/` | `0` files changed |
| `mappings/ingredient_mappings.sssom.tsv` | `0` files changed |
| `UNIFIED_INGREDIENT_MAPPING.tsv` | `0` files changed |
| `schema/record_review.yaml` | `0` files changed |
| `src/mediaingredientmech/schema/mediaingredientmech.yaml` | `0` files changed |
| `reviews/structured/` | `1` new structured batch bundle: `20261111T061500Z-cas-chebi-grounding-and-polysalt-audit` |

The new native batch review covers 54 existing ingredient records and contributes
three deferred findings:

1. `mim-c20-s04-f001` carries native issue key
   `mim-cas-chebi-ols4-seed-candidates-13`.
2. `mim-c20-s04-f002` carries native issue key
   `mim-unmapped-cas-rn-groundings-2`.
3. `mim-c20-s04-f003` carries native issue key
   `mim-polysalt-deduplicated-smiles-refused-39`.

## Deferred Finding Coverage

| Source | Deferred Workflow Findings | Issue Status |
| --- | ---: | --- |
| Cycle 19 Stage 5 carry-forward (`mim-c01-s04-f001`, `mim-c01-s04-f003`..`mim-c01-s04-f007`) | `6` | Deduplicated under existing issues `#921`, `#923`, and `#718` |
| CAS/ChEBI batch review added in PR `#1361` | `3` | Requires Cycle 20 Stage 5 deduplication and issue linkage |
| **Total** | **`9`** | **All `9` are `deferred` and listed in `evidence.yaml` `carry_forward_ids`.** |

## Exclusions

- Existing immutable `reviews/structured/` bundles were not rewritten.
- No ingredient records were sampled out of the target inventory.
- No Stage 4 finding was closed or marked accepted-risk; Stage 5 owns grouped
  disposition and issue linkage.
- `reviews/workflow/latest.yaml` remains at the last verified closure index
  synchronized in Cycle 20 Stage 1.
