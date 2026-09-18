/**
 * 轻量 Toast 提示 — 纯 Tailwind CSS，无第三方依赖
 * 替代 Element Plus 的 ElMessage，减小包体积 ~78KB gzip
 */

type ToastType = 'success' | 'warning' | 'error' | 'info'

interface ToastOptions {
  message: string
  type?: ToastType
  duration?: number
}

const TYPE_STYLES: Record<ToastType, string> = {
  success: 'bg-green-50 text-green-800 border-green-200',
  warning: 'bg-amber-50 text-amber-800 border-amber-200',
  error: 'bg-red-50 text-red-800 border-red-200',
  info: 'bg-blue-50 text-blue-800 border-blue-200',
}

const TYPE_ICONS: Record<ToastType, string> = {
  success: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>',
  warning: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01M12 2a10 10 0 100 20 10 10 0 000-20z"/>',
  error: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>',
  info: '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M12 2a10 10 0 100 20 10 10 0 000-20z"/>',
}

let container: HTMLDivElement | null = null

function getContainer(): HTMLDivElement {
  if (!container || !document.body.contains(container)) {
    container = document.createElement('div')
    container.setAttribute('aria-live', 'polite')
    container.setAttribute('role', 'status')
    Object.assign(container.style, {
      position: 'fixed',
      top: '24px',
      left: '50%',
      transform: 'translateX(-50%)',
      zIndex: '99999',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '8px',
      pointerEvents: 'none',
    })
    document.body.appendChild(container)
  }
  return container
}

function show(options: ToastOptions): void {
  const { message, type = 'info', duration = 3000 } = options
  const root = getContainer()

  const el = document.createElement('div')
  el.className = `pointer-events-auto flex items-center gap-2 px-4 py-2.5 rounded-xl border shadow-lg text-sm font-medium transition-all duration-300 opacity-0 translate-y-[-8px] ${TYPE_STYLES[type]}`
  el.innerHTML = `<svg class="w-4 h-4 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">${TYPE_ICONS[type]}</svg><span>${message}</span>`

  root.appendChild(el)

  // 入场动画
  requestAnimationFrame(() => {
    el.classList.remove('opacity-0', 'translate-y-[-8px]')
    el.classList.add('opacity-100', 'translate-y-0')
  })

  // 自动消失
  setTimeout(() => {
    el.classList.remove('opacity-100', 'translate-y-0')
    el.classList.add('opacity-0', 'translate-y-[-8px]')
    el.addEventListener('transitionend', () => el.remove(), { once: true })
  }, duration)
}

export const toast = {
  success: (message: string, duration?: number) => show({ message, type: 'success', duration }),
  warning: (message: string, duration?: number) => show({ message, type: 'warning', duration }),
  error: (message: string, duration?: number) => show({ message, type: 'error', duration }),
  info: (message: string, duration?: number) => show({ message, type: 'info', duration }),
}
