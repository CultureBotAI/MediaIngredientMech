# `data/ingredients/mapped/Guanidine_Hydrochloride.yaml`

## Verdict

Needs curation. The CAS RN, PubChem structure, and final registry rows are
internally consistent, but `NCIT:C47551` is an exact guanidine hydrochloride
class rather than a broader parent, fresh OLS now exposes exact
`CHEBI:749309`, and the adjacent active `Guanidinium_Chloride` record already
maps the same salt identity to `CHEBI:32735`.

## Identity

- Reviewed record: `data/ingredients/mapped/Guanidine_Hydrochloride.yaml`.
- Identifier and grounding: `identifier: cas:50-01-1` with
  `ontology_mapping.ontology_id: NCIT:C47551`, label
  `Guanidine Hydrochloride`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: PubChem CID `5742`, CAS-RN `50-01-1`, formula
  `CH6ClN3`, InChI `InChI=1S/CH5N3.ClH/c2-1(3)4;/h(H5,2,3,4);1H`, and SMILES
  `C(=N)(N)N.Cl`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Griseolutein_B.yaml data/ingredients/mapped/Ground_Beef.yaml data/ingredients/mapped/Guaiacol.yaml data/ingredients/mapped/Guaiazulene.yaml data/ingredients/mapped/Guanidine_Hydrochloride.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Guanidine_Hydrochloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the NCIT parent and CAS registry CURIE.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `NCIT:C47551` as active `Guanidine Hydrochloride`, lists CAS
  `50-01-1`, records `CHEBI:32735`, and includes `Guanidinium Chloride` as an
  exact synonym.
- Fresh OLS search for `Guanidine Hydrochloride` finds exact active
  `CHEBI:749309` `guanidine hydrochloride`, whose formula, InChI, mass, and
  PubChem-derived SMILES describe the same salt form.
- PubChem resolves CAS `50-01-1` to CID `5742`, lists
  `Guanidine hydrochloride`, `Guanidinium chloride`, `50-01-1`, and
  `CHEBI:32735` as synonyms, and returns the same InChI as both this record and
  the active `data/ingredients/mapped/Guanidinium_Chloride.yaml` record.
- Major: `NARROW_MATCH` to `NCIT:C47551` is too weak for the current NCIT
  target. The NCIT class denotes the same salt, not a broader parent.
- Major: the final SSSOM publishes `MIM:Guanidine_Hydrochloride` as a separate
  CAS/`kgmicrobe.compound` identity while `MIM:Guanidinium_Chloride` maps the
  same InChI salt to `CHEBI:32735`. That duplicate active identity should be
  merged or explicitly disambiguated.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found this active YAML, the adjacent
  `Guanidinium_Chloride` YAML, matching aggregate copies, generated products,
  final SSSOM rows for both records, row-review TSVs, and ignored aggregate
  backups.

## Completeness

- The CAS RN, PubChem CID, formula, InChI, SMILES, NCIT target, exact CAS
  registry row, and `kgmicrobe.compound` companion row are populated.
- The current record is not complete as a distinct identity because it overlaps
  with `Guanidinium_Chloride` and no longer needs a CAS-primary fallback while
  exact CHEBI/NCIT identities are available.

## Recommended Edits

- Major: merge or reground `data/ingredients/mapped/Guanidine_Hydrochloride.yaml`
  and `data/ingredients/mapped/Guanidinium_Chloride.yaml` so the CAS
  `50-01-1`, PubChem CID `5742`, and exact CHEBI/NCIT identifiers describe one
  active MIM subject rather than two.
- Major: rebuild final SSSOM after the merge so
  `MIM:Guanidine_Hydrochloride` no longer publishes redundant CAS and
  `kgmicrobe.compound` identity rows beside `MIM:Guanidinium_Chloride`.
