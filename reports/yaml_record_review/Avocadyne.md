# `data/ingredients/mapped/Avocadyne.yaml`

## Verdict

Needs curation; severity major. The exact `CHEBI:168507` Avocadyne identity,
formula, InChI, SMILES, IUPAC synonym, SSSOM row, and aggregate copy pass, but
the CAS field still carries non-resolving `34524-38-4` instead of ChEBI's
`24607-05-4` Avocadyne xref.

## Identity

- Reviewed record: `data/ingredients/mapped/Avocadyne.yaml`.
- Identifier and grounding: `identifier: CHEBI:168507` with
  `ontology_mapping.ontology_id: CHEBI:168507`,
  `ontology_label: Avocadyne`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:168507` to non-obsolete `Avocadyne` with CAS xref
  `24607-05-4`, formula `C17H32O3`, and the same InChI and SMILES stored on the
  record.
- PubChem lookup for ChEBI's CAS `24607-05-4` resolves to `Avocadyne` with the
  same formula and InChI.
- PubChem lookup for the local `chemical_properties.cas_rn: 34524-38-4`
  returned no CID.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Avidin.yaml data/ingredients/mapped/Avocadene.yaml data/ingredients/mapped/Avocadyne.yaml data/ingredients/mapped/Avocatin_B.yaml data/ingredients/mapped/Avoparcin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Avocadyne.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed; this confirms the `CHEBI:168507` label but does not check the local
  CAS field.
- OLS4 lookup for `CHEBI:168507` and PubChem lookup for `24607-05-4` confirmed
  the active ChEBI Avocadyne identity and structure.
- PubChem lookup for `34524-38-4` failed to resolve the CAS recorded locally.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.

## Evidence

- Hidden/ignored-inclusive searches over `data/curated`, `mappings`, and
  `data/custom`, excluding `data/curated/backups`, found the authoritative
  SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 503 and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- `mappings/ingredient_mappings_oak_ols_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` already record the
  `CHEBI:168507` mapping itself as confirmed with no curation action.
- The YAML and SSSOM carry the right IUPAC synonym `heptadec-16-yne-1,2,4-triol`.
- The CAS `34524-38-4` came from the original CultureBotHT import, but current
  ChEBI and PubChem agree on `24607-05-4` for Avocadyne.

## Completeness

- The exact identifier, formula, InChI, SMILES, IUPAC synonym, SSSOM row, and
  aggregate copy are populated.
- The CAS is the only consequential chemical-property field that does not
  resolve to the same term.
- The 0/0 occurrence count is correct for a CultureBotHT-only compound not
  present in CultureMech recipe memberships.

## Recommended Edits

- Replace `chemical_properties.cas_rn: 34524-38-4` with `24607-05-4` in
  `data/ingredients/mapped/Avocadyne.yaml`, synchronize the aggregate and SSSOM
  `other` value, regenerate flat exports, and rerun focused strict and term
  validation, product id/label correspondence, SSSOM invariants, and
  flat-export coverage.
