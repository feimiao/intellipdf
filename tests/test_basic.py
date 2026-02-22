"""Basic tests for IntelliPDF"""

def test_import():
    """Test that the package can be imported"""
    try:
        import intellipdf
        assert True
    except ImportError:
        assert False, "Failed to import intellipdf"

def test_version():
    """Test package version"""
    import intellipdf
    assert hasattr(intellipdf, '__version__'), "Package should have __version__ attribute"
    assert intellipdf.__version__ is not None, "Version should not be None"