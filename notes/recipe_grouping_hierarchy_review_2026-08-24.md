# Culturing recipe grouping and hierarchy review

**Date:** 2026-08-24

**Scope:** MediaIngredientMech's representation of culturing recipes, mixtures,
components, and parent/child relationships.

**Method:** Read-only schema, pipeline, data, validation, and generated-output audit.

Bottom line: this repo does not maintain a working hierarchy of culturing recipes.
It is an ingredient-centric mapping repository that sometimes represents named
media or mixtures as `IngredientRecord`s. Recipe grouping is mostly flat
classification; recipe composition is sparse; the only parent/child model is
dormant ingredient-variant scaffolding.

## Current model

| Mechanism | Meaning | Live usage |
|---|---|---:|
| `IngredientCollection.ingredients` | Storage container, not scientific hierarchy | 2,846 records |
| `ingredient_type` | Flat record-kind classification | 2,709 populated |
| `solution_type` | Flat subtype for stock/premix records | 76 |
| `components` | One-level “has parts” decomposition | 57 records |
| `culturemech_medium_name` | Free-text upstream link | 2 records |
| `parent_ingredient` / `child_ingredients` | Chemical-form variants, not recipe variants | 0 records |

The live type distribution is 2,232 `SINGLE_INGREDIENT`, 127 `DEFINED_MEDIUM`,
121 `STOCK_SOLUTION`, 229 `UNDEFINED_MIXTURE`, and 137 untyped. The schema
explicitly overloads `IngredientRecord` to hold complete named recipes through
`DEFINED_MEDIUM`; there is no `MediaRecipe`, recipe family, or media-variant
class. [Schema definition](../src/mediaingredientmech/schema/mediaingredientmech.yaml#L68)
[type semantics](../src/mediaingredientmech/schema/mediaingredientmech.yaml#L172)

## Main findings

### 1. Recipe membership is flattened during import

CultureMech occurrence entries can identify the medium, file, category, and
ingredient position, but MIM reduces them to `total_occurrences` and
`media_count = len(media_occurrences)`. It stores no recipe-membership edge, and
`sample_media` is empty on every live record. MIM therefore cannot reconstruct
which recipes contain an ingredient. [Importer](../scripts/import_from_culturemech.py#L107)
[occurrence schema](../src/mediaingredientmech/schema/mediaingredientmech.yaml#L468)

### 2. The apparent hierarchy is both out of scope and nonfunctional

`parent_ingredient`, `child_ingredients`, and `variant_type` are intended for
hydrates, stereoisomers, salts, and purity variants—not media recipes. The guide
expressly says not to use them for complex media. The schema calls the feature
“currently unused,” and the live corpus confirms zero populated hierarchy
fields. [Hierarchy fields](../src/mediaingredientmech/schema/mediaingredientmech.yaml#L196)
[scope guidance](../docs/HIERARCHY_GUIDE.md#L332)

More seriously, the hierarchy utilities still search for the retired `id` field
rather than the canonical `identifier`. A valid current-style parent/child pair
is consequently reported as missing. The historical water builder is explicitly
marked non-runnable and fails current strict validation. Normal QC never invokes
hierarchy validation. [Query bug](../src/mediaingredientmech/utils/hierarchy_utils.py#L18)
[validator bug](../src/mediaingredientmech/utils/hierarchy_validator.py#L14)
[disabled builder](../scripts/build_water_hierarchy.py#L13)

### 3. `ingredient_type` has competing meanings

The schema says `DEFINED_MEDIUM` means a complete named recipe, regardless of
whether it contains chemically undefined extracts. Some curation scripts instead
classify according to constituent definedness. Thus substrate combinations such
as `Formate+methanol` become `DEFINED_MEDIUM`, while complete named media
containing peptone or yeast extract become `UNDEFINED_MIXTURE`.
[Contradictory classifier](../scripts/decompose_substrate_combinations.py#L26)
[Marine-media rule](../scripts/add_culturemech_gap_labels.py#L349)

Consequently, `ingredient_type` cannot currently be trusted as either “record
granularity” or “chemical definedness.”

### 4. Composition is shallow, sparse, and semantically mixed

The 57 component-bearing records contain 147 component entries, 145 identifiers,
and no concentrations. They comprise 24 `DEFINED_MEDIUM` and 33
`UNDEFINED_MIXTURE` records; none of the 121 `STOCK_SOLUTION` records has
components. All 57 came from MicrobeDecoder curation rather than imported
CultureMech recipes.

The decomposition loader collapses three different claims—splitting a label,
matching a medium, and mapping to one ingredient—into the same `components`
structure. There is no nesting, preparation order, final volume, procedure,
optional component, or explicit relation type.
[Component schema](../src/mediaingredientmech/schema/mediaingredientmech.yaml#L648)
[collapsed strategies](../scripts/apply_curated_decompositions.py#L29)

### 5. CultureMech linking is too weak for recipe variants

`culturemech_medium_name` stores only a string, not a stable CultureMech
identifier or match relationship. BHI’s stable `CultureMech:015492` identifier
survives only in evidence prose. GYPS uses the same field even though its evidence
says the two formulations are merely close, not identical.
[BHI record](../data/ingredients/mapped/BHI.yaml#L73)
[GYPS record](../data/ingredients/mapped/GYPS.yaml#L74)

### 6. Generated views hide nearly all this structure

Browser JSON omits type, components, CultureMech links, and hierarchy fields.
Ingredient pages display only a type badge, with no components or relationships.
[Browser export](../scripts/browser_export.py#L73)
[page template](../src/mediaingredientmech/templates/ingredient.html.j2#L19)

## Relation to #317

There is a plausible direct source of some false `EXACT_MATCH` grades: MIM
translates CultureMech `DIRECT_MATCH` to `EXACT_MATCH`, while CultureMech’s
aggregator currently assigns `DIRECT_MATCH` broadly. That loses whether the
underlying evidence was actually a preferred-label or synonym match.
[MIM translation](../scripts/import_from_culturemech.py#L96)

## Recommended boundary

- Keep stable recipe identities, nested formulations, recipe families, and
  recipe variants authoritative in CultureMech.
- Keep chemical/material identity and chemical-form variants authoritative in
  MIM.
- Replace `culturemech_medium_name` with a structured reference containing stable
  ID, name/path, relationship type, evidence, and formulation-match status.
- Preserve per-recipe occurrence edges instead of deriving and retaining counts
  alone.
- Separate `record_kind` from `composition_definedness`.
- Keep `components` as partonomy; add a distinct recipe-level `variant_of`
  relation rather than reusing `parent_ingredient`.
- Either repair the dormant hierarchy around `identifier` and add reciprocal/
  cycle validation to QC, or remove the misleading utilities and
  “production-ready” documentation.
- Preserve mapping-method provenance so synonym matches cannot be promoted to
  `EXACT_MATCH`.

Overall, the repo is workable as an ingredient-mapping system, but not currently
reliable as a recipe grouping or hierarchy system.

## Follow-up issue set

The review and its #317 implementation audit were decomposed into seven new
issues and focused extensions to three existing issues. Existing owners were
reused where the underlying problem was already tracked.

### New issues

- [#447 — Replace name-only CultureMech medium links with stable, typed recipe
  references](https://github.com/CultureBotAI/MediaIngredientMech/issues/447)
  defines the cross-repository identity and relationship contract.
- [#449 — CultureMech import derives `media_count` from a capped example list and
  drops recipe memberships](https://github.com/CultureBotAI/MediaIngredientMech/issues/449)
  preserves lossless ingredient-to-recipe edges and correct counts. It depends
  on #447's stable recipe IDs.
- [#448 — Repair or retire the dormant ingredient-variant hierarchy and wire its
  invariants into QC](https://github.com/CultureBotAI/MediaIngredientMech/issues/448)
  makes the chemical/material hierarchy either operational or explicitly
  unsupported; it does not repurpose that hierarchy for recipes.
- [#453 — Retire or rebuild the public CultureMech bulk importer](https://github.com/CultureBotAI/MediaIngredientMech/issues/453)
  records the implementation-review finding that `just import-data` is both
  schema-invalid today and destructive if superficially repaired. It is the
  lifecycle/safety prerequisite for the #447/#449 redesign.
- [#454 — Resolve the thioctic-acid CAS/stereochemistry conflict](https://github.com/CultureBotAI/MediaIngredientMech/issues/454)
  tracks the one CAS-provenance candidate whose current CAS does not cross-reference
  its current ChEBI target; it is excluded from the mechanical #317 re-grade.
- [#455 — Reground five CAS-selected records with explicit form/counterion
  conflicts](https://github.com/CultureBotAI/MediaIngredientMech/issues/455)
  separates identity defects uncovered by the #317 implementation audit from
  safe evidence-grade corrections; those records are deliberately not merely
  regraded.
- [#456 — Reground ten CAS-selected records with explicit stereochemical
  conflicts](https://github.com/CultureBotAI/MediaIngredientMech/issues/456)
  tracks cis/trans, racemate, and enantiomer-specific labels whose current CAS
  or target cannot support the asserted identity.

### Existing issues extended

- [#222](https://github.com/CultureBotAI/MediaIngredientMech/issues/222#issuecomment-5384919304)
  now carries the executable semantic split between record kind and composition
  definedness, with migration criteria and coordination points for #323/#330.
- [#369](https://github.com/CultureBotAI/MediaIngredientMech/issues/369#issuecomment-5384919267)
  now carries the broader validated component-partonomy contract rather than
  treating two dangling CURIEs as the whole problem.
- [#317](https://github.com/CultureBotAI/MediaIngredientMech/issues/317#issuecomment-5384919367)
  now records the CultureMech `DIRECT_MATCH` → MIM `EXACT_MATCH` regeneration
  path and the needed import-time prevention.

### Deliberately not duplicated

Closed [#438](https://github.com/CultureBotAI/MediaIngredientMech/issues/438)
enforces self-identity rows: a MIM subject mapping to its own primary identifier
must use `skos:exactMatch`. It cannot detect #317 because mapping evidence and
identity predicates are independent. A record correctly graded
`SYNONYM_MATCH` still needs `skos:exactMatch` on its own-identifier identity row.
