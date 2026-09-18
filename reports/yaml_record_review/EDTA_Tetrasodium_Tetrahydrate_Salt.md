# `data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml`

## Verdict

Needs curation. The CAS identity and tetrasodium tetrahydrate chemistry are
internally consistent, and the CAS registry identity row is correct, but the
record still carries a provisional chelator role and publishes generic/free
EDTA labels as synonyms of the tetrahydrate salt.

## Identity

- Reviewed record:
  `data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml`.
- Identifier and grounding: `identifier: cas:13235-36-4`,
  `ontology_mapping.ontology_id: CHEBI:4735`,
  `ontology_mapping.ontology_label: ethylenediaminetetraacetic acid`,
  `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved the parent `CHEBI:4735` to
  `ethylenediaminetetraacetic acid`.
- PubChem resolved CAS RN `13235-36-4` to CID 23287279 with formula
  `C10H20N2Na4O12` and the same four-water/four-sodium InChI and SMILES
  recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/E-Amino-N-Caproic_Acid.yaml data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml data/ingredients/mapped/E_4_Aminostyryl_Acetate.yaml data/ingredients/mapped/Ebselen.yaml data/ingredients/mapped/Econazole_Nitrate_Salt.yaml --out /tmp/mim_e_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- The LinkML term-label gate was skipped for this file because its identifier
  uses the local CAS registry prefix that the justfile excludes from Engine A.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS identifier, parent ChEBI close mapping, PubChem CID, formula, structure,
  and provisional `CHELATOR` role as the per-record YAML.
- The final SSSOM CAS identity row maps
  `MIM:EDTA_Tetrasodium_Tetrahydrate_Salt` to `cas:13235-36-4` with
  `skos:exactMatch`, `registry:cas`, and only `CAS:13235-36-4` in `other`;
  that row preserves the exact local identity.
- The final SSSOM parent row maps the same subject to anhydrous
  `CHEBI:4735` with `skos:closeMatch`, which preserves non-identity, but its
  `other` column also publishes `EDTA` and
  `Ethylenediamintetraacetic acid (EDTA)`. Those are generic/free-acid labels,
  not tetrasodium tetrahydrate salt synonyms.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` found the active CAS record, the matching final
  SSSOM rows, and the `other_cross_record_baseline.tsv` entry that already
  marks `EDTA` on this MIM subject as a hydrate-family issue.
- The only `CHELATOR` role evidence is
  `reference_type: COMPUTATIONAL_PREDICTION` from
  `infer_roles_from_name_lists`, with a curator note explicitly marking the
  name-pattern role provisional.

## Completeness

- The CAS RN, PubChem CID, hydrate formula, hydrate/salt SMILES, and hydrate
  InChI describe CAS `13235-36-4` rather than the anhydrous acid parent.
- The three CultureMech recipe occurrences are represented in
  `mappings/culturemech_recipe_membership.tsv` for the same CAS identity.

## Recommended Edits

- Major: remove `EDTA` and `Ethylenediamintetraacetic acid (EDTA)` from the
  active same-subject synonym surface for
  `data/ingredients/mapped/EDTA_Tetrasodium_Tetrahydrate_Salt.yaml`, or mark
  them as rejected/provenance-only so the final SSSOM parent row no longer
  exports them in `other`.
- Major: either replace the provisional `physicochemical_roles.CHELATOR`
  evidence with claim-level support for EDTA tetrasodium tetrahydrate salt, or
  remove the role until a supported role can be curated.
- After editing the per-record YAML, run `sync-curated`, rebuild or reconcile
  the SSSOM from the maintained source, and rerun `validate-all`, `qc-sssom`,
  `validate_component_partonomy.py`, and the strict validator.
