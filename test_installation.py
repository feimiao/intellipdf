"""Test IntelliPDF installation"""

import sys
import subprocess

def test_import():
    """Test basic import"""
    try:
        import intellipdf
        print(f"✅ Import successful: intellipdf v{intellipdf.__version__}")
        return True
    except ImportError as e:
        print(f"❌ Import failed: {e}")
        return False

def test_cli():
    """Test CLI availability"""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "intellipdf.cli.main", "info"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ CLI command successful:")
            print(result.stdout)
            return True
        else:
            print(f"❌ CLI command failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ CLI test error: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing IntelliPDF installation...\n")
    
    import_ok = test_import()
    cli_ok = test_cli()
    
    print("\n" + "="*50)
    if import_ok and cli_ok:
        print("✅ All tests passed! IntelliPDF is ready to use.")
        return 0
    else:
        print("❌ Some tests failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())