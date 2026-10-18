# `data/ingredients/mapped/Fish-sperm_Dna.yaml`

## Verdict

Needs curation, with major final-SSSOM payload issues. The record correctly
mints a local exact identity for fish-sperm DNA and maps it narrowly to generic
CHEBI DNA, but broad DNA labels and a generic DNA CAS RN still export as exact
payload on the fish-sperm subject.

## Identity

- Reviewed record: `data/ingredients/mapped/Fish-sperm_Dna.yaml`.
- Identifier and grounding: `identifier:
  kgmicrobe.ingredient:fish-sperm_dna`, `ontology_mapping.ontology_id:
  CHEBI:16991`, label `deoxyribonucleic acid`, source `CHEBI`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:16991`, and `ingredient_type:
  UNDEFINED_MIXTURE`.
- The #322 curation history correctly notes that `CHEBI:16991` denotes DNA
  generally while `Fish-Sperm DNA` is source-qualified, so the exact identity
  moved to a local `kgmicrobe.ingredient:` registry CURIE and the CHEBI parent
  became a `NARROW_MATCH`.
- PubChem lookup by CAS RN `9007-49-2` resolves as deoxyribonucleic acid
  generally, not fish-sperm or herring-sperm DNA specifically.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Fildes_Enrichment.yaml data/ingredients/mapped/Filipin.yaml data/ingredients/mapped/Filtered_Seawater.yaml data/ingredients/mapped/Fish-sperm_Dna.yaml data/ingredients/mapped/Fish_peptone.yaml`:
  exited 0 for the 5-file batch and wrote zero ERROR rows.
- `uv run linkml-term-validator validate-data data/ingredients/mapped/Fish-sperm_Dna.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed.
- `uv run --frozen python scripts/validate_sssom_invariants.py`: passed Rules
  A, B1, B2, B3, C, D, E, F, G, H, I, J, and K; Rule B4 skipped because the
  sibling kg-microbe ontology transforms are not checked out.

## Evidence

- The matching active entry in `data/curated/mapped_ingredients.yaml` carries
  the same local identifier, CHEBI parent, occurrence counts, CAS RN, and
  inherited broad DNA synonyms as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` output has the expected
  `MIM:Fish-sperm_Dna skos:narrowMatch CHEBI:16991` parent row plus exact
  local registry rows for `kgmicrobe.ingredient:fish-sperm_dna` and
  `kgmicrobe.compound:fish-sperm_dna`.
- Major: the narrow CHEBI parent row's `other` column exports broad CHEBI DNA
  labels, including `DNA`, `DNAn`, `DNAn+1`, `deoxyribonucleic acids`, and
  `thymus nucleic acid`, as synonyms of the narrower fish-sperm DNA subject.
- Major: the exact local registry rows export `CAS:9007-49-2`, but the recorded
  CAS RN was fetched from the generic ontology label `deoxyribonucleic acid`
  and PubChem also resolves it as generic DNA.
- The rejected `data/ingredients/mapped/Deoxyribonucleic_Acid_From_Herring_Sperm.yaml`
  tombstone correctly points to the same local registry CURIE and publishes no
  final SSSOM row.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, `scripts`, `src`, `tests`, and `reports`, excluding prior
  per-record reports, aggregate backups, and the final SSSOM TSV, found the
  active YAML, the rejected herring-sperm tombstone, aggregate copies, parent
  row-review provenance, known kg-microbe node-id mismatch rows, occurrence
  membership, and ignored historical batch reports.

## Completeness

- The local registry identity, narrow CHEBI parent, exact local SSSOM rows, and
  occurrence counts are populated.
- Final SSSOM still needs to restrict `other` to labels and CAS RNs that denote
  the fish-sperm DNA identity itself, not its generic DNA parent.

## Recommended Edits

- Major: retype inherited generic DNA synonyms in
  `data/ingredients/mapped/Fish-sperm_Dna.yaml` so they no longer export as
  exact synonyms of the source-qualified subject; keep
  `Deoxyribonucleic acid from herring sperm` as the same-substance alias.
- Major: remove `chemical_properties.cas_rn: 9007-49-2` from the same record
  unless source-backed curation can show that the CAS RN belongs to fish-sperm
  DNA rather than generic DNA, sync `data/curated/mapped_ingredients.yaml`,
  regenerate `mappings/ingredient_mappings.sssom.tsv`, and rerun strict
  validation plus the final SSSOM invariant gates.
