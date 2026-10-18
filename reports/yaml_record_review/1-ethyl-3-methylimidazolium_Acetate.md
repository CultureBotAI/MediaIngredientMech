# `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`

## Verdict

Needs curation. The current record correctly keeps the complete
1-ethyl-3-methylimidazolium acetate salt on the CAS primary identifier
`cas:143314-17-4`, emits a narrow cation mapping to `CHEBI:61326`, and rejects
cation-only or other-salt labels so they do not leak into SSSOM `other_label`.
The remaining live defect is an unattached `kgscan` discussion seeded from
generic ionic-liquid and biopolymer literature.

## Identity

- Reviewed record:
  `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`.
- Identifier and grounding: `identifier: cas:143314-17-4` with
  `ontology_mapping.ontology_id: CHEBI:61326`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, and `mapping_status: MAPPED`.
- Official ChEBI check: the current EMBL-EBI ChEBI page for `CHEBI:61326`
  uses ChEBI ID `CHEBI:61326`, ChEBI name `1-ethyl-3-methylimidazolium`,
  formula `C6H11N2`, and net charge `+1`; that confirms the ChEBI term is only
  the cation, not the acetate salt.
- Salt identity: the exact salt remains represented by the primary CAS
  identifier and the full-salt PubChem chemistry:
  formula `C8H14N2O2`, SMILES `CCN1C=C[N+](=C1)C.CC(=O)[O-]`, and the
  disconnected-ion InChI stored in `chemical_properties`.
- Boundary checked: `1-ethyl-3-methylimidazolium_Chloride.yaml` is the
  ChEBI-modeled chloride salt, and `1-ethyl-3-methylimidazolium_Lysine.yaml`
  is a distinct EMIM lysinate ion pair with its own local
  `kgmicrobe.compound:` identity.

## Validation

- `scripts/_engine_a_obo_safe.sh data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml "CHEBI FOODON NCIT MESH UBERON ENVO BTO PATO"`:
  passed, so this record's ontology mapping is in an Engine A OBO prefix.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/1-chlorobutane.yaml data/ingredients/mapped/1-chloropropane.yaml data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml`:
  passed; 3 files scanned, 0 ERROR rows.
- `uv run --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`:
  passed the full product id/label gate earlier in this review pass.
- Evidence-reference validation:
  `uv run --frozen python scripts/run_shared_evidence_validator.py` could not
  run because the sibling `culturebotai-claw` checkout was absent at
  `../culturebotai-claw/scripts/validate_evidence_references.py`.
- Per-record/aggregate comparison against `data/curated/mapped_ingredients.yaml`:
  the core record is synchronized. The aggregate has the same acetate payload
  after excluding the per-record-only `discussions` overlay.
- `mappings/ingredient_mappings.sssom.tsv`: contains the expected three rows:
  `skos:narrowMatch CHEBI:61326`, preserving the cation parent; exact
  `cas:143314-17-4`, preserving the CAS registry identity; and exact
  `kgmicrobe.compound:1-ethyl-3-methylimidazolium_acetate`, preserving the
  local identity companion row required for a narrow-match subject.
- `mappings/ingredient_mappings_unknown_term_triage.tsv` explicitly keeps the
  CAS and `kgmicrobe.compound` rows as expected registry identifiers that are
  not OAK/OLS ontology terms.

## Evidence

- The non-exact mapping is correct: current ChEBI says `CHEBI:61326` is the
  +1 cation, while the preferred term and `chemical_properties` describe the
  1:1 acetate salt.
- The September salt-ion repair successfully rejects
  `1-ethyl-3-methyl-1H-imidazol-3-ium` and
  `1-ethyl-3-methylimidazolium lysine` as exact labels for this acetate salt.
  Neither rejected label is present in the SSSOM `other_label` field.
- The `record_research_validation.tsv` P1/P2 rows about CHEBI being cation-only
  describe the defect that has already been avoided here by the CAS primary,
  narrow ChEBI mapping, companion registry rows, and rejected cation/lysine
  labels. The `REGISTRY_FALLBACK_AGREES` row is stale because
  `mapping_status: MAPPED` is legitimate for a CAS-primary record that retains
  a valid broader ChEBI relation.
- Minor: `discussions[0]` is not a record-specific knowledge gap.
  `PMID:41015306` is at most generic ionic-liquid wastewater context, while
  `PMID:40666722`, `PMID:42195639`, and `PMID:40649189` discuss nonedible
  agro-wastes, biopolymer transformation, or broad production/regulatory
  barriers. None is attached to a precise unresolved mapping, role, salt, or
  registry question for EMIM acetate.
- The hidden/ignored-inclusive search
  `rg --no-ignore --hidden --line-number --fixed-strings -e cas:143314-17-4 -e "1-ethyl-3-methylimidazolium acetate" -e CHEBI:61326 -e 143314-17-4 -e kgscan-7872af433046 -g '!.git/*' .`
  covered the repository, ignored files, hidden files, and generated reports
  except `.git`; it found the current YAML/aggregate/docs/SSSOM rows, expected
  registry triage rows, the EMIM lysine sibling, and no duplicate active YAML
  for `cas:143314-17-4`.

## Completeness

- Empty component and role slots are acceptable. This record models a defined
  organic salt, not a culture-medium mixture, and no retained evidence supports
  a narrower role claim.
- The absence of exact synonyms is correct after the salt-ion repair. Exact
  EMIM acetate aliases such as bracketed `[emim][OAc]` or
  `[C2mim][CH3CO2]` would be useful only after source-backed enrichment.
- `find . -path ./.git -prune -o \( -iname '*chlorobutane*' -o -iname '*chloropropane*' -o -iname '*methylimidazolium*' \) -print`
  included ignored files and found the expected acetate, chloride, and lysine
  EMIM salt records among active YAML files.

## Recommended Edits

1. Remove or replace `kgscan-7872af433046` in
   `data/ingredients/mapped/1-ethyl-3-methylimidazolium_Acetate.yaml` with a
   claim-attached, EMIM-acetate-specific discussion if an actual unresolved
   evidence gap remains.
2. If `mappings/record_research_validation.tsv` is meant to be a live triage
   queue, regenerate it from its maintained recipe or mark the EMIM acetate
   cation-overclaim and registry-fallback rows resolved.
3. On a future synonym-enrichment pass, consider adding source-backed exact
   EMIM acetate aliases such as `[emim][OAc]` only to this acetate record.
4. No CAS primary identifier, `CHEBI:61326` narrow mapping, rejected-label,
   chemical-property, SSSOM, or docs edit is needed for the active salt
   identity.
