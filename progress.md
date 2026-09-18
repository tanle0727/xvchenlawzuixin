# 律师介绍系统 — 项目进度表

> **AI 必读**：每次新会话开始时必须阅读本文件，了解当前进度。
> **AI 必做**：每完成一个功能后，必须在本文件中更新进度并 git commit。

---

## 整体进度概览

| 阶段 | 状态 | 完成日期 |
|------|------|----------|
| 项目初始化 | ✅ 已完成 | 2026-09-18 |
| Django 后台 + SimpleUI | ✅ 已完成 | 2026-09-18 |
| Vue 前端框架集成 | ✅ 已完成 | 2026-09-18 |
| 许宸律师名片页前端开发 | ✅ 已完成 | 2026-09-19 |
| 后端数据模型设计 | ✅ 已完成 | 2026-09-19 |
| 后端 REST API 开发 | ✅ 已完成 | 2026-09-19 |
| 前后端联调（预约咨询） | ✅ 已完成 | 2026-09-19 |
| 前后端联调（案例+客户） | ✅ 已完成 | 2026-09-19 |
| 前后端联调（业务领域） | ✅ 已完成 | 2026-09-19 |
| 安全加固与优化 | ✅ 已完成 | 2026-09-19 |
| 测试与部署 | ⬜ 未开始 | — |

---

## 详细进度记录

### ✅ 阶段一：项目初始化（2026-09-18）
- [x] 创建 Python 虚拟环境（.venv，Python 3.13）
- [x] 安装 Django 6.1.1
- [x] 创建 Django 项目（mysite）和应用（lawyer_app）
- [x] 生成 .gitignore
- [x] Git 初始化并提交（`7477c87 项目初始化`）

### ✅ 阶段二：Django 后台 + SimpleUI（2026-09-18）
- [x] 安装 django-simpleui 2026.1.13
- [x] 配置 INSTALLED_APPS（simpleui 置于 admin 之前）
- [x] 配置中文语言（zh-hans）和时区（Asia/Shanghai）
- [x] Django 服务正常运行于 http://127.0.0.1:8000/admin/
- [x] Git 提交（`9119bc3 完成后台 simpleui 配置`）

### ✅ 阶段三：Vue 前端框架集成（2026-09-18）
- [x] 使用 Vite 创建 Vue 3 + TypeScript 项目（frontend/）
- [x] 安装 Element Plus + Icons（中文语言包已配置）
- [x] 集成 Vue Router + Pinia
- [x] 清理模板代码，创建基础首页（HomeView.vue）
- [x] 更新 .gitignore 排除 node_modules/dist
- [x] Vue 开发服务器正常运行于 http://localhost:5173/
- [x] Git 提交（`503ad62 完成 Vue 前端集成`）

### ✅ 阶段四：许宸律师名片页前端开发（2026-09-19）

> 为北京恒都律师事务所资深律师"许宸(Jenny Xu)"开发专属 B/C 端商业名片网页。
> 所有个人履历、业务领域、案例 100% 使用真实物料数据，零编造。

#### 技术栈变更
- [x] 移除 Element Plus，改用 **Tailwind CSS v4**（Apple 级极简商务风）
- [x] 自定义设计令牌：深空灰 + 藏青蓝 + 饱和金色 + 暖白米色 四色体系
- [x] 毛玻璃工具类（glass / glass-dark）

#### Step 1~5 + UI 优化
- [x] 全局 Layout（NavBar + FooterBar）
- [x] Hero 首屏破冰模块
- [x] 双轨业务领域模块（非诉6项 + 诉讼8项）
- [x] 核心战绩与客户矩阵模块（5案例 + 20客户Logo墙）
- [x] B端商业线索收集表单（双栏布局 + 校验 + 成功状态）
- [x] UI 整体优化（色彩体系、背景交替、导航深色化等）

---

### ✅ 阶段五：后端数据模型设计（2026-09-19）

#### 数据表一览
| 模型 | 表名 | 用途 |
|------|------|------|
| CustomerConsultation | customer_consultation | 客户预约咨询信息表 |
| RepresentativeCase | representative_case | 代表案例表 |
| ServiceClient | service_client | 服务客户Logo墙表 |
| PracticeArea | practice_area | 业务领域表 |

#### CustomerConsultation 字段
- [x] name（客户姓名）、position（职务）、company_name（企业名称）、phone（联系电话）
- [x] appointment_date（期望预约日期）
- [x] case_category（业务类型，15项：6非诉+8诉讼+其他，与前端完全统一）
- [x] case_description（诉求简述）、urgency_level（紧急程度：一般/紧急）
- [x] status（处理状态）、admin_remark（后台备注）、source（预约来源）

#### RepresentativeCase 字段
- [x] title、role、amount、description、sort_order、is_active

#### ServiceClient 字段
- [x] name、logo（ImageField → media/logos/）、sort_order、is_active

#### PracticeArea 字段
- [x] name（业务名称）、category（分类：non_litigation/litigation）、sort_order、is_active

#### 数据库迁移
- [x] 0001_initial.py — CustomerConsultation
- [x] 0002 — 精简字段 + 新增 position/company_name
- [x] 0003 — RepresentativeCase + ServiceClient
- [x] 0004 — PracticeArea

---

### ✅ 阶段六：后端 REST API 开发（2026-09-19）

#### 依赖安装
- [x] djangorestframework、django-cors-headers、Pillow

#### Django 配置
- [x] INSTALLED_APPS、MIDDLEWARE、CORS、REST_FRAMEWORK、MEDIA 配置

#### API 接口
| 方法 | 路径 | 用途 |
|------|------|------|
| POST | /api/consultation/ | 提交预约咨询（含限流 + honeypot 防机器人） |
| GET | /api/cases/ | 获取代表案例列表（仅 is_active=True） |
| GET | /api/clients/ | 获取服务客户列表（logo 返回完整 URL） |
| GET | /api/practice-areas/ | 获取业务领域列表（按非诉/诉讼分组） |

#### Admin 后台
- [x] CustomerConsultationAdmin — 手机号脱敏显示、筛选、搜索
- [x] RepresentativeCaseAdmin — 列表可直接编辑排序号和上下架
- [x] ServiceClientAdmin — Logo 缩略图预览、可直接编辑排序和上下架
- [x] PracticeAreaAdmin — 按分类筛选、可直接编辑排序和上下架

---

### ✅ 阶段七：前后端联调（2026-09-19）

#### 预约咨询联调
- [x] axios + Vite 代理 + ContactSection.vue 接入真实 API
- [x] 前后端字段完全统一，姓名与职务分开填写
- [x] 业务类型下拉分两组（非诉/诉讼），共 15 项
- [x] 期望预约日期选择器、honeypot 防机器人隐藏字段

#### 案例 + 客户联调
- [x] CasesSection.vue 从 API 拉取数据，替换硬编码
- [x] 预置初始数据：5+1 条案例 + 20+1 个客户

#### 业务领域联调
- [x] PracticeSection.vue 从 API 拉取数据，按分类动态渲染
- [x] 预置初始数据：6 非诉 + 8 诉讼 = 14 条

---

### ✅ 阶段八：安全加固与优化（2026-09-19）
- [x] 预约咨询接口限流（ConsultationThrottle：同 IP 每分钟5次/每天20次）
- [x] Honeypot 防机器人（website_url 隐藏字段，填入即拒绝）
- [x] 前端响应拦截器（429/403/500/网络错误统一提示）
- [x] CSRF 防护配置（xsrfCookieName/xsrfHeaderName）
- [x] 后台手机号脱敏显示（138****8000）
- [x] 前端输入 maxlength 限制（姓名15字、职务15字、公司30字、描述500字）
- [x] CasesSection.vue 加载失败提示
- [x] requirements.txt 依赖清单

---

### ⬜ 阶段九：测试与部署
- [ ] 功能测试
- [ ] 生产构建（npm run build）
- [ ] 部署配置

---

## Git 提交历史

```
5edefec 完成后端数据模型、REST API、前后端联调（预约咨询+代表案例+服务客户）
f3501a8 完成许宸律师名片页前端开发（Tailwind CSS + 五模块 + UI优化）
e72ced3 添加 agent.md 项目指南和 progress.md 进度表
503ad62 完成 Vue 前端集成
9119bc3 完成后台 simpleui 配置
7477c87 项目初始化
```

> ⚠️ 业务领域联调 + 安全加固的代码尚未 git commit，待用户确认后提交。

---

## 待办事项 / 备注

### 🔜 二期功能规划
- [ ] 诉求简述一键填入模板（按业务类型提供预设文案，用户点击后自动填充到输入框）

### 📋 日常备注
- 服务客户的 Logo 图片需通过 Django Admin 后台逐个上传（media/logos/ 目录）
- 8 家客户（金融街资本、太平资本、中邮人寿、华安人寿、国寿投资、国民养老、安联资管、美沃斯）在 PPT 中无独立 Logo 图，未录入
- DB Browser for SQLite 打开 db.sqlite3 会导致 Django 报 "database is locked"，使用时需关闭
- 管理员账户已创建（15097801284）
- SimpleUI 多标签页模式为默认行为，点击左侧菜单后注意切换顶部 tab
