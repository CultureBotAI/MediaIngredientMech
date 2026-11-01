The approved #669 rollout requires form review before merging `Sodium_Succinate_Dibasic` with `Sodium_Succinate`. Related: #738, #263 and #320.

The current identifiers agree on anhydrous disodium succinate: CAS 150-90-3, PubChem CID 9020 and CHEBI:63675. That alone does not settle the original generic record's supplied form. Its history includes supplier-derived CAS 6106-21-4 before a target-xref selection. The captured CultureBotHT input (SHA-256 `76b70a1836b25de431c4f5cc27c72bb6b06a223ce33911e93b7681d4fcdb28f9`, line 414) associates sodium succinate with Sigma S2378, 6106-21-4 and 270.14 g/mol. [Sigma S2378](https://www.sigmaaldrich.com/US/en/product/sial/s2378) is the hexahydrate; [Sigma 14160](https://www.sigmaaldrich.com/US/en/product/sial/14160) is a separate anhydrous product. Supplier evidence here is an inspected web extraction, not archived origin HTML. Existing recipe IDs derive from MIM and therefore do not independently settle the conflict.

For the approved bounded rollout, SUPPRESS `Sodium succinate` only on `MIM:Sodium_Succinate_Dibasic / skos:broadMatch / CHEBI:63675`, with a sidecar and unchanged source YAML. The alias is not established as chemically false, so it must not become REJECTED_LABEL. Preserve the explicit CHEBI:63686 hexahydrate control.

Options for the scientific decision:

- Trace the original product/form evidence and explicitly adopt an anhydrous naming convention for the generic source cohort, then merge through guarded writers with complete history, membership union and fresh review.
- If the source scope supports distinct forms, retain distinct identities and the §3 mapping pattern.

Recommendation: retain suppression and leave this issue open until that source scope or explicit evidence-backed convention is settled. No merge, replacement CAS or hydration state is inferred from the current target IDs. The bounded preflight and exact input hashes will accompany the consumer PR; this issue does not approve broader curation.
