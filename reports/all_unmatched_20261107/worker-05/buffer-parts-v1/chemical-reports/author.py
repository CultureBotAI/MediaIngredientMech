from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,copy,shutil,yaml
W=Path.cwd();B=W/'reports/all_unmatched_20261107/worker-05';S=W/'.temp/w05-buffer-parts-v1';O=S/'chemical-reports';C=W.parents[2];at=datetime.now(timezone.utc).isoformat()
j=lambda p:json.loads(p.read_text());sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();oh=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def put(n,x):
 p=O/n;assert not p.exists();p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
shutil.copytree(C/'preflight/w05-review-followups-triage-v1',O/'inputs/triage')
base=B/'tellurium-polypeptone-v1/core';ps=j(base/'proposals.json')['proposals'];ds=j(base/'decisions.json')['decisions'];es=j(base/'evidence.json')['evidence'];pi={p['proposal_id']:p for p in ps};di={d['case_id']:d for d in ds}
ids=[['R1193-P-bottom-628','R1193-P-bottom-629'],['R1193-P-mkp'],['FINAL-CHEM-P-thiamine-hcl-monohydrate'],['CHEM-C1193-ethanol95-dsmz_78'],['CHEM-C1193-Tris-HCl-salt']]
texts=['Both bottom preparations contain washed FeS preparation and agarose. JCM629 explicitly substitutes artificial saltwater for the Modified Wolfe mineral solution used by628; there is no zero-valent-iron substitution.','MKP is the MediaDive/DSMZ1895 solution6635 multicomponent medium base; HS-RFB solution6636 separately adds human serum and albumin. It is not a JCM salt preparation.','Six direct NBRC recipes positively name one-water Thiamine-HCl. The existing shared source-defined monohydrate proposal is retained unchanged; exact molecular formula, CAS, chloride stoichiometry and supplier remain unverified. Missing molecular grounding does not block this bounded material identity.','The exact applicable occurrence set has twelve members: eleven flattened DSMZ routes plus the nested DSMZ212a route. This report count correction establishes neither equal nor distinct supplied formulations, and does not establish95%v/v or solvent balance.','The selected exact CAS1185-53-1 salt stores NARROW_MATCH to CHEBI:9754. Native semantics emit skos:broadMatch plus CAS identity and B1 compound identity; the earlier review incorrectly named the enum BROAD_MATCH. This report verification changes neither payload nor source identity.']
reports=[B/'final-correction-v1/remediation/chemical-report-v3/primary-case-conclusions-v3.json',B/'final-correction-v1/chemical-supplement-v1/primary-case-conclusions-v2.json',B/'final-correction-v1/reviews/chemicals/main-review-v2.json']
reportbind=[dict(path=str(p.relative_to(B)),sha256=sha(p),author=j(p).get('author',j(p).get('reviewer')),at=j(p).get('authored_at',j(p).get('completed_at'))) for p in reports]
newD={};rows=[];ev=[];newP=[]
for n,(pids,text) in enumerate(zip(ids,texts),1):
 finding=j(O/'inputs/triage'/f'finding-{n:03d}-initial.json');selected=[pi[x] for x in pids];cids=list(dict.fromkeys(c for p in selected for c in p['case_ids']));eid=f'W05-REMAINING-CHEM-REPORT-{n:03d}'
 for p in selected:
  f=B/p['after_capture']['path'];assert sha(f)==p['after_capture']['sha256'];newP.append(copy.deepcopy(p))
  if n==3:assert len(p['applies_to_occurrence_ids'])==6
  if n==4:assert p['applies_to_occurrence_ids']==finding['reproduction']['applicable_occurrence_ids'] and len(p['applies_to_occurrence_ids'])==12
  if n==5:assert yaml.safe_load(f.read_text())['ontology_mapping']['mapping_quality']=='NARROW_MATCH'
 for cid in cids:
  d=newD.setdefault(cid,copy.deepcopy(di[cid]));d.setdefault('chemical_report_verification',[]).append(dict(author='/root',at=at,finding_id=finding['finding_id'],status='already_correct_in_published_predecessor_retained',assessment=text,unchanged_payloads=[p['after_capture'] for p in selected],source_or_export_approval=False));d['evidence_ids']=list(dict.fromkeys(d['evidence_ids']+[eid]))
  if n==3:assert d['disposition']=='new_distinct_ingredient_proposal' and not d.get('no_change_reason')
 snippets=[]
 for rp in reports:
  x=j(rp)
  for key in ['case_reviews','payload_reviews','finding_dispositions']:
   for r in x.get(key,[]):
    if (key=='case_reviews' and r.get('case_id') in cids) or (key=='payload_reviews' and r.get('proposal_id') in pids) or (key=='finding_dispositions' and r.get('finding_id')==finding['finding_id']):
     snippets.append(dict(report=str(rp.relative_to(B)),report_sha256=sha(rp),field=key,object_sha256=oh(r),assessment=r.get('assessment'),case_id=r.get('case_id'),proposal_id=r.get('proposal_id'),finding_id=r.get('finding_id')))
 rows.append(dict(finding_id=finding['finding_id'],original_finding=finding,original_finding_sha256=sha(O/'inputs/triage'/f'finding-{n:03d}-initial.json'),status='verified_already_correct_no_duplicate_payload_edit',assessment=text,case_ids=cids,selected_proposals=selected,corrected_historical_report_bindings=snippets))
 ev.append(dict(evidence_id=eid,kind='source_snapshot',capture=dict(root='artifact',path='buffer-parts-v1/chemical-reports/finding-verification-v1.json',sha256='PENDING'),url='https://github.com/CultureBotAI/MediaIngredientMech/issues/1193#issuecomment-6719161955',accessed_at=at,locator=f'rows finding_id {finding["finding_id"]}',supports_or_contradicts=text,case_ids=cids))
# Complete ignored-inclusive maintained YAML and exact currently selected proposal search; no new duplicate is created.
ownerhits=[];count=0
for f in sorted((W/'data/ingredients').rglob('*.yaml')):
 count+=1;r=yaml.safe_load(f.read_text());t=json.dumps([r.get('identifier'),r.get('preferred_term'),r.get('synonyms')],ensure_ascii=False).lower()
 if 'thiamin' in t:ownerhits.append(dict(path=str(f.relative_to(W)),sha256=sha(f),identifier=r.get('identifier'),preferred_term=r.get('preferred_term'),synonyms=r.get('synonyms')))
proposalhits=[]
for p in ps:
 r=yaml.safe_load((B/p['after_capture']['path']).read_text())
 if 'thiamin' in json.dumps([r.get('identifier'),r.get('preferred_term'),r.get('synonyms')]).lower():proposalhits.append(dict(proposal_id=p['proposal_id'],capture=p['after_capture'],identifier=r.get('identifier'),preferred_term=r.get('preferred_term')))
assert sum(x['identifier']=='kgmicrobe.compound:thiamine_hcl_monohydrate' for x in proposalhits)==1
put('monohydrate-current-owner-check.json',dict(at=at,method='Path.rglob, includes ignored/hidden ingredient paths; all selected proposal YAML parsed. No repository-wide absence claim.',maintained_records_scanned=count,selected_proposals_scanned=len(ps),maintained_hits=ownerhits,proposal_hits=proposalhits,decision='Reuse one existing selected bounded monohydrate proposal; no new owner proposal or molecular claim.'))
comment=j(S/'issues/comment6719161955.json');chronology=dict(original_finding_reports=[dict(finding_id=x['original_finding']['finding_id'],recorded_at=x['original_finding'].get('recorded_at',x['original_finding'].get('at'))) for x in rows],formal_filed_comment=comment,limit='Historical internal report/candidate corrections predate the formal filed comment. Preserve real authors and recorded times; do not retrospectively claim the formal GitHub filing preceded private corrections. All corrected objects were already published in5156d92 before this verification. Original reports remain authoritative historical artifacts, not overwritten.')
put('finding-verification-v1.json',dict(author='/root',at=at,base_head='0bac12cabfd1f67f212631d8eef9aa46379f6b41',rows=rows,context_finding_006=j(O/'inputs/triage/finding-006-initial.json'),context_006_status='Both current dispositions verified new_distinct_ingredient_proposal; inherited native outcome correction retained.',chronology=chronology,reused_report_authorship=reportbind,scope='New report verification only: unchanged six full payloads, original evidence/acquisition timestamps/history retained, all source/owner/role/export and family holds retained.'))
for e in ev:e['capture']['sha256']=sha(O/'finding-verification-v1.json')
put('decisions.json',dict(decisions=list(newD.values())));put('proposals.json',dict(proposals=newP));put('evidence.json',dict(evidence=ev))
put('primary-read-ledger-v1.json',dict(author='/root',at=at,full_primary_sources=[dict(path=str(p.relative_to(O)),sha256=sha(p)) for p in sorted((O/'inputs/triage').glob('*')) if p.suffix=='.html' or p.name.startswith('ROOT-')],full_payloads=[p['after_capture'] for p in newP],report_scope='Five filed chemical-report facts and context006; not a fresh review of all inherited chemical science.',reports=reportbind,exact_current_cases=[dict(case_id=d['case_id'],object_sha256=oh(d)) for d in newD.values()]))
print(json.dumps(dict(cases=len(newD),unchanged_payloads=len(newP),evidence=len(ev),findings=len(rows),all_payloads_preserved=True)))
