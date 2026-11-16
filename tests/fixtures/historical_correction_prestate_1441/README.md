# Historical correction evidence input (#1441)

`source.json.gz` contains the exact source-label writer bytes recorded as an
input by the immutable #1111 evidence manifest. It is read as evidence, not
executed. The current correction writer and its dependency capture stay intact.

Source object: `21e76ee324a8a04bb4e5c1d48363b647020042d8:scripts/curate_step7c_source_labels.py`.
Source SHA256: `245c02dac2fb1b2101d14eb261ab16a186bf3d2d3980e8f8d56adda178e82e67`
(19,583 bytes). The archive uses schema version 1, that source revision and one
base64 file member; JSON is sorted and compact with a final newline, and gzip
uses mtime 0. Archive SHA256:
`8bab165a062573a3af61e88265252bb9a47408b6a496d63a8dd024bdd4be61a6`.

The test helper authenticates the original correction manifest, every one of
its eight file inputs, and all six protected publication anchors before creating
a new isolated evidence root. Only the exact hash-bound historical correction
test module and its unchanged writer receive temporary evidence-root bindings;
the bindings are restored afterward. Current validation is not redirected by
this helper. The separate existing pre-mint schema fixture retains its original
scope.

Original test modules, historical manifests, source receipts, current writers,
current additional-assertion capture and the original anchor archive are unchanged.

Validation for this repair used Python 3.13.2 and the existing immutable Claw
transaction source at `7070392fcb5e31282499a599f7147b56b96e5aca`, with no package
installation. The focused context/anchor controls passed 24 tests. The complete
original source-label, corrective-note and anchor-adapter modules passed 89
tests, including native transaction, completed replay and reservation-race cases;
neither run skipped a case. Ruff passes the four changed Python files, Black
passes the three newly formatted helper/fixture files, and mypy reports no issue
in the new context helper. These are fixture tests, not campaign source or
publication execution.
