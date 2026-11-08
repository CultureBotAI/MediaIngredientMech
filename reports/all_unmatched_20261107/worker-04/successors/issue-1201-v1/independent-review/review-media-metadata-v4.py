"""Independent byte-bounded review of the media evidence-kind correction."""
import copy,datetime,hashlib,json
from pathlib import Path
W=Path('reports/all_unmatched_20261107/worker-04');S=W/'successors/issue-1201-v1'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda p:json.loads(p.read_text())
prior=S/'independent-review/media-reviewed-by-chemistry-v3.json'
old=load(prior);review=copy.deepcopy(old);archive=S/'superseded/media-v2'
before=load(archive/'media-evidence.json');after=load(S/'fragments/media-evidence.json')
assert sha(archive/'media-evidence.json')==old['reviewed_fragment_hashes']['fragments/media-evidence.json']
assert len(before['evidence'])==len(after['evidence'])==77
changes=[]
for a,b in zip(before['evidence'],after['evidence']):
    assert a['evidence_id']==b['evidence_id']
    if a==b:continue
    assert {k:v for k,v in a.items() if k!='kind'}=={k:v for k,v in b.items() if k!='kind'}
    assert a['kind']=='owner_snapshot'
    if b['evidence_id'].startswith('I1201-MEDIA-LOOKUP-'):
        assert b['kind']=='local_validation'
        note='Capture is a local ignored-inclusive owner, label-index and frozen proposal/case comparison; classification as local_validation is appropriate, not remote scientific evidence.'
    else:
        assert b['evidence_id']=='I1201-MEDIA-CROSS-W07-CMRL' and b['kind']=='source_snapshot'
        note='Capture preserves the frozen worker07 source case and original owner overlap. source_snapshot expresses documentary provenance without claiming an independent supplier identity proof.'
    p=W/b['capture']['path'];assert sha(p)==b['capture']['sha256'];text=p.read_text();assert text
    changes.append({'evidence_id':b['evidence_id'],'before_kind':a['kind'],'after_kind':b['kind'],'capture_sha256':sha(p),'review_notes':note})
assert len(changes)==27
for kind in ['reassessments','decisions','proposals']:
    p=S/f'fragments/media-{kind}.json'
    assert sha(p)==old['reviewed_fragment_hashes'][str(p.relative_to(S))]
    assert p.read_bytes()==(archive/p.name).read_bytes()
for row in old['capture_integrity']['captures']:
    c=row['capture'];p=(W if c['root']=='artifact' else Q)/c['path'];assert sha(p)==c['sha256']
for p in review['payload_reviews']:
    assert sha(W/p['path'])==p['sha256']
    assert (W/p['path']).read_bytes()==(archive/Path(p['path']).name).read_bytes()
review['reviewed_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
review['reviewed_fragment_hashes']={f'fragments/media-{k}.json':sha(S/f'fragments/media-{k}.json') for k in ['reassessments','decisions','evidence','proposals']}
review['prior_review']={'path':str(prior.relative_to(S)),'sha256':sha(prior)}
review['metadata_amendment_review']={'scope':'Independently compared all77 evidence records and all four fragment/payload bindings against preserved v2 inputs. Exactly27 kind fields changed; all other evidence fields, raw captured bytes, URLs, original retrieval timestamps, scientific decisions and eighteen payloads are byte-identical. Prior complete scientific review remains applicable.','status':'PASS','changes':changes}
review['receipt_format_note']='Version4 accepts only the checked evidence-kind metadata correction and rebinds all final exact fragments. It incorporates the unchanged full scientific case and payload reviews from v3; all prior receipts remain preserved.'
review['findings'].append({'id':'MEDIA-I1201-CHEM-F4','severity':'contract metadata','finding':'27 evidence rows used unsupported owner_snapshot enum.','status':'resolved','resolution':'26 actual local lookup captures are local_validation and one frozen cross-shard case/owner snapshot is source_snapshot; no evidence promotion or provenance retiming.'})
out=S/'independent-review/media-reviewed-by-chemistry-v4.json';assert not out.exists();out.write_text(json.dumps(review,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'path':str(out.relative_to(S)),'sha256':sha(out),'changes':len(changes),'case_reviews':len(review['case_reviews']),'payload_reviews':len(review['payload_reviews']),'reviewed_fragment_hashes':review['reviewed_fragment_hashes']},indent=2))
