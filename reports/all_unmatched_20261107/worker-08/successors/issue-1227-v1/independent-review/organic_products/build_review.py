"""Serialize this reviewer's individually written appraisals and verify exact inputs.

Read-only toward every author, source, ontology and maintained artifact. Outputs
are restricted to this independent review directory. Hash checks are explicitly
separate from the scientific reading recorded in source-read-ledger.json.
"""
import datetime, hashlib, json, pathlib, sqlite3, yaml

R = pathlib.Path('reports/all_unmatched_20261107/worker-08')
S = R / 'successors/issue-1227-v1'
A = S / 'research/organic_products'
O = S / 'independent-review/organic_products'
Q = pathlib.Path('/Users/marcin/Documents/VIMSS/ontology/Mechs/MediaIngredientMech/.temp/all-unmatched-20261107/queue/preliminary-v5')
def read(p): return json.loads(p.read_text())
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def canon(x): return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
def write(n,x):
    p=O/n
    assert not p.exists(), f'Refuse to replace {p}'
    p.write_text(json.dumps(x,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
H=read(A/'PRIMARY-HANDOFF-v3.json'); Ass=read(A/'assignment.json')
D=read(A/H['final_selection']['decisions'])['decisions']
P=read(A/H['final_selection']['proposals'])['proposals']
D2=read(A/'decisions-v2.json')['decisions']; P2=read(A/'proposals-v2.json')['proposals']
Eold=read(R/'successors/issue-1201-v1/evidence.json')['evidence']
Enew=read(A/H['final_selection']['evidence_additions'])['evidence']
E={e['evidence_id']:e for e in Eold+Enew}
frozen={c['case_id']:c for c in read(R/'provenance/shard-08.json')['cases']}

# These paragraphs were written by /root/inorganics after actual source and
# whole-payload inspection; they are not copied author or predecessor verdicts.
case_appraisals = [
"TOGO M2313 offers laminarin from brown algae among alternative carbon inputs. ChEBI6364 identifies the generic polysaccharide; it does not establish Laminaria digitata for this occurrence. Generic naming plus retained CultureBotHT supplied-form provenance is appropriate, without a second species-specific molecule or a transferred source count.",
"JCM393 replaces lactate with 0.725 g/L sodium nicotinate. NIST54-86-4 establishes a sodium-containing salt, not nicotinic acid. The CAS-primary candidate and asymmetric parent relation preserve that boundary. Bounded exact-term searches are not a global absence proof; later duplicate reconciliation is an integration dependency, not missing source chemistry.",
"The complete MediaDive1894 primary recipe lists Soya flour 20 g, mannitol 20 g and agar 20 g in tap water. FOODON03302142 means soybean flour and has soy flour as a synonym. SYNONYM_MATCH now records the actual label relationship; no peptone, supplier grade, defatting or molecular composition is inferred.",
"The frozen extracted token 0.2 N KOH comes from the TOGO M2844 indicator instruction, 0.5% bromothymol blue in 0.2 N KOH. It is a combined preparation, not a source assertion that pure KOH is the whole ingredient. Two known parts and UNKNOWN closure retain unreported percent basis and carrier.",
"The recovered TOGO M1198 JSON specifies an ethane gas supply, while JCM1120 returns Nothing found. ChEBI42266 supports the ethane component; the 10–50% gas-use instruction does not create a pure whole atmosphere or specify gas purity. The failed lookup is not positive support.",
"Both frozen occurrences were inspected separately. Readable NBRC1301 explicitly describes nalidixic acid at 30 mg/mL; exact NBRC1314 and TOGO M2023 requests remain unread after recorded failures. The acid candidate CHEBI100147 is supported, but the second occurrence remains source-held. A readable different recipe cannot release it or prove a sodium salt.",
"JCM1385 refers to JCM1130's VFA context, where the iso-valeric spelling denotes branched 3-methylbutanoic acid. The source raw spelling can be added to CHEBI28484 without merging the straight-chain acid or assigning the VFA mixture as a molecule.",
"JCM600 explicitly names a 5 mM water-saturated toluene solution and a 40 mL addition. The payload retains toluene and unquantified water, not an inferred solvent phase, saturation temperature, grade or closed two-component formulation. Receiving-medium volume errors do not prevent this bounded preparation identity.",
"DSMZ672 and both frozen broth/agar alternatives retain the disjunction Difco0003 or0001. Their labels and source comparison distinguish alternative products; they do not identify which was used in either occurrence. Holding the alternative rather than minting one blended identity remains justified.",
"All five n--Valeric acid occurrences and their VFA contexts were read. Their acid labels support CHEBI17418 and an added spelling alias; they do not equate every receiving recipe or denominator. The entire owner still contains inherited pentanoate aliases whose protonation scope remains held, as already recorded by reviewer A.",
"TOGO M148/JCM157 context names Fluid thioglycolate medium (BBL). Actual ATCC474 and177 identify BD211260 and distinguish the commercial powder from extra ingredients and a scratch alternative. The commercial candidate is a bounded brand/context inference, not a claim that the inaccessible original JCM157 was read or that scratch composition equals the product.",
"The five iso--Valeric acid occurrences were checked against their VFA contexts. ChEBI28484 is the branched acid, and the exact raw strings belong on that owner. No source correction, common stock equivalence, straight-chain isomer merger or quantity conversion is asserted.",
"All three FEBA liquid outgrowth contexts name R2A separately from antibiotics. Official MICRO0000541 distinguishes liquid medium from agar and names six organic constituents, without a closed full recipe. Final v3 uses CURATED_INTERPRETATION and UNKNOWN closure; pyruvate is linked only at the definition's named-anion scope. IF-OP1227-F1 is resolved without adding sodium, agar or amounts.",
"The complete M2972 source calls the Difco material R2A agar and uses a plant-stem agar-surface procedure. This supports a source-specific provenance addition to MICRO0000543. It does not make bare R2A (Difco) a globally resolving agar alias or identify a particular product formulation across other sources.",
"NBRC19 lists Peptic Pepton (USB), 2 g/L, without catalogue code or digestion substrate. An opaque source-qualified USB ingredient is supported; casein, generic peptone equivalence and an invented molecular component list are not. The missing formulation is stated rather than deferred as an unperformed lookup.",
"DSMZ88 separates sulfide ore from other additions and describes preparation/sterilization. Pyrite is an example, not a universal FeS2 specification for the ore. The natural-material registry candidate preserves undefined composition; receiving use does not license a pure mineral exact identity.",
"Both Song CDM frozen records contain dTMP with null amounts. Neither supplies a salt, protonation specification or an actual preparation pH that resolves the form. ChEBI15245 and neutral CHEBI17013 are distinct comparison scopes. No variable concentration or neutral/dianion identity is inferred from absent data.",
"The PYG-betain occurrence names betaine. Sigma B2629 and ChEBI17750 independently support the glycine-betaine zwitterion, CAS107-43-7, distinct from hydrochloride and hydrates. The candidate covers the named molecule, not a particular supplier grade or stock.",
"Denger2010's actual Methods identifies synthesized racemic sulfolactate; the cited Roy2003 Chemicals section explicitly describes sodium sulfolactate synthesis. The frozen DSM3043 experiment uses 10 mM substrate. A source-qualified racemic sodium salt is justified, while sodium stoichiometry, hydration and purity remain unknown. The acid parent is not an exact salt identity.",
"The n -Valeric acid occurrence was read in its full receiving context and compared with JCM1130. The acid spelling supports CHEBI17418. It does not resolve inherited n-Pentanoate/Pentanoate aliases or approve all source-specific protonation states; that existing owner hold remains.",
"All ten NLDM Trimethylglycine occurrences retain 17.5 micromolar despite other medium differences. Trimethylglycine is the exact glycine-betaine synonym supported by ChEBI17750 and Sigma, so the shared candidate is appropriate. No separate substance follows from recipe identifiers, and no hydrochloride or hydrate is substituted.",
"NBRC1045 and957 each use 30 g Trypticase Soy (BBL) with separate NaCl/agar additions. MICRO0000113 supplies the exact synonym and standard broth scope; FAO corroborates the six input recipe. SYNONYM_MATCH is correct. COMPLETE applies to that cited standard input enumeration, not every BBL lot or the supplemented receiving agar medium.",
"M949 andM950 share the JCM906 glycine–NaOH pH10 stock. The primary recipe establishes 0.5 M glycine plus NaOH with unreported titrant amount. Its basal 900 mL water is not evidence of the stock carrier. The shared preparation and UNKNOWN closure preserve that distinction without inventing a final volume.",
"FCGM, FHEPES andNCL preserve cereal leaves as the pre-extraction material. The CCAP recipes distinguish leaf input, water processing and retained extract; FCGM's 0.625 g/500 mL and NCL's 1 g/L are not separate leaf substances. Species, commercial Cerophyll equivalence and grain/flour identity remain unproved.",
"All nine methane occurrences were read with gas/headspace instructions. CHEBI16183 represents CH4 as an ingredient component. Neither mixed atmosphere proportions nor dissolved-versus-gas dose conventions become molecular properties; rejected production/process labels stay rejected and native holds remain.",
"NBRC1394's readable primary recipe specifies PQQ at 1 mg/L; the frozen imported 1 g/L is a dose defect. It still does not identify the supplied acid/salt form. The source hold remains specific to identity and is not a pretext to ignore the already established microgram/milligram-scale dose correction.",
"P5's nested MEM100X input explicitly says L-Asparagine*H2O at 1.50 g/L; its addition is 2.27 mL per 50 mL intermediate, followed by the documented NM assembly. NCIT:C87433 uniquely carries CAS5794-13-8 and exact L-hydrate synonym. CAS_RN_LOOKUP and exact primary identity are supported; non-isomeric SMILES is only connectivity evidence, not proof of a racemate or substitute stereostructure.",
"The frozen MTP4 occurrence explicitly traces archived DSMZ560's 1–2 mL methanethiol gas per50 mL culture, with medium195/193 expansions. The current PDF request failed and is described honestly. ChEBI16007 supports the component molecule; no current-source read, gas-mixture identity or molecular mass dose is invented.",
"The raw MediaDive entry says 6-methylnicotinate, while its automatically assigned CAS5470-70-2 belongs to methyl6-methylnicotinate in actual supplier evidence. The metadata is a conflicting lead, not a source-backed choice of ester, acid or anion. Holding the ambiguous source identity remains necessary.",
"The full existing sodium-stearate owner CHEBI132109/CAS822-16-2 already matches the source salt. Ontology and chemical fields agree at that scope. No additional owner delta is justified solely by the unmatched queue; inherited role/export decisions remain unapproved.",
"The source DL-sodium-lactate assertion does not make the generic stereounspecified owner exclusively racemic. The selected repair rejects L-only and concentration-qualified stock aliases while retaining exact text and provenance. The independent CHEBI232798 L-salt comparison supports the stereochemical boundary; unrelated source membership is unchanged.",
"The complete beta-NAD owner and ChEBI15846 comparison support NAD(+) rather than NADH or a guessed supplied disodium salt. The bounded provenance repair identifies the sources of CAS and structure independently. Existing roles and native WITHHOLD decisions are preserved.",
"Soytone is a branded soybean digest, while the existing FOODON03315720 target is generic hydrolyzed vegetable protein. Full sibling histories include a rejected Bacto Soytone tombstone and multiple live broad owners. Notes can preserve product evidence, but a family winner or all-product equivalence is not scientifically established by the shared identifier.",
"Glycylglycine already has exact CHEBI17201/CAS556-50-3 support in the complete owner and ontology capture. The frozen source adds no distinct salt, stereochemistry or preparation. No redundant payload is warranted; retained functional-role review remains separate.",
"The Cytovirin KG row denotes a production trait. The retained registry record preserves that unresolved named substance; a taxonomy or broad bioactivity identifier would not establish structure. PubChem search/JavaScript-limited evidence is not an inspected primary structure specification, so no exact chemical promotion is justified.",
"The KG Soya-flour row and the separate CM occurrence share the actual MediaDive1894 recipe but remain separately accounted cases. Soybean flour is supported at generic FoodOn scope, with no peptone, supplier grade or wheat assumption. The revised mapping grade records synonym lookup rather than primary-label equality.",
"The Bacto Soytone KG row was compared with the full rejected Bacto_Soytone history and active soy-peptone family. A prior merge is provenance, not proof that all branded and generic hydrolysates are the same ingredient. The bounded notes proposal retains the unresolved family and role/export holds.",
"The GTDB alpha-hydroxyglutarate-gamma-lactone label supplies neither stereochemistry nor protonation/anion form. The registry owner and source name remain appropriate; the S-anion ontology comparison cannot be imposed on an unspecified production-trait label.",
"The GTDB chlororaphin trait is a named pigment, not a species and not automatically oxychlororaphin. The historical paper's inspected first-page material is limited evidence, not a read of a complete structure determination. The existing registry placeholder remains held without a speculative exact chemical identity.",
"Actual JCM60 establishes the ISP5 glycerol/asparagine agar formula, but the generic existing Agar-extracted KG owner has no demonstrated same-version bridge. The notes/history enrichment records usable source facts now; withholding wholesale components is based on that bridge gap, not an unperformed recipe lookup.",
"The raw MediaDive1938 label names 0.5 M HOMOPIPES at pH5.4. The existing CAS202185-84-0 molecular owner and supplier identity support the solute part. A bounded preparation can retain it while carrier/titrant remain unknown; bare HOMOPIPES does not become a global alias of the stock.",
"Actual DSMZ1003's trace-mineral list says Se-acid 10 mg/L without formula, CAS or oxidation state. MediaDive's automated selenic-acid assignment is explicitly a candidate. Neither this source nor pH3 proves selenic rather than selenious acid, so the source-specific hold remains necessary.",
"The non-GTDB alpha-hydroxyglutarate-gamma-lactone row is separately retained. Its name does not specify the S stereoisomer or anion found in a comparison term. The same registry scope is reasonable without creating a second owner from source namespace alone or releasing missing stereochemistry.",
"The non-GTDB chlororaphin row shares the pigment identity question, not a taxonomy identity. Existing registry scope and historical-source limitations apply to this separate case. No complete paper or structure verification is claimed from the limited archived page.",
"Primocarcin's historical abstract supplies a named antibiotic and empirical formula but not a verified exact structure at this review scope. The current registry owner remains the supported boundary. A plausible ontology candidate or formula alone is insufficient to promote a specific molecular identity.",
"The frozen raw Flour row says plain flour (supermarket) and g/L4. The corrected notes now preserve 4 g/L, rather than silently changing it to40. FOODON00004510 is generic flour, unlike flour food product00001056; neither the label nor source proves wheat or a closed molecular mixture.",
"The raw DL-Asparagine x H2O label explicitly selects a hydrate. Actual Wako SDS identity sections support DL-monohydrate CAS69833-18-7; the TCI3130-87-8 conflict remains visible. The generic asparagine parent relation is asymmetric, not L-specific NCIT or anhydrous exactness. The provider's derived molarity does not override the literal form.",
"The raw amphotericin preparation is 10 mg/mL. Its family name and historical owner do not choose A, B, a lipid/deoxycholate product or carrier. A source-qualified stock with an UNMAPPED generic part and UNKNOWN membership is feasible; the limited supplier comparisons cannot narrow it to amphotericin B.",
"The existing MES hydrate owner preserves CAS145224-94-8 separately from parent CHEBI39005. The generated alternate spelling adds no new source-grounded identity or alias obligation. No anhydrous exact mapping, fixed hydration count or redundant owner is inferred, and existing holds remain.",
"The complete frozen Fe4Po42 owner chemistry is ferric pyrophosphate, whereas literal Fe4(PO4)2 is malformed for that identity. The selected preferred-label correction and rejected raw token preserve this distinction. They do not establish what the original source intended or release that occurrence hold.",
"The D-(+)trehalose source does not establish a new hydrate or alpha/alpha supplied form beyond the existing CHEBI27082 scope. Full owner history retains unresolved CAS/form concerns. An unmatched label alone does not justify another substance or release the inherited native decisions."
]
proposal_appraisals = [
"CHEBI17418/CAS109-52-4 remains the straight-chain neutral acid. The added n-- and n - source aliases have direct recipe provenance. Entire inherited owner, chemistry, counts and history were inspected. Existing exact n-Pentanoate/Pentanoate labels remain a protonation-scope concern already held by reviewer A; acceptance is only the bounded new acid spellings, not full-owner alias/export approval.",
"CHEBI28484/CAS503-74-2 denotes branched3-methylbutanoic acid. Both raw iso spellings have recipe provenance, and the complete history records the earlier chemistry correction. Neither n-valeric identity, VFA composition nor source occurrence statistics are transferred. Inherited role support remains separately held.",
"CHEBI16183 is CH4. The complete owner retains rejected process labels and adds the gas-component spelling without turning a mixed headspace or production trait into a pure chemical. No amounts, atmosphere ratios or role approvals are added.",
"FOODON03302142 has canonical soybean flour and exact soy-flour synonym. The successor SYNONYM_MATCH corrects the actual lookup grade; it does not change ingredient identity to soy digest or a supplier-specific product. Full raw-source provenance, original history and supplied-form limits remain.",
"NCIT:C87433 has CAS5794-13-8 and exact L-Asparagine Monohydrate synonym in official OLS and the independently queried local26.02d database. Exact primary NCIT identity/CAS_RN_LOOKUP is supported. The stereospecific InChI is retained; the non-isomeric SMILES is explicitly connectivity-only. No DL owner or dependent component is silently rewritten, and historical parent assertions are preserved as history.",
"The new CHEBI42266 ethane owner is a molecular gas component. Official ontology support now uses DATABASE_MATCH; source applicability does not infer gas purity, complete atmosphere identity or literal success of the failed JCM request. Null beforeimage and duplicate-coordination obligations remain.",
"CHEBI100147 represents nalidixic acid, not sodium nalidixate or its stock. Readable NBRC1301 is positive support; NBRC1314/M2023 is explicitly unverified. The entire new owner has truthful database evidence and no invented salt, carrier or whole-stock alias. Occurrence hold survives candidate acceptance.",
"CHEBI17750/CAS107-43-7 represents the glycine-betaine inner salt. Both betaine and trimethylglycine source labels are supported; hydrochloride/hydrate records remain distinct. New mapping evidence is a direct database assertion, not human review or an inferred supplier grade.",
"CHEBI16007 is methanethiol. The new owner preserves the archived gas-component source witness and honestly recorded current retrieval failure. It contains no gas-mixture identity, derived mass dose, supplier purity or role claim; mapping evidence is now truthful database provenance.",
"CAS54-86-4 and sodium-containing formula identify sodium nicotinate. CHEBI15940 is only the broader acid parent under the repository salt convention; NARROW_MATCH preserves the salt boundary. CAS_RN_CROSS_REFERENCE reflects the actual NIST assertion. Bounded exact-term lookup and coordinator duplicate reconciliation remain explicit, without a speculative exact acid mapping.",
"The entire UNMAPPED0122 owner remains unpromoted. Notes/history now preserve actual JCM60 ISP5 facts, while the older Agar-extracted source lacks a proven version bridge. The absence of a component replacement is a scientific scope restriction, not failure to retrieve a known recipe. Counts, roles and old history are preserved.",
"The JCM906 registry stock retains 0.5 M glycine/CHEBI15428 and NaOH/CHEBI32145 at unreported titrant amount. RECIPE_TRANSCRIPTION and UNKNOWN closure correctly exclude the basal recipe's900 mL water from stock evidence. LLM_SUGGESTION truthfully describes the registry-scope decision; no final volume or neutralization speciation is fabricated.",
"TOGO M2844's indicator preparation contains bromothymol blue/CHEBI86155 at literal0.5% and KOH/CHEBI32035 at0.2 N. UNKNOWN closure preserves unspecified percent basis/carrier. The stock is not collapsed onto the KOH fragment, and the registry decision is identified as agent inference while primary recipe evidence remains intact.",
"JCM600's literal5 mM water-saturated toluene stock is distinct from pure CHEBI17578. Toluene5 mM and unquantified water/CHEBI15377 retain input scope; UNKNOWN avoids unsupported temperature/phase/closure assumptions. The water molecular reference does not attest to distilled-water processing or approve that owner's broad aliases.",
"The USB Peptic Pepton candidate preserves the opaque named product in NBRC19 without catalogue, digestion substrate or amino-acid recipe invention. UNDEFINED_MIXTURE and source-qualified registry identity are appropriate; agent choice is no longer labelled human evidence. No global equation of every peptic peptone is asserted.",
"Sulfide ore remains an undefined natural mixture, with DSMZ88's pyrite example not promoted to a mandatory FeS2 component. The entire candidate preserves preparation facts but supplies no false molecular formula or complete composition. Agent-authored registry scope is marked explicitly.",
"The existing cereal-leaf record is promoted only to a generic pre-extraction leaf material. CCAP recipes support leaf inputs, not a universal botanical species, Cerophyll product or final extract. Full old history and raw provenance remain, with no transfer of extraction water or receiving-medium amounts into material composition.",
"The0.5 M pH5.4 HOMOPIPES preparation retains CAS202185-84-0 solute as one named part. UNKNOWN membership is suitable because carrier and titrant are not established. Registry stock scope is agent interpretation; bare molecular HOMOPIPES remains separate and is not a global resolving stock alias.",
"The candidate preserves the explicit DL monohydrate, CAS69833-18-7, supported by Wako SDS. NARROW_MATCH to generic CHEBI22653 is asymmetric and does not assert NCIT's L hydrate or anhydrous identity. The conflicting TCI CAS is not silently adopted; raw source molarity is not treated as supplier specification.",
"Complete beta-NAD chemistry/identity matches NAD(+)/CHEBI15846. The bounded evidence change separates PubChem CAS provenance from ontology structure support. No NADH/disodium supplied-form identity or functional-role approval follows, and all previous history remains.",
"Generic Laminarin naming agrees with CHEBI6364/CAS9008-22-4 across brown algae. The earlier Laminaria digitata procurement detail is retained as supplied form/catalog provenance. No TOGO species attribution or species-specific duplicate chemical is invented; LLM naming interpretation is separated from inherited database evidence.",
"The opaque BD211260 Fluid Thioglycollate product is supported by actual ATCC474/177 pages and manufacturer context. The JCM157/TOGO product association is explicitly a bounded brand/recipe inference. The scratch ATCC177 alternative is not serialized as BD's formula, and no complete product chemistry or lot equivalence is claimed.",
"The full v3 R2A owner denotes MICRO0000541 liquid medium. Its six definition-level parts are yeast extract, proteose peptone, Casamino acids, glucose, starch and pyruvate; amounts and closure are unknown. Pyruvate/CHEBI15361 is not sodium pyruvate. CURATED_INTERPRETATION plus component-specific MANUAL_CURATION rationale now describes the derivation truthfully; that enum is distinct from human mapping evidence. All six parts and UNKNOWN remained unchanged in the F1 repair.",
"The R2A agar owner retains MICRO0000543 and its inherited human evidence. New agent provenance is separately classified. M2972 supports this source's agar sense, while bare R2A(Difco) remains excluded from global resolving aliases. The full historical formulation/roles are not newly approved by this bounded annotation.",
"Actual Denger2010 and Roy2003 Methods support a racemic sodium3-sulfolactate preparation, not neutral CHEBI38023 or an enantiopure stock. Registry identity plus asymmetric acid-parent relation is defensible. Sodium stoichiometry, hydration and purity remain unstated; no formula or structure is invented to fill those gaps.",
"MICRO0000113 canonical tryptic soy broth admits Trypticase soy broth as exact synonym, so SYNONYM_MATCH is truthful. Standard input recipe: casein digest17 g/L, papaic soy digest3, glucose2.5, NaCl5, K2HPO4 2.5 and water. The two digests remain UNMAPPED at exact process scope. COMPLETE concerns that standard enumeration, not lots or extra receiving-medium agar/NaCl. Full inherited roles remain held.",
"The stereounspecified sodium-lactate owner rejects the L-only and1 M/1% preparation labels without deleting source strings. CHEBI232798 independently demonstrates a distinct L-salt target. The source DL occurrence does not turn every generic owner occurrence into a racemate; the proposal's alias boundary does not release source/role holds.",
"This notes/history-only proposal records branded soydigest evidence while keeping the broad FOODON03315720 owner and sibling reconciliation explicitly held. Full active and tombstone sibling histories were inspected. Shared identifiers and historical merges are not proof of exact product equivalence or authorization to pick a live winner.",
"FOODON00004510 denotes generic flour, distinct from flour food product00001056. The corrected source transcription is4 g/L from the raw kg-microbe row. The full record does not assume wheat, defatting, a branded supermarket product or a defined chemical composition; new agent scope evidence is labelled honestly.",
"The10 mg/mL amphotericin stock retains a named UNMAPPED amphotericin part and UNKNOWN membership. The existing generic owner distinguishes the A/B/product ambiguity. Carrier, congener and formulation are not invented, and no bare molecular or B-product label becomes a global stock synonym.",
"The whole owner's formula/structure identify ferric pyrophosphate/CHEBI132767. Preferred naming and rejection of malformed Fe4(PO4)2 align active identity with that chemistry while preserving raw text. The original source's intended chemical remains held; this repair is not a silent source correction or whole-owner release."
]
assert len(case_appraisals)==51 and len(proposal_appraisals)==31

checks=[]
def check(name,cond,detail=None):
    checks.append({'check':name,'passed':bool(cond),'detail':detail})
    assert cond, name
check('exact case scope',set(H['case_ids'])==set(Ass['case_ids'])=={x['case_id'] for x in D} and len(D)==51)
check('exact proposal scope',set(H['proposal_ids'])==set(Ass['proposal_ids'])=={x['proposal_id'] for x in P} and len(P)==31)
for n,h in H['files'].items(): check('author artifact '+n,sha(A/n)==h)
baseD={d['case_id']:d for d in Ass['decisions']}; baseP={p['proposal_id']:p for p in Ass['proposals']}
for d in D:
    cid=d['case_id']
    check('canonical case '+cid,canon(d)==H['case_hashes'][cid])
    for k in ['source','case_input_sha256','occurrence_ids','preserved_native_decisions']:
        check('frozen field '+cid+' '+k,d[k]==baseD[cid][k])
    check('frozen case digest '+cid,canon(frozen[cid])==d['case_input_sha256'])
for p in P:
    pid=p['proposal_id'];path=R/p['after_capture']['path']
    check('payload '+pid,sha(path)==p['after_capture']['sha256']==H['payload_hashes'][pid])
    for k in ['kind','owner_path','before_sha256']:check('frozen proposal '+pid+' '+k,p[k]==baseP[pid][k])
    if p['before_sha256']:
        bp=pathlib.Path(p['owner_path']);check('beforeimage '+pid,sha(bp)==p['before_sha256'])
        before=yaml.safe_load(bp.read_text());after=yaml.safe_load(path.read_text())
        bh=before.get('curation_history',[]);check('history prefix '+pid,after.get('curation_history',[])[:len(bh)]==bh)
pd2={p['proposal_id']:p for p in P2};changed=[p['proposal_id'] for p in P if p['after_capture']!=pd2[p['proposal_id']]['after_capture']]
check('v3 changes one selected payload',changed==['op1201-r2a-medium'])
r2=P[22];r2old=yaml.safe_load((R/P2[22]['after_capture']['path']).read_text());r2new=yaml.safe_load((R/r2['after_capture']['path']).read_text())
check('R2A parts identical',r2new['components']==r2old['components'])
check('R2A only assertion and appended history change',{k for k in set(r2old)|set(r2new) if r2old.get(k)!=r2new.get(k)}=={'component_assertion','curation_history'})
check('R2A method corrected',r2new['component_assertion']['method']=='CURATED_INTERPRETATION' and r2new['component_assertion']['completeness']=='UNKNOWN')
check('R2A history prefix retained',r2new['curation_history'][:-1]==r2old['curation_history'])
check('R2A case only evidence backlink changes',[d['case_id'] for a,d in zip(D2,D) if a!=d]==[D[12]['case_id']] and {k for k in D[12] if D2[12][k]!=D[12][k]}=={'evidence_ids'})

used=sorted({eid for x in D+P for eid in x['evidence_ids']})
for eid in used:
    e=E[eid];c=e['capture'];path=(R if c['root']=='artifact' else Q)/c['path']
    check('capture '+eid,sha(path)==c['sha256'])

db=pathlib.Path('/Users/marcin/.data/oaklib/ncit.db');con=sqlite3.connect(db.as_uri()+'?mode=ro',uri=True)
query="select subject,predicate,value from statements where value='5794-13-8'"
rows=con.execute(query).fetchall();terms=con.execute("select subject,predicate,object,value from statements where subject='NCIT:C87433'").fetchall()
dbinfo={'reviewed_at':now,'mode':'sqlite read-only URI mode=ro','path':str(db),'sha256':sha(db),'version':con.execute("select subject,predicate,object,value from statements where predicate in ('owl:versionIRI','owl:versionInfo')").fetchall(),'query':query,'rows':rows,'term_statements':terms,'scope':'Independent exact CAS and term lookup; no global exact-term absence claim and no downloader or cache write.'}
check('NCIT exact CAS',rows==[('NCIT:C87433','NCIT:P210','5794-13-8')])
check('NCIT database bound',dbinfo['sha256']==read(A/'cas-lookup.json')['database_sha256'])
write('independent-ncit-query.json',dbinfo)

# Independent ignored-inclusive component-reference inventory, limited to
# dependency identity rather than approval of every referenced owner's roles.
all_assign=[]
for ap in (S/'research').glob('*/assignment.json'):all_assign.extend(read(ap)['proposals'])
baseline=list(pathlib.Path('data/ingredients').rglob('*.yaml'))
dep=[]
for scope,path in [('baseline',p) for p in baseline]+[('selected_assignment',R/p['after_capture']['path']) for p in all_assign]:
    v=yaml.safe_load(path.read_text())
    for i,c in enumerate(v.get('components',[])):
        if c.get('component_id') in ['cas:5794-13-8','NCIT:C87433']:dep.append({'scope':scope,'path':str(path),'index':i,'component':c})
check('no old/new NCIT component dependents in assigned baseline scope',not dep)
write('independent-dependent-reference-check.json',{'at':now,'scope':'pathlib.rglob includes ignored individual YAMLs; all113 assignment-selected payloads. Historical source/SSSOM/export mentions are not components and remain coordinator integration obligations.','baseline_files':len(baseline),'assignment_payloads':len(all_assign),'matches':dep})

matrix={x['proposal_id']:x for x in read(S/'inputs/coordinator-triage/all113-payload-action-matrix.json')}
lineage=[]
for f in read(S/'inputs/external-review/findings.json')['finding_groups']:
    relevant=set(f.get('proposal_ids',[]))&set(H['proposal_ids'])
    if relevant or f['finding_id']=='W08-IR-007':
        lineage.append({'finding_id':f['finding_id'],'original_severity':f['severity'],'historical_status':f['status'],'proposal_ids':sorted(relevant),'observations':[{'path':x.get('path'),'sha256':x.get('sha256'),'selector':x.get('selector'),'reviewer':x.get('observation',{}).get('reviewer'),'original_severity':x.get('observation',{}).get('severity')} for x in f.get('observations',[])],'current_disposition':'Reviewed in final selected organic payloads/source decisions; bounded correction accepted with original holds. No alteration of historical receipt.'})

case_reviews=[]
for d,app in zip(D,case_appraisals):
    case_reviews.append({'case_id':d['case_id'],'index_for_navigation':d['index_for_human_navigation'],'case_hash':canon(d),'frozen_case_sha256':d['case_input_sha256'],'source':d['source'],'occurrence_ids':d['occurrence_ids'],'proposal_ids':d['proposal_ids'],'source_evidence_ids':d['evidence_ids'],'finding_ids':['IF-OP1227-F1'] if d is D[12] else [],'status':'accepted_bounded_source_outcome_with_holds','appraisal':app,'preserved_native_decisions':d['preserved_native_decisions'],'whole_owner_role_or_export_approval':False})
proposal_reviews=[]
for p,app in zip(P,proposal_appraisals):
    pid=p['proposal_id'];old=matrix[pid];v=yaml.safe_load((R/p['after_capture']['path']).read_text())
    proposal_reviews.append({'proposal_id':pid,'case_ids':p['case_ids'],'owner_path':p['owner_path'],'before_sha256':p['before_sha256'],'after_capture':p['after_capture'],'after_sha256':p['after_capture']['sha256'],'full_payload_review':True,'appraisal':app,'source_evidence_ids':p['evidence_ids'],'finding_ids':['IF-OP1227-F1'] if pid=='op1201-r2a-medium' else [],'status':'accepted_for_bounded_correction_planning_with_holds','historical_review_binding':{k:old.get(k) for k in ['reviewer','review_receipt','review_receipt_sha256','review_verdict','payload_findings','associated_source_outcome_or_evidence_findings']},'component_count':len(v.get('components',[])),'whole_owner_role_or_export_approval':False})

findings={'reviewer':'/root/inorganics','author':'/root/organics','findings':[{'finding_id':'IF-OP1227-F1','coordinator_alias':'W08-1227-PEER-OP-001','severity':'P2','status':'resolved_in_exact_v3_successor','title':'R2A definition-derived constituents were mislabeled as source-label enumeration','proposal_ids':['op1201-r2a-medium'],'case_ids':[D[12]['case_id']],'reproduction':'The pre-fix six-part list is derived from MICRO0000541 annotation/definition, while the source label is only R2A. Native LABEL_ENUMERATION requires parts enumerated in the label.','before_capture':P2[22]['after_capture'],'after_capture':P[22]['after_capture'],'referral':{'path':str((O/'new-finding-referral-v1.json').relative_to(R)),'sha256':sha(O/'new-finding-referral-v1.json')},'coordinator_routing':{'path':str((S/'COORDINATOR-NEW-FINDINGS-v2.json').relative_to(R)),'sha256':sha(S/'COORDINATOR-NEW-FINDINGS-v2.json')},'resolution':'Re-read complete v3 payload and exact semantic delta: CURATED_INTERPRETATION with explicit agent rationale under the distinct ComponentEvidenceTypeEnum.MANUAL_CURATION; same six parts, references, quantities and UNKNOWN completeness; append-only LLM-assisted history. Only case/proposal evidence backlinks changed.','open_blocking':False}],'inherited_concerns':[{'proposal_id':'op-valeric-alias','status':'existing_hold_preserved_not_new_finding','detail':'Whole owner retains n-Pentanoate/Pentanoate exact aliases on neutral acid. Official ChEBI distinguishes conjugate-base CHEBI31011 from acid17418. External reviewer A already preserved this concern. New source-acid spellings do not approve these inherited aliases.'},{'proposal_id':'op1201-soy-family-source-boundary','status':'existing_hold_preserved_not_new_finding','detail':'Broad hydrolysate identity, active duplicates and the rejected Bacto Soytone tombstone require coordinated source-specific family curation. Notes-only proposal is not full-family approval.'}],'external_finding_lineage':lineage,'open_blocking_findings':[]}
write('findings.json',findings)
write('input-validation.json',{'at':now,'scope':'Independent hashes, frozen field preservation, exact v3 delta and read-only NCIT/dependency checks; not a substitute for scientific reading or native approval.','status':'PASS','checks':checks})

# The source ledger is prepared separately from these mechanical checks.
write('case-appraisals.json',{'reviewer':'/root/inorganics','author':'/root/organics','case_reviews':case_reviews})
write('proposal-appraisals.json',{'reviewer':'/root/inorganics','author':'/root/organics','proposal_reviews':proposal_reviews})
print(json.dumps({'cases':len(case_reviews),'payloads':len(proposal_reviews),'evidence_entries':len(used),'checks':len(checks),'status':'PASS'}))
