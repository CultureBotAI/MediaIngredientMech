"""Focused tests for the one-shot lipoic stereochemistry migration (#454)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def _load():
    spec = importlib.util.spec_from_file_location(
        "fix_lipoic_stereochemistry", ROOT / "scripts" / "fix_lipoic_stereochemistry.py"
    )
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_merge_roles_deduplicates_by_role_name_within_a_facet():
    mod = _load()
    survivor = {
        "nutritional_roles": [
            {
                "role": "VITAMIN_SOURCE",
                "confidence": 1.0,
                "evidence": [{"reference_type": "DATABASE_ENTRY"}],
            }
        ]
    }
    duplicates = [
        {
            "nutritional_roles": [
                {
                    "role": "VITAMIN_SOURCE",
                    "confidence": 0.8,
                    "evidence": [{"reference_type": "COMPUTATIONAL_PREDICTION"}],
                }
            ],
            "physicochemical_roles": [
                {
                    "role": "BUFFERING_AGENT",
                    "confidence": 0.8,
                    "evidence": [{"reference_type": "COMPUTATIONAL_PREDICTION"}],
                }
            ],
        }
    ]

    assert mod._merge_roles(survivor, duplicates) == 1
    assert survivor["nutritional_roles"] == [
        {
            "role": "VITAMIN_SOURCE",
            "confidence": 1.0,
            "evidence": [{"reference_type": "DATABASE_ENTRY"}],
        }
    ]
    assert survivor["physicochemical_roles"] == [
        {
            "role": "BUFFERING_AGENT",
            "confidence": 0.8,
            "evidence": [{"reference_type": "COMPUTATIONAL_PREDICTION"}],
        }
    ]
