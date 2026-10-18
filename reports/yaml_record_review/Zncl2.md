# `data/ingredients/mapped/Zncl2.yaml`

## Verdict

Needs curation. The exact `CHEBI:49976` zinc dichloride identity, CAS,
structure, source-backed `TRACE_ELEMENT` role, aggregate row, and final exact
SSSOM predicate pass, but final SSSOM still exports the invalid `ZnCl` synonym
and the malformed hydrate-like string `ZnCl .6H O` as `other` values; the
mapping also carries a redundant auto-proposed PubMed evidence item.

## Identity

- Reviewed record: `data/ingredients/mapped/Zncl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:49976` with matching
  `ontology_mapping.ontology_id`, canonical label `zinc dichloride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- CAS RN: `7646-85-7`.
- Structure: formula `2Cl.Zn` with populated InChI and SMILES.
- Synonyms: raw CultureMech `Role: Mineral source` provenance strings, exact
  zinc-dichloride synonyms from kg-microbe, and the malformed
  `sssom_other_backfill` surface `ZnCl .6H O`.
- Role: source-backed `TRACE_ELEMENT` evidence from the CultureMech original
  `Mineral source` role.
- Occurrences: 1,839 CultureMech occurrences across 1,839 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on this 5-file batch:
  exited 0 and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data` passed for this CHEBI-primary
  record with `--labels`.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.
- Fresh OLS4 exact search for `zinc dichloride` in CHEBI returned the active
  `CHEBI:49976` label `zinc dichloride`.

## Evidence

- The final SSSOM row correctly exports
  `MIM:Zncl2 skos:exactMatch CHEBI:49976`.
- Raw `Role:` and `Properties:` strings from the YAML are filtered from final
  SSSOM.
- The final `other` field exports `ZnCl` and `ZnCl .6H O`.
- The active `LITERATURE` evidence object says it was auto-proposed and should
  be rephrased or removed; the snippet only mentions `ZnCl2` as a reagent in a
  Schiff-base complex synthesis.

## Issues

- Major: `ZnCl` is not the zinc dichloride formula and should not be exported
  as a synonym for `CHEBI:49976`.
- Major: `ZnCl .6H O` is malformed and hydrate-like, so it is not a reusable
  synonym for anhydrous zinc dichloride in the final SSSOM `other` field.
- Minor: the auto-proposed PMID `38922505` evidence is redundant on an exact
  CultureMech/ChEBI row and still advertises itself as needing review.

## Completeness

- The exact CHEBI identifier, CAS, structure fields, single-ingredient type,
  CultureMech role evidence, aggregate copy, and final SSSOM predicate agree.
- The exported synonym payload and one evidence object need cleanup.

## Recommended Edits

- Remove or suppress `ZnCl` and `ZnCl .6H O` from final SSSOM `other`.
- Remove or rewrite the auto-proposed PubMed evidence item so the exact
  ontology mapping is supported only by maintained database evidence.
- Rebuild SSSOM and rerun strict validation plus SSSOM invariant validation.
