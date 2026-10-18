# `data/ingredients/mapped/Methane.yaml`

## Verdict

Needs curation. The exact ChEBI identity, CAS number, structure, occurrence
count, and `tetrahydridocarbon` synonym pass, but the final SSSOM `other`
column still exports `produces:` process labels as synonyms.

Severity: major.

## Identity

- Reviewed record: `data/ingredients/mapped/Methane.yaml`.
- Identifier and grounding: `identifier: CHEBI:16183` with
  `ontology_mapping.ontology_id: CHEBI:16183`, label `methane`, source `CHEBI`,
  `mapping_quality: EXACT_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Occurrences: eight CultureMech recipes.
- Chemical identity: `cas_rn: 74-82-8`, formula `CH4`, and InChI and SMILES
  copied from ChEBI.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Meso-Erythritol` through `Methane`: exited 0 and wrote zero ERROR rows.
- `uv run --frozen linkml-term-validator validate-data` exited 0 for this
  CHEBI-primary record.

## Evidence

- EBI OLS4 resolves `CHEBI:16183` as active `methane` with CAS `74-82-8`,
  formula `CH4`, the same InChI and SMILES carried in the YAML, and the exact
  `tetrahydridocarbon` synonym.
- PubChem resolves CAS `74-82-8` to CID 297 with formula `CH4` and the same
  InChI carried in the YAML.
- The final SSSOM publishes one `skos:exactMatch` row from `MIM:Methane` to
  `CHEBI:16183`, but two process labels from the raw `produces:` source text
  are still exported in `other`.

## Completeness

- The acetate/formate `produces:` labels describe trait context, not methane
  identity. They can stay as provenance-only YAML strings, but they are not
  synonyms of methane.

## Recommended Edits

- Mark the two `produces:` labels as non-resolving provenance or extend the
  synonym policy so raw production-process text is filtered from final SSSOM
  `other`.
