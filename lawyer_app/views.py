import logging

from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.throttling import AnonRateThrottle
from .models import RepresentativeCase, ServiceClient, PracticeArea
from .serializers import (
    ConsultationCreateSerializer,
    RepresentativeCaseSerializer,
    ServiceClientSerializer,
    PracticeAreaSerializer,
)

logger = logging.getLogger('lawyer_app')


class ConsultationThrottle(AnonRateThrottle):
    """预约咨询接口限流：同一 IP 每分钟最多5次，每天最多20次"""
    scope = 'consultation'


@api_view(['POST'])
@throttle_classes([ConsultationThrottle])
def create_consultation(request):
    """新增客户预约咨询记录 — POST /api/consultation/"""
    serializer = ConsultationCreateSerializer(data=request.data)
    if serializer.is_valid():
        obj = serializer.save()
        ip = request.META.get('REMOTE_ADDR', 'unknown')
        logger.info(f'预约提交成功 | IP={ip} | 姓名={obj.name} | 类型={obj.case_category}')
        return Response(
            {'message': '提交成功，我们将尽快与您联系'},
            status=status.HTTP_201_CREATED,
        )
    ip = request.META.get('REMOTE_ADDR', 'unknown')
    logger.warning(f'预约提交失败 | IP={ip} | 错误={serializer.errors}')
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_cases(request):
    """获取代表案例列表（仅展示 is_active=True）— GET /api/cases/"""
    cases = RepresentativeCase.objects.filter(is_active=True)
    serializer = RepresentativeCaseSerializer(cases, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_clients(request):
    """获取服务客户列表（仅展示 is_active=True）— GET /api/clients/"""
    clients = ServiceClient.objects.filter(is_active=True)
    serializer = ServiceClientSerializer(clients, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def list_practice_areas(request):
    """获取业务领域列表（仅展示 is_active=True，按分类分组）— GET /api/practice-areas/"""
    areas = PracticeArea.objects.filter(is_active=True)
    serializer = PracticeAreaSerializer(areas, many=True)

    # 按分类分组返回
    grouped = {}
    for item in serializer.data:
        cat = item['category']
        if cat not in grouped:
            grouped[cat] = {
                'category': cat,
                'category_label': item['category_label'],
                'items': [],
            }
        grouped[cat]['items'].append(item['name'])

    return Response(list(grouped.values()))
