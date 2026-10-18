# `data/ingredients/mapped/Acacetin.yaml`

## Verdict

Pass with minor issues. The CAS-backed exact acacetin identity, exact synonym,
chemistry, SSSOM row, and aggregate copy pass; one historic auto-backfill
`changes` string contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/Acacetin.yaml`.
- Identifier and grounding: `identifier: CHEBI:15335` with
  `ontology_mapping.ontology_id: CHEBI:15335`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- CAS `480-44-4` resolves through the ChEBI xref to `CHEBI:15335`,
  `5,7-dihydroxy-4'-methoxyflavone`; the grade correctly records the CAS-RN
  lookup path instead of discarding it as a lexical match.
- The official ChEBI page resolves `CHEBI:15335` to
  `5,7-dihydroxy-4'-methoxyflavone` with formula `C16H12O5`, CAS `480-44-4`,
  and InChIKey `DANYIYRPLHHOCZ-UHFFFAOYSA-N`.
- PubChem maps CAS `480-44-4` to CID `5280442`; its formula and InChIKey agree
  with ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abyssomicin_G.yaml data/ingredients/mapped/Abyssomicin_H.yaml data/ingredients/mapped/Acacetin.yaml data/ingredients/mapped/Aces.yaml data/ingredients/mapped/Acetaldehyde.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acacetin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15335 CHEBI:15343 CHEBI:39060 CHEBI:39061`:
  returned the expected labels, exact synonyms, and related synonyms for
  `CHEBI:15335`, `CHEBI:15343`, `CHEBI:39060`, and `CHEBI:39061`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15335 CHEBI:15343 CHEBI:39060 CHEBI:39061`:
  returned formula and structure metadata for `CHEBI:15335`, `CHEBI:15343`,
  and `CHEBI:39060`; `CHEBI:39061` resolved only as the structureless `ACES`
  class.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT CAS-RN lookup, official ChEBI record, local OAK metadata,
  and PubChem CID all support the exact acacetin identity.
- The stored
  `5,7-dihydroxy-2-(4-methoxyphenyl)-4H-chromen-4-one` synonym is the ChEBI
  exact synonym.
- The SSSOM row maps `MIM:Acacetin` to `CHEBI:15335` with `skos:exactMatch`
  and exports the exact synonym plus `CAS:480-44-4`.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI, but the live `chemical_properties` values are complete and agree with
  ChEBI and PubChem.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copy, SSSOM row, OAK/OLS confirmation row, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No role, component, source occurrence, environmental context, or discussion
  entry needs review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/Acacetin.yaml` so it no longer shows a truncated
  InChI. No identity, chemistry, synonym, or SSSOM edit is required.
