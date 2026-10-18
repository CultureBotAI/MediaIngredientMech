# `data/ingredients/mapped/H23-methyl_Mercaptopropionate.yaml`

## Verdict

Pass with minor issues. The local fallback identity, two-part decomposition,
component assertion, and final SSSOM row pass, but stale notes still describe
the older unresolved label split.

## Identity

- Reviewed record:
  `data/ingredients/mapped/H23-methyl_Mercaptopropionate.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:h2_3_methyl_mercaptopropionate` with the
  same local `ontology_mapping.ontology_id`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: NAMED_MEDIUM`.
- Components: `dihydrogen` grounded to `CHEBI:18276` with
  `reference_scope: MIM_CATALOG`, and `3-(methylthio)propionic acid` grounded
  to `CHEBI:1438` with `reference_scope: EXTERNAL_TERM`.
- Component assertion: `method: LABEL_ENUMERATION`,
  `completeness: COMPLETE`, with `SOURCE_LABEL` and `CURATED_DATASET`
  evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Guanidinium_Chloride.yaml data/ingredients/mapped/Guanine.yaml data/ingredients/mapped/Guanosine.yaml data/ingredients/mapped/Gum_Arabic_From_Acacia_Tree.yaml data/ingredients/mapped/H23-methyl_Mercaptopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because the primary
  `kgmicrobe.ingredient` CURIE is local to MIM and outside the OBO/CAS scope
  of this check.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- The current curated decomposition resolves both retained top-level parts of
  `H2+3-methyl Mercaptopropionate`: `dihydrogen` to `CHEBI:18276` and
  `3-(methylthio)propionic acid` to `CHEBI:1438`.
- The `component_assertion` states that the source label explicitly names every
  retained top-level part and that the curated residual-research row reviewed
  the split.
- The final SSSOM publishes one exact local registry row from
  `MIM:H23-methyl_Mercaptopropionate` to
  `kgmicrobe.ingredient:h2_3_methyl_mercaptopropionate`.
- Minor: top-level `notes` still say the imported record had no CAS-RN or
  CHEBI/NCIT match and needed curator review, even though the current local
  fallback and decomposition have been curated.
- Minor: `ontology_mapping.evidence[0].notes` still describe the first
  automated plus-sign split with only one resolved constituent and
  `ingredient_type=DEFINED_MEDIUM`; both constituents are now resolved in the
  curated component list and the record is now `NAMED_MEDIUM`.

## Completeness

- The local primary identifier, local ontology mapping, components,
  component-assertion evidence, mapped status, and final SSSOM row are complete
  and consistent.
- Only stale free-text notes remain to clean up.

## Recommended Edits

- Minor: update top-level `notes` to summarize the accepted local fallback and
  curated two-component decomposition.
- Minor: refresh `ontology_mapping.evidence[0].notes` so the exact SSSOM
  evidence no longer describes the superseded one-of-two label split.
