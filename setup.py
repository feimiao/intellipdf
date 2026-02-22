from setuptools import setup, find_packages
import os

# 读取README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="intellipdf",
    version="0.1.0",
    author="IntelliPDF Team",
    author_email="503583219@qq.com",
    description="智能PDF处理工具箱 - 扫描件识别、章节拆分、格式转换",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/feimiao/intellipdf",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Text Processing",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "intellipdf=intellipdf.cli:main",
        ],
    },
    include_package_data=True,
    keywords="pdf, ocr, markdown, document, conversion, intelligent",
    project_urls={
        "Bug Reports": "https://github.com/feimiao/intellipdf/issues",
        "Funding": "https://github.com/sponsors/feimiao",
        "Source": "https://github.com/feimiao/intellipdf",
        "Documentation": "https://github.com/feimiao/intellipdf#readme",
    },
)