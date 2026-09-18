# `data/ingredients/mapped/Lacto-N-tetraose.yaml`

## Verdict

Needs curation. The CAS-backed CHEBI:30248 identity, CAS RN, PubChem structure,
reviewed synonym, final CHEBI row, and final CAS identity row pass, but the
carbon-source role is still a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Lacto-N-tetraose.yaml`.
- Identifier and grounding: `identifier: cas:14116-68-8` with
  `ontology_mapping.ontology_id: CHEBI:30248`, label
  `beta-D-Gal-(1->3)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `14116-68-8`, PubChem CID `440993`, molecular
  formula `C26H45NO21`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Lacto-N-fucopentaose_II` through `Lactone`: exited 0 and wrote zero ERROR
  rows.
- LinkML term validation was skipped for this CAS-primary record because the
  successful batch check covered only the CHEBI-primary records.

## Evidence

- EBI OLS4 resolves `CHEBI:30248` as active, lists
  `Lacto-N-tetraose` as a related synonym, and lists the same InChI as the YAML
  record.
- PubChem resolves CAS RN `14116-68-8` to CID `440993` with formula
  `C26H45NO21` and the same InChI as the YAML record.
- The final SSSOM publishes one `skos:exactMatch` row to `CHEBI:30248` with the
  reviewed IUPAC synonym and `CAS:14116-68-8`, plus one identity-preserving
  exact row to `cas:14116-68-8`.
- Major: `nutritional_roles.CARBON_SOURCE` is backed only by
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule and
  explicitly says review is recommended.
- The hidden and ignored-inclusive search over `mappings/ingredient_mappings.sssom.tsv`,
  `data`, `src`, `tests`, `reports`, and `docs` found the current final SSSOM
  rows and the adjacent `Lacto-N-neotetraose` record, confirming the identity is
  not conflated with the neotetraose isomer.

## Completeness

- The active CHEBI identity, PubChem-backed CAS RN, formula, structure block,
  aggregate copy, and final SSSOM rows are present and consistent.
- The provisional carbon-source role needs curation before it can be treated as
  a supported role assertion.

## Recommended Edits

- Major: either replace `nutritional_roles.CARBON_SOURCE` in
  `data/ingredients/mapped/Lacto-N-tetraose.yaml` with inspected source evidence
  for exact Lacto-N-tetraose use, or remove the provisional role.
- Sync the aggregate copy and regenerate derived products after the YAML
  changes; rerun strict, product, component, and SSSOM validation.
