import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: () => import('../views/PrivacyView.vue'),
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: {
        template: `
          <div class="min-h-screen flex flex-col items-center justify-center bg-warm-100 text-brand-900 px-6">
            <h1 class="text-6xl font-serif font-bold text-brand-300 mb-4">404</h1>
            <p class="text-lg mb-8">抱歉，您访问的页面不存在</p>
            <router-link to="/" class="inline-flex items-center gap-2 px-6 py-3 rounded-full bg-brand-800 text-white hover:bg-brand-700 transition-colors">
              ← 返回首页
            </router-link>
          </div>
        `,
      },
    },
  ],
})

export default router
