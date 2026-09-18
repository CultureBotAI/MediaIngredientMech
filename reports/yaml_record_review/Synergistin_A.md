# `data/ingredients/mapped/Synergistin_A.yaml`

## Verdict

Pass. The exact MeSH `mesh:C003372` identity, aggregate row, and final SSSOM
row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Synergistin_A.yaml`.
- Identifier and grounding: `identifier: mesh:C003372` with
  `ontology_mapping.ontology_id: mesh:C003372`, label `synergistin A`, source
  `MESH`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Synergistin_A` through `TAPS_Sodium_Salt`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this MeSH record
  because MeSH registry CURIEs are intentionally outside the CHEBI-focused OBO
  term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh exact OLS4 search resolves `mesh:C003372` with label `synergistin A`,
  agreeing with the prior local prefix-specific OLS validation.
- The record was upgraded from a temporary `kgmicrobe.compound:synergistin_a`
  placeholder to the MeSH exact label match and has no later drift back to a
  local fallback.
- The final SSSOM row exact-matches `mesh:C003372`, uses
  `semapv:LexicalMatching`, names `registry:mesh` as its object source, and
  leaves `other` empty.

## Completeness

- The exact MeSH identity, aggregate row, zero occurrence count, and final SSSOM
  row agree.
- The record has no active synonyms, components, roles, environmental contexts,
  datasets, or structure fields needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected kg-microbe placeholder,
  MeSH upgrade, prefix-triage, aggregate, generated index, and final SSSOM
  rows, and no second active MIM record for `mesh:C003372`.

## Recommended Edits

- None.
