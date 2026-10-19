# 电商核心链路接口自动化测试框架

基于 Python 3.11 + pytest + Requests + Allure 搭建的接口自动化框架。

## 技术栈
- Python 3.11+
- pytest / Requests
- GitHub Actions (CI/CD)

## 项目结构
- `config/`: 环境配置
- `api/`: 接口封装层
- `testcases/`: 测试用例层（含三层断言）
- `data/`: YAML 测试数据
- `utils/`: 工具类

## 快速开始
1. 安装依赖：`pip install -r requirements.txt`
2. 执行测试：`pytest`
