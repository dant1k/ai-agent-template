def test_python_major_version():
    import sys
    assert sys.version_info.major >= 3
