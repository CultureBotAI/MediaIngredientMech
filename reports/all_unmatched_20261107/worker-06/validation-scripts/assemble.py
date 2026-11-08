from pathlib import Path
import json,hashlib,datetime,copy
R=Path('reports/all_unmatched_20261107/worker-06');Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5');S=Q/'shards/shard-06.json';cases=json.loads(S.read_text())['cases']
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def cap(p):return {'root':'artifact','path':str(p.relative_to(R)),'sha256':sha(p)}
D=[];E=[];P=[]
for g in ['research-a','research-b','research-c','research-root']:
 D+=json.loads((R/g/'decisions.json').read_text())['decisions'];E+=json.loads((R/g/'evidence.json').read_text())['evidence'];P+=json.loads((R/g/'proposals.json').read_text())['proposals']
ds={d['case_id']:d for d in D};ps={p['proposal_id']:p for p in P};es={e['evidence_id']:e for e in E};assert len(es)==len(E)
# One reviewed combined yeast owner, authored B from exact frozen baseline.
if 'C-P-YEAST-EXTRACT' in ps:
 old=ps.pop('C-P-YEAST-EXTRACT')
 for d in D:d['proposal_ids']=['B-P-Yeast_Extract' if x=='C-P-YEAST-EXTRACT' else x for x in d['proposal_ids']]
 for cid in old['case_ids']:
  if cid not in ps['B-P-Yeast_Extract']['case_ids']:ps['B-P-Yeast_Extract']['case_ids'].append(cid)
 for x in old['evidence_ids']:
  if x not in ps['B-P-Yeast_Extract']['evidence_ids']:ps['B-P-Yeast_Extract']['evidence_ids'].append(x)
links={
 'A-P-CALCIUM-D':[75,145,166,174], 'A-P-D-GLUCOSE':[124], 'A-P-LANTHANUM-HEPTAHYDRATE':[170], 'A-P-MERCK108339':[183],
 'C-P-JCM187':[152], 'C-P-JCM151':[22,182], 'C-P-JCM197':[21,76,177], 'C-P-JCM284':[65,85,165],
 'C-P-NZAMINE-A':[71], 'A-P-ATCC-MDTMS':[81], 'B-P-Yeast_Extract':[107,144], 'B-P-NBRC1257-1321':[134], 'R-P-YEAST-CELL-PASTE':[9],
 'A-P-JCM1136-548-GLUCOSE-1M':[114,115], 'A-P-RYEGRASS-MATERIAL-REVIEW':[169], 'A-P-JCM576-SL12':[180], 'B-P-PROTEOSE-TC5577':[157]
}
for pid,indices in links.items():
 if pid not in ps:continue
 p=ps[pid]
 for i in indices:
  d=ds[cases[i]['case_id']]
  if pid not in d['proposal_ids']:d['proposal_ids'].append(pid)
  d['no_change_reason']=None
  if d['case_id'] not in p['case_ids']:p['case_ids'].append(d['case_id'])
  # Exact sharedpayload applicability derives from independently reviewed source judgments;
  # do not add external owner or erase any existing hold.
  d['applicability']+=' Shared isolated proposal '+pid+' applies only to the substance/formulation established by this case; it does not approve source-case, owner or export release.'
  for e in d['evidence_ids']:
   if e not in p['evidence_ids']:p['evidence_ids'].append(e)
# Independently requested integration corrections preserve uncertainty where source access failed.
for i in [35,183]:
 d=ds[cases[i]['case_id']]
 d['missing_requirement']='Current Merck108339 typical formulation is verified. Historical lot/formulation concordance remains unverified; keep generic Sabouraud family owner separate and require version-specific source review before release.'
 if i==183:
  d['evidence_ids'].append('A-E-MERCK108339')
  d['reasoning']='The raw source specifies Merck108339,2%glucose broth in DSMZ1429. Official supplier composition now verifies the catalog-qualified dehydrated broth, with5g/L meatpeptone,5g/L caseinpeptone and20g/L D(+)glucose at30g product/L. This supports the separate Merckproduct proposal; the receiving recipe adds agar separately. Current typicalcomposition does not establish historicallot invariance or genericSabouraudfamily identity.'
ds[cases[124]['case_id']]['missing_requirement']='Recover a version-matched JCM490/TOGO491 primary recipe; current primary retrieval was empty or failed. The frozen D--glucose spelling and existing D-glucose term support only the narrow spelling proposal, not source-release approval.'
ds[cases[22]['case_id']]['missing_requirement']='Integrate the single independently reviewed C-P-JCM151 source-defined local registry proposal using the original unmapped-owner before hash; retain exact formulation, migration obligations and separate source/owner/export review.'
ds[cases[165]['case_id']]['reasoning']='MediaDive1982 retains the explicit JCM284 vitamin-solution reference and star attribute. JCM284 defines the specific vitamin stock, distinct from complete growth media and other trace-vitamin recipes. The proposal replaces the baseline unmapped placeholder with a source-defined formulation registry and literal component quantities; no individual component ontology identity or release approval follows.'
ds[cases[182]['case_id']]['reasoning']='The exact truncated raw label references trace minerals in JCM151 and appears as10ml in JCM744. JCM151 defines a multicomponent stock. The shared proposal replaces the baseline unmapped placeholder with a formulation registry and source-transcribed components while preserving exact original before hashes, raw reference spelling and source quantities; no source or export approval follows.'
ds[cases[9]['case_id']]['missing_requirement']='The washed wet-cell preparation is now represented in the shared reviewed payload. Taxon/strain and equivalence to other yeast preparations remain unestablished; retain the existing unmapped material and separate owner/source review.'
ds[cases[21]['case_id']]['missing_requirement']='The JCM197 stock backlink and independent review are complete. Resolve unspecified child forms, including calcium-pantothenate stereochemistry, before exact child grounding; do not conflate the separately phosphate-buffered JCM1353 parent.'
ds[cases[71]['case_id']]['missing_requirement']='The exact Sheffield typeA raw alias is included in the reviewed combined payload. Manufacturer evidence is still required for any equivalence to SigmaC7290, C0626, EZMix or other grades; inherited owner and release obligations remain separate.'
for i in [114,115]:
 ds[cases[i]['case_id']]['missing_requirement']='The combined 1M stock payload and independent delta review are complete. Starting glucose form and explicit solvent specification remain unstated; preserve the distinct source preparation instructions, including N2 storage only where the source states it.'
# Resolve author integration markers to actual proposal/backlinks.
for p in ps.values():
 for cid in p['case_ids']:
  d=ds[cid]
  if p['proposal_id'] not in d['proposal_ids']:d['proposal_ids'].append(p['proposal_id']);d['no_change_reason']=None
issue=(R/'shared/issue-jcm1357-created.txt').read_text().strip();ds[cases[13]['case_id']]['issue_refs']=list(dict.fromkeys(ds[cases[13]['case_id']]['issue_refs']+[issue]))
issue=(R/'shared/issue-hipolypepton-created.txt').read_text().strip();ds[cases[43]['case_id']]['issue_refs']=list(dict.fromkeys(ds[cases[43]['case_id']]['issue_refs']+[issue]))
# One mixed-name case has only three occurrence-specific links to JCM197; its RM
# stock occurrence is explicitly excluded from this shared formulation.
d=ds[cases[57]['case_id']];p=ps['C-P-JCM197'];subset=d['integration_occurrence_ids']
assert len(subset)==3 and set(subset)<set(d['occurrence_ids'])
d['proposal_ids'].append('C-P-JCM197');p['case_ids'].append(d['case_id'])
p.setdefault('occurrence_scopes_by_case',{})[d['case_id']]={'included_occurrence_ids':subset,'excluded_occurrence_ids':[x for x in d['occurrence_ids'] if x not in subset],'reason':'Only explicitly numbered JCM197 stock occurrences; TOGO3181 RM stock belongs exclusively to B-P-TOGO3181-RM-VITAMINS.'}
d['applicability']+=' Shared C-P-JCM197 applies ONLY to the three integration_occurrence_ids, excluding the distinct RM stock occurrence. No global Trace vitamins alias.'
for eid in d['evidence_ids']:
 if eid not in p['evidence_ids']:p['evidence_ids'].append(eid)
# Independent files remain immutable. Aggregated decision review evidence points to actual scope.
reviews=[('IR-A',0,47,'independent/root-review-a/final-review-v2.json'),('IR-B',47,94,'research-a/review-b/review-b-v6.json'),('IR-C',94,145,'research-b/review-c/review-final.json'),('IR-R',145,188,'research-c/review-root/completion-addendum.json')]
for eid,lo,hi,path in reviews:
 p=R/path
 if not p.exists():continue
 obj=json.loads(p.read_text());complete=obj.get('status') in ['complete','complete_with_limitations','complete_with_coordinator_integration_obligations'] or obj.get('overall_status')=='complete_with_limitations' or obj.get('verdict') in ['accepted','pass_with_limitations']
 E.append({'evidence_id':eid,'kind':'independent_review','capture':cap(p),'url':None,'locator':'All per-case assessments, input/payload hashes and findings in the explicitly named independent reviewer scope','supports_or_contradicts':'Independent skeptical assessment of assigned source decisions and exact proposed bytes; no publication or source-claim release approval.'})
 for i in range(lo,hi):ds[cases[i]['case_id']]['independent_review']={'status':'complete' if complete else 'findings_open','evidence_ids':[eid]}
addenda=[
 ('IR-C-NZAMINE',[71,102],'research-b/review-c/nzamine-delta-review.json'),
 ('IR-R-YEAST',[9,168],'research-c/review-root/yeast-paste-addendum.json'),
 ('IR-COMBINED-OWNERS',[107,134,144],'independent/combined-owner-review-v2.json'),
]
for eid,indices,path in addenda:
 p=R/path
 E.append({'evidence_id':eid,'kind':'independent_review','capture':cap(p),'url':None,'locator':'Exact combined owner or final payload delta, independently checked after initial batch review','supports_or_contradicts':'Binds final proposal bytes and cross-case applicability without releasing source cases, owners or exports.'})
 for i in indices:ds[cases[i]['case_id']]['independent_review']['evidence_ids'].append(eid)
# Case accounting is unchanged; keep full canonical objects in the frozen queue, not duplicated.
D=[ds[c['case_id']] for c in cases];P=list(ps.values());
for d in D:
 assert all(pid in ps for pid in d['proposal_ids']),(d['case_id'],d['proposal_ids'])
 for eid in d['evidence_ids']:assert eid in es,(d['case_id'],eid)
for p in P:
 for eid in p['evidence_ids']:assert eid in es,(p['proposal_id'],eid)
for f,obj in [('decisions.json',{'schema_version':1,'worker_slot':6,'shard_sha256':sha(S),'phase':'shard','decisions':D}),('evidence.json',{'schema_version':1,'evidence':E}),('proposals.json',{'schema_version':1,'proposals':P})]:(R/f).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print('Assembled',len(D),'cases',len(E),'evidence',len(P),'proposals; independent',sum(d['independent_review']['status']=='complete' for d in D))
