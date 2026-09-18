<script setup lang="ts">
import { ref } from 'vue'

defineProps<{
  isScrolled: boolean
}>()

const navLinks = [
  { label: '履历', href: '#profile' },
  { label: '业务', href: '#practice' },
  { label: '案例', href: '#cases' },
  { label: '联系', href: '#contact' },
]

const mobileMenuOpen = ref(false)

const toggleMobile = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobile = () => {
  mobileMenuOpen.value = false
}
</script>

<template>
  <header
    class="fixed top-0 left-0 right-0 z-50 transition-all duration-500 ease-out"
    :class="isScrolled
      ? 'bg-navy-900/95 backdrop-blur-lg shadow-[0_2px_12px_rgba(0,0,0,0.15)]'
      : 'bg-navy-900/80 backdrop-blur-md'"
  >
    <div class="max-w-6xl mx-auto px-6 lg:px-8">
      <nav class="flex items-center justify-between h-16 lg:h-20">
        <!-- Logo / 律所名称 -->
        <a href="#" class="group flex items-center gap-3">
          <div class="w-8 h-8 rounded-lg bg-gold-500/20 flex items-center justify-center">
            <span class="text-gold-400 font-serif text-sm font-bold tracking-wider">恒</span>
          </div>
          <div class="flex flex-col leading-none">
            <span class="text-sm font-semibold tracking-wide text-white/90">恒都律师事务所</span>
            <span class="text-[10px] tracking-[0.2em] text-brand-400 uppercase mt-0.5">Hengdu Law Firm</span>
          </div>
        </a>

        <!-- 桌面端导航链接 -->
        <ul class="hidden md:flex items-center gap-1">
          <li v-for="link in navLinks" :key="link.href">
            <a
              :href="link.href"
              class="px-4 py-2 text-sm font-medium text-white/60 hover:text-white transition-colors duration-300 rounded-full hover:bg-white/10"
            >
              {{ link.label }}
            </a>
          </li>
        </ul>

        <!-- 移动端汉堡按钮 -->
        <button
          class="md:hidden w-10 h-10 flex items-center justify-center rounded-full hover:bg-white/10 transition-colors"
          @click="toggleMobile"
          aria-label="菜单"
        >
          <svg class="w-5 h-5 text-white/80" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path
              v-if="!mobileMenuOpen"
              stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              d="M4 6h16M4 12h16M4 18h16"
            />
            <path
              v-else
              stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5"
              d="M6 18L18 6M6 6l12 12"
            />
          </svg>
        </button>
      </nav>
    </div>

    <!-- 移动端下拉菜单 -->
    <Transition
      enter-active-class="transition-all duration-300 ease-out"
      enter-from-class="opacity-0 -translate-y-2"
      enter-to-class="opacity-100 translate-y-0"
      leave-active-class="transition-all duration-200 ease-in"
      leave-from-class="opacity-100 translate-y-0"
      leave-to-class="opacity-0 -translate-y-2"
    >
      <div v-if="mobileMenuOpen" class="md:hidden bg-navy-900/95 backdrop-blur-lg border-t border-white/10">
        <ul class="px-6 py-4 space-y-1">
          <li v-for="link in navLinks" :key="link.href">
            <a
              :href="link.href"
              class="block px-4 py-3 text-base font-medium text-white/70 hover:text-white hover:bg-white/10 rounded-xl transition-colors"
              @click="closeMobile"
            >
              {{ link.label }}
            </a>
          </li>
        </ul>
      </div>
    </Transition>
  </header>
</template>
