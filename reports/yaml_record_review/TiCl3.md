# `data/ingredients/mapped/TiCl3.yaml`

## Verdict

Pass. The MeSH exact match to titanium trichloride, local registry identity,
occurrence count, aggregate row, and final SSSOM row for TiCl3 are
synchronized.

## Identity

- Reviewed record: `data/ingredients/mapped/TiCl3.yaml`.
- Identifier and grounding: `identifier: mesh:C039460` with the same
  `ontology_mapping.ontology_id`, label `titanium trichloride`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: mesh:C039460`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- Synonyms: raw mim-queue source form `TiCl3`.
- Occurrences: 12 CultureMech recipe occurrences in 12 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thymidine` through `Tiamulin`: exited 0 and wrote zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this MeSH row because
  `mesh:C039460` is intentionally outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search for `TiCl3` returns MeSH `mesh:C039460` titanium
  trichloride, matching the stored OAK/OLS exact-audit decision.
- The final SSSOM has exactly one exact row for `MIM:TiCl3`, points at
  `mesh:C039460`, records `registry:mesh` as the object source, and leaves
  `other` empty.
- The nearby `TitaniumIII_Chloride` local record remains intentionally separate
  and not merged to `TiCl3` without exact source evidence for the same surface.

## Completeness

- The MeSH exact identity, occurrence count, aggregate copy, and final SSSOM
  row agree.
- No components, roles, CAS RN, chemical properties, or environmental contexts
  are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected mim-queue import, exact MeSH
  curation, aggregate, final SSSOM row, and separate
  `TitaniumIII_Chloride` record.

## Recommended Edits

- None.
