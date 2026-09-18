# 许宸律师个人名片网站

北京恒都律师事务所资深律师 **许宸（Jenny Xu）** 的专属 B/C 端商业名片网页。展示律师履历、业务领域、代表案例、服务客户，并提供在线预约咨询功能。

> 所有个人履历、业务领域、案例数据 100% 使用真实物料，零编造。

## 🖥️ 技术栈

| 层级 | 技术 | 版本 | 说明 |
|------|------|------|------|
| **前端框架** | Vue 3 | 3.5.x | Composition API + `<script setup>` |
| **构建工具** | Vite | 8.x | 极速 HMR 开发体验 |
| **类型系统** | TypeScript | 6.x | 全量类型覆盖 |
| **CSS 方案** | Tailwind CSS | 4.x | 自定义四色设计令牌体系 |
| **状态管理** | Pinia | 4.x | 轻量级状态管理 |
| **路由** | Vue Router | 5.x | SPA 路由 + 懒加载 |
| **HTTP 客户端** | Axios | 1.x | 请求拦截 + 统一错误处理 |
| **后端框架** | Django | 6.1 | Python Web 框架 |
| **REST API** | Django REST Framework | 3.18 | 序列化 + 限流 + 校验 |
| **管理后台** | django-simpleui | 2026.1 | 中文友好的 Admin UI |
| **跨域** | django-cors-headers | 4.9 | 前后端分离跨域支持 |
| **配置管理** | python-decouple | 3.8 | 环境变量外部化 |
| **图像处理** | Pillow | 12.x | Logo 图片处理 |
| **数据库** | SQLite3 | — | 开发环境（生产可替换 PostgreSQL） |
| **运行时** | Python 3.13 / Node.js ≥ 22 | — | — |

## ✨ 功能特性

### 前端页面

- **Hero 首屏**：律师形象照 + 核心数据（从业年限、服务客户数、主办项目数）+ 教育/职业背景
- **业务领域**：双轨卡片布局，非诉业务 6 项 + 诉讼业务 8 项，从 API 动态加载
- **代表案例**：网格卡片展示，含金额标签、律师角色、案例描述
- **服务客户**：Logo 墙，支持灰度→彩色 hover 效果，无 Logo 时文字降级
- **预约咨询表单**：
  - 双栏布局（表单 + 联系方式/微信二维码）
  - 前后端双重校验（姓名≤15字、手机号格式、公司≤30字、案情≤500字）
  - 业务类型下拉分两组（非诉/诉讼），共 15 项
  - 期望预约日期选择器（禁止选择过去日期）
  - Honeypot 防机器人隐藏字段
  - 提交成功/失败状态反馈
- **隐私保护政策**：独立页面，8 章节完整内容，符合《个人信息保护法》
- **页面路由过渡动画**：淡入淡出切换效果
- **加载骨架屏**：API 请求期间 animate-pulse 占位

### 后端 API

| 方法 | 路径 | 用途 | 安全措施 |
|------|------|------|----------|
| `POST` | `/api/consultation/` | 提交预约咨询 | 限流 5次/分钟 + Honeypot + 字段校验 + 日期校验 |
| `GET` | `/api/cases/` | 获取代表案例列表 | 仅返回 is_active=True |
| `GET` | `/api/clients/` | 获取服务客户列表 | Logo 返回完整 URL |
| `GET` | `/api/practice-areas/` | 获取业务领域列表 | 按非诉/诉讼分组返回 |

### 管理后台（SimpleUI）

- **客户预约管理**：手机号脱敏显示（138\*\*\*\*8000）、fieldsets 分组编辑、时间导航、批量标记完成/已确认
- **代表案例管理**：列表可直接编辑排序号和上下架
- **服务客户管理**：Logo 缩略图预览、可直接编辑排序和上下架
- **业务领域管理**：按分类筛选、可直接编辑排序和上下架

### 安全特性

- 🔒 SECRET_KEY 外部化（python-decouple + .env，不入库）
- 🔒 DEBUG / ALLOWED_HOSTS 从环境变量读取
- 🔒 预约接口限流（同 IP 每分钟 5 次）
- 🔒 Honeypot 防机器人（website_url 隐藏字段）
- 🔒 Serializer 字段长度校验 + 手机号正则校验 + 预约日期校验
- 🔒 安全响应头（XSS_FILTER / NOSNIFF / X_FRAME_OPTIONS=DENY / HTTPONLY Cookie）
- 🔒 SSL 配置（HSTS / SSL_REDIRECT / COOKIE_SECURE，仅生产环境启用）
- 🔒 Admin 后台手机号脱敏显示
- 🔒 API 无 PII 泄露（仅 POST 写入，无 GET 查询预约数据）
- 🔒 CSRF 防护配置
- 🔒 axios 响应拦截器统一错误提示（429/403/5xx/网络错误）
- 🔒 日志系统（业务日志 / 安全日志 / 错误日志，RotatingFileHandler）
- 🔒 数据库自动备份脚本（backup.sh，保留 30 天）
- 🔒 Python 依赖 0 漏洞（pip-audit）
- 🔒 npm 依赖 0 漏洞（npm audit）

## 📁 项目结构

```
xvchenlawzuixin/
├── manage.py                          # Django 管理入口
├── requirements.txt                   # Python 依赖清单
├── backup.sh                          # SQLite 数据库自动备份脚本
├── mysite/                            # Django 项目配置
│   ├── settings.py                    # 全局配置（安全头、CORS、日志等）
│   ├── urls.py                        # 根路由
│   └── wsgi.py / asgi.py             # 部署入口
├── lawyer_app/                        # Django 业务应用
│   ├── models.py                      # 4 个数据模型
│   ├── views.py                       # 4 个 API 视图（含限流 + 日志）
│   ├── serializers.py                 # 序列化器（含校验 + Honeypot）
│   ├── admin.py                       # 后台管理（脱敏 + 分组 + 批量操作）
│   └── migrations/                    # 5 个数据库迁移
├── frontend/                          # Vue 前端项目
│   ├── src/
│   │   ├── main.ts                    # 入口（Tailwind CSS 全局样式）
│   │   ├── App.vue                    # 根组件（NavBar + RouterView + FooterBar）
│   │   ├── api/consultation.ts        # API 请求模块（axios + toast）
│   │   ├── utils/toast.ts             # 轻量 Toast 提示（纯 Tailwind）
│   │   ├── router/index.ts            # 路由配置（懒加载）
│   │   ├── styles/main.css            # Tailwind 设计令牌 + 工具类
│   │   ├── components/
│   │   │   ├── NavBar.vue             # 顶部导航栏（毛玻璃 + 移动端汉堡菜单）
│   │   │   ├── HeroSection.vue        # Hero 首屏破冰模块
│   │   │   ├── PracticeSection.vue    # 业务领域双轨卡片（含骨架屏）
│   │   │   ├── CasesSection.vue       # 代表案例 + 客户 Logo 墙
│   │   │   ├── ContactSection.vue     # 预约咨询表单 + 联系方式
│   │   │   └── FooterBar.vue          # 底部版权栏 + 隐私政策链接
│   │   └── views/
│   │       ├── HomeView.vue           # 首页（组合四个 Section 组件）
│   │       ├── PrivacyView.vue        # 隐私保护政策页面
│   │       └── AboutView.vue          # 关于页面（预留）
│   ├── package.json                   # 前端依赖
│   └── vite.config.ts                 # Vite 配置（Tailwind + API 代理）
└── .gitignore                         # Git 排除规则
```

##  设计体系

采用 **Apple 级极简商务风**，自定义四色设计令牌：

| 色系 | 用途 | 色阶 |
|------|------|------|
| **深空灰 (Brand)** | 主色调，文字/背景 | 11 级（#0c0c0e → #f8f8fb） |
| **藏青蓝 (Navy)** | 深色区块背景 | 4 级（#0f1729 → #2a3f66） |
| **饱和金 (Gold)** | 强调色/高亮 | 5 级（#9a7b3a → #f5e6be） |
| **暖白米 (Warm)** | 柔和背景 | 3 级（#faf8f5 → #e8e0d4） |

字体栈：SF Pro Display / PingFang SC（无衬线）+ Noto Serif SC（衬线）

特色效果：毛玻璃工具类（`.glass` / `.glass-dark`）、装饰性光晕渐变、hover 微交互

## 🚀 快速开始

### 环境要求

- Python ≥ 3.13
- Node.js ≥ 22（推荐通过 [fnm](https://github.com/Schniz/fnm) 管理）
- Git

### 1. 克隆仓库

```bash
git clone https://github.com/tanle0727/xvchenlawzuixin.git
cd xvchenlawzuixin
```

### 2. 后端设置

```bash
# 创建虚拟环境并安装依赖
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env，填入你的 DJANGO_SECRET_KEY

# 数据库迁移
python manage.py migrate

# 创建管理员账户
python manage.py createsuperuser

# 启动 Django 开发服务器（端口 8000）
python manage.py runserver
```

### 3. 前端设置

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器（端口 5173，自动代理 /api → localhost:8000）
npm run dev
```

### 4. 访问

| 服务 | 地址 |
|------|------|
| 前端网站 | http://localhost:5173/ |
| Django 管理后台 | http://127.0.0.1:8000/admin/ |
| API 根路径 | http://127.0.0.1:8000/api/ |

## 📦 生产构建

```bash
# 前端构建
cd frontend
npm run build          # 产物输出到 frontend/dist/

# 后端部署（示例：Gunicorn + Nginx）
pip install gunicorn
gunicorn mysite.wsgi:application --bind 0.0.0.0:8000
```

生产环境需在 `.env` 中设置：
```env
DJANGO_SECRET_KEY=你的强密钥
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## 🗄️ 数据模型

| 模型 | 表名 | 用途 | 关键字段 |
|------|------|------|----------|
| `CustomerConsultation` | customer_consultation | 客户预约咨询 | name, phone, case_category, appointment_date, status |
| `RepresentativeCase` | representative_case | 代表案例 | title, role, amount, description, sort_order, is_active |
| `ServiceClient` | service_client | 服务客户 Logo 墙 | name, logo, sort_order, is_active |
| `PracticeArea` | practice_area | 业务领域 | name, category(non_litigation/litigation), sort_order, is_active |

## 🛡️ 安全架构

```
用户浏览器
    │
    ▼
Vue 前端 (5173)  ──Vite Proxy──▶  Django API (8000)
    │                                │
    │  • maxlength 前端限制           │  • Serializer 字段校验
    │  • Honeypot 隐藏字段            │  • Honeypot 服务端验证
    │  • Toast 错误提示               │  • IP 限流 (5/min)
    │  • CSRF Token                   │  • 日期合法性校验
    │                                │  • 安全响应头
    │                                │  • 日志记录 (IP + 操作)
    │                                │  • Admin 手机号脱敏
    │                                ▼
    │                          SQLite / PostgreSQL
    │                          (.env 密钥不入库)
```

## 📋 开发命令速查

```bash
# ===== 后端 =====
source .venv/bin/activate
python manage.py runserver              # 启动开发服务器
python manage.py makemigrations         # 生成迁移
python manage.py migrate                # 应用迁移
python manage.py createsuperuser        # 创建管理员
python manage.py check                  # 系统自检

# 持久化启动（推荐）
nohup python manage.py runserver > /tmp/django_server.log 2>&1 &

# ===== 前端 =====
cd frontend && eval "$(fnm env)"
npm run dev                             # 启动开发服务器
npm run type-check                      # TypeScript 类型检查
npm run build                           # 生产构建

# ===== 数据库备份 =====
bash backup.sh                          # 手动执行一次备份
# crontab -e → 0 2 * * * cd /项目路径 && bash backup.sh >> logs/backup.log 2>&1
```

## 📝 更新日志

| 日期 | 版本 | 内容 |
|------|------|------|
| 2026-09-19 | v1.2 | 整体优化：移除 Element Plus（包体积 -9KB gzip）、轻量 toast、无障碍修复、路由过渡动画、骨架屏、数据库索引、Admin 增强、预约日期校验 |
| 2026-09-19 | v1.1 | 日志系统（api/security/error 三级日志）+ 数据库自动备份脚本 |
| 2026-09-19 | v1.0 | 安全加固：SECRET_KEY 外部化、限流、Honeypot、CSRF、安全响应头、隐私政策页、依赖精简 |
| 2026-09-19 | v0.9 | 前后端联调完成：预约咨询 + 代表案例 + 服务客户 + 业务领域 |
| 2026-09-19 | v0.8 | 后端 REST API 开发（4 个接口 + SimpleUI 管理后台） |
| 2026-09-19 | v0.7 | 后端数据模型设计（4 张表 + 5 个迁移） |
| 2026-09-19 | v0.6 | 许宸律师名片页前端开发（Tailwind CSS + 五模块 + UI 优化） |
| 2026-09-18 | v0.3 | Vue 前端框架集成（Vue 3 + Vite + TypeScript + Tailwind CSS） |
| 2026-09-18 | v0.2 | Django 后台 + SimpleUI 配置 |
| 2026-09-18 | v0.1 | 项目初始化 |

## 📄 许可证

本项目为私人项目，未经授权请勿商用或分发。

---

<p align="center">
  <sub>Built with Vue 3 + Django · Designed for 许宸律师 @ 北京恒都律师事务所</sub>
</p>
