# `data/ingredients/mapped/Rosmarinic_Acid.yaml`

**Verdict**: needs curation, major issue.

**Identity**: `Rosmarinic acid` maps exactly to active, defining
`CHEBI:17226` / `rosmarinic acid`. Fresh OLS4 lookup resolved the ChEBI term
with the same formula, InChI, and SMILES as the record.

**Validation**: `uv run --frozen python scripts/validate_strict.py
data/ingredients/mapped/Rosaramicin.yaml
data/ingredients/mapped/Roseoflavin.yaml
data/ingredients/mapped/Rosmarinic_Acid.yaml
data/ingredients/mapped/Rosuvastatin_Calcium.yaml
data/ingredients/mapped/Rotenone.yaml` passed for the 5-file batch with 0 ERROR
rows. Direct `linkml-term-validator validate-data` with `--labels` passed for
the same 5 files.

**Evidence**: The exact ChEBI mapping is sound and CHEBI:17226 lists the
curated long IUPAC label as an exact synonym, so that part of final SSSOM row
2531 is safe. The per-record YAML agrees with the regenerated aggregate row
when keyed by `(identifier, preferred_term)`.

`chemical_properties.cas_rn` stores `20283-92-5`, and final SSSOM row 2531
exports that as `CAS:20283-92-5`; that CAS is not exact evidence for the
current subject. The CHEBI:17226 term cross-references `537-15-5` instead, and
its InChI carries the trans double-bond layer but no defined stereocenter.
Fresh PubChem lookup of `20283-92-5` resolved the same formula with an
additional chiral layer in the InChI, so the stored CAS describes a narrower
form than the exact CHEBI target.

**Completeness**: Hidden and ignored inclusive search across `data`, `src`,
`tests`, `mappings`, `scripts`, and `reports` found no independent live support
for `20283-92-5` beyond the CultureBotHT-derived record copies, generated
indexes, SSSOM row, and historical backups. No roles or components are
asserted.

**Recommended Edits**: Revisit `data/ingredients/mapped/Rosmarinic_Acid.yaml`:
either replace `chemical_properties.cas_rn: 20283-92-5` with an exact CAS for
`CHEBI:17226` or drop the CAS until a source-backed exact xref is available,
then regenerate final SSSOM so row 2531 no longer publishes `CAS:20283-92-5` as
a synonym for the broader rosmarinic-acid subject.
