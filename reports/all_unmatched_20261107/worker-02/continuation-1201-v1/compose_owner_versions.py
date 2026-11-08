"""Conservative isolated three-way composition with explicit rejected-label edits.

This never applies an owner or establishes scientific approval. Both fragments
must start from the same maintained baseline. Conflicts fail for human review.
"""
from copy import deepcopy


def compose(base, previous, revision, path=()):
    if isinstance(base, dict) and isinstance(previous, dict) and isinstance(revision, dict):
        out = {}
        for key in base:
            if key not in previous or key not in revision:
                raise ValueError('Deleted baseline field: ' + '.'.join((*path,key)))
        for key in set(base) | set(previous) | set(revision):
            if key not in base:
                if key in previous and key in revision and previous[key] != revision[key]:
                    raise ValueError('Conflicting new field: ' + '.'.join((*path,key)))
                out[key] = deepcopy(previous[key] if key in previous else revision[key])
            else:
                out[key] = compose(base[key], previous[key], revision[key], (*path,key))
        # Keep source field order for reviewability.
        return {key:out[key] for key in dict.fromkeys([*base,*previous,*revision])}
    if isinstance(base,list) and isinstance(previous,list) and isinstance(revision,list):
        if path == ('synonyms',):
            if previous[:len(base)] != base:
                raise ValueError('Predecessor synonym edits require explicit reconciliation')
            if len(revision) < len(base):
                raise ValueError('Revision deleted baseline synonyms')
            for original, revised in zip(base, revision):
                if original != revised:
                    expect = {**original, 'synonym_type':'REJECTED_LABEL'}
                    if revised != expect:
                        raise ValueError('Only exact baseline synonym reclassification is permitted')
            out = deepcopy(revision[:len(base)])
        else:
            if previous[:len(base)] != base or revision[:len(base)] != base:
                raise ValueError('Non-additive list change: ' + '.'.join(path))
            out = deepcopy(base)
        for item in previous[len(base):] + revision[len(base):]:
            if item not in out:
                out.append(deepcopy(item))
        return out
    if previous == base:
        return deepcopy(revision)
    if revision == base or revision == previous:
        return deepcopy(previous)
    raise ValueError('Conflicting scalar or unsupported edit: ' + '.'.join(path))
