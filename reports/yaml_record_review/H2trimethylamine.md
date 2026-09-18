# `data/ingredients/mapped/H2trimethylamine.yaml`

## Verdict

Pass with minor issues. The local fallback identity, two-part decomposition,
component assertion, and final SSSOM row pass, but stale notes still describe
the older unresolved import state and the superseded `DEFINED_MEDIUM`
terminology.

## Identity

- Reviewed record: `data/ingredients/mapped/H2trimethylamine.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:h2_trimethylamine`
  with the same local `ontology_mapping.ontology_id`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: NAMED_MEDIUM`.
- Components: `dihydrogen` grounded to `CHEBI:18276` and `trimethylamine`
  grounded to `CHEBI:18139`, both with `reference_scope: MIM_CATALOG`.
- Component assertion: `method: LABEL_ENUMERATION`,
  `completeness: COMPLETE`, with `SOURCE_LABEL` and `CURATED_DATASET`
  evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H2tetramethylammonium.yaml data/ingredients/mapped/H2trimethylamine.yaml data/ingredients/mapped/H2wo4.yaml data/ingredients/mapped/H3PO4.yaml data/ingredients/mapped/H3bo2.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because the primary
  `kgmicrobe.ingredient` CURIE is local to MIM and outside the OBO/CAS scope
  of this check.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- The current curated decomposition resolves both retained top-level parts of
  `H2+trimethylamine`: `dihydrogen` to `CHEBI:18276` and `trimethylamine` to
  `CHEBI:18139`.
- The `component_assertion` states that the source label explicitly names every
  retained top-level part and that the curated residual-research row reviewed
  the split as an H2 donor plus TMA methylated substrate.
- The final SSSOM publishes one exact local registry row from
  `MIM:H2trimethylamine` to `kgmicrobe.ingredient:h2_trimethylamine`.
- Minor: top-level `notes` still say the imported record had no CAS-RN or
  CHEBI/NCIT match and needed curator review, even though the current local
  fallback and decomposition have been curated.
- Minor: `ontology_mapping.evidence[0].notes` still describes
  `ingredient_type=DEFINED_MEDIUM`; the accepted current value is
  `NAMED_MEDIUM`.

## Completeness

- The local primary identifier, local ontology mapping, components,
  component-assertion evidence, mapped status, and final SSSOM row are complete
  and consistent.
- Only stale free-text notes remain to clean up.

## Recommended Edits

- Minor: update top-level `notes` to summarize the accepted local fallback and
  curated two-component decomposition.
- Minor: refresh `ontology_mapping.evidence[0].notes` so the exact SSSOM
  evidence no longer mentions the old `DEFINED_MEDIUM` value.
