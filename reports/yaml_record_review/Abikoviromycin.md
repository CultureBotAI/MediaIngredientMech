# `data/ingredients/mapped/Abikoviromycin.yaml`

## Verdict

Pass. The exact `CHEBI:210557` identity, microbedecoder source occurrence,
ChEBI chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Abikoviromycin.yaml`.
- Identifier and grounding: `identifier: CHEBI:210557` with
  `ontology_mapping.ontology_id: CHEBI:210557`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:210557` to `Abikoviromycin` with
  formula `C10H11NO` and InChIKey `KQSFHAWSULOGRI-ITIPBEISSA-N`.
- Local OAK metadata carries the same ChEBI label, formula, and structure
  strings.
- `ingredient_type: SINGLE_INGREDIENT` is present, and the
  `source_occurrences` entry preserves the microbedecoder
  `BacDive_Metabolite_production` provenance.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Abikoviromycin.yaml data/ingredients/mapped/Abscisic_Acid.yaml data/ingredients/mapped/Aburamycin_A.yaml data/ingredients/mapped/Abyssomicin_B.yaml data/ingredients/mapped/Abyssomicin_D.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Abikoviromycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:210557 CHEBI:2365`:
  returned `Abikoviromycin`, `(+)-abscisic acid`, and exact synonyms.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:210557 CHEBI:2365`:
  returned formula and structure metadata for `CHEBI:210557` and `CHEBI:2365`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The microbedecoder import used an OLS label-exact ChEBI match from
  `kgmicrobe.trait:abikoviromycin`, and ChEBI confirms that
  `CHEBI:210557` denotes Abikoviromycin.
- The live `chemical_properties` formula, SMILES, InChI, and molecular weight
  are present for the same ChEBI compound.
- The SSSOM row maps `MIM:Abikoviromycin` to `CHEBI:210557` with
  `skos:exactMatch` and the approved microbedecoder review trailer.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  and `scripts` found the active YAML, aggregate copies, SSSOM row,
  microbedecoder import row, manual approval trail, and ignored aggregate
  backups.

## Completeness

- Formula, InChI, SMILES, ChEBI grounding, microbedecoder provenance, and
  `ingredient_type` are populated.
- No CAS, role, component, environmental context, or discussion entry is needed
  for this sparse single-ingredient record.

## Recommended Edits

- None.
