from django.urls import path
from .views import categories_views

urlpatterns = [
    path('categories/', categories_views.categories_list, name='categories_list'),
]
