from django.urls import path, include
from .views import *


urlpatterns = [
    path('accounts/', include('allauth.urls')),

    path('introduce/', IntroduceViewset.as_view({'get': 'list', 'post': 'create'}),
         name='introduce_list'),
    path('introduce/<int:pk>/', IntroduceViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='introduce_detail'),

    path('category/', CategoryViewset.as_view({'get': 'list', 'post': 'create'}),
         name='category_list'),
    path('category/<int:pk>/', CategoryViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='category_detail'),

    path('product/', ProductViewset.as_view({'get': 'list', 'post': 'create'}),
         name='product_list'),
    path('product/<int:pk>/', ProductViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='product_detail'),

    path('great_product/', Great_ProductViewset.as_view({'get': 'list', 'post': 'create'}),
         name='great_product_list'),
    path('great_product/<int:pk>/', Great_ProductViewset.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='great_product_detail')
]