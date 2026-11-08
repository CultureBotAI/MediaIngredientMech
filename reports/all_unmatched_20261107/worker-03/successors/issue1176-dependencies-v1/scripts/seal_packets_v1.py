import pathlib,json,hashlib,datetime,os,shutil
O=pathlib.Path(__file__).resolve().parents[1];R=next(p for p in O.parents if (p/'MAPPING_SEMANTICS.md').is_file());P=R/'reports/all_unmatched_20261107/worker-03/successors/issue1176-dependencies-v1'
def sha(b):return hashlib.sha256(b).hexdigest()
receipt=O/'assembly/final-content-review.json';d=json.loads(receipt.read_text());assert d['status'].startswith('PASS'),d['status']
additions=[]
for rel in ['assembly/final-content-review.json','scripts/seal_packets_v1.py']:
 src=O/rel;dst=P/rel;assert not dst.exists();dst.parent.mkdir(parents=True,exist_ok=True);dst.write_bytes(src.read_bytes());additions.append({'path':rel,'sha256':sha(src.read_bytes())})
supp={'original_copy_index_sha256':sha((P/'publication-copy-index.json').read_bytes()),'additional_final_assembly_files':additions,'reason':'Exact independent assembly receipt and seal producer are added after initial copied packet review. Neither changes reviewed inputs/payloads; allregularfiles covered by finalmanifest.'}
for root in [O,P]:(root/'publication-copy-additions.json').write_text(json.dumps(supp,indent=2)+'\n')
for root in [P,O]:
 members=[];links=[]
 for q in sorted(root.rglob('*')):
  rel=str(q.relative_to(root))
  if rel in ['MANIFEST.json','SHA256SUMS','PUBLICATION-RECEIPT.json']:continue
  if q.is_symlink():links.append({'path':rel,'kind':'symlink_descriptor','target':os.readlink(q),'sha256_of_link_text':sha(os.readlink(q).encode())});continue
  if q.is_file():members.append({'path':rel,'sha256':sha(q.read_bytes()),'bytes':q.stat().st_size})
 assert not (root/'MANIFEST.json').exists();assert not (root/'SHA256SUMS').exists()
 manifest={'algorithm':'sha256','sealed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'root':str(root.relative_to(R)),'members':members,'member_count':len(members),'symlink_descriptors':links,'excluded':['MANIFEST.json (self)','SHA256SUMS (transport)','PUBLICATION-RECEIPT.json (postpublication detached receipt; private only)'],'scope':'Exact task evidence and report-only dependency successor. Onlydependency-selection.json/payloads-v2 selected. Negativefixtures and old versions are historical; not maintained or accepted owner assertions.'}
 (root/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
 sums=''.join(x['sha256']+'  '+x['path']+'\n' for x in members)+sha((root/'MANIFEST.json').read_bytes())+'  MANIFEST.json\n';(root/'SHA256SUMS').write_text(sums)
 print(json.dumps({'root':str(root.relative_to(R)),'members':len(members),'symlinks':len(links),'HANDOFF':sha((root/'HANDOFF.json').read_bytes()),'MANIFEST':sha((root/'MANIFEST.json').read_bytes()),'SHA256SUMS':sha((root/'SHA256SUMS').read_bytes())}))
