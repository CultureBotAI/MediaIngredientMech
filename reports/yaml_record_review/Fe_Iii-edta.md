# `data/ingredients/mapped/Fe_Iii-edta.yaml`

## Verdict

Needs curation, with major role-evidence and final-SSSOM synonym issues. The
ChEBI ferric EDTA identity, CAS-backed structure, and core synonyms pass, but
the record still exports a role-prefixed kg-microbe string and a concentration
surface as exact `other` synonyms, and its `TRACE_ELEMENT` role is still only
provisional.

## Identity

- Reviewed record: `data/ingredients/mapped/Fe_Iii-edta.yaml`.
- Identifier and grounding: `identifier: CHEBI:30729` with matching
  `ontology_mapping.ontology_id`, canonical label
  `ethylenediaminetetraacetatoferrate(1-)`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- PubChem lookup by CAS RN `15275-07-7` resolved to CID 197149 with formula
  `C10H12FeN2O8-` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fastidious_Anaerobe_Broth_With_Meat_Granules.yaml data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml --out /tmp/mim_fe_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Fatty_Acid_Mixture_See_Medium_No_266.yaml data/ingredients/mapped/Fe4_Po42.yaml data/ingredients/mapped/Fe_Iii-edta.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the CHEBI-primary subset in this mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, exact synonyms, merged
  unmapped duplicate history, `TRACE_ELEMENT` role, and refreshed occurrence
  counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Fe_Iii-edta` to `CHEBI:30729` with `skos:exactMatch`.
- The core `Ferric EDTA`, `Iron(III)-edta`,
  `(ethane-1,2-diyldinitrilo)tetraacetatoferrate(1-)`,
  `(ethane-1,2-diyldinitrilo)tetraacetatoferrate(III)`,
  `ethylenediaminetetraacetatoferrate`, CAS, and punctuation-only Fe/EDTA
  variants in final SSSOM `other` are acceptable exact surface forms.
- Major: the final SSSOM `other` column also exports
  `electron acceptor: ethylenediaminetetraacetatoferrate`, which is a
  role-prefixed source string, and `Fe(III)-EDTA (0.66% [wt/vol] in water)`,
  which is a concentration-specific preparation rather than a synonym of the
  compound.
- Major: `nutritional_roles.TRACE_ELEMENT` is supported only by a
  `COMPUTATIONAL_PREDICTION` reference from an in-session LLM assignment, and
  that evidence explicitly describes the assertion as provisional.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fe_Iii-edta`,
  `CHEBI:30729`, `15275-07-7`, and Fe-EDTA labels found the active YAML,
  aggregate copy, final SSSOM row, row-review provenance, CultureMech residual
  alias rows, an already rejected underspecified `Iron-EDTA` tombstone,
  CultureMech recipe memberships, and ignored aggregate backups.

## Completeness

- The Fe(III)-EDTA identity, CAS RN, structure fields, accepted exact synonyms,
  occurrence counts, ingredient type, and final SSSOM row are populated.
- The final SSSOM synonym payload and provisional nutritional role need
  curator cleanup.

## Recommended Edits

- Major: remove or filter role-prefixed and concentration-specific strings from
  exact final SSSOM `other` export.
- Major: either replace the provisional `TRACE_ELEMENT` inference with
  source-backed evidence or remove the role facet.
- Sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
