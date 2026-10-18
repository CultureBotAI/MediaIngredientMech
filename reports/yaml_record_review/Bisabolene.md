# `data/ingredients/mapped/Bisabolene.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:49235` generic bisabolene grounding,
SSSOM row, and aggregate copy agree, but `chemical_properties.cas_rn` is
over-specific: PubChem resolves the stored CAS `17627-44-0` to
alpha-Bisabolene, not to the generic ChEBI parent.

## Identity

- Reviewed record: `data/ingredients/mapped/Bisabolene.yaml`.
- Identifier and grounding: `identifier: CHEBI:49235` with
  `ontology_mapping.ontology_id: CHEBI:49235`,
  `ontology_label: bisabolene`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `ingredient_type: SINGLE_INGREDIENT`, and
  `mapping_status: MAPPED`.
- Live OLS search returns `CHEBI:49235` for the `Bisabolene` label and also
  exposes narrower alpha-, beta-, and gamma-bisabolene child terms under the
  same search.
- Live PubChem CAS lookup resolves `17627-44-0` to CID 86597
  `alpha-Bisabolene` with an InChI-bearing `C15H24` structure. The current
  ChEBI parent `CHEBI:49235` has only the generic formula and mass and does not
  expose the alpha-bisabolene structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bis_3-aminopropylamine.yaml data/ingredients/mapped/Bisabolene.yaml data/ingredients/mapped/Bismuth_Iii_Chloride.yaml data/ingredients/mapped/Blasticidin_A.yaml data/ingredients/mapped/Blasticidin_S.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bis_3-aminopropylamine.yaml data/ingredients/mapped/Bisabolene.yaml data/ingredients/mapped/Blasticidin_A.yaml data/ingredients/mapped/Blasticidin_S.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the four CHEBI-backed records in this batch.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the OAK/OLS confirmation row in
  `mappings/ingredient_mappings_row_review_manifest.tsv`, the authoritative
  exact SSSOM row at `mappings/ingredient_mappings.sssom.tsv` row 607, and the
  aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The local SSSOM row maps `MIM:Bisabolene` to generic `CHEBI:49235` with
  `skos:exactMatch`, matching the primary `identifier` and
  `ontology_mapping`.
- Live OLS search for CAS `17627-44-0` found no ChEBI term that cross-references
  that registry number, but PubChem resolves the CAS to a narrower isomer than
  the mapped ChEBI parent.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The generic ChEBI identifier, formula-only ChEBI chemistry, SSSOM row, and
  aggregate copy are populated.
- Major gap: `chemical_properties.cas_rn: 17627-44-0` should not remain on the
  generic bisabolene parent record unless a source verifies that this CAS is
  valid for the parent term rather than only the narrower alpha isomer.

## Recommended Edits

- Major: review the CultureBotHT source for `Bisabolene` and either remove
  `chemical_properties.cas_rn` from `data/ingredients/mapped/Bisabolene.yaml`
  or split/remap the record to the alpha-bisabolene identity if the source
  truly meant CAS `17627-44-0`; then run `just sync-curated`, focused
  strict/term validation, and `just qc-sssom`.
