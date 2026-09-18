from django.contrib import admin
from django.utils.html import format_html
from .models import CustomerConsultation, RepresentativeCase, ServiceClient


@admin.register(CustomerConsultation)
class CustomerConsultationAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company_name', 'phone', 'appointment_date', 'case_category', 'urgency_level', 'status', 'created_at']
    list_filter = ['status', 'case_category', 'urgency_level']
    search_fields = ['name', 'phone', 'company_name']
    readonly_fields = ['created_at', 'updated_at']


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
