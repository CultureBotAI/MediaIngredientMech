# `data/ingredients/mapped/Angustmycin.yaml`

## Verdict

Needs curation. The synonym-match grounding to `CHEBI:8612` psicofuranin,
chemistry, absorbed MicrobeDecoder source, row-review disposition, SSSOM row,
and aggregate copy pass, but the record stores a KGX/source statement as a raw
synonym and carries an unsupported provisional `SELECTIVE_AGENT` role.

## Identity

- Reviewed record: `data/ingredients/mapped/Angustmycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:8612` with
  `ontology_mapping.ontology_id: CHEBI:8612`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:8612` to `psicofuranin`
  with formula `C11H15N5O5`, CAS `1874-54-0`, the stored SMILES and InChI, and
  InChIKey `BNZYRKVSCLSXSJ-IOSLPCCCSA-N`.
- ChEBI lists `psicofuranine` as a related synonym, and curation history records
  that Angustmycin was deliberately held on the psicofuranin chemical identity.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Andrographolide.yaml data/ingredients/mapped/Anethole.yaml data/ingredients/mapped/Angolamycin.yaml data/ingredients/mapped/Angustmycin.yaml data/ingredients/mapped/Anhydrotetracycline_Hydrochloride.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Angustmycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned canonical `psicofuranin` and the related `psicofuranine` alias for
  `CHEBI:8612`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:65408 CHEBI:2716 CHEBI:8612 CHEBI:201752`:
  returned the CAS, formula, SMILES, InChI, InChIKey, average mass, and
  monoisotopic mass for `CHEBI:8612`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `data/custom/microbedecoder/unmapped_labels.tsv` still contains the absorbed
  `kgmicrobe.trait:psicofuranine` source row with count 1 from
  `BacDive_Metabolite_production`.
- `mappings/ingredient_mappings_synonym_enrich_review.tsv` and
  `mappings/ingredient_mappings_row_review_manifest.tsv` mark the historical
  Angustmycin synonym-enrichment proposal as already represented.
- `mappings/ingredient_mappings.sssom.tsv` row 428 maps `MIM:Angustmycin` to
  `CHEBI:8612` with `skos:exactMatch` and the `SYNONYM_ENRICH` trailer.
- `produces: angustmycin` is stored and exported as a `RAW_TEXT` synonym even
  though it is a source statement recovered from SSSOM `other`, not an
  ingredient label.
- The `SELECTIVE_AGENT` role is a computational prediction inferred from a
  curated name-pattern rule, not source-backed role evidence.
- A hidden/ignored-inclusive search over active YAML records, the curated
  aggregate, SSSOM and row-review TSVs, MicrobeDecoder imports, and batch
  review reports found the active YAML, aggregate copy, the absorbed
  `psicofuranine` source row, the SSSOM row, and row-review disposition.

## Completeness

- Formula, SMILES, InChI, curation history, synonym-match grounding, and
  `ingredient_type` are populated.
- No component, environmental context, discussion, or dataset entry is needed.
- The raw `produces:` source statement and unsupported selective-agent role
  remain active gaps.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML, including both gaps.

## Recommended Edits

- In `data/ingredients/mapped/Angustmycin.yaml`, remove or reject
  `produces: angustmycin` so a KGX/source statement is not exported as a
  synonym.
- Replace the provisional `SELECTIVE_AGENT` assignment with source-backed
  evidence, or remove it.
- Regenerate synchronized products, then rerun
  `uv run --frozen python scripts/validate_strict.py`, `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Angustmycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
