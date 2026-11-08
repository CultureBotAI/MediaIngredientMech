from pathlib import Path
import json,hashlib,datetime,copy,re,yaml,collections
O=Path(__file__).parent; P=O.parent/'materials'; B=Path('reports/all_unmatched_20261107/worker-05')
def load(p): return json.loads(Path(p).read_text())
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ch(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def save(n,x):
 p=O/n; assert not p.exists(),p; p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n')
now=datetime.datetime.now(datetime.timezone.utc).isoformat(); reviewer='Codex GPT-6 /root/media_research'
D=load(P/'decisions.json')['decisions']; S=load(O/'source-index.json'); R=load(O/'whole-records.json'); F=load(O/'frozen-contexts.json'); L=load(O/'proposal-lineage-audit.json'); A=load(O/'field-and-structural-audit.json'); E={s['evidence']['evidence_id']:s for s in S}
# Reviewer-authored claim-specific judgments. Numbers refer to the independently extracted primary index.
payload_notes={
1:('Fish peptone (Fluka) cannot identify Bacto Peptone: the inspected Bacto specification names bovine and porcine protein, and MICRO names mammalian peptone. The exact source token is preserved as rejected provenance. The prior Neopeptone, Universal and Oxoid exclusions remain. Inherited generic aliases, shared counts and whole-owner claims remain held.',[284,288,281,322,325]),
2:('The manufacturer distinguishes numbered Proteose Peptone No. 3 from unnumbered Proteose Peptone. The eight numbered aliases are retained as nonresolving provenance; the existing unnumbered owner is not merged. Other inherited digest and role assertions are outside this bounded correction.',[283,281,289]),
3:('Sucrose CHEBI:17992 and salicin CHEBI:17814 have different structures. Retiring d-salicin preserves its raw provenance and does not change sucrose identity or the separate D-Sucrose tombstone. This existing exact sucrose identity can support the stock component without approving other owner claims.',[287,319]),
4:('TOGO M230 identifies leafy soil as an input to an equal-volume tap-water extraction, boiled two hours and clarified. The owner denotes starting soil, not the processed aqueous extract. Plant/mineral composition remains unknown and is not needed to preserve that material boundary.',[193]),
5:('JCM1474 specifies 10 g liver powder in 170 ml water, 50–60 C for one hour, boiling five minutes, pH 7.2 and filtration. The 150 ml medium addition is a dose of the extract. Input masses do not establish retained component quantities after filtration; the payload preserves that distinction.',[194]),
6:('TOGO M2843 supports the literal Wako-qualified meat extract source. The Wako-hosted document is a Biokar product document, so it is only comparative support for an extract class and not proof of a historical Wako catalog, species or identity with MP enrichment. The final payload makes no such catalog assignment.',[195,410]),
7:('Fraction V is supported only where the assigned recipe actually says it. ADC/OADC input masses are not final-medium concentrations; unnumbered Fraction sources do not prove V. Inherited commercial catalogs and role claims remain unapproved. Source counts are unchanged.',[196,197,200,242,253,353]),
8:('TOGO M2920 explicitly supports pooled sterile human urine. Neither pooling nor sterility gives a donor composition or a sterilization method. The proposed source preparation retains these unknowns and does not add unqualified urine as a globally resolving identity.',[198]),
9:('The official Oxoid LP0032 description supports a powdered pancreatic digest of skimmed milk. The historical source names the product but no pack size; LP0032J is an orderable comparator, not an imposed historical pack. Skimmed milk is not asserted as an unchanged component after digestion.',[199,312,406]),
10:('TOGO M1331 supports the source BD/Bacto meat-peptone wording. Its GMO enrichment cannot by itself select an exact manufacturer catalog or prove identity with every generic meat peptone. The supplied-form addition is bounded to the literal source and retains the existing owner holds.',[202,281]),
11:('NBRC907 independently lists chrysalis extract, yeast extract and peptone. A source-defined chrysalis extract is supported, but insect species, extraction conditions and molecular constituents are not disclosed. The payload preserves rather than fills those gaps.',[204,420]),
12:('TOGO M2894 lists gelatin peptone separately from meat and casein peptones. The named hydrolysate identity is supported; gelatin animal species, enzyme and catalog are not established. No parent protein or neighboring peptone is used as exact identity.',[207]),
13:('JCM153 and NBRC1390 specify whole-fat cow milk, including a 10 ml source dose. The whole-fat supplied-form qualifier is confined to those sources and not propagated to every generic cow-milk occurrence or interpreted as g/L. The older lexical grounding and roles remain held.',[208,226,305]),
14:('The historical CrystalSea source states the manufacturer product family but not regular versus Bioassay Laboratory. Current regular-product thiosulfate information is comparative, not a historical ingredient assertion. The 3% source dose has no invented percentage basis.',[228,405]),
15:('DSMZ687 separately names Bacto Panton and Bacto Bitone at 10 g each. The existing Panton placeholder is promoted as the named preparation without spelling normalization to a guessed product. Unknown historical supplier spelling does not authorize collapsing the two separate entries.',[229,416]),
16:('The separate DSMZ687 Bitone line supports reuse of the existing Bitone owner. Neither similar spelling nor the same 10 g dose proves Panton/Bitone equality. The proposed identity retains the source name and unresolved historical product details.',[229,417]),
17:('All four inspected TOGO recipes specify fish-sperm DNA (SERVA), not generic DNA or thymus nucleic acid. Ten generic/conflicting tissue aliases become nonresolving while their exact sources remain. Species, chain length and counterion remain unknown; the legacy mapping direction and herring-sperm history are not independently approved.',[232,233,234,235,320]),
18:('JCM1013 explicitly states a 20% w/v sucrose stock and a 10 ml addition. The exact sucrose constituent can reference the extant CHEBI:17992 owner; this optional improvement does not require every component to be grounded. PARTIAL composition and unknown solvent/final receiving volume are retained.',[236,287]),
19:('JCM177/TOGO M170 explicitly uses fish-meat extract separately from Bacto peptone. A biological extract does not become fish peptone or dried sardine through name similarity. Species, extraction yield and hydrolysis remain unasserted.',[237,238,239]),
20:('Manufacturer 211693 and the technical guide distinguish Proteose Peptone No. 3 from No. 2 and unnumbered product. The source-named product is supported, but its variable protein digest has no invented constituent recipe or historical package assignment.',[240,283,281,293,413]),
21:('The manufacturer describes Difco Soytone and lists 212488/212489 packages. Its processing scope is distinct from the separately described Bacto Soytone and Phytone products; their interchangeability is not established. The existing Bacto Soytone tombstone and cross-worker union holds remain untouched.',[243,281,411]),
22:('JCM1054 boils small dried sardines with maize meal in 500 ml water for 20 minutes, filters, and makes the combined preparation to 1 L. The owner denotes the dried fish input, not the filtrate or fish peptone. Exact fish species is not inferred.',[245,246,301]),
23:('TOGO M2224 identifies Oxoid Special Peptone. The official LP0072 description supports a mixed digest product family without historical pack size or blend proportions. Matching the 23 g dose in an unqualified DSMZ715 peptone mixture is insufficient to route that source here.',[247,409,328]),
24:('NBRC1372 identifies rice extract as one drop. This does not establish a millilitre dose, solvent, extraction yield, tissue or cultivar. The named source preparation is retained without equating it to starch or whole grain.',[248,421]),
25:('DSMZ170 identifies Difco skim milk powder, and the manufacturer powder description corroborates its dehydrated supplied form. The payload does not merge generic skimmed milk, liquid milk or every package with this source.',[250,324]),
26:('The substantive catalase fact comes from TOGO M109, with JCM117 recorded as lineage: literal C--10, 60 mg and filtration. The direct JCM117 capture says Nothing found and cannot support a direct current recipe claim. Current C100 does not establish historical species; the C9322 coordinator proposal remains separate. Historical human NCIT exclusion is preserved.',[252,422]),
27:('The archived source records and JCM20 support NBCo liver concentrate with source-specific 1 g and 0.2 g additions. The generic liver-extract/Raka-Ray medium term is not its exact identity. Concentration factor, species and formulation remain unknown; original occurrence statistics remain intact.',[254,316,353,294]),
28:('DSMZ570 separately lists maize extract and starch. The maize extraction product is a legitimate named material without becoming corn steep liquor or purified starch. Tissue fraction, solvent and supplier remain unresolved rather than guessed.',[260,295]),
29:('The Wako catalog distinguishes casein-derived unqualified Hipolypepton from soy-derived S/N/NS variants. Nihon product identity is supported at that boundary, without selecting an alternative in the Trypticase-or-Hipolypepton recipe. The raw alternative remains a choice.',[205,292,404]),
30:('The existing Polypeptone preparation is preserved with its own registry identity, while Hipolypepton aliases are withdrawn. The BD 50:50 casein/animal-peptone description is a comparison, not proof that unqualified source 442 has that brand or recipe. Inherited Japanese product aliases remain held.',[302,281]),
31:('MICRO:0001795 is a nonobsolete named Phytone term whose definition cites the manufacturer papaic soybean digest. Its erroneous Hordeum vulgare parenthetical is not adopted. The three new applicability assertions are agent interpretations, correctly typed LLM_SUGGESTION. Bounded coordinator reuse does not import W10 histories, counts or approval of the pending union.',[296,418,438,281]),
32:('The generic soy digest remains broader than branded Phytone, Soytone and their alternatives. Five branded/alternative aliases become nonresolving, as does optional Properties metadata. Exact raw strings and history survive, along with the CHEBI:8150 tombstone and original counts; the retained peptic-digest alias is not newly endorsed.',[306,419,281]),
33:('The Oxoid CM0059 powdered whole formulation has the stated malt extract, mycological peptone and agar list. The 30/5/15 g per litre values are standard-reconstitution equivalents with the manufacturer performance qualification, not concentrations in dry powder. The 50 g product instruction and separate prepared-plate comparison remain distinct; named UNMAPPED parts are legal.',[300,407,408]),
34:('MediaDive310a names 200 ml tomato extract separately from 800 ml water. Reuse of the existing extract owner does not invent a tomato formula or identify the whole medium as its extract. Variable biological composition does not block that material identity.',[307,415]),
35:('Source 341 explicitly attributes Universal peptone to Merck. M66 is a relevant current comparator, but no source catalog selects 107043 or proves the historical casein/meat/soy blend. The product-family identity and Bacto alias exclusion preserve this distinction.',[308,322]),
36:('The single DATABASE_MATCH assertion is narrowly the nonobsolete named MICRO:0000177 lookup and its Bacto Neopeptone definition. Manufacturer product evidence supports the named family; a historical package is not selected. Broader source-applicability judgments are not mislabeled as human curation.',[309,325,285,412]),
37:('Only the six explicitly Sigma-qualified frozen occurrences in the 129-occurrence generic case are routed by this proposal. Current DSMZ829 does not resolve the unqualified historical KOMODO829 version, and generic sea salt is not thereby Sigma product. The 3000 g/L outlier is preserved as a source issue; no S9883 formula is imposed.',[310,249,206,210,211,212,214,215,216,217,218,219,220,221,222,223,224,225]),
38:('The extant UTEX organic-peat input has its own 0.5 tsp addition beside 1.5 tsp greenhouse soil in 200 ml water. It is not identical to the whole steamed soil-water preparation or automatically to the SAG peat-soil input. The existing owner is reused with those boundaries intact.',[230,314,434]),
39:('Generic Peptone has no demonstrated mammalian origin merely from MICRO:0000178 lexical matching. The local generic-material identity is justified; the malformed Peptone (0.01 % token becomes nonresolving with its original MicrobeDecoder provenance. Plural peptones and both assay observations remain. Eighteen historical inbound references still require source-specific review; identifier resolution alone does not validate them.',[281,288])}
case_notes={
4:('NBRC1611 and TOGO M3055 literally say Peptone(Difco); Bacto is an enrichment, not a product selection. The exact historic digest remains unresolved among existing candidates, so withholding a forced Bacto assignment is justified.',[191,423]),
5:('Leafy soil is the material input to the boiled equal-volume extraction, not the resulting extract. Soil composition remains unspecified.',[193]),
8:('JCM1474 provides the complete heat, pH and filtration process; the 150 ml addition is distinct from preparation input masses and unknown yield.',[194]),
9:('The Wako source qualifier is literal, whereas the hosted Biokar document is only a comparator. No historical catalog or species is assigned.',[195,410]),
11:('Both M2879 and M2880 specify Fraction V. This supports the source qualifier without selecting every inherited BSA catalog.',[196,197]),
16:('M2920 explicitly names pooled sterile human urine. Donor variation and sterilization method remain unspecified.',[198]),
18:('The Oxoid peptonised-milk product is supported by source and manufacturer; pancreatic digestion and powder form are not unchanged milk composition.',[199,406]),
20:('M1946 OADC specifies Fraction V within the supplement preparation. Its mass is not a final-medium BSA concentration.',[200]),
22:('M1331 supports its literal BD/Bacto meat-peptone qualifier; GMO enrichment alone does not establish an exact historical catalog.',[202]),
31:('The source explicitly offers SPIOR or skim milk. A whole alternative cannot be assigned to a single owner without selecting the branch; no component incompleteness pretext is used.',[203]),
32:('NBRC907 independently names chrysalis extract. Insect species and extraction method remain unknown, while the named preparation is curatable.',[204,420]),
33:('Trypticase or Hipolypepton remains a choice. The positive Hipolypepton proposal does not route the complete alternative to that product.',[205,404]),
34:('The five frozen KOMODO829 contexts omit supplier information. The different current DSMZ829 version cannot retrospectively assign Sigma or resolve other version differences. Existing candidate reconciliation remains required.',[206,225]),
35:('M2894 separates gelatin, meat and casein peptones. Source material distinguishes gelatin hydrolysate without supplying animal species or an enzyme.',[207]),
37:('NBRC923/367 identifies BBL Peptone but does not distinguish a historical digest/catalog. Existing product candidates prevent an arbitrary duplicate handle from resolving the missing selection.',[424,425]),
39:('NBRC1390 states whole-fat cow milk and 10 ml. This is a supplied-form qualifier and volumetric dose, not a universal claim about generic milk.',[208]),
40:('All 129 frozen occurrences remain present. Only six with explicit Sigma notes support positive routing; the other 123 remain unresolved. Neither matching salt dose nor a current supplier page is a bridge for those sources.',[210,211,212,214,215,216,217,218,219,220,221,222,223,224,225]),
46:('JCM153 explicitly supplies whole-fat milk. The qualifier is source-specific and does not expand the generic owner scope.',[226]),
50:('CrystalSea manufacturer identity is available, but regular versus Bioassay formulation and the percentage basis are not. A bounded named product is supported without a thiosulfate assertion.',[228,405]),
51:('DSMZ687 separately lists Bacto Panton. Its spelling is not normalized to a guessed commercial preparation.',[229,416]),
55:('DSMZ687 separately lists Bacto Bitone. Equal mass to Panton is not equality of products; existing owner continuity is retained.',[229,417]),
57:('SAG peat-soil input and UTEX organic-peat input have different source scopes. The comparison-owner correction does not assign the SAG preparation to UTEX or identify it with the whole medium.',[230,314,434]),
62:('All four TOGO sources specify SERVA fish-sperm DNA. Generic DNA and thymus aliases cannot resolve to that narrower material; species and counterion remain unknown.',[232,233,234,235,320]),
66:('JCM1013 explicitly says 20% w/v sucrose stock and 10 ml addition. Linking its sucrose part is optional and supported; missing solvent still requires PARTIAL composition.',[236,287]),
67:('The three frozen contexts preserve fish-meat extract distinct from Bacto peptone. Extract, fish peptone and dried whole sardine remain separate material types.',[237,238,239]),
69:('The source names numbered Proteose Peptone No. 3; manufacturer descriptions distinguish the numbered series. No generic-peptone substitution follows.',[240,283,281]),
70:('The BSA mass is an ADC preparation input, with no asserted final solution volume. Fraction V is retained only where explicitly stated.',[242]),
71:('The source explicitly selects Difco Soytone. Generic soy, Phytone and Bacto Soytone do not inherit that product identity; existing rejected tombstone history is retained.',[243,281,411]),
72:('The nested Scharlau MRS proteose-peptone ingredient does not specify a numbered BD product or establish its exact proprietary constituent. A 10 g quantity alone cannot make that product selection.',[244]),
81:('The three contexts preserve dried sardine as an input to the boiled maize/fish extraction, not as the final filtrate or a fish hydrolysate.',[245,246]),
89:('M2224 explicitly names Oxoid Special Peptone, supported by LP0072. A coincident 23 g unqualified peptone mixture elsewhere is insufficient to select this product.',[247,409,328]),
90:('NBRC1372 says one drop of rice extract. No millilitre conversion, extraction concentration or solvent is invented.',[248,421]),
100:('DSMZ1025 supplies Sigma sea salts. Source qualification supports the product family without a historical S9883 catalog assignment.',[249]),
101:('Both DSMZ170 contexts retain Difco skim-milk powder and its mass. Dry supplied form does not justify merging liquid skim milk.',[250,324]),
108:('The BBL Todd-Hewitt source says Peptonen. It does not select Neopeptone merely from a similar generic name or product knowledge.',[251]),
116:('Both frozen contexts bind to TOGO M109 and its JCM117 lineage. The empty current JCM page is unsuccessful evidence; C--10 and 60 mg are supported by TOGO, not a direct JCM retrieval.',[252,422]),
118:('The OADC preparation specifies BSA Fraction V and its input mass. No final-medium concentration or universal catalog identity is added.',[253]),
119:('Archived M4/M13 and JCM20 support NBCo liver concentrate, with distinct 1 g and 0.2 g recipe doses. Concentration factor and species remain unknown.',[254,316,353]),
120:('Archived M2400/M2401 say Bovine albumin fraction without a numeral. This does not justify assigning Fraction V, despite related BSA recipes elsewhere.',[353]),
122:('All three maize-extract contexts preserve its separate listing from starch. Source does not support corn-steep-liquor equality.',[260]),
125:('M3128 explicitly carries Sigma sea salts; the source-specific supplier qualifier is supported without a historical catalog/formula inference.',[353]),
127:('MediaDive2060 and the Wako catalog support unqualified casein-derived Hipolypepton. Soy S/N/NS variants remain distinct.',[292,404]),
132:('MediaDive316 carries Proteose Peptone No. 3 with its BD attribution. Manufacturer numbered-product distinctions support the positive preparation identity.',[293,283]),
133:('MediaDive1599 and the primary recipe lineage identify NBCo liver concentrate. The proposal reuses the existing owner without adopting a generic extract or whole-medium term as exact.',[294,254,353]),
134:('MediaDive575/DSMZ570 separates maize extract from starch. Variable extract composition does not prevent the named-material registry.',[295,260]),
139:('MediaDive125/362 Phytone scope is compatible with the specifically named MICRO term and manufacturer definition. The erroneous barley annotation and pending coordinator union are excluded.',[296,418,438,281]),
140:('MediaDive925 retains explicit Sigma sea-salt attribution. No equivalence with natural salt or exact current product recipe is asserted.',[297]),
143:('The source describes air-dried garden soil. Existing process-specific soil candidates are not automatically interchangeable with that input; a new arbitrary handle would not resolve the material-selection gap.',[298]),
147:('The 23 g DSMZ715 peptone mixture and the 5 g Roth Schaedler mixture are not selected as Oxoid Special Peptone by nominal dose or common medium name. The different product context remains unresolved.',[299,328,426]),
155:('MediaDive1712 names Oxoid malt extract agar at 50 g. The whole powder formula and standard-reconstitution basis are supported; neither malt extract alone nor prepared plates are exact dry-product identity.',[300,407,408]),
156:('MediaDive1986 refers to the dried sardine input. The JCM1054 process distinguishes that material from the filtered combined extract.',[301,245]),
160:('Unqualified MediaDive442 Polypeptone lacks supplier selection. The existing owner can retain a bounded generic preparation identity, while the BD blend is comparative and Hipolypepton aliases are withdrawn.',[302,281]),
163:('Peptone (Oxoid) is not a BD Bacto identity. Retiring that wrong alias does not select which Oxoid digest/catalog the source intended.',[303,281,409]),
172:('The D-Sucrose source and CAS support sucrose. Salicin is a different chemical; rejecting its alias preserves the exact original provenance and does not alter other sucrose claims.',[304,287,319]),
173:('The two MicrobeDecoder peptones observations and plural source label are retained. A truncated concentration fragment cannot serve as an unqualified material synonym; the source does not establish mammalian origin.',[281,288]),
175:('The generic cow-milk ingredient handle is preserved. Whole-fat information applies to the explicit source contexts, not all uses of that handle.',[305,208,226]),
176:('Generic soy digest is not identical to Phytone, Soytone or an either/or alternative. The five withdrawn aliases and optional metadata retirement retain sources/history; shared counts are not redistributed.',[306,419,281]),
180:('MediaDive2371/310a explicitly supplies tomato extract separately from water. Source-defined biological composition may remain partial without forcing a molecular term.',[307,415]),
184:('MediaDive341 explicitly attributes Universal peptone to Merck. Current M66 information is comparative and does not select a historical 107043 catalog.',[308,322]),
186:('MediaDive263 and the official named MICRO:0000177 term support Neopeptone. The database evidence is limited to that lookup; no broader human curation is claimed.',[309,325,285]),
187:('MediaDive2367 explicitly carries SIGMA. The preparation registry preserves that supplier scope without an exact natural-sea-salt or current-catalog assertion.',[310])}
assert len(payload_notes)==39 and set(case_notes)=={d['case_index'] for d in D}
def sb(indices):
 return [{'evidence_id':S[i]['evidence']['evidence_id'],'source_index':i,'capture':S[i]['evidence']['capture'],'url':S[i]['evidence'].get('url'),'original_accessed_at':S[i]['evidence'].get('accessed_at'),'locator':S[i]['evidence'].get('locator')} for i in sorted(set(indices))]
payload_reviews=[]
for n,r in enumerate(R,1):
 p=r['proposal'];text,ids=payload_notes[n]
 payload_reviews.append({'proposal_id':p['proposal_id'],'status':'complete','verdict':'supported_with_retained_limits','lineage':L['entries'][n-1],'whole_payload_canonical_sha256':ch(r['record']),'assessment':text,'primary_evidence':sb(ids),'changed_fields':[x['path'] for x in A['field_reviews'][n-1]['changes_from_selected_predecessor']],'before_and_predecessor_whole_objects_read':True,'all_fields_reviewed':True,'held_claim_policy':'Unchanged source, role, component-coupling, organism, duplicate-family, owner and export holds are preserved. This is not whole-owner or release approval.'})
case_reviews=[]
bycase={f['case_id']:f for f in F}
for d in D:
 f=bycase[d['case_id']]; text,ids=case_notes[d['case_index']]
 case_reviews.append({'case_index':d['case_index'],'case_id':d['case_id'],'status':'complete','verdict':'supported_with_retained_limits','decision_object_sha256':ch(d),'frozen_case_object_sha256':ch(f['raw_case']),'case_input_sha256':d['case_input_sha256'],'source':d['source'],'occurrence_ids':d['occurrence_ids'],'frozen_recipe_bindings':[{'occurrence_id':r['occurrence']['occurrence_id'],'path':r['occurrence']['full_recipe_snapshot'],'sha256':r['occurrence']['source_file_sha256'],'component_path':r['occurrence']['component_path']} for r in f['recipes']],'assessment':text,'primary_evidence':sb(ids),'proposal_ids':d['proposal_ids'],'reported_remaining_requirement':d['missing_requirement'],'substantive_source_and_owner_holds_preserved':True})
save('case-reviews.json',{'reviewer':reviewer,'at':now,'case_reviews':case_reviews})
save('payload-reviews.json',{'reviewer':reviewer,'at':now,'payload_reviews':payload_reviews})
# Verify all 27 prior mapping-evidence provenance rows, including Phytone replacement.
md=load(P/'mapping-evidence-dispositions.json')['dispositions']; mr=[]
old_to_new={old:x for x in R for old in x['proposal']['replaces_proposal_ids']}
for row in md:
 r=old_to_new[row['proposal_id']]; prev=r['predecessor']['ontology_mapping']['evidence'][0]; assert ch(prev)==row['original_evidence_canonical_sha256']==row['audit_full_value_sha256']; assert r['proposal']['predecessor_capture']['sha256']==row['guarded_payload_sha256']
 final=r['record']['ontology_mapping']['evidence']
 if row['audit_row_id']=='provenance-flag-329':
  assert len(final)==3 and all(x['evidence_type']=='LLM_SUGGESTION' for x in final)
  why='Three replacement assertions separately identify ontology application, manufacturer distinction and bounded coordinator reuse. These are agent interpretations, not human curation. The original evidence remains in the exact predecessor.'
 else:
  expected=copy.deepcopy(prev);expected['evidence_type']=row['new_native_type'];assert final[0]==expected
  why='Only the evidence type changes; source and claim text are exact.'
  why+=(' The nonobsolete named Neopeptone term and quoted database definition support DATABASE_MATCH only for this narrow lookup.' if row['new_native_type']=='DATABASE_MATCH' else ' The claim interprets source applicability or preparation identity, so LLM_SUGGESTION accurately identifies the authoring method even though it cites a primary source.')
 mr.append({'audit_row_id':row['audit_row_id'],'predecessor_proposal_id':row['proposal_id'],'successor_proposal_id':r['proposal']['proposal_id'],'prior_evidence_sha256':ch(prev),'final_evidence':final,'final_evidence_sha256':ch(final),'verdict':'supported','assessment':why,'after_capture':r['proposal']['after_capture']})
# Recursively inspect all new mapping-type objects; ComponentEvidence has its separate enum.
def walk(v,path=''):
 if isinstance(v,dict):
  if 'evidence_type' in v:yield path,v
  for k,x in v.items():yield from walk(x,path+'/'+k)
 elif isinstance(v,list):
  for i,x in enumerate(v):yield from walk(x,path+'/'+str(i))
newrows=[]
for r in R:
 old={ch(v) for path,v in walk(r['predecessor'])}; before={ch(v) for path,v in walk(r['before'] or {})}
 for path,v in walk(r['record']):
  if path.startswith('/components/'):continue
  if ch(v) not in old:
   assert v.get('evidence_type') not in ['MANUAL_CURATION','CURATOR_JUDGMENT'] or ch(v) in before,(r['proposal']['proposal_id'],path,v)
   newrows.append({'proposal_id':r['proposal']['proposal_id'],'path':path,'evidence':v,'sha256':ch(v)})
save('mapping-evidence-review.json',{'reviewer':reviewer,'at':now,'dispositions':mr,'all_new_mapping_evidence':newrows,'historical_human_policy':'Historical human evidence retained in the selected predecessor remains exact. Older evidence already withdrawn in that predecessor is preserved in before/predecessor captures and is not reinstated. ComponentEvidenceTypeEnum is distinct and was not bulk retyped.','component_assertions_reviewed_in_whole_payloads':True})
# The complete seven externally filed findings are independently assessed without modifying issue state.
ft={
'W05-MAT-001':('Five generic-soy branded/alternative aliases are nonresolving. The specific Phytone term is supported without accepting its erroneous barley annotation; Difco Soytone remains separately named. Counts, history, tombstones and pending union dependencies are preserved.',[281,411,438]),
'W05-MAT-002':('The ten generic/thymus DNA labels no longer resolve to fish-sperm DNA. Exact strings and sources remain, with source-specific SERVA evidence and no inferred species, counterion, molecular length or herring-tombstone reversal.',[232,233,234,235,320]),
'W05-MAT-003':('The truncated concentration token is rejected while plural peptones and the two assay observations remain. No inherited mammalian component reference is retargeted merely to match the new generic identity.',[281,288]),
'W05-MAT-004':('Fish peptone (Fluka) is excluded from the Bacto owner using the fish-versus-mammalian material contradiction. No replacement catalog or origin is invented.',[284,288]),
'W05-MAT-005':('All three Properties strings are preserved as rejected metadata provenance. This is the explicitly optional classification cleanup; no new resolver defect or release blocker is claimed.',[252,306]),
'W05-MAT-006':('The optional sucrose part now points to the available exact CHEBI:17992 owner. PARTIAL composition, the explicit 20% w/v basis and unknown solvent remain. A named UNMAPPED component was previously legal; this correction is not a new mandatory-grounding policy.',[236,287]),
'W05-MAT-007':('Active evidence now attributes the inspected C--10/60 mg fact to TOGO M109 and labels the empty current JCM117 response unsuccessful. Historical JCM lineage and history are retained; C100 species and separate C9322 are not inferred.',[252,422])}
fr=[]
for v in load(P/'finding-dispositions.json')['dispositions']:
 t,ids=ft[v['finding_id']]
 fr.append({'finding_id':v['finding_id'],'status':'remediation_supported_in_exact_proposed_bytes','original_finding_object_sha256':ch(v['prior_finding']),'author_disposition_object_sha256':ch(v),'successor_proposal_ids':v['successor_proposal_ids'],'successor_captures':v['successor_captures'],'assessment':t,'primary_evidence':sb(ids),'issue_closed':False,'whole_owner_or_release_approval':False})
save('finding-disposition-review.json',{'reviewer':reviewer,'at':now,'dispositions':fr,'new_findings':[]})
print('Created 61 case reviews, 39 payload reviews, 27 mapping provenance reviews and seven finding reviews.')
