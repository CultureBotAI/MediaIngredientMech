from pathlib import Path
import collections, csv, datetime, hashlib, importlib.util, json, re, sys
import yaml

HERE=Path(__file__).resolve().parent
RUN=HERE.parent
MIM=RUN/'mim'
OLD=RUN.parent/'sssom-generation-20261031T213407Z'
CANDIDATE=MIM/'output/sssom-followup-684-686/ingredient_mappings.sssom.tsv'

def read(path):
    return list(csv.DictReader((line for line in path.open() if not line.startswith('#')),delimiter='\t'))

def artifact(path):
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())

def key(row):
    return row['subject_id'],row['object_id']

def selector(row):
    return {field:row[field] for field in ['subject_id','predicate_id','object_id']}

def header(path):
    return {m.group(1):m.group(2).strip().strip('"') for line in path.read_text().splitlines()
            if (m:=re.match(r'^#\s*(mapping_date|mapping_set_version|predicate_semantics):\s*(.*)$',line))}

def compare(before,after):
    left={key(r):r for r in before};right={key(r):r for r in after}
    assert len(left)==len(before) and len(right)==len(after)
    changes=[];fields=collections.Counter();other=[]
    for k in sorted(left.keys()|right.keys()):
        if k not in left:changes.append({'change':'added','after':right[k]})
        elif k not in right:changes.append({'change':'removed','before':left[k]})
        elif left[k]!=right[k]:
            diff={f:{'before':left[k].get(f),'after':right[k].get(f)} for f in left[k].keys()|right[k].keys() if left[k].get(f)!=right[k].get(f)}
            fields.update(diff.keys())
            changes.append({'change':'changed','selector':selector(right[k]),'fields':diff})
            if 'other' in diff:
                a=set(filter(None,left[k]['other'].split('|')));b=set(filter(None,right[k]['other'].split('|')))
                other.append({'selector':selector(right[k]),'before':left[k]['other'],'after':right[k]['other'],
                              'removed_tokens':sorted(a-b),'added_tokens':sorted(b-a)})
    return {'counts':dict(collections.Counter(r['change'] for r in changes)),
            'changed_fields':dict(fields),'equal_payload_rows':sum(left[k]==right[k] for k in left.keys()&right.keys()),
            'changes':changes,'other_changes':other}

old_path=OLD/'repo/output/raw-candidate/ingredient_mappings.sssom.tsv'
canonical_path=MIM/'mappings/ingredient_mappings.sssom.tsv'
old=read(old_path);current=read(CANDIDATE);canonical=read(canonical_path)
previous_path=MIM/'output/sssom-repair/final-code-replay-r2.sssom.tsv'
previous=read(previous_path);previous_comparison=compare(previous,current)
previous_removed=[x['before'] for x in previous_comparison['changes'] if x['change']=='removed']
previous_added=[x['after'] for x in previous_comparison['changes'] if x['change']=='added']
assert len(previous_removed)==len(previous_added)==1, previous_comparison
before=previous_removed[0];after=previous_added[0]
alias_before=dict(before);alias_after=dict(after)
assert before['subject_id']==after['subject_id']=='MIM:Sodium_Nitrate_070_M_Stock'
assert before['object_id']=='kgmicrobe.compound:sodium_nitrate_070_m_stock'
assert after['object_id']=='kgmicrobe.ingredient:sodium_nitrate_070_m_stock'
assert all(before[k]==after[k] for k in before if k not in {'object_id','object_source','comment','validation_method'})
assert before['validation_method']=='none|UNKNOWN_TERM|2026-07-07' and after['validation_method']==''
assert previous_comparison['counts'].get('changed',0)==0, previous_comparison
assert header(previous_path)==header(CANDIDATE)

old_comparison=compare(old,current);canonical_comparison=compare(canonical,current)
spec=importlib.util.spec_from_file_location('native_reconcile',MIM/'scripts/reconcile_sssom.py')
native=importlib.util.module_from_spec(spec);spec.loader.exec_module(native)
aggregate=yaml.load((MIM/'data/curated/mapped_ingredients.yaml').read_text(),Loader=yaml.CSafeLoader)
drift=native.find_drift(aggregate,current)
lookup={key(r):r for r in current}
rejections=read(OLD/'repo/output/raw-candidate/rejected-rows.tsv')
outcomes=[]
for r in rejections:
    rule='G' if r['subject_id'].startswith('(header ') else re.search(r'Rule (\w+):',r['reject_reason']).group(1)
    outcome={'rule':rule,'original_reason':r['reject_reason'],'original_selector':selector(r)}
    if rule=='G':
        field=r['subject_id'][8:-1]
        outcome.update(field=field,before=header(old_path)[field],after=header(CANDIDATE)[field],newest_row_date=max(x['mapping_date'] for x in current),disposition='header_matches_newest_row_date')
        assert outcome['after']==outcome['newest_row_date']
    elif rule=='B5':
        path=MIM/'data/ingredients/mapped'/(r['subject_id'][4:]+'.yaml')
        d=yaml.safe_load(path.read_text());present=key(r) in lookup
        outcome.update(maintained_owner=str(path),primary_identifier=d['identifier'],present_after=present,
                       disposition='maintained_primary_identity_retained' if present else 'surplus_registry_identity_removed')
        assert present==(d['identifier']==r['object_id'])
    elif rule=='K':
        token=r['reject_reason'].split('["\'')[1].split("'")[0]
        after=lookup[key(r)]
        outcome.update(token=token,before=r['other'],after=after['other'],disposition='inherited_object_alias_removed')
        assert token.casefold() not in {t.casefold() for t in after['other'].split('|')}
        assert after['predicate_id']==r['predicate_id']
    outcomes.append(outcome)

# Verify every removed registry row was one of the original B5 surplus rows.
removed=[r['before'] for r in old_comparison['changes'] if r['change']=='removed']
expected_removed={tuple(o['original_selector'][f] for f in ['subject_id','object_id']) for o in outcomes if o['disposition']=='surplus_registry_identity_removed'}
assert expected_removed.issubset({key(r) for r in removed}) and len(removed)==15
assert old_comparison['counts'].get('added',0)==1
assert old_comparison['changed_fields'].get('predicate_id',0)==0
assert len(outcomes)==41
assert not any(drift.values()),drift

sys.path.insert(0,str(RUN/'claw/scripts'))
import build_mim_ingredient_sssom as builder
by_subject={builder._mim_curie(p.name):p for p in (MIM/'data/ingredients/mapped').glob('*.yaml')}
removed_curated=[]
for change in old_comparison['other_changes']:
    d=yaml.safe_load(by_subject[change['selector']['subject_id']].read_text())
    owned={(s.get('synonym_text') or '').strip().casefold() for s in d.get('synonyms',[]) if builder._is_publishable_mim_synonym(s)}
    matches=[t for t in change['removed_tokens'] if t.casefold() in owned]
    if matches:removed_curated.append({'selector':change['selector'],'removed_curated_tokens':matches})
assert not removed_curated,removed_curated

review=json.loads((MIM/'reports/sssom_completion_20260921/review.json').read_text())
dispositions=read(OLD/'repo/output/reviewed-release/mapping-dispositions.tsv')
held=[r for r in dispositions if (r['subject_id'],r['object_id'],r['predicate_id']) in {
    (o['original_selector']['subject_id'],o['original_selector']['object_id'],o['original_selector']['predicate_id']) for o in outcomes if o['rule']=='K'}]
assert len(held)==11 and all(r['disposition']=='WITHHOLD' for r in held)
prior_source_sha=json.loads((OLD/'repo/output/reviewed-release/manifest.json').read_text())['source_sha256']
assert hashlib.sha256(canonical_path.read_bytes()).hexdigest()==prior_source_sha

summary={
    'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'artifacts':{'old_candidate':artifact(old_path),'new_candidate':artifact(CANDIDATE),'maintained_canonical':artifact(canonical_path)},
    'rows':{'old_candidate':len(old),'previous_repaired_candidate':len(previous),'new_candidate':len(current),'maintained_canonical':len(canonical)},
    'versus_previous_repaired_candidate':{k:v for k,v in previous_comparison.items() if k not in {'changes','other_changes'}},
    'previous_repaired_candidate':artifact(previous_path),
    'intentional_registry_alias_change':{'before':alias_before,'after':alias_after,'scope':'Generated subject-slug alias changes to the curated identifier namespace. Curated primary identifier and parent relation remain unchanged; this is an intentional registry object identity change, not a zero-identity-change claim.'},
    'row_dates_changed_from_previous_repair':0,
    'header_previous_repair':header(previous_path),
    'versus_old_candidate':{k:v for k,v in old_comparison.items() if k not in {'changes','other_changes'}},
    'versus_maintained_canonical':{k:v for k,v in canonical_comparison.items() if k not in {'changes','other_changes'}},
    'new_candidate_native_drift':{k:len(v) for k,v in drift.items()},
    'original_rejection_counts':dict(collections.Counter(o['rule'] for o in outcomes)),
    'remediation_dispositions':dict(collections.Counter(o['disposition'] for o in outcomes)),
    'removed_other_tokens':sum(len(r['removed_tokens']) for r in old_comparison['other_changes']),
    'added_other_tokens':sum(len(r['added_tokens']) for r in old_comparison['other_changes']),
    'removed_curated_subject_synonyms':removed_curated,
    'header_before':header(old_path),'header_after':header(CANDIDATE),
    'predicate_counts':dict(collections.Counter(r['predicate_id'] for r in current)),
    'canonical_source_unchanged':True,
    'scope':'All 41 original native diagnostics resolved mechanically. No new scientific approval: historical WITHHOLD decisions remain; old validation stamps are historical metadata. Candidate is not promoted. Comparison with the old raw candidate is separate from comparison with maintained canonical mapping.'}
for filename,data in [('candidate-comparison.json',summary),('original-41-remediation.json',outcomes),
                      ('previous-candidate-changes.json',previous_comparison['changes']),('old-candidate-changes.json',old_comparison['changes']),('canonical-candidate-changes.json',canonical_comparison['changes']),
                      ('other-field-changes.json',old_comparison['other_changes']),('candidate-native-drift.json',drift),('historical-rule-k-holds.json',held)]:
    (HERE/filename).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
with (HERE/'resolved-label-values.tsv').open('w') as handle:
    w=csv.writer(handle,delimiter='\t');w.writerow(['object_id','object_label','lookup_route'])
    for oid,label in sorted({(r['object_id'],r['object_label']) for r in current}):
        prefix=oid.split(':')[0]
        route='OAK cached CHEBI label' if prefix=='CHEBI' else 'OLS4 label' if prefix in {'FOODON','UBERON','ENVO'} else 'native stored or registry label'
        w.writerow([oid,label,route])
print(json.dumps(summary,indent=2))
