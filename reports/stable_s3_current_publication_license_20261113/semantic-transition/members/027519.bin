"""2026-11-12: immutable scientific successor after independent review.

Requires the actual filed-issue reference and both saved findings. Preserves the
complete v1 selection/inspection and every source byte. Only the nicotine and
disodium-malate dispositions/reasons become WITHHOLD. One arabinan reason is
clarified to distinguish captured source table from uncaptured manufacturer
response, with no disposition change. Uses the reviewed private writer.
"""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import argparse,copy,hashlib,json,os,subprocess,sys,types

p=argparse.ArgumentParser()
p.add_argument('--issue-receipt',type=Path,required=True)
p.add_argument('--issue-receipt-sha256',required=True)
p.add_argument('--issue-url',required=True)
a=p.parse_args()
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
R=C/'integration/stable-method-cumulative-source-canary-target'
OLD=R/'.temp/s3-publication-primary-native-v1'
D=R/'.temp/s3-publication-primary-native-v2'
HERE=Path(__file__).parent
HEAD='f4b6712d9b8a888c03389149283ee2b7d124bf13'
sha=lambda b:hashlib.sha256(b).hexdigest()
now=lambda:datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
encode=lambda o:(json.dumps(o,indent=2,sort_keys=True,ensure_ascii=False)+'\n').encode()
helper=C/'preflight/stable-adoption1303-input-copy-helper-v3/copy_inputs.py'
raw=helper.read_bytes();assert sha(raw)=='e8555db0f01f30140d5a619754cad600e74e2a4a801acbbcdaacc5ce7feec504'
w=types.ModuleType('_s3_primary_v2_writer');w.__file__=str(helper);sys.modules[w.__name__]=w
exec(compile(raw,str(helper),'exec'),w.__dict__);guard=w.load_guard();frozen=[]
def read(path,expected=None):
    f=guard.FrozenFile.capture(path);assert expected is None or sha(f.content)==expected,path
    frozen.append(f);return f.content
def doc(path,expected=None):return json.loads(read(path,expected))
assert a.issue_url.startswith('https://github.com/CultureBotAI/MediaIngredientMech/issues/')
issue=read(a.issue_receipt.absolute(),a.issue_receipt_sha256)
selection=doc(OLD/'ASSESSED-SELECTION.json','344937a9a999919dfad62e12ab5cb7798b7ab49c0122a31ae3613cbe475ade68')
original=copy.deepcopy(selection)
facts=doc(OLD/'ROW-SCIENCE.json')
native=doc(R/'.temp/cumulative-source-publication-inspect-s3-v1/UNASSESSED-SELECTION.json','2c61399c7db7f5c90f254684a06dcd131105047cb104f6b6e341ae407e77cce7')
old_recovery=doc(OLD/'PREPARATION-RECEIPT-RECOVERY.json','eb97728e4bcae6de08fab38a37ca53f58173d39e07435c08a1fc6afd99d5f5ad')
finding_paths={
 'row-002125':(C/'preflight/s3-publication-skeptic-actual-selection-v1/NICOTINE-FORM-FINDING.json','7f1c38859759241f913a3971c049cfa01ac9a0210299c85f1896ea66ef7abd3d'),
 'row-001090':(HERE/'DISODIUM-MALATE-RACEMATE-FINDING.json','6984ba6bdc8fe56a44c986fd76550281431be2f6d9687783f6eba7cd36c9e295')}
findings={k:read(path,h) for k,(path,h) in finding_paths.items()}
reasons={
 'row-002125':'INSTALL_WITHHOLD: CHEBI:18723 explicitly denotes an equimolar R/S nicotine racemate. The current Nicotine (Fluka) owner has only a generic normalized lexical match, with no original stereo specification, CAS or product catalogue evidence establishing a racemate. The historical positive report does not supply that missing form evidence. Exact target-label agreement cannot select a stereochemical mixture. Preserve the complete existing assertion and earlier positive/negative history as withheld; do not infer pure S, pure R, another CAS/ontology target or a particular supplier preparation.',
 'row-001090':'INSTALL_WITHHOLD: CHEBI:91260 explicitly denotes an equimolar R/S disodium-malate racemate. The current owner contains only the unqualified MicrobeDecoder disodium_malate label and utilisation observations, with no original CAS, stereochemical or reagent specification. The historical report incorrectly treats this racemate as a generic parent of the stereospecific siblings; ontology resolution alone does not prove a mixture. Preserve the complete current assertion and history as withheld. Do not guess L, D, DL, hydration, quantity, source occurrence identity or an alternative ontology.'}
changed=[]
for e,f in zip(selection['rows'],facts['rows'],strict=True):
    assert e['entry_id']==f['entry_id']
    if e['entry_id']=='row-000416':
        old='Current Megazyme P-ARAB and ChEBI primary evidence supports botanical-source arabinan to broader polymer; retain #390 predicate semantics.'
        new='The actual CultureBotHT source capture, line 1288, explicitly names Arabinan from Sugar Beet with Megazyme P-ARAB and CAS 11078-27-6. Together with the captured CHEBI:22590 arabinan class, this supports the botanical-source arabinan to broader polymer relation under section 1 and #390. The present packet does not supply a raw manufacturer response; earlier manufacturer wording below is historical review context only, not current primary authority.'
        assert old in e['reason'] and e['disposition']=='INSTALL_SUPPORTED'
        e['reason']=f['reason']=e['reason'].replace(old,new)
        changed.append(e['entry_id'])
        continue
    if e['entry_id'] not in reasons:continue
    assert e['disposition']==f['disposition']=='INSTALL_SUPPORTED'
    reason=reasons[e['entry_id']]+' Filed review follow-up: '+a.issue_url+'. Canonical installation only; retain all full row beforeimages, source tokens, comments, original W01/W09 obligations and suppressions. No production release, source binding, role approval, identity collapse or subclass inference.'
    e['disposition']=f['disposition']='INSTALL_WITHHOLD';e['reason']=f['reason']=reason
    f['v2_review_finding']={'issue':a.issue_url,'finding_path':str((D/Path(finding_paths[e['entry_id']][0]).name).relative_to(R)),'sha256':finding_paths[e['entry_id']][1]}
    changed.append(e['entry_id'])
assert set(changed)==set(reasons)|{'row-000416'}
assert [e['entry_id'] for e,o in zip(selection['rows'],original['rows'],strict=True) if e!=o]==changed
erased=copy.deepcopy(selection)
for e in erased['rows']:e['disposition']=e['reason']=None
assert erased==native
facts['counts']=dict(Counter(e['disposition'] for e in selection['rows']))
facts['at']=now();facts['v2_changes']={'predecessor_sha256':'344937a9a999919dfad62e12ab5cb7798b7ab49c0122a31ae3613cbe475ade68','rows':changed,'issue':a.issue_url,'no_source_or_other_selection_change':True}
tree=w.Directory(D,guard)
receipt=D/'PREPARATION-RECEIPT.json'
handle=os.fdopen(os.open(receipt,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600),'w',encoding='utf-8')
written=[]
for name in ['CURRENT-DELTA-CELL-CONCLUSIONS.json','FOURTEEN-CURRENT-OWNER-CONCLUSIONS.json','CURRENT-HOLD-CONSTRAINTS.json','CANONICAL-CELL-CLASS-CONCLUSIONS.json']:
    written.append(tree.create(name,read(OLD/name)))
written.append(tree.create('author_selection_v2.py',read(Path(__file__))))
written.append(tree.create('FILED-FINDING-ISSUE.json',issue))
for k,raw in findings.items():written.append(tree.create(Path(finding_paths[k][0]).name,raw))
written.append(tree.create('ASSESSED-SELECTION.json',encode(selection)))
written.append(tree.create('ROW-SCIENCE.json',encode(facts)))
base=doc(OLD/'INPUTS.json')['inputs']
for name in ['INPUTS.json','PREPARATION-RECEIPT.json','AUTHORING-FAILURE.json','PREPARATION-RECEIPT-RECOVERY.json','INSPECT-RESULT.json','INSPECT.stdout.json','INSPECT-VERIFIED.json']:
    base[str((OLD/name).relative_to(R))]=sha(read(OLD/name))
extra={str(f.path.relative_to(R)):sha(f.content) for f in written}
written.append(tree.create('INPUTS.json',encode({'inputs':{**base,**extra}})))
def recheck():
    assert subprocess.check_output(['git','--no-optional-locks','rev-parse','HEAD'],cwd=R,timeout=30).decode().strip()==HEAD
    for f in frozen+written:f.verify()
    tree.check()
recheck()
result={'at':now(),'status':'IMMUTABLE_REVIEW_SUCCESSOR_AUTHORED','head':HEAD,'actor':'/root/s3_completed_source_audit','changed_rows':changed,'disposition_changes':['row-001090','row-002125'],'reason_only_clarification':'row-000416','issue':a.issue_url,'counts':facts['counts'],'predecessor_preserved':True,'only_disposition_reason_changed':True,'native_saved':False,'outputs':{str(f.path.relative_to(R)):sha(f.content) for f in written}}
w.finish_owned_receipt(guard,handle,receipt,result,recheck);handle.close();tree.close()
print(json.dumps({'path':str(D/'ASSESSED-SELECTION.json'),'sha256':sha((D/'ASSESSED-SELECTION.json').read_bytes()),'counts':facts['counts'],'receipt_sha256':sha(receipt.read_bytes())}))
