# `data/ingredients/mapped/Amino_Acid.yaml`

## Verdict

Pass. The record is a legitimate class-to-class MicrobeDecoder mapping from the
generic `Amino Acid` trait to `CHEBI:33709`, with a review-ingredients approval,
source occurrence, SSSOM row, and matching aggregate copy.

## Identity

- Reviewed record: `data/ingredients/mapped/Amino_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:33709` with
  `ontology_mapping.ontology_id: CHEBI:33709`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:33709` to the class
  `amino acid`.
- This is intentionally a generic chemical class rather than one concrete
  structure, so the record correctly has no `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Aluminum_Chloride_Hydrate.yaml data/ingredients/mapped/Amicoumacin_B.yaml data/ingredients/mapped/Amikacin.yaml data/ingredients/mapped/Amikacin_Disulfate_Salt.yaml data/ingredients/mapped/Amino_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amino_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned canonical `amino acid` and `amino acids` as a related synonym for
  `CHEBI:33709`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:216618 CHEBI:2637 CHEBI:2638 CHEBI:33709`:
  returned the `CHEBI:33709` amino-acid class label and definition with no
  structure metadata, as expected for the class.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:amino_acid` in `BacDive_Metabolite_utilization` with count
  `1`, matching `source_occurrences`.
- `mappings/microbedecoder_auto_mapped_review.tsv` approved
  `Amino_Acid.yaml` after `CHEBI:33709` resolved locally with canonical label
  `amino acid`.
- `mappings/ingredient_mappings.sssom.tsv` row 392 maps `MIM:Amino_Acid` to
  `CHEBI:33709` with `skos:exactMatch` and the expected review-ingredients
  `APPROVED` trailer.
- `scripts/partition_class_term_cohort.py` explicitly lists
  `Amino Acid` to `amino acid` as a legitimate class-to-class mapping, so this
  broad term is not one of the wrong-sense class matches the MicrobeDecoder
  review warning was designed to catch.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, SSSOM row, MicrobeDecoder raw occurrence, review row,
  and local tests/scripts that use `CHEBI:33709` as the amino-acid class.

## Completeness

- Source occurrence, mapping evidence, and curation history are populated.
- No CAS, structure, synonym, role, component, environmental context,
  discussion, or dataset entry is needed for the generic class.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:33709` row, which
  is consistent with `occurrence_statistics.total_occurrences: 0` because the
  record is sourced from MicrobeDecoder rather than CultureMech.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
