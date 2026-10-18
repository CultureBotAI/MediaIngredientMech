# `data/ingredients/mapped/Gramicidin.yaml`

## Verdict

Needs curation. The `cas:1405-97-6` local identity, NCIT parent mapping, CAS
registry row, `kgmicrobe.compound` registry row, and final SSSOM rows pass, but
the record types gramicidin as a single ingredient and stores a single PubChem
formula/InChI/SMILES even though the resolved NCIT target defines gramicidin as
a heterogeneous peptide mixture.

## Identity

- Reviewed record: `data/ingredients/mapped/Gramicidin.yaml`.
- Identifier and grounding: `identifier: cas:1405-97-6` with parent
  `ontology_mapping.ontology_id: NCIT:C65816`, label `Gramicidin`, source
  `NCIT`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: PubChem CID `45267103`, CAS-RN `1405-97-6`, formula
  `C96H135N19O16`, the PubChem InChI, and the PubChem isomeric SMILES.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Gossypetin.yaml data/ingredients/mapped/Gossypol.yaml data/ingredients/mapped/Gramicidin.yaml data/ingredients/mapped/Gramicidin_S.yaml data/ingredients/mapped/Gramine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Gramicidin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.

## Evidence

- The matching aggregate `data/curated/mapped_ingredients.yaml` entry is
  identical to the split per-record YAML.
- OLS4 resolves `NCIT:C65816` as `Gramicidin`, marks it active, lists CAS
  `1405-97-6`, and defines the target as a heterogeneous mixture of six
  antibiotic peptides.
- PubChem resolves CAS `1405-97-6` to CID `45267103`, and that CID reports
  synonym `Gramicidin D`, formula `C96H135N19O16`, and the same InChI as the
  record.
- `mappings/ingredient_mappings_external_prefix_ols_validation.tsv` confirms
  that `NCIT:C65816` resolves by prefix-specific OLS query; the final
  `UNKNOWN_TERM` marker on older row-review TSVs came from synonym-review
  dispatcher prefix coverage, not from a bad NCIT CURIE.
- The final `mappings/ingredient_mappings.sssom.tsv` rows map
  `MIM:Gramicidin` to `NCIT:C65816` by `skos:narrowMatch`, to
  `cas:1405-97-6` by `skos:exactMatch`, and to
  `kgmicrobe.compound:gramicidin` by `skos:exactMatch`; the CAS token in
  `other` is structured and belongs to the exact local identity.
- Major: `ingredient_type: SINGLE_INGREDIENT` and the structure fields copied
  from PubChem CID `45267103` over-specify one structured gramicidin D entry for
  a CAS/NCIT identity whose only checked ontology definition is a heterogeneous
  mixture.
- A hidden/ignored-inclusive search over `data`, `src`, `tests`, `mappings`,
  `scripts`, `conf`, `docs`, and `.claude` found the active YAML, matching
  aggregate copies, the NCIT prefix-resolution TSV, generated products, final
  SSSOM rows, row-review TSVs, and ignored aggregate backups.

## Completeness

- The CAS-local identity, NCIT parent, exact CAS registry row,
  `kgmicrobe.compound` companion row, and final SSSOM rows are present.
- A curator needs to decide whether the CultureBotHT row should denote
  gramicidin, gramicidin D, or another commercial gramicidin mixture before the
  record can safely keep a singleton type and structure-derived properties.

## Recommended Edits

- Major: in `data/ingredients/mapped/Gramicidin.yaml`, either relabel and
  reground the record to PubChem CID `45267103`'s exact Gramicidin D identity if
  the CultureBotHT CAS/source row supports that narrower form, or keep the
  gramicidin CAS/NCIT identity and remove the single-molecule formula, InChI,
  and SMILES while reclassifying the record away from
  `SINGLE_INGREDIENT`.
- After the identity decision, rebuild final SSSOM and rerun
  `scripts/validate_sssom_invariants.py` to confirm the parent and registry
  rows are still internally consistent.
