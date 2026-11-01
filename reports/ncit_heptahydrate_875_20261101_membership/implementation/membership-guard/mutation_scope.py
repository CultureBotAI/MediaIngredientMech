"""Disable only the new callback in a fresh counterfactual test process."""
def pytest_collection_modifyitems(items):
    module = next(item.module for item in items if hasattr(item.module, "writer"))
    original = module.guarded.publish
    def without_scope(*args, **kwargs):
        kwargs.pop("validate_scope", None)
        return original(*args, **kwargs)
    module.guarded.publish = without_scope
