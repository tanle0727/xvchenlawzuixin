import re
from datetime import date
from rest_framework import serializers
from .models import CustomerConsultation, RepresentativeCase, ServiceClient, PracticeArea


# 合法的业务类型（与模型 choices 保持一致）
VALID_CATEGORIES = {choice[0] for choice in CustomerConsultation._meta.get_field('case_category').choices}


class ConsultationCreateSerializer(serializers.ModelSerializer):
    """客户预约咨询 — 前端提交专用序列化器"""

    # Honeypot 隐藏字段：正常用户看不到不会填，机器人会自动填入
    website_url = serializers.CharField(required=False, allow_blank=True, write_only=True)

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
            'website_url',      # honeypot 防机器人
        ]

    def validate_website_url(self, value):
        """Honeypot：如果此字段被填写，说明是机器人提交"""
        if value:
            raise serializers.ValidationError('检测到异常提交')
        return value

    def validate_name(self, value):
        if len(value) > 15:
            raise serializers.ValidationError('姓名不能超过15个字')
        return value.strip()

    def validate_position(self, value):
        if value and len(value) > 15:
            raise serializers.ValidationError('职务不能超过15个字')
        return value.strip() if value else value

    def validate_phone(self, value):
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('请输入正确的11位手机号')
        return value

    def validate_company_name(self, value):
        if value and len(value) > 30:
            raise serializers.ValidationError('公司名称不能超过30个字')
        return value.strip() if value else value

    def validate_case_description(self, value):
        if value and len(value) > 500:
            raise serializers.ValidationError('案情描述不能超过500个字')
        return value.strip() if value else value

    def validate_case_category(self, value):
        if value not in VALID_CATEGORIES:
            raise serializers.ValidationError(f'无效的业务类型: {value}')
        return value

    def validate_appointment_date(self, value):
        """拒绝过去的日期"""
        if value and value < date.today():
            raise serializers.ValidationError('预约日期不能早于今天')
        return value

    def create(self, validated_data):
        # 移除 honeypot 字段，不存入数据库
        validated_data.pop('website_url', None)
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


class PracticeAreaSerializer(serializers.ModelSerializer):
    """业务领域 — 前端只读序列化器"""

    category_label = serializers.CharField(source='get_category_display', read_only=True)

    class Meta:
        model = PracticeArea
        fields = ['id', 'name', 'category', 'category_label']
