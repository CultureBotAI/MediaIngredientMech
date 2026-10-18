# `data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml`

## Verdict

Needs curation. The record exactly maps a concentration-qualified `0.5 M`
disodium stock label to `CHEBI:132766`, but current ChEBI defines
`CHEBI:132766` as the 3:1 trisodium salt `sodium nitrilotriacetate`. The YAML
also carries trisodium CAS, formula, SMILES/InChI, and exact synonyms on a
record whose preferred term says `disodium salt` and whose concentration says
it should be modeled as a stock solution rather than a neat single compound.

## Identity

- Reviewed record:
  `data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml`.
- Current grounding: `identifier: CHEBI:132766` with
  `ontology_mapping.ontology_id: CHEBI:132766`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:132766`
  uses ChEBI ID `CHEBI:132766`, ChEBI name `sodium nitrilotriacetate`, formula
  `C6H6NO6.3Na`, net charge `0`, average mass `257.085`, CAS `5064-31-3`, and
  the same three-sodium SMILES and InChI stored in `chemical_properties`.
- Local ontology check: the warmed OAK `sqlite:obo:chebi` adapter resolves
  `CHEBI:132766` to `sodium nitrilotriacetate` and defines it as an organic
  sodium salt composed of sodium and nitrilotriacetate ions in a `3:1` ratio;
  metadata did not report an `is_obsolete` or `deprecated` flag.
- Boundary checked:
  `data/ingredients/mapped/Nitrilotriacetic_Acid_Disodium_Salt.yaml` already
  owns `cas:15467-20-6`, the disodium salt CAS, with a non-exact parent mapping
  to `CHEBI:44557` `nitrilotriacetic acid`. The reviewed `05_M...` record is
  instead carrying the absorbed `Nitrilotriacetic_Acid_Trisodium_Salt.yaml`
  form and should not claim exact identity to a disodium stock solution.

## Validation

- Whole-corpus strict validation:
  `uv run --frozen python scripts/validate_strict.py` passed across 2,958 YAML
  documents, including all 2,951 per-record files and the seven curated
  collection files, with 0 ERROR rows.
- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed, so this record is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed; the stored `ontology_label` is the canonical label of the stored
  `CHEBI:132766`, even though that valid id-label pair is the wrong salt/form.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  exact equality for the `0.5 M Nitrilotriacetic acid, disodium salt` entry;
  curation history length is `12` in both copies.
- `mappings/ingredient_mappings.sssom.tsv`: contains one exact row,
  `MIM:05_M_Nitrilotriacetic_Acid_Disodium_Salt skos:exactMatch CHEBI:132766`,
  with object label `sodium nitrilotriacetate` and trisodium `other_label`
  values.
- `docs/data/mapped_ingredients.csv` and `docs/data/label_index.csv` publish the
  same `CHEBI:132766` identity and trisodium exact synonyms.

## Evidence

- Blocker: `CHEBI:132766` is not an exact identity for this record as labeled.
  ChEBI, local OAK, the stored CAS `5064-31-3`, formula `C6H6NO6.3Na`, SMILES,
  and InChI all describe the fully deprotonated trisodium salt. The preferred
  term says `0.5 M Nitrilotriacetic acid, disodium salt`.
- Major: the `EXACT_SYNONYM` list is dominated by trisodium labels
  (`NTA Trisodium salt`, `Trisodium NTA`,
  `Trisodium nitrilotriacetate`, and the trisodium IUPAC name). These labels
  are published as exact `other_label` values for the disodium stock-solution
  subject in final SSSOM and flat docs exports.
- Major: `ingredient_type: SINGLE_INGREDIENT` does not match the
  concentration-qualified `0.5 M` preferred term. The schema has
  `STOCK_SOLUTION` for pre-mixed solutions of defined ingredients, and stock
  solutions are in scope for `components` partonomy.
- Major: the CAS conflict was resolved toward trisodium `5064-31-3` after the
  `Nitrilotriacetic_Acid_Trisodium_Salt.yaml` duplicate was merged into this
  record. The repository now also has a distinct disodium `cas:15467-20-6`
  record, so the old merge left a trisodium exact mapping on a disodium stock
  label.
- `mappings/record_research_validation.tsv` still reports the same wrong-form
  concern against this record. Those rows are live, not stale: direct ChEBI
  verification confirmed the trisodium form conflict.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e CHEBI:132766 -e "05_M_Nitrilotriacetic_Acid_Disodium_Salt" -e "0.5 M Nitrilotriacetic acid, disodium salt" -e "Nitrilotriacetic_Acid_Trisodium_Salt" -e "5064-31-3" -e "15467-20-6" -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows, the
  disodium CAS sibling, the prior trisodium merge, and no better active exact
  identity for the complete `0.5 M` stock label.

## Completeness

- `components` is materially missing for a stock solution. The solution record
  needs source-backed solute and solvent/concentration details, or it should be
  demoted until the full stock formulation can be recovered.
- The retained `physicochemical_roles.CHELATOR` is plausible for an NTA stock,
  but its evidence is only the inherited CultureMech database role. It should
  be revisited after the identity split/remap so the role stays on the correct
  disodium or stock-solution node.
- `find . -path ./.git -prune -o -iname '*nitrilotriacetic*' -print` included
  ignored files and found the generic acid, the separate disodium CAS record,
  this stock/disodium-labeled record, and NTA-minus Wolfe mineral mix siblings.

## Recommended Edits

1. Do not keep `CHEBI:132766` as an exact identity for
   `data/ingredients/mapped/05_M_Nitrilotriacetic_Acid_Disodium_Salt.yaml`.
   Either remap this record to a local `kgmicrobe.ingredient:` stock-solution
   identifier, or merge its true disodium stock occurrences into a reviewed
   disodium stock record after source reconciliation.
2. Remove the trisodium CAS, formula, SMILES/InChI, and exact synonyms from the
   disodium `0.5 M` record. If a neat trisodium ingredient is still needed, it
   should be maintained as a separate `CHEBI:132766` record whose preferred
   term says trisodium and has no concentration qualifier.
3. Change `ingredient_type` to `STOCK_SOLUTION` and add source-backed
   `components` for the `0.5 M` solution, or demote to a non-identity pending
   state until the solvent and concentration basis are known.
4. Run `just sync-curated`, `just qc-roundtrip`, `just qc-component-partonomy`,
   `just validate-products`, and the docs/SSSOM export recipes after the
   maintained YAML fix so trisodium labels stop resolving to the disodium stock
   solution in final SSSOM and docs outputs.
