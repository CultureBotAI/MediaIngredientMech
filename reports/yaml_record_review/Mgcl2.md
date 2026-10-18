# `data/ingredients/mapped/Mgcl2.yaml`

## Verdict

Pass. The exact `CHEBI:6636` anhydrous magnesium dichloride identity, CAS,
ChEBI/PubChem structure, CultureMech mineral-source role, occurrence count, and
final SSSOM row pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgcl2.yaml`.
- Identifier and grounding: `identifier: CHEBI:6636` with
  `ontology_mapping.ontology_id: CHEBI:6636`, label `magnesium dichloride`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 291 CultureMech recipe occurrences.
- Chemical identity: CAS `7786-30-3`, formula `2Cl.Mg`, SMILES, and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2` through `Mgcl2_X_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the three CHEBI-primary hydrate records in the same batch.

## Evidence

- EBI OLS4 resolves `CHEBI:6636` as active `magnesium dichloride` with
  `Magnesiumchlorid`, `MgCl2`, and `[MgCl2]` synonyms.
- PubChem resolves CAS `7786-30-3` to CID 5360315 with the same anhydrous
  magnesium dichloride InChI carried in the YAML.
- The OAK/OLS row-review manifest confirmed the `CHEBI:6636` mapping.
- The `MINERAL_SOURCE` role is backed by a CultureMech `DATABASE_ENTRY` whose
  excerpt and curator note both document the original `Mineral source` role.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Mgcl2` to
  `CHEBI:6636`; its `other` tokens are the exact German synonym, `[MgCl2]`,
  and `CAS:7786-30-3`.

## Completeness

- The anhydrous ChEBI target, CAS, structure, CultureMech occurrence count,
  mineral-source role, and final SSSOM synonym export agree.
- Raw CultureMech role/property strings are filtered from final SSSOM `other`.

## Recommended Edits

- None.
