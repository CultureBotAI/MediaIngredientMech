# Original-source review of the three withdrawn identities

All three identity findings are resolved with recovered source evidence. The
review did not choose an isomer from a truncated label or substitute a PubChem
name-search hit for the original registry identity. The applied, hash-bound
before/after records are in `identity-plan.json`.

| Historical source label | Reviewed identity | Disposition |
| --- | --- | --- |
| 2-tetrachloroethane | CHEBI:36026, 1,1,2,2-tetrachloroethane | Exact mapping from the complete original source label and explicit BacDive ChEBI link |
| 2-dimethylsuccinic Acid | CHEBI:86537, 2,2-dimethylsuccinic acid | Exact mapping from all four original source rows; reject historical 2,3-isomer CHEBI:167506 |
| Artepaulin | cas:13902-54-0 | Restore original CAS registry fallback, corroborated by original CSV, KNApSAcK name/CAS association, and exact stereochemical InChI agreement with PubChem |

## MicrobeDecoder source recovery

An ignored-inclusive search located the original archive
`microbe_decoder/database_raw.zip`, member `file1725e5e9d8.csv`, and the parsed
KG-Microbe `data/raw/database.csv` in the sibling checkout. Both are read-only
inputs. The files are not byte-identical; the five relevant source rows,
including their CSV row numbers and full metabolite cells, are identical.
`microbedecoder-source-recovery.json` records both file hashes and all five rows.
No inference about a missing locant is needed:

- Row 4887 contains the complete `1,1,2,2-tetrachloroethane` label and BacDive
  ID 140462. The current [original BacDive record](https://bacdive.dsmz.de/strain/140462)
  gives that label and CHEBI:36026. Its underlying reference is
  [Key et al., 2017](https://doi.org/10.1099/ijsem.0.001819).
- Rows 1840, 7744, 8673, and 14465 contain `2,2-dimethylsuccinic acid` and
  BacDive IDs [140942](https://bacdive.dsmz.de/strain/140942),
  [168456](https://bacdive.dsmz.de/strain/168456),
  [140923](https://bacdive.dsmz.de/strain/140923), and
  [158680](https://bacdive.dsmz.de/strain/158680). Each current BacDive record
  explicitly associates the metabolite with CHEBI:86537. These are the four
  source occurrences imported by MIM.

The current ChEBI entries independently establish the identities:
[CHEBI:36026](https://www.ebi.ac.uk/chebi/CHEBI:36026) and
[CHEBI:86537](https://www.ebi.ac.uk/chebi/CHEBI:86537). The raw truncated labels
remain available for source lookup. Earlier unsupported reconstructions remain
in curation history. The `REJECTED_LABEL` annotation on the now source-proven
1,1,2,2 name is replaced with an exact synonym annotation.

The older raw BacDive JSON also contains negative-assay observations for
2,2-dimethylsuccinic acid. Its total occurrences must not be equated with the
four positive source rows in MicrobeDecoder. Identity resolution here uses the
actual MicrobeDecoder source CSV and the corresponding live BacDive records.

## Artepaulin

The original CultureBotHT `data/raw/google_sheets/compounds_to_cas.csv` row 784
explicitly associates Artepaulin with CAS 13902-54-0; the row and source file hash
are recorded in `artepaulin-original-source.json`.
[KNApSAcK C00013080](https://www.knapsackfamily.com/knapsack_core/information.php?word=C00013080)
also explicitly associates that name and CAS. More decisively, the **complete
stereochemical InChI** in that record is byte-identical to the InChI returned by
[PubChem CID 10977881](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/10977881/property/IUPACName,InChIKey,InChI,MolecularFormula/JSON).
`artepaulin-inchi-comparison.json` records the checked equality, including every
stereochemical layer; this is stronger evidence than matching a formula or the
connectivity prefix alone.

PubChem's name search gives CID 325292 with undefined stereochemistry and CID
73440797 with partial stereochemistry. Its CAS-specific compound omits Artepaulin
from the returned synonym list. That omission did not establish a contradictory
identity. The earlier review was too strong in treating it as proof of a
name/CAS mismatch.

A real database inconsistency remains: KNApSAcK's displayed InChIKey differs from
the key attached to the same full InChI in PubChem. We do not copy that key. The
repair restores only the source-backed CAS fallback and supplied CAS metadata;
it adds no CHEBI:174307 equivalence and no new structure fields.
`external-receipts.json` hashes the retrieved primary API and KNApSAcK responses.
KNApSAcK references Adekenov, Khim. Prir. Soedin. (1983), p. 238; the original
paper's full text was not reviewed and is not claimed as direct evidence.

## Review policy and limits

A semantic review can close an incorrect-identity finding by a documented
withdrawal when the original identity remains unknowable. Such closure means
only that the unsupported claim is absent; it cannot declare the identity
resolved or justify inventing an equivalence. Here the original evidence was
recovered, so all three records can receive supported identities.

This result resolves only these three identity findings. It does not grant
semantic approval to unrelated roles or component assertions. Final graph and
SSSOM regeneration, full-corpus validation, and the release decision are handled
by the parent review workflow.
