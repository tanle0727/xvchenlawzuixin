<script setup lang="ts">
import { ref, computed } from 'vue'
import wechatQrcode from '@/assets/images/wechat-qrcode.png'
import { submitConsultation } from '@/api/consultation'

// ===== 表单数据模型（与后端字段一一对应） =====
const form = ref({
  name: '',
  position: '',
  company_name: '',
  phone: '',
  case_category: '',
  appointment_date: '',
  case_description: '',
  urgency_level: '一般',
  agreePrivacy: false,
  website_url: '',  // honeypot 隐藏字段，防机器人
})

// ===== 业务类型选项（非诉 + 诉讼，与后端 choices 完全一致） =====
const serviceGroups = [
  {
    label: '非诉业务',
    options: [
      { value: '公司治理', label: '公司治理' },
      { value: '私募股权投融资', label: '私募股权投融资' },
      { value: '国资交易', label: '国资交易' },
      { value: '基金合规', label: '基金管理人募投管退全流程合规法律服务' },
      { value: '交易架构设计', label: '交易架构设计' },
      { value: '保险资管', label: '保险资管' },
    ],
  },
  {
    label: '诉讼业务',
    options: [
      { value: '合同纠纷', label: '合同纠纷' },
      { value: '侵权纠纷', label: '侵权纠纷' },
      { value: '劳动争议', label: '劳动争议' },
      { value: '公司股权纠纷', label: '公司股权纠纷' },
      { value: '金融借款纠纷', label: '金融借款纠纷' },
      { value: '建设工程纠纷', label: '建设工程纠纷' },
      { value: '知识产权纠纷', label: '知识产权纠纷' },
      { value: '不正当竞争纠纷', label: '不正当竞争纠纷' },
    ],
  },
]

// ===== 校验 =====
const phonePattern = /^1[3-9]\d{9}$/
const phoneError = ref('')
const nameError = ref('')

const validatePhone = () => {
  if (!form.value.phone) {
    phoneError.value = '请输入联系电话'
  } else if (!phonePattern.test(form.value.phone)) {
    phoneError.value = '请输入正确的11位手机号'
  } else {
    phoneError.value = ''
  }
}

const validateName = () => {
  nameError.value = form.value.name.trim() ? '' : '请输入客户姓名'
}

const canSubmit = computed(() => {
  return (
    form.value.name.trim() !== '' &&
    phonePattern.test(form.value.phone) &&
    form.value.case_category !== '' &&
    form.value.agreePrivacy
  )
})

// ===== 提交 =====
const submitted = ref(false)
const submitting = ref(false)
const submitError = ref('')

const handleSubmit = async () => {
  validateName()
  validatePhone()
  if (!canSubmit.value) return

  submitting.value = true
  submitError.value = ''
  try {
    await submitConsultation({
      name: form.value.name,
      position: form.value.position,
      company_name: form.value.company_name,
      phone: form.value.phone,
      case_category: form.value.case_category,
      appointment_date: form.value.appointment_date,
      case_description: form.value.case_description,
      urgency_level: form.value.urgency_level,
      website_url: form.value.website_url,  // honeypot
    })
    submitted.value = true
  } catch (err: any) {
    const data = err.response?.data
    if (data && typeof data === 'object') {
      const msgs = Object.values(data).flat() as string[]
      submitError.value = msgs.join('；') || '提交失败，请稍后重试'
    } else {
      submitError.value = '网络异常，请检查连接后重试'
    }
  } finally {
    submitting.value = false
  }
}

const resetForm = () => {
  form.value = {
    name: '',
    position: '',
    company_name: '',
    phone: '',
    case_category: '',
    appointment_date: '',
    case_description: '',
    urgency_level: '一般',
    agreePrivacy: false,
    website_url: '',
  }
  phoneError.value = ''
  nameError.value = ''
  submitted.value = false
  submitting.value = false
  submitError.value = ''
}

// ===== 日期最小值：今天 =====
const todayStr = new Date().toISOString().slice(0, 10)
</script>

<template>
  <section id="contact" class="relative py-24 lg:py-32 bg-warm-100 overflow-hidden">
    <!-- 背景装饰 -->
    <div class="absolute inset-0 -z-0">
      <div class="absolute top-0 right-0 w-[500px] h-[500px] rounded-full bg-gold-300/8 blur-[120px]" />
      <div class="absolute bottom-0 left-0 w-[400px] h-[400px] rounded-full bg-navy-700/4 blur-[100px]" />
    </div>

    <div class="relative max-w-6xl mx-auto px-6 lg:px-8">

      <!-- 区块标题 -->
      <div class="text-center mb-16 lg:mb-20 space-y-4">
        <p class="text-xs font-medium tracking-[0.3em] text-gold-500 uppercase">Get In Touch</p>
        <h2 class="text-3xl lg:text-5xl font-bold text-brand-950 tracking-tight">预约咨询</h2>
        <p class="text-base text-brand-500 max-w-lg mx-auto leading-relaxed">
          请填写以下信息，许宸律师团队将在24小时内与您取得联系
        </p>
        <div class="w-12 h-px bg-gold-500/50 mx-auto mt-6" />
      </div>

      <!-- 提交成功状态 -->
      <div
        v-if="submitted"
        class="max-w-xl mx-auto text-center py-16 space-y-6"
      >
        <div class="w-16 h-16 rounded-full bg-green-50 flex items-center justify-center mx-auto">
          <svg class="w-8 h-8 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
          </svg>
        </div>
        <h3 class="text-2xl font-bold text-brand-950">提交成功</h3>
        <p class="text-brand-500">感谢您的信任，我们将尽快与您联系。</p>
        <button
          @click="resetForm"
          class="inline-flex items-center px-6 py-2.5 rounded-full border border-brand-300 text-sm font-medium text-brand-700 hover:border-brand-950 hover:text-brand-950 transition-all duration-300"
        >
          再次提交
        </button>
      </div>

      <!-- 双栏布局：左表单 + 右联系方式 -->
      <div v-else class="grid lg:grid-cols-5 gap-10 lg:gap-16">

        <!-- 左侧：表单（占3列） -->
        <form
          @submit.prevent="handleSubmit"
          class="lg:col-span-3 space-y-5"
        >
          <!-- Honeypot 隐藏字段：防机器人，正常用户看不到 -->
          <div style="position:absolute;left:-9999px;opacity:0;height:0;width:0;overflow:hidden;" aria-hidden="true">
            <input v-model="form.website_url" type="text" name="website_url" tabindex="-1" autocomplete="off" />
          </div>

          <!-- 第一行：姓名 + 职务 -->
          <div class="grid sm:grid-cols-2 gap-5">
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-brand-700">
                客户姓名
                <span class="text-red-400 ml-0.5">*</span>
              </label>
              <input
                v-model="form.name"
                type="text"
                maxlength="15"
                placeholder="请输入姓名（最多15字）"
                class="w-full px-4 py-3 rounded-xl border bg-white text-brand-900 placeholder:text-brand-400 focus:outline-none focus:ring-2 focus:ring-gold-400/40 transition-all duration-300"
                :class="nameError ? 'border-red-300 focus:border-red-400' : 'border-brand-200/80 focus:border-gold-400'"
                @blur="validateName"
              />
              <p v-if="nameError" class="text-xs text-red-400">{{ nameError }}</p>
            </div>
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-brand-700">
                职务
                <span class="text-brand-400 font-normal ml-1">（选填）</span>
              </label>
              <input
                v-model="form.position"
                type="text"
                maxlength="15"
                placeholder="如：法务总监（最多15字）"
                class="w-full px-4 py-3 rounded-xl border border-brand-200/80 bg-white text-brand-900 placeholder:text-brand-400 focus:outline-none focus:ring-2 focus:ring-gold-400/40 focus:border-gold-400 transition-all duration-300"
              />
            </div>
          </div>

          <!-- 第二行：企业名称 + 电话 -->
          <div class="grid sm:grid-cols-2 gap-5">
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-brand-700">
                企业名称
                <span class="text-brand-400 font-normal ml-1">（选填）</span>
              </label>
              <input
                v-model="form.company_name"
                type="text"
                maxlength="30"
                placeholder="企业全称（最多30字）"
                class="w-full px-4 py-3 rounded-xl border border-brand-200/80 bg-white text-brand-900 placeholder:text-brand-400 focus:outline-none focus:ring-2 focus:ring-gold-400/40 focus:border-gold-400 transition-all duration-300"
              />
            </div>
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-brand-700">
                联系电话
                <span class="text-red-400 ml-0.5">*</span>
              </label>
              <input
                v-model="form.phone"
                type="tel"
                maxlength="11"
                placeholder="11位手机号码"
                class="w-full px-4 py-3 rounded-xl border bg-white text-brand-900 placeholder:text-brand-400 focus:outline-none focus:ring-2 focus:ring-gold-400/40 transition-all duration-300"
                :class="phoneError ? 'border-red-300 focus:border-red-400' : 'border-brand-200/80 focus:border-gold-400'"
                @blur="validatePhone"
              />
              <p v-if="phoneError" class="text-xs text-red-400">{{ phoneError }}</p>
            </div>
          </div>

          <!-- 第三行：业务类型 + 期望预约日期 -->
          <div class="grid sm:grid-cols-2 gap-5">
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-brand-700">
                业务需求类型
                <span class="text-red-400 ml-0.5">*</span>
              </label>
              <div class="relative">
                <select
                  v-model="form.case_category"
                  class="w-full px-4 py-3 rounded-xl border border-brand-200/80 bg-white appearance-none focus:outline-none focus:ring-2 focus:ring-gold-400/40 focus:border-gold-400 transition-all duration-300 cursor-pointer"
                  :class="form.case_category ? 'text-brand-900' : 'text-brand-400'"
                >
                  <option value="" disabled>请选择</option>
                  <optgroup v-for="group in serviceGroups" :key="group.label" :label="group.label">
                    <option v-for="opt in group.options" :key="opt.value" :value="opt.value" class="text-brand-900">
                      {{ opt.label }}
                    </option>
                  </optgroup>
                  <option value="其他" class="text-brand-900">其他</option>
                </select>
                <svg class="absolute right-4 top-1/2 -translate-y-1/2 w-4 h-4 text-brand-400 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" />
                </svg>
              </div>
            </div>
            <div class="space-y-1.5">
              <label class="block text-sm font-medium text-brand-700">
                期望预约日期
                <span class="text-brand-400 font-normal ml-1">（选填）</span>
              </label>
              <input
                v-model="form.appointment_date"
                type="date"
                :min="todayStr"
                class="w-full px-4 py-3 rounded-xl border border-brand-200/80 bg-white text-brand-900 focus:outline-none focus:ring-2 focus:ring-gold-400/40 focus:border-gold-400 transition-all duration-300"
              />
            </div>
          </div>

          <!-- 诉求简述 -->
          <div class="space-y-1.5">
            <label class="block text-sm font-medium text-brand-700">
              诉求简述
              <span class="text-brand-400 font-normal ml-1">（选填）</span>
            </label>
            <textarea
              v-model="form.case_description"
              rows="3"
              maxlength="500"
              placeholder="请简要描述您的法律需求（最多500字）..."
              class="w-full px-4 py-3 rounded-xl border border-brand-200/80 bg-white text-brand-900 placeholder:text-brand-400 focus:outline-none focus:ring-2 focus:ring-gold-400/40 focus:border-gold-400 transition-all duration-300 resize-none"
            />
          </div>

          <!-- Checkbox 行 -->
          <div class="flex flex-col sm:flex-row sm:items-center gap-4 pt-1">
            <label class="flex items-center gap-2.5 cursor-pointer group">
              <div class="relative">
                <input
                  type="checkbox"
                  class="sr-only peer"
                  :checked="form.urgency_level === '紧急'"
                  @change="form.urgency_level = ($event.target as HTMLInputElement).checked ? '紧急' : '一般'"
                />
                <div class="w-[18px] h-[18px] rounded border-2 border-brand-300 bg-white peer-checked:bg-brand-950 peer-checked:border-brand-950 transition-all duration-200 flex items-center justify-center">
                  <svg class="w-2.5 h-2.5 text-white opacity-0 peer-checked:opacity-100 transition-opacity duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
              </div>
              <span class="text-sm text-brand-600 group-hover:text-brand-900 transition-colors">事项紧急</span>
            </label>

            <label class="flex items-start gap-2.5 cursor-pointer group">
              <div class="relative mt-0.5">
                <input v-model="form.agreePrivacy" type="checkbox" class="sr-only peer" />
                <div class="w-[18px] h-[18px] rounded border-2 border-brand-300 bg-white peer-checked:bg-gold-500 peer-checked:border-gold-500 transition-all duration-200 flex items-center justify-center">
                  <svg class="w-2.5 h-2.5 text-white opacity-0 peer-checked:opacity-100 transition-opacity duration-200" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="3" d="M5 13l4 4L19 7" />
                  </svg>
                </div>
              </div>
              <span class="text-sm text-brand-500 leading-relaxed group-hover:text-brand-700 transition-colors">
                同意<router-link to="/privacy" class="text-gold-500 hover:text-gold-400 underline underline-offset-2">《隐私保护政策》</router-link>
              </span>
            </label>
          </div>

          <!-- 错误提示 -->
          <p v-if="submitError" class="text-sm text-red-500 bg-red-50 rounded-lg px-4 py-2.5">
            {{ submitError }}
          </p>

          <!-- 提交按钮 -->
          <button
            type="submit"
            :disabled="!canSubmit || submitting"
            class="w-full py-3.5 rounded-xl text-sm font-semibold tracking-wide transition-all duration-400"
            :class="canSubmit && !submitting
              ? 'bg-gradient-to-r from-brand-950 to-navy-800 text-white hover:shadow-xl hover:shadow-brand-950/25 cursor-pointer'
              : 'bg-brand-200 text-brand-400 cursor-not-allowed'"
          >
            {{ submitting ? '提交中...' : canSubmit ? '提交咨询' : '请填写必填项并同意隐私政策' }}
          </button>
        </form>

        <!-- 右侧：联系方式 + 二维码（占2列） -->
        <div class="lg:col-span-2 space-y-8">
          <!-- 联系信息卡片 -->
          <div class="rounded-2xl border border-brand-200/50 bg-white p-7 space-y-6">
            <h3 class="text-lg font-bold text-brand-950">联系方式</h3>

            <div class="space-y-5">
              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-gold-500/10 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-gold-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-brand-400">邮箱</p>
                  <p class="text-sm font-medium text-brand-800">chen.xu@hengdulaw.com</p>
                </div>
              </div>

              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-gold-500/10 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-gold-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-brand-400">电话</p>
                  <p class="text-sm font-medium text-brand-800">15718858798</p>
                </div>
              </div>

              <div class="flex items-center gap-3.5">
                <div class="w-10 h-10 rounded-xl bg-gold-500/10 flex items-center justify-center shrink-0">
                  <svg class="w-5 h-5 text-gold-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
                  </svg>
                </div>
                <div>
                  <p class="text-xs text-brand-400">地址</p>
                  <p class="text-sm font-medium text-brand-800">北京市朝阳区建国门外大街1号<br/>国贸大厦3期B座50层</p>
                </div>
              </div>
            </div>
          </div>

          <!-- 微信二维码卡片 -->
          <div class="rounded-2xl border border-brand-200/50 bg-white p-7 flex flex-col items-center gap-4">
            <img
              :src="wechatQrcode"
              alt="微信二维码"
              class="w-32 h-32 rounded-xl"
            />
            <p class="text-xs text-brand-500 tracking-wide">扫码添加微信 · 即时沟通</p>
          </div>

          <!-- 标语 -->
          <p class="text-center text-sm font-medium tracking-[0.15em] text-brand-400">
            合作只是开始 &nbsp; <span class="text-gold-500">服务永无止境</span>
          </p>
        </div>

      </div>
    </div>
  </section>
</template>
