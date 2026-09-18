# `data/ingredients/mapped/Guanidinium_Chloride.yaml`

## Verdict

Needs curation. The record is an exact active ChEBI match for guanidinium
chloride and the structure fields are internally consistent, but the adjacent
active `Guanidine_Hydrochloride` record duplicates the same salt identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Guanidinium_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:32735` with
  `ontology_mapping.ontology_id: CHEBI:32735`, label
  `guanidinium chloride`, source `CHEBI`, `mapping_quality: EXACT_MATCH`,
  `mapping_status: MAPPED`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: formula `CH6N3.Cl`, InChI
  `InChI=1S/CH5N3.ClH/c2-1(3)4;/h(H5,2,3,4);1H`, SMILES
  `NC(N)=[NH2+].[Cl-]`, and molecular weight `95.533`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Guanidinium_Chloride.yaml data/ingredients/mapped/Guanine.yaml data/ingredients/mapped/Guanosine.yaml data/ingredients/mapped/Gum_Arabic_From_Acacia_Tree.yaml data/ingredients/mapped/H23-methyl_Mercaptopropionate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `linkml-term-validator` passed for `CHEBI:32735`.
- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.

## Evidence

- OLS4 resolves `CHEBI:32735` as active `guanidinium chloride`; its formula
  and InChI describe the same salt recorded here.
- NCIT resolves `NCIT:C47551` as active `Guanidine Hydrochloride`, records CAS
  `50-01-1`, cross-references `CHEBI:32735`, and lists
  `Guanidinium Chloride` as an exact synonym.
- PubChem resolves CAS `50-01-1` to CID `5742`, lists
  `Guanidine hydrochloride`, `Guanidinium chloride`, `50-01-1`, and
  `CHEBI:32735` as synonyms, and returns the same InChI as this record and
  `data/ingredients/mapped/Guanidine_Hydrochloride.yaml`.
- Major: the final SSSOM publishes `MIM:Guanidinium_Chloride` as an exact
  ChEBI identity while `MIM:Guanidine_Hydrochloride` publishes a distinct
  CAS/`kgmicrobe.compound` identity for the same salt.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found this active YAML, the adjacent
  `Guanidine_Hydrochloride` YAML, matching aggregate copies, generated
  products, final SSSOM rows for both records, row-review TSVs, and ignored
  aggregate backups.

## Completeness

- The exact ChEBI target, formula, InChI, SMILES, and final exact ChEBI SSSOM
  row are populated and consistent.
- The record is not complete as a corpus identity while a second active MIM
  subject maps the same CAS and InChI salt.

## Recommended Edits

- Major: merge or reground `data/ingredients/mapped/Guanidinium_Chloride.yaml`
  and `data/ingredients/mapped/Guanidine_Hydrochloride.yaml` so CAS `50-01-1`,
  PubChem CID `5742`, `NCIT:C47551`, and `CHEBI:32735` describe one active MIM
  subject rather than two.
- Major: rebuild final SSSOM after the merge so the same salt identity is not
  published under two active MIM subjects.
