"""2026-11-13: qualify corrected-license S3 publication inputs and license authority.

Narrow successor of bind_actual_inputs.py / qualify_s3_publication_evidence_v1.py.
Reuse their existing exact historical copies and the final old scientific pair's
complete input union (including1397/1398); do not restamp their approvals. The
two authorized historical path conflicts are the original publisher and its documentation.
Require actual completed current generation/inspection references as CLI pins.
No native phase, selection vote, source change, producer replay or consumer copy.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import types
import yaml

C = Path(__file__).resolve().parents[1]
ROOT = C / 'integration/stable-method-cumulative-source-canary-target'
HEAD = 'eeb586afd00af70997b0f46e76c08e8cfa074665'
OLD_HEAD = 'f4b6712d9b8a888c03389149283ee2b7d124bf13'
DEST = ROOT / '.temp/s3-publication-current-evidence-license-v1'
WRITER = C / 'preflight/stable-adoption1303-input-copy-helper-v3/copy_inputs.py'
OLD_REQUEST = '.temp/s3-publication-bound-pair-v1/REQUEST.json'
OLD_REQUEST_SHA = '2e1f4988f148d469fe4f861ca68027ca4a5d08cb4295a259c3d0b65a549108b4'
OLD_PUBLISHER = 'cb73381802f89b9dd8f57579f21c6d7bbcd0244f3ff84c920e8897011953f8e5'
NEW_PUBLISHER = 'bfdb3a52d2974f232900e51098104a4b6b877d9f7e74a595482e86e0f65c03d0'
PUBLISHER = 'src/mediaingredientmech/curate/stable_sssom_publication.py'
DOCS = 'docs/STABLE_SSSOM_PUBLICATION.md'
OLD_DOCS = '0d37522366d576ddbbac0b20bf23bcc26d6f8f22ee18d9ac376ecbaab8325920'
NEW_DOCS = 'ad54e060f114d87528cec80a483ab542801b3e79f009758ad1e027b33d3d8d70'
ARCHIVE = C / 'preflight/s3-failed-publication-code-archive-v1'
LICENSE_EVIDENCE = (
    ('preflight/s3-prepared-license-authority-finding-v1/FINDING.json',
     'd66eb248c832d596c2c603e3dd623ec9f814b0db352d85a29a5c07cece2ef622',
     'material-header-license-finding'),
    ('preflight/s3-prepared-license-technical-withdrawal-v1/WITHDRAWAL.json',
     '359448e89a27c90c89d8c5a86b77f3bc44394bcef2f05d05368e01bc7b893ceb',
     'prior-prepared-acceptance-remains-withdrawn'),
)
sha = lambda b: hashlib.sha256(b).hexdigest()
encoded = lambda v: (json.dumps(v, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()


def bootstrap(path, expected, name):
    """#1399: reject initial aliases before executing the exact captured buffer."""
    import stat
    assert path.is_absolute() and '..' not in path.parts, 'unsafe bootstrap path'
    parents = [(p, p.lstat()) for p in path.parents]
    assert all(stat.S_ISDIR(s.st_mode) for _, s in parents), 'aliased bootstrap ancestor'
    before = path.lstat()
    assert stat.S_ISREG(before.st_mode) and before.st_nlink == 1, 'aliased bootstrap file'
    snapshot = lambda s: (s.st_dev, s.st_ino, s.st_mode, s.st_nlink, s.st_size, s.st_mtime_ns, s.st_ctime_ns)
    with os.fdopen(os.open(path, os.O_RDONLY | os.O_NOFOLLOW), 'rb') as stream:
        opened = os.fstat(stream.fileno())
        assert snapshot(before) == snapshot(opened), 'bootstrap changed while opening'
        raw = stream.read()
        after = os.fstat(stream.fileno())
    assert snapshot(before) == snapshot(after) and len(raw) == before.st_size, 'bootstrap changed while reading'
    def verify():
        assert snapshot(path.lstat()) == snapshot(before), 'bootstrap file identity changed'
        assert all((p.lstat().st_dev, p.lstat().st_ino, p.lstat().st_mode) ==
                   (s.st_dev, s.st_ino, s.st_mode) for p, s in parents), 'bootstrap ancestor changed'
    verify()
    assert hashlib.sha256(raw).hexdigest() == expected, 'bootstrap source hash differs'
    module = types.ModuleType(name)
    module.__file__ = str(path)
    sys.modules[name] = module
    exec(compile(raw, str(path), 'exec'), module.__dict__)
    verify()
    return module, raw, verify


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    names = ('generation-terminal-receipt', 'inspection-terminal-receipt', 'request', 'generation', 'selection')
    for name in names:
        parser.add_argument('--' + name, required=True)
        parser.add_argument('--' + name + '-sha256', required=True)
    args = parser.parse_args()
    assert Path.cwd() == ROOT and not os.path.lexists(DEST)
    writer, raw, writer_check = bootstrap(WRITER, 'e8555db0f01f30140d5a619754cad600e74e2a4a801acbbcdaacc5ce7feec504', '_s3_requalified_evidence_writer')
    guard_path = writer.W / writer.GUARD
    guard, guard_raw, guard_check = bootstrap(guard_path, writer.GUARD_SHA, '_s3_requalified_evidence_guard')
    frozen = {}
    def capture(path, pin=None):
        path = Path(path)
        if not path.is_absolute():
            path = ROOT / path
        assert '..' not in path.parts and path.is_relative_to(C)
        if path not in frozen:
            frozen[path] = guard.FrozenFile.capture(path)
        f = frozen[path]
        assert pin is None or sha(f.content) == pin, str(path)
        return f
    assert capture(WRITER).content == raw and capture(guard_path).content == guard_raw
    helper = capture(Path(__file__).absolute())
    license_evidence = [(capture(C / name, pin), role)
                        for name, pin, role in LICENSE_EVIDENCE]
    git = lambda *a: subprocess.check_output(['git', '--no-optional-locks', *a], cwd=ROOT)
    assert git('rev-parse', 'HEAD').decode().strip() == HEAD
    assert git('rev-parse', 'HEAD^').decode().strip() == OLD_HEAD
    index = git('ls-files', '--stage', '-z')
    flags = git('ls-files', '-v', '-z')
    assert all(x.startswith(b'H ') for x in flags.split(b'\0') if x)
    assert not git('diff', '--name-only') and not git('diff', '--cached', '--name-only')
    pins, history_refs = {}, []
    def bind(name, pin):
        assert not Path(name).is_absolute() and '..' not in Path(name).parts
        assert name not in pins or pins[name] == pin, name
        capture(name, pin)
        pins[name] = pin
    old = json.loads(capture(OLD_REQUEST, OLD_REQUEST_SHA).content)
    assert old['head'] == OLD_HEAD and len(old['reviews']) == 2
    prior = dict(old['review_inputs'])
    prior[OLD_REQUEST] = OLD_REQUEST_SHA
    for ref in old['reviews']:
        report = yaml.safe_load(capture(ref['path'], ref['sha256']).content)
        assert report['source']['git_revision'] == OLD_HEAD and report['completion'] == 'completed'
        for item in report['source']['inputs']:
            assert item['path'] not in prior or prior[item['path']] == item['sha256']
            prior[item['path']] = item['sha256']
    assert prior[PUBLISHER] == OLD_PUBLISHER and prior[DOCS] == OLD_DOCS
    old_doc_raw = git('show', OLD_HEAD + ':' + DOCS)
    assert sha(old_doc_raw) == OLD_DOCS
    archive_manifest = capture(ARCHIVE / 'ARCHIVE.json', 'c54e8385ba7b04b5c538499e664d445c2e2b48ebbb0cc7e936cc897791395f30')
    archived = capture(ARCHIVE / 'mim-source' / PUBLISHER, OLD_PUBLISHER)
    assert any(x == {'archive_path': str(archived.path), 'original_path': str(ROOT / PUBLISHER), 'sha256': OLD_PUBLISHER}
               for x in json.loads(archive_manifest.content)['copied'])
    for name, pin in sorted(prior.items()):
        if name not in (PUBLISHER, DOCS):
            bind(name, pin)
    bind(PUBLISHER, NEW_PUBLISHER)
    bind(DOCS, NEW_DOCS)
    actual, documents = {}, {}
    expected_paths = {
        'generation_terminal_receipt': '.temp/s3-qualified-generation-terminal-license-v1/RESULT.json',
        'inspection_terminal_receipt': '.temp/cumulative-source-publication-inspect-s3-license-v1/RESULT.json',
        'request': '.temp/cumulative-source-publication-inspect-s3-license-v1/REQUEST.json',
        'generation': '.temp/cumulative-source-generated-s3-license-v1/receipt.json',
        'selection': '.temp/cumulative-source-publication-inspect-s3-license-v1/UNASSESSED-SELECTION.json'}
    for key, name in expected_paths.items():
        assert getattr(args, key) == name
        pin = getattr(args, key + '_sha256')
        bind(name, pin)
        actual[key] = {'path': name, 'sha256': pin}
        documents[key] = json.loads(frozen[ROOT / name].content)
    terminal, inspected = documents['generation_terminal_receipt'], documents['inspection_terminal_receipt']
    request, generation, selection = documents['request'], documents['generation'], documents['selection']
    assert terminal['exit_code'] == 0 and terminal['terminal_input_currentness'] == 'PASS'
    assert terminal['stage'] == str(ROOT / '.temp/cumulative-source-generated-s3-license-v1')
    assert terminal['canonical_installation'] is False and terminal['scientific_approval_added'] is False
    assert inspected['state'] == 'INSPECTION_COMPLETE_UNASSESSED' and inspected['exit_code'] == 0
    assert inspected['head'] == HEAD and inspected['native_invocation_attempted'] is True
    assert inspected['scientific_approval_added'] is False and inspected['canonical_writes'] is False
    assert inspected['stdout_sha256'] == actual['selection']['sha256']
    assert request['head'] == HEAD and request['generation'] == actual['generation']
    assert request['selection'] is None and request['reviews'] == [] and request['review_inputs'] == {}
    assert generation['state'] == 'COMPLETE' and generation['returncode'] == 0 and generation['head'] == HEAD
    assert generation['root'] == str(ROOT) and generation['adoption'] is None
    context = selection['context']
    assert context['generation'] == actual['generation']
    assert context['historical_reviews'] == request['historical_reviews'] == old['historical_reviews']
    assert context['successor_input_closure'] == generation['successor_input_closure']
    assert request['operational_policy'] == old['operational_policy']
    assert all(x['disposition'] is None and x['reason'] is None for x in selection['rows'])
    prior_selection = json.loads(capture(old['selection']['path'], old['selection']['sha256']).content)
    assert selection['history'] == prior_selection['history'], 'original complete historical obligations changed'
    assert set(selection['suppression']) == {'prior', 'generated', 'proposed', 'retired'}
    for mapping in (context['owners'], context['successor_input_closure']['target']):
        for name, pin in mapping.items():
            bind(name, pin)
    for name, pin in context['before'].items():
        if pin is not None:
            bind(name, pin)
    for ref in [request['operational_policy'], context['curation_successor'], generation['cas_dispositions'],
                generation['registry_retirement_proposal'], *generation['outputs'].values(), generation['stdout'], generation['stderr']]:
        bind(ref['path'], ref['sha256'])
    cas = json.loads(frozen[ROOT / generation['cas_dispositions']['path']].content)
    for name, pin in cas['review_inputs'].items():
        bind(name, pin)
    bind(cas['claims']['path'], cas['claims']['sha256'])
    for ref in cas['reviews']:
        bind(ref['path'], ref['sha256'])
    for name in ('MAPPING_SEMANTICS.md', 'AGENTS.md', 'schema/record_review.yaml', 'docs/record-reviews.md',
                 'docs/record-review-profile.md', 'scripts/record_review.py', 'src/mediaingredientmech/stable_ids.py',
                 'LICENSE', 'LICENSE-DATA', 'README.md'):
        bind(name, sha(capture(name).content))
    def recheck():
        writer_check(); guard_check()
        assert git('rev-parse', 'HEAD').decode().strip() == HEAD
        assert git('ls-files', '--stage', '-z') == index and git('ls-files', '-v', '-z') == flags
        assert git('show', OLD_HEAD + ':' + DOCS) == old_doc_raw
        assert not git('diff', '--name-only') and not git('diff', '--cached', '--name-only')
        for f in frozen.values():
            f.verify()
    recheck()
    tree = writer.Directory(DEST, guard)
    outputs = []
    try:
        fd = os.open('COPY-RECEIPT.json', os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600, dir_fd=tree.fd)
        with os.fdopen(fd, 'w', encoding='utf-8') as handle:
            copies = [(str(f.path), f.path.name, f.content) for f in (archived, archive_manifest, helper)]
            copies.append(('git:' + str(ROOT) + ':' + OLD_HEAD + ':' + DOCS, Path(DOCS).name, old_doc_raw))
            for original_path, basename, content in copies:
                name = sha(content) + '-' + basename
                out = tree.create(name, content); outputs.append(out)
                rel = str(out.path.relative_to(ROOT)); pins[rel] = sha(out.content)
                history_refs.append({'original_path': original_path, 'qualified_path': rel,
                                     'sha256': sha(out.content), 'authority_upgraded': False})
            license_refs = []
            for source, role in license_evidence:
                out = tree.create(sha(source.content) + '-' + source.path.name, source.content)
                outputs.append(out)
                rel = str(out.path.relative_to(ROOT)); pins[rel] = sha(out.content)
                ref = {'original_path': str(source.path), 'qualified_path': rel,
                       'sha256': sha(out.content), 'authority_upgraded': False,
                       'role': role}
                history_refs.append(ref); license_refs.append(ref)
            references = {'historical_input_count': len(prior), 'historical_pair_request': {'path': OLD_REQUEST, 'sha256': OLD_REQUEST_SHA},
                          'prior_reports_remain_historical': True, 'exact_copies': history_refs,
                          'historical_path_conflicts': [
                              {'original_path': PUBLISHER, 'historical_sha256': OLD_PUBLISHER,
                               'current_sha256': NEW_PUBLISHER, 'historical_qualified_path': history_refs[0]['qualified_path']},
                              {'original_path': DOCS, 'historical_sha256': OLD_DOCS,
                               'current_sha256': NEW_DOCS, 'historical_qualified_path': history_refs[3]['qualified_path'],
                               'original_git_root': str(ROOT), 'original_git_revision': OLD_HEAD}],
                          'actual_current_refs': actual,
                          'license_policy_inputs': {n: pins[n] for n in ('LICENSE', 'LICENSE-DATA', 'README.md')},
                          'license_evidence': license_refs,
                          'license_metadata_requires_current_assessment': True}
            out = tree.create('QUALIFIED-REFERENCES.json', encoded(references)); outputs.append(out)
            pins[str(out.path.relative_to(ROOT))] = sha(out.content)
            out = tree.create('INPUTS.json', encoded({'inputs': dict(sorted(pins.items()))})); outputs.append(out)
            receipt = {'at': datetime.now(timezone.utc).isoformat(), 'state': 'QUALIFIED_CURRENT_EVIDENCE_NO_APPROVAL',
                       'copier': '/root', 'procedure_author': '/root/s3_completed_source_audit',
                       'predecessor_procedures': ['bind_actual_inputs.py', 'qualify_s3_publication_evidence_v1.py'],
                       'root': str(ROOT), 'head': HEAD, 'historical_head': OLD_HEAD, 'actual_refs': actual,
                       'historical_input_count': len(prior), 'copies': history_refs,
                       'inputs': {'path': str(out.path.relative_to(ROOT)), 'sha256': sha(out.content), 'count': len(pins)},
                       'native_phase_invoked': False, 'scientific_approval_added': False, 'maintained_files_changed': False,
                       'limits': 'Existing source/review/hold/raw-authority bytes remain historical and unchanged. Actual current full-row scientific assessment is separately required; no companion-only authority is added here.'}
            def terminal_check():
                recheck(); tree.check()
                for f in outputs:
                    f.verify()
            finished = writer.finish_owned_receipt(guard, handle, DEST / 'COPY-RECEIPT.json', receipt, terminal_check)
        print(json.dumps({'receipt': {'path': str(DEST / 'COPY-RECEIPT.json'), 'sha256': sha(finished)},
                          'inputs': receipt['inputs']}))
    finally:
        tree.close()


if __name__ == '__main__':
    main()
