<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getPracticeAreas, type PracticeAreaGroup } from '@/api/consultation'

const groups = ref<PracticeAreaGroup[]>([])
const loadError = ref(false)
const loading = ref(true)

// 图标映射
const icons: Record<string, string> = {
  non_litigation: 'M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z',
  litigation: 'M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3',
}

const subtitles: Record<string, string> = {
  non_litigation: 'Non-Litigation',
  litigation: 'Litigation',
}

onMounted(async () => {
  try {
    groups.value = await getPracticeAreas()
  } catch {
    loadError.value = true
  } finally {
    loading.value = false
  }
})
</script>

<template>
  <section id="practice" class="relative py-24 lg:py-32 bg-navy-900 overflow-hidden">
    <!-- 背景装饰 -->
    <div class="absolute inset-0 -z-0">
      <div class="absolute top-0 left-1/4 w-[500px] h-[500px] rounded-full bg-gold-500/5 blur-[120px]" />
      <div class="absolute bottom-0 right-1/4 w-[400px] h-[400px] rounded-full bg-navy-600/30 blur-[100px]" />
    </div>

    <div class="relative max-w-6xl mx-auto px-6 lg:px-8">

      <!-- 区块标题 -->
      <div class="text-center mb-16 lg:mb-20 space-y-4">
        <p class="text-xs font-medium tracking-[0.3em] text-gold-400 uppercase">Practice Areas</p>
        <h2 class="text-3xl lg:text-5xl font-bold text-white tracking-tight">业务领域</h2>
        <div class="w-12 h-px bg-gold-500/50 mx-auto mt-6" />
      </div>

      <!-- 加载骨架屏 -->
      <div v-if="loading" class="grid lg:grid-cols-2 gap-8 lg:gap-10">
        <div v-for="n in 2" :key="n" class="rounded-2xl border border-white/10 bg-white/5 p-8 lg:p-10 animate-pulse">
          <div class="flex items-center gap-4 mb-8">
            <div class="w-11 h-11 rounded-xl bg-white/10" />
            <div class="space-y-2">
              <div class="h-5 w-24 bg-white/10 rounded" />
              <div class="h-3 w-20 bg-white/5 rounded" />
            </div>
          </div>
          <div class="flex flex-wrap gap-2.5">
            <div v-for="m in 6" :key="m" class="h-9 w-20 bg-white/5 rounded-lg" />
          </div>
        </div>
      </div>

      <!-- 加载失败提示 -->
      <div v-else-if="loadError" class="text-center py-12">
        <p class="text-brand-400 text-sm">数据加载失败，请刷新页面重试</p>
      </div>

      <!-- 双轨卡片布局 -->
      <div v-else-if="groups.length" class="grid lg:grid-cols-2 gap-8 lg:gap-10">

        <div
          v-for="group in groups"
          :key="group.category"
          class="group relative rounded-2xl border border-white/10 bg-white/5 backdrop-blur-sm p-8 lg:p-10 hover:border-gold-400/30 hover:bg-white/8 transition-all duration-500"
        >
          <div class="absolute top-0 right-0 w-32 h-32 bg-gold-400/5 rounded-full blur-[50px] group-hover:bg-gold-400/10 transition-all duration-700" />

          <!-- 图标 + 标题 -->
          <div class="relative flex items-center gap-4 mb-8">
            <div class="w-11 h-11 rounded-xl bg-gold-500/15 flex items-center justify-center shrink-0">
              <svg class="w-5 h-5 text-gold-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" :d="icons[group.category] || icons.non_litigation" />
              </svg>
            </div>
            <div>
              <h3 class="text-xl font-bold text-white">{{ group.category_label }}</h3>
              <p class="text-[11px] tracking-[0.2em] text-brand-400 uppercase mt-0.5">{{ subtitles[group.category] || '' }}</p>
            </div>
          </div>

          <!-- 业务明细 — 标签式布局 -->
          <div class="relative flex flex-wrap gap-2.5">
            <span
              v-for="(item, index) in group.items"
              :key="index"
              class="inline-flex items-center px-4 py-2 rounded-lg bg-white/5 border border-white/8 text-sm text-brand-300 hover:bg-gold-500/10 hover:border-gold-400/20 hover:text-gold-300 transition-all duration-300 cursor-default"
            >
              {{ item }}
            </span>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>
