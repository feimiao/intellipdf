"""PDF processor core implementation"""

import fitz  # PyMuPDF
import os
from typing import List, Dict, Any, Optional
from .chapter_detector import ChapterDetector
from .ocr_engine import OCREngine
from .formatter import MarkdownFormatter

class PDFProcessor:
    """Main PDF processing class"""
    
    def __init__(self, filepath: str, use_ocr: bool = True):
        """Initialize PDF processor"""
        self.filepath = filepath
        self.use_ocr = use_ocr
        self.doc = None
        self.chapter_detector = ChapterDetector()
        self.ocr_engine = OCREngine() if use_ocr else None
        self.formatter = MarkdownFormatter()
    
    def open(self):
        """Open PDF document"""
        if not os.path.exists(self.filepath):
            raise FileNotFoundError(f"PDF file not found: {self.filepath}")
        self.doc = fitz.open(self.filepath)
        return self
    
    def close(self):
        """Close PDF document"""
        if self.doc:
            self.doc.close()
    
    def extract_text(self, page_range: Optional[tuple] = None) -> str:
        """Extract text from PDF"""
        if not self.doc:
            self.open()
        
        text_parts = []
        start_page, end_page = page_range or (0, len(self.doc) - 1)
        
        for page_num in range(start_page, end_page + 1):
            page = self.doc[page_num]
            text = page.get_text()
            
            # 如果文本太少，尝试OCR
            if self.use_ocr and self.ocr_engine and len(text.strip()) < 100:
                pix = page.get_pixmap()
                # 这里可以添加OCR处理
                pass
            
            text_parts.append(text)
        
        return "\n\n".join(text_parts)
    
    def split_by_chapters(self) -> List[Dict[str, Any]]:
        """Split PDF by detected chapters"""
        text = self.extract_text()
        chapter_boundaries = self.chapter_detector.detect(text)
        
        chapters = []
        for i, boundary in enumerate(chapter_boundaries):
            chapter = {
                "title": boundary["title"],
                "start_page": boundary["start_page"],
                "end_page": boundary["end_page"] if i < len(chapter_boundaries) - 1 else len(self.doc) - 1,
                "content": ""  # 可以进一步提取具体内容
            }
            chapters.append(chapter)
        
        return chapters
    
    def to_markdown(self, include_tables: bool = True, include_formulas: bool = True) -> str:
        """Convert PDF to Markdown format"""
        text = self.extract_text()
        return self.formatter.to_markdown(text, include_tables, include_formulas)
    
    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()