import axios from 'axios'
import { toast } from '@/utils/toast'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

// ===== 响应拦截器：统一错误处理 =====
api.interceptors.response.use(
  (response) => response,
  (error) => {
    const status = error.response?.status
    if (status === 429) {
      toast.warning('操作过于频繁，请稍后再试')
    } else if (status === 403) {
      toast.error('请求被拒绝，请刷新页面后重试')
    } else if (status >= 500) {
      toast.error('服务器异常，请稍后重试')
    } else if (!error.response) {
      toast.error('网络连接失败，请检查网络')
    }
    // 非 4xx 表单校验错误才弹出提示，4xx 业务错误由调用方自行处理
    return Promise.reject(error)
  },
)

/** 提交预约咨询表单 — 字段与后端模型一一对应 */
export interface ConsultationFormData {
  name: string              // 客户姓名
  position: string          // 职务
  company_name: string      // 企业名称
  phone: string             // 联系电话
  case_category: string     // 业务类型
  appointment_date: string  // 期望预约日期 (YYYY-MM-DD)
  case_description: string  // 诉求简述
  urgency_level: string     // 紧急程度: "一般" | "紧急"
  website_url?: string      // honeypot 防机器人
}

export async function submitConsultation(data: ConsultationFormData) {
  const res = await api.post('/consultation/', data)
  return res.data as { message: string }
}

// ===== 代表案例 =====
export interface CaseItem {
  id: number
  title: string
  role: string
  amount: string
  description: string
}

export async function getCases(): Promise<CaseItem[]> {
  const res = await api.get('/cases/')
  return res.data
}

// ===== 服务客户 =====
export interface ClientItem {
  id: number
  name: string
  logo: string
}

export async function getClients(): Promise<ClientItem[]> {
  const res = await api.get('/clients/')
  return res.data
}

// ===== 业务领域 =====
export interface PracticeAreaGroup {
  category: string          // "non_litigation" | "litigation"
  category_label: string    // "非诉业务" | "诉讼业务"
  items: string[]           // 业务名称列表
}

export async function getPracticeAreas(): Promise<PracticeAreaGroup[]> {
  const res = await api.get('/practice-areas/')
  return res.data
}
