<script setup lang="ts">
</script>

<template>
  <div class="home-container">
    <el-card shadow="hover">
      <template #header>
        <div class="card-header">
          <span>欢迎使用律师介绍系统</span>
        </div>
      </template>
      <p>前端框架已就绪，等待后端 API 对接。</p>
    </el-card>
  </div>
</template>

<style scoped>
.home-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f5f7fa;
}

.card-header {
  font-size: 20px;
  font-weight: bold;
}
</style>
