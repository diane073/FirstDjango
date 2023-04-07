from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/products 과 views.py 폴더의 product 함수 연결
    path('products/', views.product_create, name='products'),
    path('', views.product_list, name='sales_list')
    # path('/inbound_product', views.inbound_create, name='inbound'),
]
