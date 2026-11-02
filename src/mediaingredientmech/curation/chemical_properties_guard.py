"""Conservative, record-aware proposals for empty chemistry blocks (#268/#871).

This checks consistency with an existing declared identity, not chemical identity
or scientific approval. Grades (including CAS_RN_LOOKUP) are deliberately absent
from eligibility. Unsupported names/forms require review rather than guessing.
No ontology/cache/network imports occur in the pure preflight.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from collections.abc import Mapping
from copy import deepcopy
from datetime import datetime
from typing import Any

from mediaingredientmech.curation.hydrate_guard import (
    implausible_water_counts,
    is_hydrate_label,
    water_multiplicity,
)

# Same token boundaries as the reviewed regrade_synonym_matches concentration
# guard, extended to explicit preparation vocabulary. This finite grammar is
# not a detector for every possible preparation spelling; missing declarations
# and unknown name equivalences independently refuse below.
_PREPARATION = re.compile(
    r"(?<![a-z0-9])\d+(?:\.\d+)?\s*"
    r"(?:%|[mµμunp]?m(?![a-z])|m?g\s*/\s*m?l(?![a-z]))"
    r"|(?<![a-z])solution(?![a-z])|\bstock\b|\bpreparation\b",
    re.I,
)
_MIXTURE = re.compile(
    r"\b(?:mixture|extract|hydrolysate|peptone|tryptone|casamino|broth|serum|"
    r"plasma|DNA|RNA|polymer|polydisperse)\b",
    re.I,
)
_UNSUPPORTED_QUALIFIER = re.compile(
    r"(?<![a-z])(?:D|L|DL|D,L|R|S)[- ]|\((?:R|S|II|III|IV|VI)\)|"
    r"\b(?:cis|trans|racemic|racemate|enantiomer|stereoisomer)\b",
    re.I,
)
_CURIE = re.compile(r"CHEBI:[1-9][0-9]*\Z")
_HYDRATE_WORD = re.compile(
    r"\b(?:hemi|sesqui|mono|di|tri|tetra|penta|hexa|hepta|octa|nona|deca|undeca|dodeca)*hydrate\b",
    re.I,
)
_HYDRATE_DIGITS = re.compile(r"(?:^|[x×·•・⋅∙.\-−\s])(\d+)\s*H2\s*O(?![0-9])", re.I)
_FORMULA = re.compile(r"(?:[A-Z][a-z]?[0-9]*)+\Z")
_ELEMENTS = frozenset(
    "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og".split()
)


def _name(text: str) -> str:
    """Case/spacing normalization only; never erase counterions or stereo."""
    return " ".join(text.casefold().replace("−", "-").split())


def _hydration(text: str) -> int | None:
    """Fixed integral crystalline label count, zero for no stated hydrate.

    Bare/fractional/variable/contradictory hydrate descriptions return None.
    Counts use the maintained hydrate label primitives, with an extra multiple
    claim check: the existing helper's first matching count is insufficient here.
    """
    if implausible_water_counts(text):
        return None
    if not is_hydrate_label(text):
        return 0
    tokens = _HYDRATE_WORD.findall(text)
    tokens += [m.group(0) for m in _HYDRATE_DIGITS.finditer(text)]
    counts = {water_multiplicity(token) for token in tokens}
    value = water_multiplicity(text)
    if not tokens or None in counts or len(counts) != 1 or value not in counts:
        return None
    if not value or not value.isdigit() or not 1 <= int(value) <= 30:
        return None
    if re.search(r"\banhydrous\b", text, re.I):
        return None
    return int(value)


def _base_name(text: str) -> str:
    text = _HYDRATE_WORD.sub("", text)
    text = _HYDRATE_DIGITS.sub("", text)
    text = re.sub(r"\banhydrous\b", "", text, flags=re.I)
    return _name(text.strip(" ,()-"))


def _label_consistency(label: str, target: str) -> str | None:
    """Only exact names or the same base with matching fixed hydrate states.

    Chemical synonym, salt/counterion, oxidation-state and stereochemical
    equivalence is intentionally not inferred. Retaining all non-hydrate name
    tokens makes an unsupported identity-critical qualifier a refusal in either
    direction. Derived synonym lists never provide permission to enrich.
    """
    left, right = _hydration(label), _hydration(target)
    if left is None or right is None:
        return "AMBIGUOUS_FORM"
    if left != right:
        return "FORM_MISMATCH"
    if _base_name(label) != _base_name(target):
        return "NAME_SCOPE_UNRESOLVED"
    return None


def _declared_labels(record: Mapping[str, Any]) -> tuple[list[str], str | None]:
    preferred = record.get("preferred_term")
    if not isinstance(preferred, str) or not preferred.strip():
        return [], "MISSING_NAME"
    labels = [preferred]
    forms = record.get("supplied_form") or []
    if not isinstance(forms, list):
        return [], "UNSUPPORTED_SUPPLIED_FORM"
    for form in forms:
        if not isinstance(form, Mapping):
            return [], "UNSUPPORTED_SUPPLIED_FORM"
        supplied_name = form.get("name")
        if supplied_name:
            if not isinstance(supplied_name, str):
                return [], "UNSUPPORTED_SUPPLIED_FORM"
            labels.append(supplied_name)
        description = form.get("form")
        if description:
            if not isinstance(description, str):
                return [], "UNSUPPORTED_SUPPLIED_FORM"
            if _PREPARATION.search(description):
                return [], "PREPARATION_SCOPE"
            # Only a bare fixed hydrate/anhydrous declaration plus physical
            # powder/crystal wording can be compared without interpretation.
            remainder = _HYDRATE_WORD.sub("", description)
            remainder = _HYDRATE_DIGITS.sub("", remainder)
            remainder = re.sub(
                r"\b(?:anhydrous|powder|crystal|crystals|crystalline|solid)\b",
                "",
                remainder,
                flags=re.I,
            )
            if remainder.strip(" ,()-"):
                return [], "UNSUPPORTED_SUPPLIED_FORM"
            if (
                is_hydrate_label(description) or re.search(r"\banhydrous\b", description, re.I)
            ) and _hydration(description) != _hydration(preferred):
                return [], "FORM_MISMATCH"
    return labels, None


def chemistry_preflight(record: Mapping[str, Any]) -> str | None:
    """Pure eligibility check; nonempty blocks are handled separately.

    An explicit mapped SINGLE_INGREDIENT with identical canonical CHEBI own
    identity/target is necessary, never sufficient scientific identification.
    No source-derived formula, synonym or method grade supplies missing scope.
    """
    if record.get("mapping_status") != "MAPPED":
        return "INACTIVE_RECORD"
    if record.get("representative"):
        return "RETIRED_RECORD"
    if record.get("ingredient_type") != "SINGLE_INGREDIENT":
        return "UNRESOLVED_INGREDIENT_SCOPE"
    if any(
        record.get(key)
        for key in (
            "components",
            "component_assertion",
            "culturemech_reference",
            "preparation",
            "preparation_notes",
        )
    ):
        return "PREPARATION_SCOPE"
    mapping = record.get("ontology_mapping")
    if not isinstance(mapping, Mapping):
        return "MISSING_GROUNDING"
    own, target = record.get("identifier"), mapping.get("ontology_id")
    if (
        not isinstance(own, str)
        or not _CURIE.fullmatch(own)
        or target != own
        or mapping.get("ontology_source") != "CHEBI"
    ):
        return "OWN_IDENTITY_MISMATCH"
    target_label = mapping.get("ontology_label")
    if not isinstance(target_label, str) or not target_label.strip():
        return "MISSING_TARGET_LABEL"
    labels, reason = _declared_labels(record)
    if reason:
        return reason
    for label in [*labels, target_label]:
        if _PREPARATION.search(label):
            return "PREPARATION_SCOPE"
        if _MIXTURE.search(label):
            return "MIXTURE_SCOPE"
        if _UNSUPPORTED_QUALIFIER.search(label):
            return "UNSUPPORTED_IDENTITY_QUALIFIER"
    for label in labels:
        if reason := _label_consistency(label, target_label):
            return reason
    return None


def _formula_water(formula: str) -> tuple[int, bool] | None:
    """Count separate H2O components of a finite elemental formula.

    Dot components with positive integral coefficients only. No polymers,
    variables, fractional/covalent hydrates, adduct parentheses or guessed
    charge/formula normalization. H2O4P and H2O2 are not water components.
    """
    waters = 0
    other = False
    for part in formula.split("."):
        match = re.fullmatch(r"([1-9][0-9]*)?([A-Z].*)", part)
        if not match:
            return None
        coefficient, atoms = int(match[1] or "1"), match[2]
        if not _FORMULA.fullmatch(atoms):
            return None
        tokens = re.findall(r"([A-Z][a-z]?)([0-9]*)", atoms)
        if any(element not in _ELEMENTS or (count and int(count) < 1) for element, count in tokens):
            return None
        if atoms == "H2O":
            waters += coefficient
        else:
            other = True
    return waters, other


def _formula_atoms(formula: str) -> Counter[str]:
    """Called only after the finite formula grammar succeeds."""
    result: Counter[str] = Counter()
    for part in formula.split("."):
        match = re.fullmatch(r"([1-9][0-9]*)?([A-Z].*)", part)
        assert match is not None
        for element, count in re.findall(r"([A-Z][a-z]?)([0-9]*)", match[2]):
            result[element] += int(match[1] or "1") * int(count or "1")
    return result


def _smiles_atoms(smiles: str) -> Counter[str] | None:
    """Recognise a bounded SMILES token grammar, without chemical equivalence.

    Organic atoms, bracket atoms/ions, bonds, branches and paired ring labels;
    no wildcards, query atoms, polymers, extensions or unparsed text. This is a
    syntax/component refusal guard, not a valence or stereochemistry validator.
    """
    result: Counter[str] = Counter()
    for component in smiles.split("."):
        tokens = re.findall(
            r"\[[^\]\[]+\]|Br|Cl|[BCNOPSFIbcnops]|%[0-9]{2}|[0-9]|[()=#:/\\-]", component
        )
        if "".join(tokens) != component:
            return None
        depth = 0
        rings: Counter[str] = Counter()
        for token in tokens:
            if token == "(":
                depth += 1
            elif token == ")":
                depth -= 1
                if depth < 0:
                    return None
            elif token[0].isdigit() or token.startswith("%"):
                rings[token] += 1
            elif token.startswith("["):
                match = re.fullmatch(
                    r"\[(?:[0-9]+)?([A-Z][a-z]?|[bcnops])(?:@{1,2})?(?:H[0-9]*)?(?:[+-][0-9]*|[+-]{1,3})?(?::[0-9]+)?\]",
                    token,
                )
                if not match or match[1].capitalize() not in _ELEMENTS:
                    return None
                result[match[1].capitalize()] += 1
            elif token[0].isalpha():
                result[token.capitalize()] += 1
        if depth or any(count != 2 for count in rings.values()):
            return None
    return result or None


def _structure_consistency(label: str, props: Mapping[str, Any]) -> str | None:
    formula, inchi, smiles = (props.get(key) for key in ("molecular_formula", "inchi", "smiles"))
    if not all(isinstance(value, str) and value for value in (formula, inchi, smiles)):
        return "MISSING_STRUCTURE_EVIDENCE"
    assert isinstance(formula, str) and isinstance(inchi, str) and isinstance(smiles, str)
    formula_water = _formula_water(formula)
    if not inchi.startswith("InChI=1S/") or len(inchi.split("/")) < 3:
        return "UNSUPPORTED_STRUCTURE"
    inchi_water = _formula_water(inchi.split("/")[1])
    if (
        formula_water is None
        or inchi_water is None
        or "*" in smiles
        or any(ch.isspace() for ch in smiles)
    ):
        return "UNSUPPORTED_STRUCTURE"
    components = smiles.split(".")
    if not components or any(not component for component in components):
        return "UNSUPPORTED_STRUCTURE"
    smiles_waters = sum(component in {"O", "[OH2]", "[H]O[H]"} for component in components)
    smiles_atoms = _smiles_atoms(smiles)
    if smiles_atoms is None:
        return "UNSUPPORTED_STRUCTURE"
    formula_atoms = _formula_atoms(formula)
    inchi_atoms = _formula_atoms(inchi.split("/")[1])
    # InChI protonation layers and implicit SMILES hydrogens make hydrogen
    # totals unsuitable here. All heavy atoms must nevertheless agree.
    for atoms in (formula_atoms, inchi_atoms, smiles_atoms):
        atoms.pop("H", None)
    if formula_atoms != inchi_atoms or formula_atoms != smiles_atoms:
        return "STRUCTURE_COMPOSITION_MISMATCH"
    for name, element in {
        "sodium": "Na",
        "potassium": "K",
        "lithium": "Li",
        "calcium": "Ca",
        "magnesium": "Mg",
        "copper": "Cu",
        "cobalt": "Co",
        "nickel": "Ni",
        "iron": "Fe",
        "chloride": "Cl",
        "bromide": "Br",
    }.items():
        match = re.search(r"\b(mono|di|tri|tetra)?" + name + r"\b", label, re.I)
        if match:
            expected_count = {"mono": 1, "di": 2, "tri": 3, "tetra": 4}.get(
                (match[1] or "").lower()
            )
            if not formula_atoms[element] or (
                expected_count and formula_atoms[element] != expected_count
            ):
                return "COUNTERION_MISMATCH"
    counts = (formula_water[0], inchi_water[0], smiles_waters)
    if len(set(counts)) != 1:
        return "STRUCTURE_WATER_MISMATCH"
    pure_water = (
        not formula_water[1] and not inchi_water[1] and len(components) == smiles_waters == 1
    )
    expected = _hydration(label)
    if pure_water:
        return (
            None
            if formula == "H2O" and _name(label) == "water" and expected == 0
            else "UNSUPPORTED_STRUCTURE"
        )
    if expected is None or counts[0] != expected:
        return "STRUCTURE_FORM_MISMATCH"
    if not formula_water[1] or not inchi_water[1]:
        return "UNSUPPORTED_STRUCTURE"
    return None


def prepare_chemical_properties(
    record: Mapping[str, Any], client: Any = None
) -> tuple[dict[str, Any] | None, str]:
    """Return a new schema-safe proposal and provenance, or a stable refusal.

    Never mutates a record/history. Existing nonempty chemistry (including CAS
    or metadata alone) takes priority and makes zero provider/cache calls.
    Client creation is lazy; the strict method has no legacy fallback.
    """
    existing = record.get("chemical_properties")
    if existing not in (None, {}) or (existing is not None and not isinstance(existing, Mapping)):
        return None, "EXISTING_CHEMISTRY"
    if reason := chemistry_preflight(record):
        return None, reason
    from mediaingredientmech.utils.chemical_properties_client import (
        ChemicalPropertiesClient,
        OlsChemicalProperties,
    )

    if client is None:
        client = ChemicalPropertiesClient(cache_enabled=False)
    fetch = getattr(client, "get_ols_properties", None)
    if not callable(fetch):
        return None, "UNSUPPORTED_CLIENT"
    target = record["ontology_mapping"]["ontology_id"]
    captured_record = deepcopy(record)
    try:
        envelope = fetch(target)
    except Exception:
        return None, "PROVIDER_FAILURE"
    if record != captured_record:
        return None, "INPUT_CHANGED_DURING_FETCH"
    if envelope is None:
        return None, "NO_VALID_OLS_PROPERTIES"
    if (
        not isinstance(envelope, OlsChemicalProperties)
        or envelope.ontology_id != target
        or envelope.returned_ontology_id != target
    ):
        return None, "RETURNED_IDENTITY_MISMATCH"
    if reason := _label_consistency(record["ontology_mapping"]["ontology_label"], envelope.label):
        return None, reason
    props = envelope.to_dict()
    endpoint = (
        "https://www.ebi.ac.uk/ols4/api/ontologies/chebi/terms/"
        "http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FCHEBI_" + target.split(":")[1]
    )
    allowed = {
        "molecular_formula",
        "inchi",
        "smiles",
        "molecular_weight",
        "data_source",
        "retrieval_date",
    }
    if (
        set(props) - allowed
        or envelope.source_url != endpoint
        or not re.fullmatch(r"[a-f0-9]{64}", envelope.response_sha256)
        or props.get("data_source") != f"ChEBI {target}; {endpoint}"
        or props.get("retrieval_date") != envelope.retrieved_at
    ):
        return None, "INVALID_SOURCE_ENVELOPE"
    try:
        if datetime.fromisoformat(envelope.retrieved_at).tzinfo is None:
            return None, "INVALID_SOURCE_ENVELOPE"
    except (TypeError, ValueError):
        return None, "INVALID_SOURCE_ENVELOPE"
    weight = props.get("molecular_weight")
    if weight is not None and (
        isinstance(weight, bool)
        or not isinstance(weight, (float, int))
        or not math.isfinite(weight)
        or weight <= 0
    ):
        return None, "INVALID_SOURCE_ENVELOPE"
    if reason := _structure_consistency(envelope.label, props):
        return None, reason
    return props, (
        f"Added {', '.join(sorted(props))} from {target}; OLS {envelope.source_url}; "
        f"retrieved {envelope.retrieved_at}; response SHA256 {envelope.response_sha256}. "
        "Consistency check of existing declared single-substance identity; no mapping or role approval."
    )
