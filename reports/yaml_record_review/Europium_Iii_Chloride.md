# `data/ingredients/mapped/Europium_Iii_Chloride.yaml`

## Verdict

Pass. The CultureBotHT CAS fallback identifies anhydrous europium(III)
chloride, PubChem confirms the recorded `Cl3Eu` structure for that CAS RN,
and no exact CHEBI or NCIT replacement term was found.

## Identity

- Reviewed record: `data/ingredients/mapped/Europium_Iii_Chloride.yaml`.
- Identifier and grounding: `identifier: cas:10025-76-0` with matching
  `ontology_mapping.ontology_id`, canonical label `Europium(III) chloride`,
  source `CAS`, `mapping_quality: FALLBACK_REGISTRY`, `mapping_status:
  MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `10025-76-0` resolved to CID 24809 with formula
  `Cl3Eu` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Eugon_agar_BD-Difco.yaml data/ingredients/mapped/Euphol.yaml data/ingredients/mapped/Eurocidin.yaml data/ingredients/mapped/Europium_Iii_Chloride.yaml data/ingredients/mapped/Exfoliatin.yaml --out /tmp/mim_eug_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- Engine A term validation was skipped for this record because the ontology ID
  uses the local `cas` registry prefix rather than an OBO prefix.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  CAS identifier, exact synonym, CAS RN, formula, InChI, SMILES, and PubChem
  CID as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Europium_Iii_Chloride` to `cas:10025-76-0` with `skos:exactMatch`;
  both exported `other` tokens, `europium chloride` and `CAS:10025-76-0`,
  denote the same anhydrous compound.
- A fresh exact OLS4 search by CAS RN against CHEBI and NCIT returned no
  documents, so the existing CAS fallback is still the best available
  grounding among the reviewed targets.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for
  `MIM:Europium_Iii_Chloride`, `cas:10025-76-0`, and `10025-76-0` found the
  active YAML, aggregate copy, final SSSOM row, and ignored aggregate backups;
  it did not expose a contradictory active mapping.

## Completeness

- The CAS fallback identity, CAS RN, structure fields, exact synonym, PubChem
  CID, and final SSSOM payload are populated.
- No unsupported roles, components, source occurrences, or environmental
  contexts are asserted.

## Recommended Edits

- None.
