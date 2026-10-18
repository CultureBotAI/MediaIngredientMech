"""IngredientRecord.causal_graphs: closed-schema rules and fleet shape parity.

Two contracts, both offline:

* Rule cases. The 21 closed-validation cases the causal-graph design was
  verified against (5 accepted, 16 rejected), run through the write-time gate
  (`validate_ingredient`: closed JSON Schema from the repo schema) on an
  in-memory copy of a real record. A rejected case must fail for its own
  reason -- exactly one error, at the expected path, of the expected kind -- so
  an unrelated regression in the base record cannot make it pass vacuously.

* Fleet parity. CausalGraph, CausalNode, CausalEdge, EvidenceItem and
  ProteinExample are the fleet graph_list shape that culturebotai-claw reads
  with default field names. Their slot names, ranges and requiredness (plus
  multivalued, identifier, inlined_as_list, minimum_cardinality and pattern)
  are compared with CellStructureMech's and TraitMech's copies, vendored under
  tests/fixtures/fleet_graph_shapes/ at pinned commits so CI needs no sibling
  checkout. The computed difference must equal EXPECTED_DELTAS exactly, so
  drift on either side fails, and every intended MIM delta is written down.
"""

from __future__ import annotations

import copy
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pytest
import yaml

from mediaingredientmech.validation.write_validated import validate_ingredient

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "src" / "mediaingredientmech" / "schema" / "mediaingredientmech.yaml"
BASE_RECORD_PATH = ROOT / "data" / "ingredients" / "mapped" / "D-glucose.yaml"
FLEET_FIXTURES = Path(__file__).resolve().parent / "fixtures" / "fleet_graph_shapes"

Record = dict[str, Any]
Mutation = Callable[[Record], object]

# ---------------------------------------------------------------------------
# Rule cases
# ---------------------------------------------------------------------------

# A minimal valid graph on D-glucose: the INGREDIENT anchor and the
# structure-bearing form that is a D-glucose (a STRUCTURAL_FORM bridge).
GRAPH: Record = {
    "graph_id": "g",
    "graph_kind": "ASSIMILATION",
    "scope_status": "REVIEW_NEEDED",
    "explains": ["nutritional_roles#CARBON_SOURCE"],
    "nodes": [
        {
            "node_id": "a",
            "label": "D-glucose",
            "node_type": "INGREDIENT",
            "grounding": "CHEBI:17634",
        },
        {
            "node_id": "b",
            "label": "D-glucopyranose",
            "node_type": "CHEMICAL",
            "grounding": "CHEBI:4167",
        },
    ],
    "edges": [
        {
            "edge_id": "e1",
            "subject": "b",
            "predicate": "is a",
            "predicate_id": "rdfs:subClassOf",
            "object": "a",
            "bridge_kind": "STRUCTURAL_FORM",
            "assertion_basis": ["ONTOLOGY_AXIOM", "CHEMICAL_STRUCTURE"],
            "evidence": [{"reference": "CHEBI:4167", "notes": "asserted subClassOf"}],
        }
    ],
}


@dataclass(frozen=True)
class Case:
    """One closed-validation case; `rejected_at` is None for an accepted record."""

    case_id: str
    title: str
    record: Mutation | None = None  # applied to the record after the graph is attached
    graph: Mutation | None = None  # applied to the graph before it is attached
    with_graph: bool = True
    rejected_at: str | None = None  # JSON path of the single expected error
    because: str = ""  # fragment of that error's message


def _add_tilde_node(graph: Record) -> None:
    graph["nodes"].append(
        {
            "node_id": "c",
            "label": "x",
            "node_type": "CHEMICAL",
            "grounding": "kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29",
        }
    )


EDGE = "/causal_graphs/0/edges/0"
NODE = "/causal_graphs/0/nodes/1"

CASES = [
    Case("P1", "mapped single ingredient"),
    Case("P2", "untyped record may carry a graph", record=lambda r: r.pop("ingredient_type")),
    Case("P3", "'~' grounding allowed", graph=_add_tilde_node),
    Case("P4", "record without graphs unaffected", with_graph=False),
    Case(
        "P5",
        "SPECIATION graph NONMECHANISTIC",
        graph=lambda g: g.update(graph_kind="SPECIATION", scope_status="NONMECHANISTIC"),
    ),
    Case(
        "N1",
        "NAMED_MEDIUM with graph",
        record=lambda r: r.update(ingredient_type="NAMED_MEDIUM"),
        rejected_at="/",
        because="should not be valid under {'required': ['causal_graphs']}",
    ),
    Case(
        "N2",
        "UNMAPPED with graph",
        record=lambda r: r.update(mapping_status="UNMAPPED"),
        rejected_at="/mapping_status",
        because="'MAPPED' was expected",
    ),
    Case(
        "N3",
        "empty evidence",
        graph=lambda g: g["edges"][0].update(evidence=[]),
        rejected_at=f"{EDGE}/evidence",
        because="[]",
    ),
    Case(
        "N4",
        "predicate_id outside closed set",
        graph=lambda g: g["edges"][0].update(predicate_id="RO:9999999"),
        rejected_at=f"{EDGE}/predicate_id",
        because="'RO:9999999' is not one of",
    ),
    Case(
        "N5",
        "UniProtKB grounding",
        graph=lambda g: g["nodes"][1].update(grounding="UniProtKB:P20166"),
        rejected_at=f"{NODE}/grounding",
        because="'UniProtKB:P20166' does not match",
    ),
    Case(
        "N6",
        "TAXON node type",
        graph=lambda g: g["nodes"][1].update(node_type="TAXON"),
        rejected_at=f"{NODE}/node_type",
        because="'TAXON' is not one of",
    ),
    Case(
        "N7",
        "malformed explains",
        graph=lambda g: g.update(explains=["nutritional_roles:CARBON_SOURCE"]),
        rejected_at="/causal_graphs/0/explains/0",
        because="'nutritional_roles:CARBON_SOURCE' does not match",
    ),
    Case(
        "N8",
        "missing edge_id",
        graph=lambda g: g["edges"][0].pop("edge_id"),
        rejected_at=EDGE,
        because="'edge_id' is a required property",
    ),
    Case(
        "N9",
        "stoichiometry off ION_PART",
        graph=lambda g: g["edges"][0].update(stoichiometry=2),
        rejected_at=f"{EDGE}/bridge_kind",
        because="'ION_PART' was expected",
    ),
    Case(
        "N10",
        "NCBITaxon grounding",
        graph=lambda g: g["nodes"][1].update(grounding="NCBITaxon:83333"),
        rejected_at=f"{NODE}/grounding",
        because="'NCBITaxon:83333' does not match",
    ),
    Case(
        "N11",
        "missing graph_kind",
        graph=lambda g: g.pop("graph_kind"),
        rejected_at="/causal_graphs/0",
        because="'graph_kind' is a required property",
    ),
    Case(
        "N12",
        "empty edges",
        graph=lambda g: g.update(edges=[]),
        rejected_at="/causal_graphs/0/edges",
        because="[]",
    ),
    Case(
        "N13",
        "unknown edge field (closed)",
        graph=lambda g: g["edges"][0].update(taxon_scope=["NCBITaxon:2"]),
        rejected_at=EDGE,
        because="'taxon_scope' was unexpected",
    ),
    Case(
        "N14",
        "missing assertion_basis",
        graph=lambda g: g["edges"][0].pop("assertion_basis"),
        rejected_at=EDGE,
        because="'assertion_basis' is a required property",
    ),
    Case(
        "N15",
        "ncbi.assembly grounding",
        graph=lambda g: g["nodes"][1].update(grounding="ncbi.assembly:GCA_000009045"),
        rejected_at=f"{NODE}/grounding",
        because="'ncbi.assembly:GCA_000009045' does not match",
    ),
    Case(
        "N16",
        "SPECIATION graph marked MECHANISTIC",
        graph=lambda g: g.update(graph_kind="SPECIATION", scope_status="MECHANISTIC"),
        rejected_at="/causal_graphs/0/scope_status",
        because="'NONMECHANISTIC' was expected",
    ),
]


@pytest.fixture(scope="module")
def base_record() -> Record:
    record = yaml.safe_load(BASE_RECORD_PATH.read_text(encoding="utf-8"))
    # The cases rely on these facts about the real record. Fail loudly, not
    # vacuously, if curation ever changes them.
    assert record["identifier"] == "CHEBI:17634"
    assert record["mapping_status"] == "MAPPED"
    assert record["ingredient_type"] == "SINGLE_INGREDIENT"
    # Once D-glucose carries its own graph, P4 must still see a graphless record.
    record.pop("causal_graphs", None)
    return record


def _build(case: Case, base: Record) -> Record:
    record = copy.deepcopy(base)
    if case.with_graph:
        graph = copy.deepcopy(GRAPH)
        if case.graph is not None:
            case.graph(graph)
        record["causal_graphs"] = [graph]
    if case.record is not None:
        case.record(record)
    return record


def test_every_design_case_is_ported() -> None:
    ids = sorted(case.case_id for case in CASES)
    expected = sorted([f"P{i}" for i in range(1, 6)] + [f"N{i}" for i in range(1, 17)])
    assert ids == expected


@pytest.mark.parametrize("case", CASES, ids=[case.case_id for case in CASES])
def test_closed_schema_rule_case(case: Case, base_record: Record) -> None:
    errors = validate_ingredient(
        _build(case, base_record), target_class="IngredientRecord", schema_path=SCHEMA_PATH
    )
    messages = [error.message for error in errors]
    if case.rejected_at is None:
        assert messages == [], f"{case.case_id} ({case.title}) should validate"
        return
    assert len(messages) == 1, f"{case.case_id} ({case.title}): {messages}"
    (message,) = messages
    assert message.endswith(f" in {case.rejected_at}"), message[-300:]
    assert case.because in message, message[-300:]


# ---------------------------------------------------------------------------
# Fleet parity
# ---------------------------------------------------------------------------

# The sibling commits the fixtures were vendored from. Moving a pin means
# re-vendoring the fixture and reconciling EXPECTED_DELTAS in the same change.
PINNED = {
    "cellstructuremech": "55c4e773da4e6638a17ccc68780b3005f9f94e67",
    "traitmech": "84c3430f1f99744a682979eb5523dba4e05bfaa0",
}
GRAPH_CLASSES = ("EvidenceItem", "CausalGraph", "CausalNode", "CausalEdge", "ProteinExample")
SHAPE_KEYS = (
    "range",
    "required",
    "multivalued",
    "identifier",
    "inlined_as_list",
    "minimum_cardinality",
    "pattern",
)

LOCAL_ID = r"^[a-z][a-z0-9_]*$"
FLEET_CURIE = r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._-]+$"
MIM_GROUNDING = (
    r"^(?!(?:UniProtKB|NCBITaxon|ncbi\.assembly|kgmicrobe\.strain|insdc|RefSeq|GenBank|ENA"
    r"|biosample|bioproject|img\.taxon|patric|gtdb):)[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._~-]+$"
)
MIM_XREF = r"^[A-Za-z][A-Za-z0-9._-]*:[A-Za-z0-9._~-]+$"
REFERENCE = r"^(?:[A-Za-z][A-Za-z0-9._-]*:\S+|https?://\S+)$"
UNIPROT_ACCESSION = (
    r"^UniProtKB:(?:[OPQ][0-9][A-Z0-9]{3}[0-9]|[A-NR-Z][0-9](?:[A-Z][A-Z0-9]{2}[0-9]){1,2})$"
)


def _delta(
    only_in_mim: tuple[str, ...] = (),
    only_in_sibling: tuple[str, ...] = (),
    changed: dict[str, tuple[Any, Any]] | None = None,
) -> dict[str, Any]:
    """A class-shape difference; `changed` maps `slot.key` to (sibling, MIM)."""
    return {
        "only_in_mim": sorted(only_in_mim),
        "only_in_sibling": sorted(only_in_sibling),
        "changed": dict(changed or {}),
    }


# Deltas shared by both siblings: each is a MIM delta of spec section 2.
_GRAPH_DELTAS = {
    "graph_id.pattern": (None, LOCAL_ID),
    "nodes.minimum_cardinality": (None, 1),  # TaxonMech #66 precedent
    "edges.minimum_cardinality": (None, 1),
}
_NODE_DELTAS = {
    "node_id.pattern": (None, LOCAL_ID),
    # `~` in the local part (five MIM identifiers use it) and the genome firewall.
    "grounding.pattern": (FLEET_CURIE, MIM_GROUNDING),
    "xrefs.pattern": (FLEET_CURIE, MIM_XREF),
}
_EDGE_DELTAS = {
    # A closed predicate vocabulary; an enum range needs no CURIE pattern.
    "predicate_id.range": ("string", "IngredientGraphPredicateEnum"),
    "predicate_id.required": (False, True),
    "predicate_id.pattern": (FLEET_CURIE, None),
    "evidence.minimum_cardinality": (None, 1),
}
_EDGE_SLOTS = ("edge_id", "bridge_kind", "stoichiometry", "assertion_basis")

EXPECTED_DELTAS: dict[str, dict[str, dict[str, Any]]] = {
    # MIM keeps CellStructureMech's slot names, ranges and requiredness for the
    # four graph classes; ProteinExample follows TraitMech instead.
    "cellstructuremech": {
        "EvidenceItem": _delta(),
        "CausalGraph": _delta(
            only_in_mim=("explains", "organism_scope"),
            changed={
                **_GRAPH_DELTAS,
                # Each Mech names its own graph kinds (CellStructureMech: ASSEMBLY, ...).
                "graph_kind.range": ("GraphKindEnum", "IngredientGraphKindEnum"),
            },
        ),
        "CausalNode": _delta(
            # target_mech is MIM's; the other four are TraitMech's protein-node slots.
            only_in_mim=(
                "target_mech",
                "grounding_status",
                "grounding_notes",
                "gene_symbols",
                "protein_examples",
            ),
            changed=_NODE_DELTAS,
        ),
        "CausalEdge": _delta(only_in_mim=_EDGE_SLOTS, changed=_EDGE_DELTAS),
        "ProteinExample": _delta(
            # TraitMech's shape: its version/proteome slots, required role and
            # strict accession pattern.
            only_in_mim=("proteome_id", "entry_version", "sequence_version"),
            changed={
                "uniprot_id.pattern": (r"^UniProtKB:[A-Z0-9]+$", UNIPROT_ACCESSION),
                "role.required": (False, True),
                "evidence.minimum_cardinality": (None, 1),
            },
        ),
    },
    # Where TraitMech and CellStructureMech differ, MIM follows CellStructureMech
    # (graph_kind, required scope_status, reference pattern, component_ref, and
    # no `operon` node slot).
    "traitmech": {
        "EvidenceItem": _delta(changed={"reference.pattern": (None, REFERENCE)}),
        "CausalGraph": _delta(
            only_in_mim=("graph_kind", "explains", "organism_scope"),
            changed={**_GRAPH_DELTAS, "scope_status.required": (False, True)},
        ),
        "CausalNode": _delta(
            only_in_mim=("target_mech", "component_ref"),
            only_in_sibling=("operon",),
            changed=_NODE_DELTAS,
        ),
        "CausalEdge": _delta(only_in_mim=_EDGE_SLOTS, changed=_EDGE_DELTAS),
        "ProteinExample": _delta(changed={"evidence.minimum_cardinality": (None, 1)}),
    },
}

# Enums whose permissible values MIM shares exactly with the sibling.
SHARED_ENUMS = {
    "cellstructuremech": ("CausalGraphScopeEnum", "UniProtEntryStatusEnum"),
    "traitmech": ("CausalGraphScopeEnum", "UniProtEntryStatusEnum", "ProteinGroundingStatusEnum"),
}
# Node types MIM adds to the sibling's vocabulary (it removes none; no TAXON).
NODE_TYPE_ADDITIONS = {
    "cellstructuremech": {"INGREDIENT"},
    "traitmech": {"INGREDIENT", "STRUCTURE"},
}


def _load(path: Path) -> dict[str, Any]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def mim_schema() -> dict[str, Any]:
    return _load(SCHEMA_PATH)


def _fixture(slug: str) -> dict[str, Any]:
    return _load(FLEET_FIXTURES / f"{slug}.yaml")


def _shape(attr: dict[str, Any] | None, default_range: str) -> dict[str, Any]:
    attr = attr or {}
    return {
        "range": attr.get("range", default_range),
        "required": bool(attr.get("required", False)),
        "multivalued": bool(attr.get("multivalued", False)),
        "identifier": bool(attr.get("identifier", False)),
        "inlined_as_list": bool(attr.get("inlined_as_list", False)),
        "minimum_cardinality": attr.get("minimum_cardinality"),
        "pattern": attr.get("pattern"),
    }


def _class_delta(
    mim_attrs: dict[str, Any], sibling_attrs: dict[str, Any], sibling_default_range: str
) -> dict[str, Any]:
    changed = {}
    for slot in sorted(mim_attrs.keys() & sibling_attrs.keys()):
        mim = _shape(mim_attrs[slot], "string")
        sibling = _shape(sibling_attrs[slot], sibling_default_range)
        for key in SHAPE_KEYS:
            if mim[key] != sibling[key]:
                changed[f"{slot}.{key}"] = (sibling[key], mim[key])
    return _delta(
        only_in_mim=tuple(mim_attrs.keys() - sibling_attrs.keys()),
        only_in_sibling=tuple(sibling_attrs.keys() - mim_attrs.keys()),
        changed=changed,
    )


def _values(schema: dict[str, Any], enum: str) -> set[str]:
    return set(schema["enums"][enum].get("permissible_values") or {})


def test_mim_schema_default_range_is_string(mim_schema: dict[str, Any]) -> None:
    # _shape fills an omitted MIM range with "string"; keep that true.
    assert mim_schema["default_range"] == "string"


@pytest.mark.parametrize("slug", sorted(PINNED))
def test_fleet_fixture_is_the_pinned_vendored_copy(slug: str) -> None:
    path = FLEET_FIXTURES / f"{slug}.yaml"
    fixture = _load(path)
    source = fixture["source"]
    assert source["commit"] == PINNED[slug]
    # The human-readable header records the same commit as the data.
    assert f"#   commit:     {PINNED[slug]}\n" in path.read_text(encoding="utf-8")
    assert source["default_range"] == "string"
    assert set(GRAPH_CLASSES) <= set(fixture["classes"])
    assert source["record_class"] in fixture["classes"]


@pytest.mark.parametrize(
    ("slug", "class_name"), [(slug, name) for slug in sorted(PINNED) for name in GRAPH_CLASSES]
)
def test_graph_class_matches_the_fleet_copy_except_declared_deltas(
    slug: str, class_name: str, mim_schema: dict[str, Any]
) -> None:
    fixture = _fixture(slug)
    mim_class = mim_schema["classes"][class_name]
    sibling_class = fixture["classes"][class_name]
    # Raw `attributes` are the whole shape only without inheritance or slot_usage.
    for definition in (mim_class, sibling_class):
        assert not {"is_a", "mixins", "slots", "slot_usage"} & definition.keys()
    actual = _class_delta(
        mim_class["attributes"], sibling_class["attributes"], fixture["source"]["default_range"]
    )
    assert actual == EXPECTED_DELTAS[slug][class_name]


@pytest.mark.parametrize("slug", sorted(PINNED))
def test_record_graph_slot_matches_the_fleet(slug: str, mim_schema: dict[str, Any]) -> None:
    fixture = _fixture(slug)
    record_class = fixture["classes"][fixture["source"]["record_class"]]
    sibling = record_class["attributes"]["causal_graphs"]
    mim = mim_schema["classes"]["IngredientRecord"]["attributes"]["causal_graphs"]
    assert _shape(mim, "string") == _shape(sibling, fixture["source"]["default_range"])


@pytest.mark.parametrize("slug", sorted(PINNED))
def test_graph_enums_match_the_fleet(slug: str, mim_schema: dict[str, Any]) -> None:
    fixture = _fixture(slug)
    for enum in SHARED_ENUMS[slug]:
        assert _values(mim_schema, enum) == _values(fixture, enum), enum
    mim_types = _values(mim_schema, "CausalNodeTypeEnum")
    sibling_types = _values(fixture, "CausalNodeTypeEnum")
    assert sibling_types - mim_types == set()
    assert mim_types - sibling_types == NODE_TYPE_ADDITIONS[slug]
