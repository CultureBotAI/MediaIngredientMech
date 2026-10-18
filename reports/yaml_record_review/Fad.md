# `data/ingredients/mapped/Fad.yaml`

## Verdict

Needs curation, with major role-evidence and duplicate-identity issues. The
exact ChEBI FAD identity, structure fields, CultureMech occurrences, and final
SSSOM synonyms pass, but the `VITAMIN_SOURCE` role is still backed only by a
provisional CHEBI-ancestry inference and the active corpus also has a
`Flavin_Adenine_Dinucleotide` row for the same CAS/synonym identity.

## Identity

- Reviewed record: `data/ingredients/mapped/Fad.yaml`.
- Identifier and grounding: `identifier: CHEBI:16238` with matching
  `ontology_mapping.ontology_id`, canonical label `FAD`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`,
  `kg_microbe_node_id: CHEBI:16238`, and `ingredient_type:
  SINGLE_INGREDIENT`.
- The record has 8 CultureMech recipe occurrences, refreshed from the #337
  occurrence table.
- PubChem lookup by CAS RN `146-14-5` resolved to CID 643975 with formula
  `C27H33N9O15P2` and the same InChI recorded under `chemical_properties`.

## Validation

- `uv run --frozen python scripts/validate_strict.py data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/FSL.yaml data/ingredients/mapped/Fad.yaml data/ingredients/mapped/Farm_soil.yaml --out /tmp/mim_f_batch_strict.tsv`:
  exited 0 for the 5-file batch; the output TSV contained only its header.
- `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Exopolysaccharide.yaml data/ingredients/mapped/FCCP.yaml data/ingredients/mapped/Fad.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord --labels`:
  passed for the CHEBI subset in this mixed batch.

## Evidence

- The matching `data/curated/mapped_ingredients.yaml` entry carries the same
  ChEBI identifier, CAS RN, formula, InChI, SMILES, kg-microbe node ID,
  nutritional role, and refreshed occurrence counts as the per-record YAML.
- The final `mappings/ingredient_mappings.sssom.tsv` row maps `MIM:Fad` to
  `CHEBI:16238` with `skos:exactMatch`. Its six kg-microbe exact synonyms and
  `CAS:146-14-5` `other` token denote FAD; the raw CultureMech
  `Role: Growth factor` / `Properties: ...` text is filtered out and is not
  exported.
- Major: `nutritional_roles.VITAMIN_SOURCE` is supported only by a
  `COMPUTATIONAL_PREDICTION` reference from `infer_roles_from_chebi_ancestry`,
  and that evidence explicitly describes the assertion as provisional.
- Major: the hidden/ignored-inclusive search found
  `data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml`, an active row
  with CAS RN `146-14-5` that also emits `CAS:146-14-5` in the final SSSOM.
  ChEBI itself lists `Flavin adenine dinucleotide` as a synonym of
  `CHEBI:16238`, so these two active MIM rows need a representative or
  broader/narrower decision.
- A hidden/ignored-inclusive search over `data/ingredients`, `data/curated`,
  `mappings`, and `reports/yaml_record_review` for `MIM:Fad`, `CHEBI:16238`,
  `146-14-5`, and related FAD labels found the active FAD row, the active
  flavin adenine dinucleotide row, final SSSOM rows for both, row-review
  provenance, CultureMech recipe memberships, and ignored aggregate backups.

## Completeness

- The exact FAD identity, CultureMech occurrence counts, CAS RN, structure
  fields, ingredient type, kg-microbe cross-reference, and final SSSOM payload
  are populated.
- The nutritional role needs curator evidence or removal, and the active
  overlap with `Flavin_Adenine_Dinucleotide` needs reconciliation.

## Recommended Edits

- Major: either replace the provisional `VITAMIN_SOURCE` inference with
  source-backed evidence or remove the role facet.
- Major: review `data/ingredients/mapped/Fad.yaml` together with
  `data/ingredients/mapped/Flavin_Adenine_Dinucleotide.yaml`, preserve the
  CultureMech occurrences and accepted exact synonyms on the chosen
  representative, avoid exporting `CAS:146-14-5` on two exact identity rows,
  sync `data/curated/mapped_ingredients.yaml`, regenerate
  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus
  the final SSSOM invariant gates.
