# `data/ingredients/mapped/Trigonelline.yaml`

## Verdict

Needs curation, major. The current MeSH exact mapping still resolves, but CHEBI
now has an exact candidate for the free betaine while this chemical remains on
the MeSH fallback and lacks the usual CHEBI chemical fields.

## Identity

- Reviewed record: `data/ingredients/mapped/Trigonelline.yaml`.
- Identifier and grounding: `identifier: mesh:C009560` with matching
  `ontology_mapping.ontology_id`, label `trigonelline`, source `MESH`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Synonyms: one raw CultureBotHT label identical to the preferred term.
- Occurrences: 2 CultureBot recipe occurrences in 2 media.
- Chemical classification and structure: absent.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Triethanolamine` through `Trimethylamine-N-oxide`: exited 0 and wrote zero
  ERROR rows.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh all-ontology OLS4 search for `Trigonelline` returns the exact MeSH term
  `mesh:C009560`, so the current target is resolvable.
- Fresh CHEBI-scoped OLS4 search for `Trigonelline` returns `CHEBI:18123`
  `N-methylnicotinate`, whose related synonyms include `Trigonelline`.
- The same CHEBI search also returns the separate salt term `CHEBI:229203`
  `Trigonelline HCl`; that hydrochloride form is already modeled by
  `data/ingredients/mapped/Trigonelline_HCl.yaml` and should stay distinct.
- The final SSSOM row has `MIM:Trigonelline skos:exactMatch mesh:C009560` and
  exports no `other` tokens.

## Issues

### Major: exact ChEBI grounding is still unresolved

The record was promoted to MeSH on 2026-05-02 because no ChEBI mapping was
available at that point. ChEBI now exposes `CHEBI:18123` with `Trigonelline` as
a synonym for the free betaine, so this chemical should be reviewed against
that candidate instead of being left on a MeSH fallback with no
`ingredient_type` or `chemical_properties`.

## Completeness

- The MeSH row itself, the aggregate copy, and the final SSSOM row agree.
- The consequential gap is the unreviewed CHEBI candidate for the exact
  chemical identity.

## Recommended Edits

- Evaluate `CHEBI:18123` for `Trigonelline`; if exact, remap this record from
  `mesh:C009560` to `CHEBI:18123`, populate the normal
  `SINGLE_INGREDIENT`/chemical-property fields, regenerate the aggregate copy
  and final SSSOM row, and leave the existing `Trigonelline_HCl` salt record on
  `CHEBI:229203`.
