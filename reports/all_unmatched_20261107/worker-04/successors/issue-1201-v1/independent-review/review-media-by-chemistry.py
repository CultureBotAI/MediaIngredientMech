import datetime,hashlib,json
from pathlib import Path
import yaml
from mediaingredientmech.validation.write_validated import validate_ingredient
B=Path('reports/all_unmatched_20261107/worker-04');S=B/'successors/issue-1201-v1'
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def sh(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def dg(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def read(name,key):return json.loads((S/'fragments'/('media-'+name+'.json')).read_text())[key]
R=read('reassessments','reassessments');D=read('decisions','decisions');P=read('proposals','proposals');E=read('evidence','evidence')
olde=json.loads((B/'evidence.json').read_text())['evidence'];emap={x['evidence_id']:x for x in olde+E}
oldcases=json.loads((B/'fragments/media-assignment.json').read_text())['cases']
caseindex={x['case_id']:i for i,x in oldcases.items()} if isinstance(oldcases,dict) else {}
# Original assignment contains explicit index wrappers in some revisions.
if isinstance(oldcases,list):
 for x in oldcases:
  if 'case_id' in x:caseindex[x['case_id']]=x.get('index')
  elif 'case' in x:caseindex[x['case']['case_id']]=x['index']
caseindex.update({x['case_id']:x['case_index'] for x in R})
notes={
0:'Compared primary M2964 10x-with-glutamine source with original DSMZ403 historical042-1545 product and current21540 comparator. An additional source-qualified owner would not establish a distinct substance; unknown product/preparation and possible overlap justify the explicit hold. Case36 alone has the catalogue binding.',
7:'Three source recipes add blood or yeast/NAD/hemin separately to Columbia base. The original sources do not specify a common vendor/base formula, while the published OxoidCM0331 has a distinct formula. Hold avoids choosing one product across heterogeneous basal occurrences.',
8:'Original ATCC1047/957 explicitly says Noble(Difco0142), independently supported by the historical0142-01-8 study. Grade binding is supported; no0142→214220 packaging-equivalence claim is needed. Case121 remains excluded.',
21:'Read primary JCM1305: one OxoidSkirrow vial is reconstituted with2ml sterile purified water;0.4ml is receiving dose. Partial stock asserts the two inputs only, without importing modernSR0069 catalogue or full Helicobacter composition.',
36:'Original DSMZ403 explicitly prints GIBCO042-1545. Root cross-shard lookup exposed existingCMRL_1066 owner/source1680 with this catalogue in its source attribute. Final must reuse that owner and flag worker07; new duplicate would fail identity exclusivity. Slash/glutamine wording remains source text, not invented quantitative composition.',
51:'Original TOGOM2852 quotation identifies OxoidWilkins-Chalgren agar plates before blood/antibiotic supplementation. Prepared plate material is bounded; no dryCM0619 formula or unknown historical catalogue is substituted.',
57:'DSMZ1144 says Difco agar-agar without grade. The existence of Bacto and Noble supplier grades makes manufacturer alone insufficient; this is a real source-grade distinction, not deferred owner lookup.',
67:'Read DSMZ840 original: BBL4354005 Columbia plates with5%sheep blood are one alternative to Trypticase soy plates. Proposal retains finished blood-containing product-family boundary and does not absorb the alternative.',
71:'Read NBRC1365: ready-to-use BD-BBL Columbia5%sheep blood. Supports the same named supplier/product family as67 without claiming lot-equivalent formulations or catalogue succession.',
84:'Read all four occurrence contexts and raw P1 washing instruction (600ml water, settle/remove overlay, repeat twice, final wet volume<300ml). Three unwashed grade occurrences and one washed preparation require distinct bindings. No has-part edge or retained wash-water mass is inferred.',
86:'Chocolate-agar ontology represents the general heated-blood medium class. TOGOM2975 adds IsoVitaleX separately; source annotation to existing owner is appropriate, without new duplicate, supplier assertion or supplement incorporation.',
96:'NBRC1116 gives OxoidL28 only as an example of purified agar. A generic purification adjective does not select that product, Noble or another exact mixture. Missing selected product/grade criteria is a real source gap.',
99:'Independently read full NBRC1096. The source-defined family expressly permits natural aged OR DaigoSP seawater and optional agar. Only invariant inputs7.5gMarineBroth,5gpyruvate,200mlwater are unconditional components; branch quantities800ml/15g remain notes. Phenanthrene51mg and ethanol6ml belong to overlay, not this base. Family scope is honest and does not claim one exact composition.',
109:'NBRC1326 explicitly qualifies agarose as electrophoresis grade. Generic polymer identity2511 is retained with supplied-form note; supplier/gel strength/EEO unspecified. Narrow annotation is supported. Inherited Sepharose and non-name aliases and roles remain complete-owner release concerns, not newly reviewed claims.',
111:'TOGOM2850 identifies prepared Bordet-Gengou before sheep blood but no supplier/formula. Existing Difco438 preparation and dry248200 product cannot be selected from that text. Hold preserves the unproven equivalence rather than inventing a second potentially identical source-labelled substance.',
113:'Original CCAPMY75S is biphasic. Thoroughly disperse the agar in cold is a preparation instruction, not an ingredient. The required source repair is full phase/stock reconstruction, not a new owner or simple token deletion.',
117:'TOGOM2942 primary unit is1L prepared Mueller-Hinton agar; frozen1g/L is a separate conversion error. New source-qualified prepared material stays distinct from dryMHII product; atmosphere is not composition, and no generic ontology formula is borrowed.',
121:'Original ATCC1962 itself combines Noble wording with BD214050, which manufacturer evidence identifies as Bacto. Conflicting original claims justify hold; authenticated old0142 Noble cannot resolve it.',
131:'Primary finder→JCM418→JCM13 chain is explicit. Independently checked15main-batch inputs and subordinate-stock notes against full JCM13; quantities match. Horse blood makes this a finished formulation rather than Nissui dry BL product. Generic old alias remains provenance only.',
133:'Primary finder→JCM76→JCM26 chain is explicit. Checked all10batch inputs; extra50gNaCl belongs to JCM76 receiving medium and is excluded.1Lwater is an input, not an assumed final volume.',
142:'JCM119 explicitly uses37gBD-DifcoBCYE agar,100mlLegionella enrichment and900mlwater. Dry basal product is distinct from enrichment and finished medium. Failed manufacturer insert retrieval is acknowledged; source supplier/product boundary remains adequate.',
156:'DSMZ1775/source2177 distinguishes31.5g dry DG18 base from220g added glycerol. Existing imported owner can preserve that opaque named base; no vendor or formula is imposed from Oxoid/Merck comparators.',
173:'Read original DSMZ438: title explicitly saysDIFCO and separate15%horse blood. Source2112 measures1000mlprepared base, distinct from dry product98 and sheep-blood111. Existing imported owner can be narrowed with historical aliases retained as provenance.',
176:'Primary finder702 is pooled acrossBD-Difco JCM150/220,Nissui1329 andOxoidCM103 DSMZ831; equal17g doses do not establish equivalence. Frozen KG record lacks occurrence ID selecting one. Hold is justified even though supplier-specific candidates exist.',
177:'Primary finder→JCM51→JCM50 chain is explicit. Full JCM50 heats20goatmeal, filters and restores infusion1L before1mltrace stock and18gagar. Payload correctly asserts filtered infusion rather than20g retained whole oats; no dry-vendor identity borrowed.',
183:'Read DSMZ585: OxoidCYEbase plus BCYEsupplement is one commercial alternative; scratch ACES recipe is another. Source2125 names the combined system in1000ml. Two qualitative components with unknown amounts are appropriate; no scratch amounts or exact supplement catalogue inferred.'}
extra={65:'Original JCM905/906 explicitBD-DifcoBacto grade remains supported; revised binding must describe84 unwashed subset while excludingP1washed subset. No global rawBacto alias or implicit release.',92:'Original M460-derived BactoBD-Difco conditional solidifier remains same grade; condition belongs to recipe. Superseding proposal retains this case and correctly separates washedP1.',89:'Existing Noble grade proposal remains supported by its supplier-qualified source. Successor adds0142 case8 without changing substance scope or resolving contradictory214050 case121.',123:'Supplier-qualified Noble source remains bound to same grade; new0142 evidence supports family continuity without a catalogue replacement claim. Inherited holds retained.'}
notebyid={}
for r in R:notebyid[r['case_id']]=notes[r['case_index']]
for d in D:
 if d['case_id'] not in notebyid:
  # These four predecessor bindings are uniquely identified by their original evidence IDs.
  inds=[int(e.rsplit('-',1)[1]) for e in d['evidence_ids'] if e.startswith('media-case-')]
  n=next(i for i in inds if i in extra);caseindex[d['case_id']]=n;notebyid[d['case_id']]=extra[n]
capture_results={};ids=set()
for x in R+D+P:ids.update(x.get('evidence_ids',[]))
for eid in ids:
 e=emap[eid];c=e.get('capture')
 if not c:continue
 p=(B if c['root']=='artifact' else Q)/c['path'];assert sh(p)==c['sha256'],(eid,p)
 capture_results[str(p)]={'evidence_id':eid,'capture':c,'verified':True}
pr=[]
for p in P:
 f=B/p['after_capture']['path'];assert sh(f)==p['after_capture']['sha256'];r=yaml.safe_load(f.read_text());assert not validate_ingredient(r)
 before=None
 if p['before_sha256']:
  assert sh(p['owner_path'])==p['before_sha256'];before=yaml.safe_load(Path(p['owner_path']).read_text())
  if before.get('mapping_status')!=r.get('mapping_status'):
   last=r['curation_history'][-1];assert last.get('previous_status')==before['mapping_status'] and last.get('new_status')==r['mapping_status'],p['proposal_id']
  for k in set(before)|set(r):
   if 'role' in k:assert before.get(k)==r.get(k),(p['proposal_id'],k)
 if 'gibco_042_1545' in p['proposal_id']:assert p['kind']=='edit_existing_owner' and p['owner_path'].endswith('/CMRL_1066.yaml'),p
 pr.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'before_sha256':p['before_sha256'],'status':'accepted_narrow_delta_only','case_ids':p['case_ids'],'review_notes':[notebyid[c] for c in p['case_ids'] if c in notebyid],'closed_schema':'PASS','no_role_mutation':True,'whole_payload_publication':'WITHHELD pending all inherited owner/source/export obligations'})
allcases={r['case_id']:r for r in R};allcases.update({d['case_id']:d for d in D});dmap={d['case_id']:d for d in D};rmap={r['case_id']:r for r in R}
case_reviews=[]
for cid in sorted(allcases,key=lambda c:caseindex.get(c,999)):
 case_reviews.append({'case_id':cid,'case_index':caseindex.get(cid),'status':'accepted_with_stated_scientific_limits','review_notes':notebyid[cid],'decision_sha256':dg(dmap[cid]) if cid in dmap else None,'reassessment_sha256':dg(rmap[cid]) if cid in rmap else None,'proposal_ids':allcases[cid].get('proposal_ids',[]),'no_global_hold_release':True})
out={'status':'complete','scientific_disposition':'accepted_narrow_scope','reviewer':'worker04/chemistry; independent of media primary author','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All26 successor reassessments, all30 changed full decisions including4 predecessor bindings, all18 exact proposed payloads. Scientific review and narrow delta only; no complete owner/export release.','reviewed_fragment_hashes':{'fragments/media-'+k+'.json':sh(S/'fragments'/('media-'+k+'.json')) for k in ['reassessments','decisions','evidence','proposals']},'case_reviews':case_reviews,'proposal_reviews':pr,'capture_integrity':{'unique_capture_paths':len(capture_results),'status':'PASS','captures':list(capture_results.values())},'findings':[{'id':'MEDIA-I1201-CHEM-F1','severity':'material provenance correction','finding':'Existing-owner status promotions omitted explicit transition and used CREATED.','status':'resolved','resolution':'Final existing-owner payloads checked for previous_status/new_status against exact before bytes.'},{'id':'MEDIA-I1201-CHEM-F2','severity':'identity duplication','finding':'Root cross-shard trace identified existingCMRL_1066/source1680 with exactGibco042-1545 attribute. New owner would duplicate a known source identity.','status':'resolved','resolution':'Final36 proposal reuses exact existing owner; worker07 dependency flagged;0 retains identity hold.'},{'id':'MEDIA-I1201-CHEM-F3','severity':'source applicability clarification','finding':'Superseding Bacto65/92 wording retained stale blanket84 exclusion;84 needed occurrence-level distinction.','status':'resolved','resolution':'Final case text and exact occurrence bindings distinguish unwashed grade from washedP1.'}],'preserved_release_limits':['Existing agarose non-name/Sepharose aliases and inferred roles are not scientifically approved by a supplied-form annotation.','All inherited source/publication holds remain.','Source-family alternatives such asNBRC1096 do not establish one exact composition or cross-product equivalence.','CMRL source0 and worker07 overlap require coordinator reconciliation; no winner selected.']}
assert len(R)==26 and len(case_reviews)==30 and len(pr)==18
out['payload_reviews']=[{'proposal_id':x['proposal_id'],'path':x['after_capture']['path'],'sha256':x['after_capture']['sha256'],'full_payload_read':True,'scientific_disposition':'accepted_narrow_scope','review_notes':x['review_notes'],'publication_disposition':x['whole_payload_publication']} for x in pr]
out['receipt_format_note']='Version3 adds explicit assembler-required payload_reviews aliases; no scientific conclusions or reviewed fragment/payload bytes changed from v2. Prior receipts remain immutable.'
p=S/'independent-review/media-reviewed-by-chemistry-v3.json';p.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');print(json.dumps({'path':str(p),'sha256':sh(p),'cases':len(case_reviews),'payloads':len(pr),'captures':len(capture_results)},indent=2))
