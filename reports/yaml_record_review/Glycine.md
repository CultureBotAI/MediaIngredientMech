# `data/ingredients/mapped/Glycine.yaml`

## Verdict

Needs curation. The CultureMech exact match to active `CHEBI:15428` glycine,
CAS RN, source-backed nitrogen role, ChEBI synonyms, and exact final SSSOM row
pass, but the final SSSOM `other` column publishes `Glycine 1%`, a
concentration-qualified raw label rather than a synonym for the glycine
subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Glycine.yaml`.
- Identifier and grounding: `identifier: CHEBI:15428` with matching
  `ontology_mapping.ontology_id`, canonical label `glycine`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `56-40-6`, formula `C2H5NO2`, InChI
  `InChI=1S/C2H5NO2/c3-1-2(4)5/h1,3H2,(H,4,5)`, and SMILES `NCC(=O)O`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycerol_Mono-oleate.yaml data/ingredients/mapped/Glycerol_Monostearate.yaml data/ingredients/mapped/Glycerol_Phosphate_Disodium_Salt_Hydrate.yaml data/ingredients/mapped/Glycine-NaOH_Buffer.yaml data/ingredients/mapped/Glycine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycine.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same ChEBI exact match, CAS RN, formula, InChI, SMILES, exact synonyms,
  source-backed nitrogen-source role, occurrence count, and singleton type as
  the per-record YAML.
- OLS4 resolves `CHEBI:15428` as `glycine`, lists CAS `56-40-6` as a database
  cross-reference, and lists the curated final-SSSOM ChEBI tokens
  `Aminoacetic acid`, `Aminoessigsaeure`, `Gly`, `Glycocoll`, `Glykokoll`,
  `Glyzin`, `H2N-CH2-COOH`, `Hgly`, `Leimzucker`, and `aminoethanoic acid` as
  synonyms.
- PubChem resolves CAS `56-40-6` to `Glycine` with formula `C2H5NO2` and the
  same InChI as the record.
- The `NITROGEN_SOURCE` role is supported by `DATABASE_ENTRY` evidence from
  CultureMech and preserved original role text.
- Major: the final `mappings/ingredient_mappings.sssom.tsv` row maps
  `MIM:Glycine` to `CHEBI:15428` by `skos:exactMatch`, but it exports
  `Glycine 1%` in `other`. That token is a MicrobeDecoder concentration label
  absorbed as `RAW_TEXT`; it should preserve the duplicate label's provenance,
  not become a published synonym for dry glycine.
- The raw CultureMech `Role: ...`, `Properties: ...`, and
  `Cross-references: ...` entries are importer notes filtered by
  `src/mediaingredientmech/synonym_policy.py`, so they do not hit final SSSOM
  `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, glycine as a component of stock solutions, generated
  products, the final SSSOM row, row-review TSVs, and ignored aggregate
  backups.

## Completeness

- The exact ChEBI identity, CAS RN, formula, InChI, SMILES, ChEBI synonyms,
  ingredient type, source-backed nitrogen role, occurrence count, and final
  SSSOM row are populated.
- The MicrobeDecoder concentration label needs to be removed from resolving
  synonym surfaces before final SSSOM is rebuilt.

## Recommended Edits

- Major: retype `Glycine 1%` in `data/ingredients/mapped/Glycine.yaml` as a
  non-resolving rejected label, or teach the synonym policy to filter
  concentration-qualified raw labels, then rebuild the final SSSOM so
  `MIM:Glycine` no longer exports `Glycine 1%` in `other`.
