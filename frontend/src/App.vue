<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import FooterBar from './components/FooterBar.vue'

// 滚动状态：控制导航栏毛玻璃效果
const isScrolled = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 20
}

onMounted(() => window.addEventListener('scroll', handleScroll, { passive: true }))
onUnmounted(() => window.removeEventListener('scroll', handleScroll))
</script>

<template>
  <div class="min-h-screen flex flex-col bg-white">
    <!-- 顶部导航栏 -->
    <NavBar :is-scrolled="isScrolled" />

    <!-- 主内容区 -->
    <main class="flex-1">
      <RouterView />
    </main>

    <!-- 底部版权栏 -->
    <FooterBar />
  </div>
</template>
