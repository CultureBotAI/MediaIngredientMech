# `data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml`

## Verdict

Needs curation - major. The CAS-backed `CHEBI:32158` identity, sulfate salt
formula, occurrence count, and final SSSOM row pass, but `SELECTIVE_AGENT` is
still only a provisional name-pattern role.

## Identity

- Reviewed record: `data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml`.
- Identifier and grounding: `identifier: CHEBI:32158` with
  `ontology_mapping.ontology_id: CHEBI:32158`, label `streptomycin sulfate`,
  source `CHEBI`, `mapping_quality: CAS_RN_LOOKUP`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `3810-74-0`, formula `2C21H39N7O12.3H2O4S`, and
  ChEBI-derived InChI/SMILES for the salt.
- Occurrences: 3 occurrences across 3 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Streptomycin_Sulfate_Salt` through `Suberic_Acid`: exited 0 and wrote zero
  ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:32158` with label
  `streptomycin sulfate`, xref `cas:3810-74-0`, formula
  `2C21H39N7O12.3H2O4S`, and structure fields matching the YAML.
- PubChem resolves CAS `3810-74-0` to the same salt formula and InChI, so the
  stored CAS-RN still supports the ChEBI salt target.
- `mappings/culturemech_recipe_membership.tsv` has the three expected
  `CHEBI:32158` recipe rows, agreeing with `total_occurrences: 3` and
  `media_count: 3`.
- The final SSSOM row exact-matches `CHEBI:32158` and publishes only
  `CAS:3810-74-0` in `other`, which is a true CAS label for the same subject.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note.

## Completeness

- The exact salt identity, CAS, chemical properties, aggregate row, occurrence
  count, and final SSSOM row agree.
- An ignored/hidden search of local curated, mapping, generated, report, source,
  and documentation paths found the expected rows for this record and no
  second active MIM record for this exact salt identity.
- No unsupported active synonym, component, or final SSSOM `other` payload was
  found; the only unsupported claim is the provisional selective-agent role.

## Recommended Edits

- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` from
  `data/ingredients/mapped/Streptomycin_Sulfate_Salt.yaml`, or replace the
  name-pattern evidence with an inspected source showing that streptomycin
  sulfate is acting as a selective agent in a culture medium.
