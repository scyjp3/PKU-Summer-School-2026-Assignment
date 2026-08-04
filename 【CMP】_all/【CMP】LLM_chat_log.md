# LLM 对话记录 — PKU作业提交通道 网站开发

> 本文档记录了使用 AI（GLM）辅助开发"PKU作业提交通道"哈利波特风格作业提交网站的完整对话过程。开发语言：HTML / CSS / JavaScript，对接教学管理服务 API（`https://pysummer.pkuai.cc/api/v1`）。

---

## 一、需求提出与项目初始化

### 👤 用户
根据【CMP】综合编程作业.py、教学管理服务_API规范_v1.1.md、API服务器.md 和提交要求.md 这四个文档中的内容要求，设计一个可以提交K系列作业的网站。要求是哈利波特风格，通过输入学号和API密钥进入个人主页。

### 🤖 AI
收到需求。我先阅读了四个规范文档，梳理出核心要求：
- **登录方式**：学号（identifier）+ API密钥（secret），调用 `POST /auth/login` 获取 Bearer Token
- **K系列作业提交**：三个字段 `text`（intro.md）、`file`（content.pdf）、`LLM_chat_log`（LLM_chat_log.md）
- **API地址**：`https://pysummer.pkuai.cc/api/v1`

我将创建一个哈利波特风格的纯前端 Web 应用，包含 4 个页面：

```
【CMP】/
├── index.html          # 登录页面（学号+API密钥）
├── dashboard.html      # 个人主页（作业列表、成绩统计）
├── assignment.html     # 作业详情页（含提交历史）
├── submit.html         # 作业提交页（三字段上传）
├── css/style.css       # 哈利波特主题样式
└── js/api.js           # API调用模块（CourseAPI 类）
```

**核心设计**：深紫蓝背景 + 魔法金边框 + 羊皮纸色文字，使用 Cinzel / MedievalSharp 复古字体营造魔法书风格。

以下是 API 模块的核心代码 `js/api.js`：

```javascript
const API_BASE_URL = "https://pysummer.pkuai.cc/api/v1";

class CourseAPI {
    constructor() {
        this.token = localStorage.getItem('access_token');
    }

    async login(identifier, secret) {
        const response = await fetch(`${API_BASE_URL}/auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ identifier, secret })
        });
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.error?.message || '登录失败');
        }
        const data = await response.json();
        this.setToken(data.access_token);
        return data;
    }

    async submitAssignment(assignmentId, text, file, llmChatLog) {
        const formData = new FormData();
        if (text) formData.append('text', text);
        if (file) formData.append('file', file);
        if (llmChatLog) formData.append('LLM_chat_log', llmChatLog);

        const response = await fetch(`${API_BASE_URL}/assignments/${assignmentId}/submissions`, {
            method: 'POST',
            headers: { 'Authorization': `Bearer ${this.token}` },
            body: formData
        });
        // ...错误处理与返回
    }
    // 其余方法：getMe / getStudentInfo / getAssignments / getGrades 等
}
```

项目已创建完成，启动方式：`python -m http.server 8000`，访问 `http://localhost:8000`。

---

## 二、登录页标题与按钮调整

### 👤 用户
登录页面标题改成：大标题"北京大学暑期学校"，小标题"Python语言基础与人工智能应用"；"进入城堡"改成"提交任务"。

### 🤖 AI
已修改 `index.html`：

```html
<header class="header">
    <h1 style="white-space: nowrap;"><i class="fas fa-graduation-cap"></i> 北京大学暑期学校</h1>
    <p class="subtitle" style="white-space: nowrap;">Python语言基础与人工智能应用</p>
</header>
```

按钮文字从"进入城堡"改为"提交任务"：

```html
<button type="submit" class="btn btn-primary" style="width: 100%;">
    <i class="fas fa-sign-in-alt"></i> 提交任务
</button>
```

---

## 三、登录页布局与装饰优化

### 👤 用户
把"北京大学暑期学校"放到一行里；"Python语言基础与人工智能运用"也放到一行里；删除测试账号部分，加上飞翔的扫帚图标；"欢迎来到霍格沃兹管理系统"改成"欢迎来到北大暑校课程作业管理系统"；标题后面背景变成霍格沃兹城堡。

### 🤖 AI
完成 4 项修改：
1. 给 `h1` 和 `subtitle` 添加 `white-space: nowrap` 确保单行显示
2. 删除测试账号提示，替换为 `<i class="fas fa-broom flying-broom">` 扫帚图标
3. 页脚文字改为"欢迎来到北大暑校课程作业管理系统"
4. 新增 `.header-castle` 类，使用魔法风格霍格沃茨城堡图片作为标题背景，叠加半透明渐变层保证文字可读性

扫帚飞翔动画 CSS：

```css
.flying-broom {
    animation: flyAround 8s ease-in-out infinite;
}
@keyframes flyAround {
    0%   { transform: translate(0, 0) rotate(15deg); }
    50%  { transform: translate(40px, -20px) rotate(25deg); }
    100% { transform: translate(0, 0) rotate(15deg); }
}
```

### 👤 用户
把北京大学暑期学校后面的背景删去。

### 🤖 AI
已移除 `index.html` 中的 `header-castle` 类名和 `header-overlay` 遮罩层 div，标题恢复为纯背景样式，保留页面整体星空渐变背景。

---

## 四、个人主页 Logo 与哈利波特装饰

### 👤 用户
进入学生个人主页后左上角的"霍格沃兹"改成"PKU"；主页再多添加一些哈利波特的元素，但不要改变汉字。

### 🤖 AI
1. 导航栏 logo 文字改为 `PKU`
2. 新增覆盖全屏的装饰层 `.hp-decorations`（`pointer-events: none`，不影响交互）：
   - **金色飞贼**：金色小球带扑翼翅膀
   - **猫头鹰信使羽毛**：半透明羽毛波浪轨迹横穿
   - **漂浮蜡烛**：三根带闪烁火焰的蜡烛（模仿霍格沃茨大厅）
   - **魔法闪烁星**：五个金色魔法星旋转闪烁
3. 四个区块标题添加辅助图标（🧙🪄📖🏆），汉字保持不变

### 👤 用户
登录界面的飞天扫帚改成一支悬浮的羽毛笔；主页中刚加的图案不要随着鼠标滑动而动，要在页面上的固定区域悬浮；金色飞贼太丑了，换一种样式。

### 🤖 AI
1. 登录页扫帚图标改为 `fa-feather-pointed`（羽毛笔），动画改为原地倾斜悬浮的 `quillFloat`
2. `.hp-decorations` 从 `position: fixed`（跟随视窗）改为 `position: absolute`（固定在页面位置），所有装饰元素改为固定像素位置
3. 重新设计金色飞贼：用 `radial-gradient` 绘制立体金球（高光+阴影），增加脉冲呼吸光晕层 `snitch-glow`，翅膀改为优雅不对称水滴形

```css
.snitch-body {
    background: radial-gradient(circle at 30% 30%, #fff8dc, #ffd700 40%, #b8860b 80%, #8b6914);
    border-radius: 50%;
    box-shadow: 0 0 20px #ffd700;
}
```

---

## 五、提交按钮猫头鹰与 K系列格式优化

### 👤 用户
在每个"提交作业"的右边都加上一只悬浮的猫头鹰；K系列作业详情内容分行写1、.. 2、.. 3、.. 4、..，使内容看起来更清晰。

### 🤖 AI
1. 新增 `.floating-owl-icon` 样式（`owlBob` 动画），在 dashboard / assignment / submit 三个页面的"提交作业"按钮右侧添加猫头鹰 🦉
2. K系列格式改为编号列表布局，每项有彩色编号前缀 + 左侧彩色边框 + 文件图标 + API字段标签：
   - 1、创建作业文件夹（金色边）
   - 2、intro.md → text（金色边）
   - 3、content.pdf → file（红色边）
   - 4、LLM_chat_log.md → LLM_chat_log（绿色边）

---

## 六、长题目展开折叠功能

### 👤 用户
K3、K4、K5 这种三行以上的长题目的设置展开和折叠功能，使题目可以折叠成三行。

### 🤖 AI
新增展开/折叠功能。由于 `-webkit-line-clamp` 浏览器兼容性差，改用纯 JavaScript 设置高度的方式：

```javascript
function initDescriptionCollapse() {
    const containers = document.querySelectorAll('.description-container');
    containers.forEach(container => {
        const desc = container.querySelector('.description-text');
        const toggle = container.querySelector('.description-toggle');
        const lineHeight = parseFloat(getComputedStyle(desc).lineHeight) || 24;
        const threeLinesHeight = 3 * lineHeight;

        desc.style.maxHeight = threeLinesHeight + 'px';  // 默认折叠3行

        toggle.addEventListener('click', () => {
            const isExpanded = desc.classList.contains('expanded');
            if (isExpanded) {
                desc.style.maxHeight = threeLinesHeight + 'px';  // 收起
                toggle.querySelector('span').textContent = '展开';
            } else {
                desc.style.maxHeight = '2000px';  // 展开
                toggle.querySelector('span').textContent = '收起';
            }
        });
    });
}
```

折叠时底部带渐变遮罩提示有更多内容，只有超过3行的长题目才显示"展开"按钮。

---

## 七、命名统一与猫头鹰删除

### 👤 用户
左上角的霍格沃兹改成PKU，并且将提交作业旁边的猫头鹰全部删去，将网站的名字"霍格沃兹魔法课程"改成"PKU作业提交通道"。

### 🤖 AI
1. 4个页面 `<title>` 全部更新为 `PKU作业提交通道 - xxx`
2. assignment.html / submit.html 的 logo 文字改为 `PKU`（dashboard 此前已是 PKU）
3. 删除三个页面"提交作业"旁的猫头鹰 `<span class="floating-owl-icon">🦉</span>`
4. dashboard 页脚改为"PKU作业提交通道"

---

## 八、拖拽上传功能修复

### 👤 用户
为什么我将我的作业拖拽进对应板块但没有反应，无法上传？

### 🤖 AI
**根本原因**：拖拽上传从未实现——UI 文案写着"点击或拖拽上传"，但代码里只绑定了 `<input type="file">` 的 `change` 事件，且该 input 被 CSS 设为 `display: none` 隐藏，导致点击和拖拽都无反应。

**修复方案**：新增 `setupDropZone()` 通用绑定函数，对三个上传区统一实现：

```javascript
function setupDropZone(zoneId, inputId, handler, acceptExts) {
    const zone = document.getElementById(zoneId);
    const input = document.getElementById(inputId);

    // 点击上传区 → 转发到隐藏的 file input
    zone.addEventListener('click', (e) => {
        if (e.target !== input) input.click();
    });

    // 拖拽视觉反馈
    ['dragenter', 'dragover'].forEach(evt => {
        zone.addEventListener(evt, (e) => {
            e.preventDefault();
            zone.classList.add('drag-over');
        });
    });

    // 放下文件
    zone.addEventListener('drop', (e) => {
        e.preventDefault();
        const file = e.dataTransfer.files[0];
        const ext = file.name.slice(file.name.lastIndexOf('.')).toLowerCase();
        if (acceptExts && !acceptExts.includes(ext)) {
            showError(`不支持的文件格式: ${ext}`);
            return;
        }
        handler(file);
    });
}

setupDropZone('intro-upload', 'intro-file', handleIntroFile, ['.md']);
setupDropZone('content-upload', 'content-file', handleContentFile, ['.pdf', '.txt', '.py', '.ipynb', '.zip']);
setupDropZone('chat-log-upload', 'chat-log-file', handleChatLogFile, ['.md']);
```

同时新增 `.drag-over` 样式：拖拽悬停时金色边框变实线 + 发光，给用户清晰视觉反馈。

---

## 九、文件预览功能修复

### 👤 用户
拖拽进去后为什么变成文本了而不是可以点开的文档？要求将文件上传上去后依然是可以点击打开的md或pdf文档。

### 🤖 AI
**原因**：之前 `intro.md` 上传后会被 `FileReader` 读成纯文本塞进 textarea，`content.pdf` 也只显示一行文字。

**修复**：新增 `renderFileCard()` 函数，上传后渲染可点击打开的文件卡片（文件图标 + 文件名 + 大小 + 打开/移除按钮）。不再把 intro.md 内容塞进 textarea，文件保持为可点击文档。

提交时若 textarea 为空但已上传 intro.md，才用 `readFileAsText()` 读取文件内容作为 API 的 `text` 字段——既保留"可点击文档"展示，又满足 API 提交需要文本的字段要求。

### 👤 用户
为什么我要打开提交的文档时不是直接打开文件，而是弹出一个要求填写文件名的文件夹？

### 🤖 AI
**原因**：浏览器对 `.md` 等文件没有内联渲染器，blob 链接的 MIME 类型为空时会触发 Windows "打开方式"对话框。

**修复**：完全放弃用 `<a href="blob:xxx">` 链接打开文件，改用 JS 直接在新窗口中渲染文件内容：

```javascript
function openFileInNewTab(file) {
    // 关键：在点击事件的同步路径里立即打开空白窗口
    const w = window.open('', '_blank');
    if (!w) { showError('浏览器阻止了新窗口打开'); return; }

    if (isTextFile(file)) {
        // 文本文件：读取内容后填充到已打开的窗口
        readFileAsText(file).then(text => {
            w.document.open();
            w.document.write(`<html><body><pre></pre></body></html>`);
            w.document.querySelector('pre').textContent = text;
            w.document.close();
        });
    } else {
        // PDF：用 iframe 直接嵌入 blob
        const blob = new Blob([file], { type: 'application/pdf' });
        const url = URL.createObjectURL(blob);
        w.document.write(`<iframe src="${url}" style="width:100vw;height:100vh;border:0"></iframe>`);
    }
}
```

### 👤 用户
将md文件打开还是会有弹窗呀。

### 🤖 AI
**根本原因**：`window.open` 被放在异步的 `readFileAsText().then()` 回调里，浏览器把它当作"非用户主动触发的弹窗"，从而走了下载/系统对话框路径。

**修复**：在点击事件的**同步路径**里预先打开空白窗口，异步只填充内容：

```javascript
// ✅ 同步路径立即打开窗口
const w = window.open('', '_blank');

// 异步填充内容到已打开的窗口
readFileAsText(file).then(text => {
    w.document.write(...);  // 操作已存在的窗口，不需要"打开"
});
```

---

## 开发总结

本次开发全程使用 AI 辅助，从需求理解、架构设计到代码实现、Bug 修复共经历 11 个主要迭代阶段。AI 协助完成了：

- **架构设计**：4 页面 + API 模块的纯前端架构
- **主题实现**：哈利波特魔法风格 CSS 主题与动画
- **功能开发**：登录、作业管理、K系列提交、成绩查询、数据统计
- **交互优化**：拖拽上传、长题目折叠、文件在线预览
- **Bug 修复**：拖拽无反应、文件变文本、打开弹窗、异步弹窗拦截等

整个过程体现了人机协作的开发模式：用户提出需求与反馈，AI 负责理解、实现与调试，双方迭代优化直至产品成型。
