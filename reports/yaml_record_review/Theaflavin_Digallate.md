# `data/ingredients/mapped/Theaflavin_Digallate.yaml`

## Verdict

Needs curation. The ChEBI parent, exact kgmicrobe registry sibling, PubChem CID
structure, aggregate row, and final SSSOM row shape pass, but the CAS-primary
identity and exact CAS registry row still lack an inspected source that verifies
`30462-35-2` as the CAS RN for theaflavin digallate.

## Identity

- Reviewed record: `data/ingredients/mapped/Theaflavin_Digallate.yaml`.
- Identifier and grounding: `identifier: cas:30462-35-2` with
  `ontology_mapping.ontology_id: CHEBI:185495`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Synonyms: one exact synonym copied from the `CHEBI:185495` structure.
- Chemical properties: CAS `30462-35-2`, PubChem CID 135536164, formula
  `C43H32O20`, and matching InChI/SMILES for theaflavin 3,3'-digallate.
- Occurrences: zero CultureMech recipe occurrences.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Theaflavin` through `Thiamin_Pyrophosphate`: exited 0 and wrote zero ERROR
  rows.
- Direct old Engine A/OBO term validation was skipped for this CAS-primary row
  because registry CURIEs are intentionally outside the CHEBI-focused OBO term
  subset.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Local OAK resolves `CHEBI:185495` and returns the stored exact systematic
  synonym, supporting the ChEBI parent row.
- PubChem CID 135536164 resolves with formula `C43H32O20`, the same
  InChI/SMILES as the curated record, `CHEBI:185495` as a synonym, and a common
  `Theaflavin 3,3'-digallate` name.
- The final SSSOM has the expected three rows for
  `MIM:Theaflavin_Digallate`: a `skos:narrowMatch` parent row to
  `CHEBI:185495`, an exact `registry:cas` row for `cas:30462-35-2`, and the
  exact `kgmicrobe.compound:theaflavin_digallate` registry sibling required for
  narrow CHEBI matches.
- Fresh PubChem lookup by CAS `30462-35-2` returned no CID; PubChem's synonym
  list for CID 135536164 does not include that CAS; NCI CACTUS returned no
  structure for the CAS; and the ChEMBL record linked from PubChem did not carry
  synonyms that verify the CAS. The CAS may still be correct, but this record's
  primary identifier and exact CAS SSSOM row are currently supported only by the
  imported CultureBotHT value.

## Completeness

- The ChEBI parent, exact kgmicrobe registry sibling, CID structure, aggregate
  copy, and final row set agree.
- No components, roles, or environmental contexts are asserted.
- An ignored/hidden search of the active local curated, mapping, generated,
  source, and report paths found the expected CultureBotHT import, CAS and
  kgmicrobe unknown-term triage rows, OAK/OLS parent row-review, aggregate, and
  final SSSOM rows.

## Recommended Edits

- Major: in `data/ingredients/mapped/Theaflavin_Digallate.yaml`, either add a
  curation event and evidence note that verify CAS `30462-35-2` from an
  authoritative inspected source, or move the exact registry identity to a
  verified identifier. Then rerun strict validation, SSSOM publication, unknown
  term triage, and `scripts/validate_sssom_invariants.py`.
