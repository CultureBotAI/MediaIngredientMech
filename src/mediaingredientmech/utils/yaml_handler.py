"""Safe YAML I/O with error handling and backups.

The ``save_yaml`` helper accepts an opt-in ``validate=`` flag that routes
the write through ``write_validated_ingredient`` for closed-schema
validation. Callers that write IngredientRecord / IngredientCollection
YAMLs should pass ``validate=True``; callers that write reports, indexes,
or UMAP outputs should leave it off (default).
"""

import shutil
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: str | Path) -> dict:
    """Load a YAML file safely.

    Args:
        path: Path to YAML file.

    Returns:
        Parsed YAML data as dict.

    Raises:
        FileNotFoundError: If file does not exist.
        yaml.YAMLError: If YAML is malformed.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"YAML file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if data is None:
        return {}
    return data


def save_yaml(
    data: Any,
    path: str | Path,
    *,
    backup: bool = True,
    validate: bool = False,
    target_class: str | None = None,
) -> Path:
    """Save data to a YAML file with optional backup and optional validation.

    Args:
        data: Data to serialize.
        path: Output file path.
        backup: If True and file exists, create timestamped backup.
        validate: When True, route the write through
            ``write_validated_ingredient`` so the data is checked against
            the LinkML schema in closed mode before disk is touched. Use
            for IngredientRecord / IngredientCollection writes. Leave off
            for reports / indexes / non-ingredient YAML.
        target_class: Optional LinkML target class override (e.g.
            ``"IngredientCollection"`` or ``"IngredientRecord"``). Only
            consulted when ``validate=True``; defaults to auto-detect from
            the data shape.

    Returns:
        Path to saved file.

    Raises:
        ValidationFailedError: When ``validate=True`` and the data fails
            closed-schema validation. Disk is not modified.
    """
    path = Path(path)

    if backup and path.exists():
        _create_backup(path)

    if validate:
        # Local import to avoid a circular dependency at module import time.
        from mediaingredientmech.validation.write_validated import (
            write_validated_ingredient,
        )

        write_validated_ingredient(data, path, target_class=target_class)
        return path

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    return path


def _create_backup(path: Path) -> Path:
    """Create a timestamped backup of an existing file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = path.parent / "backups"
    backup_dir.mkdir(exist_ok=True)
    backup_path = backup_dir / f"{path.stem}_{timestamp}{path.suffix}"
    shutil.copy2(path, backup_path)
    return backup_path
