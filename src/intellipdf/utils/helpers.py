"""Helper utilities for IntelliPDF"""

def setup_logging():
    """Setup logging configuration"""
    import logging
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(__name__)

def validate_pdf(filepath):
    """Validate PDF file"""
    import os
    return os.path.exists(filepath) and filepath.lower().endswith('.pdf')