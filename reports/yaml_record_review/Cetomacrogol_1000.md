# `data/ingredients/mapped/Cetomacrogol_1000.yaml`

## Verdict

Needs curation; major issue. The existing CAS primary identifier, MeSH parent
row, registry rows, PubChem structure fields, zero occurrence count, SSSOM row,
and aggregate copy are internally consistent, but the record is still on a
fallback `mesh:D002592` narrow mapping even though ChEBI now has an active exact
`cetomacrogol 1000` term.

## Identity

- Reviewed record: `data/ingredients/mapped/Cetomacrogol_1000.yaml`.
- Current identifier and grounding: `identifier: cas:9004-95-9`,
  `ontology_mapping.ontology_id: mesh:D002592`,
  `ontology_label: Cetomacrogol`, `ontology_source: MESH`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `mesh:D002592` returns one active MeSH term labelled
  `Cetomacrogol`; its synonym list includes `Cetomacrogol 1000`, so the current
  `skos:narrowMatch` parent row is coherent.
- PubChem CID `2724259` returns title `Polyethylene Glycol Cetyl Ether`,
  formula `C56H114O21`, and the same InChI and connectivity SMILES stored in
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cetocycline.yaml data/ingredients/mapped/Cetomacrogol_1000.yaml data/ingredients/mapped/Cetrimonium_Bromide.yaml data/ingredients/mapped/Chalcopyrite.yaml data/ingredients/mapped/Champamycin_B.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cetomacrogol_1000.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed. The same focused validator also passed for `Cetocycline`,
  `Cetrimonium_Bromide`, and `Chalcopyrite`; `Champamycin_B` was skipped
  because its `kgmicrobe.compound` placeholder CURIE is a local registry ID
  outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active `MIM:Cetomacrogol_1000` SSSOM rows: a
  `skos:narrowMatch` to `mesh:D002592`, an exact CAS registry row for
  `cas:9004-95-9`, and an exact local registry row for
  `kgmicrobe.compound:cetomacrogol_1000`.
- The row-review manifest keeps the MeSH, CAS, and kg-microbe rows: the MeSH
  `UNKNOWN_TERM` was missing prefix coverage in an older synonym-review
  dispatcher, while the CAS and kg-microbe rows are expected local registry
  identifiers.
- Current OLS exact searches for `Cetomacrogol 1000` and `Cetomacrogol` in
  ChEBI both resolve `CHEBI:753915` labelled `cetomacrogol 1000`. A
  hidden/ignored-inclusive workspace search found no existing `CHEBI:753915`
  usage, so the curated record and SSSOM are stale.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `mesh:D002592`,
  `cas:9004-95-9`, or `kgmicrobe.compound:cetomacrogol_1000` rows, matching the
  explicit 0/0 `occurrence_statistics`.

## Completeness

- The current fallback parent row, exact registry rows, aggregate copy, docs
  row, PubChem structure, exact synonym, and zero occurrence count are populated
  and agree.
- No role, component, environment, or source occurrence claim needs additional
  evidence.
- The consequential gap is source-preference drift: an exact active ChEBI term
  is now available and should replace the older MeSH parent fallback.

## Recommended Edits

- Major: reground `data/ingredients/mapped/Cetomacrogol_1000.yaml` from
  `mesh:D002592` to `CHEBI:753915` `cetomacrogol 1000`, update
  `ontology_source`, `mapping_quality`, mapping evidence, and curation history
  accordingly, and keep the CAS and kg-microbe identity rows required by Rule
  B1.
- Regenerate synchronized outputs and rerun strict validation, Engine A term
  validation, SSSOM QC, aggregate roundtrip, and `git diff --check`.
