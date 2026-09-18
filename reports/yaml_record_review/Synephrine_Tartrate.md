# `data/ingredients/mapped/Synephrine_Tartrate.yaml`

## Verdict

Pass. The CAS fallback identity, PubChem structure fields, aggregate row, and
final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Synephrine_Tartrate.yaml`.
- Identifier and grounding: `identifier: cas:16589-24-5` with the same
  `ontology_mapping.ontology_id`, label `Synephrine Tartrate`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `16589-24-5`, PubChem CID `101532`, formula
  `C22H32N2O10`, and PubChem InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Supplemented_Seawater` through `Synephrine_Tartrate`: exited 0 and wrote
  zero ERROR rows.
- Direct old Engine A/OBO term validation was skipped for this CAS fallback row
  because CAS registry CURIEs are intentionally outside the CHEBI-focused OBO
  term subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh PubChem lookup for CID `101532` returns formula `C22H32N2O10` and the
  same InChI as the YAML; PubChem synonyms include CAS `16589-24-5` and the
  same `Synephrine tartrate` label.
- The record has no CHEBI or NCIT parent; the CAS fallback row therefore
  preserves the CultureBotHT identity directly.
- The final SSSOM row exact-matches `cas:16589-24-5`, uses
  `semapv:ManualMappingCuration`, and publishes only `CAS:16589-24-5` in
  `other`.

## Completeness

- The CAS fallback identity, PubChem CID, aggregate row, zero occurrence count,
  and final SSSOM row agree.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, PubChem,
  final SSSOM, row-review, registry-triage, and generated rows, and no second
  active MIM record for `cas:16589-24-5`.

## Recommended Edits

- None.
