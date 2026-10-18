# `data/ingredients/mapped/Acetylene.yaml`

## Verdict

Pass. The exact `CHEBI:27518` identity, MicrobeDecoder source occurrence,
ChEBI chemistry, aggregate copy, and SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetylene.yaml`.
- Identifier and grounding: `identifier: CHEBI:27518` with
  `ontology_mapping.ontology_id: CHEBI:27518`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:27518` to `acetylene`
  with formula `C2H2`, SMILES `C#C`, InChI
  `InChI=1S/C2H2/c1-2/h1-2H`, InChIKey `HSFWRNGVRCDJHI-UHFFFAOYSA-N`, and CAS
  `74-86-2`.
- `ingredient_type: SINGLE_INGREDIENT` is present and agrees with the ChEBI
  molecular entity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetylated_Xylan.yaml data/ingredients/mapped/Acetylene.yaml data/ingredients/mapped/Achromoviromycin.yaml data/ingredients/mapped/Aconitate.yaml data/ingredients/mapped/Acridine_Orange.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Acetylene.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned the expected ChEBI labels and synonyms for all four ChEBI terms in
  the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned formula and structure metadata for `CHEBI:27518`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings elsewhere in the corpus.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` contains
  `kgmicrobe.trait:acetylene` in `BacDive_Metabolite_utilization` with count
  `4`, matching `source_occurrences`.
- The official ChEBI page and local OAK metadata support the stored formula,
  SMILES, InChI, and molecular weight.
- `mappings/microbedecoder_auto_mapped_review.tsv` records the
  review-ingredients approval that promoted this exact ChEBI label match from
  `PENDING_REVIEW` to `MAPPED`.
- `mappings/ingredient_mappings.sssom.tsv` row 327 maps `MIM:Acetylene` to
  `CHEBI:27518` with `skos:exactMatch` and the manual approval trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, MicrobeDecoder raw occurrence, review TSV row, generated
  indexes, and ignored aggregate backups.

## Completeness

- Formula, SMILES, InChI, molecular weight, source occurrence, curation history,
  and `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
