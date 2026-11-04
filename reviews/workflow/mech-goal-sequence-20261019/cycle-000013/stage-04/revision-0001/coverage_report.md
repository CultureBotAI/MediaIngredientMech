# Cycle 13 Stage 4 Corpus and Structured Review Coverage Report (`coverage_report`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle**: `13` (`cycle-000013`)
- **Stage**: `4` (`stage-04` / `record_review`)
- **Revision**: `revision-0001`
- **Base Commit (`main`)**: `99fe4b44d78126d78041a69eeb366c52bedf0caa`

---

## 1. Corpus Accounting (`2,955` Individual Records + `7` Curated Collections = `2,962` YAML Documents)

| Directory / Surface | File Count | Status Breakdown | Manifest SHA-256 (`sha256sum`) |
| --- | ---: | --- | --- |
| `data/ingredients/mapped/*.yaml` | `2,680` | `2,611` `MAPPED`, `69` `REJECTED` | `fe35b92f81cc507d1112cea6db7d080679145ea0914eb6fa340491a705663fc5` |
| `data/ingredients/unmapped/*.yaml` | `275` | `262` `UNMAPPED`, `1` `AMBIGUOUS`, `12` `REJECTED` | `564f397b0c83d3147996ed648c465880a0c86869ec5c8a5170a55bc4ad787f3f` |
| **Total Individual Records (`data/ingredients/**/*.yaml`)** | **`2,955`** | **`2,611` `MAPPED`, `262` `UNMAPPED`, `1` `AMBIGUOUS`, `81` `REJECTED`** | **`7e734ef21db8f041cfd6ab9bbbd939558db7422b85609b38547a04a9375f89be`** |
| `data/curated/*.yaml` | `7` | `mapped_ingredients.yaml` (`2,680`), `unmapped_ingredients.yaml` (`275`), plus `5` legacy/subset collections | `mapped_ingredients.yaml`: `2bc4b3663ea6beae04693bd517e2901ce69cf912d828599a0b1f7c19d2f8ba77`; `unmapped_ingredients.yaml`: `22ececf4e0e7a37ca0636d4635ed5408a6517ba7ef6e7a1daf713f09a7802cd8` |
| **Total Validated YAML Documents** | **`2,962`** | `0` strict LinkML errors | Verified via `scripts/record_review.py check` and `scripts/validate_strict.py` |

---

## 2. Structured Review Bundle Inventory (`986` Bundles / `1,972` Files)

| Bundle Series | `kind` | Bundle Count | Verdict Breakdown | Target Coverage |
| --- | --- | ---: | --- | --- |
| `20261017T083000Z-*` | `record` | `961` | `961` `needs_curation` | `961` mapped records with `INSUFFICIENT_EVIDENCE` findings |
| `20261021T120500Z-ca-no32-x-4-h2o` | `record` | `1` | `1` `pass_with_limitations` | `1` remediated mapped record (`data/ingredients/mapped/Ca_No32_X_4_H2o.yaml`) |
| `20261101T004549Z-na2hpo4-heptahydrate-exact-identity` | `record` | `1` | `1` `needs_curation` | `1` mapped record (`data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml`) |
| `20261101T005659Z-melezitose-formof-blocked-review` | `record` | `1` | `1` `blocked` | `1` mapped record (`data/ingredients/mapped/D-_-melezitose_Monohydrate.yaml`) |
| `20261101T005710Z-carnitine-amide-alias-scientific` | `record` | `1` | `1` `pass_with_limitations` | `1` mapped record (`data/ingredients/mapped/Carnitine_Hydrochloride.yaml`, `962`nd distinct mapped record in `kind: record` bundles) |
| `20261011T080001Z-mim-*` .. `20261011T080014Z-mim-*` | `batch` | `14` | `13` `needs_curation`, `1` `not_assessed` | All `2,953` pre-PR-#1026 individual records (`2,680` mapped + `273` unmapped) |
| `20261101T005710Z-seven-generated-alias-rulings` | `batch` | `1` | `1` `pass_with_limitations` | `7` mapped records audited for generated-alias contamination in PR `#1007` |
| `20261101T*` repository review bundles (`6` bundles) | `repository` | `6` | `6` `pass_with_limitations` | `12` distinct individual records (including the `2` new unmapped hydrate records `Na2moo4_X_H2o.yaml` and `Trisodium_Citrate_X_3_H2o.yaml`), `2` curated collections, SSSOM, browser/index exports, and governance scripts/tests |
| **Total** | **`965` `record` + `15` `batch` + `6` `repository`** | **`986`** | **`975` `needs_curation`, `9` `pass_with_limitations`, `1` `blocked`, `1` `not_assessed`** | **`2,955 / 2,955` (`100.00%`) individual ingredient YAML records declared in `targets:`** |

---

## 3. Disjoint Partition of the `2,955` Individual Records

| Partition Cohort | Primary Structured Review Bundle(s) | Record Count | Share of Corpus (`2,955`) |
| --- | --- | ---: | ---: |
| Mapped records with `RECORD_DEFECT` (and/or `INSUFFICIENT_EVIDENCE`) | `20261011T080001Z`–`20261011T080010Z`, `20261101T035857Z-approved-plan-step1-unified-review`, `20261101T054115Z-approved-step2-ncit-heptahydrate-review` | `460` | `15.57%` |
| Mapped records with only `INSUFFICIENT_EVIDENCE` (remediated in Cycle 1 Stage 5) | `20261021T120500Z-ca-no32-x-4-h2o` (`Ca_No32_X_4_H2o.yaml`) | `1` | `0.03%` |
| Mapped records with only `INSUFFICIENT_EVIDENCE` (open) | `20261017T083000Z-*` & `20261011T080011Z-mim-insufficient-evidence-reconciliation` | `847` | `28.66%` |
| Mapped records with `REJECTED` status | `20261011T080013Z-mim-rejected-records-reconciliation` | `69` | `2.34%` |
| Remaining mapped records without prior blocking findings (`not_assessed` in batch reconciliation; includes `Carnitine_Hydrochloride.yaml` reviewed in `20261101T005710Z-carnitine-amide-alias-scientific`) | `20261011T080014Z-mim-remaining-corpus-reconciliation` & `20261101T005710Z-*` | `1,303` | `44.10%` |
| Unmapped directory records with `UNMAPPED` (`260`) or `AMBIGUOUS` (`1`) status (pre-PR-#1026) | `20261011T080012Z-mim-unmapped-backlog-reconciliation` | `261` | `8.83%` |
| Unmapped directory records newly split in PR `#1026` (`Na2moo4_X_H2o.yaml` [`UNMAPPED_0851`], `Trisodium_Citrate_X_3_H2o.yaml` [`UNMAPPED_0852`]) | `20261101T035857Z-approved-plan-step1-unified-review` | `2` | `0.07%` |
| Unmapped directory records with `REJECTED` status | `20261011T080013Z-mim-rejected-records-reconciliation` | `12` | `0.41%` |
| **Total Individual Records** | **`986` structured review bundles** | **`2,955`** | **`100.00%`** |
