# `data/ingredients/mapped/Thioglycolate.yaml`

## Verdict

Needs curation. The structure, aggregate row, CultureMech reducing-agent role,
and final SSSOM row are synchronized, but the record grounds the ambiguous
source label `Thioglycolate` to the dianion `CHEBI:47869` while its CAS RN
resolves to the monoanion.

## Identity

- Reviewed record: `data/ingredients/mapped/Thioglycolate.yaml`.
- Identifier and grounding: `identifier: CHEBI:47869` with the same
  `ontology_mapping.ontology_id`, label `thioglycolate(2-)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:47869`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `513-66-6`, formula `C2H2O2S`, and InChI/SMILES for
  the thioglycolate dianion.
- Occurrences: seven CultureMech recipe occurrences in seven media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine_pyrophosphate` through `Thiolutin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:47869` with canonical label `thioglycolate(2-)`
  and exact synonym `sulfidoacetate`.
- The CultureMech `REDUCING_AGENT` role is source-backed by the original
  `DATABASE_ENTRY` role text `Reducing Agent`.
- Fresh PubChem lookup by CAS `513-66-6` resolves formula `C2H3O2S-` and the
  monoanionic thioglycolate InChI, not the `C2H2O2S` dianion recorded on
  `CHEBI:47869`.
- Major: the final SSSOM row for `MIM:Thioglycolate` publishes an exact match
  to `CHEBI:47869` and `CAS:513-66-6`, but the CAS RN supports a different
  protonation state than the curated ChEBI target.

## Completeness

- The structure fields, source-backed role, occurrence count, aggregate copy,
  and final SSSOM row are internally synchronized.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, row-review,
  aggregate, and final SSSOM rows. It also found the separate sodium
  thioglycolate salt and thioglycolic-acid records, which do not shadow this
  active record.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thioglycolate.yaml`, inspect the source
  occurrences for whether the intended ingredient is thioglycolate monoanion,
  thioglycolate dianion, a salt, or the acid; then reground the record or
  remove the CAS RN so its ChEBI target, formula, and final SSSOM `other`
  payload agree. Rerun strict validation, term validation, SSSOM publication,
  row review, and `scripts/validate_sssom_invariants.py`.
