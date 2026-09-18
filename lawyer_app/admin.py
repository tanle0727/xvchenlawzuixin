from django.contrib import admin
from django.utils.html import format_html
from .models import CustomerConsultation, RepresentativeCase, ServiceClient, PracticeArea


@admin.register(CustomerConsultation)
class CustomerConsultationAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company_name', 'masked_phone', 'appointment_date', 'case_category', 'urgency_level', 'status', 'created_at']
    list_filter = ['status', 'case_category', 'urgency_level']
    search_fields = ['name', 'phone', 'company_name']
    readonly_fields = ['created_at', 'updated_at']

    def masked_phone(self, obj):
        """列表页显示脱敏手机号，如 138****8000"""
        if obj.phone and len(obj.phone) >= 7:
            return obj.phone[:3] + '****' + obj.phone[-4:]
        return obj.phone or '-'
    masked_phone.short_description = '联系电话'


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
