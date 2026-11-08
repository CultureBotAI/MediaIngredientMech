from pathlib import Path
import json,hashlib,subprocess,datetime,yaml,collections
R=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech');C=R/'.temp/all-unmatched-20261107';O=C/'preflight/w03-current-provenance-allowlist-v1';W=C/'workers/w03/worktree';A=W/'reports/all_unmatched_20261107/worker-03';P=A/'successors/issue1224-v1/publication-v1';F=C/'workers/w02/worktree/.temp/campaign-evidence-provenance-audit-v1';HEAD='f6bfbf3c185f705484aa106405f813209146c766';BASE='e000d66dd26ab053e9b17ce7bf8d3c873c3dde99'
def sha(b):return hashlib.sha256(b).hexdigest()
def canon(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def git(*args):return subprocess.check_output(['git','-C',str(W),*args])
def load(p):return json.loads(p.read_bytes())
def save(n,x):
 with(O/n).open('x')as f:json.dump(x,f,ensure_ascii=False,indent=2);f.write('\n')
def obj(b):
 h=sha(b);p=O/'objects'/h;p.parent.mkdir(exist_ok=True)
 if not p.exists():p.write_bytes(b)
 else:assert p.read_bytes()==b
 return {'path':str(p.relative_to(O)),'sha256':h,'bytes':len(b)}
assert git('rev-parse','HEAD').decode().strip()==HEAD
m=load(F/'MANIFEST.json');assert sha((F/'MANIFEST.json').read_bytes())=='7af1cc70fb22e4c96d5008449337a6abaacba18be6afccd71008c6ca7ea7a414'
for f in m['files']:assert sha((F/f['path']).read_bytes())==f['sha256'],f['path']
ledger=load(F/'provenance/entry-provenance-ledger-v1.json');assert sha((F/'provenance/entry-provenance-ledger-v1.json').read_bytes())=='98bfa525356aa223a08fcd2be11d9dc7476231aa6cd9efa4db1f85b2e66109e2'
flags=[r for r in ledger['rows']if r['worker']==3];assert len(flags)==49
core={k:load(P/(k+'.json'))[k]for k in ['proposals','decisions','evidence']};proposals={r['proposal_id']:r for r in core['proposals']};decisions={r['case_id']:r for r in core['decisions']};evidence={r['evidence_id']:r for r in core['evidence']}
for k in core:assert git('show',HEAD+':'+str((P/(k+'.json')).relative_to(W)))==(P/(k+'.json')).read_bytes()
rows=[];proposal_audit=[];fmap={r['proposal_id']:r for r in flags};assert len(fmap)==49
for p in core['proposals']:
 b=git('show',HEAD+':'+str((A/p['after_capture']['path']).relative_to(W)));assert sha(b)==p['after_capture']['sha256'];current=yaml.safe_load(b);before_b=None;before=None
 if p['before_sha256']is not None:
  before_b=git('show',BASE+':'+p['owner_path']);assert sha(before_b)==p['before_sha256'];before=yaml.safe_load(before_b)
 else:
  assert not(W/p['owner_path']).exists(),p['owner_path']
 cur_ev=current.get('ontology_mapping',{}).get('evidence',[]);old_ev=(before or{}).get('ontology_mapping',{}).get('evidence',[])
 counts=collections.Counter(canon(x)for x in old_ev);added=[];inherited=[]
 for i,v in enumerate(cur_ev):
  k=canon(v)
  if counts[k]:counts[k]-=1;inherited.append(i)
  else:added.append(i)
 added_manual=[i for i in added if cur_ev[i].get('evidence_type')=='MANUAL_CURATION'];all_manual=[i for i,v in enumerate(cur_ev)if v.get('evidence_type')=='MANUAL_CURATION']
 proposal_audit.append({'proposal_id':p['proposal_id'],'kind':p['kind'],'owner_path':p['owner_path'],'payload_sha256':sha(b),'before_sha256':p['before_sha256'],'mapping_evidence_count':len(cur_ev),'new_manual_indices':added_manual,'inherited_mapping_indices':inherited,'all_manual_indices':all_manual})
 if p['proposal_id']not in fmap:assert not added_manual,p['proposal_id'];continue
 r=fmap[p['proposal_id']];assert p['kind']==r['proposal_kind']and p['owner_path']==r['owner_path'];assert sha(b)==r['payload_sha256'];assert before_b is None and r['baseline_sha256']is None or sha(before_b)==r['baseline_sha256'];assert added_manual==[0];assert r['field']=='ontology_mapping.evidence[0]';assert cur_ev[0]==r['full_value'];assert r['suggested_native_type']=='LLM_SUGGESTION'and r['classification']=='new_agent_record';assert not r['baseline_full_value_match_indices'];assert all(h in current.get('curation_history',[])for h in r['author_evidence']['added_curation_history'])
 parent={k:v for k,v in current['ontology_mapping'].items()if k!='evidence'};priorparent={k:v for k,v in(before or{}).get('ontology_mapping',{}).items()if k!='evidence'}
 for ref in r['author_evidence']['linked_review_reports']:
  assert sha(Path(ref['path']).read_bytes())==ref['sha256'],ref['path']
 row={'audit_row_id':r['audit_row_id'],'origin_frozen_head':r['source_head'],'current_published_head':HEAD,'proposal_id':p['proposal_id'],'proposal_kind':p['kind'],'owner_path':p['owner_path'],'case_ids':p['case_ids'],'case_input_sha256':{k:decisions[k]['case_input_sha256']for k in p['case_ids']},'payload':obj(b),'published_payload_path':str((A/p['after_capture']['path']).relative_to(W)),'authentic_before':obj(before_b)if before_b is not None else None,'authentic_before_path':p['owner_path']if before_b is not None else None,'parent_context':parent,'parent_context_sha256':sha(canon(parent)),'before_parent_context':priorparent,'current_identifier':current['identifier'],'current_mapping_status':current['mapping_status'],'field':'ontology_mapping.evidence[0].evidence_type','complete_mapping_evidence_object':cur_ev[0],'complete_object_canonical_sha256':sha(canon(cur_ev[0])),'change':{'from':'MANUAL_CURATION','to':'LLM_SUGGESTION'},'classification':r['classification'],'type_basis':r['claim_specific_type_basis'],'author_evidence':r['author_evidence'],'original_full_provenance_row':obj(canon(r)),'history_prefix_sha256':sha(canon(current.get('curation_history',[]))),'required_preservation':'Only this enum plus truthful appended history; preserve complete current notes/source/parent/other evidence and scientific fields. No source-case or role/export approval.'}
 rows.append(row)
assert len(rows)==49;assert 'b-proposal-cm0149-form'not in proposals and 'b-proposal-cm0149-form'not in fmap
new=proposals['w03-oxoid-cm0149-product-1224-v1'];nb=git('show',HEAD+':'+str((A/new['after_capture']['path']).relative_to(W)));nx=yaml.safe_load(nb);assert[len(nx['ontology_mapping']['evidence']),{v['evidence_type']for v in nx['ontology_mapping']['evidence']}]==[2,{'LLM_SUGGESTION'}]
status=git('status','--porcelain=v1').decode();assert not status;assert git('rev-parse','HEAD').decode().strip()==HEAD
save('repair-allowlist.json',{'schema_version':1,'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'49 claim-specific MappingEvidence provenance fields on unchanged retained W03 payloads; no scientific reapproval','head':HEAD,'baseline':BASE,'rows':rows,'new_oxoid_excluded':{'proposal_id':new['proposal_id'],'payload_sha256':sha(nb),'already_llm_suggestion_entries':2},'retired_origin_excluded':'b-proposal-cm0149-form','authority':'https://github.com/CultureBotAI/MediaIngredientMech/issues/1226','automatic_typing_for_other_objects':False})
save('all74-proposal-audit.json',{'head':HEAD,'proposals':proposal_audit,'new_manual_entries':sum(len(x['new_manual_indices'])for x in proposal_audit),'inherited_manual_entries':sum(len(set(x['all_manual_indices'])&set(x['inherited_mapping_indices']))for x in proposal_audit),'counts':dict(collections.Counter(r['proposal_kind']for r in rows)),'full_audit_members_rehashed':len(m['files']),'full_audit_manifest_sha256':sha((F/'MANIFEST.json').read_bytes()),'full_audit_ledger_sha256':sha((F/'provenance/entry-provenance-ledger-v1.json').read_bytes()),'clean_worktree':not status})
for n in ['HANDOFF.md','MANIFEST.json']:(O/('source-audit-'+n)).write_bytes((F/n).read_bytes())
for n in ['HANDOFF.json','decisions.json','proposals.json','evidence.json']:(O/('current-'+n)).write_bytes((P/n).read_bytes())
save('frozen-w03-full-provenance-rows.json',{'rows':flags})
print(json.dumps({'rows':len(rows),'proposals':len(proposal_audit),'new_manual':sum(len(x['new_manual_indices'])for x in proposal_audit),'new_oxoid_excluded':2,'counts':dict(collections.Counter(r['proposal_kind']for r in rows)),'full_audit_members':len(m['files'])}))
