#!/bin/bash
# IntelliPDF GitHub仓库初始化脚本
# 使用方法：确保已登录GitHub CLI，然后运行此脚本

echo "🚀 IntelliPDF GitHub仓库初始化"
echo "================================"

# 检查gh CLI是否安装
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI (gh) 未安装"
    echo "请先安装: https://cli.github.com/"
    exit 1
fi

# 检查登录状态
if ! gh auth status &> /dev/null; then
    echo "🔑 请先登录GitHub:"
    gh auth login
fi

# 创建仓库
echo "📦 创建GitHub仓库: feimiao/intellipdf"
gh repo create feimiao/intellipdf \
    --public \
    --description "IntelliPDF - 智能PDF处理工具箱" \
    --homepage "https://github.com/feimiao/intellipdf" \
    --confirm

if [ $? -ne 0 ]; then
    echo "⚠️  仓库可能已存在或创建失败，继续本地初始化..."
fi

# 初始化本地仓库
echo "🔧 初始化本地Git仓库"
git init
git branch -M main

echo "📄 添加所有文件"
git add .

echo "💾 提交初始版本"
git commit -m "feat: initial commit - IntelliPDF v0.1.0"

# 推送到GitHub
echo "🚀 推送到GitHub"
git remote add origin https://github.com/feimiao/intellipdf.git
git push -u origin main

if [ $? -eq 0 ]; then
    echo "✅ IntelliPDF仓库创建成功！"
    echo ""
    echo "🔗 仓库地址: https://github.com/feimiao/intellipdf"
    echo "🔗 PyPI发布: 运行 ./publish_to_pypi.sh"
    echo "🔗 开启赞助: 访问 https://github.com/sponsors/feimiao"
    echo ""
    echo "📋 下一步行动："
    echo "1. 访问仓库添加README中的badge链接"
    echo "2. 设置GitHub Actions自动化"
    echo "3. 开启GitHub Sponsors功能"
    echo "4. 在技术社区分享项目"
else
    echo "⚠️  推送失败，请手动推送到GitHub"
    echo "手动命令:"
    echo "  git remote add origin https://github.com/feimiao/intellipdf.git"
    echo "  git push -u origin main"
fi

echo ""
echo "🎉 IntelliPDF项目初始化完成！"
