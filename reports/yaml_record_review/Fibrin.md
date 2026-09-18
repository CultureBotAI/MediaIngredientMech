# `data/ingredients/mapped/Fibrin.yaml`

## Verdict

Needs curation, with a major structure-field issue. The MicrobeDecoder import
uses an exact CHEBI label for fibrin and publishes a clean final SSSOM row, but
the copied structure-derived `chemical_properties` describe the small molecule
`C5H11N3O2`, not fibrin as a protein/polymer substrate.

## Identity

- Reviewed record: `data/ingredients/mapped/Fibrin.yaml`.
- Identifier and grounding: `identifier: CHEBI:5054` with matching
  `ontology_mapping.ontology_id`, label `Fibrin`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- The local ChEBI sqlite adapter carries `CHEBI:5054` with label `Fibrin`, CAS
  xref `9001-31-4`, formula `C5H11N3O2`, SMILES `CNC(=O)CNC(=O)CN`, and the
  same InChI copied into the YAML record.
- PubChem lookup by CAS RN `9001-31-4` also resolved to CID 439199 titled
  `Fibrins` with formula `C5H11N3O2` and the same small-molecule structure, so
  the YAML fields are a faithful copy of a registry structure conflict rather
  than a transcription typo.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Feso4_X_H2o.yaml data/ingredients/mapped/Fetal_Bovine_Serum.yaml data/ingredients/mapped/Fibrin.yaml data/ingredients/mapped/Fidaxomicin.yaml data/ingredients/mapped/Fig.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fibrin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CHEBI identifier, occurrence counts, source occurrence, ingredient type, and
  structure-derived chemical properties as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fibrin` to
  `CHEBI:5054` with `skos:exactMatch` and an empty `other` column.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the row by exact
  local OAK label review and explicitly notes that the shallow review did not
  check homonyms or wrong-sense class matches.
- Major: `chemical_properties.molecular_formula`, `smiles`, `inchi`, and
  `molecular_weight` are structure-derived fields for `C5H11N3O2`; they do not
  describe the fibrin protein/polymer identity named by the record and by the
  BacDive `BacDive_Metabolite_utilization` source occurrence.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, aggregate copy, MicrobeDecoder approval row, occurrence
  membership surfaces, and ignored historical batch reports.

## Completeness

- The exact CHEBI label, MicrobeDecoder source occurrence, ingredient type, and
  final SSSOM identity row are populated.
- No nutritional, physicochemical, component, or environment assertion requires
  evidence in this record.
- The copied ChEBI/PubChem structure fields are the consequential unsupported
  content.

## Recommended Edits

- Major: review `data/ingredients/mapped/Fibrin.yaml` as a protein/polymer
  ingredient and remove the `C5H11N3O2` `chemical_properties` fields unless a
  source can justify them for fibrin; sync
  `data/curated/mapped_ingredients.yaml`, regenerate products if structure
  fields feed them, and rerun strict validation plus the final SSSOM invariant
  gates.
