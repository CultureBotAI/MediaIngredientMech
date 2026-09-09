"""
Resolving another Mech checkout from its fleet environment variable.

The fleet addresses sibling repositories through ``<REPO>_ROOT`` variables --
``CULTUREMECH_ROOT``, ``KGMICROBE_ROOT``, ``MEDIAINGREDIENTMECH_ROOT``. The
obvious way to read one is wrong in two ways that both fail quietly:

.. code-block:: python

    Path(os.environ.get("CULTUREMECH_ROOT", REPO_ROOT.parent / "CultureMech"))

``os.environ.get`` falls back only when the variable is **absent**, so an
exported-but-empty value becomes ``Path("")``, which is ``.`` -- every path
built on it then resolves against whatever the working directory happens to
be, and the script reads a file that is not there instead of failing. And a
``~/checkouts/CultureMech`` value becomes a literal directory named ``~``.

An empty value is ordinary: a wrapper that sets the variable from an unset
one, or a CI step whose input was blank. See MediaIngredientMech#580.
"""

from __future__ import annotations

import os
from pathlib import Path


def checkout_root(env_var: str, fallback: Path) -> Path:
    """
    Return the checkout root named by ``env_var``, else ``fallback``.

    A variable that is unset, empty, or whitespace counts as unset. A value
    starting with ``~`` is expanded.

    :param env_var: Fleet environment variable naming the checkout, e.g.
        ``"CULTUREMECH_ROOT"``.
    :param fallback: Path to use when the variable does not name one.
    :return: The resolved checkout root. Existence is not checked -- callers
        report a missing checkout in their own terms.
    """
    value = os.environ.get(env_var)
    if value and value.strip():
        return Path(value.strip()).expanduser()
    return Path(fallback).expanduser()
