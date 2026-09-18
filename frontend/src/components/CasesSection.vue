<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { getCases, getClients, type CaseItem, type ClientItem } from '@/api/consultation'

const cases = ref<CaseItem[]>([])
const clients = ref<ClientItem[]>([])

onMounted(async () => {
  const [casesData, clientsData] = await Promise.all([
    getCases().catch(() => [] as CaseItem[]),
    getClients().catch(() => [] as ClientItem[]),
  ])
  cases.value = casesData
  clients.value = clientsData
})
</script>

<template>
  <section id="cases" class="py-24 lg:py-32 bg-warm-100">
    <div class="max-w-6xl mx-auto px-6 lg:px-8">

      <!-- ===== 区块标题 ===== -->
      <div class="text-center mb-16 lg:mb-20 space-y-4">
        <p class="text-xs font-medium tracking-[0.3em] text-gold-500 uppercase">Track Record</p>
        <h2 class="text-3xl lg:text-5xl font-bold text-brand-950 tracking-tight">代表案例</h2>
        <div class="w-12 h-px bg-gold-500/50 mx-auto mt-6" />
      </div>

      <!-- ===== 案例网格卡片 ===== -->
      <div v-if="cases.length" class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="item in cases"
          :key="item.id"
          class="group/card relative rounded-2xl border border-brand-200/50 bg-white p-7 hover:border-gold-400/40 hover:shadow-xl hover:shadow-brand-950/5 transition-all duration-500"
        >
          <!-- 左侧金色竖线装饰 -->
          <div class="absolute left-0 top-6 bottom-6 w-1 rounded-r-full bg-gradient-to-b from-gold-400 to-gold-300/40 opacity-0 group-hover/card:opacity-100 transition-opacity duration-500" />

          <!-- 金额标签 -->
          <div v-if="item.amount" class="inline-flex items-center px-3 py-1 rounded-full bg-gold-500/10 mb-5">
            <span class="text-xs font-semibold text-gold-600">{{ item.amount }}</span>
          </div>

          <!-- 标题 -->
          <h3 class="text-lg font-bold text-brand-950 mb-2.5 leading-snug">
            {{ item.title }}
          </h3>

          <!-- 角色 -->
          <p class="text-sm text-brand-500 mb-3 leading-relaxed">
            {{ item.role }}
          </p>

          <!-- 描述 -->
          <p v-if="item.description" class="text-sm text-brand-600 leading-relaxed">
            {{ item.description }}
          </p>
        </div>
      </div>

      <!-- ===== 合作品牌 Logo 墙 ===== -->
      <div v-if="clients.length" class="mt-24 lg:mt-28">
        <div class="text-center mb-12 space-y-3">
          <p class="text-xs font-medium tracking-[0.3em] text-gold-500 uppercase">Trusted By</p>
          <h3 class="text-2xl lg:text-3xl font-bold text-brand-950 tracking-tight">服务客户</h3>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-5 gap-3 lg:gap-4">
          <div
            v-for="client in clients"
            :key="client.id"
            class="group/logo flex items-center justify-center p-5 rounded-xl border border-brand-200/30 bg-white/80 hover:border-gold-400/30 hover:bg-white hover:shadow-md hover:shadow-brand-950/5 transition-all duration-300 h-[88px]"
          >
            <img
              v-if="client.logo"
              :src="client.logo"
              :alt="client.name"
              class="max-w-full max-h-12 object-contain opacity-50 grayscale group-hover/logo:opacity-100 group-hover/logo:grayscale-0 transition-all duration-300"
            />
            <span v-else class="text-sm text-brand-400">{{ client.name }}</span>
          </div>
        </div>
      </div>

    </div>
  </section>
</template>
