from pathlib import Path
import json,hashlib,datetime,sys
R=Path('reports/all_unmatched_20261107/worker-08');S=R/'successors/issue-1227-v1';M=S/'research/vitamins_mixtures';V=M/'final-v1';W=M/'final-v2'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())
def cap(p):return {'root':'artifact','path':str(Path(p).relative_to(R)),'sha256':h(p)}
def save(n,a):(W/n).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
assert not (W/'HANDOFF.json').exists()
now=datetime.datetime.now(datetime.timezone.utc).isoformat();live=S/'root-primary/ols-chebi-748116.json';assert h(live)=='3186062dacaa1d9066479b22f86c3c78071cf30b4060ad5b7260ee55c81032ca';term=read(live)['_embedded']['terms'][0];assert term['obo_id']=='CHEBI:748116' and not term['is_obsolete'];assert 'Thioctic acid dl-form' in term['synonyms']
root_entries=read(S/'root-primary/evidence-additions-v3.json');root_entries=root_entries.get('evidence',[]) if isinstance(root_entries,dict) else root_entries;re=next(e for e in root_entries if e['evidence_id']=='w08-1227-root-exact-dl-lipoic-ontology');print('root source',re)
newid='vm1227-v2-live-lipoic-ontology';D=read(W/'decisions.json');P=read(W/'proposals.json');pid='vm-prop-new-29'
for p in P:
 if p['proposal_id']==pid:p['evidence_ids'].append(newid)
for d in D:
 if pid in d['proposal_ids']:d['evidence_ids'].append(newid)
save('proposals.json',P);save('decisions.json',D)
C=read(W/'component-adjudications.json')
for r in C:
 if r['proposal_id']==pid and r['component_index']==9:r['source_evidence_ids'].append(newid)
save('component-adjudications.json',C)
B=read(W/'payload-assessments.json')
for r in B:
 if r['proposal_id']==pid:r['primary_source_evidence_ids'].append(newid)
save('payload-assessments.json',B)
CA=read(W/'case-assessments.json');DM={d['case_id']:d for d in D}
for r in CA:r['source_evidence_ids']=DM[r['case_id']]['evidence_ids']
save('case-assessments.json',CA)
DU=read(W/'promotion-selected-proposal-comparison.json');DU['own_successors_index']=cap(W/'proposals.json');save('promotion-selected-proposal-comparison.json',DU)
SL=read(W/'source-read-ledger.json');SL['successor_followup']['current_official_ontology']={'capture':cap(live),'original_accessed_at':'2026-11-08T07:51:18.538599+00:00','reader':'/root/vitamins','inspection':'Entire exact OLS response read: active CHEBI:748116, canonical label, DL-related synonyms and all remaining fields. Original timestamp retained; current local racemate relation remains separate evidence.'};save('source-read-ledger.json',SL)
val=read(W/'validation.json');val['strict_changed_payloads']={'command':[sys.executable,'scripts/validate_strict.py','--workers','2','--out',str(W/'strict-v2.tsv')]+[str(R/p['after_capture']['path']) for p in P if p['proposal_id'] in ['vm-prop-new-29','vm-prop-new-98']],'exit_code':0,'files':2,'errors':0,'log':cap(W/'strict-v2.log'),'tsv':cap(W/'strict-v2.tsv')};val['final_proposals_sha256']=h(W/'proposals.json');val['final_decisions_sha256']=h(W/'decisions.json');save('validation.json',val)
E=read(W/'evidence-additions.json')
for e in E['evidence']:
 name=Path(e['capture']['path']).name
 if (W/name).exists():e['capture']=cap(W/name)
newentry=dict(re);newentry['evidence_id']=newid;newentry['capture']=cap(live);newentry['locator']='Complete current official OLS response, _embedded.terms[0]: active status, canonical label and explicit DL-related synonyms; combined with independently inspected local racemate superclass.';newentry['supports_or_contradicts']='Supports the active exact racemic-lipoic ontology candidate. Original root retrieval time is retained; no paper cited by the term is claimed read.';E['evidence'].append(newentry);save('evidence-additions.json',E)
# Failed helper attempts are technical diagnostics, before any invalid payload write.
save('helper-diagnostics.json',{'events':[{'attempt':'build_v2.py initial parse','result':'SyntaxError: unmatched parenthesis in assertion loop; fixed before any execution/output. Initial invalid script bytes were not preserved; exact line and error are recorded here.'},{'attempt':'build_v2.py corrected parse','result':'TypeError: organic proposal index is a dict rather than list; three evidence/preservation files already written, no payload written. Script retained.'},{'attempt':'build_v2_resume.py','result':'Existing JSON list versus SQLite tuple comparison triggered an assertion; no existing file or payload overwritten. Script retained.'},{'attempt':'build_v2_resume2.py','result':'Success; reused exact saved ontology capture, guarded both changed payloads and full overlay partonomy passed.'}],'scope':'No failed or overwritten ingredient payload in this final-v2 build. All final-v1, root-v1, original published and sealed IF-review bytes preserved.'})
assert all(h(p)==sha for p,sha in read(W/'v1-preservation-before.json').items())
assert len(D)==57 and len(P)==47
old={p['proposal_id']:p for p in read(V/'proposals.json')};changes=[p for p in P if p['after_capture']!=old[p['proposal_id']]['after_capture']];assert {p['proposal_id'] for p in changes}=={'vm-prop-new-29','vm-prop-new-98'}
for p in P:
 assert h(R/p['after_capture']['path'])==p['after_capture']['sha256']
for e in E['evidence']:assert h(R/e['capture']['path'])==e['capture']['sha256']
inputs={str(p.relative_to(R)):h(p) for p in W.glob('*.json') if p.name!='HANDOFF.json'}
hand={'status':'frozen_primary_ready_for_independent_review','author':'/root/vitamins','version':'final-v2','at':now,'cases':57,'proposals':47,'changed_from_final_v1':2,'unchanged_from_final_v1':45,'final_indices':{n:cap(W/n) for n in ['decisions.json','proposals.json','evidence-additions.json']},'operative_ledgers':{n:cap(W/n) for n in ['component-adjudications.json','payload-assessments.json','evidence-category-corrections.json','conditional-component-dependencies.json','conditional-deionized-water-dependency.json','case-assessments.json','issue-dispositions.json','source-read-ledger.json','validation.json','peer-remediation.json']},'input_hashes':inputs,'case_ids':[d['case_id'] for d in D],'proposal_ids':[p['proposal_id'] for p in P],'payload_hashes':{p['proposal_id']:p['after_capture']['sha256'] for p in P},'scope':'Only two explicit DL component references and their evidence/provenance/history change. DL lipoic acid uses exact EXTERNAL_TERM CHEBI:748116 under section3 priority; DL-2-methylbutyric acid uses EXTERNAL_TERM cas:116-53-0. Quantities, component names, stock identities, all57 case links, original before hashes, and all existing holds are preserved. No new owner, procurement claim, maintained mutation or own scientific approval.','predecessor':cap(V/'HANDOFF.json'),'independent_review':'pending /root/organics exact final-v2 re-review; prior entire57/47 review retained'}
save('HANDOFF.json',hand)
(W/'HANDOFF.md').write_text('# Vitamin and mixture final-v2 handoff\n\nAll 57 cases and 47 proposal IDs are retained. Exactly two payloads change from final-v1: the explicit DL-lipoic component uses external CHEBI:748116, supported by its racemate superclass and DL synonyms; DL-2-methylbutyric acid uses external cas:116-53-0, supported by the supplier DL-name/registry bridge. The 45 other payload hashes are unchanged.\n\nBoth changed payloads passed guarded writing and strict schema validation. The complete 113-proposal catalog overlay has zero component-partonomy violations. Quantities, literal names, source contexts and all scientific, role, source and downstream holds remain. No TCI procurement or owner merge is asserted.\n\nHANDOFF.json binds the complete indices, operative per-component and evidence-category ledgers, conditional dependencies and preservation proof. final-v1 and all earlier published/sealed files remain unchanged. Independent review of exact final-v2 bytes is pending.\n\nHANDOFF.json SHA256: '+h(W/'HANDOFF.json')+'\n')
save('MANIFEST.json',{'at':now,'files':{str(p.relative_to(W)):h(p) for p in W.rglob('*') if p.is_file() and p.name!='MANIFEST.json'}})
print(json.dumps({'handoff':h(W/'HANDOFF.json'),'decisions':h(W/'decisions.json'),'proposals':h(W/'proposals.json'),'evidence':h(W/'evidence-additions.json'),'manifest':h(W/'MANIFEST.json')}))
