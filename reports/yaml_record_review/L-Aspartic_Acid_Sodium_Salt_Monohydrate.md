# `data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`

## Verdict

Needs curation. The CAS primary identity, sodium-salt monohydrate PubChem
structure, #342 close parent mapping, exact CAS row, and hydrate review are
consistent, but final SSSOM lacks the local KG-Microbe registry anchor, parent
L-aspartic acid synonyms publish on the hydrate record, and
`AMINO_ACID_SOURCE` is only provisional name-pattern evidence.

## Identity

- Reviewed record:
  `data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`.
- Identifier and grounding: `identifier: cas:323194-76-9` with
  `ontology_mapping.ontology_id: CHEBI:17053`, label `L-aspartic acid`, source
  `CHEBI`, `mapping_quality: CLOSE_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: CAS RN `323194-76-9`, molecular formula `C4H8NNaO5`,
  InChI, SMILES, and PubChem CID `23679051`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/L-Aspartic_Acid_Potassium_Salt.yaml data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml data/ingredients/mapped/L-Carnitine.yaml data/ingredients/mapped/L-Carnitine_Hydrochloride.yaml data/ingredients/mapped/L-Cysteic_Acid_Monohydrate.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- Engine A LinkML term validation passed for all 5 records.
- `uv run --frozen python scripts/aggregate_records.py --ingredients-dir data/ingredients --output-dir /tmp/mim_qc_roundtrip_20260916_2330`:
  aggregated 2951 records.
- `uv run --frozen python scripts/verify_roundtrip.py --original-dir data/curated --aggregated-dir /tmp/mim_qc_roundtrip_20260916_2330`:
  passed with 2 files compared, 0 data differences, and only expected
  `generation_date` metadata differences.

## Evidence

- Exact EBI OLS4 ChEBI search for
  `L-Aspartic acid sodium salt monohydrate` returned zero hits; OLS4 resolves
  `CHEBI:17053` as active `L-aspartic acid`, matching the close parent mapping.
- PubChem resolves CAS RN `323194-76-9` to CID `23679051` with formula
  `C4H8NNaO5` and the same InChI as the YAML record, supporting the exact CAS
  monohydrate identity.
- `mappings/hydrate_review.tsv` records the CAS identity as hydrate-specific
  for L-aspartic acid sodium salt monohydrate.
- Major: `reports/hydrate_grounding.tsv` still reports
  `CAS_MISSING_ANCHOR_ROWS`. Final SSSOM has the `skos:closeMatch` parent row
  and exact CAS row, but lacks the exact `kgmicrobe.compound` registry sibling
  expected for this CAS-primary close-match hydrate.
- Major: final SSSOM `other` includes `(2S)-2-aminobutanedioic acid` and
  `ASPARTIC ACID` on the parent row. Those are synonyms of anhydrous
  L-aspartic acid, not of the sodium salt monohydrate, and erase both salt and
  hydrate boundaries.
- Major: `nutritional_roles.AMINO_ACID_SOURCE` has only
  `COMPUTATIONAL_PREDICTION` evidence from a curated name-pattern rule, with no
  inspected CultureMech, FEBA, Hans80, or literature evidence attached to the
  role claim.
- The hidden and ignored-inclusive search over `data/ingredients`, `mappings`,
  `reports/kg_microbe_node_id_mismatches.tsv`, `reports/hydrate_grounding.tsv`,
  `docs/data`, `src`, `tests`, `conf`, and `.claude` found the current YAML,
  final SSSOM rows, docs projections, hydrate review rows, unknown-term triage
  rows, and the current hydrate-grounding diagnostic.

## Completeness

- The CAS primary identifier, close ChEBI parent mapping, exact CAS row,
  aggregate copy, occurrence count, and PubChem structure are present and
  consistent.
- The final SSSOM registry anchoring and `other` synonyms are incomplete.
- The record is incomplete until the amino-acid-source role is either supported
  by inspected claim-level evidence or removed.

## Recommended Edits

- Major: repair final SSSOM generation for this CAS-primary close-match hydrate
  so `MIM:L-Aspartic_Acid_Sodium_Salt_Monohydrate` receives an exact local
  `kgmicrobe.compound:l-aspartic_acid_sodium_salt_monohydrate` row alongside
  the close parent and exact CAS rows.
- Major: remove or demote `(2S)-2-aminobutanedioic acid` and `ASPARTIC ACID` in
  `data/ingredients/mapped/L-Aspartic_Acid_Sodium_Salt_Monohydrate.yaml`.
- Major: remove `nutritional_roles.AMINO_ACID_SOURCE` unless an inspected
  CultureMech, FEBA, Hans80, or literature source can support this exact
  sodium-salt monohydrate form as an amino acid source.
- Rerun strict, term, hydrate, round-trip, component, and SSSOM validation after
  those changes.
