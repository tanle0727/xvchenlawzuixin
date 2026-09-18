import csv
from django.http import HttpResponse
from django.contrib import admin, messages
from django.utils.html import format_html
from .models import CustomerConsultation, RepresentativeCase, ServiceClient, PracticeArea


@admin.register(CustomerConsultation)
class CustomerConsultationAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company_name', 'masked_phone', 'appointment_date', 'case_category', 'urgency_level', 'status', 'created_at']
    list_filter = ['status', 'case_category', 'urgency_level', 'source']
    search_fields = ['name', 'phone', 'company_name']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'

    # 编辑页字段分组
    fieldsets = [
        ('客户信息', {
            'fields': ['name', 'position', 'company_name', 'phone'],
        }),
        ('预约详情', {
            'fields': ['case_category', 'appointment_date', 'case_description', 'urgency_level'],
        }),
        ('处理状态', {
            'fields': ['status', 'admin_remark', 'source'],
        }),
        ('时间记录', {
            'fields': ['created_at', 'updated_at'],
            'classes': ['collapse'],
        }),
    ]

    actions = ['export_as_csv', 'mark_as_completed', 'mark_as_confirmed']

    def masked_phone(self, obj):
        """列表页显示脱敏手机号，如 138****8000"""
        if obj.phone and len(obj.phone) >= 7:
            return obj.phone[:3] + '****' + obj.phone[-4:]
        return obj.phone or '-'
    masked_phone.short_description = '联系电话'

    @admin.action(description='📥 导出为 CSV')
    def export_as_csv(self, request, queryset):
        """导出选中的（或全部）预约记录为 CSV 文件"""
        # 如果用户没有勾选任何记录，则导出全部
        if not queryset.exists():
            queryset = CustomerConsultation.objects.all()

        response = HttpResponse(content_type='text/csv; charset=utf-8-sig')
        response['Content-Disposition'] = 'attachment; filename="客户预约咨询导出.csv"'
        # BOM 头确保 Excel 正确识别中文
        response.write('﻿')

        writer = csv.writer(response)
        writer.writerow(['客户姓名', '职务', '企业名称', '联系电话', '业务类型', '期望预约日期', '诉求简述', '紧急程度', '处理状态', '后台备注', '预约来源', '提交时间'])

        for obj in queryset:
            writer.writerow([
                obj.name,
                obj.position,
                obj.company_name,
                obj.phone,
                obj.get_case_category_display(),
                obj.appointment_date or '',
                obj.case_description,
                obj.get_urgency_level_display(),
                obj.get_status_display(),
                obj.admin_remark,
                obj.get_source_display(),
                obj.created_at.strftime('%Y-%m-%d %H:%M') if obj.created_at else '',
            ])

        messages.success(request, f'已导出 {queryset.count()} 条记录')
        return response

    @admin.action(description='✅ 批量标记为「已完成」')
    def mark_as_completed(self, request, queryset):
        updated = queryset.update(status='已完成')
        messages.success(request, f'已将 {updated} 条记录标记为已完成')

    @admin.action(description='📋 批量标记为「已确认」')
    def mark_as_confirmed(self, request, queryset):
        updated = queryset.update(status='已确认')
        messages.success(request, f'已将 {updated} 条记录标记为已确认')


@admin.register(RepresentativeCase)
class RepresentativeCaseAdmin(admin.ModelAdmin):
    list_display = ['title', 'amount', 'sort_order', 'is_active', 'created_at']
    list_display_links = ['title']
    list_editable = ['sort_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'role']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(ServiceClient)
class ServiceClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo_preview', 'sort_order', 'is_active', 'created_at']
    list_display_links = ['name']
    list_editable = ['sort_order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at', 'logo_preview']

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="max-height:40px; max-width:120px;" />', obj.logo.url)
        return '-'
    logo_preview.short_description = 'Logo预览'


@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'sort_order', 'is_active', 'created_at']
    list_display_links = ['name']
    list_editable = ['sort_order', 'is_active']
    list_filter = ['category', 'is_active']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']
