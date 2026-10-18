# `data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml`

## Verdict

Needs curation, major. The CAS fallback, hydrate structure, registry SSSOM row,
and aggregate copy pass, but the close-match ontology row points at the neutral
`CHEBI:17270` glycerol 2-phosphate parent even though the more specific
anhydrous disodium salt parent `CHEBI:132089` is available locally.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml`.
- Current identity: `identifier: cas:154804-51-0` and `chemical_properties.cas_rn:
  154804-51-0`, with an exact registry SSSOM row preserving that CAS primary
  identifier.
- Current ontology anchor: `ontology_mapping.ontology_id: CHEBI:17270`,
  `ontology_label: glycerol 2-phosphate`, `ontology_source: CHEBI`,
  `mapping_quality: CLOSE_MATCH`, and `mapping_status: MAPPED`.
- PubChem resolves CAS `154804-51-0` to PubChem CID 44828775 and the same
  disodium monohydrate formula, InChI, and SMILES stored under
  `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Beta-D-xylose.yaml data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Beta-Lapachone.yaml data/ingredients/mapped/Beta-Lipomycin.yaml data/ingredients/mapped/Beta-alanine.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Beta-D-xylose.yaml data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Beta-Lapachone.yaml data/ingredients/mapped/Beta-Lipomycin.yaml data/ingredients/mapped/Beta-alanine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all five records.
- The previous full-corpus `uv run --frozen python scripts/validate_sssom_invariants.py`
  run passed Rules A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was
  skipped because the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `src`, `scripts`, and
  `reports`, excluding `data/curated/backups` and this review directory, found
  the authoritative close-match SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 574, the CAS registry row at row
  575, and the aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The same exhaustive search found
  `data/ingredients/mapped/Sodium_Beta-glycerophosphate.yaml`, which is already
  exactly grounded to `CHEBI:132089` `sodium glycerol 2-phosphate` and carries
  `Disodium beta-glycerophosphate` and `Disodium glycerol 2-phosphate` as
  synonyms.
- OLS search for `glycerol 2-phosphate` also returns `CHEBI:132089`, confirming
  the disodium salt parent exists.
- `mappings/hydrate_review.tsv` row 112 correctly retained a distinct MIM/CAS
  identity because the supplied form is a hydrate with unspecified stoichiometry,
  but that review did not account for the now-curated anhydrous disodium parent.

## Completeness

- The CAS primary identifier, CAS registry SSSOM row, formula, InChI, SMILES,
  exact CAS, exact PubChem CID, and aggregate copy are populated.
- Major gap: the close-match CHEBI row preserves a relationship to glycerol
  2-phosphate, but not to the closest available salt form. A future repair
  should keep the CAS registry identity and update only the informational CHEBI
  close match.

## Recommended Edits

- Major: update
  `data/ingredients/mapped/Beta-Glycerophosphate_Disodium_Salt_Hydrate.yaml` so
  its close-match `ontology_mapping` targets `CHEBI:132089` `sodium glycerol
  2-phosphate`, then run `just sync-curated` and
  `uv run --frozen python scripts/validate_sssom_invariants.py`.
