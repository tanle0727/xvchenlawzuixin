from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import RepresentativeCase, ServiceClient
from .serializers import (
    ConsultationCreateSerializer,
    RepresentativeCaseSerializer,
    ServiceClientSerializer,
)


@api_view(['POST'])
def create_consultation(request):
    """新增客户预约咨询记录 — POST /api/consultation/"""
    serializer = ConsultationCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': '提交成功，我们将尽快与您联系'},
            status=status.HTTP_201_CREATED,
        )
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
