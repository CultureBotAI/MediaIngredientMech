# `data/ingredients/mapped/5-aminovaleric_Acid.yaml`

## Verdict

Needs curation, major. The exact `CHEBI:15887` identity, CAS, chemistry,
occurrence count, SSSOM row, and aggregate copy pass, but two exact synonyms
name the wrong positional isomer and the amino-acid-source role is only an
ancestry-inferred provisional assertion.

## Identity

- Reviewed record: `data/ingredients/mapped/5-aminovaleric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:15887` with
  `ontology_mapping.ontology_id: CHEBI:15887`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- The official ChEBI page resolves `CHEBI:15887` to `5-aminopentanoic acid`
  with formula `C5H11NO2`, CAS `660-88-8`, SMILES `NCCCCC(=O)O`, and the
  stored InChI.
- Local OAK metadata carries the same label, formula, structure strings, and
  `cas:660-88-8`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/5-Hydroxyoctanoate.yaml data/ingredients/mapped/5-Keto-D-Gluconic_Acid_Potassium_Salt.yaml data/ingredients/mapped/5-_2-thienyl-pentanoic_Acid.yaml data/ingredients/mapped/5-aminovaleric_Acid.yaml data/ingredients/mapped/5-dehydro-D-gluconate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/5-aminovaleric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned the official exact and related synonym set for `CHEBI:15887`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:15887 CHEBI:180039 CHEBI:17426 CHEBI:58143`:
  returned the expected ChEBI formula, structure strings, and CAS xref.

## Evidence

- The active ChEBI term, CAS, formula, SMILES, InChI, and the exact synonym
  `5-Aminopentanoate` support the 5-aminopentanoic-acid identity.
- OAK's `CHEBI:15887` alias block includes `5-Aminopentanoic acid`,
  `5-amino-n-valeric acid`, `DANVA`, `delta-Amino-n-valeric acid`, and
  `delta-aminovaleric acid` as related synonyms, matching five of the imported
  `kg_microbe` synonyms.
- `4-aminovalerate` and `4-aminovaleric acid` are absent from the ChEBI alias
  block for `CHEBI:15887`; they put the amino group on carbon 4 instead of the
  terminal carbon 5 and should not be exact synonyms of 5-aminopentanoic acid.
- PubChem's synonym list for the CAS-backed 5-aminovaleric-acid compound also
  contains `660-88-8`, `delta-Aminovaleric acid`, `delta-Amino-n-valeric acid`,
  and `DANVA`, but not the two `4-aminovaler*` labels.
- The `AMINO_ACID_SOURCE` role is asserted only from a
  `COMPUTATIONAL_PREDICTION` whose note says the CHEBI ancestry inference is
  provisional and needs review. No inspected occurrence or source entry in the
  record supports the nutritional role.
- The SSSOM row maps `MIM:5-aminovaleric_Acid` to `CHEBI:15887` with
  `skos:exactMatch`, but it exports the two bad `4-aminovaler*` labels in
  `other` alongside the supported synonyms and `CAS:660-88-8`.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `scripts`, `tests`, and `src` found the active YAML, aggregate copy, SSSOM
  row, synonym-enrichment review rows, `record_research_validation.tsv` rows
  that also refute the two `4-aminovaler*` synonyms, and ignored aggregate
  backups.

## Completeness

- CAS, formula, InChI, SMILES, exact ChEBI synonym, occurrence counts, and
  `ingredient_type` are populated.
- The record is otherwise empty in the optional components, environment, and
  discussion sections.

## Recommended Edits

- In `data/ingredients/mapped/5-aminovaleric_Acid.yaml`, remove
  `4-aminovalerate` and `4-aminovaleric acid` from `synonyms`; rebuild
  `mappings/ingredient_mappings.sssom.tsv` and the aggregate
  `data/curated/mapped_ingredients.yaml`.
- In the same maintained YAML, either remove the provisional
  `AMINO_ACID_SOURCE` role or replace the computational placeholder with
  source-backed evidence scoped to 5-aminovaleric acid; rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen python scripts/validate_sssom_invariants.py`, and
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
  after the edit.
