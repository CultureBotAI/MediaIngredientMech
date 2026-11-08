Confirmed private metadata finding before correction: the final #1259 outer handoff at `integration/campaign-suppressions1259-v1/HANDOFF.json`, SHA256 `0b9ed5258a3a9c6e4bffe7a2759ebd2e3cccd170e01bab52654740d45f0c28da`, carries two stale relative locators from the finalizer:

- `patch: implementation.patch` is absent relative to the outer directory. Actual outer file is `implementation-v2.patch`, SHA256 `4ac02fc1e9028ace1f71f6830b088a65ca922b3d3b35f51cfb620726706824c2`.
- `portable_manifest.path: portable/MANIFEST.json` is absent. Actual file is `portable-final/MANIFEST.json`, SHA256 `dbbb96b81b3d6f1d48a6d7811888f002bb521429d1d398142f53754db6c51093`.

Root, the author and a separate archive reviewer confirmed the missing paths and exact existing targets. The inner portable-final handoff `958d29fb02c5f6c8c9571711b1cca487467d9e9344040404b21f28c69232abc8` correctly resolves its patch and check receipts; all191portable members and the four final source/test files remain exact. This is not a code/test defect or missing evidence.

Add an immutable explicit locator/base map after this filing, preserve both original handoffs/manifests, and independently verify the actual four-file patch through the corrected references. No producer/test change or repeated scientific approval follows from fixing these metadata pointers.
