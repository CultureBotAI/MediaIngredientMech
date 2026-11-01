"""Fresh-process omission of original source/promotion scope callbacks."""
def pytest_collection_modifyitems(items):
    writer = next(item.module.writer for item in items if hasattr(item.module, "writer"))
    original = writer.publish
    def without_scope(*args, **kwargs):
        kwargs.pop("validate_scope", None)
        return original(*args, **kwargs)
    writer.publish = without_scope
