"""CLI commands for IntelliPDF"""

import click
import os
from pathlib import Path
from intellipdf.core.processor import PDFProcessor

@click.group()
def cli():
    """IntelliPDF - Intelligent PDF Processing Toolkit"""
    pass

@cli.command()
@click.argument('input_file')
@click.option('--output', '-o', help='Output file path')
@click.option('--ocr/--no-ocr', default=True, help='Use OCR for scanned documents')
def convert(input_file: str, output: str, ocr: bool):
    """Convert PDF to Markdown"""
    if not os.path.exists(input_file):
        click.echo(f"Error: File not found - {input_file}", err=True)
        return
    
    if not output:
        output = Path(input_file).with_suffix('.md').name
    
    try:
        with PDFProcessor(input_file, use_ocr=ocr) as processor:
            markdown = processor.to_markdown()
            
            with open(output, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            click.echo(f"✅ Successfully converted to {output}")
            click.echo(f"📄 Output: {os.path.abspath(output)}")
            
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)

@cli.command()
@click.argument('input_file')
@click.option('--output-dir', '-d', help='Output directory for split files')
@click.option('--smart/--no-smart', default=True, help='Use smart chapter detection')
def split(input_file: str, output_dir: str, smart: bool):
    """Split PDF by chapters"""
    if not os.path.exists(input_file):
        click.echo(f"Error: File not found - {input_file}", err=True)
        return
    
    if not output_dir:
        output_dir = Path(input_file).stem + '_split'
    
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        with PDFProcessor(input_file) as processor:
            chapters = processor.split_by_chapters()
            
            for i, chapter in enumerate(chapters, 1):
                chapter_file = os.path.join(output_dir, f"chapter_{i:02d}_{chapter['title'][:50]}.md")
                # 这里可以提取具体章节内容
                content = f"# {chapter['title']}\n\nChapter content will be extracted here."
                
                with open(chapter_file, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                click.echo(f"  📖 Chapter {i}: {chapter['title']} → {chapter_file}")
            
            click.echo(f"\n✅ Successfully split into {len(chapters)} chapters")
            click.echo(f"📁 Output directory: {os.path.abspath(output_dir)}")
            
    except Exception as e:
        click.echo(f"❌ Error: {str(e)}", err=True)

@cli.command()
@click.argument('input_dir')
@click.argument('output_dir')
@click.option('--recursive', '-r', is_flag=True, help='Process subdirectories recursively')
def batch(input_dir: str, output_dir: str, recursive: bool):
    """Batch process PDF files in a directory"""
    if not os.path.exists(input_dir):
        click.echo(f"Error: Directory not found - {input_dir}", err=True)
        return
    
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_files = []
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
        if not recursive:
            break
    
    if not pdf_files:
        click.echo("No PDF files found in the directory.")
        return
    
    click.echo(f"Found {len(pdf_files)} PDF files to process.")
    
    for pdf_file in pdf_files:
        rel_path = os.path.relpath(pdf_file, input_dir)
        output_file = os.path.join(output_dir, Path(rel_path).with_suffix('.md'))
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        try:
            with PDFProcessor(pdf_file) as processor:
                markdown = processor.to_markdown()
                
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(markdown)
                
                click.echo(f"  ✅ {rel_path} → {output_file}")
                
        except Exception as e:
            click.echo(f"  ❌ {rel_path}: {str(e)}", err=True)
    
    click.echo(f"\n✅ Batch processing complete!")
    click.echo(f"📁 Output directory: {os.path.abspath(output_dir)}")

@cli.command()
def info():
    """Show IntelliPDF information"""
    from intellipdf import __version__
    click.echo(f"IntelliPDF v{__version__}")
    click.echo("Intelligent PDF Processing Toolkit")
    click.echo("GitHub: https://github.com/feimiao/intellipdf")
    click.echo("")
    click.echo("Available commands:")
    click.echo("  convert    Convert PDF to Markdown")
    click.echo("  split      Split PDF by chapters")
    click.echo("  batch      Batch process directory")
    click.echo("  info       Show this information")
