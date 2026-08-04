# 【K0】学生信息查询--AI对话记录

> 本文档记录使用 AI 编程助手完成 K0 作业（编写查询学生信息的 Python 脚本）的对话过程。
> 使用的提示词与作业要求一致：根据 API 规范编写可输入学号和密钥、查询输出学生信息的 Python 脚本。
> API 服务器地址：`https://pysummer.pkuai.cc/api/v1`

---

## 第 1 轮：初始需求与基础脚本

### 用户

请根据 API 规范，写一个 Python 脚本，可以输入学生学号和密钥，查询输出学生信息。

（附加《教学管理服务 API 规范 v1.1》文档，其中关键信息如下：）
- 登录接口：`POST /api/v1/auth/login`，请求体 `{"identifier": "学号", "secret": "密钥"}`，成功返回 `{"access_token": "...", "token_type": "bearer", ...}`
- 查询个人信息：`GET /api/v1/students/me`，需在请求头携带 `Authorization: Bearer <access_token>`
- 返回字段：`student_id`、`name`、`extra`、`created_at`、`updated_at`
- 错误格式：`{"error": {"code": "...", "message": "...", "details": null}}`，登录失败返回 `401 INVALID_CREDENTIALS`

### AI 助手

好的，根据你提供的 API 规范，我来编写一个完整的 Python 脚本，支持输入学号和密钥查询学生信息。脚本仅依赖 `requests` 库，使用前请确保已安装（`pip install requests`）。

核心逻辑分三步：
1. **登录认证**：调用 `POST /auth/login`，传入学号（identifier）和密钥（secret），获取 Bearer Token；
2. **查询信息**：调用 `GET /students/me`，在请求头携带 Token，获取学生个人信息；
3. **格式化输出**：展示学号、姓名、扩展字段（extra）、创建/更新时间。

```python
import requests

BASE_URL = "https://pysummer.pkuai.cc/api/v1"

def main():
    student_id = input("请输入学号: ").strip()
    secret = input("请输入密钥: ").strip()

    # 1. 登录获取 token
    login_resp = requests.post(
        f"{BASE_URL}/auth/login",
        json={"identifier": student_id, "secret": secret},
        timeout=15,
    )
    if login_resp.status_code != 200:
        print(f"登录失败，状态码：{login_resp.status_code}，响应：{login_resp.text}")
        return
    token = login_resp.json()["access_token"]

    # 2. 查询学生个人信息
    info_resp = requests.get(
        f"{BASE_URL}/students/me",
        headers={"Authorization": f"Bearer {token}"},
        timeout=15,
    )
    if info_resp.status_code != 200:
        print(f"查询信息失败，状态码：{info_resp.status_code}，响应：{info_resp.text}")
        return

    student = info_resp.json()

    # 3. 格式化打印学生信息
    print("=" * 50)
    print("【学生个人信息】")
    print("=" * 50)
    print(f"学号(student_id): {student['student_id']}")
    print(f"姓名(name): {student['name']}")
    extra = student.get("extra", {})
    if isinstance(extra, dict) and extra:
        print("扩展信息(extra):")
        for k, v in extra.items():
            print(f"  {k}: {v}")
    else:
        print("扩展信息(extra): 无")
    print(f"创建时间(created_at): {student['created_at']}")
    print(f"更新时间(updated_at): {student['updated_at']}")
    print("=" * 50)

if __name__ == "__main__":
    main()
```

### 用户（运行测试）

使用测试账号 `2600926009` 运行成功，输出如下：

```text
==================================================
【学生个人信息】
==================================================
学号(student_id): 2600926009
姓名(name): 陈斌
扩展信息(extra): 无
创建时间(created_at): 2026-07-19T22:03:03+08:00
更新时间(updated_at): 2026-07-19T22:18:35+08:00
==================================================
```

---

## 第 2 轮：增加 PDF 导出功能

### 用户

作业要求提交 PDF 文件。能否在脚本里增加把查询结果导出为 PDF 文件的功能？注意 PDF 里要能正常显示中文。

### AI 助手

可以，使用 `reportlab` 库生成 PDF。中文显示需要注册中文字体（如 `simhei.ttf`）。请先安装依赖：

```bash
pip install reportlab
```

下面给出导出 PDF 的实现思路和关键代码：

1. 用 `SimpleDocTemplate` 创建 PDF 文档；
2. 用 `ParagraphStyle` 定义标题、正文样式，`fontName='SimHei'` 保证中文显示；
3. 用 `Table` 渲染基本信息表格；
4. 扩展信息用 `json.dumps` 格式化后放入 `<pre>` 段落；
5. 字体注册用 `try/except` 包裹，缺失时回退到默认样式，避免脚本直接崩溃。

关键函数：

```python
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import json

try:
    pdfmetrics.registerFont(TTFont('SimHei', 'simhei.ttf'))
except Exception:
    pass

def save_pdf(info, filename=None):
    if not filename:
        filename = f"学生信息_{info.get('student_id', 'student')}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    # ... 定义 title_style / header_style / normal_style，fontName 优先用 'SimHei'
    # ... 构建 elements: 标题 + 基本信息表格 + 扩展信息段落
    doc.build(elements)
    return filename
```

同时建议增加交互式导出菜单（1=Markdown、2=PDF、3=两者、4=不导出），让用户在交互模式下选择是否导出。

---

## 第 3 轮：完善错误处理与重试机制

### 用户

脚本在网络不稳时容易直接失败，比如偶尔连接超时。能否加入重试和更完善的错误处理？

### AI 助手

可以。建议从以下几个方面加强健壮性：

1. **请求重试**：登录和查询都加 `MAX_RETRIES`（建议 2 次）循环，遇到 `ConnectionError`/`Timeout` 自动重试；
2. **超时控制**：统一 `TIMEOUT=15` 秒；
3. **分类异常捕获**：
   - `401 Unauthorized`：单独处理，提示学号/密钥错误或 Token 过期；
   - `SSLError`：提示证书问题，建议用 `--no-ssl-verify`；
   - `HTTPError`：解析 `error.code` 和 `error.message` 友好输出；
   - `JSONDecodeError`：服务器返回非 JSON 时给出提示，避免崩溃；
4. **使用 Session**：用 `requests.Session()` 复用连接，统一设置 `User-Agent`、`Accept`、`Content-Type` 头部；
5. **输入校验**：`validate_input()` 检查学号、密钥、API 地址非空。

核心重试结构示例：

```python
MAX_RETRIES = 2
TIMEOUT = 15

def api_login(session, base_url, student_id, secret):
    url = f"{base_url}/auth/login"
    payload = {"identifier": student_id.strip(), "secret": secret.strip()}
    for attempt in range(MAX_RETRIES):
        try:
            resp = session.post(url, json=payload, timeout=TIMEOUT)
            if resp.status_code == 401:
                # 解析 error.message 提示学号或密钥错误
                return None
            resp.raise_for_status()
            data = resp.json()
            if "access_token" not in data:
                return None
            return data["access_token"]
        except requests.exceptions.ConnectionError:
            print(f"[失败] 连接服务器失败 (尝试 {attempt + 1}/{MAX_RETRIES})")
        except requests.exceptions.Timeout:
            print(f"[失败] 请求超时 (尝试 {attempt + 1}/{MAX_RETRIES})")
        except requests.exceptions.SSLError:
            print("[失败] SSL 证书验证失败")
            return None
        # ... 其他异常
    print("[失败] 多次尝试后仍无法连接服务器")
    return None
```

查询接口 `GET /students/me` 用同样的重试和异常分类结构，401 时提示 Token 无效或已过期。

---

## 第 4 轮：支持命令行参数

### 用户

除了交互式输入，能否也支持命令行参数传入学号和密钥？这样方便批量测试。

### AI 助手

可以，用 `argparse` 实现。同时支持 `--export-md`、`--export-pdf`、`--export-all` 参数控制导出行为。

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="教学管理服务 - 学生信息查询")
    parser.add_argument("-s", "--student-id", help="学生学号")
    parser.add_argument("-k", "--secret", help="登录密钥")
    parser.add_argument("--export-md", action="store_true", help="导出为 Markdown 文件")
    parser.add_argument("--export-pdf", action="store_true", help="导出为 PDF 文件")
    parser.add_argument("--export-all", action="store_true", help="同时导出 Markdown 和 PDF 文件")
    args = parser.parse_args()

    if args.student_id and args.secret:
        student_id = args.student_id.strip()
        secret = args.secret.strip()
    else:
        # 进入交互模式，提示输入
        student_id = get_input("请输入学号: ")
        secret = get_input("请输入密钥: ")
    # ... 登录、查询、导出
```

运行示例：

```bash
# 命令行模式（直接导出 PDF）
python K0.py -s 2600926009 -k p22GhAlOxg62tDRLphehWN9kIg4AkfOs --export-pdf

# 交互模式
python K0.py
```

`get_input()` 用 `while True` 循环保证非空输入，并捕获 `KeyboardInterrupt`/`EOFError` 优雅退出。

---

## 第 5 轮：补充 Markdown 导出与最终整合

### 用户

把 Markdown 导出也加上，然后把所有功能整合成一个完整的 `K0.py`。

### AI 助手

好的，已整合完成。`generate_markdown()` 生成 Markdown 内容，`save_markdown()` 写文件，`save_pdf()` 生成 PDF，`print_info()` 控制台打印。

最终的 `K0.py` 包含以下模块化函数：

| 函数 | 作用 |
|------|------|
| `create_session(verify_ssl)` | 创建带统一请求头的 Session |
| `validate_input(student_id, secret, base_url)` | 校验输入非空 |
| `api_login(session, base_url, student_id, secret)` | 登录获取 Token（含重试） |
| `get_student_info(session, base_url, token)` | 查询学生信息（含重试） |
| `print_info(info)` | 控制台格式化输出 |
| `generate_markdown(info)` | 生成 Markdown 字符串 |
| `save_markdown(info, filename)` | 保存为 `.md` 文件 |
| `save_pdf(info, filename)` | 保存为 `.pdf` 文件（含中文字体） |
| `get_input(prompt, allow_empty)` | 交互式非空输入 |
| `main()` | 入口，解析参数并串联流程 |

### 用户（最终测试）

用两个账号分别测试，均成功：

| 学号 | 姓名 | 查询结果 | 导出 |
|------|------|----------|------|
| 2600926009 | 陈斌 | 成功 | PDF |
| 2600940418 | 潘静怡 | 成功 | PDF |

完整脚本见同目录 `K0_作业提交/K0.py`。

---

## 对话总结

本次作业通过 5 轮对话完成 `K0.py` 的开发：

1. **第 1 轮**：根据 API 规范生成基础脚本，实现登录 + 查询 + 格式化输出，运行测试成功。
2. **第 2 轮**：增加 `reportlab` PDF 导出功能，处理中文字体注册。
3. **第 3 轮**：完善健壮性——请求重试、分类异常捕获、Session 复用、输入校验。
4. **第 4 轮**：用 `argparse` 支持命令行参数模式，兼容交互模式。
5. **第 5 轮**：补充 Markdown 导出，整合为模块化的完整脚本并完成多账号测试。

最终脚本满足作业要求：可根据 API 规范输入学号和密钥查询学生信息，连接 API 服务器运行成功，并支持将结果导出为 PDF 文件提交。

**使用的依赖库**：`requests`（HTTP 请求）、`reportlab`（PDF 生成）。
**关键 API**：`POST /api/v1/auth/login`（登录获取 Token）、`GET /api/v1/students/me`（查询学生信息）。
