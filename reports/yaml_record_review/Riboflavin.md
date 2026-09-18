# `data/ingredients/mapped/Riboflavin.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Riboflavin` maps exactly to active, defining `CHEBI:17015` /
`riboflavin`. Fresh OLS4 lookup resolved the ChEBI term with CAS `83-88-5`,
formula `C17H20N4O6`, and the same InChI as the YAML; fresh PubChem lookup by
the stored CAS resolved CID 493570 with the same formula and InChI.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rhodomycin_A.yaml
data/ingredients/mapped/Rhodomycin_B.yaml data/ingredients/mapped/Ribitol.yaml
data/ingredients/mapped/Riboflavin.yaml
data/ingredients/mapped/Ribonucleic_Acid_From_Torula_Yeast_Type_VI.yaml` passed
for the 5-file batch with 0 ERROR rows. Direct
`linkml-term-validator validate-data` with `--labels` passed for the same 5
files.

**Evidence**: The exact ChEBI identity, CAS, chemical properties, refreshed
2123-occurrence count, and CultureMech `VITAMIN_SOURCE` role pass. The
per-record YAML also agrees with the regenerated aggregate row when keyed by
`(identifier, preferred_term)`.

Final SSSOM row 2507 still exports raw recipe labels in `other`: `Riboflavin
(0.2 mg/ml)`, `Riboflavin (see below)`, and the raw 0.05 microgram/mL
CultureMech label. These are concentration- or recipe-pointer strings, not
true alternate names for `CHEBI:17015`.

The auto-proposed PMID 40609532 mapping evidence is also out of scope. PubMed
resolves the article to a 2025 Cell Metabolism study of microbial riboflavin,
ceramide synthase 3, and colorectal cancer; it mentions riboflavin, but it does
not support this CultureMech ingredient-to-ChEBI identity claim.

**Completeness**: The exact chemical identity is complete enough, and the
vitamin role has CultureMech database evidence. The unsafe data is confined to
three raw occurrence synonyms plus the irrelevant PubMed mapping-evidence row.

**Recommended Edits**: Remove the concentration-qualified and `see below`
CultureMech labels from active exported synonyms and drop or replace the
auto-proposed PubMed evidence under `ontology_mapping.evidence`. Regenerate
final SSSOM and confirm row 2507 no longer exports non-synonym recipe text in
`other`.
