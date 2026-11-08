"""Stable subjects remain independent of labels, mappings and filename slugs (#1265)."""
import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / 'scripts' / f'{name}.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_stable_sssom_owner_retains_legacy_registry_mapping(tmp_path, monkeypatch):
    mod = script('validate_sssom_invariants')
    path = tmp_path / 'Renamed.yaml'
    path.write_text(yaml.safe_dump({'mim_id': 'MIM:0000001',
        'identifier': 'kgmicrobe.ingredient:old_identity', 'preferred_term': 'Renamed',
        'legacy_identifiers': ['MIM:Original_name'], 'mapping_status': 'MAPPED'}))
    monkeypatch.setattr(mod, 'INGREDIENTS_DIR', tmp_path)
    assert mod._subject_to_path() == {'MIM:0000001': path}
    rows = [{'subject_id': 'MIM:0000001', 'predicate_id': 'skos:exactMatch',
             'object_id': 'kgmicrobe.ingredient:old_identity'}]
    assert mod._has_registry_row(rows, 'MIM:0000001')
    assert not mod._has_registry_row([dict(rows[0], object_id='kgmicrobe.ingredient:0000001')], 'MIM:0000001')
    baseline = tmp_path / 'baseline.tsv'
    baseline.write_text('subject_id\ttoken\nMIM:Original_name\tOlder alias\n')
    monkeypatch.setattr(mod, 'OTHER_BASELINE', baseline)
    assert mod._other_baseline() == frozenset({('MIM:0000001', 'older alias')})


def test_sssom_subject_cannot_follow_display_label():
    mod = script('reconcile_sssom')
    corpus = {'ingredients': [{'mim_id': 'MIM:0000001', 'preferred_term': 'New label',
                               'mapping_status': 'MAPPED'}]}
    mod.validate_stable_subjects(corpus, [{'subject_id': 'MIM:0000001', 'subject_label': 'New label'}])
    with pytest.raises(ValueError, match='permanent subject mismatch'):
        mod.validate_stable_subjects(corpus, [{'subject_id': 'MIM:New_label', 'subject_label': 'New label'}])


def test_flat_outputs_include_identity_without_replacing_mapping(tmp_path):
    import csv
    import json
    mod = script('export_lists')
    record = {'mim_id': 'MIM:0000001', 'identifier': 'CHEBI:1',
              'preferred_term': 'Example', 'mapping_status': 'MAPPED'}
    target = tmp_path / 'export.json'
    mod.export_to_json([record], target)
    assert json.loads(target.read_text())[0]['mim_id'] == 'MIM:0000001'
    assert json.loads(target.read_text())[0]['identifier'] == 'CHEBI:1'
    target = tmp_path / 'export.csv'
    mod.export_to_csv([record], target)
    with target.open() as stream:
        row = next(csv.DictReader(stream))
    assert row['mim_id'] == 'MIM:0000001' and row['identifier'] == 'CHEBI:1'


def test_generated_jsonld_uses_permanent_record_identity():
    import json

    from linkml.generators.jsonldcontextgen import ContextGenerator

    from mediaingredientmech.stable_ids import MIM_PREFIX
    context = json.loads(ContextGenerator(str(ROOT / 'src/mediaingredientmech/schema/mediaingredientmech.yaml')).serialize())['@context']
    assert context['MIM'] == {'@id': MIM_PREFIX, '@prefix': True}
    assert context['mim_id'] == '@id'
    assert context['identifier'] != '@id'


def test_visualization_projection_preserves_coordinates_and_metadata():
    spec = importlib.util.spec_from_file_location('visual_1265', ROOT / 'scripts/adhoc/project_visualization_ids_1265.py')
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    original = [{'id': 'MIM:Name', 'name': 'Name', 'umap_x': 3.14, 'umap_y': -2.0,
                 'identifier': 'CHEBI:1'}]
    assert mod.project(original, {'MIM:Name': 'MIM:0000001'}) == [dict(original[0], id='MIM:0000001')]
    assert original[0]['id'] == 'MIM:Name'
    with pytest.raises(KeyError):
        mod.project(original, {})


@pytest.mark.parametrize('reverse', [False, True])
def test_ambiguous_legacy_alias_cannot_transfer_synonym_waiver(tmp_path, monkeypatch, reverse):
    mod = script('validate_sssom_invariants')
    paths = []
    for number in [1, 2]:
        path = tmp_path / f'{number}.yaml'
        path.write_text(yaml.safe_dump({'mim_id': f'MIM:{number:07d}',
            'identifier': f'CHEBI:{number}', 'preferred_term': str(number),
            'legacy_identifiers': ['MIM:Legacy'], 'mapping_status': 'MAPPED'}))
        paths.append((f'MIM:{number:07d}', path))
    if reverse:
        paths.reverse()
    monkeypatch.setattr(mod, '_subject_to_path', lambda: dict(paths))
    baseline = tmp_path / 'baseline.tsv'
    baseline.write_text('subject_id\ttoken\nMIM:Legacy\tOther substance\n')
    monkeypatch.setattr(mod, 'OTHER_BASELINE', baseline)
    assert ('MIM:0000001', 'other substance') not in mod._other_baseline()
    assert ('MIM:0000002', 'other substance') not in mod._other_baseline()


def test_embedding_record_identity_survives_label_mapping_filename_and_directory_changes(tmp_path):
    """Collect native text inputs only; never load or call an embedding model."""
    mod = script('embed_records')
    ingredients = tmp_path / 'ingredients'
    original = ingredients / 'mapped/Old_name.yaml'
    original.parent.mkdir(parents=True)
    record = {'mim_id': 'MIM:0000001', 'identifier': 'CHEBI:1',
              'preferred_term': 'Old name', 'mapping_status': 'MAPPED',
              'ontology_mapping': {'ontology_id': 'CHEBI:1', 'ontology_source': 'CHEBI'}}
    original.write_text(yaml.safe_dump(record))
    first = mod.collect_records(ingredients)
    assert len(first) == 1
    revised = dict(record, identifier='UNMAPPED_0042', preferred_term='New label',
                   mapping_status='UNMAPPED')
    revised.pop('ontology_mapping')
    moved = ingredients / 'unmapped/Completely_different_filename.yaml'
    moved.parent.mkdir()
    moved.write_text(yaml.safe_dump(revised))
    original.unlink()
    second = mod.collect_records(ingredients)
    assert len(second) == 1
    assert first[0]['id'] == second[0]['id'] == 'MIM:0000001'
    assert first[0]['url'] == second[0]['url'] == 'ingredient/MIM_0000001'
    assert (first[0]['title'], first[0]['identifier']) == ('Old name', 'CHEBI:1')
    assert (second[0]['title'], second[0]['identifier']) == ('New label', 'UNMAPPED_0042')
    assert second[0]['mapping_status'] == 'UNMAPPED'
    assert 'New label (MIM:0000001)' in second[0]['text']
    assert 'UNMAPPED_0042' in second[0]['text']


def test_embedding_collection_refuses_missing_permanent_identity(tmp_path):
    mod = script('embed_records')
    source = tmp_path / 'mapped/No_id.yaml'
    source.parent.mkdir()
    source.write_text(yaml.safe_dump({'identifier': 'CHEBI:1', 'preferred_term': 'No identity',
                                      'mapping_status': 'MAPPED'}))
    with pytest.raises(ValueError, match='positive seven-digit MIM identifier'):
        mod.collect_records(tmp_path)


@pytest.fixture
def text_map_projection():
    import json
    from copy import deepcopy

    spec = importlib.util.spec_from_file_location(
        'text_map_projection_1265', ROOT / 'scripts/adhoc/project_text_map_ids_1265.py'
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    payload = {
        'model': 'original-offline-model', 'dim': 1024, 'count': 2,
        'generated_at': '2026-10-16T18:20:16Z',
        'points': [
            {'id': 'MIM:Salt_mix', 'url': 'records/ingredient/mapped/Salt_mix.html',
             'title': 'Original salt mixture', 'identifier': 'CHEBI:1',
             'mapping_status': 'MAPPED', 'x': 3.14, 'y': -2.0, 'px': 0.25, 'py': -0.5},
            {'id': 'MIM:Unknown', 'url': 'records/ingredient/unmapped/Unknown.html',
             'title': 'Unknown source', 'identifier': 'UNMAPPED_0042',
             'mapping_status': 'UNMAPPED', 'x': -8.75, 'y': 4.0, 'px': -0.75, 'py': 0.5},
        ],
    }
    records = {
        'data/ingredients/mapped/Salt + mix.yaml': {'mim_id': 'MIM:0000001'},
        'data/ingredients/unmapped/Unknown.yaml': {'mim_id': 'MIM:0000002'},
    }
    prefix, suffix = '<html><script>\nconst MAP_DATA = ', ';\n</script></html>'
    html = prefix + json.dumps(payload) + suffix
    return mod, html, deepcopy(payload), records, prefix, suffix


def test_text_map_projection_changes_only_identity_and_address(text_map_projection):
    import json
    from copy import deepcopy

    mod, html, payload, records, prefix, suffix = text_map_projection
    original_records = deepcopy(records)
    changed, count = mod.project_html(html, records)
    assert count == 2
    assert changed.startswith(prefix) and changed.endswith(suffix)
    actual = json.loads(changed[len(prefix):-len(suffix)])
    expected = deepcopy(payload)
    for number, point in enumerate(expected['points'], 1):
        point['id'] = f'MIM:{number:07d}'
        point['url'] = f'ingredient/MIM_{number:07d}'
    assert actual == expected, 'Only addresses change; layout, science and generation metadata stay frozen'
    assert records == original_records
    assert json.loads(html[len(prefix):-len(suffix)]) == payload


@pytest.mark.parametrize('problem', ['unknown_url', 'duplicate_id', 'duplicate_url'])
def test_text_map_projection_refuses_unknown_or_ambiguous_owners(text_map_projection, problem):
    import json

    mod, html, payload, records, prefix, suffix = text_map_projection
    if problem == 'unknown_url':
        payload['points'][0]['url'] = 'records/ingredient/mapped/Not_in_the_corpus.html'
        html = prefix + json.dumps(payload) + suffix
        expected, diagnostic = KeyError, 'Not_in_the_corpus'
    elif problem == 'duplicate_id':
        records['data/ingredients/unmapped/Unknown.yaml']['mim_id'] = 'MIM:0000001'
        expected, diagnostic = ValueError, 'Duplicate text-map record'
    else:
        records['data/ingredients/mapped/Salt mix.yaml'] = {'mim_id': 'MIM:0000003'}
        expected, diagnostic = ValueError, 'Ambiguous legacy text-map URL'
    with pytest.raises(expected, match=diagnostic):
        mod.project_html(html, records)
