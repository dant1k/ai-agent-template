def test_import():
    import importlib
    mod = importlib.import_module("agent")
    assert hasattr(mod, "__file__")

def test_version():
    import sys
    assert sys.version_info.major >= 3
