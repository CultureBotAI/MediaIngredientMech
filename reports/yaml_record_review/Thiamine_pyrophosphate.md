# `data/ingredients/mapped/Thiamine_pyrophosphate.yaml`

## Verdict

Needs curation. The active record correctly moved off the chloride-salt ChEBI
term and onto `CHEBI:9532`, but chloride-salt structure fields and chloride
synonyms still remain and the final SSSOM exports those old chloride labels in
`other`.

## Identity

- Reviewed record: `data/ingredients/mapped/Thiamine_pyrophosphate.yaml`.
- Identifier and grounding: `identifier: CHEBI:9532` with the same
  `ontology_mapping.ontology_id`, label `thiamine(1+) diphosphate`, source
  `CHEBI`, `mapping_quality: SYNONYM_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:9532`, and `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: the record still stores CAS `136-09-4` and formula
  `C12H19N4O7P2S.Cl`, which carry over the chloride counterion removed by the
  August regrounding.
- Occurrences: 26 CultureMech recipe occurrences in 26 media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Thiamine_pyrophosphate` through `Thiolutin`: exited 0 and wrote zero ERROR
  rows.
- `uv run --frozen linkml-term-validator validate-data` on the same 5-file
  batch with `conf/term-validator.yaml`: all five CHEBI rows passed.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:9532` with canonical label
  `thiamine(1+) diphosphate` and related synonyms including
  `thiamine pyrophosphate`, supporting the salt-repair target.
- The `MIM curation (#319/#320)` evidence documents why this record was moved
  off `CHEBI:18290`: the source label does not mention a chloride counterion.
- Fresh PubChem lookup by CAS `136-09-4` resolves the same chloride-free CID
  5431 used by `Thiamin_Pyrophosphate`, not the chloride formula still stored
  on this record.
- Major: the synonyms still include chloride-specific labels such as
  `thiamine diphosphate chloride`, `thiamine(1+) diphosphate chloride`, and
  `thiaminium pyrophosphate chloride`, and the final SSSOM row for
  `MIM:Thiamine_pyrophosphate` exports those labels as exact `other` values for
  `CHEBI:9532`.

## Completeness

- The CHEBI identity, occurrence count, aggregate copy, and final SSSOM row
  identity agree.
- No components or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureMech import, #319/#320
  salt repair, aggregate, row-review, and final SSSOM rows. It also found the
  separate `Thiamin_Pyrophosphate` zwitterion record, which does not shadow this
  active record.

## Recommended Edits

- Major: in `data/ingredients/mapped/Thiamine_pyrophosphate.yaml`, remove or
  retype chloride-specific synonyms and refresh `chemical_properties` from
  `CHEBI:9532` so the formula, InChI, SMILES, and final SSSOM `other` payload
  no longer describe a chloride salt. Then rerun strict validation, SSSOM
  publication, synonym-row review, and `scripts/validate_sssom_invariants.py`.
