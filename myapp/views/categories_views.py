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
def categories_list(request):
    search_query = request.query_params.get('search', None)
    categories = Categories.objects.all().order_by("-id")

    if search_query:
        categories = categories.filter(Q(name_icontains=search_query))

    serializers = CategoriesSerializers(categories, many=True)
    return Response(serializers.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_create(request):
    serializers = CategoriesSerializers(data=request.data, context={'request': request})
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([AllowAny])
def categories_detail(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    serializers = CategoriesSerializers(category)
    return Response(serializers.data)

@api_view(['PUT'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_update(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    serializers = CategoriesSerializers(category, data=request.data, context={'request': request})
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_delete(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return Response({"detail": "Category deleted successfully."}, status=status.HTTP_200_OK)


## if serializers.is_valid: is to add data
## chnage to JSON type
## .. = folder  
## IsAuthenticated is login need || AllowAny not need login 
##api = responce || django = render
## status is to check http

## 404
## 400
## 500 and 500+