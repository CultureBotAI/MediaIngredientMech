# `data/ingredients/mapped/Mannan_From_Saccharomyces_Cerevisiae.yaml`

## Verdict

Needs curation. The CAS and local registry exact rows are present, but this
yeast mannan record is still mapped to the source organism `NCIT:C14271`, still
carries an unrelated PubChem amylotetraose structure, still exports
process-qualified raw text in final SSSOM, and has only provisional
`CARBON_SOURCE` evidence.

Severity: major.

## Identity

- Reviewed record:
  `data/ingredients/mapped/Mannan_From_Saccharomyces_Cerevisiae.yaml`.
- Identifier and grounding: `identifier: cas:9036-88-8` with
  `ontology_mapping.ontology_id: NCIT:C14271`, label
  `Saccharomyces cerevisiae`, source `NCIT`,
  `mapping_quality: NARROW_MATCH`, `mapping_status: MAPPED`, and
  `ingredient_type: SINGLE_INGREDIENT`.
- Exact subject: `Mannan from Saccharomyces cerevisiae`.
- CAS: `9036-88-8`.

## Validation

- `uv run --frozen python scripts/validate_strict.py` on the 5-file batch from
  `Mandelic_Acid` through `Mannitol`: exited 0 and wrote zero ERROR rows.
- LinkML term validation was skipped for this CAS-primary record because the
  subject identifier is outside the CHEBI/OBO term adapter scope.

## Evidence

- EBI OLS4 resolves `NCIT:C14271` as active `Saccharomyces cerevisiae`, a
  fungal species, not a mannan polymer or mannose polysaccharide.
- PubChem CID 870 has formula `C24H42O21`, an amylotetraose-like InChI, and is
  not exact to CAS `9036-88-8` yeast mannan; the earlier
  `B-Mannan_Borohydrate_Reduced_Carob_Seed` review found the same bad
  CAS-to-CID structure on the duplicate CAS fallback record.
- The final SSSOM publishes a narrow row to `NCIT:C14271`, exact rows to
  `cas:9036-88-8` and
  `kgmicrobe.compound:mannan_from_saccharomyces_cerevisiae`, and
  `filtered, Mannan from Saccharomyces cerevisiae` as the `other` value on the
  NCIT parent row.
- `reports/duplicate_identifiers.tsv` still groups this record with
  `B-Mannan_Borohydrate_Reduced_Carob_Seed` under duplicate identifier
  `cas:9036-88-8`.

## Completeness

- The exact CAS and `kgmicrobe.compound` registry rows satisfy the local
  registry companion-row pattern.
- `NCIT:C14271` denotes the source organism, not a broader class of the
  curated CAS subject, so the parent row should be removed or replaced.
- The stored PubChem CID, formula, SMILES, and InChI are for the wrong
  carbohydrate structure and should not remain on this record.
- The final SSSOM `other` token is process-qualified raw source text, not a
  clean synonym.
- `CARBON_SOURCE` is backed only by `COMPUTATIONAL_PREDICTION` evidence from a
  curated media-role name-pattern rule with a provisional curator note.

## Recommended Edits

- Remove the `NCIT:C14271` parent mapping unless a true source-organism
  qualifier model is added.
- Remove the incorrect PubChem CID 870 formula/SMILES/InChI payload.
- Reject or filter `filtered, Mannan from Saccharomyces cerevisiae` from final
  SSSOM.
- Remove `CARBON_SOURCE` unless source-backed evidence can be attached.
