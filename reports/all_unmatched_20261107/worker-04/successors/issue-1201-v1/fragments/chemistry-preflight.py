import json,pathlib,hashlib,re,subprocess,yaml
B=pathlib.Path('reports/all_unmatched_20261107/worker-04');S=B/'successors/issue-1201-v1';C=S/'captures/chemistry';C.mkdir(parents=True,exist_ok=True)
a=json.loads((S/'fragments/chemistry-assignment.json').read_text())['cases'];p=json.loads((B/'proposals.json').read_text())['proposals'];d=json.loads((B/'decisions.json').read_text())['decisions']
print('published',len(p),len(d))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
patterns={4:'titanium|TiCl',6:'potassium.*glutam|glutam.*potassium',10:'quinic',13:'ferric.*citrate|dicitrate|Fe.*citrate',19:'sodium.*citrate|Na.*citrate',27:'64758|EDTA',30:'ferric.*citrate|Fe.*citrate',31:'citrate.*5|citrate.*penta|6858-44-2',32:'molybdate|Mo7',47:'glutamat',54:'molybdate|Mo7',59:'tungstate|Na2WO4',60:'citrate.*3|citrate.*trihydrate',62:'glutamat',63:'ketoglut',73:'64758|EDTA',80:'sodium chloride|NaCl|NaCI',87:'tartrat',90:'inositol|B7',95:'citrate',102:'molybdate|Mo7',107:'tungstate|Na2WO4',119:'molybdate|Mo7',120:'feredetate|FeNaEDTA|sodium.*iron.*EDTA|EDTA',125:'EDTA',126:'Tris',132:'fumarate',138:'citrate',139:'tungstate|Na2WO4',147:'citrate',148:'citrate.*5|citrate.*penta|6858-44-2',150:'citrate.*3|citrate.*trihydrate',151:'laurat|dodecanoate',154:'ardacin|aridicin',157:'Mg.citrate|magnesium.*citrate|131389|131391',159:'sulfite|Na2SO3',162:'grisamine',169:'64758|EDTA',170:'ketoglut',172:'HEPES|hydroxyethyl.*piperazine',174:'actinomycetin',175:'64758|EDTA',184:'actinomycetin',186:'fumarate'}
rows=[]
for x in a:
 n=x['index'];pat=patterns[n];cmd=['rg','-uu','-n','-i','--glob','*.yaml',pat,'data/ingredients',str(B/'proposals')]
 q=subprocess.run(cmd,text=True,capture_output=True);indexq=subprocess.run(['rg','-uu','-n','-i',pat,'docs/data/label_index.csv'],text=True,capture_output=True)
 out={'index':n,'case_id':x['frozen_case']['case_id'],'commands':[cmd,['rg','-uu','-n','-i',pat,'docs/data/label_index.csv']],'ignored_files_included':True,'returncodes':[q.returncode,indexq.returncode],'stdout':q.stdout,'label_index_stdout':indexq.stdout,'stderr':q.stderr+indexq.stderr,'published_proposal_hits':[],'related_original_cases':[]}
 for pp in p:
  capture=pp['after_capture'];payload=(B/capture['path']).read_text();assert sha(B/capture['path'])==capture['sha256']
  if re.search(pat,payload,re.I):out['published_proposal_hits'].append({'proposal_id':pp['proposal_id'],'owner_path':pp['owner_path'],'case_ids':pp['case_ids'],'after_capture':capture})
 for dd in d:
  if re.search(pat,dd['source']['source_label'],re.I):out['related_original_cases'].append({'case_id':dd['case_id'],'label':dd['source']['source_label'],'proposal_ids':dd['proposal_ids']})
 path=C/f'lookup-{n:03d}.json';path.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n');rows.append({'index':n,'path':str(path.relative_to(B)),'sha256':sha(path),'published_proposal_ids':[z['proposal_id'] for z in out['published_proposal_hits']]})
(C/'lookup-index.json').write_text(json.dumps(rows,indent=2)+'\n')
print('44 ignored-inclusive lookup receipts and63 proposal exact-hash checks complete')
