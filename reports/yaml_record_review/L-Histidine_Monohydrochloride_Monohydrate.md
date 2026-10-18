# `data/ingredients/mapped/L-Histidine_Monohydrochloride_Monohydrate.yaml`

## Verdict

Needs curation. The CAS-backed identity, NCIT parent mapping, final exact CAS
and KG-Microbe identity rows, empty parent-row synonym payload, and hydrate
review are consistent, but `AMINO_ACID_SOURCE` is only provisional
name-pattern evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-Histidine_Monohydrochloride_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:5934-29-2` with
  `ontology_mapping.ontology_id: NCIT:C87334`, label
  `Histidine Monohydrochloride Monohydrate`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `5934-29-2`, molecular formula `C6H12ClN3O3`,
  InChI, SMILES, and PubChem CID `165377`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Histidine_Monohydrochloride_Monohydrate.yaml data/ingredients/mapped/L-Homoserine.yaml data/ingredients/mapped/L-Malic_Acid.yaml data/ingredients/mapped/L-Malic_Acid_Disodium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Meta-tyrosine.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- EBI OLS4 resolves `NCIT:C87334` as active
  `Histidine Monohydrochloride Monohydrate`, supporting the parent mapping.
- PubChem resolves CAS RN `5934-29-2` to CID `165377` with formula
  `C6H12ClN3O3` and the same InChI as the YAML record.
- `mappings/hydrate_review.tsv` records the CAS identity as hydrate-specific
  for L-histidine monohydrochloride monohydrate, and
  `reports/hydrate_grounding.tsv` reports `OK_OWN_CAS_ID`.
- The final SSSOM publishes the expected `skos:narrowMatch` row to
  `NCIT:C87334`, exact CAS and `kgmicrobe.compound` rows, no parent-row
  `other` tokens, and only `CAS:5934-29-2` on the exact identity rows.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM rows, docs
  projections, hydrate review rows, hydrate-grounding rows, and unknown-term
  triage rows.

## Completeness

- The CAS primary identifier, NCIT parent mapping, exact CAS and local registry
  rows, PubChem structure, hydrate review, empty occurrence count, and aggregate
  copy are present and consistent.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-histidine
  monohydrochloride monohydrate as an amino acid source.
- Rerun strict, term, hydrate, round-trip, role, component, and SSSOM validation
  after the role change.
