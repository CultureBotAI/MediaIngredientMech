# `data/ingredients/mapped/4-Methoxyflavone.yaml`

## Verdict

Pass with minor issues, minor. The PubChem-backed exact `CHEBI:114194` identity,
CAS row, chemistry, SSSOM rows, and aggregate row pass; only stale provenance
wording from the pre-#326 parent state remains.

## Identity

- Reviewed record: `data/ingredients/mapped/4-Methoxyflavone.yaml`.
- Identifier and grounding: `identifier: cas:4143-74-2` with exact
  `ontology_mapping.ontology_id: CHEBI:114194`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:114194` is active, resolves to
  `2-(4-methoxyphenyl)-1-benzopyran-4-one`, has formula `C16H12O3`, SMILES
  `COc1ccc(-c2cc(=O)c3ccccc3o2)cc1`, and the stored InChI.
- PubChem CID `77793` resolves to formula `C16H12O3`, SMILES
  `COC1=CC=C(C=C1)C2=CC(=O)C3=CC=CC=C3O2`, and the same InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  expected exact ChEBI row plus the exact CAS registry row.

## Evidence

- The current PubChem CID, formula, InChI, and #326 InChIKey check all support
  `CHEBI:114194` as the exact same substance, not the broader parent originally
  inferred in May.
- The row-review manifest correctly keeps the `cas:` SSSOM row as an expected
  registry identifier rather than treating it as a failed OBO term.
- Minor: the first `ontology_mapping.evidence` entry still says that no ChEBI
  entry exists and that a curator can promote the record if ChEBI adds a term.
  That was true at CAS-fallback import time but is stale now that the active
  mapping is the exact ChEBI term found through PubChem and repaired by #326.
- Stale: `mappings/record_research_validation.tsv` still refers to the old
  `NARROW_MATCH` state and asks for exactly the direct ChEBI verification that
  has since landed.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM rows, #326 regrade script, OAK/OLS and
  unknown-term review rows, generated docs, stale advisory rows, and ignored
  aggregate backups.

## Completeness

- CAS, PubChem CID, formula, InChI, SMILES, and `ingredient_type` are populated.
- This CultureBotHT fallback has no recipe-count occurrence; no role,
  component, environment, or discussion entries need review.

## Recommended Edits

Optionally replace the stale CAS-fallback evidence note with current exact
`CHEBI:114194` evidence, then resync the aggregate and rebuild SSSOM/docs.
