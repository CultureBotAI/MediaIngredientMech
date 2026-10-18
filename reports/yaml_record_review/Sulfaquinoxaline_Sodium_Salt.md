# `data/ingredients/mapped/Sulfaquinoxaline_Sodium_Salt.yaml`

## Verdict

Needs curation - major. The CAS-primary sodium-salt identity and PubChem
structure fields pass, but the record still maps to the generic
`CHEBI:26714` sodium-salt class and the final SSSOM leaks
`Propionate (sodium salt)` in `other`.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Sulfaquinoxaline_Sodium_Salt.yaml`.
- Identifier and grounding: `identifier: cas:967-80-6` with
  `ontology_mapping.ontology_id: CHEBI:26714`, label `sodium salt`, source
  `CHEBI`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS `967-80-6`, PubChem CID `3693427`, formula
  `C14H11N4NaO2S`, and PubChem InChI/SMILES for the sodium salt.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sulfaquinoxaline_Sodium_Salt` through `Sulfisoxazole`: exited 0 and wrote
  zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this CHEBI-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh PubChem lookup resolves CAS `967-80-6` to CID `3693427` with formula
  `C14H11N4NaO2S` and InChI/SMILES matching the sodium salt in the YAML.
- Fresh OLS4 lookup resolves active `CHEBI:26714` with label `sodium salt` and
  a definition covering any alkali-metal salt having sodium(1+) as the cation;
  that is a generic salt class, not a chemically informative parent for
  sulfaquinoxaline sodium salt.
- Major: the prior stem-substring parent has not been regrounded even though
  the adjacent neutral `Sulfaquinoxaline` record now maps to `CHEBI:94719`,
  whose `sulfaquinoxaline` synonym and formula make it a nearer parent.
- Major: the final SSSOM parent row to `CHEBI:26714` publishes
  `Propionate (sodium salt)` in `other`, which is not a synonym for this MIM
  subject. The exact `cas:967-80-6` and
  `kgmicrobe.compound:sulfaquinoxaline_sodium_salt` sibling rows publish only
  `CAS:967-80-6` and remain valid registry identity rows.
- `mappings/culturemech_recipe_membership.tsv` has no `cas:967-80-6` rows,
  agreeing with `total_occurrences: 0` and `media_count: 0`.

## Completeness

- The CAS sodium-salt identity, PubChem chemistry, aggregate row, and exact CAS
  and KG-Microbe final SSSOM registry rows agree.
- An ignored/hidden search of local curated, mapping, generated, report,
  source, and documentation paths found the expected CultureBotHT,
  stem-substring parent, aggregate, generated index, final SSSOM, and row-review
  rows; the neutral `Sulfaquinoxaline` record is a parent candidate, not a
  duplicate of CAS `967-80-6`.

## Recommended Edits

- Major: replace the `CHEBI:26714` sodium-salt parent in
  `data/ingredients/mapped/Sulfaquinoxaline_Sodium_Salt.yaml` with
  `CHEBI:94719` as the nearer neutral-sulfaquinoxaline parent, or with an exact
  sulfaquinoxaline sodium salt term if one becomes available.
- Major: regenerate `mappings/ingredient_mappings.sssom.tsv` so the parent row
  no longer publishes `Propionate (sodium salt)` and the exact registry sibling
  rows continue to preserve CAS `967-80-6` and the local KG-Microbe compound ID.
