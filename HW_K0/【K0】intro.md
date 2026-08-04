# K0 作业说明 —— 配置编程环境与学生信息查询

## 一、作业概述

本作业为北大暑校 K0 实验，主要目标是完成 Python 与 AI 编程环境的安装配置，并通过 AI 编程助手根据教学管理服务 API 规范，生成一个可查询学生信息的 Python 脚本，连接 API 服务器运行成功后提交。

## 二、作业要求

1. 根据助教录制教学视频（https://b23.tv/iIDbHB8）安装并配置好 Python 与 AI 编程环境。
2. 从教学网（https://course.pku.edu.cn/）下载课程资料“教学管理服务 API”文档。
3. 使用 AI 编程环境生成获取学生信息的 Python 脚本，连接到 API 服务器运行成功，使用的提示词为：
   > 请根据 API 规范，写一个 Python 脚本，可以输入学生学号和密钥，查询输出学生信息。
4. 提交内容为 Python 脚本与运行结果截图，最终提交 PDF 文件。

## 三、实验环境

- 编程语言：Python 3.x
- 主要依赖库：`requests`（HTTP 请求）、`reportlab`（PDF 导出）
- API 服务器地址：https://pysummer.pkuai.cc
- API 完整路径前缀：https://pysummer.pkuai.cc/api/v1
- API 接口文档：https://pysummer.pkuai.cc/docs

## 四、实现过程

1. **环境配置**：完成 Python 解释器安装与 AI 编程环境配置，安装 `requests`、`reportlab` 等依赖库。
2. **脚本编写**：在 AI 编程助手的辅助下，根据 API 规范完成 `K0.py` 脚本，核心流程如下：
   - 调用 `POST /auth/login`，传入学号（identifier）与密钥（secret），获取 Bearer Token；
   - 调用 `GET /students/me`，在请求头中携带 Token，获取学生个人信息；
   - 格式化输出学号、姓名、扩展字段（extra）、创建/更新时间；
   - 支持将结果导出为 Markdown 或 PDF 文件。
3. **健壮性设计**：脚本内置输入校验、请求重试（MAX_RETRIES=2）、超时控制（TIMEOUT=15s），并对连接错误、超时、SSL 错误、HTTP 错误、非 JSON 响应等异常进行捕获与友好提示。
4. **运行验证**：使用测试账号登录 API 服务器，成功获取学生信息并完成 PDF 导出。

## 五、文件说明

- `K0_作业提交/K0.py`：作业提交的 Python 主程序（核心代码）。
- `K0_作业提交/学生信息查询报告_new.pdf`：作业提交的 PDF 报告（含代码与运行结果）。
- `学生信息查询报告.md`：实验报告源文件（含实验目的、环境、代码与结果）。
- `【K0】配置编程环境.md`：作业任务要求说明。
- `API服务器.md`：API 服务器地址、路径前缀与测试账号信息。
- `LLM_chat_log_模板.md`：AI 对话记录样例与脚本生成过程。

## 六、运行方式

安装依赖：

```bash
pip install requests reportlab
```

交互模式运行（按提示输入学号与密钥）：

```bash
python K0.py
```

命令行参数模式运行：

```bash
python K0.py -s 学号 -k 密钥 --export-pdf
```

支持的参数：
- `-s / --student-id`：学生学号
- `-k / --secret`：登录密钥
- `--export-md`：导出为 Markdown 文件
- `--export-pdf`：导出为 PDF 文件
- `--export-all`：同时导出 Markdown 和 PDF 文件

## 七、实验结果

使用两个账号分别测试，均查询成功：

| 学号 | 姓名 | 查询结果 |
|------|------|----------|
| 2600926*** | 陈* | 成功 |
| 2600940*** | 潘* | 成功 |

成功获取的字段包括：`student_id`、`name`、`extra`（扩展信息）、`created_at`、`updated_at`，并成功导出 PDF 文件。

## 八、备注

- 测试账号来自 `API服务器.md` 提供的公开测试用户信息。
- PDF 导出使用 `reportlab` 库，并尝试注册 `simhei.ttf` 字体以支持中文显示；若字体文件缺失则自动回退为默认样式，不影响导出功能。
- 脚本对网络异常与认证失败做了较为完善的错误处理与重试机制，提升了运行稳定性。
