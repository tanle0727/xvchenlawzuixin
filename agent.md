# 律师介绍系统 — Agent 项目指南

## ⚡ 新会话快速启动指令

> **每次新开对话时，将以下内容作为第一条消息发送给 AI：**

```
请先依次完成以下操作：
1. 阅读当前目录下的 agent.md，了解项目全貌、技术栈和开发规范
2. 阅读当前目录下的 progress.md，了解项目进度和待办事项
3. 执行 git log --oneline -10 确认最新提交记录
4. 用 nohup 方式启动 Django 后端服务（source .venv/bin/activate && nohup python manage.py runserver > /tmp/django_server.log 2>&1 &）
5. 启动 Vue 前端开发服务器（cd frontend && eval "$(fnm env)" && npm run dev &）
6. 完成后汇报当前项目状态，然后等我指令

注意：
- 每次完成一个功能后，必须更新 progress.md 中的进度表
- 每次完成一个功能后，必须 git commit 存档
- 回复末尾必须附上所有相关服务的访问链接
- 禁止自行做超出我指令范围的开发工作
```

---

## 项目概述

这是一个**前后端分离**的律师介绍网站项目，用于展示律师信息、专业领域、案例等内容。

- **后端**：Django 6.1.1（Python 3.13），提供 REST API 和 SimpleUI 管理后台
- **前端**：Vue 3 + Vite + TypeScript + Element Plus，独立运行的 SPA 应用
- **数据库**：SQLite3（开发环境）
- **语言/时区**：简体中文 / Asia/Shanghai

## 目录结构

```
律师介绍/
├── agent.md                   # 本文件 — 项目指南（AI 必读）
├── progress.md                # 进度跟踪表（AI 必读 + 每次更新）
├── manage.py                  # Django 管理入口
├── db.sqlite3                 # SQLite 数据库
├── mysite/                    # Django 项目配置
│   ├── settings.py            # 全局配置（INSTALLED_APPS、数据库、国际化等）
│   ├── urls.py                # 根路由
│   ├── wsgi.py / asgi.py      # 部署入口
├── lawyer_app/                # Django 业务应用
│   ├── models.py              # 数据模型
│   ├── views.py               # 视图/API
│   ├── admin.py               # 后台管理注册
│   └── migrations/            # 数据库迁移
├── frontend/                  # Vue 前端项目
│   ├── src/
│   │   ├── main.ts            # 入口（已集成 Element Plus + 中文语言包）
│   │   ├── App.vue            # 根组件
│   │   ├── router/index.ts    # 路由配置
│   │   ├── stores/            # Pinia 状态管理
│   │   ├── views/             # 页面视图
│   │   └── components/        # 公共组件
│   ├── package.json           # 前端依赖
│   └── vite.config.ts         # Vite 构建配置
└── .gitignore                 # Git 排除规则
```

## 技术栈详情

### 后端
| 技术 | 版本 | 说明 |
|------|------|------|
| Python | 3.13 | 运行环境 |
| Django | 6.1.1 | Web 框架 |
| django-simpleui | 2026.1.13 | 管理后台 UI 主题 |
| SQLite3 | — | 开发数据库 |

### 前端
| 技术 | 版本 | 说明 |
|------|------|------|
| Vue | 3.5.x | 前端框架（Composition API + `<script setup>`） |
| Vite | 8.x | 构建工具 |
| TypeScript | 6.x | 开发语言 |
| Element Plus | 2.14.x | UI 组件库（已配置中文语言包） |
| @element-plus/icons-vue | 2.3.x | 图标库（已全局注册） |
| Vue Router | 5.x | 路由管理 |
| Pinia | 4.x | 状态管理 |

## 开发命令

### 后端（需先激活虚拟环境）
```bash
source .venv/bin/activate

# 启动 Django 服务（端口 8000）
python manage.py runserver

# 数据库迁移
python manage.py makemigrations
python manage.py migrate

# 创建管理员账户
python manage.py createsuperuser
```

### 前端（需 Node.js ≥ 22，通过 fnm 管理）
```bash
cd frontend
eval "$(fnm env)"

# 安装依赖
npm install

# 启动开发服务器（端口 5173）
npm run dev

# 类型检查
npm run type-check

# 生产构建
npm run build
```

### 持久化启动 Django（推荐，避免会话中断导致服务停止）
```bash
source .venv/bin/activate
nohup python manage.py runserver > /tmp/django_server.log 2>&1 &
```

## 访问地址

| 服务 | 地址 |
|------|------|
| Django 管理后台 | http://127.0.0.1:8000/admin/ |
| Vue 前端 | http://localhost:5173/ |

## 开发规范

### 通用
- 代码注释和界面文案使用**中文**
- Git 提交信息使用**中文**
- `.gitignore` 已排除 `.venv/`、`node_modules/`、`db.sqlite3`、`frontend/dist/` 等
- **每次完成功能后必须更新 `progress.md` 并提交 Git**
- **每次回复末尾必须附上所有相关服务的访问链接**
- **禁止自行做超出用户指令范围的开发工作**

### 后端
- 业务代码统一放在 `lawyer_app/` 中
- 新增模型后需执行 `makemigrations` + `migrate`
- 管理后台使用 SimpleUI，新模型需在 `admin.py` 中注册
- API 开发需安装 `djangorestframework` 和 `django-cors-headers`（尚未安装）

### 前端
- 使用 `<script setup lang="ts">` 语法编写组件
- UI 组件优先使用 Element Plus，避免重复造轮子
- 路由配置在 `src/router/index.ts`
- 全局状态使用 Pinia，store 文件放在 `src/stores/`
- API 请求建议使用 axios（需额外安装），基础 URL 指向 `http://127.0.0.1:8000`

### 前后端联调
- 当前为前后端分离架构，前端运行在 5173 端口，后端运行在 8000 端口
- 跨域问题需在后端安装并配置 `django-cors-headers`
- 生产部署时可将 Vue 构建产物放入 Django 的 static/templates 目录统一服务
