# `data/ingredients/mapped/H2_CO2.yaml`

## Verdict

Pass with minor issues. The local fallback identity, two-part decomposition,
component assertion, and final SSSOM row pass, but stale notes still describe
the older unresolved import state and the superseded `DEFINED_MEDIUM`
terminology.

## Identity

- Reviewed record: `data/ingredients/mapped/H2_CO2.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.ingredient:h2_co2` with the
  same local `ontology_mapping.ontology_id`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: NAMED_MEDIUM`.
- Components: `dihydrogen` grounded to `CHEBI:18276` and `carbon dioxide`
  grounded to `CHEBI:16526`, both with `reference_scope: MIM_CATALOG`.
- Component assertion: `method: LABEL_ENUMERATION`,
  `completeness: COMPLETE`, with `SOURCE_LABEL` and `CURATED_DATASET`
  evidence.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/H2_CO2.yaml data/ingredients/mapped/H2dimethylsulfide.yaml data/ingredients/mapped/H2methanol.yaml data/ingredients/mapped/H2seo3.yaml data/ingredients/mapped/H2so4.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- LinkML term validation was intentionally skipped because the primary
  `kgmicrobe.ingredient` CURIE is local to MIM and outside the OBO/CAS scope
  of this check.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- The current curated decomposition resolves both retained top-level parts of
  `H2 + CO2`: `dihydrogen` to `CHEBI:18276` and `carbon dioxide` to
  `CHEBI:16526`.
- The `component_assertion` states that the source label explicitly names every
  retained top-level part and that the curated residual-research row reviewed
  the split as a hydrogenotrophic-methanogen donor/acceptor pair.
- The final SSSOM publishes one exact local registry row from `MIM:H2_CO2` to
  `kgmicrobe.ingredient:h2_co2`.
- Minor: top-level `notes` still say the imported record had no CAS-RN or
  CHEBI/NCIT match and needed curator review, even though the current local
  fallback and decomposition have been curated.
- Minor: `ontology_mapping.evidence[0].notes` still describes
  `ingredient_type=DEFINED_MEDIUM`; the accepted current value is
  `NAMED_MEDIUM`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found this active YAML, matching
  aggregate copies, generated products, and the final SSSOM row.

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
