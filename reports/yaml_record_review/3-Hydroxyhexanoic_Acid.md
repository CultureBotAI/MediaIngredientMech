# `data/ingredients/mapped/3-Hydroxyhexanoic_Acid.yaml`

## Verdict

Needs curation, major. The active `CHEBI:37035`
`3-hydroxyhexanoic acid` identity itself is current, but the record's imported
CAS RN `66997-60-2` resolves to the stereospecific `(3S)-3-hydroxyhexanoic
acid` while the ChEBI target and structure are stereochemistry-unspecified.

## Identity

- Reviewed record: `data/ingredients/mapped/3-Hydroxyhexanoic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:37035` with
  `ontology_mapping.ontology_id: CHEBI:37035`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the refreshed EMBL-EBI ChEBI page for `CHEBI:37035`
  resolves to `3-hydroxyhexanoic acid`, lists formula `C6H12O3`, and carries
  CAS `10191-24-9`.
- The record's `molecular_formula`, InChI, and SMILES are also generic, matching
  the stereochemistry-unspecified ChEBI identity.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-Chloro-4-hydroxyphenylacetic_acid.yaml data/ingredients/mapped/3-Chloro-L-tyrosine.yaml data/ingredients/mapped/3-Chloroacrylic_acid.yaml data/ingredients/mapped/3-Hydroxydecanoic_Acid.yaml data/ingredients/mapped/3-Hydroxyhexanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/3-Hydroxyhexanoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:3-Hydroxyhexanoic_Acid` to `CHEBI:37035` row, but also exports
  `CAS:66997-60-2` in the row's `other` field.

## Evidence

- The active ChEBI page and OAK/OLS review both confirm the generic
  3-hydroxyhexanoic-acid identity.
- PubChem resolves CAS `66997-60-2` to formula `C6H12O3` but with isomeric
  SMILES `CCC[C@@H](CC(=O)O)O`, an InChI with `/t5-/m0/s1`, and IUPAC name
  `(3S)-3-hydroxyhexanoic acid`, all narrower than the active generic record.
- `occurrence_statistics` reports `0/0`; the record came from CultureBotHT CAS
  input rather than a counted CultureMech recipe occurrence.
- Stale: `mappings/record_research_validation.tsv` still contains old P1 rows
  asking for direct `CHEBI:37035` verification. The direct ChEBI check now
  passes for the generic identity, but it also reveals that the CAS should be
  replaced or removed.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, and advisory rows; it found no local note
  documenting an intentional stereospecific-CAS-to-generic-ChEBI broadening.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- Core formula/InChI/SMILES are complete for the active generic ChEBI identity.
- The residual issue is consequential because the generated SSSOM `other`
  field publishes a stereospecific CAS as if it were an exact synonym of the
  generic ChEBI term.

## Recommended Edits

1. Remove `cas_rn: 66997-60-2` from the generic `CHEBI:37035` record, or
   reground the record to a stereospecific term if the source CAS is more
   authoritative than the source label.
2. If the generic ChEBI target remains, use the ChEBI CAS `10191-24-9` only
   after confirming it is appropriate for this record's scope.
3. Regenerate `data/curated/mapped_ingredients.yaml`,
   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.
4. Re-run the focused strict/LinkML validators, CAS/identity plausibility
   checks, `just qc-sssom`, and `just qc-flat-coverage` after those edits.
