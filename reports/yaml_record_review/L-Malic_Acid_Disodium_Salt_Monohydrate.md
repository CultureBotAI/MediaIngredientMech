# `data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml`

## Verdict

Needs curation. The CAS primary identity, NCIT parent mapping, hydrate review,
and final exact CAS and KG-Microbe identity rows are consistent, but the
structure fields still describe the wrong PubChem compound and the carbon and
energy roles are only provisional computational assertions.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:207511-06-6` with
  `ontology_mapping.ontology_id: NCIT:C80654`, label `Malic Acid`, source
  `NCIT`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `207511-06-6`, molecular formula `C4H4NaO5-`,
  InChI, SMILES, and PubChem CID `197014`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/L-Homoserine.yaml data/ingredients/mapped/L-Malic_Acid.yaml data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Meta-tyrosine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `NCIT:C80654` as active `Malic Acid`, supporting the broad
  NCIT parent mapping for the exact CAS hydrate identity.
- PubChem resolves CAS RN `207511-06-6` to disodium monohydrate entries with
  formula `C4H6Na2O6`; those entries have two sodium atoms and one water,
  matching the supplied label.
- `mappings/hydrate_review.tsv` records the CAS identity as hydrate-specific
  for L-malic acid disodium salt monohydrate, and
  `reports/hydrate_grounding.tsv` reports `OK_OWN_CAS_ID`.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `NCIT:C80654`, exact CAS and `kgmicrobe.compound` rows, no parent-row
  `other` tokens, and only `CAS:207511-06-6` on the exact identity rows.
- Major: `chemical_properties.pubchem_cid: 197014`, formula `C4H4NaO5-`,
  SMILES `C(C(C(=O)[O-])O)C(=O)[O-].[Na+]`, and the InChI do not describe
  disodium L-malate monohydrate. They have one sodium, no hydrate water, and
  disagree with the exact PubChem records for CAS RN `207511-06-6`.
- Major: `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` have only `COMPUTATIONAL_PREDICTION`
  evidence from a curated name-pattern rule and paired carbon-source inference,
  with no inspected CultureMech, FEBA, Hans80, or literature evidence attached
  to either role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, aggregate copy, stale
  structure values in generated docs, final SSSOM rows, hydrate review rows,
  hydrate-grounding rows, and unknown-term triage rows.

## Completeness

- The CAS primary identifier, NCIT parent mapping, exact CAS and local registry
  rows, hydrate review, empty occurrence count, and aggregate copy are present
  and consistent.
- The chemical structure block is incomplete until it is regenerated for the
  exact disodium monohydrate.
- The record is incomplete until the carbon-source and energy-source roles are
  either supported by inspected claim-level evidence or removed.

## Recommended Edits

- Major: replace `chemical_properties.pubchem_cid`, `molecular_formula`,
  `smiles`, and `inchi` in
  `data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml` with
  values from a PubChem record that actually resolves CAS RN `207511-06-6`.
- Major: remove `nutritional_roles.CARBON_SOURCE` and
  `nutritional_roles.ENERGY_SOURCE` unless inspected CultureMech, FEBA, Hans80,
  or literature sources can support L-malic acid disodium salt monohydrate as a
  carbon and energy source.
- Rerun strict, term, hydrate, round-trip, role, component, and SSSOM validation
  after those changes.
