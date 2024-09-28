from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_list_or_404
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

## .. = folder  
## IsAuthenticated is login need || AllowAny not need login 
##api = responce || django = render