<script setup lang="ts">
const currentYear = new Date().getFullYear()
</script>

<template>
  <footer class="bg-navy-900">
    <div class="max-w-6xl mx-auto px-6 lg:px-8 py-10 lg:py-12">
      <div class="flex flex-col md:flex-row items-center justify-between gap-6">
        <!-- 左侧：律所信息 -->
        <div class="flex flex-col items-center md:items-start gap-2">
          <div class="flex items-center gap-2.5">
            <div class="w-7 h-7 rounded-lg bg-gold-500/20 flex items-center justify-center">
              <span class="text-gold-400 font-serif text-xs font-bold">恒</span>
            </div>
            <span class="text-sm font-semibold text-white/90 tracking-wide">北京恒都律师事务所</span>
          </div>
          <p class="text-xs text-brand-400 tracking-wide">
            Beijing Hengdu Law Firm · 专业 · 严谨 · 值得信赖
          </p>
        </div>

        <!-- 右侧：版权 + 隐私政策 -->
        <div class="flex flex-col items-center md:items-end gap-1">
          <p class="text-xs text-brand-500">
            &copy; {{ currentYear }} 北京恒都律师事务所 版权所有
          </p>
          <div class="flex items-center gap-3 text-[10px] text-brand-600">
            <router-link to="/privacy" class="hover:text-gold-400 transition-colors">隐私保护政策</router-link>
            <span class="text-brand-700">|</span>
            <span>本网站内容仅供参考，不构成法律意见</span>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>
