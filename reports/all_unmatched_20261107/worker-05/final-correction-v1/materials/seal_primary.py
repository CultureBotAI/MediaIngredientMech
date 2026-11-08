"""Seal the private author packet; this is integrity checking, not peer review."""
from pathlib import Path
import json, hashlib, datetime, subprocess, yaml

L=Path(__file__).resolve().parent
W=Path.cwd()
C=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107')
O=W/'reports/all_unmatched_20261107/worker-05'
A=json.loads((L/'context/w08-materials-assignment.json').read_text())
D=json.loads((L/'decisions.json').read_text())['decisions']
E=json.loads((L/'evidence.json').read_text())['evidence']
P=json.loads((L/'proposals.json').read_text())['proposals']
at=datetime.datetime.now(datetime.timezone.utc).isoformat()
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def objsha(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(n,x):
 p=L/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n');return p
def capture_path(r):
 if r['root']=='source':return Path(A['source_root'])/r['path']
 if r['root']=='artifact':
  prefix='final-correction-v1/materials/'
  return L/r['path'][len(prefix):] if r['path'].startswith(prefix) else O/r['path']
 raise ValueError(r)
def binding(p):return {'path':str(p),'sha256':sha(p)}

payload_scopes={
1:'The Bacto manufacturer description supports the bovine/porcine digest comparison. Fish peptone (Fluka) is explicitly incompatible with that material boundary. The retained Neopeptone, Universal and Oxoid rejections remain product-specific; other generic meat or mixture labels are preserved under their existing unresolved owner/source scope rather than newly approved.',
2:'The unnumbered Proteose owner does not denote the numbered No. 3 product. Retain the numbered-alias withdrawals and history without promoting generic peptic-digest or role claims.',
3:'Sucrose identity is retained. d-Salicin is a different named compound, so the source-preserving alias rejection is supported independently of the original lexical match.',
4:'TOGO M230 describes leafy soil and its recipe use. A bounded variable soil input is supported; no species, exact composition, fertilizer status or equality to other garden soil is inferred.',
5:'JCM 1474 specifies liver powder, water and the extraction process. The separate extract owner preserves input versus filtrate boundaries. No deictic see-below alias is made globally resolving.',
6:'The literal Wako meat-extract source is retained as a supplied form. The Wako-hosted manufacturer comparison does not establish the historical catalog, species or an exact formula.',
7:'Explicit Fraction V contexts and unspecified fraction contexts remain distinct in supplied-form provenance. Stock input masses are not recast as receiving-medium concentrations. The coordinator union with other-worker forms remains pending.',
8:'The source explicitly supplies pooled sterile human urine. The owner retains that preparation scope; an unqualified sterile urine label does not globally denote pooled urine. Donor, pooling and sterilization details are not invented.',
9:'Oxoid LP0032 describes pancreatic-digested milk material. Preserve the commercial preparation boundary and partial component assertion without equating it to untreated milk.',
10:'The source literally names meat peptone with BD Bacto attribution; its enriched Bacto label does not prove a historical catalog. Preserve bounded supplier provenance and existing mapping limits.',
11:'NBRC 907 defines chrysalis extract as a supplied ingredient without an extraction formula. The source-qualified material can be curated without fabricating components or taxonomic origin.',
12:'Peptone from gelatine is a hydrolyzed gelatin preparation, distinct from unhydrolyzed gelatin and unsupported Bacto assignment. Missing manufacturer detail does not prevent bounded material curation.',
13:'The milk sources explicitly qualify whole fat. Preserve this supplied form and the original source quantities; volume-to-mass importer errors remain upstream and do not redefine milk identity.',
14:'The manufacturer names CrystalSea Marine Mix as a commercial salt preparation. Product identity is retained without claiming all historical lots have an invariant component formula or are generic Sea Salt.',
15:'DSMZ 687 and the ingredient record name Bacto Panton. A bounded commercial peptone identity is supported, while digest substrate and historical catalog remain unasserted.',
16:'DSMZ 687 and the ingredient record name Bacto Bitone separately from Panton. The named material is curated without inventing a digest formula or treating the equal recipe doses as equivalence.',
17:'All four assigned recipes name fish-sperm DNA from SERVA. Retire the ten generic or thymus identity aliases while preserving raw provenance and the herring tombstone. The retained legacy NARROW_MATCH direction is unchanged and not endorsed by this alias/supplied-form delta.',
18:'The JCM source explicitly says sucrose 20% w/v. The optional typed link to existing sucrose is supported, but the stock remains PARTIAL because solvent and other preparation details are unspecified.',
19:'JCM 177 and the corresponding records name fish meat extract. Preserve a fish-derived extract without selecting species, catalog, extraction yield or hydrolysate identity.',
20:'The explicit numbered No. 3 supplier product is distinct from unnumbered Proteose. Manufacturer support allows bounded product and constituent-class assertions, not an invariant full composition.',
21:'Difco Soytone is a named product supported by the supplier and TOGO M1991. It remains distinct from generic soy digest, Phytone and Bacto Soytone; shared source substrate is not product equivalence.',
22:'The source uses small dried sardine as an extraction input. Preserve drying and whole-material scope without equating the fish input to the resulting maize-sardine filtrate or identifying a species.',
23:'Oxoid Special peptone is supported in its explicit Columbia context. Manufacturer LP0072 supplies the bounded digest/yeast blend comparison; it does not identify every unqualified 23 g peptone mixture as this product.',
24:'NBRC 1372 supplies rice extract as a source-qualified material. The source does not disclose an exact extraction recipe, so no concentration or molecular composition is invented.',
25:'Difco skim milk is supported as a dry preparation by the direct manufacturer source. This is separate from an ambiguous liquid skim milk alternative and does not approve every commercial milk variant.',
26:'The substantive historical preparation evidence is TOGO M109 with JCM_M117 lineage, not the empty direct JCM response. Preserve literal C--10, exclude unsupported C100 equivalence and the human NCIT identity, and keep C9322 in the separate pending coordinator candidate.',
27:'NBCo liver extract concentrate is explicitly supplied by the source. Promote the bounded existing material without guessing animal species, strength, catalog or equality to fresh liver extract.',
28:'Maize extract is a known undefined material in DSMZ 570 and MediaDive 575. The bounded identity does not assert equivalence to maize meal, corn steep liquor or an unspecified processing recipe.',
29:'The manufacturer Hipolypepton description supplies a product boundary distinct from the BD casein/animal-tissue Polypeptone blend. Preserve the Trypticase-or-Hipolypepton alternative as a choice, not one identity.',
30:'The existing Polypeptone family requires a local identity and withdrawal of the conflicting Hipolypepton routing. Manufacturer distinctions support that bounded change, while heterogeneous unresolved source variants and the coordinator union remain held.',
31:'The specific MICRO Phytone term and manufacturer description support the authentic existing Phytone owner. Reuse the coordinator bounded conclusion with original attribution, exclude the erroneous barley parenthetical and retain competing whole-payload integration separately.',
32:'The generic soy-digest owner should not resolve the five named-product or alternative aliases. Manufacturer product descriptions and source history support the withdrawals. Preserve all 200 source holds, occurrence totals, merge history and the rejected Bacto tombstone.',
33:'The Oxoid-qualified malt extract agar material is distinct from a generic formula claim. Current product and prepared-plate comparisons support partial composition without assigning an exact historical catalog or treating receiving dose as composition.',
34:'The source explicitly supplies tomato extract as a volume input. Bounded promotion of the existing material is supported; extraction chemistry, composition and final dose normalization remain unspecified.',
35:'The original MediaDive source includes Merck attribution for Universal peptone. The named supplier material is supported. The current M66 blend is a comparison and does not prove the historical catalog.',
36:'The ontology lookup directly states the named Neopeptone term and manufacturer definition, so that narrow evidence object is DATABASE_MATCH. Product applicability and all source/release holds remain separately bounded.',
37:'Sigma-qualified sea-salt contexts support reuse of the existing preparation owner with registry identity. The NCIT relation remains withdrawn. Unqualified natural/artificial and historical product routes are not universally assigned, and S9883 is only a manufacturer comparison.',
38:'UTEX supports the existing organic peat material. SAG peat extraction inputs supply process context but do not prove identical input membership. Promote the existing owner without merging peat soil, extracts or greenhouse soil.',
39:'The unqualified generic peptone owner is not established as specifically mammalian by its lexical history. Preserve the bounded local identity, reject the truncated preparation fragment and keep every component-target and source-role dependency explicit.'
}
assert len(payload_scopes)==39
save('payload-primary-assessments.json',{'author':'/root/materials_research','review_role':'Primary author reassessment; not independent skeptical review','at':at,'assessments':[{'proposal_id':p['proposal_id'],'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'predecessor':p['predecessor_capture'],'selected_successor':p['after_capture'],'case_ids':p['case_ids'],'evidence_ids':p['evidence_ids'],'full_payload_read':True,'conclusion':payload_scopes[i],'limits':'Historical event and occurrence-statistic preservation is not new approval of inherited roles, source assignment, legacy mapping directions or release.'} for i,p in enumerate(P,1)]})

prim=json.loads((L/'primary-index.json').read_text())
for x in prim:
 x['scientific_read_scope']='Substantive source recipe/component tables and preparation comments, or product/ontology definition and named-material applicability; page chrome and unrelated advertisements are not scientific evidence.'
 if x['index']==60:x['scientific_read_scope']='Manufacturer guide sections on peptone definition and manufacture, soy product descriptions and processing, Bacto/Proteose/Polypeptone descriptions, and named product catalogs (including printed pages 7, 13, 33, 49 and 92). Entire unrelated manual chapters and every referenced experiment were not read or newly endorsed.'
 if x['index']==103:x['scientific_read_scope']='Wako manual Hipolypepton series and applicable product description (printed page 8); the entire large catalog was not scientifically reviewed.'
 if x['index']==120:x['scientific_read_scope']='Entire unsuccessful JCM 117 response, Nothing found. This is explicitly not positive recipe evidence.'
 if x['index']==102:x['scientific_read_scope']='All five original archived TOGO rows, complete component tables and recipe comments. The archive fetch timestamp is an aggregate timestamp, not an exact per-record retrieval time.'
pre=json.loads((L/'preflight.json').read_text())
native=C/'workers/w08/worktree/.temp/w05-published-head-independent-review-v1/native-fixture/reviews/structured/20261108T071144Z-worker08-independent-worker05-full188-payload138/review.yaml'
save('scientific-read-ledger.json',{'author':{'identity':'Codex /root/materials_research','model':'gpt-6','role':'W05 primary materials author','independence':'Not independent of these materials proposals; independent skeptical review remains pending.'},'completed_at':at,'contract_and_input_bindings':pre['inputs'],'native_external_review':{**binding(native),'read_scope':'Review metadata, limitations and seven materials findings; the external materials packet supplies all 61 case and 39 proposal appraisals. No claim of re-reviewing other worker08 scientific cohorts.'},'assigned_cases':61,'complete_selected_payloads':39,'source_context_occurrences':191,'case_context_read_scope':'Full recipe snapshots were read into the parsed context ledger and hash checked. Scientific review considered each assigned ingredient occurrence, raw quantities, source identifiers, recipe/preparation boundaries and substantive primary recipe sections. Unrelated ingredient annotations, organism roles and historical experiments were not newly certified.','byte_read_ledger':binding(L/'input-byte-read-ledger.json'),'source_extracts':prim,'other_read_inputs':[binding(p) for p in sorted((L/'context').glob('*')) if p.is_file()],'coordinator_candidate_scope':'All 37 candidates are accounted for by the exact summary. Only bounded Phytone, Soy and Catalase field conclusions are reused; the five overlapping full payloads remain separate attributed dependencies. No complete scientific review of all 37 unions is claimed.','w02_scope':'Full audit handoff and exact 27 relevant materials suggestion rows, their complete mapping-evidence objects and 39 payload histories. The full 981-entry audit is attributed to W02, not claimed as new work by this author.','source_access_times':'Original evidence captures and their original access times are retained. Re-reading a capture is not a new network retrieval. New copied OLS and issue evidence uses the original coordinator fetch receipts.','no_primary_claim_from_hashes':True,'no_independent_review_or_release_approval':True})

errors=[];checked=0
def check(ok,message):
 global checked
 checked+=1
 if not ok:errors.append(message)
for c,d in zip(A['cases'],D):
 check(c['case_id']==d['case_id'],'case order mismatch')
 check(objsha(c)==d['case_input_sha256'],f'case hash {d["case_id"]}')
 old=next(x for x in A['decisions'] if x['case_id']==d['case_id'])
 for key in ['occurrence_ids','preserved_source_holds','preserved_downstream_holds']:
  check(d.get(key)==old.get(key),f'{key} {d["case_id"]}')
 check(d['independent_review']['status']=='pending','self approval')
eids={e['evidence_id'] for e in E};check(len(eids)==len(E),'duplicate evidence id')
pids={p['proposal_id'] for p in P};check(len(pids)==len(P),'duplicate proposal id')
for e in E:
 r=e['capture'];p=capture_path(r);check(p.is_file() and sha(p)==r['sha256'],'evidence capture '+e['evidence_id'])
for p in P:
 check(set(p['evidence_ids'])<=eids,'proposal evidence ids '+p['proposal_id'])
 check(set(p['case_ids'])<=set(A['case_ids']),'imported case '+p['proposal_id'])
 for key in ['after_capture','predecessor_copy','before_capture']:
  if p.get(key):check(sha(capture_path(p[key]))==p[key]['sha256'],'proposal '+key+' '+p['proposal_id'])
 if p['before_sha256']:check(sha(W/p['owner_path'])==p['before_sha256'],'before owner changed '+p['proposal_id'])
 old=next(x for x in A['proposals'] if x['proposal_id']==p['replaces_proposal_ids'][0])
 check(p['case_ids']==old['case_ids'],'proposal case membership changed '+p['proposal_id'])
 a=yaml.safe_load(capture_path(p['after_capture']).read_text());b=yaml.safe_load(capture_path(p['predecessor_copy']).read_text())
 check(a.get('curation_history',[])[:len(b.get('curation_history',[]))]==b.get('curation_history',[]),'history loss '+p['proposal_id'])
 check(a.get('occurrence_statistics')==b.get('occurrence_statistics'),'count change '+p['proposal_id'])
for d in D:
 check(set(d['proposal_ids'])<=pids,'decision proposal refs '+d['case_id'])
 check(set(d['evidence_ids'])<=eids,'decision evidence refs '+d['case_id'])
for x in pre['inputs']:
 p=Path(x['path']);p=p if p.is_absolute() else W/p
 check(sha(p)==x['sha256'],'frozen input changed '+str(p))
status=subprocess.run(['git','status','--short'],capture_output=True,text=True,check=True).stdout
head=subprocess.run(['git','rev-parse','HEAD'],capture_output=True,text=True,check=True).stdout.strip()
check(head==A['head'],'head changed')
check(not status,'tracked worktree mutation')
native_result=json.loads((L/'validation/native-validation.json').read_text())
check(not native_result['component_partonomy_violations'],'native partonomy failures')
check(native_result['closed_schema_errors']==0,'native schema failures')
core={n:sha(L/n) for n in ['decisions.json','evidence.json','proposals.json','primary-conclusions.json','payload-primary-assessments.json','scientific-read-ledger.json','payload-ancestry.json','finding-dispositions.json','mapping-evidence-dispositions.json','integration-dependencies.json']}
receipt={'at':at,'author':'/root/materials_research','status':'PASS' if not errors else 'FAIL','scope':'Author byte-integrity and structural checks only; not independent scientific review','checks':checked,'errors':errors,'head':head,'git_status_short':status,'counts':{'cases':len(D),'proposals':len(P),'evidence':len(E),'cases_with_proposals':sum(bool(d['proposal_ids']) for d in D),'cases_without_proposals':sum(not d['proposal_ids'] for d in D),'context_occurrences':sum(len(c.get('occurrences',[])) for c in A['cases']),'changed_payloads':sum(p['after_capture']['sha256']!=p['predecessor_copy']['sha256'] for p in P)},'core_files':core,'native_receipt':binding(L/'validation/native-validation.json'),'review_status':'Independent skeptical review pending for all 61 cases and all 39 entire payloads.'}
save('validation/integrity-receipt.json',receipt)
assert not errors,errors
handoff={'at':at,'primary_author':'Codex /root/materials_research','model':'gpt-6','status':'Primary work sealed; independent review pending','counts':receipt['counts'],'files':core,'integrity_receipt':binding(L/'validation/integrity-receipt.json'),'publication_root':'reports/all_unmatched_20261107/worker-05/final-correction-v1/materials/','artifact_capture_root':'reports/all_unmatched_20261107/worker-05','optional_findings':['W05-MAT-005','W05-MAT-006'],'retained_dependencies':['All original source, role, organism, owner and export holds.','Eighteen historical MICRO:0000178 inbound component references after the already distinct Marine repair; no automatic retargeting.','All 37 coordinator union candidates remain pending; five overlapping candidates are preserved separately with origin records.','Bacto Soytone and herring-sperm DNA tombstones remain unchanged.','Legacy retained fish-DNA and Catalase mapping directions are not endorsed by this supplied-form/alias/provenance correction.'],'requested_next_step':'Independent authorship-separated skeptical review of every case, complete payload, source/evidence applicability and final finding disposition; root then performs whole-lane integration checks.','no_maintained_or_git_writes':True,'no_source_or_export_release':True}
save('HANDOFF.json',handoff)
(L/'HANDOFF.md').write_text(f'''The materials primary successor is ready for independent review: {len(D)} cases, {len(P)} complete guarded YAML proposals and {len(E)} evidence records. {receipt['counts']['cases_with_proposals']} cases have proposals; eight retain specific product-selection, alternative-input or existing-owner dispositions.

The author is Codex `/root/materials_research` (gpt-6), the materials primary author. This is not independent review. All seven MAT findings have explicit proposed dispositions; MAT005 metadata classification and MAT006 sucrose linking are optional, nonblocking improvements. The 27 mapping-evidence audit objects have claim-specific dispositions: Neopeptone's narrow lookup uses `DATABASE_MATCH`; the agent judgments use `LLM_SUGGESTION`, while inherited human/process and component evidence types remain unchanged.

The fresh source conclusions are in `primary-conclusions.json`, the complete-payload assessments in `payload-primary-assessments.json`, and actual read scopes and hashes in `scientific-read-ledger.json`. `payload-ancestry.json`, `before/`, `predecessor/` and `diffs/` preserve the original guards and history. Nine complete payloads are byte-identical to their published predecessors; the other 30 carry the specified corrections or provenance method updates.

`integration-dependencies.json` preserves the 18 historical Peptone component dependencies and distinguishes the already changed Marine reference. A structurally resolving Bacto target does not prove that any particular source part denotes Bacto. No component references were retargeted. The 37 coordinator unions remain pending independent review; overlapping exact candidates and their origins are separate from W05 case ownership. Only the supported bounded Phytone/Soy and Catalase conclusions are reused.

All 39 YAMLs passed the unchanged native guarded writer. The in-memory published 138-proposal overlay with these 39 replacements passed component partonomy. `validation/integrity-receipt.json` records {checked} integrity checks with no errors and binds the final core bytes. These checks do not approve inherited roles, unresolved source identity, whole owners or downstream release.

No maintained data, exports, gates, code, old reports, Git state or GitHub objects were changed. Independent review of all 61 cases and all 39 entire payloads is the next step. Final file hashes are in `HANDOFF.json` and `MANIFEST.json`.
''')
members=[{'path':str(p.relative_to(L)),'sha256':sha(p),'bytes':p.stat().st_size} for p in sorted(L.rglob('*')) if p.is_file() and p.name!='MANIFEST.json']
save('MANIFEST.json',{'created_at':at,'author':'/root/materials_research','status':'sealed primary packet; independent review pending','scope':'Every materials-lane artifact except this manifest itself','files':members})
print(json.dumps({'core':core,'manifest_sha256':sha(L/'MANIFEST.json'),'files':len(members),'checks':checked,'counts':receipt['counts']},indent=2))
