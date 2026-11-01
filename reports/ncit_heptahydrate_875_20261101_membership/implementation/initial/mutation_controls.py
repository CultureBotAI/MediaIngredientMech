"""Fresh-process counterfactuals; never modify production source or artifacts."""
import os

def pytest_collection_modifyitems(items):
    mode = os.environ["MEMBERSHIP_MUTATION"]
    module = next(item.module for item in items if hasattr(item.module, "writer"))
    if mode == "routing":
        from mediaingredientmech.utils.culturemech_occurrences import SOURCE_LABEL_IDENTIFIER_OVERRIDES, _source_label_key
        for label in ("Na2HPO4 x 7 H2O", "Na2HPO4.7H2O", "Na2HPO4•7H2O"):
            SOURCE_LABEL_IDENTIFIER_OVERRIDES.pop(_source_label_key(label), None)
    elif mode == "membership":
        module.writer.repaired_membership = lambda before: before
    elif mode == "reservation":
        module.guarded.recheck_reserved = lambda reservations: None
    else:
        raise ValueError(mode)
