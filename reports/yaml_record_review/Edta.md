# `data/ingredients/mapped/Edta.yaml`

## Verdict

Needs curation. The main EDTA identity now correctly maps plain EDTA to the
free-acid ChEBI term, but old `CHEBI:64755` chemical properties and synonyms
survived the regrounding, and the chelator role is still provisional
name-pattern output.

## Identity

- Reviewed record: `data/ingredients/mapped/Edta.yaml`.
- Identifier and grounding: `identifier: CHEBI:4735` with matching
  `ontology_mapping.ontology_id`, canonical label
  `ethylenediaminetetraacetic acid`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:4735`, 569 total CultureMech occurrences across
  568 media, and `ingredient_type: SINGLE_INGREDIENT`.
- `runoak -i ols:chebi info` resolved `CHEBI:4735` to
  `ethylenediaminetetraacetic acid`.
- EBI OLS lists `EDTA` and `EDTA (chelating agent)` as related synonyms for
  `CHEBI:4735`, supporting the repaired free-acid identity and the prior
  duplicate merge from `EDTA (acid form)`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Ectoine.yaml data/ingredients/mapped/Edta.yaml data/ingredients/mapped/Edta_Acid_Form.yaml data/ingredients/mapped/Edta_Chelating_Agent.yaml data/ingredients/mapped/Edta_Stock.yaml --out /tmp/mim_edta_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Edta.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  repaired `CHEBI:4735` identifier, preferred term, synonyms, CAS RN, stale
  formula/structure, kg-microbe node id, occurrence counts, and provisional
  `CHELATOR` role as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Edta` to
  `CHEBI:4735` with `skos:exactMatch`, the canonical ChEBI object label, and
  `CAS:60-00-4`; the CAS token belongs to EDTA.
- The two final SSSOM `other` tokens
  `2,2',2'',2'''-(ethane-1,2-diyldiammonio)tetraacetate` and
  `2,2',2'',2'''-(ethane-1,2-diyldiazaniumyl)tetraacetate` are stale
  `CHEBI:64755` labels. Fresh exact ChEBI OLS searches resolve them to
  `CHEBI:64755` `EDTA(2-)` and related salt terms, not to `CHEBI:4735`.
- PubChem resolves CAS RN `60-00-4` to neutral EDTA formula `C10H16N2O8` and a
  neutral EDTA InChI, while the record still stores formula `C10H14N2O8` and
  an InChI ending in `/p-2` from the old deprotonated `CHEBI:64755` identity.
- A hidden/ignored-inclusive search over `data/ingredients`, `mappings`, and
  `reports/yaml_record_review` found the active YAML, aggregate copy, final
  SSSOM row, `other_cross_record_baseline.tsv` row for the merged
  `EDTA (acid form)` surface, and expected EDTA family records; it confirmed
  the stale `CHEBI:64755` labels occur on the active `Edta` surfaces.
- The only `CHELATOR` role evidence is
  `reference_type: COMPUTATIONAL_PREDICTION` from
  `infer_roles_from_name_lists`, with a curator note explicitly marking the
  name-pattern role provisional.

## Completeness

- The ChEBI identifier, preferred term, synonym-match grade, CAS RN,
  `kg_microbe_node_id`, occurrence count, and duplicate-merge history are
  populated.
- Raw `Properties:` aliases remain in YAML, but the final SSSOM builder filters
  them and they do not leak into `other`.

## Recommended Edits

- Major: in `data/ingredients/mapped/Edta.yaml`, replace the stale
  `CHEBI:64755` formula, InChI, and SMILES with properties for free-acid
  `CHEBI:4735` / CAS `60-00-4`.
- Major: remove the two old `CHEBI:64755` exact synonyms from the active EDTA
  synonym surface, or reclassify them as rejected/provenance-only so the final
  SSSOM `other` column for `MIM:Edta` no longer exports them.
- Major: either replace the provisional `physicochemical_roles.CHELATOR`
  evidence with claim-level support for EDTA in MIM media, or remove the role.
- After editing the per-record YAML, run `sync-curated`, rebuild SSSOM if
  synonyms changed, and rerun `validate-all`, `qc-sssom`, strict validation,
  and id-label correspondence.
