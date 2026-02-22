# PDF处理工具 - 核心代码

import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import re
import os
from typing import List, Dict, Optional
import json

class PDFProcessor:
    """PDF处理核心类"""
    
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.chapters = []
        
    def extract_text(self, page_numbers: Optional[List[int]] = None) -> str:
        """提取PDF文本内容"""
        text_parts = []
        pages = page_numbers if page_numbers else range(len(self.doc))
        
        for page_num in pages:
            page = self.doc[page_num]
            text = page.get_text()
            if text.strip():
                text_parts.append(text)
            else:
                # 扫描件，尝试OCR
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                ocr_text = pytesseract.image_to_string(img, lang="chi_sim+eng")
                text_parts.append(ocr_text)
                
        return "\n\n".join(text_parts)
    
    def detect_chapters(self) -> List[Dict]:
        """检测章节结构"""
        # 章节检测逻辑
        chapter_patterns = [
            r"第[一二三四五六七八九十]+章",
            r"Chapter\s+\d+",
            r"\d+\.\s+[^\n]+",  # 如"1. 引言"
        ]
        
        chapters = []
        current_chapter = {"title": "前言", "start_page": 0, "content": ""}
        
        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            text = page.get_text()
            
            for pattern in chapter_patterns:
                matches = re.findall(pattern, text)
                if matches:
                    # 新章节开始
                    if current_chapter["content"]:
                        chapters.append(current_chapter.copy())
                    
                    current_chapter = {
                        "title": matches[0],
                        "start_page": page_num,
                        "content": text
                    }
                    break
            else:
                # 没有匹配到章节标题，继续当前章节
                if current_chapter["content"]:
                    current_chapter["content"] += "\n\n" + text
                
        # 添加最后一个章节
        if current_chapter["content"]:
            chapters.append(current_chapter)
            
        self.chapters = chapters
        return chapters
    
    def convert_to_markdown(self, use_katex: bool = True) -> str:
        """转换为Markdown格式"""
        md_parts = []
        
        for i, chapter in enumerate(self.chapters):
            # 章节标题
            md_parts.append(f"# {chapter["title"]}\n\n")
            
            # 处理内容
            content = chapter["content"]
            
            # 公式转换（简化版）
            if use_katex:
                # 匹配简单的数学公式
                content = re.sub(r"\$(.*?)\$", r"$$\1$$", content)
                
            # 表格检测（简化版）
            lines = content.split("\n")
            for line in lines:
                if "|" in line and line.count("|") >= 2:
                    # 可能是表格，保持原样
                    md_parts.append(line + "\n")
                else:
                    md_parts.append(line + "\n")
            
            md_parts.append("\n\n")
            
        return "".join(md_parts)
    
    def split_by_chapter(self, output_dir: str) -> List[str]:
        """按章节拆分为多个Markdown文件"""
        os.makedirs(output_dir, exist_ok=True)
        output_files = []
        
        for i, chapter in enumerate(self.chapters):
            # 生成文件名
            safe_title = re.sub(r"[^\w\d-]", "_", chapter["title"])
            filename = f"chapter_{i+1:02d}_{safe_title[:50]}.md"
            filepath = os.path.join(output_dir, filename)
            
            # 写入文件
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"# {chapter["title"]}\n\n")
                f.write(chapter["content"])
                
            output_files.append(filepath)
            
        return output_files
    
    def close(self):
        """关闭PDF文档"""
        if self.doc:
            self.doc.close()

# 命令行接口
def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="PDF处理工具")
    parser.add_argument("input", help="输入PDF文件路径")
    parser.add_argument("--output", "-o", help="输出目录或文件")
    parser.add_argument("--split", action="store_true", help="按章节拆分")
    parser.add_argument("--ocr", action="store_true", help="启用OCR")
    
    args = parser.parse_args()
    
    # 处理PDF
    processor = PDFProcessor(args.input)
    
    try:
        # 检测章节
        chapters = processor.detect_chapters()
        print(f"检测到 {len(chapters)} 个章节")
        
        if args.split:
            # 拆分模式
            output_dir = args.output if args.output else "output_chapters"
            files = processor.split_by_chapter(output_dir)
            print(f"已拆分为 {len(files)} 个文件到目录: {output_dir}")
        else:
            # 单一文件模式
            markdown = processor.convert_to_markdown()
            
            if args.output:
                with open(args.output, "w", encoding="utf-8") as f:
                    f.write(markdown)
                print(f"Markdown文件已保存: {args.output}")
            else:
                print(markdown[:1000])  # 预览前1000字符
                
    finally:
        processor.close()

if __name__ == "__main__":
    main()
