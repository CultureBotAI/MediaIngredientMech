# `data/ingredients/mapped/Anisodamine_Hydrobromide.yaml`

## Verdict

Needs curation. The NCIT lookup now resolves to an Anisodamine Hydrobromide term,
but the active CAS `17659-49-3`, stored PubChem CID `6918612`, and stored
formula/structure describe base anisodamine rather than the hydrobromide salt;
the imported preferred label also retains a stray empty parenthetical.

## Identity

- Reviewed record: `data/ingredients/mapped/Anisodamine_Hydrobromide.yaml`.
- Active local identity: `identifier: cas:17659-49-3`, preferred term
  `Anisodamine Hydrobromide ()`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `ontology_mapping` targets `NCIT:C221850` with label
  `Anisodamine Hydrobromide`, source `NCIT`, and
  `mapping_quality: NARROW_MATCH`.
- EBI OLS resolves `NCIT:C221850` as non-obsolete NCIT
  `Anisodamine Hydrobromide` with exact synonyms and NCIT CAS annotation
  `55449-49-5`.
- PubChem resolves the record CAS `17659-49-3` to CID `2198`; PubChem CID
  `2198` and the stored `pubchem_cid: 6918612` both report base-anisodamine
  formulas without bromide.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Anisodamine_Hydrobromide.yaml data/ingredients/mapped/Anthracene.yaml data/ingredients/mapped/Anthracycline_Antibiotic.yaml data/ingredients/mapped/Anthranilamide.yaml data/ingredients/mapped/Anthranilic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anisodamine_Hydrobromide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings.sssom.tsv` rows 430-432 export the NCIT
  `skos:narrowMatch`, the exact CAS registry row, and the exact kg-microbe
  registry row for `MIM:Anisodamine_Hydrobromide`.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` resolves
  `NCIT:C221850` exactly, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` classifies the
  legacy NCIT/CAS/kg-microbe unknown-term rows as expected registry or missing
  prefix-validator coverage.
- PubChem PUG lookups confirmed two incompatible pieces of the active record:
  CAS `17659-49-3` resolves to PubChem CID `2198`, while the stored CID
  `6918612` resolves to title `Anisodamine`; both CIDs have formula
  `C17H23NO4`, so the stored chemistry has no hydrobromide component.
- A hidden, ignored-inclusive search across `data`, `src`, `tests`,
  `mappings`, and `scripts` found the active YAML, aggregate copy, SSSOM
  rows, row-review rows, and historical ignored aggregate backups; it found no
  second active curated record for `17659-49-3`, `6918612`, or `NCIT:C221850`.

## Completeness

- The curated aggregate contains the same label, NCIT mapping, CAS, PubChem CID,
  and base-anisodamine formula as the per-record YAML.
- Source occurrence counts are intentionally zero because this is a CultureBotHT
  CAS fallback rather than a media recipe ingredient.
- No component, role, environmental context, discussion, or dataset entry is
  needed once the chemical form is made internally consistent.

## Recommended Edits

- In `data/ingredients/mapped/Anisodamine_Hydrobromide.yaml`, decide whether the
  maintained record is hydrobromide or base anisodamine. If hydrobromide,
  replace CAS `17659-49-3` and the base PubChem chemistry with a
  hydrobromide-specific identifier and formula, remove the empty `()` label
  artifact, and regrade the NCIT row if it is exact. If base anisodamine, rename
  the record and remove the hydrobromide NCIT grounding.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Anisodamine_Hydrobromide.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
