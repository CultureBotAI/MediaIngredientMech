"""Independent skeptical review by primary_b of primary_c's complete 48 cases.
Manual findings follow direct frozen case, owner, source and ontology reads.
"""
import json,pathlib,hashlib,datetime
R=pathlib.Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
D=json.loads((R/'parts/c-decisions.json').read_text())['decisions']
P=json.loads((R/'parts/c-proposals.json').read_text())['proposals']
E={e['evidence_id']:e for e in json.loads((R/'parts/c-evidence.json').read_text())['evidence']}
notes={
140:'DSM652 trace table explicitly has one-water wording; anhydrous CAS/API cannot silently select form. Hold is supported.',
141:'Exact frozen Bergey substrate category is a union of two sugar classes. A molecular or purchased-mixture assignment would invent scope.',
142:'Source name/formula and CAS150-90-3 candidate differ from glycoside ChEBI pointer. Keeping source conflict unresolved avoids granting inherited owner approval.',
143:'Whole-egg API has no recipe links/species. Neither200ml nor generic biological material specifies yolk or a chicken-specific identity.',
144:'DSM354 original gives20–25fresh eggs,yolk+white,one-litre mixture,external alcohol cleaning. Proposal correctly excludes alcohol; constituent-list completeness needs correction.',
145:'Supplier155322 trans structure/CAS1914-58-5 differs from generic styrylacetic/isomer claims. Existing local identity can remain while parent/source linkage awaits evidence.',
146:'35.4g Oxoid source is consistent with CM0957 but not an exact catalog witness. Contrasting explicitcatalog case181 is appropriate.',
147:'Six waters,CAS6106-21-4 andCHEBI63686 agree. Source-bound hydrate assignment does not release unrelated aliases.',
148:'JCM1105 explicitly specifies three waters and three sodium ions. The source database formula C6H8O7.3/2H2O.2Na contradicts both counts; the unresolved disposition preserves that conflict without substituting free citric acid.',
149:'DSM188 supports ferric hydrate. Current capturedDSM1053 has ferrous sulfate heptahydrate in Wolin stock, so claim both independently repeat ferric hydrate must be corrected.',
150:'DSM1740 acid parenthetical and Merck108416SDS CAS139-13-9 directly support Titriplex1. Added alias has suitable scope; existing wrongsalt aliases and literature remain separate held findings.',
151:'Unqualified cysteine-HCl has no stereo/water witness;QSY9 pointer is unrelated. No exactL assignment justified.',
152:'JCM196 original corresponding3microgram row statesNa2MoO4.2H2O, unlike source1678Na2MoO7. Source-specific correction is supported, not a globalmalformed synonym.',
153:'Supplier53588 formulaC9H20N2O6S2 and homopiperazine structure substantiate HomoPIPES,CAS202185-84-0; ordinaryPIPES remains distinct.',
154:'157.62mass and nonstereo hydrochloride label conflict with hydratedLterm91248. Hold is warranted.',
155:'DSM1617 papaic soy digest supports material class but not allsoy products or exact vegetablehydrolysate broadclass equivalence.',
156:'Independently read JCM1209 complete basalstock and comparedBpayload eightinputs. VariableMnSO4hydrate and methyleneblue remain ungrounded; sharedproposalbacklink needed.',
157:'DuchefaN0903 actual producttitle/CAS86-87-3 aligns1-naphthaleneaceticacidCHEBI32918. Source spelling alone is not used as proof.',
158:'JCM788 repeatsK2HSO4; neutral ordinarysalt charge impossible. Several candidatecorrections exist, none independently selected.',
159:'DSM1560 original malformedNa2MoO7O4 row retained. Separatecorrectmolybdate in anotherstock is not sufficient correctionauthority.',
160:'JCM68010ml unquantified cysteinemonohydratestock distinct fromsolute. QSY9dye+instruction retypednonresolving, preserving rawprovenance.',
161:'Sigma72565 one-watertrisodiumformula/CAS18662-53-8 is coherent. CASprimary withbroaderanhydrous132766 andrequiredregistryrow is supported; noexactparentidentity.',
162:'DSM687 distinguishesPanton andBitone. No silent brandspellingrepair toBactoPeptone or anotherproduct.',
163:'ExplicitL/HCl/H2O,CAS7048-04-6 and175.636 agree. Duplicatedowners require coordinatedmerging independently ofsourcesupport.',
164:'JSTAGEcellostatin report namesantibiotic isolatedassulfate, but structuralidentity not established. No promotionfromnameorproducer.',
165:'SeparateGTDB-metatraits sourcerow checked;same transsupplier evidence scope as145,sourceidentity kept separate.',
166:'NativeNLM M0045998 has narrowerConceptM0045996,Lsubstrate; OLSsynonym alone cannot makegenericheadingexact.',
167:'Frozen sourceattribute gives0.1%w/v whileAPI gives sodiumsalt,CAS62758-13-8. Neutralresazurin mismatch isreal; nominalsource-qualified stockproposal should be considered rather than onlyfutureaction.',
168:'Cyanocobalamin specificCyano ligandCHEBI17439 dominates broadvitamer176843; competingowneralias mustremainheld.',
169:'DSM1560 Na-Nitrilotriacetat lacksNa stoichiometry/hydration. DatabaseautoCAS3Na doesnot independently establish orderedform.',
170:'FrozenGIBCO042-1545+10x+glutamin qualifiers distinguish historicalproduct. CurrentAPI broaderCMRLsynonyms cannot settle exactcatalogversion.',
171:'ATCCproducerdescription establishes namedetabetacin,not molecularstructure orCAS. No fabricatedidentifier.',
172:'Sodiumbenzoate sourceCAS532-32-1 agrees withsalt113455,distinctbenzoicacid.',
173:'T0647 sodiumformula/CAS91000-53-2 verifies specificsalt;freeacid191055 onlyparent. Suppliermixedsodiumpotassiumsynonym is not adopted.',
174:'Distinctmetatraits case checked against same nativeNLM narrowerstereoconcept; no falsely exact heading mapping.',
175:'DSM672 onlyDifco0003or0001 underhalfstrengthbroth/agar. Labeldoesnot chooseproductoption/catalogformulation.',
176:'Frozen source_record has10ml,7.5g/Lstock;REST2154/download lacktheseattrs. Proposalconcentration needsfrozenlocator oractualrecipe andUNKNOWN completeness.',
177:'ExplicitLlabel conflictswithracemicCAS/QSY9 sourcefields;holdpreserves contradiction instead of trusting onefield.',
178:'JCM1079 includes4initialsolutes/water plus4stocks before To complete. JCM1081/1082 expresslyreference basalprep. Proposedboundarysupported; listcompleteness shouldnotdependonrecursivegrounding.',
179:'DSM1148twoNH4versusDSM1165oneNH4changesironvalence. Twelvewaterlabel doesnotjustifycommonhexahydratecorrection.',
180:'JCM758literaltrisodiummonohydrate lacksformCAS. GenericMeSHcannotprovewatercount;holdappropriate.',
181:'ExactCM0957catalogmatchesmanufacturer15ingredientdrytypicalrecipe. Quantitysum35.4055rounds35.4; noassumedpowderfractions orunlistedwaterpart.',
182:'DSM1600L15onepack withseparateadditives doesnotdeterminepacksize orformulation. Preservesdryproduct versusassembled2xstock.',
183:'SpacingonlyNa2MoO4.2H2O,CAS10102-40-6,CHEBI75213agree;not transferredtoanhydrousowner.',
184:'CHEBI3374fourcapsaicinaliases cannotresolveCHEBI31345. Rejectiondeltacorrect;D/DLunreviewedaliases remainheld. RootmustcomposeBsourcealiasfromsamebaseline.',
185:'Frozen10%ferricsulfatein0.01NH2SO4 is anacidifiedstock. CASsolute cannotidentifywholepreparation; nominalsourcequalifiedproposalshouldretainunknownpercentbasis.',
186:'0.25g/2.06339mmol implies121.16g/mol,notHCl157.62. Sourceinternalmassconversionconflict remainsunresolved.',
187:'Na2MoO4.2H2O/CAS10102-40-6 supportsdihydrate; cannotrescueothermalformed/onewatercases.'}
open_cases=set()
resolutions={
144:'Re-review: C-P06 now marks the complete source input list COMPLETE; egg species and yolk:white proportions remain unreported. The source-qualified material scope is supported.',
149:'Re-review: the false DSMZ1053 corroboration was removed. DSMZ188 remains direct ferric-hydrate support; the current1053 difference is explicit.',
167:'Re-review: C-P09 now represents a nominal0.1%w/v sodium-resazurin stock. Full original DSMZ330 independently repeats0.5ml of this stock; frozen source_record attribution is explicit. UNKNOWN constituent completeness preserves the unspecified solvent.',
176:'Re-review: DSMZ1592,1593 and1593a explicitly supply10ml of7.5g/L stock, while1673/1677/1678 use350g/L and1845 uses solid7g. C-P08 is restricted to the exact frozen7.5g/L context, has appropriate primary evidence, and uses UNKNOWN completeness.',
178:'Re-review: C-P07 now marks all nine bounded source inputs COMPLETE, while recursive stock identities remain unasserted. The four post-cooling supplements occur before the primary source instruction To complete the medium.',
185:'Re-review: C-P10 captures the nominal10% ferric-sulfate stock in0.01N sulfuric-acid solution. Original JCM1267 independently repeats the88.8ml source addition. Percent basis and supplied hydrate remain unknown; no exact solid identity is inferred.'}
cases=[]
for i,d in enumerate(D,140):
 refs=[]
 for eid in d['evidence_ids']:
  e=E[eid];p=R/e['capture']['path'] if e['capture']['root']=='artifact' else None
  if p and p.exists():refs.append({'evidence_id':eid,'path':e['capture']['path'],'sha256':sha(p)})
 cases.append({'case_index':i,'case_id':d['case_id'],'status':'findings_open' if i in open_cases else 'complete','reviewer':'primary_b (independent of primary_c author)','assessment':notes[i],'resolution':resolutions.get(i),'reviewed_decision_sha256':hashlib.sha256(json.dumps(d,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest(),'reviewed_proposal_captures':[p['after_capture'] for p in P if d['case_id'] in p['case_ids']],'evidence_checked':refs,'holds':'All frozen WITHHOLD/REJECTED and owner payload review obligations remain; this assesses only the bounded source decision/proposal.','independence_limit':'This reviewer authored the shared B122/JCM1209 stock proposal, so its payload requires independent A review; this C156 review covers only primary_c source linkage.' if i==156 else None})
out={'reviewer':'primary_b','reviewed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'scope':'All48 assigned Ccases140:188; primary evidence, source raw_record attributes, actual owner scope and exact proposed deltas. No publication approval.','input_hashes':{n:sha(R/'parts'/n) for n in ['c-input.json','c-decisions.json','c-evidence.json','c-proposals.json']},'cases':cases,'proposals_checked':[{'proposal_id':p['proposal_id'],'capture':p['after_capture'],'assessment':'Bounded delta reviewed; any open related case finding must be resolved before complete status.'} for p in P],'findings':[{'cases':[149],'finding':'DSM1053 current source does not repeat ferric hydrate; correct source attribution.'},{'cases':[144,178,176],'finding':'PARTIAL completeness incorrectly justified by unresolved identities/solvent: use schema list completeness semantics.'},{'cases':[176,167,185],'finding':'RESTingredient response does not carry occurrence stock attributes; source locator must bind frozen source_record or matched original recipe.'},{'cases':[167,185],'finding':'Explicit nominal stock context permits bounded proposal; remaining percentage/solvent details need not defer source identity.'}]}
for f in out['findings']:f['status']='resolved_after_direct_re_review'
out['resolved_findings_case_indices']=sorted(resolutions)
out['all_cases_reviewed']=len(cases)==48 and {x['case_index'] for x in cases}==set(range(140,188))
out['supersedes']='parts/b-independent-c-review.json; original finding statements remain in findings and each case assessment, followed by explicit resolution. No original scientific finding is discarded.'
(R/'parts/b-independent-c-review-final.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
print('Independent48case review saved; openfindings',sorted(open_cases))
