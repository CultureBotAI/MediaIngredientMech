# `data/ingredients/mapped/4-nitrophenyl_Alpha-D-galactoside.yaml`

## Verdict

Pass, none. The restored `CHEBI:546840` alpha-D-galactoside identity, exact
label grounding, microbedecoder provenance, ChEBI/PubChem chemistry, SSSOM row,
and aggregate copy pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-nitrophenyl_Alpha-D-galactoside.yaml`.
- Identifier and grounding: `identifier: CHEBI:546840` with
  `ontology_mapping.ontology_id: CHEBI:546840`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:546840` is active and resolves to
  `4-nitrophenyl alpha-D-galactoside`.
- PubChem CID `82000`, the record's formula `C12H15NO8`, and the stored InChI
  agree on the same alpha-D-galactoside stereochemistry.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-nitrophenyl_6-O-phosphono-beta-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-galactoside.yaml data/ingredients/mapped/4-nitrophenyl_Alpha-D-glucopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-galactopyranoside.yaml data/ingredients/mapped/4-nitrophenyl_Beta-D-glucopyranoside.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-nitrophenyl_Alpha-D-galactoside.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus component partonomy, SSSOM invariants, and flat-export coverage
  passed earlier in this all-record review; only SSSOM Rule B4 was skipped
  because the sibling `kg-microbe` ontology transforms are absent.

## Evidence

- The active ChEBI label supports the record's exact-label mapping. The
  historical 2026-08-04 demotion was explicitly marked as a false positive
  caused by a stale `CHEBI:300000` ceiling, and the later restoration event
  put the same ChEBI identity back under review before promotion.
- The PubChem CID, formula, InChI, and record chemistry all support a single
  alpha-D-galactoside compound rather than a mixture or adjacent stereoisomer.
- The microbedecoder occurrence block records 3 uses from
  `BacDive_Metabolite_utilization` and carries the source accession
  `kgmicrobe.trait:4_nitrophenyl_alpha_d_galactoside`.
- The SSSOM row maps `MIM:4-nitrophenyl_Alpha-D-galactoside` to
  `CHEBI:546840` with `skos:exactMatch`, `semapv:LexicalMatching`, and no
  `other` synonym payload.
- The hidden/ignored-inclusive search over `data`, `mappings`, `docs`, and
  `UNIFIED_INGREDIENT_MAPPING.tsv` found the active YAML, aggregate copy, SSSOM
  row, source review and regrounding rows, generated docs, stale advisory rows,
  and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, molecular weight, source occurrence counts, and
  `ingredient_type` are populated.
- No synonyms, roles, components, environment, or discussion entries need
  review.

## Recommended Edits

No YAML edit is required for this record.
