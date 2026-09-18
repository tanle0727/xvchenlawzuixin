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
| 日志系统 + 数据库备份 | ✅ 已完成 | 2026-09-19 |
| 整体优化（依赖清理+体验增强） | ✅ 已完成 | 2026-09-19 |
| 生产服务器部署（579云） | ✅ 已完成 | 2026-09-19 |

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

#### 第一批：严重级
- [x] SECRET_KEY 外部化（python-decouple + .env，移除硬编码密钥）
- [x] DEBUG / ALLOWED_HOSTS 从环境变量读取（上线时改 .env 即可）
- [x] 预约咨询接口限流（ConsultationThrottle：同 IP 每分钟5次）
- [x] Honeypot 防机器人（website_url 隐藏字段，填入即拒绝）
- [x] Serializer 字段长度校验（姓名≤15、职务≤15、公司≤30、案情≤500）
- [x] 前端 maxlength 限制 + honeypot 隐藏字段
- [x] db.sqlite3 文件权限收紧为 600
- [x] Admin 后台手机号脱敏显示（138****8000）
- [x] API 无 PII 泄露确认（仅 POST 写入，无 GET 查询）

#### 第二批：高危级
- [x] 安全响应头（XSS_FILTER / NOSNIFF / X_FRAME_OPTIONS=DENY / HTTPONLY Cookie）
- [x] SSL 相关配置（HSTS / SSL_REDIRECT / COOKIE_SECURE，仅 DEBUG=False 时启用）
- [x] 隐私保护政策页面（/privacy，8章节完整，符合《个人信息保护法》）
- [x] 表单隐私政策链接修复（href="#" → router-link to="/privacy"）
- [x] axios CSRF 配置（xsrfCookieName / xsrfHeaderName）
- [x] 响应拦截器统一错误提示（429/403/5xx/网络错误）
- [x] CasesSection.vue 加载失败状态区分（不再静默吞错）
- [x] 虚拟环境精简（187包 → 9包，减少95%攻击面）
- [x] requirements.txt 精确版本依赖清单

#### 依赖安全扫描
- [x] pip-audit：Python 依赖 0 漏洞（pip 已升级修复）
- [x] npm audit：前端依赖 0 漏洞

---

### ✅ 阶段九：日志系统 + 数据库备份（2026-09-19）

#### 日志配置（mysite/settings.py）
- [x] LOGGING 配置，日志目录 logs/（已加入 .gitignore）
- [x] api.log — 业务日志（预约提交成功/失败，含 IP、姓名、类型）
- [x] security.log — Django 安全事件（登录失败、CSRF 拒绝等）
- [x] error.log — 服务器错误日志
- [x] 均使用 RotatingFileHandler（单文件10MB，保留5份）

#### 业务日志埋点（lawyer_app/views.py）
- [x] create_consultation 视图记录提交成功/失败日志（含来源 IP）

#### 数据库备份脚本（backup.sh）
- [x] 基于 sqlite3 .backup 命令的安全备份（避免复制中写入导致损坏）
- [x] 按时间戳生成备份文件，存放于 backups/（已加入 .gitignore）
- [x] 保留最近30天备份，自动清理过期文件
- [x] 预留 crontab 每日定时执行说明（未实际配置 crontab）

---

### ✅ 阶段十：整体优化（2026-09-19）

#### P0 — 必须修复
- [x] 移除 Element Plus 残留依赖（element-plus + @element-plus/icons-vue），包体积减少 ~9KB gzip
- [x] 新建 utils/toast.ts 轻量 toast（纯 Tailwind CSS，无第三方依赖），替换 ElMessage
- [x] 删除 Pinia counter store 无用代码（Vite 模板遗留）
- [x] 后端添加预约日期校验（validate_appointment_date 拒绝过去日期）

#### P1 — 建议优化
- [x] PrivacyView 复用全局 NavBar + FooterBar，移除内联 nav/footer 重复代码
- [x] NavBar 汉堡按钮加 aria-expanded；SVG 加 aria-hidden="true"
- [x] App.vue 加 skip-to-content 无障碍链接
- [x] FooterBar 补充隐私政策链接
- [x] 数据库索引优化（phone/appointment_date/status 加 db_index=True）
- [x] Admin 后台增强：fieldsets 分组、date_hierarchy、批量标记完成/已确认 action
- [x] ServiceClient.logo 允许为空（blank=True, default=''）

#### P2 — 锦上添花
- [x] 页面路由过渡动画（淡入淡出 0.25s）
- [x] PracticeSection 加载骨架屏（animate-pulse 占位）

#### 验证结果
- [x] TypeScript 类型检查零错误
- [x] 生产构建成功，模块数 1668 → 104，包体积 210KB → 185KB（gzip 78KB → 69KB）
- [x] Django check 零问题，迁移生成并应用成功
- [x] API 测试：过去日期 → 400 拒绝 ✅，正常提交 → 201 ✅
- [x] npm audit：0 漏洞

---

### ✅ 阶段十一：生产服务器部署（2026-09-19）

#### 服务器信息
| 项目 | 详情 |
|------|------|
| 云服务商 | 579云（内蒙古电信机房） |
| 公网 IP | 211.101.233.19 |
| 系统 | Ubuntu 24.04 |
| CPU / 内存 | 4核 / 4G |
| 系统盘 / 数据盘 | 50G / 50G |
| 登录用户 | root |
| 到期时间 | 2026-10-18 |
| 月费 | ¥34.50 |

#### 第一阶段：基础环境安装
- [x] apt update && apt upgrade
- [x] 安装 python3, python3-venv, python3-pip, git, nginx, curl
- [x] 安装 Node.js 22.x（前端要求 ≥22.18，从 Node 20 升级）
- [x] 创建项目目录 /home/lawyer-site

#### 第二阶段：代码拉取与后端环境
- [x] git clone https://github.com/tanle0727/xvchenlawzuixin.git .
- [x] Python 虚拟环境 .venv 创建并激活
- [x] pip install -r requirements.txt（清华镜像源）
- [x] pip install gunicorn（生产 WSGI 服务器）
- [x] 创建 .env 文件（DEBUG=False, ALLOWED_HOSTS=211.101.233.19）
- [x] settings.py 添加 STATIC_ROOT = BASE_DIR / 'static'
- [x] python manage.py migrate（数据库迁移）
- [x] python manage.py collectstatic --noinput（2606 个静态文件）
- [x] python manage.py createsuperuser（用户名 Tanle0727）

#### 第三阶段：前端打包 + Gunicorn + Nginx
- [x] npm install + npm run build（前端打包到 frontend/dist/）
- [x] 创建 /etc/systemd/system/lawyer_backend.service（Gunicorn 守护进程，3 workers，开机自启）
- [x] 创建 /etc/nginx/sites-available/lawyer_site（Nginx 反向代理配置）
- [x] Nginx 监听 8080 端口（80 端口因未备案被 579 云拦截）
- [x] systemctl restart nginx + lawyer_backend

#### 部署后修复
- [x] settings.py 中 SECURE_SSL_REDIRECT / SESSION_COOKIE_SECURE / CSRF_COOKIE_SECURE 改为 False（未配置 SSL 时强制 HTTPS 会导致无法访问）

#### 访问地址
| 服务 | 地址 |
|------|------|
| 网站前台 | http://211.101.233.19:8080 |
| Admin 后台 | http://211.101.233.19:8080/admin/ |
| 管理员账号 | Tanle0727 |

#### 更新部署命令（每次代码更新后在服务器执行）
```bash
cd /home/lawyer-site
git pull origin master
source .venv/bin/activate
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
python manage.py migrate --noinput
python manage.py collectstatic --noinput
cd frontend && npm install --registry=https://registry.npmmirror.com && npm run build && cd ..
systemctl restart lawyer_backend
```

---

## Git 提交历史

```
22b55d1 更新 progress.md：补充安全加固完整记录（第一批+第二批+依赖扫描）
3b6a876 更新 progress.md：补充安全加固提交记录，移除过时提示
16fc1d1 新增业务领域后台管理 + 安全加固（限流/防机器人/CSRF/脱敏）
5edefec 完成后端数据模型、REST API、前后端联调（预约咨询+代表案例+服务客户）
f3501a8 完成许宸律师名片页前端开发（Tailwind CSS + 五模块 + UI优化）
e72ced3 添加 agent.md 项目指南和 progress.md 进度表
503ad62 完成 Vue 前端集成
9119bc3 完成后台 simpleui 配置
7477c87 项目初始化
```

---

## 待办事项 / 备注

### 🔴 高优先级（影响线上可用性）
- [ ] ICP 备案：579 云不支持备案，80 端口被拦截，当前用 8080。需迁移到阿里云/腾讯云后备案
- [ ] HTTPS 配置：未配置 SSL 证书，settings.py 中 SECURE_SSL_REDIRECT=False。绑域名后用 certbot 申请 Let's Encrypt 证书
- [ ] 服务器续费/迁移：2026-10-18 到期，届时网站不可访问
- [ ] 更换生产 SECRET_KEY：当前沿用开发环境密钥，应在服务器 .env 中生成新密钥

### 🟡 中优先级（运维完善）
- [ ] 配置 crontab 定时备份：`0 3 * * * /home/lawyer-site/backup.sh`（每日凌晨 3 点自动备份）
- [ ] 接入 UptimeRobot 免费监控：监控 http://211.101.233.19:8080 可用性
- [ ] SQLite → PostgreSQL：当前流量小可暂用，流量增大后需迁移

### 🟢 低优先级 / 二期功能
- [ ] 诉求简述一键填入模板（按业务类型提供预设文案，用户点击后自动填充到输入框）
- [ ] 邮件/短信通知：有新预约时通知律师
- [ ] Admin 后台数据导出 Excel
- [ ] CI/CD 自动化部署（GitHub Actions → 服务器自动拉取更新）

### 📋 日常备注
- 服务客户的 Logo 图片需通过 Django Admin 后台逐个上传（media/logos/ 目录）
- 8 家客户（金融街资本、太平资本、中邮人寿、华安人寿、国寿投资、国民养老、安联资管、美沃斯）在 PPT 中无独立 Logo 图，未录入
- DB Browser for SQLite 打开 db.sqlite3 会导致 Django 报 "database is locked"，使用时需关闭
- 管理员账户：Tanle0727
- SimpleUI 多标签页模式为默认行为，点击左侧菜单后注意切换顶部 tab
- 服务器 pip 必须加清华镜像源 `-i https://pypi.tuna.tsinghua.edu.cn/simple`，否则超时
- 服务器 npm 必须加淘宝镜像源 `--registry=https://registry.npmmirror.com`
