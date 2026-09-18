# `data/ingredients/mapped/Fe4_Po42.yaml`

## Verdict

Needs curation, with a major identity issue. The active ChEBI ferric
pyrophosphate term and CAS-backed structure are internally consistent, but the
MIM subject label `Fe4(PO4)2` is not a synonym or formula for ferric
pyrophosphate.

## Identity

- Reviewed record: `data/ingredients/mapped/Fe4_Po42.yaml`.
- Identifier and grounding: `identifier: CHEBI:132767` with matching
  `ontology_mapping.ontology_id`, canonical label `ferric pyrophosphate`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `10058-44-3` resolved to CID 24877 with formula
  `Fe4O21P6` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml --out /tmp/mim_fe_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the CHEBI-primary subset in this mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms, merge
  history, and refreshed occurrence counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fe4_Po42` to `CHEBI:132767` with `skos:exactMatch`; the exported
  `other` tokens are ferric pyrophosphate synonyms and the CAS RN.
- Major: `CHEBI:132767` and CAS `10058-44-3` denote ferric pyrophosphate with
  formula `Fe4O21P6`, while the source label `Fe4(PO4)2` is not that formula.
  A fresh exact OLS4 search for the literal source label against CHEBI and NCIT
  returned no documents.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fe4_Po42`,
  `CHEBI:132767`, and `10058-44-3` found the active YAML, aggregate copy,
  final SSSOM row, row-review provenance, CultureMech recipe memberships, and
  ignored aggregate backups.

## Completeness

- The ferric pyrophosphate CAS RN, structure fields, exact synonyms,
  occurrence counts, and final SSSOM payload are populated.
- The source-label-to-term identity must be rechecked because the displayed
  formula is inconsistent with the mapped ChEBI identity.

## Recommended Edits

- Major: review the 10 CultureMech source occurrences to determine whether
  `Fe4(PO4)2` is a source typo for ferric pyrophosphate or a distinct unmapped
  iron phosphate label.
- Major: once the source label is resolved, either rename this row to ferric
  pyrophosphate and preserve source typo provenance outside exact synonyms, or
  move the `Fe4(PO4)2` occurrences to a local corrected identity. Sync
  `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
