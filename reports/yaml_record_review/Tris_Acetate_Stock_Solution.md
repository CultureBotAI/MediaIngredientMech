# `data/ingredients/mapped/Tris_Acetate_Stock_Solution.yaml`

## Verdict

Needs curation, major. A CultureMech stock-solution label is exact-mapped to
the dry CHEBI `tris acetate` salt with no stock-solution components, and its
`BUFFER` role is still provisional name-pattern evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Tris_Acetate_Stock_Solution.yaml`.
- Identifier and grounding: `identifier: CHEBI:66869` with matching
  `ontology_mapping.ontology_id`, label `tris acetate`, source `CHEBI`,
  `mapping_quality: LEXICAL_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: STOCK_SOLUTION`.
- Synonyms: raw stock-solution label plus the ChEBI exact synonym
  `2-amino-2-(hydroxymethyl)propane-1,3-diol acetate`.
- Occurrences: 1 CultureMech recipe occurrence in 1 medium.
- Roles: one `physicochemical_roles.BUFFER` facet at confidence `0.8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trimethylamine-hcl` through `Tris_Acetate_Stock_Solution`: exited 0 and
  wrote zero ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 term lookup for `CHEBI:66869` returns `tris acetate`, formula
  `C2H4O2.C4H11NO3`, and the same InChI and SMILES as the YAML.
- That ChEBI term is an acetate salt, not a stock solution.
- The CultureMech label is `Tris Acetate Stock Solution`, and the record was
  classified as `STOCK_SOLUTION` from its name.
- A hidden/ignored-inclusive search across `mappings`, `data/curated`, and
  `reports` found the same label in `data/curated/unmapped_complex_media.yaml`
  as `UNMAPPED_0077` with notes `Complex media or named solution -
  intentionally unmapped`.
- The final SSSOM row has
  `MIM:Tris_Acetate_Stock_Solution skos:exactMatch CHEBI:66869` and exports
  the ChEBI salt synonym in `other`.

## Issues

### Major: a stock solution is exact-mapped to a small salt

`Tris Acetate Stock Solution` denotes a supplied solution; `CHEBI:66869` is
the acetate salt only. The record has `ingredient_type: STOCK_SOLUTION` but no
components, concentration, solvent, or broader/narrower mapping that preserves
the solution boundary.

### Major: `BUFFER` is provisional name-pattern evidence

The only role assertion is:

```yaml
physicochemical_roles:
- role: BUFFER
  confidence: 0.8
  evidence:
  - reference_type: COMPUTATIONAL_PREDICTION
    reference_text: Inferred from curated media-role name pattern
    curator_note: Provisional role from a curated name-pattern rule; review recommended.
```

The stem match to ChEBI does not independently curate the buffer role.

## Completeness

- The YAML, aggregate copy, and final SSSOM row are synchronized for the
  current exact CHEBI mapping.
- The consequential gaps are the wrong exact identity, absent stock-solution
  representation, stale duplicate unmapped complex-media entry, and
  provisional role evidence.

## Recommended Edits

- Replace the exact `CHEBI:66869` mapping with a stock-solution representation
  that keeps the solution distinct from the dry tris acetate salt; add
  components only if the source gives enough solvent and concentration detail.
- Reconcile the stale `UNMAPPED_0077` complex-media aggregate entry after the
  stock-solution identity is resolved.
- Replace the `BUFFER` computational prediction with curated evidence, or
  remove `physicochemical_roles` until such support is added.
