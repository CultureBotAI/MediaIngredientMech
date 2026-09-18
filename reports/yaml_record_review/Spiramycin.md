# `data/ingredients/mapped/Spiramycin.yaml`

## Verdict

Needs curation - major. The record is internally coherent enough to pass schema
and SSSOM invariants, but its generic spiramycin identity is grounded to an NCIT
parent while CHEBI now has spiramycin terms, its structure fields are for
Spiramycin I rather than CAS `8025-81-8`, and its `SELECTIVE_AGENT` role is
only a provisional name-pattern inference.

## Identity

- Reviewed record: `data/ingredients/mapped/Spiramycin.yaml`.
- Identifier and grounding: `identifier: cas:8025-81-8` with
  `ontology_mapping.ontology_id: NCIT:C839`, label `Spiramycin`, source
  `NCIT`, `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Chemical properties: `cas_rn: 8025-81-8`, `pubchem_cid: 5289394`, and formula
  `C43H74N2O14`.
- Occurrences: 0 source occurrences across 0 CultureMech media.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Sphondin` through `Spiramycin_II`: exited 0 and wrote zero ERROR rows.
- Direct `linkml-term-validator validate-data` exited 0 for this NCIT-parent
  record.
- Local aggregate comparison found this per-record file synchronized with its
  keyed row in `data/curated/mapped_ingredients.yaml`.

## Evidence

- Fresh OLS4 lookup resolves active `NCIT:C839` with label `Spiramycin`, and
  the final SSSOM keeps the required NCIT narrow row plus CAS and
  `kgmicrobe.compound` identity rows.
- Major: the YAML evidence still says no CHEBI entry exists for spiramycin, but
  a fresh exact CHEBI OLS4 search returns active `CHEBI:748977` for
  `spiramycin`, alongside CHEBI child terms for Spiramycin I, Spiramycin II,
  and Spiramycin III.
- Major: PubChem CID `5289394` is Spiramycin I with synonym `CHEBI:85260` and
  CAS `24916-50-5`, while CAS `8025-81-8` returned no PubChem CID in the fresh
  lookup. The current record therefore attaches Spiramycin-I formula, InChI,
  SMILES, and PubChem CID values to a generic spiramycin/CAS identity.
- Major: `physicochemical_roles.SELECTIVE_AGENT` is supported only by
  `COMPUTATIONAL_PREDICTION` from `infer_roles_from_name_lists`, with the
  provisional name-pattern curator note.

## Completeness

- The NCIT parent row and companion registry rows satisfy current SSSOM
  invariants, but they need regeneration after the YAML identity is repaired.
- No unsafe final `other` synonym was found; `CAS:8025-81-8` is the only
  published `other` payload.

## Recommended Edits

- Major: re-evaluate whether `data/ingredients/mapped/Spiramycin.yaml` should
  map to generic `CHEBI:748977`, to specific Spiramycin I `CHEBI:85260`, or to
  a local mixture identity anchored to the appropriate parent; then update the
  identifier, ontology mapping, and SSSOM rows to match that decision.
- Major: remove the Spiramycin-I-specific `chemical_properties` values unless
  the record is explicitly narrowed to Spiramycin I.
- Major: either remove `physicochemical_roles.SELECTIVE_AGENT` or replace the
  provisional name-pattern evidence with a source that explicitly uses the
  curated spiramycin form as a selective agent in a culture context.
