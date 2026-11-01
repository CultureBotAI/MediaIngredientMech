from pathlib import Path
import csv,json,hashlib,datetime,yaml
RUN=Path(__file__).resolve().parents[1];ROOT=RUN/'mim';A=RUN/'audit669'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(p):
 with p.open() as h:return list(csv.DictReader((x for x in h if not x.startswith('#')),delimiter='\t'))
canonical=rows(ROOT/'mappings/ingredient_mappings.sssom.tsv');baseline=rows(ROOT/'mappings/other_cross_record_baseline.tsv');review=json.loads((ROOT/'reports/sssom_completion_20260921/review.json').read_text());plans=json.loads((A/'seven-alias-apply.json').read_text())['plans'];before=rows(A/'seven-alias-apply.before.tsv');out=[]
for p in plans:
 match=lambda r: all(r[k]==p[k] for k in ['subject_id','predicate_id','object_id'])
 b=[r for r in before if match(r)];n=[r for r in canonical if match(r)];assert len(b)==len(n)==1
 expected=dict(b[0]);tokens=expected['other'].split('|');tokens.remove(p['token']);expected['other']='|'.join(tokens);assert n[0]==expected
 assert sha(ROOT/p['source_record'])==p['owner_sha256']
 assert not any(r['subject_id']==p['subject_id'] and r['token']==p['token'] for r in baseline)
 decisions=[r for r in review['decisions'] if r['owner_record']==p['source_record']];assert decisions and all(r['disposition']=='WITHHOLD' for r in decisions)
 out.append({'selector':{k:p[k] for k in ['subject_id','predicate_id','object_id']},'removed_token':p['token'],'only_changed_fields':['other'],'owner_unchanged':True,'owner_sha256':p['owner_sha256'],'dispositions':decisions})
assert len(baseline)==38
inventory=json.loads((A/'inventory.json').read_text());seven_yaml=[r for r in inventory['inventory'] if r['yaml_token_present']]
for r in seven_yaml:assert sha(Path(r['subject_path']))==r['subject_sha256']
selected={(p['subject_id'],p['token']) for p in plans};remaining={(r['subject_id'],r['token']) for r in inventory['inventory']}-selected;assert {(r['subject_id'],r['token']) for r in baseline}==remaining
recordpath='data/ingredients/mapped/Carnitine_Hydrochloride.yaml';rec=yaml.safe_load((ROOT/recordpath).read_text());old=yaml.safe_load((A/'carnitinamide-apply.before.yaml').read_text());alias='4-amino-2-hydroxy-N,N,N-trimethyl-4-oxobutan-1-aminium chloride'
assert set(rec)==set(old)
for key in rec.keys()-{'synonyms','curation_history'}:assert rec[key]==old[key]
assert rec['synonyms']==[{**old['synonyms'][0],'synonym_type':'REJECTED_LABEL'}]
assert rec['curation_history'][:-1]==old['curation_history'];assert rec['curation_history'][-1]['curator']=='reject_carnitinamide_synonym.py'
agg=yaml.safe_load((ROOT/'data/curated/mapped_ingredients.yaml').read_text())['ingredients'];matched=[r for r in agg if r['identifier']==rec['identifier'] and r['preferred_term']==rec['preferred_term']];assert matched==[rec]
with (ROOT/'docs/data/label_index.csv').open() as h: index=list(csv.DictReader(h))
assert not any(r['label'].casefold()==alias.casefold() for r in index)
carn=[r for r in canonical if r['subject_id']=='MIM:Carnitine_Hydrochloride'];assert len(carn)==2;parent=next(r for r in carn if r['object_id']=='CHEBI:17126');assert parent['other']=='DL-carnitine';assert any(r['subject_id']==parent['subject_id'] and r['token']=='DL-carnitine' for r in baseline)
carn_decisions=[r for r in review['decisions'] if r['owner_record']==recordpath];assert len(carn_decisions)==2 and all(r['disposition']=='WITHHOLD' for r in carn_decisions)
identity_holds={}
for slug in ['Carnitine_Dl_Hydrochloride','Sn-Glycerol_3-phosphate_Lithium_Salt']:
 dec=[r for r in review['decisions'] if r['owner_record']==f'data/ingredients/mapped/{slug}.yaml'];assert len(dec)==3 and all(r['disposition']=='WITHHOLD' for r in dec);identity_holds[slug]=dec
result={'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'canonical_sha256':sha(ROOT/'mappings/ingredient_mappings.sssom.tsv'),'review_sha256':sha(ROOT/'reports/sssom_completion_20260921/review.json'),'canonical_rows':len(canonical),'supported':sum(r['disposition']=='SUPPORTED' for r in review['decisions']),'withheld':sum(r['disposition']=='WITHHOLD' for r in review['decisions']),'seven_aliases':out,'seven_policy_records_unchanged':True,'exact_remaining_baseline_pairs_preserved':True,'baseline_count':len(baseline),'carnitine':{'record_sha256':sha(ROOT/recordpath),'aggregate_equal':True,'only_record_changes':['synonyms[0].synonym_type','curation_history[-1]'],'rejected_alias_absent_from_resolving_index':True,'canonical_rows':carn,'dispositions':carn_decisions,'deferred_DL_carnitine_retained':True},'identity_issue_holds':identity_holds}
(A/'final-scoped-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
