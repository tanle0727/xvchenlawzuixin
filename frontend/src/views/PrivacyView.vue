<script setup lang="ts">
// 隐私保护政策页面 — 纯静态内容，无需数据请求
// 导航栏和页脚由 App.vue 全局提供，本页仅渲染正文
</script>

<template>
  <div class="min-h-screen bg-warm-100 pt-20 lg:pt-28">
    <!-- 返回链接 -->
    <div class="max-w-4xl mx-auto px-6 mb-6">
      <router-link
        to="/"
        class="inline-flex items-center gap-1.5 text-sm text-brand-500 hover:text-gold-500 transition-colors"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
        </svg>
        返回首页
      </router-link>
    </div>

    <!-- 正文区域 -->
    <main class="max-w-4xl mx-auto px-6 pb-12 lg:pb-16">
      <article class="bg-white rounded-2xl shadow-sm border border-brand-200/50 p-5 lg:p-12 space-y-8 text-brand-800 leading-relaxed">

        <!-- 标题 -->
        <header class="text-center space-y-3 pb-8 border-b border-brand-100">
          <h1 class="text-2xl lg:text-3xl font-bold text-brand-950">隐私保护政策</h1>
          <p class="text-sm text-brand-400">更新日期：2026年9月19日 &nbsp;|&nbsp; 生效日期：2026年9月19日</p>
        </header>

        <!-- 引言 -->
        <p>
          北京恒都律师事务所（以下简称"本所"）高度重视您的个人信息安全。本隐私保护政策（以下简称"本政策"）适用于您通过本网站预约咨询服务时所提供的个人信息。请您在提交信息前仔细阅读并充分理解本政策的全部内容。
        </p>

        <!-- 一、收集的个人信息 -->
        <section class="space-y-4">
          <h2 class="text-lg font-bold text-brand-950">一、我们收集的个人信息</h2>
          <p>在您使用本网站预约咨询功能时，我们会收集以下信息：</p>
          <div class="overflow-x-auto -mx-2 px-2">
            <table class="w-full min-w-[480px] text-sm border-collapse">
              <thead>
                <tr class="bg-brand-50 text-left">
                  <th class="px-3 py-2.5 font-semibold text-brand-900 border-b border-brand-200 whitespace-nowrap">字段</th>
                  <th class="px-3 py-2.5 font-semibold text-brand-900 border-b border-brand-200 whitespace-nowrap">是否必填</th>
                  <th class="px-3 py-2.5 font-semibold text-brand-900 border-b border-brand-200">用途</th>
                </tr>
              </thead>
              <tbody class="text-brand-700">
                <tr><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">客户姓名</td><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">是</td><td class="px-3 py-2 border-b border-brand-100">识别委托人身份，用于回电联系</td></tr>
                <tr><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">联系电话</td><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">是</td><td class="px-3 py-2 border-b border-brand-100">与您取得联系、确认预约事宜</td></tr>
                <tr><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">职务</td><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">否</td><td class="px-3 py-2 border-b border-brand-100">了解您的角色背景，便于提供更精准的法律服务</td></tr>
                <tr><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">企业名称</td><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">否</td><td class="px-3 py-2 border-b border-brand-100">了解企业主体信息，便于开展尽职调查或利益冲突检索</td></tr>
                <tr><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">业务需求类型</td><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">是</td><td class="px-3 py-2 border-b border-brand-100">分配合适的律师团队及专业领域</td></tr>
                <tr><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">期望预约日期</td><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">否</td><td class="px-3 py-2 border-b border-brand-100">协调安排咨询时间</td></tr>
                <tr><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">诉求简述</td><td class="px-3 py-2 border-b border-brand-100 whitespace-nowrap">否</td><td class="px-3 py-2 border-b border-brand-100">初步了解您的法律需求，提高沟通效率</td></tr>
                <tr><td class="px-3 py-2 whitespace-nowrap">紧急程度</td><td class="px-3 py-2 whitespace-nowrap">否</td><td class="px-3 py-2">评估事项优先级，合理安排响应时间</td></tr>
              </tbody>
            </table>
          </div>
          <p class="text-sm text-brand-500 mt-3">
            除上述信息外，我们不会主动收集您的身份证号、银行账户、生物识别信息等敏感个人信息。如在后续法律服务过程中确有必要收集，我们将另行取得您的书面同意。
          </p>
        </section>

        <!-- 二、使用目的 -->
        <section class="space-y-3">
          <h2 class="text-lg font-bold text-brand-950">二、个人信息的使用目的</h2>
          <p>我们仅在以下目的范围内使用您的个人信息：</p>
          <ol class="list-decimal list-inside space-y-1.5 pl-2 text-brand-700">
            <li>响应您的预约咨询请求，安排律师与您联系；</li>
            <li>进行利益冲突检索，确保依法合规承接业务；</li>
            <li>为您提供法律咨询服务及后续委托代理事宜；</li>
            <li>法律法规规定的其他必要用途。</li>
          </ol>
        </section>

        <!-- 三、存储与保护 -->
        <section class="space-y-3">
          <h2 class="text-lg font-bold text-brand-950">三、个人信息的存储与保护</h2>
          <ol class="list-decimal list-inside space-y-2 pl-2 text-brand-700">
            <li><strong class="text-brand-900">存储地点：</strong>您的个人信息存储于中华人民共和国境内的服务器中，不进行跨境传输。</li>
            <li><strong class="text-brand-900">存储期限：</strong>我们仅在实现服务目的所必需的最短期限内保留您的个人信息。如双方未建立委托关系，我们将在咨询结束后30日内删除您的预约信息；如建立委托关系，相关信息将依据《律师法》及档案管理要求保存。</li>
            <li><strong class="text-brand-900">安全措施：</strong>我们采取加密传输、访问权限控制、数据库文件权限限制等技术和管理措施保护您的信息安全。仅授权人员可在履行职责所需范围内访问相关信息。</li>
          </ol>
        </section>

        <!-- 四、共享与披露 -->
        <section class="space-y-3">
          <h2 class="text-lg font-bold text-brand-950">四、个人信息的共享与披露</h2>
          <p>未经您的明确同意，我们不会向任何第三方共享、转让或公开披露您的个人信息，但以下情形除外：</p>
          <ol class="list-decimal list-inside space-y-1.5 pl-2 text-brand-700">
            <li>为完成利益冲突检索，需在本所内部系统中进行必要查询；</li>
            <li>依据法律法规、司法程序或政府主管部门的强制性要求；</li>
            <li>为保护国家安全、公共利益或他人合法权益所必需。</li>
          </ol>
        </section>

        <!-- 五、您的权利 -->
        <section class="space-y-3">
          <h2 class="text-lg font-bold text-brand-950">五、您的权利</h2>
          <p>根据《个人信息保护法》，您对个人信息享有以下权利：</p>
          <ol class="list-decimal list-inside space-y-2 pl-2 text-brand-700">
            <li><strong class="text-brand-900">查阅权：</strong>您有权查阅我们持有的关于您的个人信息；</li>
            <li><strong class="text-brand-900">更正权：</strong>如发现信息有误，可要求我们更正；</li>
            <li><strong class="text-brand-900">删除权：</strong>您可要求我们删除您的个人信息（法律法规另有规定的除外）；</li>
            <li><strong class="text-brand-900">撤回同意权：</strong>您可随时撤回对个人信息处理的同意，但不影响撤回前已进行的处理活动的效力；</li>
            <li><strong class="text-brand-900">注销/投诉权：</strong>如您认为我们的处理行为侵犯您的合法权益，可通过下方联系方式向我们提出，或向有关主管部门投诉。</li>
          </ol>
        </section>

        <!-- 六、未成年人保护 -->
        <section class="space-y-3">
          <h2 class="text-lg font-bold text-brand-950">六、未成年人保护</h2>
          <p>本网站面向具有完全民事行为能力的成年人提供法律服务。如您未满十八周岁，请在监护人的陪同下阅读本政策，并由监护人代为提交信息。</p>
        </section>

        <!-- 七、政策更新 -->
        <section class="space-y-3">
          <h2 class="text-lg font-bold text-brand-950">七、政策的更新</h2>
          <p>我们可能适时修订本政策。重大变更将以网站公告形式通知您。更新后的政策自公布之日起生效。</p>
        </section>

        <!-- 八、联系我们 -->
        <section class="space-y-3">
          <h2 class="text-lg font-bold text-brand-950">八、联系我们</h2>
          <p>如您对本政策有任何疑问、意见或需要行使上述权利，请通过以下方式联系：</p>
          <ul class="space-y-2 pl-2 text-brand-700">
            <li><strong class="text-brand-900">邮箱：</strong>chen.xu@hengdulaw.com</li>
            <li><strong class="text-brand-900">电话：</strong>15718858798</li>
            <li><strong class="text-brand-900">地址：</strong>北京市朝阳区建国门外大街1号国贸大厦3期B座50层</li>
          </ul>
        </section>

      </article>
    </main>
  </div>
</template>
