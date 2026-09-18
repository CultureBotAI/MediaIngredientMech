# `data/ingredients/mapped/Mgcl2_X_7_H2o.yaml`

## Verdict

Needs curation. The unresolved local heptahydrate identity, close anhydrous
ChEBI parent row, exact kg-microbe registry row, rejected wrong-hydrate labels,
cleared unverified CAS/structure, and final SSSOM rows pass, but
`MINERAL_SOURCE` is still a provisional name-list role with only
`COMPUTATIONAL_PREDICTION` evidence.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Mgcl2_X_7_H2o.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:mgcl2_x_7_h2o`
  with `ontology_mapping.ontology_id: CHEBI:6636`, label
  `magnesium dichloride`, source `CHEBI`, `mapping_quality: CLOSE_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: 19 CultureMech recipe occurrences.
- Chemical identity: the unverified CAS and anhydrous structure were cleared;
  the record intentionally has an empty `chemical_properties` block.
- Role: one `nutritional_roles` entry, `MINERAL_SOURCE`, inferred by
  `infer_roles_from_name_lists` as a curated name-pattern rule.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mgcl2` through `Mgcl2_X_H2o`: exited 0 and wrote zero ERROR rows.
- Direct Engine A term validation was skipped for this local registry record
  because its primary `kgmicrobe.compound` identifier is outside the OBO subset
  used for the batch.

## Evidence

- EBI OLS4 exact search found mono-, di-, and hexa-hydrate ChEBI terms for
  magnesium dichloride but no magnesium dichloride heptahydrate term.
- `reports/hydrate_grounding.tsv` marks this row `OK_LOCAL_REGISTRY_ID`.
- `mappings/hydrate_review.tsv` keeps `mediadive.compound:632` as an
  unresolved local source identity, retains `CHEBI:6636` only as the closest
  anhydrous parent, and publishes no exact formula, CAS, InChI, or SMILES for
  the heptahydrate label.
- The final SSSOM publishes a `skos:closeMatch` parent row to `CHEBI:6636` and
  an exact `kgmicrobe.compound:mgcl2_x_7_h2o` registry row.
- The final `other` tokens are limited to MgCl2 7-water labels retained for
  this local subject; the rejected anhydrous, 6-water, 76-water, and
  nonbreaking-space 6-water labels do not publish.

## Completeness

- The local registry identifier and exact companion row preserve the unresolved
  source label without collapsing it into anhydrous `CHEBI:6636`.
- The `MINERAL_SOURCE` role is not backed by recipe-specific or imported
  database evidence. The only role evidence says it was inferred from a curated
  media-role name pattern and is provisional.

## Recommended Edits

- Major: replace the provisional `MINERAL_SOURCE` role with a supported role
  assertion if this local source identity was imported with a mineral-source
  role, or remove the role facet from
  `data/ingredients/mapped/Mgcl2_X_7_H2o.yaml`.
