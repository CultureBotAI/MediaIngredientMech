# `data/ingredients/mapped/Trace_Mineral_Solution.yaml`

## Verdict

Needs curation, major. The local stock-solution identity is synchronized, but
all five raw CultureMech note variants leak into final SSSOM `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Trace_Mineral_Solution.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:trace_mineral_solution` with matching
  `ontology_mapping.ontology_id`, label `Trace mineral solution`, source
  `kgmicrobe.ingredient`, `mapping_quality: FALLBACK_REGISTRY`,
  `mapping_status: MAPPED`, and `ingredient_type: STOCK_SOLUTION`.
- Synonyms: raw mim-queue source form plus five raw CultureMech forms carrying
  `see Medium`, `see below`, or double-asterisk recipe notes.
- Occurrences: 2 CultureMech recipe occurrences in 2 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Trace_Mineral_Solution` through `Trans-aconitic_Acid`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this row because
  `kgmicrobe.ingredient` is a non-OBO local registry prefix.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- The August issue 288 curation minted a local `kgmicrobe.ingredient` identity
  after searching ChEBI, NCIT, MeSH, FOODON, and ENVO and retaining no parent
  because a generic trace-mineral solution is a named multi-component
  preparation.
- The final SSSOM row has
  `MIM:Trace_Mineral_Solution skos:exactMatch
  kgmicrobe.ingredient:trace_mineral_solution` and exports five raw
  CultureMech labels in `other`, including Medium No. 151, Medium No. 852,
  `see below`, and double-asterisk variants.

## Issues

### Major: recipe cross-references and footnotes reach final `other`

`Trace mineral solution (see Medium No. 151 )`, `Trace mineral solution (see
Medium No. 852 )`, `Trace mineral solution (see Medium No.852)`, `Trace
mineral solution (see below)`, and `Trace mineral solution**` are recipe-local
instructions or footnoted surfaces. They are occurrence aliases, not true
synonyms of the local stock identity, and should not be exported.

## Completeness

- The local identity, fallback registry mapping, occurrence count, aggregate
  copy, and final exact row agree.
- No roles, components, parent ontology rows, or chemical properties are
  asserted.
- The only issue is the leaked raw CultureMech aliases.

## Recommended Edits

- Mark the five CultureMech aliases as non-exportable raw source text so the
  final SSSOM `other` column is empty for this row.
