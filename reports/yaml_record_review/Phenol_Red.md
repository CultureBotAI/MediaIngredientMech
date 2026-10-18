# `data/ingredients/mapped/Phenol_Red.yaml`

## Verdict

Needs curation; major. The CultureMech import maps exactly to active
`CHEBI:31991` phenol red, but final SSSOM `other` exports salt- and
concentration-qualified source text as if it were an exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Phenol_Red.yaml`.
- Identifier and grounding: `identifier: CHEBI:31991` with
  `ontology_mapping.ontology_id: CHEBI:31991`, label `phenol red`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 113 CultureMech occurrences across 113 recipes.

## Validation

- `uv run --frozen python scripts/validate_strict.py` exited 0 across this
  five-record batch and wrote zero ERROR rows.
- A fresh OLS4 exact search for `CHEBI:31991` resolves `CHEBI:31991`
  `phenol red` and returns the kg-microbe synonym set carried by this record.
- A local CAS checksum calculation confirmed that `143-74-8` has the expected
  check digit.
- The final SSSOM row was inspected directly and maps `MIM:Phenol_Red` exactly
  to `CHEBI:31991`.

## Evidence

- The CHEBI primary identifier, mapping target, structured formula, InChI, and
  SMILES all describe phenol red.
- The `PH_INDICATOR` role is backed by imported CultureMech database evidence
  whose original role text was `Ph Indicator`.
- The raw `Role:`/`Properties:` strings remain provenance-only and are not
  leaked into final SSSOM `other`.
- Major: `(sodium salt)`, `Phenol red (0.04%)`, and
  `Phenol red (0.1% aqueous)` are form- or concentration-qualified source
  strings, not exact synonyms of CHEBI phenol red, but final SSSOM exports the
  latter two in `other`.

## Completeness

- The exact CHEBI mapping and pH-indicator role evidence are complete enough.
- The final synonym surface remains incomplete while solution-qualified labels
  are exported as exact synonyms.

## Recommended Edits

- Major: in `data/ingredients/mapped/Phenol_Red.yaml`, retype or suppress the
  concentration-qualified raw synonyms so they remain occurrence provenance
  only and no longer appear in `mappings/ingredient_mappings.sssom.tsv`;
  rebuild the final SSSOM and rerun `scripts/validate_sssom_invariants.py`.
- Major: confirm whether `(sodium salt)` is still excluded by the current
  synonym policy; if not, retype it so it cannot be exported as an exact
  synonym of the free phenol red form.
