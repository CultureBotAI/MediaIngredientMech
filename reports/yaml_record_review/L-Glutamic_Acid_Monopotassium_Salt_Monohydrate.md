# `data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`

## Verdict

Needs curation. The CAS primary identity, monohydrate PubChem structure, exact
CAS row, and close ChEBI parent mapping are consistent, but final SSSOM lacks
the local KG-Microbe registry anchor, publishes parent L-glutamic acid synonyms
on the salt monohydrate parent row, and the amino-acid-source role is only
provisional name-pattern evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:6382-01-0` with
  `ontology_mapping.ontology_id: CHEBI:16015`, label `L-glutamic acid`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `6382-01-0`, molecular formula `C5H10KNO5`,
  InChI, SMILES, and PubChem CID `23695977`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Cysteine_X_HCl_X_H2O_Solution.yaml data/ingredients/mapped/L-Deoxyalliin.yaml data/ingredients/mapped/L-Galactose.yaml data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Glutathione.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_yjzjKv`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Exact EBI OLS4 ChEBI search for
  `L-Glutamic acid monopotassium salt monohydrate` returned zero hits; OLS4
  resolves `CHEBI:16015` as active `L-glutamic acid`, matching the close parent
  mapping.
- PubChem resolves CAS RN `6382-01-0` to hydrate-specific entries with formula
  `C5H10KNO5` and the same InChI as the YAML record, supporting the exact CAS
  monohydrate identity.
- `mappings/hydrate_review.tsv` records the CAS identity as hydrate-specific
  for L-glutamic acid monopotassium salt monohydrate.
- The final SSSOM publishes the expected parent `skos:closeMatch` row to
  `CHEBI:16015` plus the exact CAS identity row with `CAS:6382-01-0` in
  `other`.
- Major: `reports/hydrate_grounding.tsv` still reports
  `CAS_MISSING_ANCHOR_ROWS`. Final SSSOM lacks the exact
  `kgmicrobe.compound:l-glutamic_acid_monopotassium_salt_monohydrate` registry
  sibling expected for this CAS-primary close-match hydrate.
- Major: final SSSOM `other` includes
  `L-Glutamic acid potassium salt monohydrate, L-Glutamic acid potassium salt`,
  `(2S)-2-aminopentanedioic acid`, and `GLUTAMIC ACID` on the parent row. The
  comma-joined salt token is not a single resolving synonym and includes the
  anhydrous potassium salt; the last two are parent L-glutamic acid synonyms
  that erase the salt and hydrate boundary.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  role claim.
- The hidden and ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `src`, and `tests` found the current YAML, final SSSOM rows, docs
  projections, unknown-term triage rows, hydrate review rows, and the current
  hydrate-grounding diagnostic.

## Completeness

- The CAS primary identifier, close ChEBI parent mapping, exact CAS row,
  occurrence count, PubChem structure, hydrate review, and aggregate copy are
  present and consistent.
- The final SSSOM registry anchoring and parent-row synonym surface are
  incomplete.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: repair final SSSOM generation for this CAS-primary close-match hydrate
  so `MIM:L-Glutamic_Acid_Monopotassium_Salt_Monohydrate` receives an exact
  local `kgmicrobe.compound:l-glutamic_acid_monopotassium_salt_monohydrate` row
  alongside the close parent and exact CAS rows.
- Major: split or demote the comma-joined salt synonym and remove parent
  L-glutamic acid synonyms from
  `data/ingredients/mapped/L-Glutamic_Acid_Monopotassium_Salt_Monohydrate.yaml`;
  only labels for the monopotassium salt monohydrate should publish on the
  parent SSSOM row.
- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support L-glutamic acid
  monopotassium salt monohydrate as an amino acid source.
- Rerun strict, term, hydrate, round-trip, role, component, and SSSOM validation
  after those changes.
