from django.urls import path
from . import views

urlpatterns = [
    # 127.0.0.1:8000/products_list 와 views.py 폴더의 product 함수 연결
    path('product_register/', views.product_register, name='product_register'),
    path('product_list/', views.product_list, name='home'),
    path('', views.product_list, name='home'),
    # path('/inbound_product', views.inbound_create, name='inbound'),
]
