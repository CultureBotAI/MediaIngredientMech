# `data/ingredients/mapped/Coenzyme_A.yaml`

## Verdict

Needs curation; major. The record is grounded to active `CHEBI:15346` coenzyme
A, the CAS RN, formula, InChI, SMILES, 10/10 CultureMech occurrence count,
final SSSOM row, and aggregate copy agree, and the exported `other` values are
real synonyms plus `CAS:85-61-0`. The material gap is that `COFACTOR_PROVIDER`
is supported solely by a provisional in-session LLM role assignment.

## Identity

- Reviewed record: `data/ingredients/mapped/Coenzyme_A.yaml`.
- Identifier and grounding: `identifier: CHEBI:15346`,
  `ontology_mapping.ontology_id: CHEBI:15346`, `ontology_label: coenzyme A`,
  `ontology_source: CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, `kg_microbe_node_id: CHEBI:15346`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Live OLS lookup by `CHEBI:15346` returns active `CHEBI:15346` labelled
  `coenzyme A` and includes the record's exported exact synonyms, including
  `CoA-SH`, `CoASH`, `HSCoA`, `Coenzym A`, `Koenzym A`, and the two IUPAC-like
  names.
- The record stores CAS RN `85-61-0`, formula `C21H36N7O16P3S`, and populated
  InChI and SMILES values for the exact coenzyme A identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml data/ingredients/mapped/Colistin_Sulfate.yaml data/ingredients/mapped/Colistin_Sulfate_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cocl2_X_6_H2o.yaml data/ingredients/mapped/Coenzyme_A.yaml data/ingredients/mapped/Colchiceine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-identified records in this batch.
  `Colistin_Sulfate` and `Colistin_Sulfate_Salt` were intentionally skipped
  because they are grounded to NCIT, while this LinkML term-validation pass was
  limited to CHEBI records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed before this read-only report batch; both curated collection files had
  0 data differences and only the expected scratch `generation_date` metadata
  differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K before this read-only report
  batch. Rule B4 was skipped because the sibling kg-microbe ontology transforms
  were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found exactly the expected active `MIM:Coenzyme_A` final SSSOM row,
  the row-review `SYNONYM_ENRICH` note for the filtered sodium-salt raw text,
  and matching generated docs rows.
- Hidden/ignored-inclusive search under `data/ingredients` found no second
  active record using `CHEBI:15346`.
- Hidden/ignored-inclusive search of
  `mappings/culturemech_recipe_membership.tsv` found 10 rows for `CHEBI:15346`
  whose occurrence weights sum to 10, matching the explicit 10/10
  `occurrence_statistics`.
- The final SSSOM `other` column contains ChEBI exact synonyms and
  `CAS:85-61-0`. The raw `(sodium salt)` token is filtered from final SSSOM and
  search output.
- `COFACTOR_PROVIDER` has only `COMPUTATIONAL_PREDICTION` evidence from
  `claude_in_session_curation` and is explicitly marked "Provisional
  in-session LLM role assignment; review recommended."

## Completeness

- The ChEBI identifier, CAS RN, formula, InChI, SMILES, SSSOM row, aggregate
  copy, docs row, and occurrence count are populated and agree.
- The only consequential gap is the unsupported provisional role.

## Recommended Edits

- Major: in `data/ingredients/mapped/Coenzyme_A.yaml`, either replace
  `nutritional_roles.COFACTOR_PROVIDER` with inspected evidence for coenzyme A
  as a cofactor provider in this media scope, or remove the role.
- Regenerate synchronized products and rerun strict validation, SSSOM QC,
  aggregate roundtrip, and `git diff --check`.
