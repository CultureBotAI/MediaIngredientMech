# `data/ingredients/mapped/4-hydroxy-L-proline.yaml`

## Verdict

Pass, none. The `CHEBI:18240` generic 4-hydroxy-L-proline identity,
stereochemically partial structure, occurrence accounting, SSSOM row, and
aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/4-hydroxy-L-proline.yaml`.
- Identifier and grounding: `identifier: CHEBI:18240` with
  `ontology_mapping.ontology_id: CHEBI:18240`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:18240` is active, resolves to
  `4-hydroxy-L-proline`, defines the L stereoisomer of 4-hydroxyproline, has
  formula `C5H9NO3`, CAS `51-35-4`, and stores the same C-4-unspecified InChI
  and SMILES as the record.
- Official OLS/ChEBI check of the adjacent `CHEBI:18095` shows the separate
  term is the fully specified `trans-4-hydroxy-L-proline`; that narrower
  identity is curated in the separate `Hydroxy-l-proline.yaml` record, not
  conflated here.
- PubChem lookup by `4-hydroxy-L-proline` returns generic, trans, and
  stereochemistry-unspecified CIDs; CID `69248` carries the same partially
  specified InChI as `CHEBI:18240`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-coumarate.yaml data/ingredients/mapped/4-dihydroxy-biphenyl.yaml data/ingredients/mapped/4-guanidinobutyric_Acid.yaml data/ingredients/mapped/4-hydroxy-L-proline.yaml data/ingredients/mapped/4-hydroxybenzoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-hydroxy-L-proline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2,951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, K; Rule B4 was skipped because the
  sibling `kg-microbe` ontology transforms are absent.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed;
  `docs/data/` is fresh and every curated label is published.

## Evidence

- The microbedecoder import supplied exact raw label `4-hydroxy-L-proline` in
  `BacDive_Metabolite_utilization` with count 94.
- The exact ChEBI term is active and intentionally leaves the 4-hydroxy
  stereocenter unspecified; the stored SMILES and InChI preserve that same
  `t3?,4-` boundary instead of silently narrowing the record to the trans
  isomer.
- CultureMech occurrence membership adds two verified recipe occurrences while
  the raw microbedecoder count stays in `source_occurrences`.
- The SSSOM row maps `MIM:4-hydroxy-L-proline` to `CHEBI:18240` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and no `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, `tests`, `scripts`, `conf`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, microbedecoder source row, generated
  docs, advisory rows, the distinct `Hydroxy-l-proline` record, and ignored
  aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrences, CultureMech
  occurrence counts, and `ingredient_type` are populated.
- No roles, components, environment, or discussion entries need review.
- The CAS `51-35-4` is shared across the generic and trans ChEBI terms, so its
  absence from this record is acceptable; adding it would need source-specific
  care.

## Recommended Edits

No YAML edit is required for this record.
