# `data/ingredients/mapped/Glycerol_Monostearate.yaml`

## Verdict

Needs curation. The record validates structurally and the ChEBI ID exists, but
the generic `Glycerol monostearate` label, ChEBI `2-stearoylglycerol`
grounding, and PubChem-derived CAS/structure disagree about the acyl position.
The surfactant role is also unsupported computational curation.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycerol_Monostearate.yaml`.
- Identifier and grounding: `identifier: CHEBI:75456` with matching
  `ontology_mapping.ontology_id`, canonical label `2-stearoylglycerol`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `31566-31-1`, formula `C21H42O4`, InChI
  `InChI=1S/C21H42O4/c1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-21(24)25-20(18-22)19-23/h20,22-23H,2-19H2,1H3`,
  and SMILES `CCCCCCCCCCCCCCCCCC(=O)OC(CO)CO`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycerol_Mono-oleate.yaml data/ingredients/mapped/Glycerol_Monostearate.yaml data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Glycine-NaOH_Buffer.yaml data/ingredients/mapped/Glycine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycerol_Monostearate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI synonym match, ChEBI-derived formula/InChI/SMILES, PubChem CAS
  RN, kg-microbe node id, occurrence count, singleton type, and provisional
  surfactant role as the per-record YAML.
- OLS4 resolves `CHEBI:75456` as `2-stearoylglycerol`; its definition is
  specific to the 2-monoglyceride with an octadecanoyl acyl group.
- Major: the record is internally inconsistent. The SSSOM identity row and
  ChEBI-derived structure are for `2-stearoylglycerol`, while PubChem resolves
  CAS `31566-31-1` to `Monostearin` with terminal-ester InChI
  `InChI=1S/C21H42O4/c1-2-3-4-5-6-7-8-9-10-11-12-13-14-15-16-17-21(24)25-19-20(23)18-22/h20,22-23H,2-19H2,1H3`.
  OLS4 also exposes separate 1-monoester and rac-1-monoester ChEBI terms, so
  the terminal ester cannot be treated as exact identity with `CHEBI:75456`.
- Major: OLS4's exact search for `monostearin` finds a generic
  `CHEBI:748837` glyceryl monostearate class as well as a 1-stearoyl child.
  That makes the current exact substitution of the generic MIM subject with the
  2-isomer under-supported even though `glycerol monostearate` is a related
  synonym on `CHEBI:75456`.
- Major: `physicochemical_roles.SURFACTANT` is still backed only by
  `COMPUTATIONAL_PREDICTION` from in-session reasoning and a provisional
  curator note. No inspected CultureMech, database, or literature evidence
  supports that role for this record.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycerol_Monostearate` to `CHEBI:75456` by `skos:exactMatch` and
  exports 2-stearoylglycerol synonyms plus `CAS:31566-31-1` in `other`; the CAS
  token is unsafe until the identity conflict is resolved.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, the final SSSOM row, row-review TSVs,
  the in-session surfactant name list that targeted `CHEBI:75456`, CultureMech
  membership rows, and ignored aggregate backups.

## Completeness

- The record has an ontology row, final SSSOM row, occurrence count, singleton
  type, CAS RN, formula, InChI, SMILES, and ChEBI synonyms.
- The CAS and mapped ChEBI form need reconciliation before this record can
  safely publish an exact mapping or CAS synonym.
- The surfactant role needs claim-level evidence or removal.

## Recommended Edits

- Major: re-curate `data/ingredients/mapped/Glycerol_Monostearate.yaml` against
  the source labels and decide whether the intended substance is generic
  glyceryl monostearate, 1-monostearoylglycerol, rac-1-monostearoylglycerol, or
  2-stearoylglycerol. Then update `identifier`, `ontology_mapping`,
  `chemical_properties`, synonyms, and the final SSSOM row to one consistent
  identity.
- Major: remove `physicochemical_roles.SURFACTANT`, or replace its provisional
  computational evidence with inspected source evidence that specifically
  supports glycerol monostearate functioning as a surfactant in this
  medium-ingredient context.
