"""Preserve challenged draft bytes and apply three narrow overlay corrections."""
import copy, datetime, hashlib, json, shutil
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import write_validated_ingredient, validate_ingredient
from mediaingredientmech.curate.curation_event import record_curation_event

W=Path('reports/all_unmatched_20261107/worker-04'); S=W/'successors/issue-1201-v1'
F=S/'fragments'; C=S/'captures/chemistry'; A=C/'overlay-corrections-v1'
assert not A.exists(), 'Do not overwrite preserved reviewed bytes'
A.mkdir(parents=True)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
manifest=[]
def archive(p):
    q=A/p.relative_to(S);q.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(p,q)
    manifest.append({'path':str(p.relative_to(S)), 'archive':str(q.relative_to(S)), 'sha256':sha(q)})
for name in ['reassessments','decisions','evidence','proposals']:
    archive(F/f'chemistry-{name}.json')
archive(F/'chemistry-successor.py');archive(C/'integrity-final.json')
ps=json.loads((F/'chemistry-proposals.json').read_text())
edits=[]
for p in ps['proposals']:
    path=W/p['after_capture']['path']
    assert sha(path)==p['after_capture']['sha256']
    r=yaml.safe_load(path.read_text()); before=copy.deepcopy(r)
    if p['proposal_id']=='I1201-CHEM-P-nbrc_1378_fenaedta_stock':
        assert r['synonyms']==[{'synonym_text':'FeNaEDTA','synonym_type':'REJECTED_LABEL','source':'https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1378'}]
        del r['synonyms']
        change='Remove the rejected FeNaEDTA synonym because native partonomy treats every alias as a possible identity self-reference. Preserve the exact raw source label FeNaEDTA here and in source evidence; it is not a globally resolving alias for this stock. Component and stock concentration claims are unchanged.'
        r['notes']+=' '+change
    elif p['proposal_id'] in {'I1201-CHEM-P-trisodium-citrate-pentahydrate','I1201-CHEM-P-trisodium-citrate-trihydrate'}:
        assert r['ontology_mapping']['ontology_id']=='CHEBI:53258'
        assert r['ontology_mapping']['ontology_label']=='trisodium citrate'
        r['ontology_mapping']['ontology_label']='sodium citrate'
        change='Correct CHEBI:53258 ontology_label to the canonical local ontology label sodium citrate. The distinct hydrate identifier, supplied water count and asymmetric NARROW_MATCH mapping remain unchanged.'
    else: continue
    archive(path)
    record_curation_event(r,curator='codex_worker04_chemistry_issue1201',action='CORRECTED',changes=change,previous_status=r['mapping_status'],new_status=r['mapping_status'],llm_assisted=True,timestamp=now)
    write_validated_ingredient(r,path)
    oldhash=p['after_capture']['sha256'];p['after_capture']['sha256']=sha(path)
    edits.append({'proposal_id':p['proposal_id'],'path':str(path.relative_to(S)), 'before_sha256':oldhash,'after_sha256':sha(path),'change':change})
assert len(edits)==3
(F/'chemistry-proposals.json').write_text(json.dumps(ps,indent=2,ensure_ascii=False)+'\n')
# Keep the first-stage authoring script consistent, without rerunning it or retiming captures.
builder=F/'chemistry-successor.py'; text=builder.read_text()
text=text.replace("'CHEBI:53258','trisodium citrate',notes", "'CHEBI:53258','sodium citrate',notes")
text=text.replace("'ontology_id':'CHEBI:53258','ontology_label':'trisodium citrate'", "'ontology_id':'CHEBI:53258','ontology_label':'sodium citrate'")
text=text.replace(" return propose(key,[n],r,label.replace(' ','_'),notes)", " if key=='nbrc_1378_fenaedta_stock':\n  r.pop('synonyms'); r['notes']+=' Exact raw source label FeNaEDTA is retained as provenance only, not a globally resolving stock alias.'\n return propose(key,[n],r,label.replace(' ','_'),notes)")
builder.write_text(text)
receipt={'checked_at':now,'status':'PASS','scope':'Three narrow draft corrections after actual combined overlay failure; no maintained owner, source capture, role or publication-hold change. Prior independently reviewed bytes preserved. No remote retrieval occurred.','archived_files':manifest,'edits':edits,'all_four_fragments':{str((F/f'chemistry-{name}.json').relative_to(S)):sha(F/f'chemistry-{name}.json') for name in ['reassessments','decisions','evidence','proposals']}}
for p in ps['proposals']:
    path=W/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256']
    assert not validate_ingredient(yaml.safe_load(path.read_text())),p['proposal_id']
receipt['all_ten_payloads_closed_schema_pass']=True
(C/'overlay-corrections-v1.json').write_text(json.dumps(receipt,indent=2)+'\n')
integrity=json.loads((C/'integrity-final.json').read_text())
integrity['checked_at']=now;integrity['fragments']=receipt['all_four_fragments'];integrity['after_payloads']=[p['after_capture'] for p in ps['proposals']]
integrity['narrow_overlay_correction_receipt']={'path':str((C/'overlay-corrections-v1.json').relative_to(S)),'sha256':sha(C/'overlay-corrections-v1.json')}
(C/'integrity-final-v2.json').write_text(json.dumps(integrity,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
