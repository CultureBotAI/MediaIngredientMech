# `data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml`

## Verdict

Pass. The CAS fallback identity remains intentional, no fresh exact CHEBI or
NCIT replacement was found, PubChem confirms the retained structure for the CAS
RN, and the final SSSOM CAS registry row is internally consistent.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml`.
- Identifier and grounding: `identifier: cas:20846-91-7` with matching
  `ontology_mapping.ontology_id`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, `mapping_status: MAPPED`, exact
  synonym `EDDS`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `20846-91-7` resolved to CID 497266 with formula
  `C10H16N2O8` and the same InChI recorded under `chemical_properties`.
- Fresh exact OLS4 searches against CHEBI and NCIT for both `20846-91-7` and
  `Ethylenediamine-N,N'-disuccinic acid` returned 0 documents, so the local
  CAS fallback has no exact external ontology term to promote to today.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ethyl_Decanoate.yaml data/ingredients/mapped/Ethyl_Methyl_Sulfide.yaml data/ingredients/mapped/Ethyl_octanoate.yaml data/ingredients/mapped/Ethylene_Glycol.yaml data/ingredients/mapped/Ethylenediamine-NN-disuccinic_Acid.yaml --out /tmp/mim_ethyl_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the `cas:` registry prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS identifier, CAS RN, PubChem CID, formula, InChI, SMILES, `EDDS` synonym,
  and fallback-registry history as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Ethylenediamine-NN-disuccinic_Acid` to `cas:20846-91-7` with
  `skos:exactMatch`, `object_source: registry:cas`, `EDDS`, and the same
  `CAS:20846-91-7` token in `other`.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` records
  `expected_registry_identifier` for this row because CAS registry CURIEs are
  not OAK/OLS ontology terms.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Ethylenediamine-NN-disuccinic_Acid`, `cas:20846-91-7`, `20846-91-7`,
  and `497266` found the active YAML, aggregate copy, final SSSOM row,
  expected UNKNOWN_TERM triage row, and ignored aggregate backups; it did not
  expose a contradictory active mapping.

## Completeness

- The CAS identity, CAS RN, PubChem CID, structure fields, EDDS synonym, and
  final SSSOM row are populated.
- Roles, components, source occurrences, and environmental contexts are
  correctly empty.

## Recommended Edits

- None.
