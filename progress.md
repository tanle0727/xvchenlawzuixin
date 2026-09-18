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
| 后端数据模型设计 | ⬜ 未开始 | — |
| 后端 REST API 开发 | ⬜ 未开始 | — |
| 前后端联调 | ⬜ 未开始 | — |
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
- [x] 代表案例 5 个（网格布局，桌面端 3 列）：
  - 金智维科技C轮融资（5亿元）
  - 思为科技C轮融资（数亿元）
  - 深桑达子公司增资（4亿元）
  - 中润化学融资项目（超一亿元）
  - 与睿创新首轮融资（数千万元）
- [x] 客户 Logo 墙 20 家（从 PPT Slide 7 提取真实 Logo 图片）：
  - vivo、招商局资本、招商创投、远毅资本、蔚来汽车、中国人寿、大家资产、盛世美天、中意资产、光大永明人寿、中信信托、新华保险、阳光保险、中信保诚、招商信诺、光大信托、国开金融、中保投资、中金公司、合众资产
- [x] Logo 默认灰度半透明，hover 恢复彩色

#### Step 5：B端商业线索收集表单
- [x] 双栏布局（左3列表单 + 右2列联系方式）
- [x] 表单字段：企业名称(选填)、联系人及职务(必填)、联系电话(必填+正则校验)、业务需求类型(Select下拉)、诉求简述(选填)、是否紧急(Checkbox)、隐私政策同意(Checkbox，不勾选禁用提交)
- [x] 提交成功状态 + 再次提交按钮
- [x] 右侧联系方式卡片（邮箱、电话、地址）
- [x] 微信二维码（从 PPT 最后一页提取）+ "合作只是开始 服务永无止境"标语

#### UI 整体优化
- [x] 色彩体系升级：纯黑白灰 → 深空灰 + 藏青蓝 + 饱和金色 + 暖白米色
- [x] 各区块背景交替节奏：暖白渐变 → 藏青深色 → 暖米色 → 暖米色 → 藏青底栏
- [x] 导航栏改为藏青深色，与浅色背景形成区分
- [x] 首屏背景多层渐变（暖米金底色 + 金色/藏青/灰紫光斑），杜绝纯白
- [x] 案例从横向滑动改为网格布局
- [x] 表单从单列长表单改为双栏紧凑布局

#### 素材资源
- [x] frontend/src/assets/images/lawyer-profile.png — 许宸律师形象照
- [x] frontend/src/assets/images/wechat-qrcode.png — 微信二维码
- [x] frontend/src/assets/images/logos/ — 20 张 PPT 提取的客户 Logo

---

### ⬜ 阶段五：后端数据模型设计
- [ ] 设计律师信息模型（Lawyer）
- [ ] 设计专业领域模型（PracticeArea）
- [ ] 设计案例模型（Case）
- [ ] 执行数据库迁移
- [ ] 在 admin.py 中注册模型到 SimpleUI 后台

### ⬜ 阶段六：后端 REST API 开发
- [ ] 安装 djangorestframework + django-cors-headers
- [ ] 创建序列化器（Serializers）
- [ ] 创建 API 视图（ViewSets）
- [ ] 配置 API 路由
- [ ] 配置跨域（CORS）

### ⬜ 阶段七：前后端联调
- [ ] 对接律师列表 API
- [ ] 对接律师详情 API
- [ ] 对接专业领域 API
- [ ] 对接案例 API
- [ ] 联调测试

### ⬜ 阶段八：测试与部署
- [ ] 功能测试
- [ ] 生产构建（npm run build）
- [ ] 部署配置

---

## Git 提交历史

```
e72ced3 添加 agent.md 项目指南和 progress.md 进度表
503ad62 完成 Vue 前端集成
9119bc3 完成后台 simpleui 配置
7477c87 项目初始化
```

---

## 待办事项 / 备注

- 前端名片页已完成静态开发，所有数据硬编码在组件中，后续需对接后端 API
- 尚未安装 `djangorestframework` 和 `django-cors-headers`
- 尚未安装 `axios`（前端 HTTP 请求库）
- 尚未创建管理员账户（`python manage.py createsuperuser`）
- lawyer_app 中 models.py / views.py / admin.py 均为空，等待业务开发
- 8 家客户（金融街资本、太平资本、中邮人寿、华安人寿、国寿投资、国民养老、安联资管、美沃斯）在 PPT 中无独立 Logo 图，未展示在 Logo 墙中
