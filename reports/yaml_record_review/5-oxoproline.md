# `data/ingredients/mapped/5-oxoproline.yaml`

## Verdict

Pass, none. The exact `CHEBI:16010` identity, microbedecoder provenance,
chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/5-oxoproline.yaml`.
- Identifier and grounding: `identifier: CHEBI:16010` with
  `ontology_mapping.ontology_id: CHEBI:16010`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:16010` to `5-oxoproline` with
  formula `C5H7NO3`, the stored SMILES, and the stored InChI.
- Local OAK metadata reports the same label, formula, structure strings, and
  mass for `CHEBI:16010`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-deoxy-5-_Methylthioadenosine.yaml data/ingredients/mapped/5-didehydro-D-gluconic_Acid.yaml data/ingredients/mapped/5-fluorouracil.yaml data/ingredients/mapped/5-methyluridine.yaml data/ingredients/mapped/5-oxoproline.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-oxoproline.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the official exact and related synonym set for `CHEBI:16010`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:17509 CHEBI:18281 CHEBI:46345 CHEBI:45996 CHEBI:16010`:
  returned the expected ChEBI formula, structure strings, and mass for
  `CHEBI:16010`.

## Evidence

- The active ChEBI term, formula, SMILES, InChI, and exact label support the
  5-oxoproline identity imported from `kgmicrobe.trait:5_oxoproline`.
- The source occurrence count is traceable to
  `data/custom/microbedecoder/unmapped_labels.tsv`, where
  `kgmicrobe.trait:5_oxoproline` appears in `BacDive_Metabolite_utilization`
  with count 5.
- The SSSOM row maps `MIM:5-oxoproline` to `CHEBI:16010` with
  `skos:exactMatch`, `semapv:LexicalMatching`, and the expected manual
  `review-ingredients` provenance.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, microbedecoder source row, stale advisory rows, one downstream
  L-pyroglutamic acid 2-naphthylamide note that names pyroglutamate as
  5-oxoproline, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence count, and
  `ingredient_type` are populated.
- No CAS, roles, components, environmental context, or discussion entries are
  required for this record.

## Recommended Edits

No YAML edit is required for this record.
