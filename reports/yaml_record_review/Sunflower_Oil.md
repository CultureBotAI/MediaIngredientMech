# `data/ingredients/mapped/Sunflower_Oil.yaml`

## Verdict

Pass. The CAS fallback identity, `NCIT:C1241` parent, CAS registry field,
aggregate row, and three final SSSOM rows all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sunflower_Oil.yaml`.
- Identifier and grounding: `identifier: cas:8001-21-6` with
  `ontology_mapping.ontology_id: NCIT:C1241`, label `Sunflower Oil`, source
  `NCIT`, `mapping_quality: NARROW_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `8001-21-6` from CultureBotHT.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfur_Compounds` through `Sunflower_Oil`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this NCIT parent
  because NCIT is outside the CHEBI-focused OBO term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `NCIT:C1241` with label `Sunflower Oil` and
  CAS Registry `8001-21-6`, matching the YAML parent and CAS fallback
  identifier.
- Fresh PubChem lookup for CAS `8001-21-6` found no CID, agreeing with the
  record's CAS-primary fallback instead of a CHEBI/PubChem exact term with
  structure fields.
- The final SSSOM has the expected `skos:narrowMatch` parent row to
  `NCIT:C1241` plus exact CAS and KG-Microbe compound registry sibling rows,
  both publishing only `CAS:8001-21-6` in `other`.

## Completeness

- The CAS fallback identity, NCIT parent, aggregate row, zero occurrence count,
  final parent row, and final registry sibling rows agree.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, NCIT, final
  SSSOM, row-review, prefix-triage, and generated rows, and no second active
  MIM record for `cas:8001-21-6`.

## Recommended Edits

- None.
