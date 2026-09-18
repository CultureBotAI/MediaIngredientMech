# `data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml`

## Verdict

Needs curation, major. The hydrate-specific CAS registry identity, broader
`CHEBI:232796` close match, SSSOM rows, and aggregate copy agree, but several
`chemical_properties` fields still describe anhydrous cadmium acetate rather
than cadmium acetate dihydrate.

## Identity

- Reviewed record: `data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml`.
- Identifier and grounding: `identifier: cas:5743-04-4`,
  `ontology_mapping.ontology_id: CHEBI:232796`,
  `ontology_label: cadmium acetate`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:232796` returns the active broader label
  `cadmium acetate`; no exact ChEBI term is asserted for the dihydrate.
- PubChem resolves CAS `5743-04-4` to cadmium acetate dihydrate as CID 6537495,
  with formula `C4H10CdO6` and structure strings that include two waters.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cacl2_X_7_H2o.yaml data/ingredients/mapped/Caco3.yaml data/ingredients/mapped/Cadaverine.yaml data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml data/ingredients/mapped/Cadmium_Chloride_Hemipentahydrate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.GkFQqh`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.GkFQqh`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `docs/data`, and `reports`, excluding bulky backups and generated
  review-report directories, found the `CAS_MISSING_ANCHOR_ROWS` hydrate
  grounding row, the hydrate-review row that treats `cas:5743-04-4` as the
  specific identity, the expected-registry unknown-term triage row, the parent
  close-match SSSOM row, and the required CAS registry exact-match SSSOM row.
- The two SSSOM rows are directionally correct: `MIM:Cadmium_Acetate_Dihydrate`
  uses `skos:closeMatch` to broader `CHEBI:232796` and `skos:exactMatch` to
  its own `cas:5743-04-4` registry identity.
- Major gap: `chemical_properties.pubchem_cid` is still `10986`, the CID
  referenced when the broader anhydrous parent was found; CAS `5743-04-4`
  resolves to PubChem CID 6537495 instead.
- Major gap: `chemical_properties.molecular_formula` was patched to
  `C4H6CdO4.2H2O`, but the local InChI and SMILES remain the anhydrous
  cadmium acetate values and do not include the two waters returned by the
  hydrate CAS lookup.

## Completeness

- The CAS primary identifier, broader ChEBI close match, registry identity
  SSSOM row, one occurrence, and aggregate copy are populated.
- The structure bundle is incomplete until the CID, formula, InChI, and SMILES
  are all derived from the same hydrate-specific PubChem record or until
  unverifiable structure slots are removed.

## Recommended Edits

- Major: update `chemical_properties` in
  `data/ingredients/mapped/Cadmium_Acetate_Dihydrate.yaml` so `pubchem_cid`,
  `molecular_formula`, `inchi`, and `smiles` consistently describe CAS
  `5743-04-4` / PubChem CID 6537495, or clear the derived structure fields if
  the curation standard does not accept that PubChem compound; then run
  `just sync-curated` and focused strict/SSSOM validation.
