# Ingredient and recipe hierarchy boundary

MediaIngredientMech does not currently encode a local parent/child hierarchy
among ingredient records. The former `parent_ingredient`, `child_ingredients`,
`variant_type`, `variant_notes`, and `role_inheritance` schema surface was
retired in [#448](https://github.com/CultureBotAI/MediaIngredientMech/issues/448):
no curated record used it, its helpers depended on a retired record key, and the
current `identifier` field is not a unique document key for every record.

## What MIM represents

- Each ingredient record denotes one distinct substance or material and is
  grounded independently under [MAPPING_SEMANTICS.md](../MAPPING_SEMANTICS.md).
- Decisions about whether a form or grade is a distinct record follow the
  identity and `supplied_form` rules in `MAPPING_SEMANTICS.md`; retiring the
  hierarchy neither authorizes a merge nor requires a split.
- `components` is a one-level material has-part assertion for mixtures and
  stocks. It is not a variant relation and must not be used to imitate one.
- `ingredient_type` classifies record granularity. It is not a hierarchy edge.

MIM presently records no local relationship from one chemical form or grade to
another. Broader ontology relationships may be documented as grounding evidence,
but they do not create a local parent record. `MAPPING_SEMANTICS.md` remains the
authority for the identity boundary.

## What CultureMech represents

CultureMech is authoritative for culturing-recipe bodies, nested preparations,
recipe families, and media variants. MIM may ground a named medium or preserve a
cross-repository reference, but it does not reproduce CultureMech's recipe
hierarchy. In particular, `components` must not be read as a complete recipe
unless its own assertion and evidence explicitly establish completeness.

## Requirements before any hierarchy returns

A future proposal needs all of the following before adding schema fields or an
API:

1. a stable, unique record-addressing contract distinct from ontology grounding;
2. a curated use case and migration cohort;
3. an explicit relationship vocabulary and topology;
4. resolution, ambiguity, reciprocity, self-link, duplicate-edge, and cycle
   validation in normal QC;
5. defined role/provenance behavior; and
6. tested public exports and consumer coordination.

The retired prototype, water example, and old duplicate/variant analysis remain
in `ATTIC/` as historical design material, not as supported instructions,
runnable tooling, or current analysis output.
