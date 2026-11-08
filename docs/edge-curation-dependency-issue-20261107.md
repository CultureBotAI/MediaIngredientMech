# Separate shared curation contracts from the full orchestration dependency

The native EdgeMech adapter for CLAW #767 needs only the canonical
`kg_microbe_curation` identity and native-assertion validators. A direct optional
dependency on the full `kg-microbe-orchestration` distribution cannot resolve:

- MediaIngredientMech `pyproject.toml` requires `linkml>=1.7.0,<1.10` and
  `linkml-runtime>=1.7.0,<1.10`.
- CLAW commit `1b5391d083ba85ac94e5279c3cba25ac4fde243c` requires
  `linkml>=1.10` and `linkml-runtime>=1.10`.

The bounds have no overlap, including when the dependency is placed in a
native optional extra, because uv resolves all extras into the shared lock.

In-scope mitigation: pin the exact CLAW source revision in native metadata,
verify its Git identity and import origin, and run a dedicated mandatory
integration tier using only that source path and the existing native runtime.
No native LinkML upgrade is included in the adapter PR.

Follow-up: expose the minimal shared identity/review/curation contracts as a
separately installable distribution with explicit small dependencies and
cross-package conformance tests. This requires coordinated CLAW packaging
work and should remain open after the native adapter's source-pin mitigation.
