Independent bounded completion finding: `COMBINED37-COMPONENT-GROUNDING-001`.

The frozen, unapplied 37-candidate packet preserves a blanket UNMAPPED disposition for all 16 Marine Broth parts and all nine Difco RCM parts. The source evidence supports at least the three exact references below. Uncertain hydrate forms and undefined peptones do not justify withholding these literal salt identities.

| Exact candidate | Component index (zero-based) | Printed nominal input | Supported existing owner |
|---|---:|---|---|
| TARGET-012, Marine_Broth_2216.yaml, SHA256 `34ce518a98ba30ee826ddd083687df477ab796a28f494b015e5bea82841e4dcf` | 3 | Sodium chloride, 19.45 g/L at standard reconstitution | Nacl.yaml, CHEBI:26710 |
| Same | 7 | Potassium chloride, 0.55 g/L at standard reconstitution | Kcl.yaml, CHEBI:32588 |
| TARGET-032, Reinforced_Clostridial_Medium.yaml, SHA256 `431d24db8ff93084d5cb2260cd016b9d1a466561d618c68a6e2dd4e78c7f2c28` | 4 | Sodium chloride, 5 g/L at standard reconstitution | Nacl.yaml, CHEBI:26710 |

Primary sources: the [Marine manufacturer table](https://cdn.media.interlabdist.com.br/uploads/2021/01/Marine-2216-Agar-e-Broth.pdf), SHA256 `de2504598b1133074ba2239c045958e9a6564dc1b2a2d8f13ab4bac99233199f`, and [Difco RCM table](https://cdn.media.interlabdist.com.br/uploads/2021/01/Reinforced-Clostridial-Medium.pdf), SHA256 `e11b1ff246e72286261ac3d7117711bde8b59669a8ea365fa9dd75d298cb2864`. Exact manufacturer ingredient names agree with the current [sodium chloride ontology definition](https://www.ebi.ac.uk/chebi/CHEBI:26710) and [potassium chloride ontology definition](https://www.ebi.ac.uk/chebi/CHEBI:32588), independently read alongside the complete current MIM owners. No unprinted hydrate, stereochemistry, commercial subproduct or dissolved ion is inferred.

Keep the literal component names, nominal amounts/units and manufacturer adjustment footnotes. Add only the supported MIM_CATALOG references and claim-specific evidence/history. Independently assess the remaining constituents one by one; leave genuinely unresolved form/product claims UNMAPPED. This finding does not authorize blanket mapping of the other salts, peptone or every yeast/extract preparation. Existing #1208 broth-versus-agar, #1224 supplier partition, #1176 peptone, source, role and release obligations remain separate.

Independent counterfactual: adding exactly these three references in memory passes the native closed schema and full 2,957-record overlay partonomy, with no corpus writes. This verifies that the existing native contract accepts the precise supported links; it does not approve the complete owners or publication. Exact before/after cells and owner hashes are in `component-grounding-probe.json` under `preflight/combined37-v3-independent-v1`.

Deduplication: fresh complete #1208/#1224 bodies and comments already cover formulation correction and supplier scope, but not these three missing exact references. This is a coherent addition to the campaign completion work on #1193, cross-linked to #1208/#1224; it need not create another owner/parent-identity issue. Rebind final published origins and independently review the corrected combined bytes before application. The active 37 packet has a declared historical source cutoff, and later worker source corrections also need incorporation.

<!-- mim-fingerprints:combined37-component-grounding-001 -->
