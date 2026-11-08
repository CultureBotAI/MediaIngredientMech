Independent #1174 review reproduced missing prospective owner-chain validation before writes in both provisional operators. This is separate from #1194 membership and #1195 loaded-producer binding.

Reviewed source snapshots:
- `src/mediaingredientmech/curate/campaign_owner_apply.py`: `74a448602d8d512a1b12037d88d0eba0a9ac9e1ea55c89e6bd3051afb23f0a99`.
- `src/mediaingredientmech/campaign_publication.py`: `f7350ba3487e12cf4ecd4abd85e6fb3663fe0eb454fcd1483602072eeba29274`.

A valid historical native checkpoint ends the selected existing owner's chain at bytes B, but the exact current source plan proposes A→C. The source operator checks the checkpoint internally and promotion old-path restrictions, without requiring ordinary existing-owner preimages to equal the latest applicable chain endpoint. Real native source prepare/application/completed verification all accept and change that private owner fixture.

The publisher constructs/replays rows without validating the complete prospective owner chain. When historical policy attribution equals A, its optional older-pin bridge does not catch the disconnected endpoint B. Its dry-run accepts; subsequent private application changes canonical and policy before completed native validation raises `Owner receipt chain has a gap`. Success receipts are correctly cleared. The defect is the avoidable preflight miss, not a false success receipt.

The source reproduction uses actual native source application without a mocked owner proof. The publisher reproduction explicitly isolates owner-proof/generation boundaries while keeping native row, receipt, owner-chain and file-write behavior real. The matching-endpoint positive succeeds. No author file or real campaign ingredient was changed.

Before any source or canonical/policy mutation, require each selected existing preimage to match its applicable latest native owner-chain endpoint and validate the complete prospective chain, including create/promotion destination history. Preserve unsupported migration refusals. Do not rewrite or rebase history. Add positive bridge and disconnected-history regression cases that assert all data bytes remain unchanged on refusal; independently re-review final implementation.

Finding `IR-CAMPAIGN-OPERATORS-3`, SHA256 `e7f24f6dc77a449d2a11493e88fb44cc27ab4b78f586fe25f0a8861c3e23c6b4`. Source probe/result: `c8144acaba4523cb5f8fa5495c58dd55fb9c01bba866742e981415f3afa27320` / `72aacc23ef4f283f598282453c844f17f0f080f9868bfe68d2cbb199531fa974`. Publisher probe/result: `a6bbb7873ee1b501332ff4c5d86b3f6ba8d0b1ff3e3de9698aebbcd809d9826b` / `7c1e6444a7f7a537b0ba660a9beae3ad7789ba4aed64893b2cc7056532746756`. Preserved evidence accompanies the implementation PR.

Deduplication: live all-state campaign/chain search returned no match; the full current issue snapshot was also checked. #1174 remains the parent task. No production corruption or scientific identity result is inferred from these private counterexamples.
