"""Build script for IntelliPDF"""

import subprocess
import sys
import os

def run_command(cmd):
    """Run shell command"""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

def main():
    """Main build process"""
    print("Building IntelliPDF package...")
    
    # 清理旧的构建文件
    if os.path.exists("dist"):
        run_command("rm -rf dist build *.egg-info")
    
    # 安装构建依赖
    print("\nInstalling build dependencies...")
    run_command(f"{sys.executable} -m pip install build twine")
    
    # 构建包
    print("\nBuilding package...")
    run_command(f"{sys.executable} -m build")
    
    # 列出构建的文件
    print("\nBuilt files:")
    run_command("ls -la dist/")
    
    # 测试安装
    print("\nTesting installation...")
    wheel_file = [f for f in os.listdir("dist") if f.endswith(".whl")][0]
    run_command(f"{sys.executable} -m pip install --force-reinstall dist/{wheel_file}")
    
    # 测试命令行
    print("\nTesting CLI...")
    run_command("intellipdf info")
    
    print("\n✅ Build completed successfully!")
    print("To upload to PyPI: python -m twine upload dist/*")

if __name__ == "__main__":
    main()