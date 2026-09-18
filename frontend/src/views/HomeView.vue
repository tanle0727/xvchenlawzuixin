<script setup lang="ts">
import HeroSection from '@/components/HeroSection.vue'
import PracticeSection from '@/components/PracticeSection.vue'
import CasesSection from '@/components/CasesSection.vue'
import ContactSection from '@/components/ContactSection.vue'
</script>

<template>
  <div>
    <!-- Hero 首屏 -->
    <HeroSection />

    <!-- 业务领域 -->
    <PracticeSection />

    <!-- 代表案例与客户矩阵 -->
    <CasesSection />

    <!-- B端商业线索收集表单 -->
    <ContactSection />
  </div>
</template>
