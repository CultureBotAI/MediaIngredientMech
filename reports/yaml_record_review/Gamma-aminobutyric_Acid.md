# `data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml`

## Verdict

Needs curation, with major synonym and unsupported-role issues. The exact
gamma-aminobutyric acid identity, CultureMech occurrences, structure fields,
and most kg-microbe synonyms pass, but final SSSOM exports two non-identical
aliases and `AMINO_ACID_SOURCE` is still only a provisional ChEBI-ancestry
prediction.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16865` with matching
  `ontology_mapping.ontology_id`, canonical label `gamma-aminobutyric acid`,
  source `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  and `ingredient_type: SINGLE_INGREDIENT`.
- OLS4 resolved `CHEBI:16865` as active gamma-aminobutyric acid with formula
  `C4H9NO2`, InChI
  `InChI=1S/C4H9NO2/c5-3-1-2-4(6)7/h1-3,5H2,(H,6,7)`, SMILES
  `NCCCC(=O)O`, and CAS xref `56-12-2`; PubChem lookup by that CAS RN resolved
  to CID 119 with the same formula and InChI.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gallate_Formate.yaml data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gallium_Iiichloride.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gallic_Acid.yaml data/ingredients/mapped/Gambogic_Acid.yaml data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the three CHEBI-primary records in the batch.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed;
  2951 records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, 13 CultureMech occurrences, CAS RN, structure fields,
  kg-microbe synonyms, provisional amino-acid-source role, and ingredient type
  as the per-record YAML.
- OLS4 confirms most exported synonyms are live ChEBI synonyms for
  `CHEBI:16865`, including `4-Aminobutanoic acid`, `4-Aminobutyric acid`,
  `4Abu`, `GABA`, `GAMMA-AMINO-BUTANOIC ACID`, `gamma-Aminobuttersaeure`,
  `gamma-amino-n-butyric acid`, `gamma-aminobutanoic acid`,
  `omega-aminobutyric acid`, `piperidic acid`, and `piperidinic acid`.
- Major: `2-aminobutyrate` is a positional/isomeric drift label for the
  2-amino acid, and `Gamma-Aminobutyric Acid Hydrochloride` names a salt form;
  neither appears among the OLS4 synonyms for `CHEBI:16865`, but both are
  active YAML synonyms and both leak into the final SSSOM `other` column.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` from CHEBI ancestry with a provisional curator
  note; no inspected source in the record supports the role.
- `mappings/ingredient_mappings_row_review_manifest.tsv` marks the
  `2-aminobutyrate|Gamma-Aminobutyric Acid Hydrochloride` synonym-enrichment
  row as already represented, which accurately describes the YAML state but
  does not make either token a valid final SSSOM synonym.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, and `reports` found the active YAML, aggregate copy, final SSSOM
  row, synonym-enrichment row, old residual rows that assign CAS `56-12-2` to
  gamma-aminobutyric acid rather than adjacent labels, generated indexes, and
  ignored aggregate backups.

## Completeness

- The exact gamma-aminobutyric acid identity, CAS RN, structure fields,
  CultureMech occurrences, most synonyms, and final SSSOM row are populated.
- The two non-identical synonyms and the amino-acid-source role need curator
  review.

## Recommended Edits

- Major: remove or retag `2-aminobutyrate` and
  `Gamma-Aminobutyric Acid Hydrochloride` in
  `data/ingredients/mapped/Gamma-aminobutyric_Acid.yaml` so the final SSSOM no
  longer exports them as gamma-aminobutyric acid synonyms; sync the aggregate
  YAML, regenerate final SSSOM, and rerun SSSOM invariants.
- Major: replace `AMINO_ACID_SOURCE` with source-backed evidence or remove it,
  then rerun strict validation.
