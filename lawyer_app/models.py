from django.db import models


class CustomerConsultation(models.Model):
    """客户预约咨询信息表"""

    # 客户基本信息
    name = models.CharField("客户姓名", max_length=50)
    position = models.CharField("职务", max_length=50, blank=True, default='')
    company_name = models.CharField("企业名称", max_length=100, blank=True, default='')
    phone = models.CharField("联系电话", max_length=20)

    # 预约信息
    appointment_date = models.DateField("期望预约日期", blank=True, null=True)

    # 咨询内容
    case_category = models.CharField(
        "业务类型",
        max_length=50,
        choices=[
            # 非诉业务
            ("公司治理", "公司治理"),
            ("私募股权投融资", "私募股权投融资"),
            ("国资交易", "国资交易"),
            ("基金合规", "基金管理人募投管退全流程合规法律服务"),
            ("交易架构设计", "交易架构设计"),
            ("保险资管", "保险资管"),
            # 诉讼业务
            ("合同纠纷", "合同纠纷"),
            ("侵权纠纷", "侵权纠纷"),
            ("劳动争议", "劳动争议"),
            ("公司股权纠纷", "公司股权纠纷"),
            ("金融借款纠纷", "金融借款纠纷"),
            ("建设工程纠纷", "建设工程纠纷"),
            ("知识产权纠纷", "知识产权纠纷"),
            ("不正当竞争纠纷", "不正当竞争纠纷"),
            # 其他
            ("其他", "其他"),
        ],
        default="其他",
    )
    case_description = models.TextField("诉求简述", blank=True, default='')
    urgency_level = models.CharField(
        "紧急程度",
        max_length=10,
        choices=[
            ("一般", "一般"),
            ("紧急", "紧急"),
        ],
        default="一般",
    )

    # 处理状态（后台管理）
    status = models.CharField(
        "处理状态",
        max_length=20,
        choices=[
            ("待确认", "待确认"),
            ("已确认", "已确认"),
            ("已完成", "已完成"),
            ("已取消", "已取消"),
        ],
        default="待确认",
    )
    admin_remark = models.TextField("后台备注", blank=True, default='')

    # 来源与时间戳
    source = models.CharField(
        "预约来源",
        max_length=30,
        choices=[
            ("官网", "官网表单"),
            ("微信小程序", "微信小程序"),
            ("电话咨询", "电话咨询"),
            ("其他", "其他"),
        ],
        default="官网",
    )
    created_at = models.DateTimeField("提交时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        db_table = "customer_consultation"
        verbose_name = "客户预约咨询信息"
        verbose_name_plural = "客户预约咨询信息表"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.phone} ({self.appointment_date})"


class RepresentativeCase(models.Model):
    """代表案例表"""

    title = models.CharField("案例标题", max_length=100)
    role = models.CharField("律师角色", max_length=200)
    amount = models.CharField("金额标签", max_length=50, blank=True, default='')
    description = models.TextField("案例描述", blank=True, default='')
    sort_order = models.IntegerField("排序优先级", default=0, help_text="数字越小越靠前")
    is_active = models.BooleanField("是否展示", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        db_table = "representative_case"
        verbose_name = "代表案例"
        verbose_name_plural = "代表案例表"
        ordering = ['sort_order', '-created_at']

    def __str__(self):
        return self.title


class ServiceClient(models.Model):
    """服务客户Logo墙表"""

    name = models.CharField("客户名称", max_length=100)
    logo = models.ImageField("Logo图片", upload_to='logos/')
    sort_order = models.IntegerField("排序优先级", default=0, help_text="数字越小越靠前")
    is_active = models.BooleanField("是否展示", default=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("更新时间", auto_now=True)

    class Meta:
        db_table = "service_client"
        verbose_name = "服务客户"
        verbose_name_plural = "服务客户Logo墙表"
        ordering = ['sort_order', '-created_at']

    def __str__(self):
        return self.name
