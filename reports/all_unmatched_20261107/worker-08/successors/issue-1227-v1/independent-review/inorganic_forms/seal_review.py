import json,hashlib,datetime,subprocess,yaml
from pathlib import Path
R=Path('reports/all_unmatched_20261107/worker-08');S=R/'successors/issue-1227-v1';I=S/'research/inorganic_forms';O=S/'independent-review/inorganic_forms'
def h(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def canon(a):return hashlib.sha256(json.dumps(a,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(n,a):
 p=O/n;assert not p.exists(),n;p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
D=json.loads((I/'decisions.json').read_text());P=json.loads((I/'proposals.json').read_text());A=json.loads((I/'assignment.json').read_text());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
checks=[]
def ck(n,b):
 checks.append({'check':n,'passed':bool(b)});assert b,n
ck('exact assigned case IDs',[d['case_id'] for d in D]==A['case_ids']);ck('exact assigned proposal IDs',[p['proposal_id'] for p in P]==A['proposal_ids'])
AD={d['case_id']:d for d in A['decisions']};AP={p['proposal_id']:p for p in A['proposals']}
for d in D:
 for f in ['source','case_input_sha256','occurrence_ids','occurrence_context','preserved_native_decisions','preserved_holds']:
  ck(d['case_id']+' '+f,d.get(f)==AD[d['case_id']].get(f))
for p in P:
 ck(p['proposal_id']+' exact payload',h(R/p['after_capture']['path'])==p['after_capture']['sha256'])
 for f in ['proposal_id','owner_path','before_sha256','kind','case_ids']:ck(p['proposal_id']+' '+f,p.get(f)==AP[p['proposal_id']].get(f))
 if p['before_sha256']:ck(p['proposal_id']+' exact original preimage',h(p['owner_path'])==p['before_sha256'])
ck('input decisions frozen',h(I/'decisions.json')=='2f56b8f9d932534ffc66fbe6d340f2d434ea3c8a0474c28df9172de420463921')
ck('input proposals frozen',h(I/'proposals.json')=='07cbd40be3bf0694ce1af3f56a05312b068fb1910c97c2aff8fd2177badb5ec1')
ck('input evidence frozen',h(I/'evidence-additions.json')=='cf143abefb8002b1458001ddd74cda58a42cb719f427a932fef185cff3fc3a8b')
case_text='''JCM 574 directly defines the 1 M KH2PO4 input and its 16.6 ml contribution to a buffer. Later dilution water does not identify the input carrier; JCM 1181 imports the buffer. PBBM remains a conditional comparison, not an equality claim.
The DSMZ trace preparation identifies a 2 N NaOH input, not the resulting EDTA mixture. UNKNOWN closure and the source-qualified anchor preserve the distinction from generic pure NaOH.
JCM 1130 directly specifies 26 ml of 10 N NaOH in the VFA mixture; JCM 1385 explicitly inherits it. Other titrant/crotonate uses remain conditional, and the VFA acids are not components of this reagent.
NBRC 268 explicitly says anhydrous base. The new spelling belongs to the anhydrous K2HPO4 owner; the four malformed/generic phosphate aliases are separately non-resolving, without source reassignment.
The supplied ammonium magnesium phosphate lacks hydration proof. Supplier hydrated and hexahydrate witnesses are not interchangeable, so a specific hydrate remains scientifically unresolved.
JCM 908 expressly supplies a 10% w/v sodium sulfide nonahydrate stock and filter sterilization. Its unknown carrier does not prevent a bounded stock proposal, but does prevent complete membership claims.
The literal KH2PO4 seven-water formula is not verified by an appropriate form-specific primary witness. Retaining the exact literal and hold is preferable to assigning ordinary monobasic phosphate.
EDTA disodium is explicit but hydration is not. The two-source contexts do not establish dihydrate; the form hold is substantive.
The 1 N NaOH occurrences can be compared with the directly defined ATCC 1340 reagent, but concentration alone does not establish identical preparation. Generic solution aliases are rejected on the pure owner.
NBRC 1601 actually prints Na2Mo4O4. The unusual stoichiometry cannot be silently corrected to molybdate from lexical similarity; the 27.6 microgram recipe amount does not resolve identity.
TOGO M3140 retains Na2NPO4 at 0.11 g. The nitrogen/sodium formula ambiguity is real, so a guessed phosphate identity is not supported.
PCR-S11 enumerates 3.55 g Na2HPO4 and 500 ml distilled water for the nominal 50 mM stock. COMPLETE describes the two printed inputs, not inferred hydrate or exact final volume.
The ATCC Nitrosolobus phenol-red preparation supplies 1 ml of 6 N NaOH; the separate 99 ml deionized water belongs to the receiving preparation. UNKNOWN closure is appropriate.
CCAP SP supports the manganese sulfate heptahydrate source reading. The malformed parser token requires a source-layer correction, not a new globally resolving chemical alias.
JCM 1357 gives EDTA disodium without hydration. Retaining the source amount and hydrate uncertainty avoids manufacturing a dihydrate identity.
JCM 899 describes a 5% sulfide input and its own dose. The ATCC 1942 stock is an explicit comparison anchor; equal percent does not prove shared carrier or preparation.
PBBM's 2.5% sulfide input remains a conditional comparison to ATCC 1943. Neither the percent basis nor whole-stock equivalence is supplied by the shared label.
The eight JCM 5% sulfide contexts have different receiving doses/processes. The proposal preserves these occurrences while declining concentration-only equivalence with the ATCC anchor.
PCR-S11 directly identifies 0.1 N NaOH as the EDTA-preparation reagent. Hemin and SGP7 titration occurrences retain their independent scope; no receiving solutes are imported.
JCM 820 prints NaHPO4 dodecahydrate with an incomplete sodium count. That literal is insufficient for exact disodium phosphate identification despite the water count.
The Ilyobacter source literal names KH2PO4 dihydrate, while the relevant direct primary retrieval is unavailable. No verified chemical-form correction can be inferred from the name alone.
JCM 574 directly supplies 83.4 ml of a 1 M K2HPO4 input. Subsequent water and KH2PO4 belong to the buffer, not the input stock; the hydrate remains unresolved.
JCM 647/657 specify thiosulfate pentahydrate as a receiving-medium concentration. This supports existing chemical identity, not a newly invented stock formulation.
The six truncated Na tokens belong to sodium sesquicarbonate preparation contexts. The outcome correctly routes source parsing rather than creating a universal Na alias.
ATCC 1490 and DSMZ hemin sources specify 1 N NaOH. They remain comparisons to the ATCC 1340 defined reagent; rejecting solution aliases on pure NaOH is independently supported.
The Ilyobacter and SGP7 KH2PO4 dihydrate literals retain their form conflict. Similar buffer function is not evidence that the dihydrate token means anhydrous KH2PO4.
The spaced/unspaced 2 N NaOH cases share exact DSMZ 1094 witnesses. Named trace protocols provide bounded reuse; unrelated M3213 titration remains outside exact preparation assignment.
DSMZ 901a describes a 3 g sulfide input. Parser repair and rejection of stock-qualified aliases on the nonahydrate owner do not alter the actual supplied-form scope.
DSMZ 1669 uses 3 g Tris in a receiving medium. The amount token is source context, not an identity alias; Tris buffer and hydrochloride strings remain rejected on the base.
Allen M2231 supplies a literal seven-water phosphate stock. Its bounded preparation can be represented without approving the chemically unresolved seven-water component.
The explicit EDTA disodium dihydrate spelling matches the active form-specific owner. The merge tombstone and pre-existing role/export restrictions remain unchanged.
JCM 1020's autoclaved 5% sulfide input retains process specificity and only a conditional comparison to ATCC 1942; no concentration-only merge is authorized.
PCR-S11 combines 100 ml of each named 50 mM stock and adjusts to pH 7.5. The unnamed adjustment input supports PARTIAL; the separate 2 L EDTA instruction is not a buffer final volume.
EMA's mixed-cation tetrahydrate is supported by the full Thermo CAS/formula/structure table. CAS identity and asymmetric class grounding preserve the water and cation stoichiometry; cross-shard selection remains held.
PBBM's 1 M KH2PO4 is a meaningful source input, but does not establish identical stock manufacture to JCM 574. The existing conditional link avoids both automatic collapse and a speculative duplicate.
NOS and phenol-red contexts identify 0.1 N NaOH inputs. They remain comparison scopes around the stronger PCR-S11 preparation rather than identical full recipes.
ATCC 1340 explicitly defines N NaOH as 4 g/100 ml and uses 30 ml. The other bare-N contexts do not inherit that mass/volume definition automatically.
JCM 941 Solution C explicitly contains 5 g literal Na2S2O4 dihydrate plus 40 ml distilled water. COMPLETE is limited to these printed inputs; the unusual hydrate remains UNMAPPED.
The H3BO4 literal recurs in actual source recipes. Recurrence does not prove boric-acid identity; a source correction or supplied-form witness is still needed.
TOGO M3160 describes carbon monoxide gas. The Co token is a symbol collision with cobalt, not a global metal identity; source-context correction is warranted.
DSMZ 104 directly calls for 8 N NaOH for pH adjustment. Its carrier and production recipe are unreported, so UNKNOWN is suitable for this distinct strength-defined reagent.
TOGO M988 repeats the JCM 941 Solution C context. It supports the same bounded recipe comparison while leaving the bare dihydrate compound unresolved.
PBBM explicitly uses 10 ml of a 1 M Na2HPO4 stock. Hydration and carrier are unspecified; the source-qualified input is not exact anhydrous sodium phosphate.
JCM 554's KH2PO4 instruction includes dissolving and adjusting pH to 7.0. The instruction belongs to preparation context and is not a new pure-chemical synonym.
JCM 221 directly supplies 200 ml of 0.2 N NaOH before later reducing-agent additions. ATCC 1190/1191 have a cysteine-hydration difference, so their whole reducing mixtures are not equated.
CCAP PC supplies a calcium chloride stock at 10 g/L and a 1 ml dose. The truncated CaCl token and unspecified hydration cannot justify a universal chemical alias.
DSMZ 533 explicitly requires deionized water. The proposed treatment-grade identity is distinct from distilled water and does not claim purity, resistivity or sterility.
ATCC 1942's 10 ml stock dose and 0.5 g/L receiving amount support the stated 5% w/v basis. Nitrogen autoclaving is processing context, and carrier/closure remain unknown.
ATCC 1943 gives a 2.5% nonahydrate stock prepared under nitrogen and autoclaved. The percent basis and carrier remain unstated; separate cysteine is not included.
The actual retained OSTI article page 6 specifies LS4D K2HPO4 at 2.2 mM. This supports correcting TOGO's K2PO4 transcription, without approving all LS4D or Thauer formulation equivalence.
DSMZ 694's 3.5 g mixed-cation tetrahydrate agrees with the supplier's CAS 7783-13-3 identity. The complete batch7 evidence is now linked; W03 reconciliation remains a coordinator dependency.
Allen M2231 establishes 6 g plus 1 L deionized water and a 5 ml dose. The remaining requirement correctly concerns only the unusual seven-water chemical form, not already resolved dosing.
JCM 533/646/650 specify final sulfide nonahydrate concentrations. These are receiving-medium amounts and do not independently define a new stock recipe.
JCM 647 specifies a final 1 mM sulfide concentration. The existing chemical form is relevant, while stock composition remains a separate assertion.
The actual Sander dissertation page 22 prints ZnCl2 at 42 mg in the SL12 list. This supports the ZnCI2 transcription correction; the uninspected original 1992 chapter is not claimed as read.
TOGO M3152 and M3153 repeat the Wolin mineral-preparation protocol with 10 ml of 0.5 N NaOH. Their shared stated protocol supports one bounded reagent proposal, with unknown carrier.
JCM 497's sulfide amount is a receiving-medium concentration. The unsuccessful direct source request is preserved, and no unverified stock formulation is inferred.
PCR-S11 lists 6 g NaH2PO4 and 1 L distilled water. The two-input recipe is COMPLETE as printed; molarity arithmetic is not used to select a hydrate.
JCM 713 specifies a separately filter-sterilized 24% nonahydrate stock and 1 ml dose. Lack of percent basis is retained in fields, with UNKNOWN closure and no guessed solvent.
The source names Tris hydrochloride; Sigma T3253 verifies a chloride salt distinct from neutral Tris and Htris cation. The exact W05 candidate is only a coordinator referral, not an approved owner or merge.
JCM 650's 6 mM thiosulfate pentahydrate is a receiving concentration. It supports the form-specific chemical context without stock creation.
KG monohydrate source metadata conflicts with automatic anhydrous/hydrate matches. The coupled source override and alias cleanup retains all six sibling holds rather than choosing from lexical matches.
The KG hexahydrate owner still carries native identity/parent-row withholding. Its local presence is not independent supplied-form proof, so no automatic mapping release follows.
KG ammonium magnesium phosphate retains the same unresolved hydration issue as the C100 source. Supplier variants do not justify forcing the hexahydrate.
KG KH2PO4 dihydrate retains the supplied-form ambiguity. An existing lexical owner or buffer role cannot establish the literal hydrate identity.
The raw diammonium hydrogenphosphate formula is compatible with CHEBI:63051. Existing Fisher/source and native holds remain separate from that chemical spelling assessment.
KG Na2S x H2O conflicts with an automatic anhydrous target. The unspecified hydrate is not collapsed to anhydrous or nonahydrate, and rejected-source evidence is preserved.
KG H3BO4 remains an unresolved literal formula. No new global boric-acid identity follows from a plausible typographic interpretation.
The heptahydrate owner uses NCIT:C61946 and CAS 7782-85-6. Retaining its existing structure/role holds avoids treating ontology recognition as full owner approval.
The K2HPO4 trihydrate CAS 16788-57-1 has a known two-owner reconciliation dependency. No duplicate creation or winner selection is hidden in this no-change outcome.
The six scutellarin/glucuronide aliases are chemically foreign to dithionite. Their rejection on both live and tombstone owners is justified; the tombstone's obsolete chemistry is not reapproved.
The dihydrate owner must not resolve monohydrate aliases. The coupled cleanup preserves raw strings and the local identity/parent mapping holds.
KG KH2PO4 seven-water material remains chemically unverified. The Allen preparation context does not manufacture an exact solid identity for this bare component.
The third mixed-cation tetrahydrate case is bound to the full original supplier capture and CAS identity. Its W03 competing-owner boundary remains explicit and unresolved by this review.
ChEBI:91259 supplies exact dodecahydrate structure including twelve waters. The replacement corrects inherited anhydrous chemistry; old contradictory history and source/role holds are preserved.
The KH2PO4 owner correctly rejects generic, incomplete, dibasic and concentration-qualified labels. This protects pure-chemical scope without transferring source memberships.
The monohydrate alias additions and three coupled source overrides remain connected to the sibling rejections. They do not independently release the six original native holds.
The frozen MediaDive 552 row explicitly gives 5 g thiosulfate in 100 ml water and a separate 10 ml dose. COMPLETE covers those inputs; conflicting automated form metadata remains unresolved.
The eleven malformed or form-unspecified molybdate aliases do not establish exact disodium molybdate dihydrate identity. Rejection preserves provenance and avoids guessing corrected source chemistry.
The KG dithionite dihydrate case has a JCM 941 Solution C context. The bounded stock proposal is supported, while the bare unusual hydrate remains chemically held and is not equated to anhydrous dithionite.'''.splitlines()
assert len(case_text)==80,len(case_text)
proposal_text='''NBRC 268 expressly specifies anhydrous K2HPO4. The added spelling is compatible; KH2HPO4 and K2HPO are preserved as rejected formula fragments, with original history and holds intact.
The three one-water labels are non-resolving on the two-water owner. The exact raw strings, original provenance, source counts and inherited mapping restrictions are preserved.
The three explicit monohydrate spellings match the live CHEBI:114249 owner. This is only the owner-side part of the coupled issue758/source override correction.
The six flavonoid aliases are rejected on the existing REJECTED Na2s2o4 tombstone. Its obsolete inherited chemical packet and rejected status remain unapproved and unchanged.
The same six flavonoid aliases are rejected on the live dithionite owner, preserving the exact owner family dependency rather than merging physical records.
Full Thermo 040320 batch7 verifies CAS 7783-13-3, H13NNaO8P and four-water structure. CAS-primary with NARROW_MATCH to sodium phosphate is asymmetric class grounding. The original access time and all three cases are bound; W03 integration remains held.
The explicit disodium dihydrate source spelling is compatible with CHEBI:64758. The retired duplicate remains retired and no role or count assertion is introduced.
DSMZ 533 supports a deionized-water grade. Registry identity and CURATOR_JUDGMENT are appropriate; no distilled equivalence, purity or molecular-water decomposition is invented.
DSMZ 1094 supplies the 2 N NaOH anchor and the named trace-protocol contexts. The proposed reagent contains NaOH at the stated normality; carrier closure remains UNKNOWN and unrelated titration uses are not equated.
JCM 1130's 26 ml of 10 N NaOH is an input to its VFA mixture. The payload preserves the input identity, excludes receiving acids and limits reuse to the explicit bridge; UNKNOWN closure is supported.
ATCC 929 supplies 1 ml 6 N NaOH in a phenol-red preparation. The separate 99 ml water is not attributed to the input stock; the catalog NaOH component and UNKNOWN closure are compatible.
PCR-S11 specifies 0.1 N NaOH for its EDTA preparation. The reference targets NaOH, not the resulting chelate; unrelated hemin and titration comparisons remain conditional.
DSMZ 104's 8 N NaOH pH reagent has a distinct stated strength. Unknown carrier is honestly retained, separate from its other 1 N hemin reagent.
JCM 221's 0.2 N NaOH input is represented before sulfide/cysteine addition. Nitrogen/hydrogen treatment is operational context; the differing ATCC cysteine hydration is not erased.
Both TOGO Wolin preparations state the same 0.5 N NaOH protocol. One scoped reagent is appropriate, with initial carrier unknown and later mineral/water inputs excluded.
ATCC 1340 explicitly defines N NaOH as 4 g/100 ml. That mass/volume value is source-bound; other bare-N occurrences are comparisons rather than automatic assignments.
JCM 574's 1 M KH2PO4 input is a preparation distinct from its later buffer. Unknown hydration prevents a form-specific catalog link; later water is not imported, and UNKNOWN closure is accurate.
JCM 574's 1 M K2HPO4 input has the same independent carrier boundary and a distinct chemical constituent. The 83.4 ml receiving amount does not become stock composition.
PBBM's 1 M Na2HPO4 input has explicit concentration but unknown hydrate/carrier. Keeping the constituent UNMAPPED and closure UNKNOWN avoids anhydrous substitution.
The PCR-S11 recipe enumerates NaH2PO4 6 g and distilled water 1 L. COMPLETE is source-input completeness only; the phosphate hydrate and final solution volume remain unasserted.
The PCR-S11 recipe enumerates Na2HPO4 3.55 g and distilled water 500 ml. Both quantities are batch inputs; COMPLETE does not resolve hydrate by molarity arithmetic.
The PCR-S11 buffer contains 100 ml of each selected stock plus an unspecified pH-adjustment input. PARTIAL is justified; nested references require joint overlay integration and are not already maintained-catalog approvals.
Allen M2231 enumerates literal K2HPO4 seven-water material 6 g plus 1 L deionized water. COMPLETE covers the two inputs; the chemical component remains unresolved. The DI reference requires conditional joint integration.
JCM 908 expressly states 10% w/v nonahydrate and filter sterilization. The compatible catalog reference does not select a carrier or establish complete membership.
JCM 713 specifies 24% nonahydrate and filter sterilization. The payload correctly omits a guessed percent-basis quantity and retains UNKNOWN closure.
ATCC 1943 specifies 2.5% nonahydrate stock under nitrogen and autoclaving. Carrier and percent basis remain unasserted; the separate cysteine preparation is excluded.
Pure NaOH cannot globally resolve 1 N or 0.38 M solution labels. Their rejected status preserves source text and pure-solute identity while avoiding concentration collapse.
The eleven malformed/form-unspecified molybdate aliases are rejected with exact provenance. Identity CHEBI:75213, structure, counts and earlier1216 lineage are retained; no source chemical is guessed.
The operative dodecahydrate chemistry now matches CHEBI:91259 and CAS 10039-32-4, including twelve waters. Generic and Role aliases are non-resolving; contradictory historical events remain historical.
ATCC 1942's explicit stock dose and final solute amount support the stated 5% w/v interpretation. The note makes the arithmetic boundary visible, while carrier and equality to other 5% stocks remain unknown.
The exact frozen MediaDive 552 attribute supplies 5 g thiosulfate and 100 ml water, with 10 ml a distinct dose. COMPLETE is limited to the printed input list and the supplied salt form remains UNMAPPED.
JCM 941 and MediaDive solution4957 agree on 5 g literal dithionite dihydrate and 40 ml distilled water. COMPLETE covers the inputs; nitrogen is processing and the unusual hydrate is not approved chemically.
KH PO and Potassium Phosphate are non-resolving alongside the earlier dibasic/concentration rejections. Valid monobasic identity, original provenance, all counts and source holds remain preserved.
The two concentration-qualified nonahydrate strings remain provenance-only. Their rejection on the pure chemical owner does not alter explicit nonahydrate chemistry or assign stock recipes.
Tris hydrochloride, 1 M buffer and nitrilotriacetate strings cannot globally resolve to free Tris. The existing salt rejections and exact W05 referral remain; this review does not approve the competing W05 payload.'''.splitlines()
assert len(proposal_text)==35,len(proposal_text)
E=json.loads((R/'successors/issue-1201-v1/evidence.json').read_text())['evidence']+json.loads((I/'evidence-additions.json').read_text());used=set(sum([d['evidence_ids'] for d in D],[])+sum([p['evidence_ids'] for p in P],[]));ES={e['evidence_id']:e for e in E if e['evidence_id'] in used}
logs=[json.loads(x) for x in (O/'read-log.jsonl').read_text().splitlines()];readhash={x['sha256'] for x in logs};U={}
for e in ES.values():
 ck(e['evidence_id']+' capture bytes',h((R if e['capture']['root']=='artifact' else Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5'))/e['capture']['path'])==e['capture']['sha256'])
 if e['kind'] in ['primary_source','ontology','unsuccessful_search']:U.setdefault(e['capture']['path'],[]).append(e)
source_rows=[]
for path,es in U.items():
 sha=es[0]['capture']['sha256'];ck(path+' actual read or exact identical read',sha in readhash)
 row={'path':path,'sha256':sha,'evidence_ids':[e['evidence_id'] for e in es],'original_accessed_at':[e.get('accessed_at') for e in es],'locators':[e.get('locator') for e in es],'urls':[e.get('url') for e in es],'status':'actual_capture_content_inspected','scope':'Actual captured recipe, supplier identity, ontology result or failed-response content; PDF text where applicable. Navigation boilerplate is not scientific evidence. A web-rendered capture is not a new live retrieval.'}
 if path.endswith('primary-batch7-exact.json'):row.update(status='exact_identical_bytes_to_independently_read_capture',identical_read_path='research/inorganic_forms/captures/primary-batch7.json',scope='Entire original batch7 capture inspected, including Thermo lines103–160; the exact successor copy has identical SHA256.')
 if 'primary-batch6' in path:row['qualification']='Thermo item is incomplete historical retrieval, not active supplier property support. Full batch7 is the active source.'
 if any(e['kind']=='unsuccessful_search' for e in es):row['qualification']='Inspected search/failure outcome; absence is bounded to the captured query and is not universal absence or paper access.'
 raw=(R/path).read_bytes()
 if b'Nothing found' in raw or b'403 Forbidden' in raw or b'Internal Server Error' in raw:row['failure_qualification']='A failed/no-content response appears in this capture. It does not establish the unseen recipe; other successful witnesses are distinguished in individual appraisals.'
 source_rows.append(row)
retained=[{'path':'.temp/all-unmatched-worker-08/retained-primary-fulltexts/vitamins-af319dc1132578d8.source','sha256':'17580b1bc763e9acbcf856fd055d8c280dc41ea4e21c6af82fd1c67167d88af6','locator':'Actual PDF page6, Cell growth: LS4D K2HPO4 2.2 mM','scope':'Actual retained PDF page extracted with pdftotext and read; other article pages not claimed read.'},{'path':'.temp/all-unmatched-worker-08/inorganics/issue-1201-v1/sander2005.pdf','sha256':'14d9e107ff65f6898446a1e5b5d292f0dad0a75f765fce65b8f4219856973082','locator':'Actual PDF page22 / printed15, SL12 trace-element list: ZnCl2 42 mg per batch with A.dest. ad1 L','scope':'Actual retained dissertation page extracted and read; cited1992 book chapter not claimed read.'}]
for r in retained:ck(r['path']+' retained bytes',h(r['path'])==r['sha256'])
# Confirm ledger assertions against exact selected payloads; scientific appraisals above are separate.
PM={p['proposal_id']:yaml.safe_load((R/p['after_capture']['path']).read_text()) for p in P}
for r in json.loads((I/'evidence-category-ledger.json').read_text())['rows']:
 idx=int(r['path'].split('[')[1].split(']')[0]);ck(r['proposal_id']+' mapping evidence '+str(idx),PM[r['proposal_id']]['ontology_mapping']['evidence'][idx]==r['after'])
 if r['inherited_from_frozen_owner']:ck(r['proposal_id']+' inherited unchanged '+str(idx),r['before']==r['after'])
input_paths=[p for p in I.glob('*.json') if p.name not in ['progress.json','progress-final.json']]+[I/'HANDOFF.md']
input_hashes={str(p.relative_to(R)):h(p) for p in input_paths}
for name in ['issue1227-live-body.json','issue1201-live-comments.json','issue811-live-comments.json']:input_hashes[str((S/'inputs'/name).relative_to(R))]=h(S/'inputs'/name)
contracts={str(p):h(p) for p in map(Path,['MAPPING_SEMANTICS.md','AGENTS.md','src/mediaingredientmech/schema/mediaingredientmech.yaml','docs/record-review-profile.md','docs/record-reviews.md','.claude/skills/review-yaml-category/SKILL.md','.claude/skills/add-media/SKILL.md'])}
case_hashes={d['case_id']:canon(d) for d in D};payload_hashes={p['proposal_id']:p['after_capture']['sha256'] for p in P}
case_reviews=[{'case_id':d['case_id'],'decision_sha256':case_hashes[d['case_id']],'case_input_sha256':d['case_input_sha256'],'outcome':'accepted_with_preserved_holds','appraisal':case_text[j],'source_evidence_ids':d['evidence_ids'],'proposal_ids':d['proposal_ids'],'finding_ids':[],'full_frozen_case_and_occurrence_context_read':True,'hold_release':False} for j,d in enumerate(D)]
proposal_reviews=[{'proposal_id':p['proposal_id'],'selected_sha256':p['after_capture']['sha256'],'after_capture':p['after_capture'],'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'case_ids':p['case_ids'],'outcome':'bounded_proposal_accepted_with_preserved_holds','appraisal':proposal_text[j],'source_evidence_ids':p['evidence_ids'],'finding_ids':[],'entire_payload_and_history_read':True,'original_beforeimage_read':bool(p['before_sha256']),'whole_owner_release_approved':False} for j,p in enumerate(P)]
limitations=['This is authorship-separated review of the exact W08 inorganic packet. It does not approve own vitamin/mixture science, other workers, roles, source assignment, export or merge.','W03 shared sodium ammonium phosphate owner remains a coordinator cross-shard acceptance dependency; W05 Tris salt is only an exact referral. Neither competing payload is approved here.','PCR nested stock and deionized-water references denote proposed joint-overlay dependencies, not already-maintained physical YAML rows.','Original source/native withholding remains in every case. A compatible entity reference does not release identity, role, occurrence or export holds.','Captured failed requests and bounded no-result queries remain failures, not inspected paper content. Retained full papers were read only at the exact pages listed.','Author native schema/partonomy checks and failure controls are hash-bound and inspected; they were not rerun in this review. Root performs final combined native checks.','The final author case-assessment prose repeats the already read decisions; author assertions are not independent evidence. Every final decision and selected payload received the separate appraisal recorded here.']
save('source-read-ledger.json',{'reviewer':'/root/vitamins','author':'/root/inorganics','finished_at':now,'scope':'All relevant selected primary/ontology/unsuccessful-search captures, every final outcome and occurrence context, all35 whole payloads and12 original preimages.','capture_count':len(source_rows),'captures':source_rows,'retained_primary_pages':retained,'read_log':{'path':str((O/'read-log.jsonl').relative_to(R)),'sha256':h(O/'read-log.jsonl')},'beforeimage_comparison':{'path':str((O/'beforeimage-comparison.json').relative_to(R)),'sha256':h(O/'beforeimage-comparison.json')},'limitations':limitations})
save('independent-checks.json',{'finished_at':now,'checks':checks,'all_passed':all(c['passed'] for c in checks),'native_checks':'Read and hash-bound author validation; no redundant native run. Root final native overlay remains required.','input_hashes':input_hashes,'contract_hashes':contracts})
save('findings.json',{'reviewer':'/root/vitamins','author':'/root/inorganics','findings':[],'open_blocking_findings':[],'existing_findings_dispositions':[{'finding_id':f,'disposition':'bounded_inorganic_correction_supported','hold_release':False} for f in ['W08-IR-001','W08-IR-003','W08-IR-006','W08-IR-008','W08-IR-010','W08-IR-011']],'boundary':'No newly confirmed defect in this exact assigned packet. Existing unrelated scientific, native and cross-shard holds remain.'})
save('review.json',{'schema_version':'1.0','reviewer':'/root/vitamins','author':'/root/inorganics','independence':'Different agent authored the selected inorganic packet; no author edits made by this reviewer. Own VM work excluded.','started_at':'2026-11-08T07:35:35+00:00','finished_at':now,'status':'complete','verdict':'pass_with_limitations','full_payload_review':True,'case_ids':[d['case_id'] for d in D],'proposal_ids':[p['proposal_id'] for p in P],'case_hashes':case_hashes,'payload_hashes':payload_hashes,'input_hashes':input_hashes,'contract_hashes':contracts,'case_reviews':case_reviews,'proposal_reviews':proposal_reviews,'open_blocking_findings':[],'scientific_scope':'All80 final cases and35 whole selected payloads, including unchanged10; quantities, forms, salt/hydrate boundaries, aliases, component references, source completeness, mapping evidence categories and full histories.','limitations':limitations,'supporting_receipts':{n:{'path':str((O/n).relative_to(R)),'sha256':h(O/n)} for n in ['source-read-ledger.json','independent-checks.json','findings.json','beforeimage-comparison.json']}})
(O/'HANDOFF.md').write_text('# Independent inorganic review — issue1227\n\nComplete authorship-separated review of all80 assigned cases and35 entire selected payloads, including12 original beforeimages and all151 relevant primary/ontology capture paths. No newly confirmed blocker. Every case and proposal has an individual appraisal in review.json.\n\nThe bounded inorganic corrections are supported with all existing source, native, role and export holds preserved. W03 shared phosphate and W05 Tris remain coordinator dependencies; no competing owner or merge is approved. Proposed nested-stock/DI references require joint integration. Native validation is separately required at final assembly.\n\nReview SHA256: '+h(O/'review.json')+'\n\nThe immutable source ledger records actual captured-content reads, exact identical-byte reuse, failed requests, and the two retained PDF pages inspected. It does not claim full-paper access or treat hash verification as scientific review.\n')
save('completion.json',{'status':'complete','finished_at':now,'case_count':len(D),'proposal_count':len(P),'primary_capture_paths':len(source_rows),'checks_passed':len(checks),'files':{n:h(O/n) for n in ['review.json','findings.json','source-read-ledger.json','independent-checks.json','HANDOFF.md']}})
print(json.dumps({'review_sha256':h(O/'review.json'),'completion_sha256':h(O/'completion.json'),'checks':len(checks),'captures':len(source_rows)}))
