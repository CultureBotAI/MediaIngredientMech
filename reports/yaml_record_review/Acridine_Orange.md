# `data/ingredients/mapped/Acridine_Orange.yaml`

## Verdict

Pass with minor issues. The exact `CHEBI:51739` identity, exact synonym, CAS,
chemistry, SSSOM row, and aggregate copy pass; one historical auto-backfill
change string has a truncated InChI.

## Identity

- Reviewed record: `data/ingredients/mapped/Acridine_Orange.yaml`.
- Identifier and grounding: `identifier: CHEBI:51739` with
  `ontology_mapping.ontology_id: CHEBI:51739`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:51739` to
  `acridine orange` with formula `H.C17H19N3.Cl`, SMILES
  `CN(C)c1ccc2cc3ccc(N(C)C)cc3nc2c1.[Cl-].[H+]`, InChIKey
  `VSTHNGLPHBTRMB-UHFFFAOYSA-N`, and CAS `494-38-2`.
- The stored `N,N,N',N'-tetramethylacridine-3,6-diamine hydrochloride` synonym
  is an exact ChEBI synonym for `CHEBI:51739`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Acetylated_Xylan.yaml data/ingredients/mapped/Acetylene.yaml data/ingredients/mapped/Achromoviromycin.yaml data/ingredients/mapped/Aconitate.yaml data/ingredients/mapped/Acridine_Orange.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Acridine_Orange.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned the expected ChEBI labels and synonyms for all four ChEBI terms in
  the batch.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:134431 CHEBI:27518 CHEBI:22210 CHEBI:51739`:
  returned formula and structure metadata for `CHEBI:51739`.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id/label pairs correspond, with 104 non-blocking plausibility
  warnings elsewhere in the corpus.

## Evidence

- The CultureBotHT CAS import, official ChEBI record, and local OAK metadata
  support the exact acridine orange identity and CAS `494-38-2`.
- The official ChEBI page and local OAK metadata support the stored formula,
  SMILES, and InChI.
- `mappings/ingredient_mappings_oak_ols_review.tsv` confirms `CHEBI:51739`
  through OAK/OLS; `mappings/ingredient_mappings.sssom.tsv` row 330 exports
  `MIM:Acridine_Orange` with the exact ChEBI synonym and `CAS:494-38-2`.
- `data/custom/microbedecoder/unmapped_labels.tsv` also contains
  `kgmicrobe.trait:acridine_orange`, but the current record is the earlier
  CultureBotHT CAS-backed record and not a MicrobeDecoder import.
- The only defect is historical: the 2026-05-01 `AUTO_BACKFILL_CHEBI_CHEMISTRY`
  change string cuts the InChI after `...6-8-1`, while
  `chemical_properties.inchi` stores the full ChEBI InChI.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `src`, `tests`, `scripts`, and `history` found the active YAML, aggregate
  copy, SSSOM row, OAK/OLS confirmation row, raw CAS/source leads, generated
  indexes, ignored aggregate backups, and stale advisory batch rows.

## Completeness

- CAS, formula, SMILES, InChI, exact synonym, curation history, and
  `ingredient_type` are populated.
- No role, component, environmental context, discussion, or dataset entry is
  needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- Optionally annotate the stale 2026-05-01 history `changes` prose in
  `data/ingredients/mapped/Acridine_Orange.yaml`; the active
  `chemical_properties` fields are already correct.
