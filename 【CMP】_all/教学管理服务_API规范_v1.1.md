[TOC]

# 教学管理服务 API 规范

> 版本：v1.1  
> 状态：课程组讨论稿  
> 本版变更：作业提交新增可选字段 `LLM_chat_log`，用于上传 Markdown 格式的 AI 聊天记录  
> 适用范围：单门、两周制短期课程  
> API 前缀：`/api/v1`  
> 默认时区：`Asia/Shanghai`

---

## 1. 文档目的

本规范定义一套轻量级教学管理服务的 Web API，供课程组开发后端，并供学生使用 Python、JavaScript 或 AI 编程工具开发自己的客户端和前端。

系统仅服务于一次短期课程，核心目标是：

1. 管理学生基本信息；
2. 发布和查询作业；
3. 接收文本、作业文件及 Markdown 格式 AI 聊天记录的作业提交；
4. 录入、发布和查询成绩；
5. 提供适合学生制作图表的个人统计数据；
6. 为管理员提供全班进度查询和成绩导出能力。

本系统是课程教学工具，不按成熟教务产品设计。

---

## 2. 设计原则

- **单课程**：系统只服务当前这一门课程，不设置课程或班级实体。
- **接口优先**：先固定 API 契约，再并行开发后端和示例前端。
- **功能最小化**：不实现注册、找回密码、消息通知、审批、Rubric、OJ、第三方登录等功能。
- **字段最小化**：学生固定字段仅包含学号和姓名，其他信息放入可选扩展字段。
- **学生数据隔离**：学生只能访问自己的资料、提交记录和已发布成绩。
- **管理员集中配置**：学生账户、作业和成绩均由管理员维护。
- **实现轻量**：推荐使用 SQLite 单文件保存结构化数据，本地目录保存上传文件；API 规范不强制具体框架。

---

## 3. 不在本期范围内的功能

以下功能明确不属于本服务：

- 多课程、多学期、多班级管理；
- 学生自助注册；
- 邮件或短信验证；
- 找回密码；
- 复杂用户资料；
- 教师和助教权限细分；
- 自动评测、沙箱执行或 OJ；
- 多维评分量表；
- 通知、公告和站内信；
- 排行榜、隐私策略和复杂统计分析；
- 文件在线预览和 ZIP 解压；
- 成熟产品级审计、审批和工作流。

---

## 4. 角色与权限

系统仅包含两种角色。

### 4.1 学生 `student`

学生可以：

- 登录并获取访问令牌；
- 查询自己的学号、姓名和扩展信息；
- 查询已发布或已关闭的作业；
- 在允许的时间内提交作业；
- 查询自己的所有提交版本；
- 下载自己提交的作业文件和 AI 聊天记录；
- 查询自己已发布的成绩和评语；
- 查询自己的作业完成和成绩统计。

学生不能：

- 查询其他学生的信息、提交或成绩；
- 修改自己的学号、姓名和扩展信息；
- 创建或修改作业；
- 录入或发布成绩。

### 4.2 管理员 `admin`

管理员可以：

- 登录并获取访问令牌；
- 创建、批量创建、修改学生；
- 重置学生密钥；
- 创建、修改和切换作业状态；
- 查看全体学生的提交情况；
- 下载任意学生提交的作业文件和 AI 聊天记录；
- 录入和修改成绩；
- 统一发布某次作业的成绩；
- 查看全班进度；
- 导出 CSV 成绩单。

管理员账户不通过 API 创建，用户名和密钥由服务端配置提供。

---

## 5. 基本约定

### 5.1 协议与数据格式

- 生产环境必须使用 HTTPS。
- 普通请求和响应使用 `application/json; charset=utf-8`。
- 包含作业文件或 `LLM_chat_log` 的提交使用 `multipart/form-data`。
- CSV 导出使用 `text/csv; charset=utf-8`。
- 时间字段使用 ISO 8601，并必须包含时区，例如：

```text
2026-07-20T23:59:59+08:00
```

### 5.2 API 地址

所有接口均位于：

```text
/api/v1
```

示例：

```text
https://course-api.example.com/api/v1/assignments
```

### 5.3 标识符

- `student_id` 必须使用字符串，防止前导零丢失。
- `assignment_id`、`submission_id` 使用正整数。
- API 不要求客户端自行生成整数 ID。

### 5.4 成功响应

成功时直接返回资源对象或资源数组，不额外包裹 `data` 字段。

示例：

```json
{
  "student_id": "20260001",
  "name": "张三",
  "extra": {}
}
```

### 5.5 无响应体操作

成功但无需返回内容的操作使用：

```http
204 No Content
```

### 5.6 认证请求头

除登录接口外，其他受保护接口均使用 Bearer Token：

```http
Authorization: Bearer <access_token>
```

### 5.7 列表接口

本课程人数和作业数量较少，v1 不实现分页。列表接口直接返回完整数组。

---

## 6. 统一错误格式

所有失败响应统一使用以下格式：

```json
{
  "error": {
    "code": "ASSIGNMENT_CLOSED",
    "message": "该作业当前不接受提交",
    "details": null
  }
}
```

字段说明：

| 字段 | 类型 | 说明 |
|---|---|---|
| `error.code` | string | 稳定的机器可读错误码 |
| `error.message` | string | 面向调用者的中文错误说明 |
| `error.details` | object/null | 可选的参数错误详情 |

参数校验错误示例：

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "请求参数不合法",
    "details": {
      "score": "分数必须在 0 到 max_score 之间"
    }
  }
}
```

---

## 7. HTTP 状态码

| 状态码 | 使用场景 |
|---|---|
| `200 OK` | 查询、修改或普通操作成功 |
| `201 Created` | 资源创建成功 |
| `204 No Content` | 操作成功且无需返回响应体 |
| `400 Bad Request` | 请求格式错误或无法解析 |
| `401 Unauthorized` | 未登录、Token 无效或密钥错误 |
| `403 Forbidden` | 已登录但无权访问该资源 |
| `404 Not Found` | 资源不存在 |
| `409 Conflict` | 状态冲突、重复学号、作业不接受提交等 |
| `413 Payload Too Large` | 上传文件超过大小限制 |
| `415 Unsupported Media Type` | 文件类型不允许 |
| `422 Unprocessable Entity` | 字段校验失败 |
| `500 Internal Server Error` | 未预期的服务端错误 |

---

## 8. 数据模型

## 8.1 Student

```json
{
  "student_id": "20260001",
  "name": "张三",
  "extra": {
    "group": "A",
    "github": "zhangsan"
  },
  "created_at": "2026-07-16T10:00:00+08:00",
  "updated_at": "2026-07-16T10:00:00+08:00"
}
```

| 字段 | 类型 | 必需 | 说明 |
|---|---|---:|---|
| `student_id` | string | 是 | 学号，系统内唯一 |
| `name` | string | 是 | 姓名 |
| `extra` | object | 否 | 任意 JSON 扩展字段，默认 `{}` |
| `created_at` | datetime | 响应字段 | 创建时间 |
| `updated_at` | datetime | 响应字段 | 最近修改时间 |

约束：

- `student_id` 长度建议为 1～32 个字符；
- `name` 长度建议为 1～100 个字符；
- `extra` 必须是 JSON 对象，不能是数组或字符串；
- 学生本人不能修改这些字段。

---

## 8.2 Assignment

```json
{
  "id": 1,
  "title": "第一次作业",
  "description": "完成一个调用课程 API 的 Python 程序。",
  "deadline": "2026-07-20T23:59:59+08:00",
  "max_score": 100,
  "allow_late": true,
  "status": "published",
  "created_at": "2026-07-16T10:30:00+08:00",
  "updated_at": "2026-07-16T10:30:00+08:00"
}
```

| 字段 | 类型 | 必需 | 说明 |
|---|---|---:|---|
| `id` | integer | 响应字段 | 作业 ID |
| `title` | string | 是 | 作业标题 |
| `description` | string | 是 | Markdown 或纯文本说明 |
| `deadline` | datetime | 是 | 截止时间 |
| `max_score` | number | 是 | 满分，必须大于 0 |
| `allow_late` | boolean | 是 | 截止后是否允许迟交 |
| `status` | enum | 是 | `draft`、`published` 或 `closed` |
| `created_at` | datetime | 响应字段 | 创建时间 |
| `updated_at` | datetime | 响应字段 | 最近修改时间 |

状态定义：

| 状态 | 学生可见 | 学生可提交 | 说明 |
|---|---:|---:|---|
| `draft` | 否 | 否 | 管理员准备中的作业 |
| `published` | 是 | 按截止时间和 `allow_late` 判断 | 已发布作业 |
| `closed` | 是 | 否 | 已关闭，不再接受提交 |

---

## 8.3 Submission

```json
{
  "id": 15,
  "assignment_id": 1,
  "student_id": "20260001",
  "version": 2,
  "text": "本次作业的说明或代码文本。",
  "file": {
    "original_name": "homework.zip",
    "size": 1048576,
    "content_type": "application/zip",
    "download_url": "/api/v1/submissions/15/file"
  },
  "LLM_chat_log": {
    "original_name": "LLM_chat_log.md",
    "size": 32768,
    "content_type": "text/markdown",
    "download_url": "/api/v1/submissions/15/llm-chat-log"
  },
  "submitted_at": "2026-07-19T20:30:00+08:00",
  "is_late": false
}
```

| 字段 | 类型 | 说明 |
|---|---|---|
| `id` | integer | 提交 ID |
| `assignment_id` | integer | 所属作业 ID |
| `student_id` | string | 提交学生学号 |
| `version` | integer | 该学生在该作业下的提交版本，从 1 开始 |
| `text` | string/null | 文本内容 |
| `file` | object/null | 作业上传文件信息 |
| `LLM_chat_log` | object/null | 可选的 AI 聊天记录文件信息；文件名字段大小写固定 |
| `submitted_at` | datetime | 提交时间，以服务端时间为准 |
| `is_late` | boolean | 是否迟交 |

约束：

- 每次提交至少包含 `text` 或 `file` 之一；仅上传 `LLM_chat_log` 不构成有效作业提交；
- `LLM_chat_log` 为可选字段，用于上传学生与 AI 的聊天记录；
- `LLM_chat_log` 必须是 `.md` 文件，内容采用 Markdown 格式；
- 每次最多上传一个作业文件和一个 `LLM_chat_log` 文件；
- 新提交创建新版本，不覆盖旧版本，聊天记录也随该版本独立保存；
- ZIP 文件仅保存，不在服务器上解压；
- 服务器不得执行学生上传的代码。

---

## 8.4 Grade

```json
{
  "assignment_id": 1,
  "student_id": "20260001",
  "submission_id": 15,
  "score": 92,
  "feedback": "功能完整，异常处理可以改进。",
  "published": true,
  "graded_at": "2026-07-21T12:00:00+08:00",
  "published_at": "2026-07-21T18:00:00+08:00"
}
```

| 字段 | 类型 | 说明 |
|---|---|---|
| `assignment_id` | integer | 作业 ID |
| `student_id` | string | 学号 |
| `submission_id` | integer/null | 本次评分对应的提交版本，可为空 |
| `score` | number | 总分 |
| `feedback` | string | 评语，可为空字符串 |
| `published` | boolean | 是否已向学生发布 |
| `graded_at` | datetime | 最近评分时间 |
| `published_at` | datetime/null | 发布时间 |

约束：

- 每个学生在每个作业下最多有一条当前成绩；
- 重复录入使用覆盖更新语义；
- `score` 必须满足 `0 <= score <= assignment.max_score`；
- 未发布成绩仅管理员可见。

---

## 8.5 StudentSummary

```json
{
  "assignment_count": 5,
  "submitted_count": 4,
  "on_time_count": 3,
  "late_count": 1,
  "unsubmitted_count": 1,
  "graded_count": 3,
  "total_score": 257,
  "total_max_score": 300,
  "average_percentage": 85.67,
  "assignments": [
    {
      "assignment_id": 1,
      "title": "第一次作业",
      "deadline": "2026-07-20T23:59:59+08:00",
      "submitted": true,
      "latest_submission_id": 15,
      "is_late": false,
      "score": 92,
      "max_score": 100,
      "grade_published": true
    }
  ]
}
```

计算规则：

- `assignment_count`：学生可见的作业总数，即 `published` 和 `closed` 状态作业；
- `submitted_count`：至少有一次提交的作业数；
- `on_time_count`：最新提交存在且不是迟交的作业数；
- `late_count`：最新提交存在且为迟交的作业数；
- `unsubmitted_count`：当前没有提交的作业数；
- `graded_count`：已向学生发布成绩的作业数；
- `total_score`：所有已发布成绩之和；
- `total_max_score`：已有已发布成绩的作业满分之和；
- `average_percentage`：`total_score / total_max_score * 100`，无成绩时为 `null`。

---

# 9. 认证接口

## 9.1 登录

```http
POST /api/v1/auth/login
```

权限：公开。

学生和管理员共用该接口。`identifier` 对学生为学号，对管理员为配置中的管理员用户名。

### 请求体

```json
{
  "identifier": "20260001",
  "secret": "初始长密钥"
}
```

| 字段 | 类型 | 必需 | 说明 |
|---|---|---:|---|
| `identifier` | string | 是 | 学号或管理员用户名 |
| `secret` | string | 是 | 密钥 |

### 成功响应

```http
200 OK
```

```json
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 86400,
  "user": {
    "role": "student",
    "identifier": "20260001",
    "name": "张三"
  }
}
```

管理员登录响应示例：

```json
{
  "access_token": "eyJ...",
  "token_type": "bearer",
  "expires_in": 86400,
  "user": {
    "role": "admin",
    "identifier": "admin",
    "name": "管理员"
  }
}
```

### 错误

- `401 INVALID_CREDENTIALS`：用户名、学号或密钥错误。

---

## 9.2 查询当前身份

```http
GET /api/v1/auth/me
```

权限：学生或管理员。

### 学生响应

```json
{
  "role": "student",
  "identifier": "20260001",
  "name": "张三"
}
```

### 管理员响应

```json
{
  "role": "admin",
  "identifier": "admin",
  "name": "管理员"
}
```

---

## 9.3 修改自己的密钥

```http
PUT /api/v1/auth/secret
```

权限：学生或管理员。

### 请求体

```json
{
  "current_secret": "旧密钥",
  "new_secret": "新的长密钥"
}
```

建议要求新密钥至少 16 个字符。

### 成功响应

```http
204 No Content
```

### 错误

- `401 INVALID_CREDENTIALS`：旧密钥错误；
- `422 WEAK_SECRET`：新密钥不符合长度要求。

---

# 10. 学生接口

## 10.1 查询个人信息

```http
GET /api/v1/students/me
```

权限：学生。

### 成功响应

```json
{
  "student_id": "20260001",
  "name": "张三",
  "extra": {
    "group": "A"
  },
  "created_at": "2026-07-16T10:00:00+08:00",
  "updated_at": "2026-07-16T10:00:00+08:00"
}
```

---

## 10.2 查询作业列表

```http
GET /api/v1/assignments
```

权限：学生。

只返回 `published` 和 `closed` 状态的作业，按截止时间升序排列。

### 成功响应

```json
[
  {
    "id": 1,
    "title": "第一次作业",
    "description": "完成一个调用课程 API 的 Python 程序。",
    "deadline": "2026-07-20T23:59:59+08:00",
    "max_score": 100,
    "allow_late": true,
    "status": "published",
    "submission_status": {
      "submitted": true,
      "latest_submission_id": 15,
      "latest_version": 2,
      "submitted_at": "2026-07-19T20:30:00+08:00",
      "is_late": false
    },
    "grade_status": {
      "published": true,
      "score": 92
    }
  }
]
```

说明：

- `submission_status` 为当前学生在该作业下的提交概况；
- 未提交时，`submitted=false`，其他字段为 `null`；
- `grade_status.score` 仅在成绩已发布时返回，否则为 `null`。

---

## 10.3 查询作业详情

```http
GET /api/v1/assignments/{assignment_id}
```

权限：学生。

### 路径参数

| 参数 | 类型 | 说明 |
|---|---|---|
| `assignment_id` | integer | 作业 ID |

### 成功响应

返回单个 Assignment 对象，并包含当前学生的提交和成绩概况：

```json
{
  "id": 1,
  "title": "第一次作业",
  "description": "完成一个调用课程 API 的 Python 程序。",
  "deadline": "2026-07-20T23:59:59+08:00",
  "max_score": 100,
  "allow_late": true,
  "status": "published",
  "submission_status": {
    "submitted": true,
    "latest_submission_id": 15,
    "latest_version": 2,
    "submitted_at": "2026-07-19T20:30:00+08:00",
    "is_late": false
  },
  "grade": {
    "score": 92,
    "feedback": "功能完整，异常处理可以改进。",
    "published": true
  }
}
```

### 错误

- `404 ASSIGNMENT_NOT_FOUND`：作业不存在、仍为草稿，或学生不可见。

---

## 10.4 提交作业

```http
POST /api/v1/assignments/{assignment_id}/submissions
Content-Type: multipart/form-data
```

权限：学生。

### 表单字段

| 字段 | 类型 | 必需 | 说明 |
|---|---|---:|---|
| `text` | string | 条件必需 | 作业文本内容，可为空 |
| `file` | binary | 条件必需 | 单个作业文件，可为空 |
| `LLM_chat_log` | binary | 否 | AI 聊天记录文件，仅接受 Markdown 格式的 `.md` 文件 |

`text` 和 `file` 至少提供一个。`LLM_chat_log` 是可选的补充材料，不能单独作为作业内容提交。字段名大小写敏感，必须写为 `LLM_chat_log`。

### 文件限制

- 每次最多上传一个作业文件和一个 AI 聊天记录文件；
- 每个文件最大 20 MB；
- 作业文件允许扩展名：`.txt`、`.py`、`.ipynb`、`.pdf`、`.zip`；
- `LLM_chat_log` 仅允许 `.md` 扩展名，推荐 MIME 类型为 `text/markdown`；客户端发送 `text/plain` 时服务端也可接受，但仍必须校验 `.md` 扩展名；
- 服务端应为两个文件分别重新生成存储文件名；
- 服务端仅保存文件，不执行、不解压，也不要求解析 Markdown 内容。

### cURL 示例

```bash
curl -X POST \
  'https://course-api.example.com/api/v1/assignments/1/submissions' \
  -H 'Authorization: Bearer <access_token>' \
  -F 'text=这是我的第二版提交' \
  -F 'file=@homework.zip' \
  -F 'LLM_chat_log=@LLM_chat_log.md;type=text/markdown'
```

### 成功响应

```http
201 Created
```

```json
{
  "id": 15,
  "assignment_id": 1,
  "student_id": "20260001",
  "version": 2,
  "text": "这是我的第二版提交",
  "file": {
    "original_name": "homework.zip",
    "size": 1048576,
    "content_type": "application/zip",
    "download_url": "/api/v1/submissions/15/file"
  },
  "LLM_chat_log": {
    "original_name": "LLM_chat_log.md",
    "size": 32768,
    "content_type": "text/markdown",
    "download_url": "/api/v1/submissions/15/llm-chat-log"
  },
  "submitted_at": "2026-07-19T20:30:00+08:00",
  "is_late": false
}
```

### 业务规则

- `draft` 作业不可见，也不可提交；
- `closed` 作业不可提交；
- `published` 且未超过截止时间时可正常提交；
- 超过截止时间后，仅 `allow_late=true` 时可提交；
- 迟交记录的 `is_late=true`；
- 每次成功提交均生成新的 `version`；
- `LLM_chat_log` 与本次提交版本绑定；后续重新提交时，如需保留或更新聊天记录，应再次上传；
- 服务端接收时间是是否迟交的唯一判断依据。

### 错误

- `404 ASSIGNMENT_NOT_FOUND`：作业不存在或学生不可见；
- `409 ASSIGNMENT_CLOSED`：作业已关闭；
- `409 LATE_SUBMISSION_NOT_ALLOWED`：已超过截止时间且不允许迟交；
- `422 EMPTY_SUBMISSION`：未提供 `text` 和 `file`，或仅提供了 `LLM_chat_log`；
- `413 FILE_TOO_LARGE`：任一上传文件超过 20 MB；
- `415 FILE_TYPE_NOT_ALLOWED`：作业文件扩展名不允许；
- `415 LLM_CHAT_LOG_TYPE_NOT_ALLOWED`：`LLM_chat_log` 不是 `.md` 文件。

---

## 10.5 查询自己的提交历史

```http
GET /api/v1/assignments/{assignment_id}/submissions
```

权限：学生。

按 `version` 降序返回当前学生在该作业下的全部提交。

### 成功响应

```json
[
  {
    "id": 15,
    "assignment_id": 1,
    "student_id": "20260001",
    "version": 2,
    "text": "第二版提交",
    "file": {
      "original_name": "homework.zip",
      "size": 1048576,
      "content_type": "application/zip",
      "download_url": "/api/v1/submissions/15/file"
    },
    "LLM_chat_log": {
      "original_name": "LLM_chat_log.md",
      "size": 32768,
      "content_type": "text/markdown",
      "download_url": "/api/v1/submissions/15/llm-chat-log"
    },
    "submitted_at": "2026-07-19T20:30:00+08:00",
    "is_late": false
  },
  {
    "id": 11,
    "assignment_id": 1,
    "student_id": "20260001",
    "version": 1,
    "text": "第一版提交",
    "file": null,
    "LLM_chat_log": null,
    "submitted_at": "2026-07-18T10:00:00+08:00",
    "is_late": false
  }
]
```

---

## 10.6 查询最新提交

```http
GET /api/v1/assignments/{assignment_id}/submissions/latest
```

权限：学生。

### 成功响应

返回最新 Submission 对象。

### 错误

- `404 SUBMISSION_NOT_FOUND`：当前学生尚未提交该作业。

---

## 10.7 下载提交文件

```http
GET /api/v1/submissions/{submission_id}/file
```

权限：提交所属学生或管理员。

### 成功响应

返回作业文件流，并设置：

```http
Content-Disposition: attachment; filename="homework.zip"
```

### 错误

- `403 FORBIDDEN`：学生尝试下载他人的文件；
- `404 SUBMISSION_NOT_FOUND`：提交不存在；
- `404 SUBMISSION_FILE_NOT_FOUND`：该提交没有作业文件或文件已丢失。

---

## 10.8 下载 AI 聊天记录

```http
GET /api/v1/submissions/{submission_id}/llm-chat-log
```

权限：提交所属学生或管理员。

### 成功响应

返回 Markdown 文件流，并设置：

```http
Content-Type: text/markdown; charset=utf-8
Content-Disposition: attachment; filename="LLM_chat_log.md"
```

服务端可使用学生上传时的原始文件名作为下载文件名，但必须进行安全转义。

### 错误

- `403 FORBIDDEN`：学生尝试下载他人的聊天记录；
- `404 SUBMISSION_NOT_FOUND`：提交不存在；
- `404 LLM_CHAT_LOG_NOT_FOUND`：该提交未上传 AI 聊天记录，或文件已丢失。

---

## 10.9 查询自己的已发布成绩

```http
GET /api/v1/grades
```

权限：学生。

只返回已发布成绩，按作业截止时间升序排列。

### 成功响应

```json
[
  {
    "assignment_id": 1,
    "assignment_title": "第一次作业",
    "submission_id": 15,
    "score": 92,
    "max_score": 100,
    "feedback": "功能完整，异常处理可以改进。",
    "published_at": "2026-07-21T18:00:00+08:00"
  }
]
```

---

## 10.10 查询个人统计

```http
GET /api/v1/students/me/summary
```

权限：学生。

用于学生端展示进度卡片、折线图、柱状图和完成率。

### 成功响应

返回 StudentSummary 对象。

---

# 11. 管理员：学生管理接口

## 11.1 查询学生列表

```http
GET /api/v1/admin/students
```

权限：管理员。

按 `student_id` 升序返回全部学生。

### 成功响应

```json
[
  {
    "student_id": "20260001",
    "name": "张三",
    "extra": {},
    "created_at": "2026-07-16T10:00:00+08:00",
    "updated_at": "2026-07-16T10:00:00+08:00"
  }
]
```

---

## 11.2 创建单个学生

```http
POST /api/v1/admin/students
```

权限：管理员。

### 请求体

```json
{
  "student_id": "20260001",
  "name": "张三",
  "extra": {
    "group": "A"
  }
}
```

### 成功响应

```http
201 Created
```

```json
{
  "student": {
    "student_id": "20260001",
    "name": "张三",
    "extra": {
      "group": "A"
    },
    "created_at": "2026-07-16T10:00:00+08:00",
    "updated_at": "2026-07-16T10:00:00+08:00"
  },
  "initial_secret": "4kmJmS8vKz..."
}
```

`initial_secret` 只在创建成功时返回一次。服务端应仅保存密钥哈希。

### 错误

- `409 STUDENT_ALREADY_EXISTS`：学号已存在。

---

## 11.3 批量创建学生

```http
POST /api/v1/admin/students/batch
```

权限：管理员。

### 请求体

```json
{
  "students": [
    {
      "student_id": "20260001",
      "name": "张三",
      "extra": {}
    },
    {
      "student_id": "20260002",
      "name": "李四",
      "extra": {
        "group": "B"
      }
    }
  ]
}
```

### 成功响应

```http
201 Created
```

```json
{
  "created": [
    {
      "student_id": "20260001",
      "name": "张三",
      "initial_secret": "4kmJmS8vKz..."
    },
    {
      "student_id": "20260002",
      "name": "李四",
      "initial_secret": "yU3qP9aX..."
    }
  ],
  "failed": []
}
```

批量接口采用“逐条处理”语义：

- 合法且不重复的学生正常创建；
- 失败项放入 `failed`；
- 不因一条失败而回滚其他成功项。

部分失败示例：

```json
{
  "created": [
    {
      "student_id": "20260002",
      "name": "李四",
      "initial_secret": "yU3qP9aX..."
    }
  ],
  "failed": [
    {
      "student_id": "20260001",
      "code": "STUDENT_ALREADY_EXISTS",
      "message": "学号已存在"
    }
  ]
}
```

若请求体结构本身不合法，整个请求返回 `422`。

---

## 11.4 查询单个学生

```http
GET /api/v1/admin/students/{student_id}
```

权限：管理员。

### 成功响应

返回 Student 对象。

---

## 11.5 修改学生信息

```http
PATCH /api/v1/admin/students/{student_id}
```

权限：管理员。

学号作为主标识，不允许通过本接口修改。

### 请求体

所有字段均可选，但至少提供一个：

```json
{
  "name": "张三丰",
  "extra": {
    "group": "A",
    "note": "课程组临时备注"
  }
}
```

`extra` 使用整体替换语义，不进行深层合并。

### 成功响应

返回更新后的 Student 对象。

---

## 11.6 重置学生密钥

```http
POST /api/v1/admin/students/{student_id}/reset-secret
```

权限：管理员。

### 成功响应

```json
{
  "student_id": "20260001",
  "new_secret": "W8sP2n..."
}
```

新密钥只返回一次。重置后，旧密钥立即失效；已有访问令牌是否立即失效由实现决定，推荐同时失效。

---

# 12. 管理员：作业管理接口

## 12.1 查询全部作业

```http
GET /api/v1/admin/assignments
```

权限：管理员。

返回 `draft`、`published` 和 `closed` 的全部作业，按创建时间升序排列。

### 成功响应

```json
[
  {
    "id": 1,
    "title": "第一次作业",
    "description": "完成一个调用课程 API 的 Python 程序。",
    "deadline": "2026-07-20T23:59:59+08:00",
    "max_score": 100,
    "allow_late": true,
    "status": "published",
    "created_at": "2026-07-16T10:30:00+08:00",
    "updated_at": "2026-07-16T10:30:00+08:00"
  }
]
```

---

## 12.2 创建作业

```http
POST /api/v1/admin/assignments
```

权限：管理员。

### 请求体

```json
{
  "title": "第一次作业",
  "description": "完成一个调用课程 API 的 Python 程序。",
  "deadline": "2026-07-20T23:59:59+08:00",
  "max_score": 100,
  "allow_late": true,
  "status": "draft"
}
```

`status` 可省略，默认值为 `draft`。

### 成功响应

```http
201 Created
```

返回创建后的 Assignment 对象。

---

## 12.3 查询单个作业

```http
GET /api/v1/admin/assignments/{assignment_id}
```

权限：管理员。

返回 Assignment 对象。

---

## 12.4 修改作业

```http
PATCH /api/v1/admin/assignments/{assignment_id}
```

权限：管理员。

### 请求体

所有字段均可选，但至少提供一个：

```json
{
  "title": "第一次作业：API 调用",
  "description": "更新后的说明",
  "deadline": "2026-07-21T23:59:59+08:00",
  "max_score": 100,
  "allow_late": false,
  "status": "published"
}
```

### 状态转换

允许的转换：

```text
draft -> published
published -> draft
published -> closed
closed -> published
```

说明：

- `published -> draft` 仅建议在尚无学生提交时使用；
- 已有提交后仍允许修改标题、说明、截止时间和迟交设置；
- 修改 `max_score` 后，已有成绩必须仍满足新的满分限制，否则返回冲突；
- 成绩统一发布后，作业自动变为 `closed`。

### 错误

- `409 INVALID_ASSIGNMENT_STATE`：状态转换不允许；
- `409 MAX_SCORE_CONFLICT`：新满分低于已有成绩。

---

# 13. 管理员：提交管理接口

## 13.1 查询某次作业的提交

```http
GET /api/v1/admin/assignments/{assignment_id}/submissions
```

权限：管理员。

### 查询参数

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---:|---|
| `student_id` | string | 无 | 仅查看指定学生 |
| `latest_only` | boolean | `true` | 是否只返回每名学生的最新提交 |
| `late` | boolean | 无 | 仅查看迟交或非迟交提交 |

示例：

```text
GET /api/v1/admin/assignments/1/submissions?latest_only=true&late=false
```

### 成功响应

```json
[
  {
    "id": 15,
    "assignment_id": 1,
    "student_id": "20260001",
    "student_name": "张三",
    "version": 2,
    "text": "第二版提交",
    "file": {
      "original_name": "homework.zip",
      "size": 1048576,
      "content_type": "application/zip",
      "download_url": "/api/v1/submissions/15/file"
    },
    "LLM_chat_log": {
      "original_name": "LLM_chat_log.md",
      "size": 32768,
      "content_type": "text/markdown",
      "download_url": "/api/v1/submissions/15/llm-chat-log"
    },
    "submitted_at": "2026-07-19T20:30:00+08:00",
    "is_late": false,
    "grade": {
      "score": 92,
      "published": true
    }
  }
]
```

---

## 13.2 查询单次提交详情

```http
GET /api/v1/admin/submissions/{submission_id}
```

权限：管理员。

### 成功响应

返回 Submission 对象，并额外包含 `student_name` 和当前成绩概况。

---

## 13.3 查询作业提交概况

```http
GET /api/v1/admin/assignments/{assignment_id}/submission-summary
```

权限：管理员。

### 成功响应

```json
{
  "assignment_id": 1,
  "student_count": 30,
  "submitted_count": 26,
  "on_time_count": 24,
  "late_count": 2,
  "unsubmitted_count": 4,
  "graded_count": 20,
  "published_grade_count": 0,
  "students": [
    {
      "student_id": "20260001",
      "name": "张三",
      "submitted": true,
      "latest_submission_id": 15,
      "latest_version": 2,
      "submitted_at": "2026-07-19T20:30:00+08:00",
      "is_late": false,
      "graded": true,
      "score": 92,
      "grade_published": false
    }
  ]
}
```

该接口用于管理员前端显示提交进度表。

---

# 14. 管理员：成绩管理接口

## 14.1 录入或修改单个成绩

```http
PUT /api/v1/admin/assignments/{assignment_id}/grades/{student_id}
```

权限：管理员。

该接口使用“创建或覆盖”语义。

### 请求体

```json
{
  "submission_id": 15,
  "score": 92,
  "feedback": "功能完整，异常处理可以改进。"
}
```

| 字段 | 类型 | 必需 | 说明 |
|---|---|---:|---|
| `submission_id` | integer/null | 否 | 本次评分对应的提交；为空表示不绑定具体版本 |
| `score` | number | 是 | 总分 |
| `feedback` | string | 否 | 评语，默认空字符串 |

### 成功响应

```json
{
  "assignment_id": 1,
  "student_id": "20260001",
  "submission_id": 15,
  "score": 92,
  "feedback": "功能完整，异常处理可以改进。",
  "published": false,
  "graded_at": "2026-07-21T12:00:00+08:00",
  "published_at": null
}
```

### 业务规则

- 录入和修改成绩后，`published` 均保持原值；
- 新建成绩默认 `published=false`；
- `submission_id` 如提供，必须属于该学生和该作业；
- 允许未提交作业直接录入成绩，例如记 0 分。

### 错误

- `404 STUDENT_NOT_FOUND`：学生不存在；
- `404 ASSIGNMENT_NOT_FOUND`：作业不存在；
- `409 SUBMISSION_MISMATCH`：提交不属于指定学生或作业；
- `422 SCORE_OUT_OF_RANGE`：分数超出允许范围。

---

## 14.2 查询某次作业的成绩列表

```http
GET /api/v1/admin/assignments/{assignment_id}/grades
```

权限：管理员。

### 成功响应

```json
[
  {
    "student_id": "20260001",
    "student_name": "张三",
    "submission_id": 15,
    "score": 92,
    "feedback": "功能完整，异常处理可以改进。",
    "published": false,
    "graded_at": "2026-07-21T12:00:00+08:00",
    "published_at": null
  }
]
```

未评分学生不出现在此列表中；如需查看未评分名单，使用提交概况接口。

---

## 14.3 统一发布某次作业的成绩

```http
POST /api/v1/admin/assignments/{assignment_id}/grades/publish
```

权限：管理员。

### 请求体

无。

### 成功响应

```json
{
  "assignment_id": 1,
  "published_count": 26,
  "published_at": "2026-07-21T18:00:00+08:00",
  "assignment_status": "closed"
}
```

### 业务规则

- 发布该作业下所有已经录入的成绩；
- 未录入成绩的学生不生成成绩记录；
- 发布完成后，作业状态自动改为 `closed`；
- 已发布成绩允许管理员继续修改，修改结果对学生立即可见；
- 重复调用为幂等操作，不重复创建成绩。

---

# 15. 管理员：全局统计与导出

## 15.1 查询全班概况

```http
GET /api/v1/admin/summary
```

权限：管理员。

### 成功响应

```json
{
  "student_count": 30,
  "assignment_count": 5,
  "published_assignment_count": 3,
  "closed_assignment_count": 1,
  "total_expected_submissions": 120,
  "submitted_count": 104,
  "on_time_count": 97,
  "late_count": 7,
  "unsubmitted_count": 16,
  "graded_count": 80,
  "published_grade_count": 54,
  "assignments": [
    {
      "assignment_id": 1,
      "title": "第一次作业",
      "status": "closed",
      "student_count": 30,
      "submitted_count": 28,
      "late_count": 2,
      "graded_count": 28,
      "published_grade_count": 28,
      "average_score": 84.6,
      "max_score": 100
    }
  ]
}
```

说明：

- 只统计学生可见的 `published` 和 `closed` 作业；
- `average_score` 仅基于已录入成绩计算，没有成绩时为 `null`；
- 该接口主要供管理员前端制作全班进度卡片和图表。

---

## 15.2 导出成绩单 CSV

```http
GET /api/v1/admin/grades/export.csv
```

权限：管理员。

### 查询参数

| 参数 | 类型 | 默认值 | 说明 |
|---|---|---:|---|
| `published_only` | boolean | `false` | 是否只导出已经发布的成绩 |

### 成功响应

```http
200 OK
Content-Type: text/csv; charset=utf-8
Content-Disposition: attachment; filename="grades.csv"
```

建议 CSV 使用 UTF-8 BOM，以便直接用常见表格软件打开中文。

### 推荐 CSV 结构

```csv
student_id,name,assignment_1_score,assignment_1_max,assignment_2_score,assignment_2_max,total_score,total_max,percentage
20260001,张三,92,100,85,100,177,200,88.50
20260002,李四,80,100,90,100,170,200,85.00
```

规则：

- 每个作业占两列：得分和满分；
- 未评分项留空；
- `total_score` 只汇总已有成绩；
- `total_max` 只汇总已有成绩对应的满分；
- `percentage` 无成绩时留空。

---

# 16. API 清单

## 16.1 认证

| 方法 | 路径 | 权限 | 说明 |
|---|---|---|---|
| POST | `/auth/login` | 公开 | 登录并获取 Token |
| GET | `/auth/me` | 已登录 | 查询当前身份 |
| PUT | `/auth/secret` | 已登录 | 修改自己的密钥 |

## 16.2 学生

| 方法 | 路径 | 权限 | 说明 |
|---|---|---|---|
| GET | `/students/me` | 学生 | 查询个人信息 |
| GET | `/assignments` | 学生 | 查询可见作业 |
| GET | `/assignments/{assignment_id}` | 学生 | 查询作业详情 |
| POST | `/assignments/{assignment_id}/submissions` | 学生 | 提交作业 |
| GET | `/assignments/{assignment_id}/submissions` | 学生 | 查询自己的提交历史 |
| GET | `/assignments/{assignment_id}/submissions/latest` | 学生 | 查询自己的最新提交 |
| GET | `/submissions/{submission_id}/file` | 本人或管理员 | 下载作业文件 |
| GET | `/submissions/{submission_id}/llm-chat-log` | 本人或管理员 | 下载 AI 聊天记录（Markdown） |
| GET | `/grades` | 学生 | 查询自己的已发布成绩 |
| GET | `/students/me/summary` | 学生 | 查询个人统计 |

## 16.3 管理员：学生

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/admin/students` | 查询学生列表 |
| POST | `/admin/students` | 创建单个学生 |
| POST | `/admin/students/batch` | 批量创建学生 |
| GET | `/admin/students/{student_id}` | 查询单个学生 |
| PATCH | `/admin/students/{student_id}` | 修改学生信息 |
| POST | `/admin/students/{student_id}/reset-secret` | 重置学生密钥 |

## 16.4 管理员：作业

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/admin/assignments` | 查询全部作业 |
| POST | `/admin/assignments` | 创建作业 |
| GET | `/admin/assignments/{assignment_id}` | 查询作业详情 |
| PATCH | `/admin/assignments/{assignment_id}` | 修改作业和状态 |

## 16.5 管理员：提交

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/admin/assignments/{assignment_id}/submissions` | 查询作业提交列表 |
| GET | `/admin/submissions/{submission_id}` | 查询提交详情 |
| GET | `/admin/assignments/{assignment_id}/submission-summary` | 查询提交概况 |

## 16.6 管理员：成绩与统计

| 方法 | 路径 | 说明 |
|---|---|---|
| PUT | `/admin/assignments/{assignment_id}/grades/{student_id}` | 录入或修改成绩 |
| GET | `/admin/assignments/{assignment_id}/grades` | 查询作业成绩列表 |
| POST | `/admin/assignments/{assignment_id}/grades/publish` | 统一发布成绩 |
| GET | `/admin/summary` | 查询全班概况 |
| GET | `/admin/grades/export.csv` | 导出成绩单 |

---

# 17. 错误码表

| 错误码 | 推荐 HTTP 状态码 | 说明 |
|---|---:|---|
| `VALIDATION_ERROR` | 422 | 通用字段校验失败 |
| `INVALID_CREDENTIALS` | 401 | 登录凭据或旧密钥错误 |
| `INVALID_TOKEN` | 401 | Token 无效 |
| `TOKEN_EXPIRED` | 401 | Token 已过期 |
| `FORBIDDEN` | 403 | 无权执行操作 |
| `WEAK_SECRET` | 422 | 新密钥过短 |
| `STUDENT_NOT_FOUND` | 404 | 学生不存在 |
| `STUDENT_ALREADY_EXISTS` | 409 | 学号已存在 |
| `ASSIGNMENT_NOT_FOUND` | 404 | 作业不存在或当前用户不可见 |
| `INVALID_ASSIGNMENT_STATE` | 409 | 作业状态转换不允许 |
| `ASSIGNMENT_CLOSED` | 409 | 作业已关闭 |
| `LATE_SUBMISSION_NOT_ALLOWED` | 409 | 截止后不允许迟交 |
| `EMPTY_SUBMISSION` | 422 | `text` 和 `file` 均为空；仅上传聊天记录也视为空提交 |
| `FILE_TOO_LARGE` | 413 | 文件超过大小限制 |
| `FILE_TYPE_NOT_ALLOWED` | 415 | 作业文件类型不允许 |
| `LLM_CHAT_LOG_TYPE_NOT_ALLOWED` | 415 | AI 聊天记录不是 `.md` 文件 |
| `SUBMISSION_NOT_FOUND` | 404 | 提交不存在 |
| `SUBMISSION_FILE_NOT_FOUND` | 404 | 提交没有作业文件或文件丢失 |
| `LLM_CHAT_LOG_NOT_FOUND` | 404 | 提交没有 AI 聊天记录或文件丢失 |
| `SUBMISSION_MISMATCH` | 409 | 提交与学生或作业不匹配 |
| `SCORE_OUT_OF_RANGE` | 422 | 分数超出范围 |
| `MAX_SCORE_CONFLICT` | 409 | 新满分低于已有成绩 |
| `INTERNAL_ERROR` | 500 | 未预期的服务端错误 |

---

# 18. 典型调用流程

## 18.1 学生调用流程

```text
1. POST /auth/login
2. GET  /students/me
3. GET  /assignments
4. GET  /assignments/{id}
5. POST /assignments/{id}/submissions
6. GET  /assignments/{id}/submissions
7. GET  /grades
8. GET  /students/me/summary
```

## 18.2 管理员初始化流程

```text
1. POST  /auth/login
2. POST  /admin/students/batch
3. POST  /admin/assignments
4. PATCH /admin/assignments/{id}  将 status 改为 published
```

## 18.3 管理员评分流程

```text
1. GET  /admin/assignments/{id}/submission-summary
2. GET  /admin/assignments/{id}/submissions
3. PUT  /admin/assignments/{id}/grades/{student_id}
4. POST /admin/assignments/{id}/grades/publish
5. GET  /admin/grades/export.csv
```

---

# 19. Python 学生端最小示例

以下代码仅用于说明接口调用方式，不属于后端实现要求。

```python
from pathlib import Path
import requests

BASE_URL = "https://course-api.example.com/api/v1"
STUDENT_ID = "20260001"
SECRET = "your-secret"

# 1. 登录
login_response = requests.post(
    f"{BASE_URL}/auth/login",
    json={"identifier": STUDENT_ID, "secret": SECRET},
    timeout=15,
)
login_response.raise_for_status()
token = login_response.json()["access_token"]
headers = {"Authorization": f"Bearer {token}"}

# 2. 查询作业
assignments_response = requests.get(
    f"{BASE_URL}/assignments",
    headers=headers,
    timeout=15,
)
assignments_response.raise_for_status()
print(assignments_response.json())

# 3. 提交作业，并附带 Markdown 格式的 AI 聊天记录
file_path = Path("homework.zip")
chat_log_path = Path("LLM_chat_log.md")
with file_path.open("rb") as file_obj, chat_log_path.open("rb") as chat_log_obj:
    submit_response = requests.post(
        f"{BASE_URL}/assignments/1/submissions",
        headers=headers,
        data={"text": "这是我的作业说明"},
        files={
            "file": (file_path.name, file_obj, "application/zip"),
            "LLM_chat_log": (
                chat_log_path.name,
                chat_log_obj,
                "text/markdown",
            ),
        },
        timeout=60,
    )
submit_response.raise_for_status()
print(submit_response.json())

# 4. 查询成绩
grades_response = requests.get(
    f"{BASE_URL}/grades",
    headers=headers,
    timeout=15,
)
grades_response.raise_for_status()
print(grades_response.json())
```

---

# 20. 最低安全和实现要求

本系统不以抵御高强度攻击为目标，但服务可能通过公网隧道访问，因此后端至少应做到：

1. 全部公网请求使用 HTTPS；
2. 学生和管理员密钥只保存哈希，不明文保存；
3. 使用不可预测的长随机初始密钥；
4. 对所有管理员接口执行服务端角色校验；
5. 对学生资源执行所有权校验；
6. 作业文件和 `LLM_chat_log` 均限制为 20 MB，并分别校验允许的扩展名；
7. 存储文件名由服务端生成，禁止直接使用用户文件名拼接路径；
8. 不执行、不导入、不解压学生文件；
9. 参数必须经过类型、长度和范围校验；
10. Token 应有过期时间，建议 24 小时；
11. 记录基本访问和错误日志，但不得在日志中记录密钥或完整 Token；
12. 定期复制数据库文件和上传目录作为备份。

---

# 21. 推荐但不强制的后端实现

为减少开发和部署复杂度，推荐：

- 语言：Python；
- Web 框架：FastAPI；
- 结构化数据：SQLite 单文件；
- 上传文件：本地目录；
- 认证：Bearer 访问令牌；
- API 文档：框架自动生成 Swagger UI；
- 部署：办公室小主机加 Cloudflare Tunnel。

推荐存储目录：

```text
data/
├── course.db
└── uploads/
    └── assignment-{assignment_id}/
        └── {student_id}/
            ├── submission-{submission_id}.{ext}
            └── submission-{submission_id}-LLM-chat-log.md
```

这些属于实现建议，不影响客户端按照本 API 文档开发。

---

# 22. 验收标准

后端达到以下条件即可视为满足本规范：

- 管理员可以批量创建学生并获得初始密钥；
- 学生可以使用学号和密钥登录；
- 管理员可以创建并发布作业；
- 学生只能看到已发布或已关闭的作业；
- 学生可以提交文本、普通文件或 ZIP，并可选附带 Markdown 格式的 `LLM_chat_log`；
- 系统能够保留多次提交版本并正确标记迟交；
- 学生不能查看其他学生的提交和成绩；
- 管理员可以查看全班提交情况，并下载学生提交的 AI 聊天记录；
- 管理员可以录入总分和评语；
- 成绩发布前学生不可见，统一发布后可见；
- 学生可以获取适合图表展示的个人统计；
- 管理员可以导出 CSV 成绩单；
- 所有失败响应符合统一错误格式；
- 所有需要认证的接口均校验 Bearer Token 和角色。

---

# 23. 结论

本规范以单门短期课程的实际教学需求为边界，保留学生、作业、提交和成绩四个核心概念。接口数量和业务规则均控制在较小范围内，同时覆盖学生开发前端所需的认证、作业文件与 AI 聊天记录上传、数据查询、统计和图表展示场景。

后端实现方应优先保证接口行为与本规范一致，不应在首期自行扩展复杂的课程、班级、审批、消息或自动评测功能。
