# `data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`

## Verdict

Needs curation, major. The CAS-backed local identity for
`3'-sialyllactose sodium salt` and PubChem chemistry pass, but the ontology row
still maps to generic `CHEBI:26714` `sodium salt`; ChEBI now has the closer
free-acid parent `CHEBI:59226` for 3'-sialyllactose, and the SSSOM `other`
field also carries an unrelated `Propionate (sodium salt)` label.

## Identity

- Reviewed record: `data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:128596-80-5` with
  `ontology_mapping.ontology_id: CHEBI:26714`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- CAS `128596-80-5`, formula `C23H38NNaO19`, PubChem CID `71308479`, and the
  stored InChI/SMILES describe 3'-sialyllactose sodium salt.
- ChEBI does not expose an exact sodium-salt term, but it does expose the
  corresponding free acid as `CHEBI:59226`
  `N-acetyl-alpha-neuraminyl-(2->3)-beta-D-galactosyl-(1->4)-beta-D-glucose`.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-methyl-3-butenol.yaml data/ingredients/mapped/3-nitropropanoate.yaml data/ingredients/mapped/3-octanone.yaml data/ingredients/mapped/3-phenylpropionate.yaml data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` agree with
  the YAML and publish the same generic `sodium salt` parent plus CAS and
  kg-microbe registry exact rows.

## Evidence

- The local CAS/PubChem identity is self-consistent for the sodium salt.
- Major: `CHEBI:26714` is only the generic sodium-salt class. The historical
  `scripts/reground_compositional_classes.py` exclusion said no closer parent
  existed, but `CHEBI:59226` is now a direct ChEBI term for 3'-sialyllactose and
  is much narrower than the generic sodium-salt class.
- Major: `mappings/ingredient_mappings.sssom.tsv` publishes
  `Propionate (sodium salt)` as `other` on this subject. That text names sodium
  propionate, not 3'-sialyllactose sodium salt.
- Major: the `CARBON_SOURCE` role is supported only by the provisional
  `Inferred from curated media-role name pattern` evidence.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM rows, generated docs, generic-salt repair
  script, row-review surfaces, and ignored aggregate backups.

## Completeness

- CAS, PubChem CID, formula, InChI, and SMILES are populated for the sodium
  salt.
- Exact ChEBI grounding is absent because ChEBI does not currently have a
  sodium-salt record for CAS `128596-80-5`.
- The registry rows preserving `cas:128596-80-5` and
  `kgmicrobe.compound:3-sialyllactose_sodium_salt` are appropriate for a local
  identity with a non-exact ChEBI parent.

## Recommended Edits

1. Reground `data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml` from
   generic `CHEBI:26714` to parent `CHEBI:59226`, leaving the CAS record as the
   primary local identity and retaining registry exact rows.
2. Remove `Propionate (sodium salt)` from the `MIM:3-sialyllactose_Sodium_Salt`
   SSSOM `other` field when rebuilding SSSOM; if it still appears after the
   parent change, fix the SSSOM writer or synonym-enrichment source that carries
   the generic-sodium-salt leakage.
3. Either replace the provisional `CARBON_SOURCE` evidence with inspected,
   claim-level evidence or remove the role.
4. Run `just sync-curated`, rebuild SSSOM and docs, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/3-sialyllactose_Sodium_Salt.yaml`.
