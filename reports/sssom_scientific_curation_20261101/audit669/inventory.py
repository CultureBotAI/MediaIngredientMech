from pathlib import Path
import collections, csv, datetime, hashlib, importlib.util, json, sys
import yaml

AUDIT=Path(__file__).resolve().parent
RUN=AUDIT.parent
MIM=RUN/'mim'
KG=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/kg-microbe')
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        while b:=f.read(8*1024*1024):h.update(b)
    return h.hexdigest()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
native=module('audit669_native',MIM/'scripts/validate_sssom_invariants.py')
loader=module('audit669_kg_loader',RUN/'claw/scripts/kgm_unified_mappings.py')
kg_path=KG/'mappings/kgmicrobe_unified_entity_mappings.sssom.tsv.gz'
kg_labels=loader.load_kgm_labels(kg_path)
prelude,fields,rows=native._read_sssom(MIM/'mappings/ingredient_mappings.sssom.tsv')
paths=native._subject_to_path();data={sid:yaml.safe_load(p.read_text()) for sid,p in paths.items()};owners=native._preferred_term_owners()
with (MIM/'mappings/other_cross_record_baseline.tsv').open() as f:baseline=list(csv.DictReader(f,delimiter='\t'))
basekeys={(b['subject_id'],b['token'].casefold()) for b in baseline}
native_failures=list(native.evaluate_rule_k(rows))
index=collections.defaultdict(list)
for n,row in enumerate(rows,1):index[row['subject_id']].append((n,row))
all_collisions=[]
for n,row in enumerate(rows,1):
    for token in row['other'].split('|'):
        token=token.strip();holders=owners.get(token.casefold(),frozenset())
        if holders and row['subject_id'] not in holders:
            all_collisions.append({'row_number':n,'token':token,'subject_id':row['subject_id'],'predicate_id':row['predicate_id'],'object_id':row['object_id'],'current_owners':sorted(holders),'baselined':(row['subject_id'],token.casefold()) in basekeys})
inventory=[]
for b in baseline:
    sid=b['subject_id'];token=b['token'];folded=token.casefold();record=data.get(sid,{})
    synonyms=[s for s in record.get('synonyms',[]) if isinstance(s,dict) and str(s.get('synonym_text','')).strip().casefold()==folded]
    actual=[]
    for n,row in index.get(sid,[]):
        if folded in {t.strip().casefold() for t in row['other'].split('|')}:
            name,alts=kg_labels.get(row['object_id'],('',[]))
            actual.append({'row_number':n,'row':row,'in_kg_target_aliases':folded in {str(x).casefold() for x in [name,*alts]},'kg_canonical_name':name,'kg_aliases_matching':[x for x in [name,*alts] if str(x).casefold()==folded]})
    holders=sorted(owners.get(folded,[]));holder_records=[]
    for holder in holders:
        d=data.get(holder,{})
        holder_records.append({'subject_id':holder,'path':str(paths.get(holder,'')),'identifier':d.get('identifier'),'preferred_term':d.get('preferred_term'),'mapping_status':d.get('mapping_status'),'ontology_mapping':d.get('ontology_mapping'),'representative':d.get('representative')})
    retired=[{'subject_id':s,'path':str(paths[s]),'identifier':d.get('identifier'),'representative':d.get('representative'),'mapping_status':d.get('mapping_status')} for s,d in data.items() if str(d.get('preferred_term','')).casefold()==folded and d.get('mapping_status')=='REJECTED']
    ownmap=record.get('ontology_mapping') or {}
    entry={**b,'subject_path':str(paths.get(sid,'')),'subject_sha256':sha(paths[sid]) if sid in paths else None,'subject_status':record.get('mapping_status'),'subject_identifier':record.get('identifier'),'subject_ontology_mapping':ownmap,'matching_yaml_synonyms':synonyms,'yaml_token_present':bool(synonyms),'stored_mapping_label_matches':str(ownmap.get('ontology_label','')).casefold()==folded,'current_owner_records':holder_records,'retired_owners':retired,'current_sssom_occurrences':actual,'still_collision':bool(actual) and bool(holders) and sid not in holders}
    inventory.append(entry)
inventory.sort(key=lambda x:(x['subject_id'],x['token']))
counts={'baseline_entries':len(baseline),'baseline_dispositions':dict(collections.Counter(x['disposition'] for x in baseline)),'canonical_rows':len(rows),'canonical_colliding_rows':len({x['row_number'] for x in all_collisions}),'canonical_colliding_tokens':len(all_collisions),'canonical_collision_pairs':len({(x['subject_id'],x['token'].casefold()) for x in all_collisions}),'unbaselined_native_failure_rows':len(native_failures),'unused_baseline_entries':sum(not x['still_collision'] for x in inventory),'yaml_backed_baseline_entries':sum(x['yaml_token_present'] for x in inventory),'non_yaml_baseline_entries':sum(not x['yaml_token_present'] for x in inventory),'kg_backed_non_yaml_entries':sum(not x['yaml_token_present'] and any(y['in_kg_target_aliases'] for y in x['current_sssom_occurrences']) for x in inventory)}
inputs=[MIM/'AGENTS.md',MIM/'MAPPING_SEMANTICS.md',MIM/'mappings/ingredient_mappings.sssom.tsv',MIM/'mappings/other_cross_record_baseline.tsv',MIM/'scripts/validate_sssom_invariants.py',RUN/'claw/scripts/kgm_unified_mappings.py',kg_path,*sorted(set(paths[x['subject_id']] for x in inventory if x['subject_id'] in paths)),*sorted(set(Path(y['path']) for x in inventory for y in x['current_owner_records'] if y['path']))]
result={'captured_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'counts':counts,'inventory':inventory,'collisions':all_collisions,'native_unbaselined_failures':[{'row_number':n,'row':r,'reason':reason} for n,r,reason in native_failures],'inputs':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in dict.fromkeys(inputs)],'scope':'Read-only native Rule K ownership and current canonical baseline inventory. KG alias membership is a present-input attribution clue, not proof of a historical build. No baseline exemptions removed; no source edits. Current native ownership includes mapped-directory records and credits retired names to explicit representative/identifier owners.'}
(AUDIT/'inventory.json').write_text(json.dumps(result,indent=2,default=str,ensure_ascii=False)+'\n')
print(json.dumps(counts,indent=2))
for x in inventory:print(x['subject_id'],repr(x['token']),'YAML='+str([(y.get('synonym_type'),y.get('source')) for y in x['matching_yaml_synonyms']]),'KG='+str(any(y['in_kg_target_aliases'] for y in x['current_sssom_occurrences'])),'owners='+','.join(y['subject_id'] for y in x['current_owner_records']))
