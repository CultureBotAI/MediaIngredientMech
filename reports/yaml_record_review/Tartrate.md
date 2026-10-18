# `data/ingredients/mapped/Tartrate.yaml`

## Verdict

Needs curation - major. The generic MicrobeDecoder surface `Tartrate` maps
cleanly to active `CHEBI:132950`, but the final SSSOM publishes the typo
`Tartate` in `other`, and that token is not a real synonym for the subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Tartrate.yaml`.
- Identifier and grounding: `identifier: CHEBI:132950` with
  `ontology_mapping.ontology_id: CHEBI:132950`, label `tartrate`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Occurrences: zero CultureMech recipe occurrences and 3 MicrobeDecoder
  metabolite-utilization rows.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Tangeritin` through `Tartrate`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:132950` as `tartrate` and lists
  same-substance ChEBI synonyms such as `tartrate anion` and `tartrates`.
- The structured mapping evidence preserves the MicrobeDecoder OLS
  label-exact import for `kgmicrobe.trait:tartrate`.
- Major: `Tartate` is explicitly curated as a single-character typo absorbed
  from an unmapped duplicate, but the final exact CHEBI row for
  `MIM:Tartrate` publishes `Tartate` in `other`. Fresh OLS4 and PubChem
  searches did not find a resolving tartrate synonym for that token.

## Completeness

- The CHEBI identity, aggregate row, MicrobeDecoder source occurrence, and
  final SSSOM object all agree.
- The active `RAW_TEXT` typo is not complete enough for the final SSSOM because
  `other` is a published synonym column, not a typo or rejected-label channel.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected MicrobeDecoder import,
  typo-merge provenance, aggregate, row-review, final SSSOM, and generated
  rows.

## Recommended Edits

- Major: in `data/ingredients/mapped/Tartrate.yaml`, retype `Tartate` as a
  provenance-only or rejected label, or move it to a field the SSSOM builder
  will not export as a same-subject synonym.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` so
  `MIM:Tartrate` no longer publishes `Tartate` in `other`.
