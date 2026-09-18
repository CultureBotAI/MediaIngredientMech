# `data/ingredients/mapped/Ascomycin.yaml`

## Verdict

Pass. The record exactly denotes ChEBI `ascomycin`, and its MicrobeDecoder
import, ChEBI structure, PubChem structure, SSSOM row, and aggregate copy agree.

## Identity

- Reviewed record: `data/ingredients/mapped/Ascomycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:29582` with
  `ontology_mapping.ontology_id: CHEBI:29582`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- OLS resolves `CHEBI:29582` to non-obsolete ChEBI `ascomycin` with formula
  `C43H69NO12`, molecular weight `792.02`, and the same InChI and isomeric
  SMILES as the record.
- PubChem name lookup for Ascomycin resolves CID `5282071` with formula
  `C43H69NO12` and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` fits the fixed CHEBI structure.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Arsenate.yaml data/ingredients/mapped/Artepaulin.yaml data/ingredients/mapped/Artificial_Sea_Salt.yaml data/ingredients/mapped/Artificial_seawater.yaml data/ingredients/mapped/Ascomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Ascomycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `runoak -i ols:chebi info CHEBI:29125 CHEBI:29582` and
  `runoak -i ols:chebi aliases CHEBI:29125 CHEBI:29582`: unavailable because
  `runoak` is not on PATH in this shell; direct OLS and PubChem `curl` checks
  were used instead.
- OLS4 lookup for `CHEBI:29582`: resolved the current ChEBI label, formula,
  InChI, SMILES, molecular weight, and xrefs.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs corresponded and 104 non-blocking plausibility
  warnings were reported.
- `uv run --frozen python scripts/check_flat_export_coverage.py`: passed; docs
  data were fresh and every curated label was resolvable.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:ascomycin` from `BacDive_Metabolite_production` with one
  occurrence, matching `occurrence_statistics.source_occurrences`.
- `data/custom/microbedecoder/ingredient_candidates.tsv` contains the
  lower-case candidate `ascomycin` with one occurrence in the same source
  column.
- `mappings/microbedecoder_auto_mapped_review.tsv` row 64 records the
  `APPROVED` decision that promoted `Ascomycin.yaml` to `MAPPED`.
- `mappings/ingredient_mappings.sssom.tsv` row 483 maps `MIM:Ascomycin` to
  `CHEBI:29582` with `skos:exactMatch`.

## Completeness

- Formula, molecular weight, SMILES, InChI, ChEBI identity, MicrobeDecoder
  source occurrence, curation history, SSSOM, and the aggregate copy are
  populated.
- No roles, components, environmental context, datasets, or discussion entries
  are needed for this exact small-molecule record.

## Recommended Edits

- None.
