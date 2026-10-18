# `data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`

## Verdict

Needs curation with a blocker identity finding. The record label and CAS name
the DL or stereo-unspecified form, but the record still uses
`CHEBI:37023`, the L-enantiomer, as both its identifier and exact ontology
mapping; final SSSOM therefore publishes an exact match to the wrong
stereochemical form and leaks an L-specific synonym in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`.
- Current identifier and grounding: `identifier: CHEBI:37023` with
  `ontology_mapping.ontology_id: CHEBI:37023`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Local OAK resolves `CHEBI:37023` to active `L-2-aminoadipic acid`; its
  definition scopes the term to the L-enantiomer, and its InChIKey is
  `OYIFNHCXNCRBQI-BYPYZUCNSA-N`.
- PubChem resolves the record's CAS `542-32-5` to
  `Alpha-Aminoadipic Acid` with non-isomeric InChIKey
  `OYIFNHCXNCRBQI-UHFFFAOYSA-N`, not to the L-only ChEBI structure.
- Live OLS exact search for `DL-2-Aminoadipic acid` resolves to
  `CHEBI:37024` by related synonym, and local OAK confirms `CHEBI:37024`
  is the stereo-unspecified `2-aminoadipic acid` term with CAS xref
  `542-32-5`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DEANONOate.yaml data/ingredients/mapped/DETANO.yaml data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml data/ingredients/mapped/DL-2-Aminobutyric_Acid.yaml data/ingredients/mapped/DL-3-Aminoisobutyric_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for all 5 files.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:77707 CHEBI:50154 CHEBI:37023 CHEBI:35621 CHEBI:27389`:
  returned formula, charge, InChI, InChIKey, SMILES, mass, synonyms, and xrefs
  for `CHEBI:37023`.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:37024`:
  returned the candidate stereo-unspecified parent with formula `C6H11NO4`,
  non-isomeric InChI, CAS `542-32-5`, and the related synonym
  `DL-2-Aminoadipic acid`.
- `curl -L ... q=DL-2-Aminoadipic%20acid&ontology=chebi&exact=true`: live OLS
  returned `CHEBI:37024`, not the record's current `CHEBI:37023`.
- `curl -L ... /compound/name/542-32-5/property/.../JSON`: PubChem resolved the
  CAS value to `Alpha-Aminoadipic Acid`.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; all id-label pairs corresponded, with full-corpus plausibility
  warnings only. This semantic DL/L conflict is outside that lexical validator.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- `mappings/culturemech_recipe_membership.tsv` has no rows for
  `CHEBI:37023`, matching `occurrence_statistics.media_count: 0` and
  `total_occurrences: 0`.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:DL-2-Aminoadipic_Acid` to the L-only `CHEBI:37023` with
  `skos:exactMatch`.
- The final SSSOM `other` token `(2S)-2-aminohexanedioic acid` is an exact
  synonym of L-2-aminoadipic acid and is not a same-subject synonym for the DL
  record.
- The `AMINO_ACID_SOURCE` role is supported only by a
  `COMPUTATIONAL_PREDICTION` evidence object whose curator note calls the ChEBI
  ancestry inference provisional and recommends review.

## Completeness

- The hidden/ignored-inclusive exact-identifier search over active `data`,
  `mappings`, `docs`, `scripts`, and `tests` found no second primary record for
  `CHEBI:37023`.
- The adjacent `fix_cas_stereochemical_identity_conflicts.py` script already
  repairs the same DL-to-parent pattern for `DL-2-Aminobutyric acid` and
  `DL-3-Aminoisobutyric acid`; the aminodipic record appears to be a missed
  member of that repair set.
- No source occurrences, mixture components, or environmental contexts are
  asserted.

## Recommended Edits

- Extend `scripts/fix_cas_stereochemical_identity_conflicts.py` to repair
  `data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml`: preserve
  `cas:542-32-5` as the exact local identity, map to `CHEBI:37024` by
  `NARROW_MATCH`, replace L-specific chemistry and synonyms, and emit the
  required CAS and kg-microbe identity rows in final SSSOM.
- Remove the provisional `AMINO_ACID_SOURCE` role or replace its
  `COMPUTATIONAL_PREDICTION` evidence with inspected claim-level evidence for
  this supplied form.
- Regenerate synchronized curated and SSSOM products, then rerun
  `uv run --frozen python scripts/validate_strict.py`,
  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/DL-2-Aminoadipic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`,
  `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`,
  and `uv run --frozen python scripts/validate_sssom_invariants.py`.
