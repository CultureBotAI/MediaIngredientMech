# `data/ingredients/mapped/Sulfamethizole.yaml`

## Verdict

Pass. The exact `CHEBI:9331` identity, CAS, IUPAC synonym, structure fields,
aggregate row, and final SSSOM row all pass.

## Identity

- Reviewed record: `data/ingredients/mapped/Sulfamethizole.yaml`.
- Identifier and grounding: `identifier: CHEBI:9331` with
  `ontology_mapping.ontology_id: CHEBI:9331`, label `sulfamethizole`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `144-82-1`, formula `C9H10N4O2S2`, and
  ChEBI/PubChem InChI/SMILES.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulbactam` through `Sulfamethizole`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `CHEBI:9331` with label `sulfamethizole`,
  CAS xref `144-82-1`, formula `C9H10N4O2S2`, and structure fields matching
  the YAML.
- The active synonym
  `4-amino-N-(5-methyl-1,3,4-thiadiazol-2-yl)benzenesulfonamide` is the OLS
  exact IUPAC synonym for `CHEBI:9331`.
- Fresh PubChem lookup resolves CAS `144-82-1` to the same formula and InChI as
  the YAML.
- `mappings/culturemech_recipe_membership.tsv` has no `CHEBI:9331` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM row exact-matches `CHEBI:9331` and publishes only the IUPAC
  synonym and `CAS:144-82-1` in `other`; both are true labels for the same
  subject.

## Completeness

- The exact CHEBI identity, CAS, active synonym, aggregate row, and final SSSOM
  row agree.
- The record has no components, roles, environmental contexts, or datasets
  needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT,
  MicrobeDecoder candidate, aggregate, generated index, final SSSOM, and
  row-review rows, and no second active MIM record for `CHEBI:9331` or CAS
  `144-82-1`.

## Recommended Edits

- None.
