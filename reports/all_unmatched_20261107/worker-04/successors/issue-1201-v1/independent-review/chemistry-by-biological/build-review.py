"""Hash-bind the completed independent chemistry successor review."""
import json, hashlib, datetime, subprocess
from pathlib import Path
import yaml
S=Path(__file__).resolve().parents[2]
W=S.parents[1]
Q=Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
canon=lambda x:hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
expected={'reassessments':'dd2461113355173a6c9b4d272613fc66784648377649d11366fccc6c41f21b66','decisions':'8e0eb9be744d10366365148ef86eb12b631a0d533db126379eb7d8e7afe327f4','evidence':'a5d2064402479d2f80f9de49ad59f20b857c8067884e6881d392448b47e8ac4f','proposals':'04ddf6b71a124d69d34da7b18904ce9d46021ec83911fb0c98ecc658fbfd190e'}
parts={}
for k,h in expected.items():
 p=S/'fragments'/f'chemistry-{k}.json';assert sha(p)==h,(k,sha(p));parts[k]=json.loads(p.read_text())[k]
A={r['index']:r for r in json.loads((S/'fragments/chemistry-assignment.json').read_text())['cases']}
E={e['evidence_id']:e for e in json.loads((W/'evidence.json').read_text())['evidence']}
assert len({e['evidence_id'] for e in parts['evidence']})==len(parts['evidence'])
E.update({e['evidence_id']:e for e in parts['evidence']})
D={d['case_id']:d for d in parts['decisions']}
notes={
4:'The titanium(III) title conflicts with the literal TiCl2 precursor in the same primary preparation. A known50ml stock volume does not resolve oxidation state; the separately published TiCl3 preparation is not evidence that this source silently meant TiCl3.',
6:'Raka-Ray supplier ingredient list and DSMZ source do not specify optical sense, hydrate or salt stoichiometry. Existing L-specific potassium-glutamate monohydrate cannot be selected from the generic wording. This is a reagent identity gap, not an unperformed owner lookup.',
10:'The JCM401 primary PDF identifies a5mM quinic-acid addition. The isolated partial stock preserves this concentration and leaves solvent and optical sense unspecified. Its receiving-medium volume discrepancy does not determine stock composition and remains separate.',
13:'All13 frozen occurrence contexts remain heterogeneous. A metabolic-model dicitrate mnemonic does not prove the physical ferric reagent, ligand ratio, counterions or a shared stock across papers. Lovley evidence cannot be transferred to every modeled row.',
19:'The BSK source Na-citrate lacks sodium count/hydration. Mono-, di- and trisodium owners do not supply missing procurement evidence. Holding this case avoids turning a generic salt token into a selected ionic composition.',
27:'Full owner bytes confirm one CHEBI64758 record is REJECTED and the active survivor has corrected CAS6381-92-6. CCAP TAP explicitly establishes disodium dihydrate; selecting that existing identity for the occurrence needs no new global truncated alias or duplicate-owner merge.',
30:'DSMZ878 supplies a0.01M Fe-citrate stock and0.5ml receiving dose. Partial stock identity and literal concentration are supportable while iron valence/ligand ratio and solvent remain ungrounded; no chemical mass or final-medium concentration is fabricated.',
31:'ICSC1220 explicitly verifies CAS6858-44-2 and five waters. I challenged the claimed second FAO/JECFA corroboration because that source says pentahemihydrate; final wording corrects it. The CAS primary owner remains separate from the anhydrous parent, with asymmetric grounding only.',
32:'The primary NBRC formula itself has Mo7O4. Chemically incompatible oxygen count cannot be normalized by choosing a familiar heptamolybdate tetrahydrate owner. An authoritative formula correction is a real missing fact.',
47:'I challenged the draft one-sodium formula/monosodium parent because JCM904 gives neither sodium stoichiometry nor optical sense. Final payload is withdrawn. Full issue655 and existing L-specific owner history were checked: lexical alias advice and automated CAS lookup do not supply a source-specific reagent specification. The established one-water qualifier is retained.',
54:'Literal (NH4)6(MO7)24 has unresolved element capitalization, grouping and oxygen count. No source-defined molecular form can be safely minted from this token without a correction; registry naming would conceal rather than resolve the ambiguity.',
59:'The primary NBRC recipes consistently state Na2WO4·H2O. Preserving that stated one-water form with registry identity and a broader sodium-tungstate anchor is supportable without claiming a measured crystal phase. The common dihydrate is not silently substituted.',
60:'Existing UNMAPPED0852 already preserves the trihydrate boundary under#882/#1021. Promotion retains that original owner/history, rather than duplicates it. DSMZ661 explicit three waters support the source-form identity; PubChem and failed RSC attempts do not become independent procurement proof.',
62:'Lee2009 Table4 row13 contains L-glutamic acid, and AAM-minus omits it. This contradicts the corresponding D-glutamate row. The separate Klein1979 source cases remain unresolved after the documented retrieval limit; no cross-paper stereo correction is inferred.',
63:'The named20mM stock preparation is recoverable, but the alpha-ketoglutamate name and sodium-bearing heading fail to identify the solute. Recording the preparation candidate without asserting an exact chemical stock is justified; receiving dose and storage facts do not solve chemistry.',
73:'CCAP Waris-H independently specifies Na2EDTA·2H2O. The active64758 owner is known and the apparent duplicate is a tombstone. Bounded source binding is justified while KG sodium-unspecified and hydrate-conflicted rows remain separate.',
80:'Visually inspected original1985 page3331: NaCl0.2g is printed in the S-medium paragraph, though PDF text extraction omits that row. This verifies the occurrence-level NaCI transcription correction. Retaining the typo only as source provenance avoids a global malformed alias.',
87:'The primary ammonium-tartrate wording does not select one/two ammonium ions or tartrate stereochemistry. Supplier examples for diammonium L-tartrate are not source-specific identity evidence. The retained requirement is concrete.',
90:'The source names myo-inositol with a misleading B7 annotation and separately lists biotin. Selecting myo-inositol for this occurrence is justified by its chemical name; no vitamin-number synonym or functional role is added.',
95:'Fe-Citrate in the anaerobic RM source leaves oxidation state, ratio/counterions and hydrate unresolved. Medium redox conditions do not prove the bottle identity. Retrieving the source again does not justify choosing a ferric or ferrous owner.',
102:'JCM713 itself carries the Mo7O7 formula. Other well-defined trace salts and the common tetrahydrate do not authorize replacing O7 with O24. The remaining formula conflict is substantive.',
107:'DSMZ863 NaWO4·6H2O conflicts with the two-sodium frozen/ingredient spelling. This positive primary disagreement differs from the coherent one-water source assertions in59. Holding sodium count and hydrate identity is appropriate.',
119:'NBRC943 explicitly states the chemically coherent six-ammonium/heptamolybdate/two-water formula. Registry preservation of the source assertion does not claim crystallographic validation. Final CHEBI35505 hydrate is a verified broad class only; no exact tetrahydrate86244 or orthomolybdate relation is asserted.',
120:'The source separately describes578mg/L FeNaEDTA stock and1.5mM. Keeping the stated mass concentration in a partial stock avoids inferring hydration from correlated arithmetic. The final-medium5ml dose and malformed frozen578g/L remain separate.',
125:'Primary DSMZ1005 disodium wording contradicts TOGO trisodium wording. The unrelated reviewed Na3-edta proposal cannot repair this source-specific disagreement. No extension of its resolving alias is allowed.',
126:'The50mM Tris-HC1/pH7.6 text describes the complete medium. It does not establish a separately prepared50mM stock, its solvent or acid/base recipe. Retaining a precise supplied-preparation gap avoids inventing an isolated buffer.',
132:'Existing source-compatible disodium-fumarate owner was actually checked. No missing identity/alias work remains for this bounded input, and no full-owner publication hold is cleared.',
138:'Source706 conflicts internally between the disodium label and trisodium metadata. The trisodium owner already rejects Na2-citrate. Related penta/trihydrate proposals cannot select sodium count for this source.',
139:'This duplicate KG source shares the real DSMZ863 sodium-count conflict with107. Common dihydrate and automatic metadata do not establish the six-water reagent; neither source is silently promoted.',
147:'The existing diammonium hydrogen-citrate owner matches the source-compatible ammonium-citrate claim in the prior reviewed evidence. Fresh lookup finds no additional authorized delta; the existing full-payload/source holds persist.',
148:'The KG penta-form and CultureMech31 are correctly backlinked to one CAS6858-44-2 proposal. Five-water ICSC evidence is retained; JECFA pentahemihydrate is explicitly excluded as corroboration.',
150:'The KG trihydrate joins60 on the original UNMAPPED0852 owner, preserving both case links and the original beforehash. No duplicate record or dihydrate collapse is introduced.',
151:'The source sodium-laurate identity already has a compatible existing owner. No new owner, speculative form, alias or role follows from reopening the cohort.',
154:'The Ardacin placeholders and prior primary discovery do not connect ardacinB to a verified product/structure. Duplicating the lexical placeholder with a registry name would not complete chemistry; the specific missing primary identity remains stated.',
157:'Independently inspected DSMZ354: it says only Mg-citrate. MediaDive404 CAS/formula and computed mass↔molarity are correlated enrichment, not independent physical-reagent proof. The new CHEBI131389 owner denotes the independently ontology-defined1:1 candidate only. Rejecting global Mg-citrate as its alias, leaving the3:2 owner unchanged, and withholding five-occurrence reassignment are essential acceptance limits; no source404 procurement identity is approved.',
159:'The source pentahydrate label conflicts with anhydrous CAS/mass. Unlike consistent source-stated hydrates, this case contains direct contradictory identity evidence. Neither a speculative pentahydrate nor automatic anhydrous normalization resolves it.',
162:'The1955 bibliographic record does not define the graph source product or verified structure. Original full isolation/product evidence is still missing; no griseofulvin substitution or duplicate lexical owner is justified.',
169:'The prior duplicate-owner consolidation prerequisite is withdrawn correctly after reading the tombstone. Ingredient676 still conflicts between dihydrate label and anhydrous CAS/mass; CCAP source evidence cannot globally repair that independent record.',
170:'The complete acid owner history records a prior typo merge, not proof that source2384 supplied the acid rather than a salt/anion. Changing only the ambiguous global alias to REJECTED_LABEL is justified; history and unrelated roles are retained.',
172:'The compatible existing HEPES identity and spelling were checked. No duplicate compound or new generic stock follows; the separate published HEPES-NaOH stock retains its own scope.',
174:'Original Welsch1947 pages distinguish actinomycetin as crude culture filtrate potentially containing multiple agents. Correcting only ingredient_type to UNDEFINED_MIXTURE is supported. The placeholder identity and unresolved exact preparation remain; no pure antibiotic structure is invented.',
175:'The second EDTA label lacks sodium count and conflicts with automatic anhydrous metadata. The rejected duplicate owner does not create a real merge prerequisite, but removing that prerequisite does not resolve the source identity.',
184:'The independent actinomycetin source case is retained on the same narrow type-correction proposal as174. Historical filtrate evidence supports mixture classification, not exact product/formulation identity or an unreviewed source release.',
186:'Existing disodium fumarate identity already supports this explicit two-sodium source. Fresh catalog/proposal comparisons justify no additional material edit and preserve all existing publication limitations.'}
assert set(notes)==set(A)
checked={};case_reviews=[]
for r in parts['reassessments']:
 n=r['index'];a=A[n];old=a['published_decision'];cid=r['case_id'];assert cid==old['case_id']
 assert r['predecessor_decision_sha256']==canon(old)
 active=D.get(cid,old)
 for k in ['case_id','case_input_sha256','source','occurrence_ids']:
  assert active[k]==old[k],(cid,k)
 for k in old:
  if 'hold' in k:assert active.get(k)==old[k],(cid,k)
 for eid in r['evidence_ids']:
  e=E[eid];p=(W if e['capture']['root']=='artifact' else Q)/e['capture']['path'];assert sha(p)==e['capture']['sha256'],eid
  checked[str(p)]={'path':str(p),'sha256':sha(p)}
 case_reviews.append({'index':n,'case_id':cid,'status':'accepted_narrow_scope','scientific_review':notes[n],'reassessment_sha256':canon(r),'predecessor_decision_sha256':canon(old),'changed_decision_sha256':canon(D[cid]) if cid in D else None,'evidence_ids_reviewed':r['evidence_ids'],'proposal_ids_reviewed':r['proposal_ids']})
payload_reviews=[]
for p in parts['proposals']:
 path=W/p['after_capture']['path'];assert sha(path)==p['after_capture']['sha256'];after=yaml.safe_load(path.read_text())
 if p['before_sha256']:
  before=subprocess.check_output(['git','show','e000d66dd26ab053e9b17ce7bf8d3c873c3dde99:'+p['owner_path']]);assert hashlib.sha256(before).hexdigest()==p['before_sha256'];old=yaml.safe_load(before)
  for k in ['nutritional_roles','physicochemical_roles','biological_roles']:
   assert after.get(k)==old.get(k),(p['proposal_id'],k)
 payload_reviews.append({'proposal_id':p['proposal_id'],'path':p['after_capture']['path'],'sha256':sha(path),'full_payload_read':True,'before_sha256':p['before_sha256'],'scope':'Complete proposed bytes read; scientific acceptance is restricted to the described delta/source scope. Unchanged owner assertions and release holds are not independently approved.'})
assert len(payload_reviews)==10 and len(case_reviews)==44
review={'schema_version':1,'reviewer':'Codex /root/biological','primary_author':'Codex /root/chemistry','independence':'Separate primary author and skeptical reviewer. Reviewer did not edit chemistry decisions, evidence or proposed owner payloads.','reviewed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'complete','scientific_disposition':'accepted_narrow_scope','unresolved_blocking_findings':[],'scope':{'reassessments':44,'changed_decisions':22,'payloads':10,'sampled':False},'reviewed_fragment_hashes':{f'fragments/chemistry-{k}.json':v for k,v in expected.items()},'case_reviews':case_reviews,'payload_reviews':payload_reviews,'capture_checks':{'unique_paths':len(checked),'all_hashes_valid':True,'bindings':list(checked.values())},'resolved_challenges':[{'case_ids':[47],'finding':'Draft monosodium formula/parent added unsupported sodium stoichiometry; issue655 also required explicit reconciliation.','resolution':'Final draft withdrawn, final no-payload decision retains one-water source fact and precise sodium/stereo gaps; complete issue/history reconciliation recorded.'},{'case_ids':[31,148],'finding':'JECFA was incorrectly claimed to corroborate pentahydrate although its text says pentahemihydrate.','resolution':'Final payload/decisions distinguish the forms and rely on ICSC1220 for the five-water CAS identity.'},{'case_ids':[10],'finding':'Convenience primary-source URL did not identify the actual recovered J401 capture.','resolution':'Final payload cites the exact recovered bacmedia J401 endpoint.'},{'case_ids':[157],'finding':'MediaDive CAS/formula/computed molarity are correlated metadata and cannot prove physical reagent identity or reassignment of five historical occurrences.','resolution':'Final candidate owner remains ontology-defined1:1 only, no global Mg-citrate alias, no old3:2 regrounding and no occurrence reassignment; source hold explicitly retained.'},{'case_ids':[119],'finding':'Distinct tetrahydrate cannot serve as exact identity for source-stated dihydrate.','resolution':'Final registry identity retains two waters and uses only asymmetric verified general hydrate35505 anchor.'}],'visual_source_check':{'path':str((S/'independent-review/chemistry-by-biological/s-medium-1985-p1.png').relative_to(W)),'sha256':sha(S/'independent-review/chemistry-by-biological/s-medium-1985-p1.png'),'finding':'Original page3331 visibly includes NaCl0.2g; plain PDF text extraction omitted that line.'},'limitations':['No whole-owner publication, source-selector release, role approval, maintained data change, or downstream rebuild is approved.','Existing source-specific holds remain. Registry preservation of coherent stated forms does not certify supplier identity or measured crystal phases.','Unchanged original source evidence was checked against retained hashes and prior independent review; no fresh remote retrieval time is fabricated.']}
out=S/'independent-review/chemistry-reviewed-by-biological-v1.json';assert not out.exists();out.write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'receipt':str(out),'sha256':sha(out),'cases':len(case_reviews),'payloads':len(payload_reviews),'capture_paths':len(checked)}))
