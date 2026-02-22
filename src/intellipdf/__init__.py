"""IntelliPDF - Intelligent PDF Processing Toolkit"""

__version__ = "0.1.0"
__author__ = "IntelliPDF Team"
__email__ = "503583219@qq.com"

from intellipdf.core.processor import PDFProcessor
from intellipdf.cli.commands import cli

__all__ = ["PDFProcessor", "cli", "__version__"]