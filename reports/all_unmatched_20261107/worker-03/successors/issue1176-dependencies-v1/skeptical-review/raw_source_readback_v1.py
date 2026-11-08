import json,zipfile,csv,io,pathlib,hashlib,datetime
R=pathlib.Path.cwd();O=R/'.temp/peptone-final-dependencies-v1/skeptical-review';p=R/'.temp/peptone-consumer-independent-v1/other/captures/microbedecoder_database.zip';sha=lambda b:hashlib.sha256(b).hexdigest()
with zipfile.ZipFile(p) as z:
 b=z.read('database.csv'); rows=list(csv.DictReader(io.StringIO(b.decode('latin1'))))
 out=[]
 for n,label,species in [(3351,'GYPS','sporogenes'),(4105,'PYGS','frigidicarnis'),(4110,'PYGS','gasigenes'),(8884,'PYGS','algidixylanolytica')]:
  r=rows[n-2];assert r['Bergey_Substrates_for_end_products']==label and r['Species']==species
  out.append({'row_including_header':n,'field':'Bergey_Substrates_for_end_products','literal':label,'source_context':{k:r[k] for k in ['Genus','Species','Bergey_Genus','Bergey_Species','Bergey_Article_link']},'important_limit':'Bind to the exact Bergey/source-specific substrate context, not disparate adjacent database taxonomy columns; no new organism assertion approval.'})
 data={'reviewer':'/root/peptone_final_skeptic','read_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive_path':str(p),'archive_sha256':sha(p.read_bytes()),'member':'database.csv','member_sha256':sha(b),'encoding':'latin1','readbacks':out,'literal_is_component_proof':False,'primary_component_support':'Separate three primary abstract contexts and Alain original GYPS culture method, as recorded in primary-skeptical-assessment-v1.json.'}
 target=O/'raw-source-readback-v1.json';assert not target.exists();target.write_text(json.dumps(data,indent=2)+'\n');print(sha(target.read_bytes()))
