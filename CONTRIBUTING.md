# IntelliPDF 贡献指南

欢迎为 IntelliPDF 做出贡献！本指南将帮助您开始贡献流程。

## 🌟 如何贡献

### 报告 Bug
1. 使用 [Bug 报告模板](.github/ISSUE_TEMPLATE/bug_report.md)
2. 提供详细的重现步骤
3. 包括环境信息（OS、Python版本等）

### 请求功能
1. 使用 [功能请求模板](.github/ISSUE_TEMPLATE/feature_request.md)
2. 清晰描述解决的问题
3. 提供使用场景示例

### 提交代码
1. Fork 仓库
2. 创建功能分支：`git checkout -b feature/AmazingFeature`
3. 提交更改：`git commit -m 'Add some AmazingFeature'`
4. 推送到分支：`git push origin feature/AmazingFeature`
5. 开启 Pull Request

## 🛠️ 开发环境设置

### 克隆仓库
```bash
git clone https://github.com/feimiao/intellipdf.git
cd intellipdf
```

### 安装依赖
```bash
# 安装开发版本
pip install -e .

# 安装开发依赖
pip install -r requirements.txt
pip install pytest black flake8 mypy
```

### 运行测试
```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_processor.py -v
```

## 📝 代码规范

### 代码风格
- 使用 [Black](https://github.com/psf/black) 自动格式化代码
- 行长度限制：88个字符
- 使用类型注解（Type hints）

### 提交信息规范
采用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：
- `feat:` 新功能
- `fix:` 修复bug
- `docs:` 文档更新
- `style:` 代码格式调整
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建过程或辅助工具变动

### 质量检查
```bash
# 代码格式化
black src/

# 代码检查
flake8 src/

# 类型检查
mypy src/
```

## 🔧 项目结构

```
intellipdf/
├── src/intellipdf/          # 核心代码
│   ├── core/               # 核心模块
│   ├── cli/                # 命令行界面
│   └── utils/              # 工具函数
├── tests/                  # 测试文件
├── examples/               # 使用示例
├── docs/                   # 文档
└── .github/               # GitHub配置
```

## 🧪 测试指南

### 测试结构
- 单元测试在 `tests/` 目录
- 测试文件以 `test_` 开头
- 使用 pytest 框架

### 编写测试
```python
def test_pdf_processor():
    processor = PDFProcessor("test.pdf")
    result = processor.extract_text()
    assert result is not None
```

## 📚 文档指南

### 文档类型
1. **API文档** - 代码自动生成
2. **用户指南** - 使用教程
3. **开发文档** - 内部实现说明

### 文档更新
- 修改代码时同步更新相关文档
- 使用清晰的示例代码
- 保持文档与代码一致

## 🚀 发布流程

### 版本管理
采用 [语义化版本](https://semver.org/)：
- `MAJOR` 不兼容的API修改
- `MINOR` 向下兼容的功能新增
- `PATCH` 向下兼容的问题修复

### 发布步骤
1. 更新 `CHANGELOG.md`
2. 更新 `setup.py` 版本号
3. 创建 Git tag：`git tag v1.0.0`
4. 推送到 GitHub：`git push origin v1.0.0`
5. 发布到 PyPI

## 💖 支持贡献者

### 赞助支持
如果您是赞助者，将获得：
- 优先技术支持
- 高级功能提前体验
- 专属感谢名单

### 社区认可
优秀贡献者将：
- 列入项目感谢名单
- 获得贡献者证书
- 优先考虑核心团队邀请

## 📞 联系与支持

- 问题讨论：[GitHub Discussions](https://github.com/feimiao/intellipdf/discussions)
- Bug报告：[GitHub Issues](https://github.com/feimiao/intellipdf/issues)
- 邮件联系：503583219@qq.com

---

感谢您对 IntelliPDF 的贡献！🎉
