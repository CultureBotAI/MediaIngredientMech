"""2026-11-12: current S3 primary complete-row installation judgments.

Inputs are the actual completed native selection, current owners, retained
per-row evidence and this reviewer's current source/cell analysis. Writes a
fresh private assessed selection and its full reasoning ledger, changing only
disposition/reason. No native publication, source change or release approval.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
import copy
import hashlib
import json
import os
import re
import subprocess
import sys
import types
import yaml

C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R = C / 'integration/stable-method-cumulative-source-canary-target'
D = R / '.temp/s3-publication-primary-native-v1'
HERE = Path(__file__).parent
HEAD = 'f4b6712d9b8a888c03389149283ee2b7d124bf13'
sha = lambda b: hashlib.sha256(b).hexdigest()
now = lambda: datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
encode = lambda o: (json.dumps(o, indent=2, sort_keys=True, ensure_ascii=False) + '\n').encode()
helper = C / 'preflight/stable-adoption1303-input-copy-helper-v3/copy_inputs.py'
raw = helper.read_bytes()
assert sha(raw) == 'e8555db0f01f30140d5a619754cad600e74e2a4a801acbbcdaacc5ce7feec504'
w = types.ModuleType('_s3_primary_private_writer'); w.__file__ = str(helper)
sys.modules[w.__name__] = w
exec(compile(raw, str(helper), 'exec'), w.__dict__)
guard = w.load_guard()
captured = []

def read(path, expected=None):
    path = path if path.is_absolute() else R / path
    f = guard.FrozenFile.capture(path)
    assert expected is None or sha(f.content) == expected, str(path)
    captured.append(f)
    return f.content

def doc(path, expected=None):
    return json.loads(read(Path(path), expected))

def head():
    return subprocess.check_output(['git', '--no-optional-locks', 'rev-parse', 'HEAD'], cwd=R, timeout=30).decode().strip()

assert head() == HEAD
base_inputs = doc('.temp/s3-publication-current-evidence-v1/INPUTS.json', 'a6620f1dbe3c514b991d51be0e3040f36bc7071649fa7a527b0faec865be5293')['inputs']
inputs = doc('.temp/s3-publication-cas-evidence1397-v1/INPUTS.json', 'f1bc411d12251b763695ea5835f5e283c9c233b423b2da5659fe879750a2691d')['inputs']
assert all(inputs.get(p)==h for p,h in base_inputs.items())
by_hash = defaultdict(list)
for p, h in inputs.items(): by_hash[h].append(p)

def qualified(h):
    assert h in by_hash, h
    return sorted(by_hash[h], key=lambda p: (len(p), p))[0]

issue1121 = doc(qualified('64f143f6cf9c99359df8eb626ff266a59de99a98bb7b10acca6ea80051283189'), '64f143f6cf9c99359df8eb626ff266a59de99a98bb7b10acca6ea80051283189')
held_owner_names = set(re.findall(r'data/ingredients/mapped/([^/)]+\.yaml)',issue1121['body']))
assert issue1121['state']=='open' and len(held_owner_names)==13

P = doc(qualified('ab0937484b591bfc600c36788ab685b0f59eec97e2799af7a644558aba2df8ec'), 'ab0937484b591bfc600c36788ab685b0f59eec97e2799af7a644558aba2df8ec')
prior = {(p['subject_id'], p['predicate_id'], p['object_id']): p for p in P}
assert len(prior) == len(P) == 3017
native_name = '.temp/cumulative-source-publication-inspect-s3-v1/UNASSESSED-SELECTION.json'
native = doc(native_name, '2c61399c7db7f5c90f254684a06dcd131105047cb104f6b6e341ae407e77cce7')
selection = copy.deepcopy(native)
current = doc(HERE / 'FOURTEEN-CURRENT-OWNER-CONCLUSIONS.json')
current = {o['mim_id']: o for o in current}
assert len(current) == 14
cell_conclusions = doc(HERE / 'CURRENT-DELTA-CELL-CONCLUSIONS.json', '26fda9ec6bca39c57966961461752995af9448a54a5509cd66a9b5f52eb4574a')
holds = doc(HERE / 'CURRENT-HOLD-CONSTRAINTS.json', 'cd0f5699ff7d295ea491fd59b0e025c111c7c8ff355c8c62a133520e0ccaba7b')
source_request = doc('.temp/cumulative-source-successor-assessed-s3-v1/ASSESSED-REQUEST.json', '1c979c3d89b4e75102044939eab6b393cff2b2e9fa835aa9e0917be833738881')
ops = {o['mim_id']: o for o in source_request['operations']}
all_owner = {}
for e in selection['rows']:
    if e['owner'] not in all_owner:
        all_owner[e['owner']] = yaml.safe_load(read(Path(e['owner']), e['owner_sha256']))
key = lambda r: (r['subject_id'], r['predicate_id'], r['object_id'])
mandatory = {'MIM:0000761', 'MIM:0000862', 'MIM:0002227', 'MIM:0001139', 'MIM:0001389', 'MIM:0001639', 'MIM:0001663', 'MIM:0001956', 'MIM:0001805', 'MIM:0001903'}
cas_gap = set()  # Raw captures now fill the evidence gap; owner holds stay separate.
resolved_source_blocks = {'MIM:0000967','MIM:0001002','MIM:0001555','MIM:0001893','MIM:0002202','MIM:0002360'}
row_facts = []
evidence_cache = {}

def evidence_for(p):
    result = []
    if p is None: return result
    for e in p['evidence']:
        kind = e['kind']; h = None
        if kind == 'current_owner_assertion': continue
        if kind == 'prior_review': h = e['reference']['archive_sha256']
        elif isinstance(e.get('capture'), dict): h = e['capture']['sha256']
        elif isinstance(e.get('capture'), str): h = e.get('capture_sha256')
        elif e.get('sha256'): h = e['sha256']
        if not h: continue
        name = qualified(h)
        if h not in evidence_cache:
            evidence_cache[h] = read(Path(name), h)
        result.append({'path': name, 'sha256': h, 'basis_kind': kind,
                       'locator': e.get('target') or e.get('matches') or '/',
                       'scope': e.get('scope', 'Read captured declaration in its recorded acquisition scope; not fresh retrieval.')})
    return result

for entry in selection['rows']:
    row = entry['proposed_row']
    historical = entry['before_rows']
    focus = row if row is not None else historical[0]['row']
    mid = focus['subject_id']; obj = focus['object_id']
    owner = all_owner[entry['owner']]
    assert owner['mim_id'] == mid
    p = prior.get(key(focus))
    if p is None and mid in {'MIM:0000359','MIM:0000862','MIM:0002227'}:
        choices = [v for v in P if v['subject_id'] == mid]
        assert len(choices) == 1
        p = choices[0]
    assert p is not None, key(focus)
    evidence = evidence_for(p)
    additional = {
        'MIM:0002742': ['b92df3f1aedce5ed217cba4602fca7b156946d04db6f0ca479069f51255c60ba', 'ac546b35b48419fcefbe5d3571777c92d018bb0c50e75aea9ed8de3761ab2810'],
        'MIM:0002957': ['2724a0074719e6a1ba3cb6b324fc3efb08557d978b430ab4a9f295af8fd57367', '3f00d0eb7f2cfc6c54893c000a6f4d65470887de39303fdbb780c2c77aa6147b'],
        'MIM:0002450': ['0121ab59d06f166e61479bcd50f6f978678495c569589d8c7e4695af468fc2c2','8571ee98d9ac3ababd8de2db9df061787a4c7f2d39a363d8c5bc7edcd21ca414'],
        'MIM:0002512': ['5aafee16ecdde938c6369cd021d01d6e5d12631a0d172fbcd6b319fce567b6aa','a65b000884b3d2a6cd36a3d467fa44e00eef703e12b1ae6a2bddc46b5b6e4fec'],
        'MIM:0001387': ['9c6ae698406c969fff99ac0f6e08963d0d0f28915ac0c9b5855a865da5af383a','a407030b5bf0f9cc9d7284eaa9f4bd3c1b066eca79ba88973ae27356f46866ae','fc4f964faaaa5b45fc557b912d5ef4d11e6e3ff9bdf3ec3b9259d7e2d2acce88'],
    }
    for h in additional.get(mid, []):
        name = qualified(h)
        if h not in evidence_cache: evidence_cache[h] = read(Path(name), h)
        basis = 'conflicting_database_capture' if h in {'a407030b5bf0f9cc9d7284eaa9f4bd3c1b066eca79ba88973ae27356f46866ae','fc4f964faaaa5b45fc557b912d5ef4d11e6e3ff9bdf3ec3b9259d7e2d2acce88'} else 'actual_case_primary_capture'
        evidence.append({'path':name,'sha256':h,'basis_kind':basis,'locator':mid,
                         'scope':'Actual captured primary declaration; supplied-source procurement/quantity remains unapproved.'})
    if Path(entry['owner']).name in held_owner_names:
        h='64f143f6cf9c99359df8eb626ff266a59de99a98bb7b10acca6ea80051283189'
        evidence.append({'path':qualified(h),'sha256':h,'basis_kind':'prior_review','locator':Path(entry['owner']).name,'scope':'Current issue 1121 explicitly retains this whole owner under its unresolved scientific/material decision hold.'})
    if mid in current:
        assert current[mid]['owner']['sha256'] == entry['owner_sha256']
        for ref in current[mid]['original_source_delta_evidence']:
            if ref['sha256'] not in evidence_cache:
                evidence_cache[ref['sha256']] = read(Path(ref['path']), ref['sha256'])
            evidence.append({**ref, 'basis_kind': 'current_source_delta_evidence', 'locator': mid,
                             'scope': 'Actual source proposal evidence; classify raw authority separately from review/history.'})
    rationale = []
    if row is None:
        action = 'REMOVE_WITH_HISTORY'
        explanations = {
            'MIM:0000359': 'The generic apidaecin SCR mesh:C061361 is not the Ib concept. Actual NLM concept M0170179 and the explicit Apidaecin IB source support the current distinct assertion. Remove only the obsolete generic mapping, preserving its complete beforeimage, reviews and limitations; no peptide-sequence, lot or CAS inference.',
            'MIM:0000862': 'The current source-corrected owner rejects malformed cas:138-86-7. Raw source distinguishes d from DL limonene and captured ChEBI:15382 identifies the R form. Remove only the rejected historical CAS assertion; preserve its complete negative lineage and keep the new CHEBI row WITHHOLD.',
            'MIM:0001438': 'Original MediaDive 2082 identifies a complex phosphatidylcholine material, not the defined acyl-chain/stereochemical species CHEBI:86658. The applied owner remains the same permanent MIM concept, now unmapped. Remove this unsupported external assertion and retain all historical payload; no replacement external identity or source-binding approval.',
            'MIM:0002227': 'Source Sigma A9384 explicitly names the L-homocysteine material, corroborated by the official product capture and ChEBI:16680. The applied owner rejects malformed cas:9789-92-0. Remove only that historical CAS assertion with its full history; the new CHEBI row remains WITHHOLD.',
            'MIM:0002332': 'The old synthetic compound-namespace handle is not the current explicit ingredient-namespace identity of the 0.70 M stock. Native stock retirement evidence preserves current stock identity and its typed broader solute link. Remove only this obsolete assertion with its full beforeimage and all composition/source/alias holds.'}
        rationale.append(explanations[mid])
    else:
        action = 'INSTALL_WITHHOLD'
        if p['action'] in {'PROPOSE_RETAIN_QUALIFIED_SUPPORT','PROPOSE_SCOPED_SUPPORT_FROM_CURRENT_PRIMARY_EVIDENCE'}:
            action = 'INSTALL_SUPPORTED'
        if mid in resolved_source_blocks or mid in {'MIM:0002742','MIM:0000359'}:
            action = 'INSTALL_SUPPORTED'
        if p['action'] == 'BLOCK_OMISSION_RESTORE_PRIOR_WITHHOLD':
            action = 'INSTALL_WITHHOLD'
            rationale.append('Restore the current owner CAS assertion that the earlier candidate omitted without retirement evidence. Restoration preserves the original whole-row WITHHOLD and does not mint or approve chemistry.')
        if mid in mandatory:
            action = 'INSTALL_WITHHOLD'
            rationale.append('The current mandatory complete-row hold remains. Source correction, valid core identity, method/date changes and diagnostic retention do not clear inherited scientific decisions.')
        if mid == 'MIM:0000761':
            rationale.append('Issue 1121 retains the whole chromium-potassium double-salt owner under a grounding decision hold. CAS/name evidence cannot clear the potassium/stoichiometry mismatch with CHEBI:53471, so both current rows remain withheld.')
        if Path(entry['owner']).name in held_owner_names:
            action='INSTALL_WITHHOLD'
            rationale.append('Current issue 1121 holds this complete owner pending the named material/registry/ontology decision. Preserve all current assertions as withheld, including any historically supported CAS companion; correct core CAS evidence alone does not settle that owner-wide condition.')
        if mid=='MIM:0002450':
            rationale.append('Fresh PubChem CID 109334 properties/synonyms identify TAPSO CAS 68399-81-5, C7H17NO7S and the exact emitted IUPAC name plus its N-tris alternative. These support the current buffer concept and both current other names. The database also lists sodium-salt and unrelated contextual names; none is imported or used to collapse supplied forms. Peptide/diclocymet false hits stay rejected; no buffer role, sodium salt, stereoisomer, preparation or source occurrence is approved.')
        if mid=='MIM:0002512':
            rationale.append('Fresh PubChem CID 62646 properties establish Cl3Ti, trichlorotitanium and the III chloride name with CAS 7705-07-9. Support is scoped to this generic Ti(III) chloride concept, without selecting a polymorph or supplied solution. Mixed database synonyms such as methyltitanium(IV), aluminium-reduced material and HCl solutions are excluded. No merge to another record or source normalization is authorized.')
        if mid=='MIM:0001387':
            rationale.append('The captured primary paper PMC7346359 Methods explicitly names potassium phosphite monobasic KH2PO3 and supplier CAS 13977-65-6. This directly corroborates the existing salt/formula registry identity; the retained broad link to phosphonic acid is a typed salt-of relation, never subclass or exact identity. PubChem CID 23707081 instead encodes HKO3P+ and cannot establish the chemistry; its conflicting structure/formula is explicitly rejected, not imported. No BG-11 quantity, actual source occurrence, supplier procurement or functional-role approval follows.')
        if mid in {'MIM:0001805','MIM:0001903'}:
            rationale.append('METHOD_UNRESOLVED: historical DIRECT_MATCH is an aggregate default, not proof of lexical establishment. Neither an inferred lexical route nor the withdrawn blanket manual-route inference establishes the actual method.')
        if mid in cas_gap and obj.startswith('cas:'):
            action = 'INSTALL_WITHHOLD'
            rationale.append('Current captured closure has no raw claim-specific CAS/name authority for this external identity. Owner assertions and archived review prose do not replace the underlying response. Preserve the row, all existing chemistry and historical review, without claiming the identity is false.')
        # Historical W01 is a comment-only recommendation with explicit holds;
        # no blanket comment review becomes support for the full current row.
        if any(h['history_entry'] == 'history-001' for h in p['history_obligations']):
            action = 'INSTALL_WITHHOLD'
            rationale.append('The linked original W01 comment-retention review leaves its whole-row and forty scientific obligations pending. The comment and its complete original report are retained, but this review does not resolve all of those source/alias/material conditions or turn comment support into full-row approval.')
        if mid in current:
            rationale.append(current[mid]['scientific_conclusion'])
        elif p['scientific_rationale']:
            rationale.append(p['scientific_rationale'][0])
        if mid not in current and p['action'] == 'PROPOSE_SCOPED_SUPPORT_FROM_CURRENT_PRIMARY_EVIDENCE':
            rationale.append(p['scientific_rationale'][-1])
        if action == 'INSTALL_WITHHOLD':
            if p['prior_exact_reason']:
                rationale.append('Original complete-row reason retained: ' + p['prior_exact_reason'])
            rationale.append('Install this full row only as withheld evidence/backlog. No changed stamp, positive core target or local ID is used to release the negative decision.')
        else:
            if obj.startswith('kgmicrobe.'):
                rationale.append('The current maintained owner and permanent-ID/legacy registry establish this existing internal concept handle only. No external substance identity, source procurement equivalence, role, preparation or ontology parent follows from the handle.')
            else:
                rationale.append('Current captured target/source declarations corroborate this named material and the actual predicate within the retained qualified scientific scope. The historical assessment is context, not substituted primary authority. The complete current row, owner and all changed metadata/aliases are assessed here; source occurrence approval remains separate.')
            if p['prior_exact_reason']:
                rationale.append('Retained scope restriction from earlier assessment: ' + p['prior_exact_reason'])
        if focus['predicate_id'] != 'skos:exactMatch':
            rationale.append('The typed ' + focus['predicate_id'] + ' relation is not identity, replacement or subclass_of. Its form, salt, hydrate, preparation or similarity scope remains explicit.')
        assert row == entry['candidate_row'] or all(row[k] == entry['candidate_row'][k] for k in row if k not in {'source','comment'})
        for b in historical:
            assert set(filter(None,b['row']['source'].split('|'))) <= set(filter(None,row['source'].split('|')))
            assert not b['row']['comment'] or b['row']['comment'] in row['comment']
        rationale.append('All prior source tokens and nonempty comments survive the native proposed row. Mapping date is the latest recorded owner event, not new literature acquisition; deterministic confidence is not a calibrated probability. Cleared validation stamps remain in exact beforeimages and are not claimed as current checks.')
    rationale.append('Canonical installation only; no production release, source binding, role approval, identity collapse, subclass inference or KG rebuild. Full row beforeimages, owner evidence, suppressions and original W01/W09 history remain linked.')
    entry['disposition'] = action
    entry['reason'] = ' '.join(rationale)
    row_facts.append({'entry_id': entry['entry_id'], 'key': list(key(focus)),
        'owner': entry['owner'], 'owner_sha256': entry['owner_sha256'],
        'disposition': action, 'reason': entry['reason'], 'captured_evidence': evidence,
        'prior_proposal_action': p['action'], 'prior_disposition': p['prior_disposition'],
        'prior_exact_reason': p['prior_exact_reason'], 'history_obligations': p['history_obligations'],
        'prior_evidence': p['prior_original_evidence'],
        'current_owner_changed_since_original_proposal': p['owner_sha256'] != entry['owner_sha256'],
        'current_source_conclusion': current.get(mid),
        'complete_proposed_row': row, 'complete_before_rows': historical})
assert len(selection['rows']) == 3020 and len(selection['history']) == 2
erased = copy.deepcopy(selection)
for e in erased['rows']: e['disposition'] = e['reason'] = None
assert erased == native
assert sum(e['disposition']=='REMOVE_WITH_HISTORY' for e in selection['rows']) == 5

tree = w.Directory(D, guard)
receipt_path = D / 'PREPARATION-RECEIPT.json'
fd = os.open(receipt_path, os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW, 0o600)
handle = os.fdopen(fd, 'wb')
written = []
for name in ['CURRENT-DELTA-CELL-CONCLUSIONS.json','FOURTEEN-CURRENT-OWNER-CONCLUSIONS.json','CURRENT-HOLD-CONSTRAINTS.json','CANONICAL-CELL-CLASS-CONCLUSIONS.json']:
    written.append(tree.create(name, read(HERE/name)))
written.append(tree.create('author_selection.py', read(Path(__file__))))
written.append(tree.create('ASSESSED-SELECTION.json', encode(selection)))
facts = {'at':now(), 'reviewer':'Codex /root/s3_completed_source_audit', 'head':HEAD,
    'scope':'current complete canonical installation selection; not release approval',
    'prior_roles':'Source integrity auditor and seven-CAS skeptic; current primary is not independent of those own earlier conclusions. Separate publication skeptic required.',
    'counts':dict(Counter(e['disposition'] for e in selection['rows'])),
    'rows':row_facts, 'history':selection['history'], 'suppression':selection['suppression'],
    'payload_change_rule':'Only rows[].disposition and reason changed; erased pair equals exact native selection.',
    'science_reuse':'Reassessed complete current rows/owners against retained captured science; did not restamp historical votes or treat hashes as scientific authority.',
    'supplied_form_source_holds_preserved':True, 'scientific_release_approval':False}
written.append(tree.create('ROW-SCIENCE.json', encode(facts)))
extra = {str(f.path.relative_to(R)):sha(f.content) for f in written}
written.append(tree.create('INPUTS.json', encode({'inputs':{**inputs,**extra}})))

def recheck():
    assert head()==HEAD
    for f in captured+written: f.verify()
    tree.check()

recheck()
receipt = {'at':now(), 'status':'ASSESSED_SELECTION_AUTHORED_NOT_NATIVE_SAVED', 'head':HEAD,
           'reviewer':'Codex /root/s3_completed_source_audit', 'native_selection_sha256':'2c61399c7db7f5c90f254684a06dcd131105047cb104f6b6e341ae407e77cce7',
           'outputs':{str(f.path.relative_to(R)):sha(f.content) for f in written},
           'counts':facts['counts'], 'row_count':3020,'target_count':3023,
           'no_other_selection_field_changed':True, 'release_approval':False}
w.finish_owned_receipt(guard,handle,receipt_path,receipt,recheck)
tree.close()
print(json.dumps({'directory':str(D),'selection_sha256':sha((D/'ASSESSED-SELECTION.json').read_bytes()),'counts':facts['counts'],'native_saved':False}))
