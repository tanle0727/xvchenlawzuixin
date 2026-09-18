import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000,
  headers: { 'Content-Type': 'application/json' },
})

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
