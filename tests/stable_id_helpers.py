"""Resolve current corpus owners in scientific regressions after #1265.

Scientific expected mappings remain explicit in each test. This helper changes
only the address used to select their owning record; aliases must be unambiguous.
"""
from functools import lru_cache
from pathlib import Path
import yaml

from mediaingredientmech.stable_ids import build_record_index

ROOT = Path(__file__).resolve().parents[1]


@lru_cache(maxsize=1)
def current_records():
    return {path.relative_to(ROOT).as_posix(): yaml.safe_load(path.read_text())
            for group in ('mapped', 'unmapped')
            for path in (ROOT / 'data/ingredients' / group).glob('*.yaml')}


@lru_cache(maxsize=1)
def current_index():
    return build_record_index(current_records())


def current_subject(legacy: str) -> str:
    return current_record(legacy)['mim_id']


def current_record(subject: str) -> dict:
    return current_records()[current_index().lookup(subject)]


def legacy_registry_slug(subject: str) -> str:
    record = current_record(subject)
    identifier = record['identifier']
    if identifier.startswith(('kgmicrobe.compound:', 'kgmicrobe.ingredient:')):
        return identifier.split(':', 1)[1]
    aliases = [value[4:].lower() for value in record['legacy_identifiers'] if value.startswith('MIM:')]
    assert len(aliases) == 1
    return aliases[0]
