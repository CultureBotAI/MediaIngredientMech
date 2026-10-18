# `data/ingredients/mapped/Titanium_chloride.yaml`

## Verdict

Needs curation, major. The final SSSOM row is synchronized, but the exact
match from the under-specified surface `Titanium chloride` to titanium
tetrachloride is supported only by a broad ChEBI synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Titanium_chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:231499` with matching
  `ontology_mapping.ontology_id`, label `titanium tetrachloride`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `match_level: NORMALIZED`, and
  `mapping_status: MAPPED`.
- Synonyms: none.
- Occurrences: 2 CultureMech occurrences in 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Titanium_chloride` through `Tomatidine_Hydrochloride`: exited 0 and wrote
  zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 search for `titanium chloride` returns only `CHEBI:231499`
  `titanium tetrachloride` in ChEBI, but the matching string is in the broad
  synonym bucket rather than the exact-synonym bucket.
- The final SSSOM row has
  `MIM:Titanium_chloride skos:exactMatch CHEBI:231499`, uses `obo:chebi.owl`,
  cites the restored CultureMech occurrence source, and leaves `other` empty.

## Issues

### Major: the source surface omits the oxidation state

The source text says `Titanium chloride`, while the exact SSSOM object is
titanium tetrachloride. The live OLS response shows `titanium chloride` as a
related ChEBI synonym for `CHEBI:231499`; it does not establish that the two
CultureMech recipes meant TiCl4 rather than another titanium chloride surface.
That makes the current `skos:exactMatch` too strong until the recipe context is
reviewed.

## Completeness

- Occurrence counts, the aggregate row, and the final SSSOM row agree.
- No media roles, chemical properties, components, or final SSSOM synonym
  tokens are asserted.
- The only issue is the unsupported specificity of the exact TiCl4 grounding.

## Recommended Edits

- Inspect the two source recipes and either keep `CHEBI:231499` with explicit
  context evidence for titanium tetrachloride or downgrade/remap this surface
  to an under-specified local registry entry.
