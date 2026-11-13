"""2026-11-13: author current S3 installation judgments after actual inspection.

Fixed current S3 qualification only. Requires exact actual qualified input-map
and unassessed-selection hashes. Reuses this scientist's still-applicable
complete earlier row reasons only after strict full-payload/owner/history
comparison and explicit current applicability assessment. No old report is
restamped; separate native inspect/save and skeptical assessment follow.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, copy, hashlib, json, os, subprocess, sys, types
C = Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R = C/'integration/stable-method-cumulative-source-canary-target'
D = R/'.temp/s3-publication-primary-native-license-v1'
OLD = R/'.temp/s3-publication-primary-native-requalified1401-v1'
HEAD = 'eeb586afd00af70997b0f46e76c08e8cfa074665'
WRITER = C/'preflight/stable-adoption1303-input-copy-helper-v3/copy_inputs.py'
sha = lambda b: hashlib.sha256(b).hexdigest()
encode = lambda v: (json.dumps(v,indent=2,sort_keys=True,ensure_ascii=False)+'\n').encode()
now = lambda: datetime.now(timezone.utc).isoformat()
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
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--inputs-sha256',required=True)
    p.add_argument('--native-selection-sha256',required=True)
    a=p.parse_args()
    for v in vars(a).values(): assert len(v)==64 and set(v)<=set('0123456789abcdef')
    w,wr,wb=bootstrap(WRITER,'e8555db0f01f30140d5a619754cad600e74e2a4a801acbbcdaacc5ce7feec504','_current_primary_writer')
    gp=w.W/w.GUARD;guard,gr,gb=bootstrap(gp,w.GUARD_SHA,'_current_primary_guard')
    captured=[]
    def read(path,h=None):
        f=guard.FrozenFile.capture(path);assert h is None or sha(f.content)==h,str(path)
        captured.append(f);return f.content
    def doc(path,h=None): return json.loads(read(path,h))
    git=lambda *v:subprocess.check_output(['git','--no-optional-locks',*v],cwd=R,timeout=60)
    assert Path.cwd()==R and git('rev-parse','HEAD').decode().strip()==HEAD
    index=git('ls-files','--stage','-z')
    assert git('diff','--name-only')==b'' and git('diff','--cached','--name-only')==b''
    inputs_path=R/'.temp/s3-publication-current-evidence-license-v1/INPUTS.json'
    base=doc(inputs_path,a.inputs_sha256)['inputs']
    native_path=R/'.temp/cumulative-source-publication-inspect-s3-license-v1/UNASSESSED-SELECTION.json'
    native=doc(native_path,a.native_selection_sha256)
    old=doc(OLD/'ASSESSED-SELECTION.json','cefdc225dbfb44dc56898d676b625d8ed325f9d03572121f40fc1e9586e0d7c2')
    facts=doc(OLD/'ROW-SCIENCE.json','c99a38957e80cc8f27623f1b126b65e047d784cbc4d55067c99890099cdb3fd4')
    # Current prior-analysis files are explicit supplements, never substitutions for base inputs.
    for prior_name,prior_pin in [('ASSESSED-SELECTION.json','cefdc225dbfb44dc56898d676b625d8ed325f9d03572121f40fc1e9586e0d7c2'),('ROW-SCIENCE.json','c99a38957e80cc8f27623f1b126b65e047d784cbc4d55067c99890099cdb3fd4')]:
        prior_rel=str((OLD/prior_name).relative_to(R))
        assert prior_rel not in base or base[prior_rel]==prior_pin, 'conflicting prior-analysis input'
        read(OLD/prior_name,prior_pin)
        base[prior_rel]=prior_pin
    assert base[str((OLD/'ASSESSED-SELECTION.json').relative_to(R))]=='cefdc225dbfb44dc56898d676b625d8ed325f9d03572121f40fc1e9586e0d7c2'
    assert base[str((OLD/'ROW-SCIENCE.json').relative_to(R))]=='c99a38957e80cc8f27623f1b126b65e047d784cbc4d55067c99890099cdb3fd4'
    assert native['context']['generation']=={'path':'.temp/cumulative-source-generated-s3-license-v1/receipt.json','sha256':'37e36398eac724b3eb13acd2156c819c4dadc0163ee4bbf09a3926e95e1ed524'}
    erased=copy.deepcopy(old)
    erased['context']['generation']=native['context']['generation']
    for e in erased['rows']:e['disposition']=e['reason']=None
    assert erased==native,'Unexpected current row/context/history/suppression drift requires new assessment'
    assert len(native['rows'])==3020 and len(native['history'])==2
    for path,h in native['context']['owners'].items():read(R/path,h)
    notes_path=C/'preflight/s3-publication-primary-license-current-readiness-v1/CURRENT-READINESS-NOTES.json'
    notes_raw=read(notes_path,'cfe9cce26903ace86c320f26eca37c43ae745524a2ce4e8e68f568ee52107bcb')
    notes=json.loads(notes_raw);assert notes['source_head']==HEAD and notes['scientific_approval_added'] is False
    readiness=C/'preflight/s3-publication-primary-license-current-readiness-v1'
    hydrate=doc(readiness/'HYDRATE-ORIGIN-CLOSURE.json','2f2c840d2d415e7e83ac539129b5fce988c53e6bea17674ca4d206a25702cfd6')
    assert hydrate['current_native_assessment'] is None and hydrate['new_origin_fetch'] is False
    for path,h in hydrate['inputs'].items():read(R/path,h);base[path]=h
    readback=doc(readiness/'FULL-READBACK.json','678d093726d8107a708cecd3ca09bcda71c2dbf17174b1b7739d66a77d181e35')
    assert readback['head']==HEAD and readback['rows']==3015 and readback['owners_read']==2957 and readback['current_scientific_approval'] is False
    candidate=read(R/'.temp/cumulative-source-generated-s3-license-v1/candidate.sssom.tsv','3fdd2f7e8e1542bfc3103816459755202b78d00a821a29974a18f4dd3f1dfb64')
    assert b'# license: "https://creativecommons.org/licenses/by/4.0/"\n' in candidate.split(b'subject_id\t',1)[0]
    for path,h in notes['input_pins'].items():read(R/path,h)
    selection=copy.deepcopy(native)
    for entry,previous,fact in zip(selection['rows'],old['rows'],facts['rows'],strict=True):
        assert entry['entry_id']==previous['entry_id']==fact['entry_id']
        assert previous['disposition']==fact['disposition'] and previous['reason']==fact['reason']
        action=previous['disposition']
        assert action in ({'REMOVE_WITH_HISTORY'} if entry['proposed_row'] is None else {'INSTALL_SUPPORTED','INSTALL_WITHHOLD'})
        if entry.get('mandatory_disposition'):assert action==entry['mandatory_disposition']
        reason=('Current license-corrected publication assessment: I have read the complete current assertion, owner, claim-specific captured authority and preserved negative conditions. The project-authored header now correctly states CC BY4.0; this metadata correction grants no chemistry, source identity, role or release support. Current claim-specific conclusion and its complete inherited scope: '+previous['reason'].replace('Fresh PubChem','Captured PubChem'))
        subject=(entry['proposed_row'] or entry['before_rows'][0]['row'])['subject_id']
        if subject in hydrate['current_scientific_readiness_notes']:
            reason+=' Current direct origin-capture reading: '+hydrate['current_scientific_readiness_notes'][subject]
            envelope=next(e for e in hydrate['source_envelopes'] if e['subject_id']==subject)
            for source in envelope['sources']:
                fact['captured_evidence'].append({'basis_kind':('actual_case_primary_capture' if source['source_id'] in {'pubchem-16217716-properties','pubchem-16217716-cas','pubchem-92817-properties','ols-chebi-6731','pubchem-516899-properties','pubchem-516899-cas','ols-chebi-132103'} else 'conflicting_database_capture' if source['source_id']=='ols-chebi-183824' else 'case_context_capture'),'path':source['path'],'sha256':source['sha256'],'locator':source.get('url','/'),'scope':'Existing archived origin response; original retrieval '+str(source.get('retrieved_at'))+'; HTTP '+str(source.get('http_status'))+'. Scope restricted to exact current hydrate identity/form comparison; failed responses do not establish term status.'})
        entry['disposition']=fact['disposition']=action;entry['reason']=fact['reason']=reason
    check=copy.deepcopy(selection)
    for e in check['rows']:e['disposition']=e['reason']=None
    assert check==native
    facts.update(at=now(),head=HEAD,prior_roles='Current primary and Claw license-fix author; earlier publisher/source technical and CAS skeptical roles. Root owns this current generation and inspection. Separate current skeptic required.',science_reuse='Explicit current reassessment of unchanged full assertions/supplied scope using prior complete claim-specific work and current critical raw-authority/negative-condition reads; no copied report or inherited reviewer identity.',counts=dict(Counter(e['disposition'] for e in selection['rows'])))
    facts['metadata_review']={'candidate_sha256':'3fdd2f7e8e1542bfc3103816459755202b78d00a821a29974a18f4dd3f1dfb64','license':'https://creativecommons.org/licenses/by/4.0/','scope':'Project-authored mapping/data scope only; upstream notices and prior-release licenses remain. No scientific support follows from this correction.'}
    facts['current_requalification']={'previous_selection_sha256':'cefdc225dbfb44dc56898d676b625d8ed325f9d03572121f40fc1e9586e0d7c2','previous_fact_sha256':'c99a38957e80cc8f27623f1b126b65e047d784cbc4d55067c99890099cdb3fd4','native_selection_sha256':a.native_selection_sha256,'only_context_change':'actual generation receipt; all row cells, owners, history, suppressions and scientific conditions equal','current_applicability_notes':str((D/notes_path.name).relative_to(R)),'new_release_or_source_approval':False}
    tree=w.Directory(D,guard);written=[]
    fd=os.open('PREPARATION-RECEIPT.json',os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600,dir_fd=tree.fd)
    with os.fdopen(fd,'w',encoding='utf-8') as handle:
        def recheck():
            wb();gb();tree.check()
            assert git('rev-parse','HEAD').decode().strip()==HEAD and git('ls-files','--stage','-z')==index
            for f in captured+written:f.verify()
        read(WRITER,sha(wr));read(gp,sha(gr));recheck()
        for name in ['CURRENT-DELTA-CELL-CONCLUSIONS.json','FOURTEEN-CURRENT-OWNER-CONCLUSIONS.json','CURRENT-HOLD-CONSTRAINTS.json','CANONICAL-CELL-CLASS-CONCLUSIONS.json']:
            written.append(tree.create(name,read(OLD/name)))
        written.append(tree.create(notes_path.name,notes_raw))
        for name in ['HYDRATE-ORIGIN-CLOSURE.json','FULL-READBACK.json','READINESS-HANDOFF.json']:
            written.append(tree.create(name,read(readiness/name)))
        written.append(tree.create('AUTHORING.py',read(Path(__file__).absolute())))
        written.append(tree.create('ASSESSED-SELECTION.json',encode(selection)))
        written.append(tree.create('ROW-SCIENCE.json',encode(facts)))
        base[str(inputs_path.relative_to(R))]=a.inputs_sha256
        base.update({str(f.path.relative_to(R)):sha(f.content) for f in written})
        written.append(tree.create('INPUTS.json',encode({'inputs':base})))
        result={'at':now(),'state':'CURRENT_FULL_INSTALLATION_JUDGMENTS_AUTHORED_NOT_NATIVE_SAVED','head':HEAD,'actor':'/root/s3_completed_source_audit','counts':facts['counts'],'only_disposition_reason_changed':True,'original_reports_unchanged':True,'scientific_release_approval':False,'outputs':{str(f.path.relative_to(R)):sha(f.content) for f in written}}
        raw=w.finish_owned_receipt(guard,handle,D/'PREPARATION-RECEIPT.json',result,recheck)
    tree.close()
    print(json.dumps({'path':str(D/'ASSESSED-SELECTION.json'),'sha256':sha((D/'ASSESSED-SELECTION.json').read_bytes()),'receipt_sha256':sha(raw),'counts':facts['counts']}))
if __name__=='__main__':main()
