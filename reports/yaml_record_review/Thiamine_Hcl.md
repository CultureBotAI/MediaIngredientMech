# `data/ingredients/mapped/Thiamine_Hcl.yaml`

## Verdict

Needs curation. The exact CHEBI identity, CAS RN, structure fields,
source-backed vitamin role, occurrence counts, aggregate row, and final SSSOM
identity pass, but the final SSSOM `other` field still publishes truncated and
context-qualified thiamine-HCl labels.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiamine_Hcl.yaml`.
- Identifier and grounding: `identifier: CHEBI:49105` with the same
  `ontology_mapping.ontology_id`, label `thiamine hydrochloride`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:49105`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `67-03-8`, formula `C12H17N4OS.Cl.HCl`, and
  matching PubChem InChI/SMILES for thiamine hydrochloride.
- Occurrences: 2009 CultureMech recipe occurrences in 1996 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine-hcl_X_2_H2o` through `Thiamine_monophosphate`: exited 0 and wrote
  zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` on the CHEBI subset
  from this batch: `Thiamine-hcl_X_2_H2o`, `Thiamine`, `Thiamine_Hcl`, and
  `Thiamine_monophosphate` all passed. The local `Thiamine_Vitamin_Solution`
  row was skipped because its exact `kgmicrobe.ingredient` ID and close `MICRO`
  parent are outside the CHEBI-focused term-validator subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:49105` with canonical label
  `thiamine hydrochloride`, exact systematic synonyms, and related synonyms for
  thiamine HCl and thiamine dichloride labels.
- Fresh PubChem lookup by CAS `67-03-8` resolves CID 6202, formula
  `C12H18Cl2N4OS`, and the same InChI as the curated record.
- The CultureMech `VITAMIN_SOURCE` role is source-backed by original
  `DATABASE_ENTRY` role text from the CultureMech database.
- Major: the final SSSOM row for `MIM:Thiamine_Hcl` publishes contextual or
  malformed labels in `other`, including `Thiamine HCl (B ) -`,
  `Thiamine HCl (Vitamin B )`, `Thiamine HCl (Vitamin B1)`, and the
  CultureMech `see below` surface. Those are catalog or recipe artifacts, not
  exact synonyms for `CHEBI:49105`.

## Completeness

- The CHEBI identity, CAS RN, structure fields, source-backed role, occurrence
  count, aggregate copy, and final SSSOM row identity agree.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, duplicate
  merge, alias backfill, OAK/OLS row-review, aggregate, and final SSSOM rows.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thiamine_Hcl.yaml`, remove or retype the
  truncated vitamin parentheticals and CultureMech `see below` label so they
  cannot publish as exact `other` values. Then rerun strict validation, SSSOM
  publication, synonym-row review, and `scripts/validate_sssom_invariants.py`.
