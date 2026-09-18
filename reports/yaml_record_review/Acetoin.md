# `data/ingredients/mapped/Acetoin.yaml`

## Verdict

Pass. The exact `CHEBI:15688` identity, merged
`3-hydroxy 2-butanone` surface, microbedecoder source occurrence, ChEBI
chemistry, SSSOM row, and aggregate copy pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Acetoin.yaml`.
- Identifier and grounding: `identifier: CHEBI:15688` with
  `ontology_mapping.ontology_id: CHEBI:15688`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- ChEBI resolves `CHEBI:15688` to `acetoin` with formula `C4H8O2`, CAS
  `513-86-0`, and InChIKey `ROWKJAVDOGWPAT-UHFFFAOYSA-N`.
- The absorbed `3-hydroxy 2-butanone` surface is a punctuation-normalized
  acetoin synonym and was merged from the residual microbedecoder unmapped
  record.
- `ingredient_type: SINGLE_INGREDIENT` is present, and the
  `source_occurrences` entry preserves the microbedecoder production and
  utilization provenance.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetoin.yaml data/ingredients/mapped/Acetomycin.yaml data/ingredients/mapped/Acetone.yaml data/ingredients/mapped/Acetosyringone.yaml data/ingredients/mapped/Acetovanillone.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Acetoin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
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

- The microbedecoder import used an OLS label-exact ChEBI match from
  `kgmicrobe.trait:acetoin`, and ChEBI confirms that `CHEBI:15688` denotes
  acetoin.
- Local OAK metadata, ChEBI, and the live `chemical_properties` agree on the
  formula, SMILES, InChI, InChIKey, and molecular weight for acetoin.
- `mappings/edison_residual_merges.tsv` documents the
  `3-hydroxy 2-butanone` absorption as a single-compound identity for acetoin.
- The SSSOM row maps `MIM:Acetoin` to `CHEBI:15688` with `skos:exactMatch` and
  exports `3-hydroxy 2-butanone` in `other`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `src`, `tests`,
  `scripts`, and `reports/yaml_record_review_batch` found the active YAML,
  aggregate copies, SSSOM row, Edison residual-merge row, microbedecoder
  review row, and ignored aggregate backups.

## Completeness

- Formula, InChI, SMILES, ChEBI grounding, microbedecoder provenance, the
  residual synonym merge, and `ingredient_type` are populated.
- No role, component, environmental context, or discussion entry is needed.

## Recommended Edits

- None.
