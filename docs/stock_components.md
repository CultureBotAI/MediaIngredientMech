# Ingredient/mixture partonomy: `components`

`IngredientRecord.components` is an unordered, one-level material **has-part**
assertion for a `STOCK_SOLUTION`, `DEFINED_MEDIUM`, or `UNDEFINED_MIXTURE`.
It may transcribe a combination label or record known parts of a named mixture.
It does not say that the record *is* one of its parts, and it is not evidence of
a complete culturing recipe unless the assertion says so explicitly.

```yaml
- identifier: kgmicrobe.ingredient:example_mix
  preferred_term: Example mix
  ingredient_type: STOCK_SOLUTION
  components:
    - component_name: FeCl3 x 6 H2O
      component_id: CHEBI:86254
      reference_scope: MIM_CATALOG
      concentration_value: "1.5"
      concentration_unit: G_PER_L
    - component_name: unpublished cofactor fraction
      reference_scope: UNMAPPED
  component_assertion:
    method: RECIPE_TRANSCRIPTION
    completeness: COMPLETE
    evidence:
      - evidence_type: RECIPE_SOURCE
        source: example:recipe-1
        source_record: stock solution A
```

## Reference scope

Every component declares how its identifier should resolve:

- `MIM_CATALOG`: at least one non-rejected MIM record has this exact primary
  `identifier`. Historical duplicate-identifier families mean this resolves the
  represented entity, not necessarily one physical YAML document.
- `EXTERNAL_TERM`: the CURIE deliberately names an ontology/registry entity not
  represented by an active MIM record. This does not require fabricating a local
  ingredient row.
- `UNMAPPED`: the supporting source names the part, but no `component_id` is known.

`MIM_CATALOG` and `EXTERNAL_TERM` require `component_id`; `UNMAPPED` forbids it.
When a previously external term gains a MIM record, the corpus validator requires
its scope to be updated.

## Method, completeness, and evidence

`component_assertion` is required whenever `components` is present. Its method is
one of:

- `LABEL_ENUMERATION`: the source label explicitly lists every retained top-level part;
- `ABBREVIATION_EXPANSION`: a reviewed curation expands shorthand such as `PYG`;
- `CURATED_INTERPRETATION`: reviewed evidence establishes the list without a
  literal enumeration or direct recipe transcription;
- `RECIPE_TRANSCRIPTION`: constituents and quantities come from a cited verified recipe.

Completeness is independent of method. `COMPLETE` means complete relative to the
cited source assertion; it does not turn a MicrobeDecoder label into a CultureMech
recipe. Use `PARTIAL` when the source explicitly says constituents are omitted and
`UNKNOWN` when it does not settle completeness.

Evidence is structured (`evidence_type`, `source`, and optional `source_record` /
`notes`). The legacy per-component `source` string remains readable for compatibility,
but new record-level provenance belongs in `component_assertion.evidence`.

## Validation and current corpus

`just qc-component-partonomy` checks the cross-record invariants that LinkML cannot:
local resolution, target-label agreement, self-reference, duplicate parts, and
reference-scope currency. LinkML write-time validation additionally enforces the
closed shape, assertion pairing, allowed parent types, scope/identifier pairing,
and concentration value/unit pairing.

After the #369 migration, MIM has 54 component-bearing records and 143 parts:
131 `MIM_CATALOG`, 10 `EXTERNAL_TERM`, and 2 `UNMAPPED`. These came from
MicrobeDecoder trait/source curation; none should be read as a full CultureMech
recipe merely because it has `components`.

## Boundaries

- A whole-to-part identity or ontology match belongs in grounding/SSSOM, never in
  `components`. Giving a mixture one part's CAS or CURIE would assert that the
  whole *is* that part.
- MIM currently encodes no local relationship among records that differ in
  hydration, stereochemistry, salt form, or grade. Whether those details create
  a distinct identity or live in `supplied_form` follows `MAPPING_SEMANTICS.md`;
  `components` must not substitute for either decision.
- CultureMech recipe procedure, solution hierarchy, family, and variant semantics
  remain CultureMech responsibilities; this slot carries only the MIM-side material
  parts supported by the cited evidence.

See [MAPPING_SEMANTICS.md](../MAPPING_SEMANTICS.md) for the identity boundary and
[HIERARCHY_GUIDE.md](HIERARCHY_GUIDE.md) for the hierarchy boundary.
