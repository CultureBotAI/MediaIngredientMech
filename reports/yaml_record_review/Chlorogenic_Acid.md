# `data/ingredients/mapped/Chlorogenic_Acid.yaml`

## Verdict

Needs curation; major issue. The CultureBotHT chlorogenic acid identity is
correctly grounded to active `CHEBI:16112`, and its CAS, formula, InChI,
SMILES, SSSOM row, zero occurrence count, and aggregate copy agree, but one
upstream ChEBI IUPAC string beginning `edit(` is retained and exported as a
resolving exact synonym.

## Identity

- Reviewed record: `data/ingredients/mapped/Chlorogenic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16112`,
  `ontology_mapping.ontology_id: CHEBI:16112`,
  `ontology_label: chlorogenic acid`, `ontology_source: CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Direct ChEBI and exact OLS lookups for `CHEBI:16112` return one active term
  labelled `chlorogenic acid`. ChEBI publishes CAS `327-97-9`, formula
  `C16H18O9`, mass `354.311`, the same SMILES, and the same standard InChI
  stored in `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlororaphin.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Chloridazon.yaml data/ingredients/mapped/Chlorogenic_Acid.yaml data/ingredients/mapped/Chlorpromazine_Hydrochloride.yaml data/ingredients/mapped/Chlortetracycline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 4 CHEBI-grounded records in this batch. `Chlororaphin` was
  intentionally skipped because its `kgmicrobe.compound` placeholder CURIE is a
  local registry ID outside Engine A's OBO prefix scope.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip.wqYt47`
  followed by
  `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip.wqYt47`:
  passed; both curated collection files had 0 data differences and only the
  expected scratch `generation_date` metadata differences.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K. Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- Hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `reports` found the active exact `MIM:Chlorogenic_Acid` SSSOM row, the
  `CONFIRMED` row-review disposition, and matching aggregate and docs rows for
  `CHEBI:16112`.
- ChEBI and OLS both show the `edit(1S,3R,4R,5R)-...` IUPAC string on
  `CHEBI:16112`, so the row came from ChEBI exact-synonym enrichment rather
  than a local misspelling. It is still malformed as a chemical name and is
  currently exported in `mappings/ingredient_mappings.sssom.tsv`,
  `docs/data/label_index.csv`, and the docs JSON/CSV ingredient exports as a
  resolving synonym.
- PubChem lookup of CAS `327-97-9` returned the same formula and InChI as
  ChEBI/MIM.
- Hidden/ignored-inclusive search of `mappings/culturemech_recipe_membership.tsv`
  plus `data` found no CultureMech membership rows for `CHEBI:16112`, matching
  the explicit 0/0 `occurrence_statistics`.
- The record carries no role, component, or environment claims.

## Completeness

- The exact ChEBI identifier, CAS, formula, InChI, SMILES, SSSOM row,
  aggregate copy, docs row, and zero occurrence count are populated and agree.
- The only consequential gap is the resolving malformed synonym inherited from
  ChEBI.

## Recommended Edits

- Major: remove the malformed `edit(1S,3R,4R,5R)-...` synonym from
  `data/ingredients/mapped/Chlorogenic_Acid.yaml` or retain it only as a
  non-resolving `REJECTED_LABEL`.
- Major: update `scripts/apply_synonym_review.py` with a deterministic skip for
  this upstream ChEBI synonym or for the `edit(` malformed IUPAC pattern before
  rerunning exact-synonym enrichment, otherwise the bad ChEBI string will be
  re-added.
- Regenerate synchronized outputs and rerun strict validation, SSSOM QC,
  aggregate roundtrip, flat-export coverage, and `git diff --check`.
