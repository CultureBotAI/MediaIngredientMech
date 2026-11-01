from pathlib import Path
import json,csv,datetime,collections,hashlib
A=Path(__file__).resolve().parent
I=json.loads((A/'inventory.json').read_text())
prs={n:{f['filename'] for f in json.loads((A/f'pr-{n}-files-all.json').read_text())} for n in [912,914]}
# These are recommendations about alias publication, not whole-record approval.
settled={
'4-Methyl-2-oxopentanoic_Acid_Sodium_Salt': ('salt_free_acid','PubChem CAS 4502-00-5 is sodium 4-methyl-2-oxovalerate, C6H9NaO3; ChEBI:48430 is the acid C6H10O3. The parent preferred name cannot assert exact substance identity for this sodium salt.',['sources/PubChem-CAS-4502-00-5.json','sources/CHEBI_48430.ols.json']),
'84_GL_NaHCO3_Solution': ('solution_solute','The maintained identity is explicitly a stock solution kgmicrobe.ingredient:84_gl_nahco3_solution, with concentration and solution curation; the owner NaHCO3 is neat sodium hydrogencarbonate CHEBI:32139. This is a mixture/concentration boundary, not merely spelling.',['sources/CHEBI_32139.ols.json']),
'Betaine_Hydrochloride': ('different_salt_hydrate','PubChem CAS 590-46-5 is betaine chloride C5H12ClNO2; the owner ChEBI:91242 is glycine betaine monohydrate C5H11NO2.H2O (CAS 590-47-6). Chloride and hydrate identities differ.',['sources/PubChem-CAS-590-46-5.json','sources/CHEBI_91242.ols.json']),
'D-Mannose_6-phosphate_Sodium_Salt': ('salt_free_acid','PubChem CAS 70442-25-0 is sodium mannose 6-phosphate C6H12NaO9P; ChEBI:17369 is D-mannose 6-phosphate C6H13O9P. The sodium counterion is chemically material.',['sources/PubChem-CAS-70442-25-0.json','sources/CHEBI_17369.ols.json']),
'MES_Hydrat': ('hydrate_anhydrous','PubChem CAS 145224-94-8 is MES hydrate C6H15NO5S; ChEBI:39005 is MES C6H13NO4S. This evidence supports a form boundary independent of KG alias availability.',['sources/PubChem-CAS-145224-94-8.json','sources/CHEBI_39005.ols.json']),
'Sn-glycerol_3-phosphate_Bis_Cyclohexylammonium_Salt': ('salt_free_acid','PubChem CAS 29849-82-9 is the bis(cyclohexylammonium) salt C15H35N2O6P; ChEBI:15978 is the free acid C3H9O6P. Removing the unqualified parent alias does not require guessing the salt identity.',['sources/PubChem-CAS-29849-82-9.json','sources/CHEBI_15978.ols.json']),
'Sodium_Perchlorate': ('anhydrous_hydrate','PubChem CAS 7601-89-0 is sodium perchlorate ClNaO4; CAS 7791-07-3 is monohydrate ClH2NaO5. ChEBI:132103 confirms the anhydrous subject.',['sources/PubChem-CAS-7601-89-0.json','sources/PubChem-CAS-7791-07-3.json','sources/CHEBI_132103.ols.json']),
}
held={
'24-diamino-67-di-iso-propylpteridine_phosphate': ('commercial_alias_scope','Vibriostat is a commercial/common reagent label; the current owner is a freebase ChEBI term, but this audit did not verify whether source usage means freebase or phosphate. Do not infer an invalid phosphate alias solely from the separate generic owner.'),
'Carnitine_Dl_Hydrochloride': ('contradictory_primary_identity','CAS 461-06-3 and PubChem CID288/ChEBI17126 identify DL-carnitine without chloride, while the preferred name says hydrochloride. Resolve the original material identity first; #1004 tracks this, no guessed CAS or rename.'),
'Carnitine_Hydrochloride': ('unresolved_salt_and_stereo','The local primary preserves an unspecified hydrochloride but has no independent exact salt evidence in this bounded audit; DL-carnitine scope needs source adjudication. The different amide alias fixed under #1003 is a separate settled wrong-compound defect and does not settle this baseline token.'),
'Magnesium_Chloride': ('shared_identity_duplicate_form','Both records currently use CHEBI:86345 (magnesium dichloride hexahydrate); the source CAS7791-18-6/formula also indicate hexahydrate. The token may be a valid same-substance alias; resolve duplicate/form identity, do not retire on dictionary absence.'),
'Na2glycerophosphate5h2o': ('salt_form_and_positional_identity','The salt/pentahydrate label is more specific than the free acid owner, but exact positional/stereochemical grounding and source salt identity were not independently settled here. Do not turn a generator omission into a full scientific ruling.'),
'Nh42ni_So42': ('shared_identity_duplicate_form','Both records use CHEBI:86149, which explicitly denotes ammonium nickel sulfate hexahydrate; source formula is also hexahydrate while its CAS differs. Resolve family/form identity, not a blanket synonym retirement.'),
'Sn-Glycerol_3-phosphate_Lithium_Salt': ('contradictory_primary_identity','CAS17989-41-2 and PubChem CID439162/ChEBI15978 are the free acid; the preferred label says lithium salt. #1005 requires original-source identity adjudication; previous rejected parent labels did not settle the primary identity.'),
'Sodium_Succinate_Dibasic': ('same_substance_identity','Source CAS150-90-3 and ChEBI:63675 both identify anhydrous disodium succinate C4H4Na2O4. The alias is not shown false; investigate duplicate/grounding relationship instead of automatically retiring it.'),
}
rows=[]
for i in I['inventory']:
 slug=i['subject_id'].removeprefix('MIM:')
 files={'data/ingredients/mapped/'+Path(i['subject_path']).name}|{'data/ingredients/mapped/'+Path(x['path']).name for x in i['current_owner_records']}
 overlaps={str(n):sorted(files&paths) for n,paths in prs.items() if files&paths}
 r={k:i[k] for k in ['subject_id','token','owned_by','disposition','subject_identifier','yaml_token_present','matching_yaml_synonyms','retired_owners']}
 r.update(subject_sha256=i['subject_sha256'],current_owner_records=i['current_owner_records'],row_selectors=[{k:o['row'][k] for k in ['subject_id','predicate_id','object_id']} for o in i['current_sssom_occurrences']],current_kg_target_alias=any(o['in_kg_target_aliases'] for o in i['current_sssom_occurrences']),record_overlap=overlaps)
 if i['yaml_token_present']:
  r.update(group='preserve_seven_policy_cases',reason='An extant typed YAML alias is also an official ChEBI synonym in at least related scope. Generic preferred-name owner is already first in the current label index. Unqualified SSSOM alias publication still needs an explicit consumer policy; preserve pending that choice.',recommendation='No automatic synonym retirement or identity merge; policy options in report and #669 comment.',evidence=['seven-generic-policy-pairs.json'])
 elif slug in settled:
  category,reason,evidence=settled[slug];r.update(group='bounded_scientific_removal_candidate',category=category,reason=reason,recommendation='Scientifically supportable removal from resolving unqualified alias publication, with preserved source provenance and native generation/receipt. Not applied in this run; full regeneration is not authorized for promotion.',evidence=evidence)
 elif overlaps:
  r.update(group='defer_active_pr912_family',category='active_hydrate_or_solution_family',reason='The subject or preferred-name owner belongs to open PR #912. The exact mapped primary identities, form distinctions, and ontology-owned synonyms require that family decision. Missing today from KG alias dictionary does not decide chemical validity.',recommendation='Preserve baseline; defer to coordinated family curation, and do not supersede or edit the overlapping record.',evidence=['pr-912-files-all.json','inventory.json','generated-alias-chebi-sources.json'])
 else:
  category,reason=held[slug];r.update(group='defer_identity_or_alias_ruling',category=category,reason=reason,recommendation='Preserve baseline and provenance pending the named identity or alias-scope ruling.',evidence=['inventory.json','generated-alias-chebi-sources.json','primary-pubchem-cas-sources.json'])
 for rel in r['evidence']:
  assert (A/rel).exists(),rel
 rows.append(r)
counts=dict(collections.Counter(r['group'] for r in rows))
result={'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'source_revision':'4625afd492b6cf43e3b499d1425d2453d490009d','source_inventory':'inventory.json','scope':'Pre-edit canonical collision inventory. Recommendations only, not whole-record scientific review or release approval. The separately authorized #1003 amide correction is outside these 45 tokens.','counts':counts,'pairs':rows,'full_file_overlap':{str(n):sorted(paths&{'data/curated/mapped_ingredients.yaml','data/curated/unmapped_ingredients.yaml','mappings/ingredient_mappings.sssom.tsv','mappings/other_cross_record_baseline.tsv','docs/data/label_index.csv','docs/data/ingredients.json'}) for n,paths in prs.items()}}
(A/'pair-dispositions.json').write_text(json.dumps(result,indent=2)+'\n')
with (A/'pair-dispositions.tsv').open('w') as h:
 w=csv.DictWriter(h,fieldnames=['subject_id','token','owned_by','group','category','current_kg_target_alias','record_overlap','reason'],delimiter='\t');w.writeheader()
 for r in rows:w.writerow({k:json.dumps(r[k]) if isinstance(r.get(k),(dict,list)) else r.get(k,'') for k in w.fieldnames})
print(json.dumps({'counts':counts,'full_file_overlap':result['full_file_overlap'],'retired_owners':sum(len(r['retired_owners']) for r in rows)},indent=2))
