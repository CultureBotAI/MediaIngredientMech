"""Tests for the reviewed-LLM suggestion importer (issue #422)."""

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml
from click.testing import CliRunner

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "src"))


def _load():
    spec = importlib.util.spec_from_file_location(
        "apply_claude_suggestions", ROOT / "scripts" / "apply_claude_suggestions.py"
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _suggestion(**overrides):
    suggestion = {
        "identifier": "UNMAPPED_0001",
        "name": "NaNO",
        "ontology_id": "CHEBI:75229",
        "ontology_label": "sodium nitrate",
        "ontology_source": "CHEBI",
        "confidence": 0.9,
        "quality": "LLM_ASSISTED",
        "match_level": "MANUAL",
        "reasoning": "The incomplete formula denotes sodium nitrate.",
    }
    suggestion.update(overrides)
    return suggestion


def _curator(mod, tmp_path, record):
    curator = mod.IngredientCurator(data_path=tmp_path / "unused.yaml", curator_name="reviewer")
    curator.load()
    curator._records = [record]
    curator._collection["ingredients"] = curator._records
    return curator


def test_load_suggestions_validates_complete_document_before_use(tmp_path):
    mod = _load()
    path = tmp_path / "suggestions.yaml"
    path.write_text(yaml.safe_dump({"suggestions": [_suggestion(), {"name": "missing id"}]}))

    with pytest.raises(mod.SuggestionValidationError, match=r"suggestions\[1\]\.identifier"):
        mod.load_suggestions(path)


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("confidence", 1.1, "confidence"),
        ("ontology_id", "not-a-curie", "CURIE"),
        ("ontology_source", "FOODON", "prefix"),
    ],
)
def test_typed_suggestion_rejects_invalid_mapping_fields(field, value, message):
    mod = _load()

    with pytest.raises(mod.SuggestionValidationError, match=message):
        mod.MappingSuggestion.from_mapping(_suggestion(**{field: value}))


def test_apply_is_transactional_and_restores_dirty_state_on_failure(tmp_path):
    mod = _load()
    original = {
        "identifier": "UNMAPPED_0001",
        "preferred_term": "NaNO",
        "mapping_status": "UNMAPPED",
    }
    curator = _curator(mod, tmp_path, original)

    def fail_after_mutation(record, candidate, **kwargs):
        record["identifier"] = candidate.ontology_id
        curator._dirty = True
        raise RuntimeError("enrichment failed")

    curator.accept_mapping = fail_after_mutation
    success, message = mod.apply_suggestion(
        _suggestion(), curator, mod.OntologyClient(), validate=False
    )

    assert not success
    assert "enrichment failed" in message
    assert curator.records == [original]
    assert curator.records[0]["identifier"] == "UNMAPPED_0001"
    assert not curator.is_dirty


def test_apply_deduplicates_synonyms_and_records_provider_model(tmp_path):
    mod = _load()
    original = {
        "identifier": "UNMAPPED_0001",
        "preferred_term": "NaNO",
        "mapping_status": "UNMAPPED",
        "synonyms": [
            {"synonym_text": "NaNO", "synonym_type": "INCOMPLETE_FORMULA", "source": "manual"},
            {"synonym_text": "nano", "synonym_type": "RAW_TEXT", "source": "duplicate"},
        ],
    }
    curator = _curator(mod, tmp_path, original)

    success, _ = mod.apply_suggestion(
        _suggestion(),
        curator,
        mod.OntologyClient(),
        validate=False,
        auto_enrich=False,
        provider="openai",
        model="gpt-test",
    )

    assert success
    assert original["identifier"] == "UNMAPPED_0001"  # committed from a copy
    mapped = curator.records[0]
    assert mapped["identifier"] == "CHEBI:75229"
    assert [item["synonym_text"] for item in mapped["synonyms"]] == ["NaNO"]
    event = mapped["curation_history"][-1]
    assert event["llm_model"] == "openai:gpt-test"
    assert "openai reasoning" in event["changes"]


def test_dry_run_uses_source_identifier_and_has_no_external_or_file_side_effects(
    tmp_path, monkeypatch
):
    mod = _load()
    suggestions = tmp_path / "suggestions.yaml"
    suggestions.write_text(yaml.safe_dump({"suggestions": [_suggestion()]}))

    class FakeClient:
        def __init__(self, *args, **kwargs):
            pass

    class FakeCurator:
        last = None

        def __init__(self, *args, **kwargs):
            type(self).last = self
            self.records = []
            self.saved = False
            self.auto_enrich = None
            self._dirty = False

        @property
        def is_dirty(self):
            return self._dirty

        def load(self):
            self.records = [
                {
                    "identifier": "UNMAPPED_0001",
                    "preferred_term": "NaNO",
                    "mapping_status": "UNMAPPED",
                }
            ]

        def accept_mapping(self, record, candidate, **kwargs):
            self.auto_enrich = kwargs["auto_enrich"]
            record["identifier"] = candidate.ontology_id
            record["mapping_status"] = "MAPPED"
            self._dirty = True

        def save(self):
            self.saved = True

    monkeypatch.setattr(mod, "OntologyClient", FakeClient)
    monkeypatch.setattr(mod, "IngredientCurator", FakeCurator)

    result = CliRunner().invoke(
        mod.main,
        ["--suggestions", str(suggestions), "--dry-run"],
    )

    assert result.exit_code == 0, result.output
    assert "UNMAPPED_0001" in result.output
    assert "no files, ontology downloads, or enrichment caches" in result.output
    assert FakeCurator.last.auto_enrich is False
    assert FakeCurator.last.saved is False


def test_apply_instructions_promote_collection_before_sync_and_qc(tmp_path, monkeypatch):
    mod = _load()
    suggestions = tmp_path / "suggestions.yaml"
    suggestions.write_text(yaml.safe_dump({"suggestions": [_suggestion()]}))

    class FakeClient:
        def __init__(self, *args, **kwargs):
            pass

    class FakeCurator:
        def __init__(self, *args, **kwargs):
            self.records = []
            self._dirty = False

        @property
        def is_dirty(self):
            return self._dirty

        def load(self):
            self.records = [
                {
                    "identifier": "UNMAPPED_0001",
                    "preferred_term": "NaNO",
                    "mapping_status": "UNMAPPED",
                }
            ]

        def accept_mapping(self, record, candidate, **kwargs):
            record["identifier"] = candidate.ontology_id
            record["mapping_status"] = "MAPPED"
            self._dirty = True

        def save(self):
            pass

    monkeypatch.setattr(mod, "OntologyClient", FakeClient)
    monkeypatch.setattr(mod, "IngredientCurator", FakeCurator)

    result = CliRunner().invoke(
        mod.main,
        [
            "--suggestions",
            str(suggestions),
            "--skip-validation",
            "--data-path",
            str(ROOT / "data" / "curated" / "unmapped_ingredients.yaml"),
        ],
    )

    assert result.exit_code == 0, result.output
    preview = "move_mapped_out_of_unmapped_collection.py` (preview)"
    apply = "move_mapped_out_of_unmapped_collection.py --apply"
    normalized_output = " ".join(result.output.split())
    assert preview in result.output
    assert apply in result.output
    assert "`just sync-individual` alone" in normalized_output
    assert result.output.index(preview) < result.output.index(apply)
    assert result.output.index(apply) < result.output.index("`just sync-individual`")
    assert result.output.index("`just sync-individual`") < result.output.index("`just qc`")
