# `data/ingredients/mapped/1-naphtylacetic_Acid.yaml`

## Verdict

Needs curation. The repaired record now denotes
`CHEBI:32918`/`1-naphthaleneacetic acid` with the source misspelling preserved
only as raw text, and the chemistry and synchronized exports agree. The one
live defect is an unattached `kgscan` discussion seeded from broad dogwood,
melanoma, and depression gap sentences rather than a specific unresolved
NAA/ingredient claim.

## Identity

- Reviewed record:
  `data/ingredients/mapped/1-naphtylacetic_Acid.yaml`.
- Identifier and grounding: `identifier: CHEBI:32918` with
  `ontology_mapping.ontology_id: CHEBI:32918`, label
  `1-naphthaleneacetic acid`, source `CHEBI`,
  `mapping_quality: SYNONYM_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:32918`
  resolves to `1-naphthaleneacetic acid`, formula `C12H10O2`, SMILES
  `O=C(O)Cc1cccc2ccccc12`, the same InChI stored in `chemical_properties`,
  synonym `naphthalen-1-ylacetic acid`, and CAS RN `86-87-3`.
- Spelling boundary: the raw source label `1-Naphtylacetic Acid` is the
  misspelling; the current `preferred_term` and exact synonym use `Naphthyl`.
  That corrected surface still denotes the same `CHEBI:32918` substance.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-naphtylacetic_Acid.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-naphtylacetic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-naphtylacetic_Acid.yaml data/ingredients/mapped/1-o-methyl_Alpha-galactopyranoside.yaml data/ingredients/mapped/1-octen-3-ol.yaml data/ingredients/mapped/1-phenazinecarboxamide.yaml data/ingredients/mapped/1-propanolCO2.yaml`:
  passed; 5 files scanned, 0 ERROR rows.
- Whole-corpus checks run earlier in this review pass passed:
  `scripts/validate_strict.py`, `scripts/validate_all.py --mode both`,
  `scripts/validate_sssom_invariants.py`,
  `scripts/check_flat_export_coverage.py`,
  `scripts/audit_duplicate_identifiers.py --check`,
  `scripts/audit_kg_microbe_node_ids.py --check`,
  `scripts/validate_component_partonomy.py`, and
  `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  matched after excluding the per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected
  `MIM:1-naphtylacetic_Acid skos:exactMatch CHEBI:32918` row, and the
  corrected spelling plus the raw typo and CAS RN are exported in generated
  docs and label indexes.

## Evidence

- The current ChEBI page supports the target identity, CAS RN, formula, SMILES,
  InChI, and exact mapping to `CHEBI:32918`.
- The August `fix_naphthyl_spelling` event preserves the original misspelling
  as a raw synonym while preventing the typo from becoming the published KG
  display name for the ChEBI node.
- The stale `mappings/record_research_validation.tsv` P1/P2 rows for this slug
  predate the spelling fix, regrade to `SYNONYM_MATCH`, and populated chemistry.
  They no longer describe the active identifier, SSSOM row, or structure fields.
- Minor: `discussions[0]` is not a record-specific knowledge gap. None of its
  PMID snippets is attached to an unresolved mapping, synonym, CAS, supplied
  form, role, or source-occurrence question for 1-naphthaleneacetic acid.
- The hidden/ignored-inclusive search over YAML, TSV, Markdown, ignored backups,
  and generated review output found the active YAML/aggregate/SSSOM/docs rows,
  the old unmapped-audit and validation TSV rows, and no duplicate active YAML
  for `CHEBI:32918`.

## Completeness

- Empty component and role slots are acceptable for this single ChEBI chemical.
- CAS RN `86-87-3`, formula, SMILES, InChI, and molecular weight are already
  populated.
- No source occurrence is present beyond the original MediaDive queue import;
  the review found no contradictory active occurrence row.

## Recommended Edits

1. Remove or replace `kgscan-546f113a807c` with a claim-attached,
   NAA-specific discussion only if a concrete unresolved evidence gap remains.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or clear the obsolete
   `1-naphtylacetic_Acid` rows.
3. No identifier, ChEBI mapping, synonym, CAS, formula, SMILES, InChI,
   aggregate, SSSOM, or docs edit is needed for the active identity.
