"""Tests for MediaIngredientMech deep research command wiring."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from research_ingredient import (  # noqa: E402
    build_command,
    build_provider_command,
    infer_status_slug,
    load_ingredient,
    provider_args,
    research_env,
    resolve_ingredient_file,
    template_vars,
)


def test_resolve_ingredient_file_finds_status_slug_record():
    path = resolve_ingredient_file("mapped", "Glucose")
    assert path == REPO_ROOT / "data" / "ingredients" / "mapped" / "Glucose.yaml"


def test_resolve_ingredient_file_accepts_direct_target():
    # Resolve against whatever unmapped record actually exists (don't hard-code a
    # specific slug — records get promoted out of unmapped/ over time).
    some = next((REPO_ROOT / "data" / "ingredients" / "unmapped").glob("*.yaml"))
    rel = some.relative_to(REPO_ROOT)
    assert resolve_ingredient_file(target=rel) == some


def test_infer_status_slug_for_ingredient_tree_record():
    path = REPO_ROOT / "data" / "ingredients" / "unmapped" / "Some_Unmapped_Record.yaml"
    assert infer_status_slug(path) == ("unmapped", "Some_Unmapped_Record")


def test_template_vars_include_ingredient_context():
    path = resolve_ingredient_file("mapped", "Glucose")
    variables = template_vars(load_ingredient(path), "mapped", "Glucose")
    assert variables["ingredient_label"] == "Glucose"
    assert variables["ingredient_identifier"] == "CHEBI:17234"
    assert variables["ingredient_status"] == "mapped"
    assert variables["ingredient_slug"] == "Glucose"
    assert "molecular_formula=C6H12O6" in variables["chemical_properties"]
    assert "ontology_id=CHEBI:17234" in variables["ontology_mapping"]


def test_provider_args_mirror_sibling_repo_shortcut():
    assert provider_args("falcon") == ["--provider", "falcon"]
    assert provider_args("cborg") == ["--use-cborg"]


def test_build_command_for_falcon_research():
    command = build_command(
        provider="falcon",
        template=Path("templates/ingredient_mapping_research.md"),
        output_file=Path("research/ingredients/mapped/Glucose-deep-research-falcon.md"),
        citations_file=Path(
            "research/ingredients/mapped/Glucose-deep-research-falcon.citations.md"
        ),
        variables={"ingredient_label": "Glucose", "ingredient_identifier": "CHEBI:17234"},
        passthrough_args=["--max-cost", "1"],
    )
    assert command[:4] == [
        "deep-research-client",
        "research",
        "--template",
        "templates/ingredient_mapping_research.md",
    ]
    assert "--provider" in command
    assert "falcon" in command
    assert "--separate-citations" in command
    assert "research/ingredients/mapped/Glucose-deep-research-falcon.citations.md" in command
    assert command[-2:] == ["--max-cost", "1"]


def test_build_provider_command_for_falcon():
    assert build_provider_command("falcon") == [
        "deep-research-client",
        "providers",
        "--provider",
        "falcon",
    ]


def test_research_env_maps_futurehouse_key_to_edison(monkeypatch):
    monkeypatch.delenv("EDISON_API_KEY", raising=False)
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "test-key")
    env = research_env("falcon")
    assert env["EDISON_API_KEY"] == "test-key"


def test_research_env_keeps_existing_edison_key(monkeypatch):
    """The canonical EDISON_API_KEY wins over the deprecated alias.

    `--provider falcon` IS the Edison provider (deep_research_client/client.py
    registers it as "Edison provider (formerly Falcon/FutureHouse)" and resolves
    `EDISON_API_KEY or FUTUREHOUSE_API_KEY` into an EdisonClient), so an Edison
    key is exactly the right credential for it. FUTUREHOUSE_API_KEY is a
    deprecated alias for that same key and must not override it.
    """
    monkeypatch.setenv("EDISON_API_KEY", "edison-key")
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "futurehouse-key")
    assert research_env("falcon")["EDISON_API_KEY"] == "edison-key"


def test_research_env_passes_edison_key_to_falcon(monkeypatch):
    """Regression guard: falcon must not be starved of the Edison credential.

    A previous change stripped EDISON_API_KEY for `--provider falcon` on the
    false premise that falcon was a third-party FutureHouse endpoint. It is not,
    and the effect was that the falcon provider stopped registering at all
    (client.py only registers it when a key resolves), so every Falcon run
    failed.
    """
    monkeypatch.setenv("EDISON_API_KEY", "edison-key")
    monkeypatch.delenv("FUTUREHOUSE_API_KEY", raising=False)
    assert research_env("falcon")["EDISON_API_KEY"] == "edison-key"


def test_research_env_leaves_edison_providers_untouched(monkeypatch):
    monkeypatch.setenv("EDISON_API_KEY", "edison-key")
    assert research_env("edison")["EDISON_API_KEY"] == "edison-key"


@pytest.mark.parametrize("spelling", ["Falcon", "FALCON", " falcon ", "FaLcOn"])
def test_research_env_alias_applies_regardless_of_provider_spelling(monkeypatch, spelling):
    """`--provider` is free text, so the alias must not hinge on capitalisation."""
    monkeypatch.delenv("EDISON_API_KEY", raising=False)
    monkeypatch.setenv("FUTUREHOUSE_API_KEY", "futurehouse-key")
    assert research_env(spelling)["EDISON_API_KEY"] == "futurehouse-key"
