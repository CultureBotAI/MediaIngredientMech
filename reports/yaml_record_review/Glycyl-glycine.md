# `data/ingredients/mapped/Glycyl-glycine.yaml`

## Verdict

Needs curation. The CultureMech exact match to active `CHEBI:17201`
glycylglycine, CAS RN, source-backed nitrogen role, ChEBI synonyms, duplicate
merge, and most final SSSOM synonyms pass, but the final SSSOM row publishes
`Glycylglycine(CAS: 556-50-3)`, a CAS-decorated raw merge label, in `other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycyl-glycine.yaml`.
- Identifier and grounding: `identifier: CHEBI:17201` with matching
  `ontology_mapping.ontology_id`, canonical label `glycylglycine`, source
  `CHEBI`, `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `556-50-3`, formula `C4H8N2O3`, InChI
  `InChI=1S/C4H8N2O3/c5-1-3(7)6-2-4(8)9/h1-2,5H2,(H,6,7)(H,8,9)`, and SMILES
  `NCC(=O)NCC(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycolate.yaml data/ingredients/mapped/Glycolic_Acid.yaml data/ingredients/mapped/Glycyl-L-proline.yaml data/ingredients/mapped/Glycyl-glycine.yaml data/ingredients/mapped/Glycyl_L-aspartic_Acid.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycyl-glycine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching active aggregate `data/curated/mapped_ingredients.yaml` entry
  carries the same ChEBI exact match, CAS RN, formula, InChI, SMILES, curated
  synonyms, source-backed nitrogen role, duplicate-merge labels, occurrence
  count, and singleton type as the per-record YAML.
- OLS4 resolves `CHEBI:17201` as `glycylglycine`, lists CAS `556-50-3` as a
  database cross-reference, and lists `2-(aminoacetamido)acetic acid`,
  `Gly-Gly`, `Gly2`, `N-glycylglycine`,
  `[(aminoacetyl)amino]acetic acid`, `glycine dipeptide`, and `Glycylglycine`
  as synonyms.
- PubChem resolves CAS `556-50-3` to `Glycylglycine` with formula `C4H8N2O3`
  and the same InChI as the record.
- The `NITROGEN_SOURCE` role is supported by `DATABASE_ENTRY` evidence from
  CultureMech and preserved original role text.
- The duplicate-identifier family also contains a rejected `Glycylglycine`
  tombstone with the same CHEBI identifier, so active/rejected comparisons must
  include `preferred_term`, not just `identifier`.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycyl-glycine` to `CHEBI:17201` by `skos:exactMatch`, but it exports
  `Glycylglycine(CAS: 556-50-3)` in `other`. That raw merge label combines the
  synonym and CAS payload in one display string; `CAS:556-50-3` is already
  published separately.
- Raw CultureMech `Role: ...; Properties: ...` text is an importer note
  filtered by `src/mediaingredientmech/synonym_policy.py`, so it does not reach
  final SSSOM `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, the rejected
  duplicate tombstone, matching aggregate copies, generated products, final
  SSSOM rows, row-review TSVs, and ignored aggregate backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, curated ChEBI
  synonyms, source-backed nitrogen role, ingredient type, occurrence count, and
  duplicate merge are populated.
- The CAS-decorated merge label needs to be removed from resolving synonym
  surfaces before final SSSOM is rebuilt.

## Recommended Edits

- Major: retype `Glycylglycine(CAS: 556-50-3)` in
  `data/ingredients/mapped/Glycyl-glycine.yaml` and the rejected
  `data/ingredients/mapped/Glycylglycine.yaml` tombstone as a non-resolving
  rejected label, or teach the synonym policy to filter labels that append a
  parenthesized CAS payload, then rebuild the final SSSOM so
  `MIM:Glycyl-glycine` no longer exports the combined label in `other`.
