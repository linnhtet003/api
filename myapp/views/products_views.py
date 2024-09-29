from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.db.models import Q
from ..models import *
from ..serializers import *
from django.http import JsonResponse

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def products_list(request):
    search_query = request.query_params.get('search', None)
    products = Product.objects.all().order_by("-id")

    if search_query:
        products = products.filter(Q(name_icontains=search_query))

    serializers = ProductSerializers(products, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def products_create(request):
    serializers = ProductSerializers(data=request.data, context={'request': request})
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def products_detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    serializers = ProductSerializers(products)
    return Response(serializers.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def products_update(request, pk):
    products = get_object_or_404(Product, pk=pk)
    serializers = ProductSerializers(products, data=request.data, context={'request': request})
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def products_delete(request, pk):
    products = get_object_or_404(Product, pk=pk)
    products.delete()
    return Response({"detail": "Category deleted successfully."}, status=status.HTTP_200_OK)

