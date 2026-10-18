# `data/ingredients/mapped/Amoxicillin.yaml`

## Verdict

Needs curation. The exact `CHEBI:2676` identity, CAS, formula, exact ChEBI
synonym, row-review confirmation, SSSOM row, and aggregate copy pass, but the
active record is missing MicrobeDecoder/BacDive source occurrences and still
carries an unsupported provisional `SELECTIVE_AGENT` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Amoxicillin.yaml`.
- Identifier and grounding: `identifier: CHEBI:2676` with
  `ontology_mapping.ontology_id: CHEBI:2676`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:2676` to
  `amoxicillin` with formula `C16H19N3O5S`, CAS `26787-78-0`, SMILES
  `[H][C@]12SC(C)(C)[C@H](C(=O)O)N1C(=O)[C@H]2NC(=O)[C@H](N)c1ccc(O)cc1`,
  and InChIKey `LSQZJLSUYDQPKJ-NJBDSQKTSA-N`.
- ChEBI contains the YAML's long structural synonym as an exact synonym.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ammonium_Sulfamate.yaml data/ingredients/mapped/Ammonium_Sulfide_Solution.yaml data/ingredients/mapped/Ammonium_Sulfite_Monohydrate.yaml data/ingredients/mapped/Amoxicillin.yaml data/ingredients/mapped/Amphomycin.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amoxicillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:81950 CHEBI:2676 CHEBI:201652`:
  returned canonical `amoxicillin` and the stored exact structural synonym for
  `CHEBI:2676`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:81950 CHEBI:2676 CHEBI:201652`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:2676`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/ingredient_mappings_oak_ols_review.tsv` confirmed the
  `MIM:Amoxicillin` to `CHEBI:2676` mapping, and
  `mappings/ingredient_mappings_row_review_manifest.tsv` records no action was
  required in that row-review pass.
- `mappings/ingredient_mappings.sssom.tsv` row 410 maps `MIM:Amoxicillin` to
  `CHEBI:2676` with `skos:exactMatch`, CAS `26787-78-0`, the exact ChEBI
  synonym, and the `CONFIRMED` trailer.
- The ignored MicrobeDecoder import row
  `data/custom/microbedecoder/unmapped_labels.tsv` still contains
  `kgmicrobe.trait:amoxicillin` with count 133 from
  `BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity`; the active
  record has no matching `source_occurrences` entry.
- The only role is a `SELECTIVE_AGENT` computational prediction inferred from a
  curated name-pattern rule; no medium or source claim demonstrates that
  amoxicillin was curated as a selective agent in this record.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and hydrate
  review files found the active record, aggregate copy, exact SSSOM row,
  row-review confirmation, and the stale MicrobeDecoder amoxicillin source row.

## Completeness

- CAS, formula, SMILES, InChI, exact structural synonym, curation history, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The missing MicrobeDecoder/BacDive occurrences and unsupported selective-agent
  role remain active gaps.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including the provisional role.

## Recommended Edits

- Integrate or explicitly reject the `kgmicrobe.trait:amoxicillin`
  MicrobeDecoder row from `data/custom/microbedecoder/unmapped_labels.tsv`, and
  update `occurrence_statistics.source_occurrences` if the row remains in
  scope.
- Replace the provisional `SELECTIVE_AGENT` assignment with source-backed
  evidence, or remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amoxicillin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
