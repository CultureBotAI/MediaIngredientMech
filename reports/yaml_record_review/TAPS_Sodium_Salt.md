# `data/ingredients/mapped/TAPS_Sodium_Salt.yaml`

## Verdict

Needs curation - major. The CAS sodium-salt identity, PubChem structure,
neutral `CHEBI:191055` parent, occurrence count, aggregate row, and exact
registry rows pass, but the record still has a provisional `BUFFER` role and
the final SSSOM parent row publishes the neutral-acid shorthand `TAPS` in
`other`.

## Identity

- Reviewed record: `data/ingredients/mapped/TAPS_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:91000-53-2` with
  `ontology_mapping.ontology_id: CHEBI:191055`, label
  `N-[tris(hydroxymethyl)methyl]-3-aminopropanesulfonic acid`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `91000-53-2`, PubChem CID `23667519`, formula
  `C7H16NNaO6S`, and PubChem InChI/SMILES for the sodium salt.
- Occurrences: 8 occurrences across 8 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Synergistin_A` through `TAPS_Sodium_Salt`: exited 0 and wrote zero ERROR
  rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:191055` as neutral TAPS with CAS
  `29915-38-6`, formula `C7H17NO6S`, and no sodium counterion; the parent is
  narrower than generic `CHEBI:26714` sodium salt but still only a parent for
  CAS `91000-53-2`.
- Fresh PubChem lookup for CID `23667519` returns CAS `91000-53-2`, formula
  `C7H16NNaO6S`, and InChI/SMILES matching the YAML sodium salt.
- `mappings/culturemech_recipe_membership.tsv` has eight `cas:91000-53-2`
  rows, agreeing with `total_occurrences: 8` and `media_count: 8`.
- Major: `physicochemical_roles.BUFFER` cites only
  `reference_type: COMPUTATIONAL_PREDICTION` from a curated name pattern and
  explicitly notes that review is recommended.
- Major: the final `skos:narrowMatch` parent row to `CHEBI:191055` publishes
  `TAPS` in `other`. `TAPS` is the neutral-acid shorthand and is not precise
  enough for the sodium-salt MIM subject; the exact CAS and KG-Microbe sibling
  rows correctly publish only `CAS:91000-53-2`.

## Completeness

- The CAS sodium-salt identity, nearer neutral-TAPS parent, PubChem structure,
  aggregate row, occurrence count, and exact registry rows agree.
- The record has no components, environmental contexts, or datasets needing
  narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT, parent
  repair, occurrence membership, final SSSOM, row-review, registry-triage, and
  generated rows; the old `CHEBI:26714` row is stale row-review history, not a
  current final SSSOM mapping.

## Recommended Edits

- Major: remove bare `TAPS` as an active synonym from
  `data/ingredients/mapped/TAPS_Sodium_Salt.yaml`, or retype it as provenance
  that the SSSOM builder will not export for the sodium-salt subject.
- Major: replace the provisional name-pattern `BUFFER` role with source-backed
  evidence for TAPS sodium salt as a buffer, or remove the role if no maintained
  source supports it.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` so the
  `CHEBI:191055` parent row no longer publishes `TAPS` in `other` while the
  exact CAS and KG-Microbe sibling rows continue to preserve `CAS:91000-53-2`.
