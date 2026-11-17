"""#1431: explicit unknown is evidence-bound, never zero or scientific approval."""
import copy
import hashlib
from pathlib import Path

import pytest
import yaml

from mediaingredientmech.occurrence_coverage import (
    content_sha256, load_coverage, occurrence_view, stored_counts,
)


def write_bundle(tmp_path):
    root = tmp_path / 'data' / 'ingredients'
    (root / 'mapped').mkdir(parents=True)
    record = {'mim_id': 'MIM:0000001', 'identifier': 'cas:1-00-0',
              'preferred_term': 'reviewed material', 'mapping_status': 'MAPPED'}
    owner = root / 'mapped' / 'record.yaml'
    owner.write_text(yaml.safe_dump(record))
    bundle = tmp_path / 'mappings' / 'occurrence_coverage.yaml'
    bundle.parent.mkdir()
    source = bundle.parent / 'source.tsv'
    source.write_text('source_id\tcontext\ns1\tone captured subset\n')
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    declaration = {
        'mim_id': record['mim_id'], 'owner_sha256': hashlib.sha256(owner.read_bytes()).hexdigest(),
        'owner_content_sha256': content_sha256(record), 'state': 'UNKNOWN',
        'reason_code': 'INCOMPLETE_SOURCE_COVERAGE',
        'reason': 'Only a reviewed subset was captured; complete media usage is unknown.',
        'evidence': [{'path': 'source.tsv', 'sha256': digest, 'description': 'Frozen subset'}],
        'source_coverage': [{'source': 'example', 'revision': 'v1', 'evidence_path': 'source.tsv',
                             'source_sha256': digest, 'scanned_at': '2026-11-17T00:00:00Z',
                             'row_count': 1, 'scope': 'One subset, not the complete media universe'}],
    }
    doc = {'contract': 'mim-occurrence-coverage-v1', 'created_at': '2026-11-17T00:00:00Z',
           'declarations': [declaration]}
    bundle.write_text(yaml.safe_dump(doc))
    return root, record, owner, bundle, doc


def save(bundle, doc):
    bundle.write_text(yaml.safe_dump(doc))


def test_unknown_distinct_from_zero_and_missing(tmp_path):
    root, record, _, bundle, _ = write_bundle(tmp_path)
    coverage = load_coverage(bundle, root)
    view = occurrence_view(record, {'cas:1-00-0': (1, 1)}, coverage)
    assert view['occurrence_statistics_state'] == 'UNKNOWN'
    assert view['media_count'] is None and view['total_occurrences'] is None
    assert view['occurrence_statistics_provenance']['coverage_sha256'] == coverage.sha256
    assert occurrence_view(record)['occurrence_statistics_state'] == 'MISSING'
    zero = {**record, 'occurrence_statistics': {'media_count': 0, 'total_occurrences': 0}}
    assert occurrence_view(zero)['total_occurrences'] == 0
    assert occurrence_view(zero)['occurrence_statistics_state'] == 'RECORDED'


@pytest.mark.parametrize('field', ['reason', 'evidence', 'source_coverage', 'owner_sha256', 'state'])
def test_required_declaration_fields(tmp_path, field):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    del doc['declarations'][0][field]
    save(bundle, doc)
    with pytest.raises(ValueError):
        load_coverage(bundle, root)


@pytest.mark.parametrize('mutation', ['wrong_id', 'owner_bytes', 'owner_content', 'duplicate',
                                      'evidence_bytes', 'blank_reason', 'extra_count', 'timezone'])
def test_binding_and_closed_shape_failures(tmp_path, mutation):
    root, _, owner, bundle, doc = write_bundle(tmp_path)
    item = doc['declarations'][0]
    if mutation == 'wrong_id': item['mim_id'] = 'MIM:0000002'
    elif mutation == 'owner_bytes': owner.write_text(owner.read_text() + '# new bytes\n')
    elif mutation == 'owner_content': item['owner_content_sha256'] = '0' * 64
    elif mutation == 'duplicate': doc['declarations'].append(copy.deepcopy(item))
    elif mutation == 'evidence_bytes': (bundle.parent / 'source.tsv').write_text('changed')
    elif mutation == 'blank_reason': item['reason'] = '   '
    elif mutation == 'extra_count': item['total_occurrences'] = 0
    elif mutation == 'timezone': doc['created_at'] = '2026-11-17T00:00:00'
    save(bundle, doc)
    with pytest.raises(ValueError): load_coverage(bundle, root)


@pytest.mark.parametrize('path_kind', ['absolute', 'traversal', 'symlink'])
def test_evidence_containment(tmp_path, path_kind):
    root, _, _, bundle, doc = write_bundle(tmp_path)
    outside = tmp_path / 'outside.tsv'
    outside.write_text((bundle.parent / 'source.tsv').read_text())
    if path_kind == 'absolute': name = str(outside)
    elif path_kind == 'traversal': name = '../outside.tsv'
    else:
        (bundle.parent / 'escape.tsv').symlink_to(outside)
        name = 'escape.tsv'
    doc['declarations'][0]['evidence'][0]['path'] = name
    save(bundle, doc)
    with pytest.raises(ValueError): load_coverage(bundle, root)


@pytest.mark.parametrize('stats', [None, {}, {'media_count': 0}, {'media_count': 0, 'total_occurrences': None},
                                   {'media_count': 0, 'total_occurrences': -1},
                                   {'media_count': -1, 'total_occurrences': 1},
                                   {'media_count': True, 'total_occurrences': 1},
                                   {'media_count': 0, 'total_occurrences': '1'},
                                   {'media_count': 0, 'total_occurrences': 1.0},
                                   {'media_count': 2, 'total_occurrences': 1}])
def test_invalid_counts_cannot_be_unknown(stats):
    with pytest.raises(ValueError):
        stored_counts({'occurrence_statistics': stats})


def test_rejected_nonzero_separate_from_negative_or_order_errors():
    with pytest.raises(ValueError, match='REJECTED'):
        stored_counts({'mapping_status': 'REJECTED', 'occurrence_statistics': {'media_count': 1, 'total_occurrences': 2}})
    assert stored_counts({'mapping_status': 'REJECTED', 'occurrence_statistics': {'media_count': 0, 'total_occurrences': 0}}) == (0, 0)


@pytest.mark.parametrize('stats', [None, {'media_count': 0}, {'media_count': 0, 'total_occurrences': 0}])
def test_unknown_cannot_hide_present_statistics(tmp_path, stats):
    root, record, owner, bundle, doc = write_bundle(tmp_path)
    record['occurrence_statistics'] = stats
    owner.write_text(yaml.safe_dump(record))
    doc['declarations'][0].update(owner_sha256=hashlib.sha256(owner.read_bytes()).hexdigest(), owner_content_sha256=content_sha256(record))
    save(bundle, doc)
    with pytest.raises(ValueError): load_coverage(bundle, root)


def test_changed_aggregate_does_not_reuse_owner_declaration(tmp_path):
    root, record, _, bundle, _ = write_bundle(tmp_path)
    coverage = load_coverage(bundle, root)
    with pytest.raises(ValueError, match='stale owner content'):
        occurrence_view({**record, 'preferred_term': 'another concept'}, coverage=coverage)


def test_observation_is_not_complete_media_usage(tmp_path):
    root, record, _, bundle, doc = write_bundle(tmp_path)
    item = doc['declarations'][0]
    for name in ('primary.json', 'skeptic.json'):
        path = bundle.parent / name
        path.write_text('{"scope": "example subset only"}\n')
        item['evidence'].append({'path': name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'description': name})
    item['observations'] = [{'source': 'example', 'unit': 'NONMEDIA_OBSERVATION', 'count': 7,
                             'scope': 'source graph observation, not media usage', 'evidence_path': 'source.tsv',
                             'primary_review_path': 'primary.json', 'skeptical_review_path': 'skeptic.json',
                             'attribution': 'REVIEWED_SOURCE_SCOPE'}]
    save(bundle, doc)
    coverage = load_coverage(bundle, root)
    result = occurrence_view(record, coverage=coverage)
    assert result['total_occurrences'] is None and result['media_count'] is None
    assert result['occurrence_statistics_provenance']['observations'][0]['count'] == 7
    item['reason_code'] = 'SOURCE_ATTRIBUTION_WITHHELD'
    save(bundle, doc)
    with pytest.raises(ValueError, match='unsettled attribution'):
        load_coverage(bundle, root)


def test_known_membership_route_and_rejected_tombstone_preserved():
    rec = {'identifier': 'CHEBI:1', 'mapping_status': 'MAPPED',
           'occurrence_statistics': {'media_count': 2, 'total_occurrences': 3}}
    view = occurrence_view(rec, {'CHEBI:1': (4, 5)})
    assert (view['media_count'], view['total_occurrences']) == (4, 5)
    rec.update(mapping_status='REJECTED', occurrence_statistics={'media_count': 0, 'total_occurrences': 0})
    assert occurrence_view(rec, {'CHEBI:1': (4, 5)})['total_occurrences'] == 0
