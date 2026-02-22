from setuptools import setup, find_packages

# 读取README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="intellipdf",
    version="0.1.0",
    author="IntelliPDF Team",
    author_email="503583219@qq.com",
    description="Intelligent PDF Processing Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feimiao/intellipdf",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: General",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pymupdf>=1.23.0",
        "pillow>=10.0.0",
        "paddleocr>=2.7.0",
        "pytesseract>=0.3.10",
        "opencv-python>=4.8.0",
        "click>=8.1.0",
        "rich>=13.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "intellipdf=intellipdf.cli.main:cli",
        ],
    },
)