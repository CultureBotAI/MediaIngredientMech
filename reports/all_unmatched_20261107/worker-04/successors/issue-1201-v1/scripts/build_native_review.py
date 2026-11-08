"""Prepare exact successor targets and a fail-closed native source review."""
import datetime,hashlib,json,sys
from pathlib import Path
S=Path(__file__).resolve().parents[1];W=Path(__file__).resolve().parents[3];R=Path(__file__).resolve().parents[6]
REL=str(S.relative_to(R)); WREL=str(W.relative_to(R));sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
now=lambda:datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def verify_gates():
 bp=S/'validation/input-bindings.json';binding=json.loads(bp.read_text())
 for b in binding['files']+binding['gate_outputs']:assert sha(Path(b['path']))==b['sha256'],('changed gate input/output',b['path'])
 receipts=json.loads((S/'validation/command-receipts.json').read_text())
 for name in ['predecessor','structural','schema','overlay','guarded_writer','auditor_controls']:
  row=receipts[name];assert row['exit_code']==0,(name,row['exit_code'])
  assert row['input_binding_sha256']==sha(bp),('stale gate binding',name)
  assert sha(S/row['log'])==row['log_sha256'],('changed gate log',name)
 structural=receipts['structural'];audit_path=(S/structural['result_path']).resolve()
 assert audit_path.is_relative_to(S.resolve()),'structural result outside successor'
 assert str(audit_path)==structural['command'][structural['command'].index('--output')+1],'structural command/result path mismatch'
 assert sha(audit_path)==structural['result_sha256'],'changed structural result'
 assert {'path':str(audit_path),'sha256':sha(audit_path)} in binding['gate_outputs'],'structural result absent from output bindings'
 audit=json.loads(audit_path.read_text())
 assert audit['structural_accounting']=='PASS' and audit['scientific_adequacy_or_approval_established'] is False
 assert audit['accounted_case_count']==audit['assigned_shard_case_count']==188
 assert audit['independent_review_status_counts']=={'complete':188}
 assert json.loads((S/'validation/proposal-overlay.json').read_text())['status']=='PASS'
 assert json.loads((S/'validation/guarded-writer-replay.json').read_text())['status']=='PASS'
 return receipts
def build(mode):
 ds=json.loads((S/'decisions.json').read_text())['decisions']; byid={d['case_id']:d for d in ds}
 rs=json.loads((S/'reassessments.json').read_text())['reassessments']; reassess={a['case_id']:a for a in rs}
 assembly=json.loads((S/'validation/assembly-bindings.json').read_text())
 selected=set(reassess)|set(assembly['changed_cases']);ids=[d['case_id'] for d in ds if d['case_id'] in selected]
 groups={cid:b['group'] for b in assembly['bindings'] for cid in b['reviewed_case_ids']}
 targets=[]
 for cid in ids:
  d=byid[cid];t={'target_id':cid,'path':WREL+'/provenance/shard-04.json','selector':'cases[case_id='+cid+']','label':d['source']['source_label'] or '(blank original source label)','kind':'snapshot_row'}
  if d['owner_records']:t['owner_paths']=[{'repository':'CultureBotAI/MediaIngredientMech','path':o['path'],'role':'Frozen owner relevant to isolated proposal; inherited complete payload remains outside approval scope.'} for o in d['owner_records']]
  else:t['ownership_note']='Source-case target. New proposed owners are isolated prospective bytes, not invented maintained owner or publication approval.'
  targets.append(t)
 if mode=='targets':
  (S/'native-targets.json').write_text(json.dumps({'targets':targets},indent=2)+'\n');return
 receipts=verify_gates();inspection=json.loads((S/'validation/native-inspection.json').read_text());assert inspection['targets']==targets
 timestamp=now();es={e['evidence_id']:e for e in json.loads((S/'evidence.json').read_text())['evidence']};used=set()
 case_evidence={}
 for cid in ids:
  case_evidence[cid]=list(dict.fromkeys(byid[cid]['evidence_ids']+reassess.get(cid,{}).get('evidence_ids',[])+['I1201-INDEPENDENT-'+groups[cid]]))
  used.update(case_evidence[cid])
 eid={old:f'E{i:04d}' for i,old in enumerate(sorted(used),1)};evidence=[]
 kindmap={'primary_source':'primary_source','source_snapshot':'record_content','ontology':'database','native_record_review':'prior_review','independent_review':'prior_review','unsuccessful_search':'search','local_validation':'validation'}
 for old in sorted(used):
  e=es[old];cap=e['capture'];local_ref=(WREL+'/'+cap['path'] if cap['root']=='artifact' else 'frozen-queue:'+cap['path'])
  original_time=e.get('accessed_at');access=original_time or timestamp
  if access.endswith(' UTC'):
   parsed_access=datetime.datetime.strptime(access,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=datetime.timezone.utc)
  else:parsed_access=datetime.datetime.fromisoformat(access.replace('Z','+00:00'))
  dt=parsed_access.astimezone(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
  locator=e['locator']+'; evidence ID '+old+'; exact capture '+cap['root']+':'+cap['path']
  if not original_time:locator+='; accessed_at records local artifact inspection for this native review, NOT a new remote retrieval. Original retrieval timestamps remain in the unmodified capture/receipt; original URL: '+str(e.get('url'))
  row={'evidence_id':eid[old],'kind':kindmap[e['kind']] if original_time else ('search' if e['kind']=='unsuccessful_search' else 'record_content'),'reference':(e.get('url') or local_ref) if original_time else local_ref,'locator':locator,'accessed_at':dt,'support':'context_only' if e['kind']=='unsuccessful_search' else 'partial','summary':e['supports_or_contradicts'],'snapshot_sha256':cap['sha256']}
  if e['kind']=='unsuccessful_search':row['search_scope']='Only the recorded exact endpoint/query/catalog scope. Failed retrieval is not evidence of nonexistence; local catalog search scope is recorded in the capture.'
  evidence.append(row)
 checks=[]
 for name,row in receipts.items():
  vid='V-'+name;evidence.append({'evidence_id':vid,'kind':'validation','reference':REL+'/'+row['log'],'locator':'Actual command receipt with exact input and log hashes; validation/command-receipts.json','accessed_at':timestamp,'support':'supports','summary':name+' mechanical gate; no scientific or export approval.','snapshot_sha256':row['log_sha256']})
  checks.append({'check_id':name,'name':name.replace('_',' '),'status':'passed','required':True,'summary':'Actual exit0 on exact bound active188-case/proposal set; structural checks and scientific review have distinct scopes.','target_ids':ids,'command':json.dumps(row['command']),'exit_code':0,'expected_exit_code':0,'evidence_ids':[vid]})
 checks.append({'check_id':'maintained-integration','name':'Maintained integration and downstream rebuild','status':'not_applicable','required':False,'summary':'Isolated proposals only. Maintained data are unchanged; integration, complete-owner review and downstream gates belong to the coordinator.','target_ids':ids})
 assessments=[]
 for n,cid in enumerate(ids):
  d=byid[cid];a=reassess.get(cid);summary=d['reasoning'] if a is None else next((a[k] for k in ['reasoning','assessment','scientific_assessment'] if k in a),d['reasoning'])
  details='Final active disposition: '+d['disposition']+'. Proposal IDs: '+', '.join(d['proposal_ids'])+'. '
  if a:details+='Successor reassessment (exact author record): '+json.dumps(a,ensure_ascii=False)
  else:details+='Additional previously proposed case: shared-payload supersession and retained source/backlink review, not a new claim to rerun the entire original scientific review.'
  assessments.append({'assessment_id':f'A{n:03d}','area':'identity','topic':'No-change reassessment' if a else 'Shared-payload successor binding','outcome':'unknown' if d['disposition']=='unresolved' else 'supported','summary':summary,'details':details,'target_ids':[cid],'evidence_ids':[eid[x] for x in case_evidence[cid]]})
 ps=json.loads((S/'proposals.json').read_text())['proposals'];stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 review={'schema_version':'1.0.0','review_id':stamp+'-worker04-issue1201-successor','kind':'batch','repository':'CultureBotAI/MediaIngredientMech','title':'Worker04 issue1201: complete no-change reassessment and isolated successor proposals','started_at':inspection.get('inspected_at',timestamp),'finished_at':timestamp,'reviewer':{'identity':'Codex worker04 /root; primary biological/chemistry/media and separate skeptical ring','kind':'agent','independence':'self_review','independence_basis':'Root authored consolidation. Different named agents reviewed each primary fragment and every exact changed payload; all108 reassessment scopes, additional changed bindings and reviews are hash-bound in assembly-bindings and independent-review.'},'skill':'.claude/skills/add-media/SKILL.md; .claude/skills/map-media-ingredients/SKILL.md; .claude/skills/review-ingredients/SKILL.md','completion':'completed','verdict':'needs_curation','native_verdict':'Successor source/proposal review completed; scientific holds and coordinator integration remain. No complete-owner or release approval.','scientific_review':True,'summary':f'All108 predecessor no-proposal cases reassessed; {len(ids)-108} additional cases reviewed for shared-payload successor bindings. Active whole-shard accounting remains188 cases with {len(ps)} proposals. The predecessor review and every original artifact remain immutable.','source':inspection['source'],'scope':{'description':'Full no-proposal cohort reassessment, plus exact changed bindings of previously proposed source cases. Whole188-case validation is mechanical accounting; unselected scientific assessments are inherited without a new review claim.','selection':'All108 predecessor decisions without proposal_ids, union every source case whose successor payload/binding changed.','coverage':'full','population_size':len(ids),'reviewed_target_ids':ids,'exclusions':[{'target':'Other predecessor source cases','reason':'Original independently reviewed assessment preserved; only full-shard structural revalidation performed.'},{'target':'Whole-owner publication, roles, source/export selector release, other shards','reason':'No authorization or approval inferred from isolated proposals.'}]},'targets':targets,'checks':checks,'evidence':evidence,'assessments':assessments,'findings':[],'actions':[{'action_id':'coordinator-integration','description':'Reconcile reviewed successor proposals with all other shard deltas and original baseline owners. Apply accepted nonconflicting proposals through guarded writer, with full-owner rereview and retained source holds.','target_ids':ids,'ownership_note':'Coordinator; worker has not edited maintained data. Existing issues1190/1191/1192/1173 and campaign1201 retain their independent scopes.','acceptance_checks':['Use active proposals.json and immutable supersession bindings; retain every original case link.','Resolve cross-shard-dependencies.json and do not duplicate existing owners or choose another worker winner.','Preserve #312 human-protein exclusion, role restrictions and all source-specific holds.','Run maintained synchronization and native publication gates only after authorized integration.']}],'limitations':['No new independent defect is asserted by an empty findings list; existing predecessor findings remain open and are not retired or superseded here. Issue1201 tracks this bounded completion work.','Source-defined partial preparations do not certify absent ingredients, unknown yields, solvent, quantities, formulation, stoichiometry or product version. Actual missing facts and performed searches remain per case.','Exact primary capture bytes and original retrieval timestamps are preserved. Native entries without a top-level original retrieval time explicitly report local artifact inspection; they never invent a fresh remote retrieval.','Unchanged original assessments and original review limitations remain applicable outside the successor scientific scope.','New registry or broader ontology mappings are prospective identities, not owner/export approval. Receiving-medium dose/unit repairs do not silently create stock composition.'],'related_reviews':[{'repository':'CultureBotAI/MediaIngredientMech','review_id':'20261108T053803Z-worker04-all-unmatched-source-review','relationship':'Scoped supplementary source/proposal reassessment and immutable successor bindings. Does not retire, close or replace any predecessor finding or its unreviewed targets.'}],'tags':['worker04','issue1201','successor','proposals-only'],'links':['https://github.com/CultureBotAI/MediaIngredientMech/issues/1201']}
 for action in review['actions']:action.setdefault('finding_ids',[])
 (S/'native-review-content.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n');print(review['review_id'])
if __name__=='__main__':build(sys.argv[1])
