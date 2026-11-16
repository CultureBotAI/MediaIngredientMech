"""Compare proposed type-only sources for issues #1430/#1432/#1433/#1434 (2026-11-15).

Purpose: qualify a bounded annotation repair without executing historical code.
Inputs: explicit original/proposed UTF-8 Python paths and named typing imports.
Outputs: JSON to stdout and, optionally, a new output file; nonzero on mismatch.

Report raw compiled-code differences before normalization. Normalization permits
simple-name bare annotations with postponed evaluation and selected typing imports; those additions
can change metadata/import behavior. This is not universal runtime equivalence,
source authentication, a sandbox proof, or replacement canary evidence. Guards,
assignments, calls and annotations with assigned values remain in the comparison.
Function/method code must also remain unchanged before normalization, so local
binding changes cannot disappear. Scalar constant types and floating-point bits
are preserved. Neither input is imported or executed; interpreter identity is reported.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import inspect
import json
import marshal
import sys
import types
from collections import defaultdict
from pathlib import Path

CODE_FIELDS = (
    "co_argcount",
    "co_posonlyargcount",
    "co_kwonlyargcount",
    "co_nlocals",
    "co_stacksize",
    "co_flags",
    "co_code",
    "co_names",
    "co_varnames",
    "co_freevars",
    "co_cellvars",
    "co_name",
    "co_qualname",
    "co_exceptiontable",
)


def fingerprint(code):
    def constant(value):
        if isinstance(value, types.CodeType):
            return ("code", fingerprint(value))
        if isinstance(value, tuple):
            return ("tuple", tuple(constant(item) for item in value))
        if isinstance(value, frozenset):
            return ("frozenset", frozenset(constant(item) for item in value))
        return (type(value).__name__, marshal.dumps(value))

    return tuple((field, getattr(code, field)) for field in CODE_FIELDS) + (
        (
            "co_consts",
            tuple(constant(item) for item in code.co_consts),
        ),
    )


def inventory(code):
    result = defaultdict(list)

    def visit(value):
        result[value.co_qualname].append(value)
        for item in value.co_consts:
            if isinstance(item, types.CodeType):
                visit(item)

    visit(code)
    return result


class RemoveTypeMetadata(ast.NodeTransformer):
    def __init__(self, imports, postponed_annotations):
        self.imports = set(imports)
        self.postponed_annotations = postponed_annotations

    def visit_AnnAssign(self, node):
        # Attribute/subscript targets can execute calls even without a value.
        # Without postponed annotations, annotation expressions can also execute.
        if (
            self.postponed_annotations
            and node.value is None
            and isinstance(node.target, ast.Name)
            and node.simple == 1
        ):
            return None
        return self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module == "typing":
            node.names = [item for item in node.names if item.name not in self.imports]
            if not node.names:
                return None
        return node


def compare(original, proposed, imports=()):
    before, after = [
        compile(raw, "<compared-source>", "exec", dont_inherit=True) for raw in (original, proposed)
    ]
    left, right = inventory(before), inventory(after)
    differing = []
    function_changes = []
    for name in sorted(left.keys() | right.keys()):
        a, b = left[name], right[name]
        if [fingerprint(code) for code in a] != [fingerprint(code) for code in b]:
            differing.append(name)
            if any(code.co_flags & inspect.CO_NEWLOCALS for code in (*a, *b)):
                function_changes.append(name)
    normalized = []
    for raw in (original, proposed):
        tree = ast.parse(raw)
        postponed = any(
            isinstance(node, ast.ImportFrom)
            and node.module == "__future__"
            and node.level == 0
            and any(item.name == "annotations" for item in node.names)
            for node in tree.body
        )
        tree = RemoveTypeMetadata(imports, postponed).visit(tree)
        # Reparse canonical text so line offsets cannot influence compiler NOPs.
        normalized.append(
            compile(ast.unparse(tree), "<compared-source>", "exec", dont_inherit=True)
        )
    return {
        "python": sys.version,
        "original_sha256": hashlib.sha256(original.encode()).hexdigest(),
        "proposed_sha256": hashlib.sha256(proposed.encode()).hexdigest(),
        "raw_differing_code_objects": differing,
        "code_objects_checked": sum(map(len, left.values())),
        "raw_code_equivalent": fingerprint(before) == fingerprint(after),
        "function_code_changes": function_changes,
        "normalized_structure_equivalent": fingerprint(normalized[0]) == fingerprint(normalized[1]),
        "normalized_type_only_equivalent": (
            not function_changes and fingerprint(normalized[0]) == fingerprint(normalized[1])
        ),
        "normalization": {
            "bare_annotations": "simple names with postponed evaluation only",
            "typing_imports": sorted(imports),
        },
        "ignored_metadata": [
            "co_firstlineno",
            "co_linetable",
            "co_filename",
        ],
        "compared_fields": [*CODE_FIELDS, "co_consts recursively"],
        "scope": "Compile only. Input modules are never imported or executed. Raw differences remain disclosed.",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("original", type=Path)
    parser.add_argument("proposed", type=Path)
    parser.add_argument("--ignore-typing-import", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = compare(
        args.original.read_text(), args.proposed.read_text(), args.ignore_typing_import
    )
    raw = json.dumps(result, indent=2) + "\n"
    if args.output:
        with args.output.open("x") as stream:
            stream.write(raw)
    sys.stdout.write(raw)
    return 0 if result["normalized_type_only_equivalent"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
