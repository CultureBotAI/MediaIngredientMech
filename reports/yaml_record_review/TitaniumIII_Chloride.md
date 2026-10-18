# `data/ingredients/mapped/TitaniumIII_Chloride.yaml`

## Verdict

Pass. The CAS fallback identity for titanium(III) chloride is synchronized
across the per-record YAML, aggregate row, and final SSSOM output.

## Identity

- Reviewed record: `data/ingredients/mapped/TitaniumIII_Chloride.yaml`.
- Identifier and grounding: `identifier: cas:7705-07-9` with matching
  `ontology_mapping.ontology_id`, label `TitaniumIII chloride`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `7705-07-9`.
- Synonyms: raw mim-queue source form `TitaniumIII chloride`.
- Occurrences: no MediaDive/media occurrence count.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Ticarcillin` through `TitaniumIII_Chloride`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this CAS fallback
  row because `cas:7705-07-9` is intentionally outside the CHEBI-focused OBO
  term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh PubChem lookup for CAS `7705-07-9` returns formula `Cl3Ti` with the
  same trichloride connectivity expected for titanium(III) chloride.
- Fresh exact OLS4 search for `titanium trichloride` returns the nearby MeSH
  `mesh:C039460` term and lists `titanium(III) chloride` as a synonym, agreeing
  with the Edison review that CAS `7705-07-9` denotes titanium trichloride.
- The final SSSOM row has
  `MIM:TitaniumIII_Chloride skos:exactMatch cas:7705-07-9`, uses
  `registry:cas`, and exports only `CAS:7705-07-9` in `other`.

## Completeness

- The CAS identity, aggregate copy, and final SSSOM row agree.
- No components, media roles, chemical structure fields, environmental
  contexts, or extra final `other` tokens require curation.
- The `TiCl3` local record remains a separate reviewed source surface and
  already carries the direct MeSH exact mapping.

## Recommended Edits

- None.
