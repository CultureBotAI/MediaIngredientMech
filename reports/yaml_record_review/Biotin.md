# `data/ingredients/mapped/Biotin.yaml`

## Verdict

Needs curation, minor. The exact `CHEBI:15956` biotin identity, CAS, merged
aliases, vitamin role, structure fields, SSSOM row, occurrence count, and
aggregate copy pass, but one auto-proposed PubMed search snippet is attached to
the ontology mapping despite not supporting the grounding.

## Identity

- Reviewed record: `data/ingredients/mapped/Biotin.yaml`.
- Identifier and grounding: `identifier: CHEBI:15956` with
  `ontology_mapping.ontology_id: CHEBI:15956`,
  `ontology_label: biotin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- PubChem resolves CAS `58-85-5` to the same formula and standard InChI stored
  under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biochanin_A_Diacetate.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biotin_Vitamin_Solution.yaml data/ingredients/mapped/Biphenyl.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Bimuno.yaml data/ingredients/mapped/Biotin.yaml data/ingredients/mapped/Biphenyl.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the NCIT/CHEBI records in this batch.
- Engine A term validation is intentionally skipped for the CAS registry record
  and the `kgmicrobe.ingredient` record. The previous full-corpus SSSOM
  validator passed, with Rule B4 skipped because sibling kg-microbe ontology
  transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `data/custom`, and `reports`, excluding `data/curated/backups` and generated
  review directories, found the authoritative exact SSSOM row at
  `mappings/ingredient_mappings.sssom.tsv` row 597, the already-represented
  synonym review in `mappings/ingredient_mappings_row_review_manifest.tsv`, and
  the aggregate copy in `data/curated/mapped_ingredients.yaml`.
- The merged synonyms preserve source aliases and exact kg-microbe aliases for
  biotin, while the concentration-qualified `Biotin (1 ug/uL)` source form is
  retained only as raw CultureMech text.
- A parsed comparison against `data/curated/mapped_ingredients.yaml` found
  exactly one aggregate record with the same identifier and preferred term, and
  it is identical to this per-record YAML.

## Completeness

- The exact CHEBI identifier, CAS RN, single-ingredient classification,
  formula, InChI, SMILES, vitamin role, SSSOM row, occurrence statistics, and
  aggregate copy are populated.
- Minor gap: the `pmid: 39201737` PubMed search evidence says only that
  pharmacological concentrations of biotin have therapeutic effects on
  metabolic syndrome. It does not support the identity mapping to `CHEBI:15956`
  and should not live under `ontology_mapping.evidence`.

## Recommended Edits

- Minor: remove the `pmid: 39201737` PubMed search entry from
  `data/ingredients/mapped/Biotin.yaml`, or move it to a claim it actually
  supports if a curator finds one; then run `just sync-curated` and focused
  strict/term validation.
