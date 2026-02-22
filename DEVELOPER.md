# SmartPDF Pro 开发环境配置

## Python版本
Python 3.8+

## 环境变量
# OCR语言包路径（如果需要）
export TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata/

## 本地开发
# 安装开发版本
pip install -e .

# 安装所有依赖
pip install -r requirements.txt

# 安装中文语言包（如果需要更好的中文OCR）
sudo apt-get install tesseract-ocr-chi-sim

## 测试
pytest tests/ -v

## 代码检查
black src/
flake8 src/
mypy src/

## 打包发布
python setup.py sdist bdist_wheel

## 运行示例
smartpdf --help
smartpdf convert example.pdf output.md
