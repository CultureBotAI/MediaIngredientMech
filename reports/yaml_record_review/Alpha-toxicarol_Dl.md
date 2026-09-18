# `data/ingredients/mapped/Alpha-toxicarol_Dl.yaml`

## Verdict

Pass. The record intentionally uses a local
`kgmicrobe.compound:alpha-toxicarol_dl` identity for the DL/racemic form after
rejecting sibling stereospecific `CHEBI:9643`; the active SSSOM row and
aggregate copy reflect that local fallback.

## Identity

- Reviewed record: `data/ingredients/mapped/Alpha-toxicarol_Dl.yaml`.
- Identifier and grounding: `identifier: kgmicrobe.compound:alpha-toxicarol_dl`
  with matching `ontology_mapping.ontology_id`, source `kgmicrobe.compound`,
  `mapping_quality: FALLBACK_REGISTRY`, and `mapping_status: MAPPED`.
- Local OAK and the official ChEBI page resolve `CHEBI:9643` to `Toxicarol`
  with CAS `82-09-7`, formula `C23H22O7`, and a fixed stereochemical InChIKey
  `JLTNCZQNGBLBGO-MOPGFXCFSA-N`; the record correctly removed that sibling
  ChEBI term from its identity.
- `ingredient_type: SINGLE_INGREDIENT` is present, and the retained
  `chemical_properties.molecular_formula` is form-compatible formula-only
  metadata.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Alpha-ketoglutaric_Acid.yaml data/ingredients/mapped/Alpha-toxicarol_Dl.yaml data/ingredients/mapped/Alphaalpha-Trehalose.yaml data/ingredients/mapped/Althiomycin.yaml data/ingredients/mapped/Aluminium_Sulfate.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/Alpha-toxicarol_Dl.yaml "BFO CHEBI ENVO FOODON MICRO NCIT OBI PATO PO RO UBERON"`:
  exited 1 because `kgmicrobe.compound` is a local non-OBO prefix. Engine A was
  intentionally skipped for this record.
- `uv run --frozen runoak -i sqlite:obo:chebi aliases CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned `Toxicarol` and `alpha-Toxicarol` aliases for the rejected
  stereospecific `CHEBI:9643` sibling.
- `uv run --frozen runoak -i sqlite:obo:chebi term-metadata CHEBI:30915 CHEBI:16551 CHEBI:157683 CHEBI:74772 CHEBI:9643`:
  returned formula, charge, SMILES, InChI, InChIKey, CAS, average mass, and
  monoisotopic mass for the rejected `CHEBI:9643` sibling.
- `uv run --frozen python scripts/validate_component_partonomy.py`: passed; 2951
  records, 83 decompositions, 505 components, 0 violations.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed; the local CURIE is skipped by Engine B as a no-adapter prefix.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 was skipped because
  the sibling kg-microbe ontology transforms were absent.

## Evidence

- The `REGROUNDED_STEREOCHEMICAL_FORM` history entry records the
  `CHEBI:9643` to `kgmicrobe.compound:alpha-toxicarol_dl` correction and
  explains that no exact external ontology term or broader parent was verified.
- `scripts/fix_cas_stereochemical_identity_conflicts.py` retains the same
  subject ID, old ChEBI ID, and local identity for this record, with tests
  covering the alpha-toxicarol rewrite.
- `mappings/ingredient_mappings.sssom.tsv` row 382 maps
  `MIM:Alpha-toxicarol_Dl` to the local registry identity with
  `skos:exactMatch` and the manual `#456` explanation.
- A hidden/ignored-inclusive search over `data`, `mappings`, `reports`, `src`,
  `tests`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md` found the active
  YAML, aggregate copy, fixed SSSOM row, stereochemical repair script/tests,
  and stale advisory row-review outputs against the old `CHEBI:9643` grounding.

## Completeness

- The local identity, mapping evidence, formula-only chemistry, and curation
  history are populated.
- Occurrence statistics are correctly `0/0`: the record came from a CAS lookup
  with no CultureMech or MicrobeDecoder occurrence rows in this repository.
- No synonym, role, component, environmental context, discussion, or dataset
  entry is needed.
- The aggregate copy in `data/curated/mapped_ingredients.yaml` matches the
  per-record YAML.

## Recommended Edits

- None.
