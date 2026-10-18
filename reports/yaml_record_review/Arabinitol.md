# `data/ingredients/mapped/Arabinitol.yaml`

## Verdict

Pass. The record exactly denotes generic ChEBI `arabinitol`, preserves the raw
MicrobeDecoder occurrence that introduced it, and the ChEBI formula, SSSOM row,
and aggregate copy are synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/Arabinitol.yaml`.
- Identifier and grounding: `identifier: CHEBI:22605` with
  `ontology_mapping.ontology_id: CHEBI:22605`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:22605` to non-obsolete ChEBI `arabinitol`, formula
  `C5H12O5`, and mass `152.146`.
- The adjacent `data/ingredients/mapped/Arabitol.yaml` record is not an active
  duplicate: it denotes `CHEBI:18403` `L-arabinitol` and preserves
  stereospecific `L-Arabinitol`/`L-Arabitol` synonyms separately from this
  generic arabinitol import.
- `ingredient_type: SINGLE_INGREDIENT` is present and fits the ChEBI molecular
  entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Apramycin.yaml data/ingredients/mapped/Apramycin_Sulfate_Salt.yaml data/ingredients/mapped/Arabinan_From_Sugar_Beet.yaml data/ingredients/mapped/Arabinitol.yaml data/ingredients/mapped/Arabinobiose.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Arabinitol.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:2790 CHEBI:190734 CHEBI:22605`:
  returned formula and mass metadata for `CHEBI:22605`.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:2790 CHEBI:190734 CHEBI:22605`:
  returned the canonical `arabinitol` label and related `arabitol` synonym for
  `CHEBI:22605`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:arabinitol` with raw label `arabinitol`, source column
  `BacDive_Metabolite_utilization`, and count 11, matching the record
  `source_occurrences` entry.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved the
  `Arabinitol.yaml` import against `CHEBI:22605`; the record history preserves
  the PENDING_REVIEW hold and later `review-ingredients` promotion.
- `mappings/ingredient_mappings.sssom.tsv` row 456 maps `MIM:Arabinitol` to
  `CHEBI:22605` with `skos:exactMatch`, `manual:review-ingredients`, and
  `APPROVED`.
- A hidden, ignored-inclusive search across the full checkout, excluding the
  old `data/curated/backups` snapshots and noncanonical batch-review output,
  found the active YAML, aggregate copy, SSSOM row, MicrobeDecoder review row,
  raw ignored MicrobeDecoder source row, and the separate `Arabitol` sibling.

## Completeness

- Formula, ChEBI identity, non-media source occurrence, curation history,
  `ingredient_type`, SSSOM, and the aggregate copy are populated.
- SMILES and InChI are absent because the ChEBI `arabinitol` entry does not
  expose a structure in the local OBO metadata.
- No role, component, environmental context, discussion, or dataset entry is
  needed for this ChEBI single-ingredient import.

## Recommended Edits

- None.
