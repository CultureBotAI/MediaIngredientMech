import json, hashlib
from pathlib import Path
from datetime import datetime, timezone
R=Path.cwd();S=R/'.temp/w05-buffer-parts-v1';B=R/'reports/all_unmatched_20261107/worker-05';Q=S/'review'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def oh(v):return hashlib.sha256(json.dumps(v,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
def j(p):return json.loads(Path(p).read_text())
def bind(p):return {'path':str(Path(p).relative_to(R)),'sha256':h(p)}
def save(n,v):
 p=Q/n;assert not p.exists();p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n');print(n,h(p))
def cap(c):
 p=S/c['path'].split('buffer-parts-v1/',1)[1] if c['path'].startswith('buffer-parts-v1/') else B/c['path'];assert h(p)==c['sha256'];return p
now=datetime.now(timezone.utc).isoformat()
manifest=j(S/'parents/MANIFEST.json');checks=[]
for x in manifest['members']:
 p=S/'parents'/x['path'];assert h(p)==x['sha256'];checks.append({'path':x['path'],'sha256':h(p),'verified':True})
selected=j(S/'parents/selected-files.json')
for x in selected['files']:assert h(S/'parents'/x['path'])==x['sha256']
ev0=j(S/'parents/final/evidence.json')['evidence'];ev=j(S/'parents/final/evidence-v2.json')['evidence'];ed=[]
for a,b in zip(ev0,ev):
 if a!=b:ed.append({'id':a['evidence_id'],'before':a['original_capture_attribution'],'after':b['original_capture_attribution']})
assert len(ed)==1 and ed[0]['id']=='W05-PARENTS-THERMO'
assert h(R/ed[0]['after']['authentic_author_source'])==ed[0]['after']['authentic_author_source_sha256']
all_ev=ev+j(S/'parents/final/tombstone-evidence-v2.json')['evidence']
echecks=[{'evidence_id':e['evidence_id'],'capture':e['capture'],'capture_verified':h(cap(e['capture']))==e['capture']['sha256'],'kind':e['kind']} for e in all_ev]
save('parents-final-integrity-v1.json',{'reviewer':'/root/final_skeptical','at':now,'manifest':bind(S/'parents/MANIFEST.json'),'members':checks,'selected_index':bind(S/'parents/selected-files.json'),'evidence_objects':echecks,'attribution_erratum':ed,'limitation':'Integrity and provenance checks do not establish scientific applicability; separate assessments below.'})
ps=j(S/'parents/final/proposals.json')['proposals']+j(S/'parents/final/tombstone-proposals-v2.json')['proposals']
assess={
'W05-FINAL-MAT-032':'Full MICRO:0000181 definition and its source discussion describe generic enzymatic soy-flour digest, consistent with MediaDive75 and the independent manufacturer definition. This is a supported exact generic identity. The erroneous Hordeum parenthesis, branded/papaic synonyms and numerical product annotations are not imported. The complete final payload preserves five existing alias exclusions, the unresolved peptic-process alias context, old evidence/history, statistics and roles. The separately reviewed rejected Bacto tombstone prevents the inherited shared-ID representative from acquiring an unsupported generic-Soy equivalence. Neither shared-ID source membership nor export admission is established.',
'W05-FINAL-MAT-039':'The two raw peptones observations do not establish feedstock, manufacturer, process or precipitation behavior. Manufacturer generic peptones include partial protein hydrolysates from plant, yeast or animal sources and acid, base or enzyme processing. Direct MeSH Peptones adds acid-or-enzyme and solubility/precipitation specifications; MICRO178 adds mammalian enzymatic/Bacto scope, MICRO174 enzyme scope and MICRO172 plant-or-animal scope. None is entailed for the entire unspecified generic owner. NLM D011492/M0017860 defines partial or extensive protein hydrolysates without those extra material restrictions. Retaining the local identity with NARROW_MATCH to mesh:D011492 is supported. Its therapeutic/nutrient indexing annotation is not a role assertion for this material. The complete payload preserves raw plural provenance, rejected truncated token, all old history/evidence, statistics and role/source holds. Conditional named-part references require separate source-specific review.',
'W05-PARENTS-BACTO-SOYTONE-CONTINUITY':'The authentic rejected Bacto Soytone tombstone previously redirected through a nonunique FOODON identifier. Explicit empty representative is the native unresolved-target mechanism; removal instead invokes legacy identifier fallback. Independent execution confirms the empty value retains the tombstone name and emits no SSSOM rows while avoiding active shared-ID owner credit. A redirect to generic MICRO181 would assert unsupported product equivalence. All original identity/mapping/status/aliases/zero statistics/history/evidence remain unchanged; only the bounded continuity annotation and event are appended. The new unsupported human attribution was removed in exact v2; historical enums and objects remain intact. This does not reconstruct a branded owner or repartition historic source membership.'}
checks0=j(Q/'parents-media-independent-checks-v1.json')
payload=[]
for p in ps:
 cap(p['after_capture'])
 payload.append({'proposal_id':p['proposal_id'],'proposal_object_sha256':oh(p),'after_capture':p['after_capture'],'reviewer':'/root/final_skeptical','assessment':assess[p['proposal_id']],'conclusion':'PASS_BOUNDED_SUCCESSOR_WITH_LIMITATIONS','complete_payload_read':True,'protected_fields':'Original history/evidence, roles, statistics, source forms and raw names checked in complete payloads and independent parsed comparisons. No source/owner/export approval.'})
ds=j(S/'parents/final/decisions.json')['decisions']
cr=[]
for d in ds:
 pid='W05-FINAL-MAT-032' if d['source']['raw_source_label']=='Soy peptone' else 'W05-FINAL-MAT-039'
 cr.append({'case_id':d['case_id'],'selected_decision_object_sha256':oh(d),'assessment':assess[pid],'limitation':'This author fragment precedes root composition with dependency/tombstone deltas; final full composed decision binding is required.'})
matrix=[
 {'candidate':'MICRO:0000181','assessment':'Supported exact generic soy digest; false taxonomy/product aliases and numeric annotations excluded.'},
 {'candidate':'FOODON:03315720','assessment':'Broader vegetable hydrolysate; more specific supported generic Soy term exists. Shared owner identifier does not establish source membership.'},
 {'candidate':'MICRO:0000178','assessment':'Mammalian enzyme digest/Bacto context narrower than unspecified Peptone.'},
 {'candidate':'MICRO:0000174','assessment':'Enzyme processing not established for all generic Peptone.'},
 {'candidate':'MICRO:0000172','assessment':'Plant/animal scope omits manufacturer yeast-inclusive generic definition; no inferred feedstock.'},
 {'candidate':'FOODON:03315306','assessment':'Actual full OWL adds member_of some food additive (us cfr), not merely an ignorable flavoring comment. Source use in that scope is unproven. Initial candidate unselected; shared Polypeptone question remains separate.'},
 {'candidate':'CHEBI:749541','assessment':'Sparse two-star ChEMBL molecular-entity record lacks sufficient defined whole-mixture scope; matching label is insufficient.'},
 {'candidate':'mesh:D010461','assessment':'Direct Peptones name checked; acid-or-enzyme plus precipitation/solubility criteria not fully established for generic scope including base hydrolysates.'},
 {'candidate':'mesh:D011492','assessment':'Selected broader material definition explicitly permits partial or extensive protein hydrolysis; no inferred therapeutic, food-additive or nutrient-role assertion.'},
 {'candidate':'MICRO:0000167','assessment':'Defined organic mixture is a valid but less specific broad alternative than the supported protein-hydrolysate material family.'}]
save('parents-scientific-review-v1.json',{'reviewer':'/root/final_skeptical','completed_at':now,'primary_author':'/root/buffer_hepes','independence':'No primary payload authorship or maintained edits. Current formal ontology and manufacturer material scopes independently inspected.','base_head':'0bac12cabfd1f67f212631d8eef9aa46379f6b41','verdict':'pass_with_limitations','payload_reviews':payload,'case_reviews':cr,'candidate_reviews':matrix,'input_integrity':bind(Q/'parents-final-integrity-v1.json'),'independent_native_and_payload_check':bind(Q/'parents-media-independent-checks-v1.json'),'tombstone_exact_rereview':bind(Q/'tombstone-independent-review-v1.json'),'finding_dispositions':[{'finding_id':'W05-PARENTS-NEW01','disposition':'RESOLVED_FOR_GENERIC_PEPTONE_WITH_MESH_SUCCESSOR; SHARED_POLYPEPTONE_APPLICABILITY_SEPARATE','original':bind(S/'parents/new-finding-before-fix.json'),'chronology':bind(S/'parents/chronology.json'),'assessment':'Worker report preceded private MeSH selection; formal GitHub filing occurred later. No reconstructed filing-before-private-fix claim.'},{'finding_id':'W05-CONSOLIDATED-PARENTS-REVIEW-001','disposition':'RESOLVED_EXACT_V2','original':bind(Q/'parents-new-finding-v1.json'),'remedy':bind(S/'parents/tombstone/wording-erratum.json'),'assessment':'Only new unsupported human-attribution phrase removed; exact original evidence/history unchanged.'}],'provenance_erratum':{'receipt':bind(S/'parents/attribution-erratum.json'),'assessment':'One new metadata retriever corrected to authentic /root/polypeptone_supplement; original captured bytes/time unchanged. No reauthored historical scientific support.'},'limitations':['All original source-case and export holds remain. Two raw generic observations and Soy source record assessed; 200 quarantined Soy associations are preserved, not 200 freshly approved source cases.','Shared membership associations, source routing and final owner integration remain coordinator-owned.','The whole tombstone is reviewed as an unresolved rejected continuity record, not a supported branded active identity.','Root-composed final decisions and consolidated full native validation remain separate.']})
