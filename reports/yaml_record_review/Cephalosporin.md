# `data/ingredients/mapped/Cephalosporin.yaml`

## Verdict

Needs curation; major issue. The MicrobeDecoder class label exactly denotes the
active ChEBI `cephalosporin` class and the SSSOM/aggregate copies are
synchronized, but `chemical_properties.inchi` contains a concrete
`C15H21N3O7S` structure while `CHEBI:23066` is an R-group class with no exact
InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/Cephalosporin.yaml`.
- Identifier and grounding: `identifier: CHEBI:23066`,
  `ontology_mapping.ontology_id: CHEBI:23066`,
  `ontology_label: cephalosporin`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct OLS lookup for `CHEBI:23066` returns one active ChEBI term labelled
  `cephalosporin`, with the generic formula `C7H5NO3SR2`, the generic R-group
  SMILES stored in this record, and no InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml`:
  passed.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Cellulose.yaml data/ingredients/mapped/Cellulose_powder.yaml data/ingredients/mapped/Cephalexin.yaml data/ingredients/mapped/Cephalosporin.yaml data/ingredients/mapped/Cephalothin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed all 5 external-ontology records in this batch.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data/curated`, `mappings`,
  `docs/data`, and `reports`, excluding generated review reports and curated
  backups, found the active exact `MIM:Cephalosporin` SSSOM row, the approved
  `mappings/microbedecoder_auto_mapped_review.tsv` row, and matching
  aggregate/docs rows for `CHEBI:23066`.
- Hidden/ignored-inclusive anchored search of
  `mappings/culturemech_recipe_membership.tsv` found no `CHEBI:23066` rows,
  which matches the explicit 0/0 media `occurrence_statistics`.
- The MicrobeDecoder `source_occurrences` annotation preserves the 17 BacDive
  antibiotic sensitivity/resistance mentions that caused this class-level
  trait to be imported. Those source mentions are not CultureMech recipe
  occurrences.
- The OLS payload for `CHEBI:23066` has formula, SMILES, and mass annotations
  for the cephalosporin class skeleton. It has no exact InChI, and the stored
  InChI has formula `C15H21N3O7S`, not the R-group class formula.

## Completeness

- The ChEBI class identifier, class formula, class SMILES, zero occurrence
  count, source occurrence count, SSSOM row, aggregate copy, and docs row are
  populated and agree.
- The over-specific InChI is the only consequential structure gap; no role,
  component, or environment claim is present.

## Recommended Edits

- Major: remove `chemical_properties.inchi` from the generic cephalosporin
  class record, then rerun strict validation, SSSOM QC, aggregate roundtrip,
  and `git diff --check`.
