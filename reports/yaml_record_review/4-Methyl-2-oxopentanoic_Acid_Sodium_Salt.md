# `data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml`

## Verdict

Needs curation, major. The CAS/PubChem sodium-salt identity and local registry
rows are coherent, but the record exports the neutral acid and a bare anion as
labels of the sodium salt.

## Identity

- Reviewed record:
  `data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:4502-00-5` with a narrow
  `ontology_mapping.ontology_id: CHEBI:48430`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Official OLS/ChEBI check: `CHEBI:48430` is active, resolves to the neutral
  acid `4-methyl-2-oxopentanoic acid`, and has formula `C6H10O3`, CAS
  `816-66-0`, SMILES `CC(C)CC(=O)C(=O)O`, and the neutral-acid InChI.
- PubChem CID `4137900` resolves to the sodium salt formula `C6H9NaO3`, SMILES
  `CC(C)CC(=O)C(=O)[O-].[Na+]`, and the stored salt InChI.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/4-Methoxyflavone.yaml data/ingredients/mapped/4-Methyl-2-oxopentanoic_Acid_Sodium_Salt.yaml data/ingredients/mapped/4-Methyl-2-oxovaleric_Acid.yaml data/ingredients/mapped/4-Methylimidazole.yaml data/ingredients/mapped/4-Pyridoxic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  expected narrow ChEBI parent, exact CAS row, and exact kg-microbe registry row.

## Evidence

- Supported: retaining `cas:4502-00-5` as the exact registry identity and
  `CHEBI:48430` as a narrow parent is consistent with the sodium-salt PubChem
  structure and the official neutral-acid ChEBI target.
- Supported: `Sodium 4-methyl-2-oxovalerate` is an exact label for the salt.
- Major: `4-Methyl-2-oxopentanoate` denotes the conjugate-base anion without
  specifying sodium, but it is stored as an `EXACT_SYNONYM` and exported in the
  SSSOM `other` field for this sodium-salt record.
- Major: the SSSOM `other` field also carries `4-Methyl-2-oxovaleric acid`, the
  neutral sibling record's preferred label, beside the sodium-salt CAS.
- Stale: `mappings/record_research_validation.tsv` still recommends demotion to
  `UNMAPPED`; the active CAS and kg-microbe registry rows now already encode
  the absence of an exact ChEBI salt term.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM rows, OAK/OLS and unknown-term review rows,
  generated docs, same-name conflict baseline, stale advisory rows, and ignored
  aggregate backups.

## Completeness

- CAS, PubChem CID, formula, InChI, SMILES, and `ingredient_type` are populated.
- The active parent is non-exact, but that loss is explicit in
  `mapping_quality: NARROW_MATCH` and the exact registry rows preserve the
  supplied sodium-salt identity.
- This CultureBotHT fallback has no recipe-count occurrence; no role,
  component, environment, or discussion entries need review.

## Recommended Edits

1. Remove or demote `4-Methyl-2-oxopentanoate` so it no longer publishes as an
   exact sodium-salt synonym.
2. Keep `4-Methyl-2-oxovaleric acid` as a related parent label at most; do not
   export it in SSSOM `other` for the exact salt identity.
3. Resync `data/curated/mapped_ingredients.yaml`, rebuild SSSOM and docs, then
   verify `docs/data/label_index.csv` no longer reports the anion label as a
   `conflict:different_substances` synonym across the salt and neutral acid.
