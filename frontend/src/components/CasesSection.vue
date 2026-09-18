<script setup lang="ts">
// Logo 图片导入（从 PPT 提取的真实 Logo）
import logoVivo from '@/assets/images/logos/logo_vivo.png'
import logoZhaoshangCapital from '@/assets/images/logos/logo_zhaoshang_capital.png'
import logoZhaoshangVenture from '@/assets/images/logos/logo_zhaoshang_venture.png'
import logoYuanyi from '@/assets/images/logos/logo_yuanyi.jpg'
import logoNio from '@/assets/images/logos/logo_nio.jpg'
import logoChinaLife from '@/assets/images/logos/logo_china_life.jpg'
import logoDajia from '@/assets/images/logos/logo_dajia.jpg'
import logoMetime from '@/assets/images/logos/logo_metime.jpg'
import logoGcamc from '@/assets/images/logos/logo_gcamc.png'
import logoSunlife from '@/assets/images/logos/logo_sunlife.jpg'
import logoCiticTrust from '@/assets/images/logos/logo_citic_trust.jpg'
import logoNci from '@/assets/images/logos/logo_nci.jpg'
import logoSunshine from '@/assets/images/logos/logo_sunshine.jpg'
import logoCiticPrudential from '@/assets/images/logos/logo_citic_prudential.jpg'
import logoCignacmb from '@/assets/images/logos/logo_cigna_cmb.jpg'
import logoEverbrightTrust from '@/assets/images/logos/logo_everbright_trust.jpg'
import logoCdbCapital from '@/assets/images/logos/logo_cdb_capital.jpg'
import logoZhongbao from '@/assets/images/logos/logo_zhongbao.jpg'
import logoCicc from '@/assets/images/logos/logo_cicc.jpg'
import logoUnionAsset from '@/assets/images/logos/logo_union_asset.png'

// ===== 真实物料数据（严禁篡改或编造） =====

const cases = [
  {
    id: 1,
    title: '金智维科技C轮融资',
    role: '领投方国开制造业基金及部分跟投方法律顾问',
    amount: '5亿元',
    description: '为珠海金智维信息科技有限公司5亿元人民币C轮融资提供全程法律服务',
  },
  {
    id: 2,
    title: '思为科技C轮融资',
    role: '领投方招商局创投法律顾问',
    amount: '数亿元',
    description: '为深圳思为科技有限公司数亿元人民币的C轮融资提供全程法律服务',
  },
  {
    id: 3,
    title: '深桑达子公司增资',
    role: '外部战略投资者国开制造业基金法律顾问',
    amount: '4亿元',
    description: '为深桑达下属全资子公司中电云认购全部4亿元人民币外部战略投资者增资额度提供全程法律服务',
  },
  {
    id: 4,
    title: '中润化学融资项目',
    role: '领投方招商局资本法律顾问',
    amount: '超一亿元',
    description: '为重庆市中润化学有限公司完成超一亿元人民币的融资提供全程法律服务',
  },
  {
    id: 5,
    title: '与睿创新首轮融资',
    role: '独家投资人远毅资本法律顾问',
    amount: '数千万元',
    description: '为与睿创新（苏州）医疗科技有限公司数千万元人民币的首轮融资提供全程法律服务',
  },
] as const

// 客户列表（仅展示 PPT Slide 7 照片墙中有真实 Logo 图片的企业）
const clients = [
  { name: 'vivo', logoSrc: logoVivo },
  { name: '招商局资本', logoSrc: logoZhaoshangCapital },
  { name: '招商创投', logoSrc: logoZhaoshangVenture },
  { name: '远毅资本', logoSrc: logoYuanyi },
  { name: '蔚来汽车', logoSrc: logoNio },
  { name: '中国人寿', logoSrc: logoChinaLife },
  { name: '大家资产', logoSrc: logoDajia },
  { name: '盛世美天', logoSrc: logoMetime },
  { name: '中意资产', logoSrc: logoGcamc },
  { name: '光大永明人寿', logoSrc: logoSunlife },
  { name: '中信信托', logoSrc: logoCiticTrust },
  { name: '新华保险', logoSrc: logoNci },
  { name: '阳光保险', logoSrc: logoSunshine },
  { name: '中信保诚', logoSrc: logoCiticPrudential },
  { name: '招商信诺', logoSrc: logoCignacmb },
  { name: '光大信托', logoSrc: logoEverbrightTrust },
  { name: '国开金融', logoSrc: logoCdbCapital },
  { name: '中保投资', logoSrc: logoZhongbao },
  { name: '中金公司', logoSrc: logoCicc },
  { name: '合众资产', logoSrc: logoUnionAsset },
]
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

      <!-- ===== 案例网格卡片（桌面端3列，移动端单列） ===== -->
      <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="item in cases"
          :key="item.id"
          class="group/card relative rounded-2xl border border-brand-200/50 bg-white p-7 hover:border-gold-400/40 hover:shadow-xl hover:shadow-brand-950/5 transition-all duration-500"
        >
          <!-- 左侧金色竖线装饰 -->
          <div class="absolute left-0 top-6 bottom-6 w-1 rounded-r-full bg-gradient-to-b from-gold-400 to-gold-300/40 opacity-0 group-hover/card:opacity-100 transition-opacity duration-500" />

          <!-- 金额标签 -->
          <div class="inline-flex items-center px-3 py-1 rounded-full bg-gold-500/10 mb-5">
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
          <p class="text-sm text-brand-600 leading-relaxed">
            {{ item.description }}
          </p>
        </div>
      </div>

      <!-- ===== 合作品牌 Logo 墙 ===== -->
      <div class="mt-24 lg:mt-28">
        <div class="text-center mb-12 space-y-3">
          <p class="text-xs font-medium tracking-[0.3em] text-gold-500 uppercase">Trusted By</p>
          <h3 class="text-2xl lg:text-3xl font-bold text-brand-950 tracking-tight">服务客户</h3>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-5 gap-3 lg:gap-4">
          <div
            v-for="client in clients"
            :key="client.name"
            class="group/logo flex items-center justify-center p-5 rounded-xl border border-brand-200/30 bg-white/80 hover:border-gold-400/30 hover:bg-white hover:shadow-md hover:shadow-brand-950/5 transition-all duration-300 h-[88px]"
          >
            <img
              :src="client.logoSrc"
              :alt="client.name"
              class="max-w-full max-h-12 object-contain opacity-50 grayscale group-hover/logo:opacity-100 group-hover/logo:grayscale-0 transition-all duration-300"
            />
          </div>
        </div>
      </div>

    </div>
  </section>
</template>
