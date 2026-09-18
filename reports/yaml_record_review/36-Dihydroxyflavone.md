# `data/ingredients/mapped/36-Dihydroxyflavone.yaml`

## Verdict

Needs curation, minor. The #324 repair successfully moved
`3',6-Dihydroxyflavone` off the wrong dimethoxy ChEBI term and onto a local
kg-microbe identity plus broad `CHEBI:24698` `hydroxyflavone` parent, but
superseded evidence entries still live under the active `ontology_mapping` and
feed stale sources into SSSOM.

## Identity

- Reviewed record: `data/ingredients/mapped/36-Dihydroxyflavone.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:36-dihydroxyflavone`
  with `ontology_mapping.ontology_id: CHEBI:24698`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- The exact local identity is `3',6-Dihydroxyflavone`; PubChem CID `688662`
  resolves to `6,3'-Dihydroxyflavone`, formula `C15H10O4`, and InChI
  `InChI=1S/C15H10O4/c16-10-3-1-2-9(6-10)15-8-13(18)12-7-11(17)4-5-14(12)19-15/h1-8,16-17H`.
- Official ChEBI check: the previous `CHEBI:107657` target resolves to a
  dimethoxyflavone, formula `C17H14O4`, and remains unsuitable; the active
  `CHEBI:24698` parent is the broader `hydroxyflavone` class.
- `ingredient_type: SINGLE_INGREDIENT` is present.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/345-Trimethoxycinnamic_acid.yaml data/ingredients/mapped/35-Dihydroxybenzoic_acid.yaml data/ingredients/mapped/35-Dinitrosalicylic_Acid.yaml data/ingredients/mapped/36-Dihydroxyflavone.yaml data/ingredients/mapped/4-Acetoxy-3-methoxycinnamic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- Whole-corpus checks run earlier in this review pass passed; only the shared
  evidence validator was unavailable because `../culturebotai-claw` is absent.
- The active aggregate and `mappings/ingredient_mappings.sssom.tsv` contain the
  expected broad ChEBI parent plus exact kg-microbe registry row.

## Evidence

- The active ChEBI target is no longer the wrong `CHEBI:107657` dimethoxy
  compound, and the stale `cas:71592-46-6` identity no longer publishes as an
  exact SSSOM registry row.
- Minor: the first two entries in `ontology_mapping.evidence` are marked
  `SUPERSEDED (#324)` and explicitly describe CID `676293`, not this
  ingredient. Because they remain active evidence objects, the SSSOM row still
  lists `MIM:CultureBotHT` and `MIM:CHEBI via PubChem (pubchem-xref)` as
  sources for the current `hydroxyflavone` parent.
- Minor: the #324 note says PubChem listed no CAS for CID `688662`; the current
  PubChem view now lists CAS `71592-46-6` on both CID `688662`
  `6,3'-Dihydroxyflavone` and CID `676293` `6,3'-Dimethoxyflavone`, so the CAS
  situation needs a fresh registry decision rather than reuse of the old
  triage text.
- Stale: row-review TSVs still discuss `CHEBI:107657` and `cas:71592-46-6`
  rows that are no longer present in the active SSSOM.
- The hidden/ignored-inclusive search over `data`, `mappings`, `reports`,
  `docs`, `scripts`, `conf`, `src`, `tests`, `.github`, and `.claude` found the
  active YAML, aggregate copy, SSSOM rows, #324 repair script, stale row-review
  surfaces, generated docs, and ignored aggregate backups.

## Completeness

- The active parent is broad, but that is explicit in `NARROW_MATCH` and the
  exact kg-microbe identity row preserves the local compound identity.
- `chemical_properties` is empty. The PubChem CID `688662` formula and InChI
  are now available for the exact dihydroxy molecule, but CAS should be treated
  cautiously until the conflicting PubChem synonym assignment is resolved.
- No role, component, environment, or discussion entries need review.

## Recommended Edits

1. Replace or remove superseded `ontology_mapping.evidence` entries so only
   evidence for the current `kgmicrobe.compound:36-dihydroxyflavone` to
   `CHEBI:24698` narrow parent remains active.
2. Add current PubChem CID `688662` structure fields if desired, but keep or
   reject CAS `71592-46-6` explicitly instead of silently restoring it.
3. Run `just sync-curated`, rebuild SSSOM and docs, then verify with
   `just validate-all`, `just qc-sssom`, `just qc-roundtrip`, and
   `just validate-terms data/ingredients/mapped/36-Dihydroxyflavone.yaml`.
