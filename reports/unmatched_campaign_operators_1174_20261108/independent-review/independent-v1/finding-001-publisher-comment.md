Independent review also reproduced the #1194 omission at the outer publisher boundary in provisional `campaign_publication.py` SHA256 `f7350ba3487e12cf4ecd4abd85e6fb3663fe0eb454fcd1483602072eeba29274`.

The publisher checks the owner proof first, performs generation/receipt/policy work, then verifies captured files without repeating complete membership. A deterministic late unmapped-owner addition during the generation boundary makes `validate` return verified with a changed inventory. Fixing only source `verify_completed` is insufficient: the outer publisher must recheck its current owner proof/inventory before its own final return.

This second fixture explicitly mocks the owner-proof and generation boundaries; native row/policy/receipt/filesystem boundaries remain real. Its unchanged positive passes. It demonstrates validation order, not a full native-generation exploit. No maintained source was edited.

Addendum SHA256 `9ea2d071928aa60862d8a0473cdfd36b24bd0df155f82b430644d144b117c415`; probe `72057ff932a1e999e0dd23fbefbfa78a7c6d12764267939e09b141c42f4cd47e`; result `e1825551de860f11959d3cabae99cd4176b285980913e9c9be78e8e164a458ae`. Both operator authors have the preserved counterexamples for repair and independent re-review.
