# `data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`

## Verdict

Needs curation, major. The `CHEBI:16411` remap to neutral
`indole-3-acetic acid` is correct and the CultureMech occurrence count, SSSOM
row, aggregate row, CAS, InChI, and official ChEBI SMILES pass; two stale
`kg_microbe` exact synonyms from the former `CHEBI:87514` ethyl ester mapping
still export through the record and SSSOM `other` field.

## Identity

- Reviewed record: `data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:16411` with
  `ontology_mapping.ontology_id: CHEBI:16411`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: `CHEBI:16411` resolves to `indole-3-acetic acid`, CAS
  `87-51-4`, formula `C10H9NO2`, InChI
  `InChI=1S/C10H9NO2/c12-10(13)5-7-6-11-9-4-2-1-3-8(7)9/h1-4,6,11H,5H2,(H,12,13)`,
  and SMILES `O=C(O)Cc1cnc2ccccc12`; those agree with the record.
- `1H-indol-3-ylacetic acid` is a valid exact synonym for this ChEBI term.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/3-hydroxybutyric_Acid.yaml data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml data/ingredients/mapped/3-methyl-1-butanol.yaml data/ingredients/mapped/3-methyl-2-butenol.yaml data/ingredients/mapped/3-methyl-2-oxopentanoic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  same exact `MIM:3-indolyl_Acetic_Acid` to `CHEBI:16411` row.

## Evidence

- The active ChEBI page confirms the neutral indole-3-acetic acid identity,
  official label, CAS, formula, InChI, and SMILES.
- The August CultureMech occurrence refresh records 6 distinct CultureMech
  recipe ids, and `mappings/culturemech_recipe_membership.tsv` has six
  `CHEBI:16411` memberships.
- Major: `ethyl 2-hexenoate` and `ethyl hex-2-enoate` are retained as
  `EXACT_SYNONYM` values with `source: kg_microbe`, but the curation history
  says those labels came from the old `CHEBI:87514` ethyl 2-hexenoate mapping.
  They do not denote `CHEBI:16411`, and both now appear in the generated label
  index and the SSSOM `other` field for indole-3-acetic acid.
- Stale: `mappings/record_research_validation.tsv` says direct ChEBI inspection
  was missing and disputes the SMILES. The active official ChEBI SMILES matches
  the record; the ethyl-ester synonym objections remain real.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM row, generated docs, stale advisory rows,
  and ignored aggregate backups.

## Completeness

- Formula, CAS, InChI, and SMILES are populated for the neutral acid.
- The six CultureMech occurrences are reflected in `occurrence_statistics`.
- No role assertion needs review because the record has no
  `nutritional_roles`, `physicochemical_roles`, `cellular_roles`, or
  `community_roles`.

## Recommended Edits

1. In `data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`, remove the two
   `kg_microbe` exact synonyms `ethyl 2-hexenoate` and `ethyl hex-2-enoate`;
   keep `1H-indol-3-ylacetic acid`.
2. Run `just sync-curated`, rebuild SSSOM and docs so `other` and
   `docs/data/label_index.csv` drop those ester labels, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/3-indolyl_Acetic_Acid.yaml`.
