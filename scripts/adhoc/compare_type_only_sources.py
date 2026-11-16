"""Compare proposed type-only sources for issue #1430 (2026-11-15).

Purpose: qualify a bounded annotation repair without executing historical code.
Inputs: explicit original/proposed UTF-8 Python paths and named typing imports.
Outputs: JSON to stdout and, optionally, a new output file; nonzero on mismatch.

Report raw compiled-code differences before normalization. Normalization permits
bare annotation metadata and explicitly selected typing imports; those additions
can change metadata/import behavior. This is not universal runtime equivalence,
source authentication, a sandbox proof, or replacement canary evidence. Guards,
assignments, calls and annotations with assigned values remain in the comparison.
Neither input is imported or executed. Python/compiler identity is reported.
"""

from __future__ import annotations

import argparse
import ast
import dis
import hashlib
import json
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
    instructions = list(dis.get_instructions(code))

    def is_class_line_store(index):
        return (
            index + 1 < len(instructions)
            and instructions[index + 1].opname == "STORE_NAME"
            and instructions[index + 1].argval == "__firstlineno__"
        )

    # Python 3.13 stores class line metadata in co_consts too. Normalize it only
    # when that constant slot has no executable use outside the metadata store.
    line_slots = {
        instruction.arg
        for index, instruction in enumerate(instructions)
        if instruction.opname == "LOAD_CONST"
        and is_class_line_store(index)
        and all(
            is_class_line_store(other)
            for other, value in enumerate(instructions)
            if value.opname == "LOAD_CONST" and value.arg == instruction.arg
        )
    }

    def constant(value):
        if isinstance(value, types.CodeType):
            return fingerprint(value)
        if isinstance(value, tuple):
            return tuple(constant(item) for item in value)
        if isinstance(value, frozenset):
            return frozenset(constant(item) for item in value)
        return value

    return tuple((field, getattr(code, field)) for field in CODE_FIELDS) + (
        (
            "co_consts",
            tuple(
                ("compiler-class-firstlineno",) if index in line_slots else constant(item)
                for index, item in enumerate(code.co_consts)
            ),
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
    def __init__(self, imports):
        self.imports = set(imports)

    def visit_AnnAssign(self, node):
        return None if node.value is None else self.generic_visit(node)

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
    for name in sorted(left.keys() | right.keys()):
        a, b = left[name], right[name]
        if [fingerprint(code) for code in a] != [fingerprint(code) for code in b]:
            differing.append(name)
    normalized = []
    for raw in (original, proposed):
        tree = RemoveTypeMetadata(imports).visit(ast.parse(raw))
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
        "normalized_type_only_equivalent": fingerprint(normalized[0]) == fingerprint(normalized[1]),
        "normalization": {"bare_annotations": True, "typing_imports": sorted(imports)},
        "ignored_metadata": [
            "co_firstlineno",
            "co_linetable",
            "co_filename",
            "exclusive compiler class __firstlineno__ constant",
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
