# IntelliPDF 核心包

__version__ = "0.1.0"
__author__ = "IntelliPDF Team"
__email__ = "503583219@qq.com"

from .core.processor import PDFProcessor
from .core.ocr_engine import OCREngine
from .core.chapter_detector import ChapterDetector
from .core.formatter import MarkdownFormatter
from .utils.helpers import setup_logging, validate_pdf

__all__ = [
    "PDFProcessor",
    "OCREngine", 
    "ChapterDetector",
    "MarkdownFormatter",
    "setup_logging",
    "validate_pdf"
]
