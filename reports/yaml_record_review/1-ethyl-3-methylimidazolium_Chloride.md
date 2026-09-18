# `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Chloride.yaml`

## Verdict

Pass. The record denotes the complete 1-ethyl-3-methylimidazolium chloride salt,
not only the EMIM cation, and its ChEBI identifier, label, exact synonym, CAS
RN, molecular formula, SMILES, InChI, aggregate copy, generated docs, and SSSOM
row agree.

## Identity

- Reviewed record:
  `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Chloride.yaml`.
- Identifier and grounding: `identifier: CHEBI:61327` with
  `ontology_mapping.ontology_id: CHEBI:61327`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:61327`
  uses ChEBI ID `CHEBI:61327`, ChEBI name
  `1-ethyl-3-methylimidazolium chloride`, formula `C6H11N2.Cl`, SMILES
  `CCn1cc[n+](C)c1.[Cl-]`, and the same disconnected-ion InChI stored in
  `chemical_properties`. ChEBI also lists CAS RN `65039-09-0`.
- Synonym boundary: `1-ethyl-3-methyl-1H-imidazol-3-ium chloride` is the
  ChEBI IUPAC name for this chloride salt and is safe as an exact synonym.
- Sibling boundary checked: `1-ethyl-3-methylimidazolium_Acetate.yaml` is the
  distinct EMIM acetate salt on a CAS primary identifier, and
  `1-ethyl-3-methylimidazolium_Lysine.yaml` is the distinct EMIM lysinate ion
  pair on a local `kgmicrobe.compound:` identifier.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-ethyl-3-methylimidazolium_Chloride.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed earlier in this review pass, so this record's ontology mapping is in
  an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-ethyl-3-methylimidazolium_Chloride.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-ethyl-3-methylimidazolium_Chloride.yaml data/ingredients/mapped/1-ethyl-3-methylimidazolium_Lysine.yaml data/ingredients/mapped/1-methylphenanthrene.yaml`:
  passed; 3 files scanned, 0 ERROR rows.
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
  normalized semantic equality passed after ignoring empty default fields that
  are materialized only in the aggregate export.
- `mappings/ingredient_mappings.sssom.tsv` contains the expected exact row:
  `MIM:1-ethyl-3-methylimidazolium_Chloride skos:exactMatch CHEBI:61327`,
  with the IUPAC synonym and CAS RN in `other_label`.
- `docs/data/mapped_ingredients.*`, `docs/data/all_ingredients.*`,
  `docs/data/ingredients.json`, and graph/UMAP data contain the same
  `CHEBI:61327` identity and ChEBI label.

## Evidence

- The exact ChEBI grounding is supported: ChEBI `CHEBI:61327` denotes
  `1-ethyl-3-methylimidazolium chloride`, records its chloride-salt formula and
  disconnected-ion structure, and links it to the EMIM cation as a part rather
  than conflating the cation with the whole salt.
- `chemical_properties.cas_rn: 65039-09-0`, formula `C6H11N2.Cl`, SMILES, and
  InChI all describe the same chloride salt that ChEBI models for
  `CHEBI:61327`.
- The only exact synonym is the ChEBI IUPAC name and still includes the
  chloride counterion.
- The CultureBotHT evidence explains why the record exists. It is narrow to the
  import provenance and does not overclaim literature support for a role,
  component decomposition, or microbial use case.
- The hidden/ignored-inclusive search
  `find . -path ./.git -prune -o \( -iname '*methylimidazolium*' -o -iname '*methylphenanthrene*' \) -print`
  covered ignored files and hidden files outside `.git`; it found the expected
  EMIM acetate, chloride, and lysine active records and no duplicate active
  chloride YAML.

## Completeness

- Empty component and role slots are acceptable. The record models a defined
  ChEBI salt and has no retained evidence for a narrower nutritional,
  physicochemical, cellular-metabolic, or community role assertion.
- `occurrence_statistics.total_occurrences: 0` and `media_count: 0` are
  consistent with the CultureBotHT FEBA/Hans80 source provenance rather than a
  CultureMech medium occurrence.
- No open `discussions` or `datasets` entries need triage.
- A hidden/ignored-inclusive search over YAML, TSV, generated docs, and review
  artifacts found no stale `record_research_validation.tsv` entry for the
  active `CHEBI:61327` chloride identity.

## Recommended Edits

No edit is needed for the active record, aggregate export, SSSOM row, docs
surface, synonym, CAS RN, structure fields, or ingredient type.
