from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProductModel
from django.http import HttpResponse
from django.db import transaction

# Create your views here.


@login_required
def product_create(request):
    # 상품 등록 view
    if request.method == 'GET':
        # 상품이 추가된 페이지가 떠야함.
        return render(request, '/products')
        # 여기에 추가한 페이지를 render 해 줄 수 있도록하기

    elif request.method == 'POST':
        # 상품을 등록하는 POST요청
        # 자료를 등록해준다.
        product = ProductModel
        product.name = request.POST.get('productname', None)
        product.user = request.POST.get('username', None)
        product.description = request.POST.get('description', None)
        product.price = request.POST.get('price', None)
        product.size = request.POST.get('size', None)
        product.stock = request.POST.get('stock', None)

        if product.objects.filter(name=product.name).exists():
            return HttpResponse("같은 이름의 상품이 존재합니다. 다시 등록해주세요")
        else:
            product.save()
            return redirect('/product')


@login_required
def product_list(request):
    # 등록 된 상품의 리스트를 볼 수 있는 GET(사용자가 보는,)
    if request.method == '/product':
        all_product = ProductModel.objects.all()
        return render(request, 'home.html', {'products': all_product})
    else:
        return HttpResponse('유효한 요청이 아닙니다.')


@login_required
@transaction.atomic
def inbound_create(request):
    # 상품 입고 view
    # 입고 기록 생성

    # 입고 수량 조정
    pass
