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

这是一个**前后端分离**的律师个人商业名片网站，用于展示北京恒都律师事务所许宸(Jenny Xu)律师的信息、专业领域、代表案例，并提供 B 端客户预约咨询功能。

- **后端**：Django 6.1（Python 3.12），提供 REST API 和 SimpleUI 管理后台
- **前端**：Vue 3 + Vite + TypeScript + Tailwind CSS v4，独立运行的 SPA 应用
- **数据库**：SQLite3（开发 + 生产环境）
- **语言/时区**：简体中文 / Asia/Shanghai
- **代码仓库**：https://github.com/tanle0727/xvchenlawzuixin（公开仓库）

---

## ️ 生产服务器信息（AI 必读）

| 项目 | 详情 |
|------|------|
| 云服务商 | 579云（内蒙古电信机房） |
| 公网 IP | 211.101.233.19 |
| 系统 | Ubuntu 24.04 |
| CPU / 内存 | 4核 / 4G |
| 系统盘 / 数据盘 | 50G / 50G |
| SSH 登录 | `ssh root@211.101.233.19` |
| 到期时间 | 2026-10-18 |
| 月费 | ¥34.50 |

### 服务器目录结构

```
/home/lawyer-site/                 # 项目根目录
├── .venv/                         # Python 虚拟环境
├── .env                           # 环境变量（DEBUG=False, ALLOWED_HOSTS, SECRET_KEY）
├── manage.py                      # Django 管理入口
├── db.sqlite3                     # SQLite 数据库（生产数据）
├── mysite/                        # Django 项目配置
│   └── settings.py                # 已添加 STATIC_ROOT = BASE_DIR / 'static'
├── lawyer_app/                    # Django 业务应用
├── frontend/                      # Vue 前端源码
│   └── dist/                      # 前端打包产物（Nginx 直接 serve）
├── static/                        # collectstatic 收集的静态文件
├── media/                         # 用户上传文件（Logo 等）
├── logs/                          # 日志文件（api.log / security.log / error.log）
├── backups/                       # 数据库备份
└── requirements.txt               # Python 依赖清单
```

### 服务器关键配置文件

| 文件 | 路径 | 说明 |
|------|------|------|
| Gunicorn 服务 | `/etc/systemd/system/lawyer_backend.service` | 3 workers，绑定 127.0.0.1:8000，开机自启 |
| Nginx 站点配置 | `/etc/nginx/sites-available/lawyer_site` | 监听 8080 端口，反向代理 |
| Nginx 软链接 | `/etc/nginx/sites-enabled/lawyer_site` | → sites-available/lawyer_site |
| 环境变量 | `/home/lawyer-site/.env` | DJANGO_SECRET_KEY / DEBUG / ALLOWED_HOSTS |

### Nginx 路由规则

| 路径 | 处理方式 |
|------|---------|
| `/` | 前端 Vue SPA（root → /home/lawyer-site/frontend/dist，try_files 解决路由刷新 404） |
| `/api/` | 代理到 Gunicorn http://127.0.0.1:8000 |
| `/admin/` | 代理到 Gunicorn http://127.0.0.1:8000 |
| `/static/` | alias → /home/lawyer-site/static/ |
| `/media/` | alias → /home/lawyer-site/media/ |

### 生产环境访问地址

| 服务 | 地址 |
|------|------|
| 网站前台 | http://211.101.233.19:8080 |
| Admin 后台 | http://211.101.233.19:8080/admin/ |
| 管理员账号 | Tanle0727（密码由用户自行设置） |

### 服务器运维命令速查

```bash
# 查看后端服务状态
systemctl status lawyer_backend

# 重启后端服务
systemctl restart lawyer_backend

# 查看后端日志
journalctl -u lawyer_backend -f

# 重启 Nginx
systemctl restart nginx

# 验证 Nginx 配置
nginx -t

# 查看 Nginx 错误日志
tail -f /var/log/nginx/error.log

# 进入 Django Shell
cd /home/lawyer-site && source .venv/bin/activate && python manage.py shell

# 手动执行数据库备份
cd /home/lawyer-site && bash backup.sh
```

### 更新部署流程（每次代码更新后执行）

用户在本地修改代码并 `git push origin master` 后，SSH 登录服务器执行：

```bash
cd /home/lawyer-site
git pull origin master
source .venv/bin/activate

# 如果后端依赖有变更
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# 如果数据库模型有变更
python manage.py migrate --noinput

# 收集静态文件
python manage.py collectstatic --noinput

# 如果前端有变更
cd frontend && npm install --registry=https://registry.npmmirror.com && npm run build && cd ..

# 重启后端
systemctl restart lawyer_backend
```

> **简化版**：不确定改了什么就全部跑一遍，不会出错，约 1 分钟完成。

### pip / npm 镜像源（服务器在国内，必须使用镜像）

| 工具 | 镜像源 |
|------|--------|
| pip | `-i https://pypi.tuna.tsinghua.edu.cn/simple` |
| npm | `--registry=https://registry.npmmirror.com` |

> ⚠️ 服务器默认 apt 源指向阿里云内网镜像（mirrors.cloud.aliyuncs.com），但 579 云不在阿里云内网，pip 不加镜像源会超时。

---

## ⚠️ 已知问题与待解决事项

### 🔴 高优先级

| 问题 | 说明 | 解决方案 |
|------|------|---------|
| ICP 备案未办理 | 579 云不支持备案接入，80 端口被拦截，当前使用 8080 端口 | 迁移到阿里云/腾讯云后提交 ICP 备案，通过后改回 80 端口 |
| 无 HTTPS | 未配置 SSL 证书，settings.py 中 SECURE_SSL_REDIRECT=False | 绑定域名后申请免费 SSL 证书（Let's Encrypt），启用 HTTPS |
| 服务器到期 | 2026-10-18 到期，届时网站将不可访问 | 续费或迁移到新服务器 |
| 数据库为 SQLite | 生产环境使用 SQLite，并发写入性能有限 | 当前流量小可暂用；流量增大后迁移到 PostgreSQL |

### 🟡 中优先级

| 问题 | 说明 | 解决方案 |
|------|------|---------|
| crontab 未配置 | backup.sh 备份脚本已写好但未设置定时任务 | 在服务器执行 `crontab -e` 添加 `0 3 * * * /home/lawyer-site/backup.sh` |
| SECRET_KEY 未更换 | 生产环境沿用开发环境的密钥 | 在服务器 .env 中生成新密钥：`python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"` |
| CORS 仅配开发地址 | CORS_ALLOWED_ORIGINS 只有 localhost:5173 | 同域部署下不影响；若后续前后端分离部署需更新 |
| 无监控告警 | 服务宕机无人知晓 | 可接入 UptimeRobot（免费）监控 http://211.101.233.19:8080 |

### 🟢 低优先级 / 二期规划

| 问题 | 说明 |
|------|------|
| 诉求简述模板 | 按业务类型提供预设文案，用户点击自动填充 |
| 邮件通知 | 有新预约时发邮件/短信通知律师 |
| 数据导出 | Admin 后台支持导出 Excel |
| 移动端适配优化 | NavBar 组件已有移动端适配，可进一步打磨 |

---

## 📋 后续优化路线图

### 短期（服务器到期前）
1. 配置 crontab 定时备份数据库
2. 接入 UptimeRobot 免费监控
3. 更换生产环境 SECRET_KEY

### 中期（迁移新服务器时）
1. 购买阿里云/腾讯云 Ubuntu 24.04 服务器
2. 执行一键部署脚本（见 progress.md 阶段十一）
3. 提交 ICP 备案
4. 绑定域名 + 配置 HTTPS（certbot + Let's Encrypt）
5. Nginx 端口改回 80，配置 443 SSL
6. settings.py 中恢复 SECURE_SSL_REDIRECT=True 等安全配置
7. 数据库从 SQLite 迁移到 PostgreSQL（可选）

### 长期
1. CI/CD 自动化部署（GitHub Actions → 服务器自动拉取更新）
2. 日志集中管理
3. 性能优化（CDN 加速静态资源、数据库索引优化）

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
| Python | 3.12（服务器）/ 3.13（本地） | 运行环境 |
| Django | 6.1 | Web 框架 |
| django-simpleui | 2026.1.13 | 管理后台 UI 主题 |
| djangorestframework | password | REST API |
| django-cors-headers | 4.9.0 | 跨域支持 |
| python-decouple | 3.8 | .env 环境变量读取 |
| Pillow | 12.3.0 | 图片处理 |
| gunicorn | 26.2.0 | 生产 WSGI 服务器（仅服务器安装） |
| SQLite3 | — | 数据库 |

### 前端
| 技术 | 版本 | 说明 |
|------|------|------|
| Vue | 3.5.x | 前端框架（Composition API + `<script setup>`） |
| Vite | 8.x | 构建工具 |
| TypeScript | 6.x | 开发语言 |
| Tailwind CSS | 4.x | 样式框架（Apple 级极简商务风） |
| Vue Router | 5.x | 路由管理 |
| Pinia | 4.x | 状态管理 |
| axios | 1.20.x | HTTP 请求（baseURL: '/api'） |

> ⚠️ Element Plus 已在阶段十移除，改用纯 Tailwind CSS + 自建 toast 组件。

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

### 本地开发
| 服务 | 地址 |
|------|------|
| Django 管理后台 | http://127.0.0.1:8000/admin/ |
| Vue 前端 | http://localhost:5173/ |

### 生产环境
| 服务 | 地址 |
|------|------|
| 网站前台 | http://211.101.233.19:8080 |
| Admin 后台 | http://211.101.233.19:8080/admin/ |

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
- UI 样式使用 **Tailwind CSS v4**（Element Plus 已移除，不要引入）
- Toast 提示使用 `@/utils/toast`（纯 Tailwind 实现，不要用 ElMessage）
- 路由配置在 `src/router/index.ts`
- 全局状态使用 Pinia，store 文件放在 `src/stores/`
- API 请求使用 axios，baseURL 为 `/api`（生产环境由 Nginx 转发到 Django）
- Node.js 版本要求 ≥22.18（package.json engines 字段约束）

### 前后端联调
- 本地开发：前端 5173 端口，后端 8000 端口，通过 Vite proxy 转发 /api 请求
- 生产环境：Nginx 统一入口 8080 端口，/api/ 和 /admin/ 转发到 Gunicorn 8000 端口
- 跨域：同域部署无需 CORS；本地开发通过 Vite proxy 解决
