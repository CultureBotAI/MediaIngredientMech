# `data/ingredients/mapped/Acetovanillone.yaml`

## Verdict

Pass with minor issues. The CAS-backed exact apocynin identity, exact synonym,
chemistry, SSSOM row, and aggregate copy pass; one historic auto-backfill
`changes` string contains a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetovanillone.yaml`.
- Identifier and grounding: `identifier: CHEBI:2781` with
  `ontology_mapping.ontology_id: CHEBI:2781`, source `CHEBI`,
  `mapping_quality: CAS_RN_LOOKUP`, and `mapping_status: MAPPED`.
- CAS `498-02-2` resolves through the ChEBI xref to `CHEBI:2781` `apocynin`;
  the grade correctly records the CAS-RN lookup path instead of discarding it
  as a lexical match.
- The official ChEBI page resolves `CHEBI:2781` to `apocynin` with formula
  `C9H10O3`, CAS `498-02-2`, and InChIKey
  `DFYRUELUNQRZTB-UHFFFAOYSA-N`.
- PubChem maps CAS `498-02-2` to CID `2214`; its formula and InChIKey agree
  with ChEBI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetoin.yaml data/ingredients/mapped/Acetomycin.yaml data/ingredients/mapped/Acetone.yaml data/ingredients/mapped/Acetosyringone.yaml data/ingredients/mapped/Acetovanillone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetovanillone.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15688 CHEBI:209246 CHEBI:15347 CHEBI:2404 CHEBI:2781`:
  returned the expected ChEBI labels and synonyms for all five target ChEBI
  identifiers.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15688 CHEBI:209246 CHEBI:15347 CHEBI:2404 CHEBI:2781`:
  returned formula and structure metadata for all five target ChEBI identifiers.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The CultureBotHT CAS-RN lookup, official ChEBI record, local OAK metadata,
  and PubChem CID all support the exact `CHEBI:2781` apocynin identity.
- The stored
  `1-(4-hydroxy-3-methoxyphenyl)ethan-1-one` synonym is the ChEBI exact
  synonym for the same compound, and `Acetovanillone` is a ChEBI related
  synonym on the same term.
- The SSSOM row maps `MIM:Acetovanillone` to `CHEBI:2781` with
  `skos:exactMatch` and exports the exact synonym plus `CAS:498-02-2`.
- The `AUTO_BACKFILL_CHEBI_CHEMISTRY` event's `changes` string truncates the
  InChI, but the live `chemical_properties` values are complete and agree with
  ChEBI and PubChem.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copy, SSSOM row, OAK/OLS confirmation row, regrade history, and
  ignored aggregate backups.

## Completeness

- CAS, formula, InChI, SMILES, the exact ChEBI synonym, and `ingredient_type`
  are populated.
- No role, component, source occurrence, environmental context, or discussion
  entry needs review.

## Recommended Edits

- Optionally clarify the stale
  `curation_history[AUTO_BACKFILL_CHEBI_CHEMISTRY].changes` string in
  `data/ingredients/mapped/Acetovanillone.yaml` so it no longer shows a
  truncated InChI. No identity, chemistry, synonym, or SSSOM edit is required.
