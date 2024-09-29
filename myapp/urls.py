from django.urls import path
from .views import categories_views,products_views

urlpatterns = [
    #categories
    path('categories/', categories_views.categories_list, name='categories_list'),
    path('categories/create/', categories_views.categories_create, name='categories_create'),
    path('categories/<int:pk>/', categories_views.categories_detail, name='categories_detail'),
    path('categories/<int:pk>/update/', categories_views.categories_update, name='categories_update'),
    path('categories/<int:pk>/delete/', categories_views.categories_delete, name='categories_delete'),

    #products
    path('products/', products_views.products_list, name='product_list'),
    path('products/create', products_views.products_create, name='products_create'),
    path('products/<int:pk>/', products_views.products_detail, name='products_detail'),
    path('products/<int:pk>/update/', products_views.products_update, name='products_update'),
    path('products/<int:pk>/delete/', products_views.products_delete, name='products_delete'),
]
