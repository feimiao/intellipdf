from setuptools import setup, find_packages

setup(
    name="intellipdf",
    version="0.1.0",
    author="IntelliPDF Team",
    author_email="503583219@qq.com",
    description="Intelligent PDF Processing Toolkit",
    long_description="See README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/feimiao/intellipdf",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[],  # 完全空依赖，先让构建通过
    extras_require={
        "full": [
            "pymupdf>=1.23.0",
            "pillow>=10.0.0",
            "click>=8.1.0",
            "rich>=13.0.0",
        ],
    },
)