# `data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml`

## Verdict

Pass with minor issues. The CAS fallback identity, PubChem-backed chemistry,
SSSOM row, aggregate row, and docs pass; only optional DBNPA synonym enrichment
and stale local-registry advisory rows remain.

## Identity

- Reviewed record:
  `data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml`.
- Identifier and grounding: `identifier: cas:10222-01-2` with
  `ontology_mapping.ontology_id: cas:10222-01-2`, source `CAS`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- PubChem check: CID `25059` reports formula `C3H2Br2N2O`, SMILES
  `C(#N)C(C(=O)N)(Br)Br`, and the same InChI as the active YAML.
- The July unknown-term triage marks the `cas:10222-01-2` row as an expected
  registry identifier: CAS registry CURIEs are not OAK/OLS ontology terms.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/2-undecanol.yaml data/ingredients/mapped/20AA_mix.yaml data/ingredients/mapped/22-Dipyridyl.yaml data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml data/ingredients/mapped/2244688-heptamethylnonane.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  skipped as expected because `cas` is not an OBO-backed prefix for Engine A.
- Whole-corpus checks run earlier in this review pass passed, including the
  Engine B id/label product gate; only the shared evidence validator was
  unavailable because `../culturebotai-claw` is absent.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality passed.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact
  `MIM:22-dibromo-2-cyanoacetamide` to `cas:10222-01-2` registry row.

## Evidence

- The active PubChem chemistry confirms the CAS-primary fallback identity.
- The OAK/OLS `UNKNOWN_TERM` status for `cas:10222-01-2` is expected because
  this is a registry identity, not an ontology term to be resolved by OAK/OLS.
- Minor: `mappings/record_research_validation.tsv` suggests adding `DBNPA` and
  `2,2-dibromo-3-nitrilopropionamide` as synonyms; those lexical aliases are
  not yet represented.
- The hidden/ignored-inclusive search over `data/custom`, `data/curated`,
  `data/ingredients`, `mappings`, and `reports` found the active YAML,
  aggregate, SSSOM, OAK/OLS review, unknown-term triage, row-review manifest,
  and stale advisory rows.

## Completeness

- `ingredient_type: SINGLE_INGREDIENT` is present.
- CAS RN, PubChem CID, formula, InChI, and SMILES are populated for the active
  registry identity.
- The missing DBNPA aliases are useful but optional synonym enrichment.

## Recommended Edits

1. No required curation edit was found for
   `data/ingredients/mapped/22-dibromo-2-cyanoacetamide.yaml`.
2. Optionally add `DBNPA` as an exact synonym from an inspected source.
3. When stale advisory artifacts are next regenerated, confirm the obsolete
   CAS-local-CURIE findings drop out for this record.
