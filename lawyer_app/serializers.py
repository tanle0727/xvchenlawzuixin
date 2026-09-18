import re
from rest_framework import serializers
from .models import CustomerConsultation, RepresentativeCase, ServiceClient


# 合法的业务类型（与模型 choices 保持一致）
VALID_CATEGORIES = {choice[0] for choice in CustomerConsultation._meta.get_field('case_category').choices}


class ConsultationCreateSerializer(serializers.ModelSerializer):
    """客户预约咨询 — 前端提交专用序列化器"""

    class Meta:
        model = CustomerConsultation
        fields = [
            'name',             # 客户姓名
            'position',         # 职务
            'company_name',     # 企业名称
            'phone',            # 联系电话
            'case_category',    # 业务类型
            'appointment_date', # 期望预约日期
            'case_description', # 诉求简述
            'urgency_level',    # 紧急程度
        ]

    def validate_phone(self, value):
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('请输入正确的11位手机号')
        return value

    def validate_case_category(self, value):
        if value not in VALID_CATEGORIES:
            raise serializers.ValidationError(f'无效的业务类型: {value}')
        return value

    def create(self, validated_data):
        # 默认值
        validated_data.setdefault('status', '待确认')
        validated_data.setdefault('source', '官网')
        return super().create(validated_data)


class RepresentativeCaseSerializer(serializers.ModelSerializer):
    """代表案例 — 前端只读序列化器"""

    class Meta:
        model = RepresentativeCase
        fields = ['id', 'title', 'role', 'amount', 'description']


class ServiceClientSerializer(serializers.ModelSerializer):
    """服务客户 — 前端只读序列化器，logo 返回完整 URL"""

    logo = serializers.SerializerMethodField()

    class Meta:
        model = ServiceClient
        fields = ['id', 'name', 'logo']

    def get_logo(self, obj):
        if obj.logo:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.logo.url)
            return obj.logo.url
        return ''
