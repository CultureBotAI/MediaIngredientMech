# Media Ingredient Mapping Review

Generated: 2026-05-05
Branch: `review-media-ingredient-mappings`

## Scope

This review covers both authoritative individual ingredient records and older
aggregate/index views.

Files inspected:

- `data/ingredients/mapped/*.yaml`
- `data/ingredients/unmapped/*.yaml`
- `data/curated/mapped_ingredients.yaml`
- `data/curated/unmapped_ingredients.yaml`
- `data/curated/MAPPED_INGREDIENTS.md`
- `data/curated/UNMAPPED_INGREDIENTS.md`
- `docs/data/mapped_ingredients.csv`
- `docs/data/unmapped_ingredients.csv`
- `mappings/ingredient_mappings.sssom.tsv`
- `mappings/complex_ingredients.tsv`
- `MAPPING_SEMANTICS.md`
- `CURATION_PRIORITY_LIST.md`
- `notes/unmapped_analysis.md`
- `data/custom/kgmicrobe_ingredients.tsv`

## Summary

The most current data appear to be the individual YAML records under
`data/ingredients/`, not the aggregate files in `data/curated/`.

Observed counts:

| Source | Mapped | Unmapped | Notes |
|---|---:|---:|---|
| `data/ingredients/mapped/*.yaml` | 1,861 | 0 | Current granular mapped records |
| `data/ingredients/unmapped/*.yaml` | 0 | 480 | Current granular unmapped records |
| `data/curated/mapped_ingredients.yaml` | 1,004 | 0 | Stale aggregate relative to individual records |
| `data/curated/unmapped_ingredients.yaml` | 0 | 0 | Stale/empty aggregate |
| `data/curated/UNMAPPED_INGREDIENTS.md` | 0 | 68 | Older generated index |

Primary recommendations:

1. Treat `data/ingredients/{mapped,unmapped}` as the working curation source.
2. Regenerate aggregate/index outputs after review, or clearly mark stale outputs
   as historical.
3. Prioritize exact local duplicate cleanup in unmapped records before doing new
   external ontology searches.
4. Manually review the mapped records below before exporting to KG-Microbe.

## Mapped Ingredient Issues

### Likely Incorrect Mappings

These records look incorrect or overly broad based on the local labels,
mapping evidence, and mapping semantics. Suggested action is review before
automatic export.

| Record | Current mapping | Issue | Suggested edit | Confidence |
|---|---|---|---|---|
| `data/ingredients/mapped/Tetramethyl_Ammonium_Chloride.yaml` | `CHEBI:31206` ammonium chloride, `LEXICAL_MATCH` | "Tetramethyl ammonium chloride" is not ammonium chloride; the auto-upgrade used a stem-substring match and dropped the tetramethyl substituent. | Replace with an exact tetramethylammonium chloride ontology term if present; otherwise revert to unmapped or mint a kg-microbe compound with a parent/narrow mapping only after validation. | High |
| `data/ingredients/mapped/P-Amino_Benzoic_Acid.yaml` | `CHEBI:30746` benzoic acid, `LEXICAL_MATCH` | p-Aminobenzoic acid is more specific than benzoic acid and should not be treated as resolved to benzoic acid. | Remap to p-aminobenzoic acid if an ontology term is available; otherwise use a non-identity parent mapping with a kg-microbe identity row. | High |
| `data/ingredients/mapped/Butyrate_(sodium_Salt).yaml` | `CHEBI:26714` sodium salt, `LEXICAL_MATCH` | Maps a specific organic acid salt to the generic class "sodium salt". | Remap to sodium butyrate/butanoate if available, or use a non-identity parent mapping plus registry row. | High |
| `data/ingredients/mapped/Lactate_(sodium_Salt).yaml` | `CHEBI:26714` sodium salt, `LEXICAL_MATCH` | Same generic sodium-salt parent problem. | Remap to sodium lactate if available, or use non-identity parent mapping plus registry row. | High |
| `data/ingredients/mapped/Propionate_(sodium_Salt).yaml` | `CHEBI:26714` sodium salt, `LEXICAL_MATCH` | Same generic sodium-salt parent problem. | Remap to sodium propionate if available, or use non-identity parent mapping plus registry row. | High |
| `data/ingredients/mapped/Trace_Element_Solution_See_Medium_No_187.yaml` | `NCIT:C896` Trace Element, `LEXICAL_MATCH` | A named trace element solution is not the same entity as the element category. | Keep as complex solution; map to a solution parent only with non-identity predicate or keep unmapped with composition note. | Medium |
| `data/ingredients/mapped/Yeast_Extract-malt_Extract_Agar.yaml` | `FOODON:03301056` malt extract, `LEXICAL_MATCH` | The ingredient combines yeast extract, malt extract, and agar; mapping to malt extract alone loses composition. | Reclassify as complex mixture or named medium component; do not exact-map to malt extract. | High |

### Duplicate Or Variant Groups Needing Review

The following ontology IDs are used by multiple mapped files. Some are valid
variant records, but several collapse hydrate, stock, preparation, brand, or
source differences into the same ontology identifier.

| Ontology ID | Records | Suggested edit | Confidence |
|---|---:|---|---|
| `CHEBI:34683` | 6 | Review `Na2HPO4` hydrate variants. If hydrate-specific ontology terms exist, use them; otherwise use non-identity mappings for hydrate variants. | High |
| `FOODON:03301056` | 6 | Split malt extract, malt extract agar, malt extract broth, and yeast extract-malt extract agar semantics. Only plain malt extract should retain identity mapping. | High |
| `MICRO:0000460` | 6 | Vitamin solution variants should not all be identity-equivalent to a generic vitamin solution. Preserve named formulations as complex mixtures or narrow/close mappings. | Medium |
| `ENVO:00002149` | 5 | Sea water variants such as pasteurized/supplemented/natural seawater should not be exact identity unless the preparation distinction is intentionally ignored. | Medium |
| `NCIT:C29321` | 5 | Phosphate buffer stock and sodium/potassium phosphate buffer variants need parent/child semantics, not blanket identity. | High |
| `CHEBI:31206` | 3 | `Tetramethyl ammonium chloride` should be removed from the ammonium chloride group. | High |
| `CHEBI:26714` | 3 | Butyrate/lactate/propionate sodium salts should not all map to generic sodium salt. | High |

### Low Confidence / Non-Exact Mapping Surface

`mappings/ingredient_mappings.sssom.tsv` contains:

- 1,666 `skos:exactMatch` rows
- 337 `skos:closeMatch` rows
- 176 `skos:narrowMatch` rows

The non-exact mappings are expected in this repo, but the high count means
consumers must honor `MAPPING_SEMANTICS.md`. Any `narrowMatch` subject should
retain a kg-microbe registry/identity row, and close/narrow rows must not be
collapsed as identity.

## Unmapped Ingredients With Suggested Mappings

The highest-confidence unmapped suggestions are cases where a local mapped
record or SSSOM row already exists. These can be resolved without external
search.

| Unmapped record | Local evidence | Suggested edit | Confidence |
|---|---|---|---|
| `data/ingredients/unmapped/Nacl.yaml` (`UNMAPPED_0015`, NaCl) | Exact local mapped record `data/ingredients/mapped/Nacl.yaml` -> `CHEBI:26710`; matching CAS `7647-14-5`; SSSOM exact row exists. | Merge into mapped NaCl or mark as duplicate represented by `CHEBI:26710`. | High |
| `data/ingredients/unmapped/Nh4cl.yaml` (`UNMAPPED_0034`, NH4Cl) | Exact local mapped record `data/ingredients/mapped/Nh4cl.yaml` -> `CHEBI:31206`; matching CAS `12125-02-9`; SSSOM exact row exists. | Merge into mapped NH4Cl or mark duplicate. | High |
| `data/ingredients/unmapped/Kcl.yaml` (`UNMAPPED_0020`, KCl) | Exact local mapped record `data/ingredients/mapped/Kcl.yaml` -> `CHEBI:32588`; matching CAS `7447-40-7`; SSSOM exact row exists. | Merge into mapped KCl or mark duplicate. | High |
| `data/ingredients/unmapped/Na2edta2h2o.yaml` (`UNMAPPED_0040`, Na2EDTA.2H2O) | Exact local mapped record `data/ingredients/mapped/Na2edta2h2o.yaml` -> `CHEBI:64758`; SSSOM exact row exists. | Merge into mapped EDTA disodium salt dihydrate. | High |
| `data/ingredients/unmapped/Mgso47h2o.yaml` (`UNMAPPED_0003`, MgSO4.7H2O) | Local mapped hydrate/formula variants exist under `CHEBI:32599` and `CHEBI:31795`. | Review hydrate identity first; likely merge into the correct magnesium sulfate heptahydrate record rather than generic magnesium sulfate. | Medium |
| `data/ingredients/unmapped/Cacl22h2o.yaml` (`UNMAPPED_0007`, CaCl2.2H2O) | Local mapped `CHEBI:86158` records exist. The unmapped CAS is `10043-52-4`, which appears to be the anhydrous calcium chloride CAS in local records, so CAS needs review. | Merge to calcium chloride dihydrate after fixing/verifying CAS, or preserve as anhydrous if the source CAS is authoritative. | Medium |
| `data/ingredients/unmapped/Na2sio39h2o.yaml` (`UNMAPPED_0016`, Na2SiO3.9H2O) | Local mapped `data/ingredients/mapped/Na2sio3_X_9_H2o.yaml` -> `CHEBI:132108`; matching local CAS evidence. | Merge into mapped sodium metasilicate nonahydrate. | High |
| `data/ingredients/unmapped/Caso42h2o.yaml` (`UNMAPPED_0048`, CaSO4.2H2O) | Local mapped `data/ingredients/mapped/Caso4_X_2_H2o.yaml` -> `CHEBI:32583`. | Merge into mapped calcium sulfate dihydrate after validating identifier. | Medium |
| `data/ingredients/unmapped/FeSO4_7H2O.yaml` | Local mapped `data/ingredients/mapped/Feso4_X_7_H2o.yaml` -> `CHEBI:75836`. | Merge into mapped ferrous sulfate heptahydrate if hydrate and oxidation state agree. | Medium |
| `data/ingredients/unmapped/Hepes_Buffer.yaml` (`UNMAPPED_0057`, HEPES buffer) | Local mapped `data/ingredients/mapped/Hepes.yaml` -> `CHEBI:46756`; matching CAS `7365-45-9`. | Map/merge to HEPES, with "buffer" kept as raw synonym or role/solution context. | High |
| `data/ingredients/unmapped/Tes_Buffer.yaml` (`UNMAPPED_0080`, TES buffer) | CAS match to local mapped `data/ingredients/mapped/Tes.yaml` -> `CHEBI:39035`. | Map/merge to TES after confirming CAS. | High |
| `data/ingredients/unmapped/Trizma_Base_Ph.yaml` (`UNMAPPED_0090`, Trizma Base pH) | Local mapped `data/ingredients/mapped/Tris_Base.yaml` -> `CHEBI:9754`. | Normalize "Trizma Base pH" to Tris base; keep pH as preparation note rather than identity text. | Medium |

Additional exact local/SSSOM duplicate candidates found:

- `(E)-4-Aminostyryl acetate` -> local `kgmicrobe.compound:e_4_aminostyryl_acetate`
- `atrop-abyssomicin C` -> local `kgmicrobe.compound:atrop_abyssomicin_c`
- `bacteriocin ISK-1` -> local `kgmicrobe.compound:bacteriocin_isk_1`
- `O-carbamyl-D-serine` -> local `kgmicrobe.compound:o_carbamyl_d_serine`
- `trans-styrylacetic acid` -> local `kgmicrobe.compound:trans_styrylacetic_acid`

## Normalization And Synonym Edits

Suggested normalization edits:

- Normalize hydrate notation across mapped and unmapped files:
  - `MgSO4.7H2O`, `MgSO4 x 7 H2O`, `MgSO4*7H2O`, and source bullet variants should
    point to one representative record.
  - Same for `CaCl2.2H2O`, `Na2EDTA.2H2O`, `Na2HPO4.7H2O`,
    `Na2SiO3.9H2O`, and `CaSO4.2H2O`.
- Keep supplier/catalog notes such as Fisher, Sigma, Difco, and Oxoid in raw
  synonym or provenance fields, not in preferred terms.
- Move `Role: ...; Properties: ...` pseudo-synonyms into role/property fields
  where possible. A quick scan found roughly 400 mapped records with role,
  merge, or instruction-like raw synonyms.
- Treat "stock", "solution", "medium", "agar", "broth", "pasteurized",
  "supplemented", "autoclaved", and named formulation qualifiers as preparation
  or mixture context unless the ontology term is equally specific.

## Entries That Should Remain Unmapped

These categories should generally remain unmapped to simple CHEBI/FOODON terms
unless a composition-specific local entity is minted or a true named medium term
exists.

| Category | Examples | Reason |
|---|---|---|
| Placeholders | `See source for composition`, `Full composition available at source database` | Not ingredients; pointers to external composition. |
| Named media | `BG-11 Medium`, `F/2 Medium`, `Erdschreiber's Medium`, `Modified COMBO Medium` | Full recipes or named media, not single ingredients. |
| Stock/trace solutions | `P-IV Metal Solution`, `Trace Metals Solution`, `Hunter's Trace Stock Solution` | Defined mixtures; map constituents if composition is available. |
| Environmental preparations | `Soilwater: GR+ Medium`, `Soil+Seawater Medium`, `Supplemented Seawater` | Mixture/preparation context; generic parent ENVO identity would lose specificity. |
| Commercial complex mixtures | `Difco Marine Broth`, `Trypticase Soy Agar`, `Fastidious Anaerobe Broth` | Product/formulation, not a single ontology material. |

## Proposed Next Edits

1. Resolve the high-confidence unmapped duplicates listed above by merging or
   marking represented-by links to existing mapped records.
2. Manually repair the high-confidence mapped errors:
   `Tetramethyl_Ammonium_Chloride`, `P-Amino_Benzoic_Acid`, and the three
   `CHEBI:26714` sodium-salt records.
3. Re-run or regenerate aggregate files from individual records with
   `scripts/aggregate_records.py` after curatorial edits.
4. Re-run SSSOM validation after mapping changes, especially for any new
   `skos:narrowMatch` rows to ensure the required registry rows exist.

## Validation Results

Commands run:

- `just validate-all`: failed with 185 schema errors and 2,338 warnings across
  2,349 checked files. Ontology format checks reported 1,999 valid terms. The
  first failures were in existing collection/category files:
  `data/curated/mapped_ingredients.yaml`,
  `data/ingredients/unmapped/complex_mixture.yaml`,
  `data/ingredients/unmapped/placeholder.yaml`, and
  `data/ingredients/unmapped/simple_chemical.yaml`.
- `just test`: failed before collection because this environment lacks the
  pytest coverage plugin required by `pyproject.toml` addopts
  (`--cov=mediaingredientmech`, `--cov-report=...`).
- `PYTHONPATH=src pytest -o addopts='' tests/`: ran the suite without the
  missing coverage addopts. Result: 219 passed, 28 failed, 1 warning. Failures
  are in existing fixture/schema expectations, merge API expectations, and
  purity-aware merge blocking tests.

No validation failures are caused by this markdown report.
