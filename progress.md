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

#### Step 1：全局 Layout
- [x] 安装 tailwindcss + @tailwindcss/vite
- [x] 全局设计令牌（src/styles/main.css）
- [x] 顶部导航栏（NavBar.vue）— 藏青深色底 + 白色文字 + 滚动加深效果
- [x] 底部版权栏（FooterBar.vue）— 藏青深色底栏
- [x] HomeView.vue 四个 section 锚点占位

#### Step 2：Hero 首屏破冰模块
- [x] 姓名（许宸）、中英文头衔（Jenny Xu · 资深律师）
- [x] 教育背景（中国政法大学 硕士）
- [x] 过往履历（环球律所、通力律所北京分所）
- [x] 数据看板（6+年 / 50+家 / 100+个）
- [x] 个人形象照（从用户提供照片导入，响应式变量绑定）
- [x] 多层渐变背景（暖米金 → 淡蓝灰 + 金色/藏青光斑）
- [x] CTA 按钮（预约咨询 / 了解业务领域）

#### Step 3：双轨业务领域模块
- [x] 藏青深色背景（navy-900）+ 毛玻璃卡片
- [x] 非诉业务 6 项：公司治理、私募股权投融资、国资交易、基金管理人募投管退全流程合规法律服务、交易架构设计、保险资管
- [x] 诉讼业务 8 项：合同纠纷、侵权纠纷、劳动争议、公司股权纠纷、金融借款纠纷、建设工程纠纷、知识产权纠纷、不正当竞争纠纷
- [x] 标签药丸式布局，hover 金色高亮

#### Step 4：核心战绩与客户矩阵模块
- [x] 代表案例 5 个（网格布局，桌面端 3 列）
- [x] 客户 Logo 墙 20 家（从 PPT Slide 7 提取真实 Logo 图片）
- [x] Logo 默认灰度半透明，hover 恢复彩色

#### Step 5：B端商业线索收集表单
- [x] 双栏布局（左3列表单 + 右2列联系方式）
- [x] 表单字段 + 校验 + 提交成功状态
- [x] 右侧联系方式卡片 + 微信二维码

#### UI 整体优化
- [x] 色彩体系升级、背景交替节奏、导航栏深色化、首屏多层渐变等

---

### ✅ 阶段五：后端数据模型设计（2026-09-19）

#### 数据表一览
| 模型 | 表名 | 用途 |
|------|------|------|
| CustomerConsultation | customer_consultation | 客户预约咨询信息表 |
| RepresentativeCase | representative_case | 代表案例表 |
| ServiceClient | service_client | 服务客户Logo墙表 |

#### CustomerConsultation 字段
- [x] name（客户姓名）、position（职务）、company_name（企业名称）、phone（联系电话）
- [x] appointment_date（期望预约日期）
- [x] case_category（业务类型，15项：6非诉+8诉讼+其他，与前端完全统一）
- [x] case_description（诉求简述）、urgency_level（紧急程度：一般/紧急）
- [x] status（处理状态：待确认/已确认/已完成/已取消）、admin_remark（后台备注）
- [x] source（预约来源）、created_at、updated_at

#### RepresentativeCase 字段
- [x] title（案例标题）、role（律师角色）、amount（金额标签）、description（案例描述）
- [x] sort_order（排序优先级，数字越小越靠前）
- [x] is_active（是否展示，上下架开关）

#### ServiceClient 字段
- [x] name（客户名称）、logo（Logo图片，ImageField 上传到 media/logos/）
- [x] sort_order（排序优先级）
- [x] is_active（是否展示）

#### 数据库迁移
- [x] 0001_initial.py — CustomerConsultation
- [x] 0002 — 精简字段（去掉 email/gender/appointment_time 等前端不需要的字段，新增 position/company_name）
- [x] 0003 — RepresentativeCase + ServiceClient

---

### ✅ 阶段六：后端 REST API 开发（2026-09-19）

#### 依赖安装
- [x] djangorestframework
- [x] django-cors-headers
- [x] Pillow（ImageField 支持）

#### Django 配置
- [x] INSTALLED_APPS 添加 rest_framework、corsheaders
- [x] MIDDLEWARE 添加 CorsMiddleware
- [x] CORS_ALLOWED_ORIGINS 允许 localhost:5173
- [x] REST_FRAMEWORK 配置（JSONRenderer、日期格式）
- [x] MEDIA_URL / MEDIA_ROOT 配置
- [x] 开发环境 media 文件 URL 路由

#### API 接口
| 方法 | 路径 | 用途 |
|------|------|------|
| POST | /api/consultation/ | 提交预约咨询（前端→后端写入） |
| GET | /api/cases/ | 获取代表案例列表（仅 is_active=True） |
| GET | /api/clients/ | 获取服务客户列表（仅 is_active=True，logo 返回完整 URL） |

#### Admin 后台
- [x] CustomerConsultationAdmin — 列表展示、筛选、搜索
- [x] RepresentativeCaseAdmin — 列表可直接编辑排序号和上下架
- [x] ServiceClientAdmin — 列表可直接编辑排序号和上下架，Logo 缩略图预览

---

### ✅ 阶段七：前后端联调（2026-09-19）

#### 预约咨询联调
- [x] 安装 axios
- [x] 创建 src/api/consultation.ts — 封装 submitConsultation()
- [x] Vite 代理配置（/api → Django 8000）
- [x] ContactSection.vue 接入真实 API（async handleSubmit + loading 状态 + 错误提示）
- [x] 前后端字段完全统一（name/position/company_name/phone/case_category/appointment_date/case_description/urgency_level）
- [x] 姓名与职务分开填写
- [x] 业务类型下拉分两组（非诉业务/诉讼业务），共 15 项，与后端 choices 一致
- [x] 期望预约日期选择器（date input，min=今天）

#### 案例 + 客户联调
- [x] API 函数 getCases() / getClients()
- [x] CasesSection.vue 改为 onMounted 从 API 拉取数据，替换硬编码
- [x] Logo 图片 src 使用后端返回的完整 URL
- [x] 预置初始数据：5 条案例 + 20 个客户名称（Logo 需通过后台上传）

---

### ⬜ 阶段八：测试与部署
- [ ] 功能测试
- [ ] 生产构建（npm run build）
- [ ] 部署配置

---

## Git 提交历史

```
f3501a8 完成许宸律师名片页前端开发（Tailwind CSS + 五模块 + UI优化）
e72ced3 添加 agent.md 项目指南和 progress.md 进度表
503ad62 完成 Vue 前端集成
9119bc3 完成后台 simpleui 配置
7477c87 项目初始化
```

> ⚠️ 阶段五~七的代码尚未 git commit，待用户确认后提交。

---

## 待办事项 / 备注

- 服务客户的 Logo 图片需通过 Django Admin 后台逐个上传（media/logos/ 目录）
- 8 家客户（金融街资本、太平资本、中邮人寿、华安人寿、国寿投资、国民养老、安联资管、美沃斯）在 PPT 中无独立 Logo 图，未录入
- DB Browser for SQLite 打开 db.sqlite3 会导致 Django 报 "database is locked"，使用时需关闭
- 管理员账户已创建（15097801284）
- SimpleUI 多标签页模式为默认行为，点击左侧菜单后注意切换顶部 tab
