# `data/ingredients/mapped/Mgcl2_X_H2o.yaml`

## Verdict

Needs curation. The exact `CHEBI:86355` magnesium dichloride monohydrate
identity, CAS, ChEBI/PubChem structure, hydrate grounding audit, occurrence
count, and final SSSOM row pass, but `MINERAL_SOURCE` is still a provisional
name-list role with only `COMPUTATIONAL_PREDICTION` evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgcl2_X_H2o.yaml`.
- Identifier and grounding: `identifier: CHEBI:86355` with
  `ontology_mapping.ontology_id: CHEBI:86355`, label
  `magnesium dichloride monohydrate`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: five CultureMech recipe occurrences.
- Chemical identity: CAS `22756-14-5`, formula `2Cl.H2O.Mg`, SMILES, and
  InChI.
- Role: one `nutritional_roles` entry, `MINERAL_SOURCE`, inferred by
  `infer_roles_from_name_lists` as a curated name-pattern rule.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2` through `Mgcl2_X_H2o`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-primary
  record and the three other CHEBI-primary records in the same batch.

## Evidence

- EBI OLS4 resolves `CHEBI:86355` as active
  `magnesium dichloride monohydrate` with `MgCl2.H2O`,
  `Magnesium chloride, monohydrate`, and
  `magnesium dichloride--water (1/1)` synonyms.
- PubChem resolves CAS `22756-14-5` to CID 168060 with formula `Cl2H2MgO` and
  the same one-water InChI carried in the YAML.
- `reports/hydrate_grounding.tsv` marks this row `OK_HYDRATE_TERM`, and
  `mappings/hydrate_review.tsv` records that its CAS, ChEBI term, and formula
  consistently identify magnesium chloride monohydrate.
- The OAK/OLS row-review manifest confirmed the `CHEBI:86355` mapping.
- The final SSSOM publishes one `skos:exactMatch` row from
  `MIM:Mgcl2_X_H2o` to `CHEBI:86355`; its `other` tokens are exact
  monohydrate synonyms plus `CAS:22756-14-5`.

## Completeness

- The chemical identity, CAS, active ChEBI target, hydrate count, and final
  SSSOM synonym export agree.
- The `MINERAL_SOURCE` role is not backed by recipe-specific or imported
  database evidence. The only role evidence says it was inferred from a curated
  media-role name pattern and is provisional.

## Recommended Edits

- Major: replace the provisional `MINERAL_SOURCE` role with a CultureMech
  `DATABASE_ENTRY` role assertion if this ingredient was imported with a
  mineral-source role, or remove the role facet from
  `data/ingredients/mapped/Mgcl2_X_H2o.yaml`.
