"""OCR engine for PDF text recognition"""

class OCREngine:
    """Main OCR engine class supporting multiple backends"""
    
    def __init__(self, backend='paddle'):
        self.backend = backend
    
    def recognize(self, image):
        """Recognize text from image"""
        # TODO: Implement OCR recognition
        return "OCR text - coming soon"