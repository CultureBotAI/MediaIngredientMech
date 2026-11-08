from pathlib import Path
import json,hashlib,datetime,yaml
O=Path('reports/all_unmatched_20261107/worker-02');S=O/'continuation-1201-v1';A=S/'a';R=A/'review-c';SRC=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
L=lambda p:json.loads(p.read_text());H=lambda b:hashlib.sha256(b).hexdigest();CAN=lambda o:H(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode());now=datetime.datetime.now(datetime.timezone.utc).isoformat()
notes=L(R/'scientific_notes.json');resolved={
'142':'Resolved on exact successor: personally inspected government inventory entry11389 (polycarbonate diol, carbonate polymer of1,6-hexanediol, CAS61630-98-6), the supplier PHC-diol declaration and original DSMZ885/ingredient812 source CAS. These corroborate the registry at polymer scope; no fixed chain length, end-group structure, grade equality or emulsion identity is imported. Exact C v2 payload uses CAS primary and broader CHEBI61433.',
'159':'Resolved with new exact successor: personally checked EPA2020-14401 listing magnesium sulfate hexahydrate CAS17830-18-1 separately from adjacent hydrates, plus AmericanElements explicit MgSO4·6H2O datasheet. The final proposal promotes the existing local primary to that CAS, retains broader CHEBI32599, original six-water formula and rejected sibling-hydrate labels, and imports neither anhydrous structure nor supplier melting point.',
'169':'Resolved by adverse evidence rather than invented promotion: the suggested AlphaChem SDS was not successfully retrieved; actual captured Jinan Shenghe supplier page associates139939-75-6 with magnesium sulfate anhydrous. The internally inconsistent lead does not verify Mn seven-water CAS. Retaining the already distinct local seven-water identity is justified; no anhydrous or variable-hydrate collapse follows.',
'171':'Resolved on exact v2 payload: all five related-synonym tokens, including the enumerated (5) Sodium metasilicate, are REJECTED_LABEL with source/history retained. The exact IUPAC assertion for disodium oxosilanediolate is distinguishable from a merely related synonym. Existing hydrate-specific and generic-silicate source holds remain.',
'175':'Resolved on same exact v2 five-token correction; generic Na-silicate source is still not assigned an unstated modulus, hydrate, formulation or vendor. Worker03 separate hydrate obligations remain.',
'185':'Resolved in final decision: source CAS12439-96-2 versus maintained owner14708-82-8 is explicitly retained as a mismatch. The literal five-water target and bounded stock/bare-alias rejections are supported; the review does not silently treat all source annotations as agreeing.'}
finalnotes={k:v+(' '+resolved[k] if k in resolved else '') for k,v in notes.items()};(R/'scientific_notes_final.json').write_text(json.dumps(finalnotes,indent=2,ensure_ascii=False)+'\n')
findings=[{'finding_id':'a2-review-c-'+k,'case_index':int(k),'initial_finding':notes[k],'status':'resolved','disposition':v,'re_reviewed_at':now} for k,v in resolved.items()]
D=L(S/'c/decisions.json')['decisions'];P=L(S/'c/proposals.json')['proposals'];C={c['case_id']:(i+130,c) for i,c in enumerate(L(Path('.temp/all-unmatched-worker-02/cases-c.json')))};E={e['evidence_id']:e for e in L(O/'evidence.json')['evidence']}
for team in 'abc':E.update({e['evidence_id']:e for e in L(S/team/'evidence.json')['evidence']})
manifest={};errors=[]
def bind(root,path,expected=None):
 p={'artifact':O,'source':SRC,'mim':Path('.')}[root]/path;b=p.read_bytes();h=H(b);manifest[(root,path)]={'root':root,'path':path,'sha256':h}
 if expected is not None and h!=expected:errors.append({'path':path,'expected':expected,'actual':h})
 return b
def capt(cp):return bind(cp['root'],cp['path'],cp['sha256'])
for n in ['decisions.json','evidence.json','proposals.json','reassessments.json','owner-lookup.json','primary-integrity.json']:bind('artifact',f'continuation-1201-v1/c/{n}')
for n in ['read-and-integrity-receipt.json','primary-cas-challenges.json','scientific_notes.json','scientific_notes_final.json','phc-government-inventory.txt','mg6-epa.txt','bd-emjh-manual.txt','dsmz-1113.txt','dsmz-399.txt','dsmz-492.txt','dsmz-498.txt']:bind('artifact',f'continuation-1201-v1/a/review-c/{n}')
case_reviews=[]
for d in D:
 idx,c=C[d['case_id']]
 if idx==151:continue
 assert str(idx) in finalnotes and CAN(c)==d['case_input_sha256']
 for eid in d['evidence_ids']:capt(E[eid]['capture'])
 for o in d['owner_records']:bind('mim',o['path'],o['sha256'])
 for occ in c.get('occurrences',[]):bind('source',occ['full_recipe_snapshot'],occ.get('source_file_sha256'))
 case_reviews.append({'case_id':d['case_id'],'case_index':idx,'case_input_sha256':d['case_input_sha256'],'decision_canonical_sha256':CAN(d),'status':'approve','reasoning':finalnotes[str(idx)]+' Approval is for this source-bound successor and cited isolated payload scope, with every inherited publication/owner/quantity/dependency hold retained.','inspected_evidence_ids':d['evidence_ids']})
assert len(case_reviews)==45
proposalreviews=[]
for p in P:
 rec=yaml.safe_load(capt(p['after_capture']))
 if p['kind']=='edit_existing_owner':before=yaml.safe_load(bind('mim',p['owner_path'],p['before_sha256']));assert rec['curation_history'][:len(before.get('curation_history',[]))]==before.get('curation_history',[])
 for eid in p['evidence_ids']:
  if eid in E:capt(E[eid]['capture'])
 cases=[x for x in case_reviews if x['case_id'] in p['case_ids']];reason=' '.join(x['reasoning'] for x in cases)
 assert reason,p['proposal_id']
 if p['proposal_id']=='c2-proposal-mohr-stock-aliases':reason+=' This approval covers only the C-authored three-stock-alias rejection against its declared baseline. It does not approve the future root-composed Mohr payload or prior A/B additions; root has assigned a fresh reviewer for those combined bytes.'
 proposalreviews.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'status':'approve','reasoning':reason,'inspected_evidence_ids':p['evidence_ids']})
assert not errors,errors
receipt={'schema_version':1,'reviewer':'/root/research_a','primary_author_reviewed':'/root/research_c','reviewed_at':now,'scope':'Independent scientific review of all45 C-authored successor cases excluding C151 and all16 C-authored isolated proposals. C151 is excluded because it links the reviewer-authored Mn-variable proposal; B is its independent reviewer. Root-composed shared-owner payloads are outside this receipt.','input_hash_manifest':list(manifest.values()),'case_reviews':case_reviews,'proposal_reviews':proposalreviews,'findings':findings,'independence_statement':'I authored no reviewed C proposal. I independently inspected full frozen case context, referenced primary/ontology captures, actual owner bytes and final after payloads, pursued adverse CAS and synonym leads, requested the documented revisions and re-read their exact successors. No approval is inferred from author text or validation success alone.','errors':errors,'publication_authorization':False};(R/'independent-review.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
# Additional independent source-case links to the C-authored shared payloads.
manifest={};BD=L(S/'b/decisions.json')['decisions'];BC=L(Path('.temp/all-unmatched-worker-02/cases-b.json'));case_reviews=[];pselected=[]
for n in ['decisions.json','evidence.json','proposals.json','reassessments.json']:bind('artifact',f'continuation-1201-v1/b/{n}')
for n in ['decisions.json','evidence.json','proposals.json']:bind('artifact',f'continuation-1201-v1/c/{n}')
for idx in [112,117]:
 c=BC[idx-63];d=next(x for x in BD if x['case_id']==c['case_id']);assert CAN(c)==d['case_input_sha256'];assert set(d['occurrence_ids'])=={o['occurrence_id'] for o in c['occurrences']}
 for eid in d['evidence_ids']:capt(E[eid]['capture'])
 for occ in c['occurrences']:yaml.safe_load(bind('source',occ['full_recipe_snapshot'],occ['source_file_sha256']))
 for o in d['owner_records']:yaml.safe_load(bind('mim',o['path'],o['sha256']))
 p=next(x for x in P if x['proposal_id'] in d['proposal_ids']);yaml.safe_load(capt(p['after_capture']))
 for eid in p['evidence_ids']:capt(E[eid]['capture'])
 if idx==112:reason='Personally inspected both complete frozen recipes, successful TOGO provider records and original NBRC1004/1390 ingredient tables. Both explicitly name desiccated ox bile at8g input, while their other ingredients differ. The C-authored promotion preserves this dried biological material using a local identity with broader ox-bile grounding and does not assign a manufacturer, commercial grade, chemical composition or whole-medium equality. Actual Desicatted_Ox-bile, Ox-bile and Oxgall candidates were inspected; no merge is approved.'
 else:
  assert '100 G_PER_L' in d['reasoning'] or '100G_PER_L' in d['reasoning'] or '100 G_PER_L' in d['applicability']
  reason='Personally inspected all three complete frozen recipes, DSMZ1113 primary PDF and MediaDive2234 source JSON. Original source distinguishes100ml EMJH enrichment from2.3g EMJH base. Frozen derivatives instead carry100 G_PER_L twice and100 PERCENT_V_V once; the final corrected decision explicitly retains those quantity conflicts. Manufacturer-authored Difco/BBL manual supports albumin/Tween80 plus unspecified growth factors, so the C-authored enrichment with PARTIAL composition is supported without albumin species, component amounts, exact historical vendor-version equality or whole-base conflation.'
 case_reviews.append({'case_id':d['case_id'],'case_index':idx,'case_input_sha256':d['case_input_sha256'],'decision_canonical_sha256':CAN(d),'status':'approve','reasoning':reason+' All inherited source and publication holds remain.','inspected_evidence_ids':list(dict.fromkeys(d['evidence_ids']+p['evidence_ids']))});pselected.append({'proposal_id':p['proposal_id'],'after_capture':p['after_capture'],'status':'approve','reasoning':reason})
assert not errors,errors
receipt={'schema_version':1,'reviewer':'/root/research_a','reviewed_at':now,'scope':'Independent additional review of B112 and B117 linked to C-authored shared payloads; neither B source author nor C target author self-approves these links.','input_hash_manifest':list(manifest.values()),'case_reviews':case_reviews,'proposal_reviews':pselected,'findings':[{'finding_id':'a2-review-b117-quantity-source-wording','status':'resolved','initial_finding':'The earlier decision incorrectly said original and frozen derivatives all specify100ml; frozen units instead conflict.','disposition':'Final wording separates original DSMZ100ml from two frozen100G_PER_L and one100PERCENT_V_V assertions, retaining all quantity holds. Exact corrected decision and shared after bytes are hash-bound here.','re_reviewed_at':now}],'errors':errors,'publication_authorization':False};(R/'independent-review-b112-b117.json').write_text(json.dumps(receipt,indent=2,ensure_ascii=False)+'\n')
print('C independent45cases16proposals; Bshared2cases2payloads; nohasherrors')
