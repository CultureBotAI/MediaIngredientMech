# `data/ingredients/mapped/Sulfamethazine_Sodium_Salt.yaml`

## Verdict

Pass. The CAS-primary sodium-salt identity, `CHEBI:102265` parent mapping,
PubChem structure fields, aggregate row, and three-row final SSSOM
representation all pass.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sulfamethazine_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:1981-58-4` with
  `ontology_mapping.ontology_id: CHEBI:102265`, label `sulfamethazine`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `1981-58-4`, PubChem CID `13456556`, formula
  `C12H13N4NaO2S`, and PubChem InChI/SMILES for the sodium salt.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulbactam` through `Sulfamethizole`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh PubChem lookup resolves CAS `1981-58-4` to CID `13456556` with formula
  `C12H13N4NaO2S` and InChI/SMILES matching the sodium salt in the YAML.
- Fresh OLS4 lookup resolves active `CHEBI:102265` with label
  `sulfamethazine`, formula `C12H14N4O2S`, and neutral-parent structure
  fields, so the YAML correctly keeps the CAS sodium salt as primary and uses a
  `NARROW_MATCH` parent relation.
- `mappings/culturemech_recipe_membership.tsv` has no `cas:1981-58-4` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.
- The final SSSOM has the expected `skos:narrowMatch` row to `CHEBI:102265`
  plus exact registry rows for `cas:1981-58-4` and
  `kgmicrobe.compound:sulfamethazine_sodium_salt`; the two exact rows publish
  only `CAS:1981-58-4` in `other`, which is a true CAS label for this subject.

## Completeness

- The parent remapping history in
  `scripts/reground_compositional_classes.py` documents the intentional move
  from the over-broad sodium-salt class to the sulfamethazine parent.
- The record has no active synonyms, components, roles, environmental contexts,
  or datasets needing narrower evidence.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT,
  regrounding, aggregate, generated index, final SSSOM, and row-review rows,
  and no second active MIM record for CAS `1981-58-4` or the same sodium-salt
  identity.

## Recommended Edits

- None.
