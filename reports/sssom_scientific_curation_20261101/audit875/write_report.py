from pathlib import Path
import datetime,hashlib,json
ROOT=Path(__file__).resolve().parent;RUN=ROOT.parent
inputs=json.loads((ROOT/'input-manifest.json').read_text());record=json.loads((ROOT/'record-and-occurrence-audit.json').read_text())
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
sources=[]
for name in ['primary-fetch-manifest.json','exact-terms-fetch-manifest.json']:
 for s in json.loads((ROOT/'sources'/name).read_text()):
  sources.append({**s,'path':'sources/'+s['file']})
changes=[i['path'] for i in inputs if sha(Path(i['path']))!=i['sha256']]
report={
 'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'kind':'focused scientific curation audit input for root combined native review',
 'scientific_review':True,'coverage':'partial: exact identity/whole-form properties, prior decisions, source occurrences and PR914 overlap; BUFFER role scientific support not reassessed',
 'target':'data/ingredients/mapped/Na2hpo4_X_7_H2o.yaml',
 'verdict':'needs_curation; exact identity evidence settled, application awaiting unified rebuild coordination',
 'recommendation':{
  'primary_identifier':'NCIT:C61946','canonical_label':'Sodium Phosphate, Dibasic, Heptahydrate','ontology_version':'26.10d','ontology_active':True,
  'rule':'MAPPING_SEMANTICS §3 step 1 takes precedence over step 2 CAS fallback because an exact form-specific ontology term exists.',
  'cas_rn':'7782-85-6','fda_unii':'70WT22SF4B','pubchem_cid':6096963,
  'whole_form_formula':'H15Na2O11P','whole_form_mass_g_mol':'268.07',
  'whole_form_inchi':'InChI=1S/2Na.H3O4P.7H2O/c;;1-5(2,3)4;;;;;;;/h;;(H3,1,2,3,4);7*1H2/q2*+1;;;;;;;;/p-2',
  'whole_form_smiles':'O.O.O.O.O.O.O.OP(=O)([O-])[O-].[Na+].[Na+]',
  'identity_boundary':'NCIT:C61946 denotes the complete heptahydrate. CHEBI:34683 denotes the anhydrous salt and cannot be retained as an exact identity. A separately retained parent/component annotation must keep its non-identity scope and an approved representation; do not infer a new broadMatch merely from CAS promotion.',
  'mapping_quality_note':'An exact same-substance row uses skos:exactMatch. Record the actual verification method; the discovery here followed the FDA UNII link to a directly inspected exact NCI label/formula and CAS corroboration, not a blind CAS remap.',
 },
 'primary_evidence':[
  {'source':'NCI EVS NCIt','url':'https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full','snapshot':'sources/ncit-C61946.json','claim':'Active NCIT:C61946 explicitly names the dibasic heptahydrate; CAS_Registry=7782-85-6, Chemical_Formula=2Na.HO4P.7H2O, FDA_UNII_Code=70WT22SF4B.'},
  {'source':'FDA UNII','url':'https://precision.fda.gov/uniisearch/srs/unii/70WT22SF4B','snapshot':'sources/fda-unii.html','claim':'Names the dibasic heptahydrate, assigns CAS 7782-85-6 and seven-water formula, and links to NCIT:C61946.'},
  {'source':'PubChem PUG REST','url':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/7782-85-6/cids/JSON','snapshot':'sources/pubchem-cas-resolve.json','claim':'CAS query resolves CID6096963.'},
  {'source':'PubChem PUG REST','url':'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/6096963/property/MolecularFormula,MolecularWeight,InChI,InChIKey,CanonicalSMILES/JSON','snapshot':'sources/pubchem-properties.json','claim':'CID6096963 includes seven waters, H15Na2O11P,268.07 and heptahydrate InChI/SMILES. FDA-linked CID517013 independently returns the same formula/InChIKey.'},
  {'source':'ChEBI','url':'https://www.ebi.ac.uk/chebi/CHEBI:34683','snapshot':'sources/chebi-parent.json','claim':'Anhydrous term has HO4P.2Na and exactly the InChI/SMILES currently stored on the hydrate record; hydrate-specific entries visible under it are dihydrate and dodecahydrate.'},
 ],
 'bounded_chebi_search':{'queries':['7782-85-6','disodium hydrogenphosphate heptahydrate','sodium phosphate heptahydrate','heptahydrate','hydrogenphosphate','sodium phosphate'],'result':'No exact heptahydrate term found in these live OLS ChEBI query results; full results retained. This is bounded search coverage, not a claim that chemistry lacks the form.','returned_counts':{'CAS':0,'exact_name':0,'sodium_phosphate_heptahydrate':0,'heptahydrate':118,'hydrogenphosphate':12,'sodium_phosphate':44}},
 'duplicates':{'result':'No other maintained record has primary NCIT:C61946 or cas:7782-85-6 or current chemical_properties.cas_rn7782-85-6. Target alone currently owns that CAS.','scope':record['duplicate_search_scope'],'separate_stock':'Disodium_Phosphate_Heptahydrate_002_M_Stock is a concentration-qualified STOCK_SOLUTION with its own identity; it must not merge into the pure heptahydrate. Other-hydrate text hits are REJECTED_LABEL/history, not duplicate current identities.'},
 'current_surfaces':{'aggregate_equal':record['record_matches_aggregate'],'occurrences':{k:record[k] for k in ['current_culturemech_rows','distinct_recipes','occurrence_labels','occurrence_raw_identifiers']},'record_cached_occurrences':26,'sssom_rows':record['sssom_rows'],'ledger_rows':record['rejections']},
 'prior_decisions':{
  '863':'Merged PR withdrew the anhydrous kg_microbe_node_id and added rejection ledger; explicitly deferred own-CAS decision as875 and anhydrous structure as871. No scientific approval for the withheld mapping rows.',
  '334':'Hydrate-family CAS scrambling was explicit; x7 needs independent exact-form verification, not CAS-keyed merge. Current x3/x6 records no longer carry this CAS.',
  '459':'Comment establishes ChEBI coverage absence does not imply chemical impossibility and warns formula composition can conflate isomers. Current exact NCI evidence adds an ontology option absent from its ChEBI-only discussion.',
  'existing_semantic_finding':'SEM:cb9ec35166086d936f70 contains identity promotion, inherited anhydrous structure and provisional BUFFER role. Resolving identity alone cannot retire the whole finding.'},
 'pr914_overlap':{
  'head':'8dc2f266ebf72959a5d2f601d1c767c9138db44f','url':'https://github.com/CultureBotAI/MediaIngredientMech/pull/914','diff':'sources/pr-914.diff',
  'target_yaml':'No target YAML modification in PR #914.',
  'aggregate':'No target-record hunk in PR #914 mapped aggregate; common aggregate path alone is not a semantic conflict.',
  'ledger':'Existing Na2HPO4 x7 H2O ledger row is unchanged context in PR #914. Updating its mim_id is a disjoint row edit despite shared ledger path; other rows are added by914.',
  'unified':'Direct same-row overlap: PR914 changes Na2HPO4 x7 H2O occurrence_count from 19 to 28 and retains localID; identity promotion changes that same row to NCIT:C61946 and changes hydrate alias rows. Required unified regeneration/provenance belongs to active914. Coordinate this before application under user nonoverlap instruction.',
  'fail_closed_coupling':'Claw build_unified_ingredient_mapping.load_mapping_rejections checks ledger mim_id equals live MIM label resolution and raises rejection disagrees with MIM identity. Moving primary without paired ledger update is invalid.'},
 'supported_future_fix_scope':[
  'Guarded target-only identifier and ontology_mapping promotion to exact NCIT:C61946, with direct primary-source evidence and an append-only honest curation event; preserve preferred formula name, accepted same-hydrate synonyms, rejected sibling labels and history.',
  'Synchronize mapped aggregate and native label/browser exports; regenerate only owned SSSOM identities through supported builder and mapping-change receipt chain. Do not claim supported scientific approval from a regenerated row.',
  'Move the existing stale-CHEBI rejection ledger mim_id to NCIT:C61946 in the same identity change and update its no-exact-term/CAS-only rationale; keep CHEBI:34683 rejected as unified identity.',
  'Coordinate unified snapshot rebuild/provenance with activePR914 rather than independently rebuilding/overwriting its work.',
  'Separately reviewed structure correction can replace inherited anhydrous InChI/SMILES with the exact seven-water PubChem values and matching provenance; this is supported by inspected source but was not applied.',
  'Do not close broader SEM finding without separately addressing or retaining the BUFFER evidence and chemical-structure scopes.'
 ],
 'options':[{'option':'Evidence/report only now','recommendation':True,'reason':'Preserves user nonoverlap restriction while fixing875 decision from CAS-only to exact NCIT; no scientific data touched.'},{'option':'Coordinated atomic identity promotion','recommendation':False,'reason':'Use exact NCIT plus paired ledger/receipts and unified refresh only after914 coordination authorizes an ownership split or follow-up.'}],
 'validation_checks':[json.loads((RUN/'logs'/f'{name}.json').read_text()) for name in ['audit875_strict','audit875_terms']],
 'limitations':['CAS Common Chemistry detail page returned403 via browsing and API401; no CAS credentials, paid provider or access bypass used. CAS association is independently explicit in NCI/FDA and confirmed byPubChem.','BUFFER role evidence was not scientifically reassessed.','This is evidence input for the root combined native structured review, not a saved native review bundle or release approval.','No broader corpus curation, provider calls, GitHub mutations, source YAML edits or qc-evidence workflow edits were performed.'],
 'source_inputs_changed_since_capture':changes,
 'source_manifests':['sources/primary-fetch-manifest.json','sources/exact-terms-fetch-manifest.json','input-manifest.json']
}
(ROOT/'audit875.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
md='''# Issue #875 scientific audit

The supported primary identity is **NCIT:C61946 — Sodium Phosphate, Dibasic, Heptahydrate**, not the CAS fallback proposed by the issue. NCI's active 26.10d record explicitly binds the exact name, CAS 7782-85-6, seven-water formula 2Na.HO4P.7H2O and FDA UNII 70WT22SF4B. MAPPING_SEMANTICS §3 step 1 therefore precedes step 2.

Inspected primary sources: [NCI EVS](https://api-evsrest.nci.nih.gov/api/v1/concept/ncit/C61946?include=full), [FDA UNII](https://precision.fda.gov/uniisearch/srs/unii/70WT22SF4B), [PubChem CAS resolution](https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/7782-85-6/cids/JSON), [PubChem CID6096963](https://pubchem.ncbi.nlm.nih.gov/compound/6096963), and [ChEBI anhydrous parent](https://www.ebi.ac.uk/chebi/CHEBI:34683). Raw responses, URLs, timestamps and SHA256 digests are retained under sources/. CAS Common Chemistry was inaccessible (HTTP 403 for the page; 401 for the API); this is an access limitation, not negative evidence.

NCIT denotes the complete hydrate. CHEBI:34683 denotes the anhydrous salt and cannot become its exact identity. Any separately retained parent/component assertion needs its own honest nonidentity representation; do not turn the current CLOSE_MATCH into broadMatch merely because CAS is verified. The repository's singular ontology_mapping can point to the exact NCI term; any legacy parent relation must follow a supported separate representation or stay historical.

No other maintained record owns NCIT:C61946 or current CAS 7782-85-6 in an ignored-inclusive record search. The 0.02 M stock is a distinct prepared solution and must remain separate. Current CultureMech output has 35 explicitly heptahydrate occurrences across 35 recipes:28 preferred formula,4 dot notation,3 middle-dot notation. Of these, 32 already resolve to the local heptahydrate identity, 2 are unresolved and 1 still carries anhydrous CHEBI:34683. The stored 26 occurrences are historical and not current; this audit did not update them.

The YAML and aggregate agree. Its InChI/SMILES are byte-equivalent to anhydrous ChEBI:34683, whereas PubChem 6096963 carries seven waters, H15Na2O11P,268.07 g/mol and InChIKey PYLIXCKOHOHGKQ-UHFFFAOYSA-L. That structure repair is separately supported and tracked in prior review and #871. The provisional BUFFER evidence was not reassessed. Existing SEM:cb9ec35166086d936f70 covers all three topics, so identity alone cannot close it.

PR #914 exact overlap: target YAML and target aggregate entry are unchanged. Its ledger target row is unchanged context, so sharing the ledger file is not itself a semantic conflict. However, PR #914 changes the exact unified heptahydrate row's occurrence_count from 19 to 28 and rebuilds the unified snapshot/provenance; identity promotion would change that row and aliases too. The required unified rebuild remains coordination work. Claw rejects a primary/ledger mismatch, so the target's existing ledger mim_id must move atomically with any promotion.

Recommended now: keep this evidence/report, preserve the exact NCIT decision, and coordinate the atomic target+ledger+SSSOM receipt+unified-refresh change with PR #914. Do not independently apply a CAS-only promotion or overwrite its unified work. No scientific inputs were edited.

Detailed evidence, scope, bounded ChEBI search, prior decisions and proposed acceptance scope: audit875.json. Native structured review is being consolidated by the root agent.
'''
(ROOT/'audit875.md').write_text(md)
manifest=[]
for p in sorted(ROOT.rglob('*')):
 if p.is_file() and p.name!='artifact-manifest.json':manifest.append({'path':str(p.relative_to(ROOT)),'sha256':sha(p),'bytes':p.stat().st_size})
(ROOT/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps({'report':'audit875.json','artifacts':len(manifest),'changed_inputs':changes},indent=2))
