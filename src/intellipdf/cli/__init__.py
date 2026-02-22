# IntelliPDF 命令行接口

import click
from rich.console import Console
from rich.progress import Progress
import os
from pathlib import Path

console = Console()

@click.group()
@click.version_option(version="0.1.0")
def main():
    """IntelliPDF - 智能PDF处理工具箱"""
    pass

@main.command()
@click.argument("input", type=click.Path(exists=True))
@click.argument("output", type=click.Path())
@click.option("--ocr", is_flag=True, help="启用OCR识别扫描件")
@click.option("--lang", default="zh+en", help="OCR语言设置")
@click.option("--format", default="markdown", type=click.Choice(["markdown", "html", "text"]), help="输出格式")
def convert(input, output, ocr, lang, format):
    """转换PDF文件为其他格式"""
    from ..core.processor import PDFProcessor
    
    with Progress() as progress:
        task = progress.add_task("[green]处理PDF...", total=100)
        
        try:
            processor = PDFProcessor(input)
            progress.update(task, advance=30)
            
            if format == "markdown":
                result = processor.convert_to_markdown(use_ocr=ocr, lang=lang)
            elif format == "html":
                result = processor.convert_to_html(use_ocr=ocr, lang=lang)
            else:
                result = processor.extract_text(use_ocr=ocr, lang=lang)
                
            progress.update(task, advance=50)
            
            with open(output, "w", encoding="utf-8") as f:
                f.write(result)
                
            progress.update(task, advance=20)
            console.print(f"✅ 转换完成: {output}", style="bold green")
            
        except Exception as e:
            console.print(f"❌ 转换失败: {e}", style="bold red")

@main.command()
@click.argument("input", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
@click.option("--smart", is_flag=True, help="智能章节检测")
@click.option("--pattern", help="自定义章节模式")
def split(input, output_dir, smart, pattern):
    """按章节拆分PDF文件"""
    from ..core.processor import PDFProcessor
    
    console.print("[blue]开始章节拆分...")
    
    try:
        processor = PDFProcessor(input)
        
        if pattern:
            chapters = processor.detect_chapters_with_pattern(pattern)
        elif smart:
            chapters = processor.detect_chapters_smart()
        else:
            chapters = processor.detect_chapters_basic()
            
        console.print(f"📖 检测到 {len(chapters)} 个章节")
        
        os.makedirs(output_dir, exist_ok=True)
        files = processor.split_by_chapter(output_dir, chapters)
        
        for file in files:
            console.print(f"  📄 {Path(file).name}")
            
        console.print(f"✅ 拆分完成，文件保存在: {output_dir}", style="bold green")
        
    except Exception as e:
        console.print(f"❌ 拆分失败: {e}", style="bold red")

@main.command()
@click.argument("input_dir", type=click.Path(exists=True))
@click.argument("output_dir", type=click.Path())
@click.option("--workers", default=4, help="并行处理数量")
def batch(input_dir, output_dir, workers):
    """批量处理文件夹中的PDF文件"""
    console.print(f"[blue]批量处理: {input_dir} → {output_dir}")
    
    # 实现批量处理逻辑
    console.print("批量处理功能开发中...", style="yellow")

@main.command()
def web():
    """启动Web界面"""
    console.print("启动Web界面: http://localhost:8000", style="blue")
    
    # 实现Web界面启动逻辑
    console.print("Web界面开发中...", style="yellow")

if __name__ == "__main__":
    main()
