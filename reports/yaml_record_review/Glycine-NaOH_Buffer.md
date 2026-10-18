# `data/ingredients/mapped/Glycine-NaOH_Buffer.yaml`

## Verdict

Pass with minor issues. The deliberately local `kgmicrobe.ingredient` identity
for a named multi-component buffer, the stock-solution type, occurrence count,
and final SSSOM row pass, but the top-level note still says curator review is
needed even though #288 promoted the record.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycine-NaOH_Buffer.yaml`.
- Identifier and grounding:
  `identifier: kgmicrobe.ingredient:glycine-naoh_buffer` with matching
  `ontology_mapping.ontology_id`, label `Glycine-NaOH buffer`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- A bounded exact OLS4 search across ChEBI, NCIT, MeSH, FOODON, and ENVO found
  no standard term for `Glycine-NaOH buffer`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycerol_Mono-oleate.yaml data/ingredients/mapped/Glycerol_Monostearate.yaml data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Glycine-NaOH_Buffer.yaml data/ingredients/mapped/Glycine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Glycine-NaOH_Buffer.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  exited 1, so Engine A term validation correctly skips this local
  `kgmicrobe.ingredient` mapping.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same local primary identifier, local ontology mapping, stock-solution
  type, raw queue synonym, occurrence count, and #288 fallback evidence as the
  per-record YAML.
- The #288 evidence explicitly records the stock-solution convention: a
  multi-component preparation gets a `kgmicrobe.ingredient` mint with no single
  ontology parent.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycine-NaOH_Buffer` to
  `kgmicrobe.ingredient:glycine-naoh_buffer` by `skos:exactMatch` and exports
  no `other` synonyms.
- Minor: the top-level `notes` still preserve the original queue text saying
  `Curator review needed`; that was true at import time but stale after the
  #288 `PROMOTED_TO_MAPPED` curation event.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, the
  `mim_curie_alias` rows preserving a historical subject-case variant, and
  ignored aggregate backups.

## Completeness

- The local fallback identity, stock-solution type, occurrence count, raw queue
  label, and exact local SSSOM row are populated.
- No component decomposition is present. The label names glycine and NaOH, but
  it does not specify concentrations or pH, so omitting `components` is not a
  blocking identity defect.
- The stale top-level note needs cleanup.

## Recommended Edits

- Minor: refresh `notes` in
  `data/ingredients/mapped/Glycine-NaOH_Buffer.yaml` so they describe the #288
  local stock-solution decision instead of the old unresolved queue state.
