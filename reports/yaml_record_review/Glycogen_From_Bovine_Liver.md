# `data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml`

## Verdict

Needs curation. The source-qualified glycogen identity, CAS primary id, narrow
match to `CHEBI:28087`, and required exact registry rows pass, but
`CARBON_SOURCE` is unsupported computational curation and the stored PubChem
structure is a small fixed glycan rather than the bovine-liver glycogen
polymer.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml`.
- Identifier and grounding: `identifier: cas:9005-79-2`, narrow-mapped to
  `CHEBI:28087` with canonical label `glycogen`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS-RN `9005-79-2`, PubChem CID `439177`, formula
  `C24H42O21`, InChI, and SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Glycocholic_Acid_Hydrate.yaml data/ingredients/mapped/Glycocyamine.yaml data/ingredients/mapped/Glycogen.yaml data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml data/ingredients/mapped/Glycolaldehyde.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry carries
  the same CAS primary identifier, ChEBI narrow match, PubChem structure,
  singleton type, #322 class-overstatement evidence, #322 registry mint, and
  provisional carbon-source role as the per-record YAML.
- OLS4 resolves `CHEBI:28087` as `glycogen` and lists CAS `9005-79-2` as a
  database cross-reference for the generic class. An exact OLS4 search found no
  ChEBI term for `Glycogen from bovine liver`, so keeping a source-qualified
  CAS identity with a narrow ChEBI parent is consistent with
  MAPPING_SEMANTICS.
- PubChem resolves CAS `9005-79-2` to CID `439177` and the same fixed formula,
  InChI, and SMILES as the YAML.
- Major: the PubChem `C24H42O21` structure is a fixed four-residue glycan, while
  `Glycogen from bovine liver` denotes a source-qualified glycogen preparation
  and ChEBI defines glycogen as a polydisperse, highly branched glucan. The
  stored `chemical_properties` therefore over-specify the polymer identity.
- Major: `nutritional_roles.CARBON_SOURCE` is still backed only by
  `COMPUTATIONAL_PREDICTION` from a curated name-pattern rule and a provisional
  curator note. No inspected CultureMech, database, or literature evidence
  supports that role for this record.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Glycogen_From_Bovine_Liver` to `CHEBI:28087` by `skos:narrowMatch`, to
  `cas:9005-79-2` by `skos:exactMatch`, and to
  `kgmicrobe.compound:glycogen_from_bovine_liver` by `skos:exactMatch`; the
  exact rows keep only `CAS:9005-79-2` in `other`.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, generated products, final SSSOM rows for the parent and
  registry identities, row-review TSVs, and ignored aggregate backups.

## Completeness

- The CAS primary identity, source-qualified narrow ChEBI parent, exact
  registry rows, occurrence count, and ingredient type are populated.
- The PubChem structure fields need review.
- The carbon-source role needs claim-level evidence or removal.

## Recommended Edits

- Major: remove or replace `chemical_properties.molecular_formula`,
  `chemical_properties.inchi`, `chemical_properties.smiles`, and
  `chemical_properties.pubchem_cid` in
  `data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml` unless inspected
  evidence proves PubChem CID `439177` is a valid representative structure for
  bovine-liver glycogen in this corpus.
- Major: remove `nutritional_roles.CARBON_SOURCE`, or replace its provisional
  name-pattern evidence with inspected source evidence that specifically
  supports bovine-liver glycogen as a carbon source.
