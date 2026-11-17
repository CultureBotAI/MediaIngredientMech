from pathlib import Path
import csv,collections,datetime,hashlib,json,shutil
ROOT=Path(__file__).resolve().parent
KG=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe-mim-1788-20261107')
def sha(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def snap(path):
 dest=ROOT/'snapshots'/path.relative_to(KG);dest.parent.mkdir(parents=True,exist_ok=True)
 if dest.exists():assert sha(dest)==sha(path)
 else:shutil.copyfile(path,dest)
 return {'path':str(path.relative_to(KG)),'snapshot':str(dest.relative_to(ROOT)),'sha256':sha(path),'bytes':path.stat().st_size,'mtime_utc':datetime.datetime.fromtimestamp(path.stat().st_mtime,datetime.timezone.utc).isoformat()}
additional=[];graph_proofs=[];candidates=[]
for source in ['metatraits','metatraits_gtdb']:
 nodes=KG/'data/transformed'/source/'nodes.tsv';edges=nodes.with_name('edges.tsv');marker=json.loads(nodes.with_name('source_finalization.json').read_text());additional.append(snap(nodes));assert sha(nodes)==marker['members']['nodes.tsv']['sha256']
 with nodes.open() as f: selected={r['id']:r for r in csv.DictReader(f,delimiter='\t') if r['id'].startswith('kgmicrobe.compound:')}
 count=collections.Counter();pred=collections.defaultdict(collections.Counter);digest=hashlib.sha256();before=edges.stat()
 with edges.open('rb') as f:
  def lines():
   for b in f:digest.update(b);yield b.decode('utf-8')
  rows=csv.DictReader(lines(),delimiter='\t')
  total=0
  for r in rows:
   total+=1
   for ident in {r.get('subject',''),r.get('object','')} & selected.keys():
    count[ident]+=1;pred[ident][r['predicate']]+=1
 after=edges.stat();assert (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns);assert digest.hexdigest()==marker['members']['edges.tsv']['sha256']
 graph_proofs.append({'source':source,'edges_path':str(edges),'edges_sha256':digest.hexdigest(),'edge_rows':total,'compound_placeholders':len(selected),'native_finalization_hash_matches':True,'count_definition':'Current graph edges incident to this exact source node ID; one count per edge, not recipe frequency.'})
 for ident,r in sorted(selected.items()):candidates.append({'source':source,'source_id':ident,'source_label':r.get('name',''),'raw_source_label':r.get('name',''),'category':r.get('category',''),'occurrences':count[ident],'occurrences_definition':'current_graph_incident_edges','predicate_counts':json.dumps(dict(pred[ident]),sort_keys=True),'node_record_json':json.dumps(r,sort_keys=True,ensure_ascii=False)})
 print(source,'placeholder rows',len(selected),'graph edges',total,flush=True)
with (ROOT/'queues/other-current-compound-placeholders.tsv').open('x',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(candidates[0]),delimiter='\t');w.writeheader();w.writerows(candidates)
for name in ['mediadive_material_scope_quarantine.tsv','mediadive_oatmeal_identity.tsv','mediadive_substrate_identity.tsv']:
 additional.append(snap(KG/'data/transformed/mediadive'/name))
marker=json.loads((KG/'data/transformed/mediadive/source_finalization.json').read_text())
for key in ['material_scope_context_policy','material_scope_reviewed_claims','mediadive_recipe_identity_evidence','mediadive_recipe_identity_policy','mediadive_unknown_disposition_policy','mediadive_unknown_policy','mediadive_generation_manifest','mediadive_generation_pointer']:
 rec=marker['consumed_inputs'][key];p=Path(rec['path']);assert sha(p)==rec['sha256'];additional.append(snap(p))
(ROOT/'additional-sources.json').write_text(json.dumps({'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':additional,'graph_proofs':graph_proofs},indent=2)+'\n')
print('saved other compound rows',len(candidates))
