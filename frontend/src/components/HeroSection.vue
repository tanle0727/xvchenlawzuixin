<script setup lang="ts">
import { ref } from 'vue'
import lawyerProfileImg from '@/assets/images/lawyer-profile.png'

// ===== 真实物料数据（严禁篡改） =====
const lawyer = {
  nameZh: '许宸',
  nameEn: 'Jenny Xu',
  title: '资深律师',
  firm: '北京恒都律师事务所',
  education: '中国政法大学 硕士',
  prevFirms: [
    '北京市环球律师事务所',
    '上海市通力律师事务所北京分所',
  ],
} as const

// 核心数据看板（严格使用真实数据）
const stats = [
  { value: '6+', unit: '年', label: '从业经验' },
  { value: '50+', unit: '家', label: '服务客户' },
  { value: '100+', unit: '个', label: '主办项目' },
] as const

// 个人形象照（使用本地真实照片，响应式变量便于后续对接 API 替换）
const profileImageSrc = ref(lawyerProfileImg)
</script>

<template>
  <section
    id="profile"
    class="relative min-h-screen flex items-center pt-20 lg:pt-24 overflow-hidden"
  >
    <!-- 背景装饰：多层渐变 + 光斑 -->
    <div class="absolute inset-0 -z-10">
      <!-- 主渐变底色：暖米金 → 淡蓝灰，杜绝纯白 -->
      <div class="absolute inset-0 bg-gradient-to-br from-warm-200 via-gold-200/15 to-brand-100" />
      <!-- 右上角大面积金色晕染 -->
      <div class="absolute top-[-15%] right-[-10%] w-[900px] h-[900px] rounded-full bg-gradient-to-bl from-gold-300/30 via-gold-200/15 to-transparent" />
      <!-- 右侧中部暖橙光斑 -->
      <div class="absolute top-[25%] right-[8%] w-[450px] h-[450px] rounded-full bg-gold-400/12 blur-[60px]" />
      <!-- 左下角藏青蓝渐变 -->
      <div class="absolute bottom-[-10%] left-[-10%] w-[700px] h-[700px] rounded-full bg-gradient-to-tr from-navy-800/15 via-navy-700/8 to-transparent" />
      <!-- 左侧淡紫灰光斑 -->
      <div class="absolute top-[15%] left-[3%] w-[350px] h-[350px] rounded-full bg-brand-300/18 blur-[60px]" />
      <!-- 底部向藏青业务区的过渡 -->
      <div class="absolute bottom-0 left-0 right-0 h-32 bg-gradient-to-b from-transparent to-navy-900/12" />
    </div>

    <div class="max-w-6xl mx-auto px-6 lg:px-8 w-full">
      <div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">

        <!-- 左侧：文字信息 -->
        <div class="order-2 lg:order-1 space-y-8">
          <!-- 律所标签 -->
          <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-brand-100/80 border border-brand-200/60">
            <div class="w-1.5 h-1.5 rounded-full bg-gold-500" />
            <span class="text-xs font-medium tracking-wider text-brand-700">{{ lawyer.firm }}</span>
          </div>

          <!-- 姓名与头衔 -->
          <div class="space-y-2">
            <h1 class="text-5xl lg:text-7xl font-bold tracking-tight text-brand-950 leading-[1.1]">
              {{ lawyer.nameZh }}
            </h1>
            <p class="text-xl lg:text-2xl font-light tracking-wide text-brand-600">
              {{ lawyer.nameEn }} · {{ lawyer.title }}
            </p>
          </div>

          <!-- 教育与履历 -->
          <div class="space-y-3 pt-2">
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-gold-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 14l9-5-9-5-9 5 9 5z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
              </svg>
              <span class="text-base text-brand-700">{{ lawyer.education }}</span>
            </div>
            <div class="flex items-start gap-3">
              <svg class="w-5 h-5 text-gold-500 mt-0.5 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
              <div class="space-y-0.5">
                <p class="text-sm text-brand-500">曾就职于</p>
                <p v-for="firm in lawyer.prevFirms" :key="firm" class="text-base text-brand-700">
                  {{ firm }}
                </p>
              </div>
            </div>
          </div>

          <!-- CTA 按钮 -->
          <div class="flex items-center gap-4 pt-4">
            <a
              href="#contact"
              class="inline-flex items-center justify-center px-8 py-3.5 rounded-full bg-brand-950 text-white text-sm font-medium tracking-wide hover:bg-brand-800 transition-all duration-300 shadow-lg shadow-brand-950/20"
            >
              预约咨询
            </a>
            <a
              href="#practice"
              class="inline-flex items-center justify-center px-8 py-3.5 rounded-full border border-brand-300 text-brand-700 text-sm font-medium tracking-wide hover:border-brand-950 hover:text-brand-950 transition-all duration-300"
            >
              了解业务领域
            </a>
          </div>
        </div>

        <!-- 右侧：形象照 + 数据看板 -->
        <div class="order-1 lg:order-2 flex flex-col items-center lg:items-end gap-8">
          <!-- 个人形象照 -->
          <div class="relative group">
            <div class="absolute inset-0 rounded-3xl bg-gradient-to-tr from-gold-500/20 to-brand-200/30 blur-2xl group-hover:blur-xl transition-all duration-700" />
            <img
              :src="profileImageSrc"
              alt="许宸律师"
              class="relative w-72 h-96 lg:w-80 lg:h-[28rem] object-cover rounded-3xl shadow-2xl shadow-brand-950/10 ring-1 ring-white/60"
            />
            <!-- 照片底部金色装饰线 -->
            <div class="absolute bottom-0 left-8 right-8 h-px bg-gradient-to-r from-transparent via-gold-400/60 to-transparent" />
          </div>

          <!-- 数据看板 -->
          <div class="glass rounded-2xl border border-brand-200/60 p-6 w-full max-w-md shadow-lg shadow-brand-950/5">
            <div class="grid grid-cols-3 divide-x divide-brand-200/60">
              <div
                v-for="(stat, index) in stats"
                :key="index"
                class="flex flex-col items-center gap-1 px-2"
              >
                <div class="flex items-baseline gap-0.5">
                  <span class="text-3xl lg:text-4xl font-bold text-brand-950 tracking-tight">
                    {{ stat.value }}
                  </span>
                  <span class="text-sm font-medium text-gold-500">{{ stat.unit }}</span>
                </div>
                <span class="text-xs text-brand-500 tracking-wide">{{ stat.label }}</span>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- 底部滚动提示 -->
    <div class="absolute bottom-8 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 opacity-60 animate-bounce">
      <span class="text-[10px] tracking-[0.3em] text-brand-400 uppercase">Scroll</span>
      <svg class="w-4 h-4 text-brand-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
      </svg>
    </div>
  </section>
</template>
