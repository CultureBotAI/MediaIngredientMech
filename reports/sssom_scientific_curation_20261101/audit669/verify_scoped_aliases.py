from pathlib import Path
import csv,json,hashlib,datetime
RUN=Path(__file__).resolve().parents[1]; ROOT=RUN/'mim'; A=RUN/'audit669'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def rows(path):
 with path.open() as h:return list(csv.DictReader((x for x in h if not x.startswith('#')),delimiter='\t'))
receipt=json.loads((A/'seven-alias-apply.json').read_text());before=rows(A/'seven-alias-apply.before.tsv');after=rows(ROOT/'mappings/ingredient_mappings.sssom.tsv');plans=receipt['plans'];out=[]
assert len(before)==len(after)
for plan in plans:
 def selected(r):return all(r[k]==plan[k] for k in ['subject_id','predicate_id','object_id'])
 b=[r for r in before if selected(r)];n=[r for r in after if selected(r)];assert len(b)==len(n)==1
 expected=dict(b[0]);tokens=expected['other'].split('|');tokens.remove(plan['token']);expected['other']='|'.join(tokens);assert n[0]==expected
 assert sha(ROOT/plan['source_record'])==plan['owner_sha256']
 out.append({'selector':{k:plan[k] for k in ['subject_id','predicate_id','object_id']},'removed_token':plan['token'],'only_changed_fields':[k for k in b[0] if b[0][k]!=n[0][k]],'owner_sha256':plan['owner_sha256'],'owner_unchanged':True})
selected_keys={(p['subject_id'],p['predicate_id'],p['object_id']) for p in plans}
unselected_before=[r for r in before if (r['subject_id'],r['predicate_id'],r['object_id']) not in selected_keys];unselected_after=[r for r in after if (r['subject_id'],r['predicate_id'],r['object_id']) not in selected_keys];assert unselected_before==unselected_after
baseline=rows(ROOT/'mappings/other_cross_record_baseline.tsv');assert len(baseline)==38
carn=[r for r in after if r['subject_id']=='MIM:Carnitine_Hydrochloride'];assert len(carn)==2
parent=next(r for r in carn if r['object_id']=='CHEBI:17126');assert parent['other']=='DL-carnitine'
assert any(r['subject_id']=='MIM:Carnitine_Hydrochloride' and r['token']=='DL-carnitine' for r in baseline)
proof={'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'canonical_sha256':sha(ROOT/'mappings/ingredient_mappings.sssom.tsv'),'baseline_sha256':sha(ROOT/'mappings/other_cross_record_baseline.tsv'),'row_count':len(after),'seven_changes':out,'all_other_rows_unchanged_since_seven_transform':True,'baseline_count':len(baseline),'carnitine_parent_other':parent['other'],'carnitine_deferred_token_baseline_retained':True,'scope':'Comparisons are against canonical immediately before the seven-token transform; the preceding two-subject native splice is recorded separately.'}
(A/'post-apply-alias-proof.json').write_text(json.dumps(proof,indent=2)+'\n');print(json.dumps(proof,indent=2))
