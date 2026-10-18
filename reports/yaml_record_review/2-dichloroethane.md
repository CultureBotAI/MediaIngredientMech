# `data/ingredients/mapped/2-dichloroethane.yaml`

## Verdict

Needs curation, minor. The active `CHEBI:27789` identity and locant repair pass,
but the top-level `notes` field still describes the obsolete unmapped importer
state.

## Identity

- Reviewed record: `data/ingredients/mapped/2-dichloroethane.yaml`.
- Identifier and grounding: `identifier: CHEBI:27789` with
  `ontology_mapping.ontology_id: CHEBI:27789`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:27789`
  resolves to `1,2-dichloroethane`, lists CAS `107-06-2`, formula `C2H4Cl2`,
  and SMILES `ClCCCl`.
- The 2026-08-08 `apply_locant_corrections` event documents why the impossible
  raw source label `2-dichloroethane` was repaired to `1,2-dichloroethane`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-deoxyinosine.yaml data/ingredients/mapped/2-deoxythymidine-5-4-nitrophenyl_Phosphate.yaml data/ingredients/mapped/2-deoxyuridine.yaml data/ingredients/mapped/2-dichloroethane.yaml data/ingredients/mapped/2-dimethylsuccinic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/2-dichloroethane.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:2-dichloroethane` to `CHEBI:27789` row.

## Evidence

- The active ChEBI target confirms the repaired `1,2-dichloroethane` identity,
  CAS RN, formula, and SMILES.
- The raw `2-dichloroethane` text is retained only as a `RAW_TEXT`
  microbedecoder synonym, preserving provenance without asserting it as an
  accepted exact synonym.
- Stale: top-level `notes` still say there was no CAS-RN or CHEBI/NCIT match
  and curator review was needed, even though the record was promoted on
  2026-08-04 and locant-corrected on 2026-08-08.
- Non-blocking audit nit: `curation_history` is not timestamp-monotonic; the
  2026-08-04T00:00 promotion precedes the 2026-08-04T02:54 import event.
- The hidden/ignored-inclusive search over `data`, `mappings`, and `reports`
  found the active YAML/aggregate/SSSOM rows and stale advisory rows, with no
  live contradiction of the active `CHEBI:27789` identity.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Formula, InChI, SMILES, and molecular weight are populated for the active
  chemical form.
- The official CAS RN could be added later, but its absence does not make the
  current ChEBI grounding ambiguous.

## Recommended Edits

1. In `data/ingredients/mapped/2-dichloroethane.yaml`, replace the stale `notes`
   text with a concise statement that the microbedecoder dropped-locant artifact
   was resolved to `CHEBI:27789` and corrected to `1,2-dichloroethane`.
2. Run `just sync-curated`, `just validate-strict
   data/ingredients/mapped/2-dichloroethane.yaml`, `just validate-terms
   data/ingredients/mapped/2-dichloroethane.yaml`, `just qc-sssom`, and
   `just qc-flat-coverage` after that curation edit.
