# Selenium 自动化测试项目（基于 Page Object Model）

本项目采用 **Page Object Model (POM)** 设计模式，结合 **Python + Selenium** 构建可维护、可扩展的 Web 自动化测试框架。

---

## 一、项目结构
```
project-root/
	├── config/ # 配置文件（如 URL、浏览器类型、超时等）
	├── data/ # 测试数据（Excel、JSON、YAML 等）
	├── files/ # 通用文件（用于上传/下载等场景）
	├── pictures/ # 截图目录（失败时自动保存）
	├── reports/ # 测试报告输出目录
	└── src/
		├── common/ # 公共工具类（驱动管理、日志、基类等）
		├── pages/ # 页面对象层（POM 核心：每个页面一个类）
		├── business/ # 业务流程层（组合多个页面操作）
		├── test_case/ # 测试用例层（使用 unittest 或 pytest 编写）
		└── test_run/ # 测试执行入口（启动脚本、生成报告）
```


---

## 二、POM 分层说明

| 层级 | 目录 | 作用 |
|------|------|------|
| **配置层** | `config/` | 集中管理环境配置 |
| **数据层** | `data/` | 实现数据与代码分离，支持数据驱动测试 |
| **工具层** | `common/` | 封装 WebDriver 初始化、日志、等待、基类等 |
| **页面层** | `pages/` | ✅ **POM 核心**：每个页面封装为类，包含元素定位和操作方法 |
| **业务层** | `business/` | 封装跨页面的用户行为（如登录 → 购物 → 支付） |
| **测试层** | `test_case/` | 编写具体测试逻辑，调用业务层方法 |
| **执行层** | `test_run/` | 启动测试并生成 HTML/XML 报告 |

---

## 三、POM 模式优势

- **高可维护性**：页面元素变更只需修改对应 Page 类。
- **代码复用**：公共操作封装在 `common/` 和 `business/` 中。
- **清晰分层**：测试逻辑与页面操作解耦，提升可读性。
- **易于协作**：开发可定义页面对象，测试专注验证逻辑。
- **支持扩展**：便于集成 Allure、Jenkins、CI/CD 等工具。

---

## 四、快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2.配置环境

```
编辑 config/config.py 或 config.ini，设置：
浏览器类型（Chrome / Firefox）
基础 URL
隐式等待时间等
```

### 3.编写页面对象

```
# src/pages/login_page.py
from src.common.base_page import BasePage

class LoginPage(BasePage):
    username = ("id", "username")
    password = ("id", "password")
    login_btn = ("xpath", "//button[@type='submit']")

    def login(self, user, pwd):
        self.send_keys(self.username, user)
        self.send_keys(self.password, pwd)
        self.click(self.login_btn)

```

### 4.编写测试用例

```
# src/test_case/test_login.py
import pytest
from src.pages.login_page import LoginPage
from src.common.driver import get_driver

class TestLogin:
    def setup_method(self):
        self.driver = get_driver()
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.open("/login")
        self.login_page.login("admin", "123456")
        assert "Dashboard" in self.driver.title

    def teardown_method(self):
        self.driver.quit()
```

### 5.运行测试

```
# 使用 pytest 运行所有测试并生成 HTML 报告
cd src/test_run
python run_all.py
或直接：
bash
编辑
pytest ../test_case/ --html=../../reports/report.html --self-contained-html
```

### 6.报告示例

测试完成后，报告将生成在 reports/ 目录下，例如：
report.html：可视化测试结果（通过/失败/错误）
失败用例自动截图保存至 pictures/