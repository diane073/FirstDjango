from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db import transaction
from .models import ProductModel
from .form import ProductForm
from django.views.decorators.csrf import csrf_exempt


@login_required
@csrf_exempt
def product_register(request):
    # 상품 등록 view
    if request.method == 'GET':
        # 상품을 추가하는 페이지가 떠야함.
        product_form = ProductForm()
        return render(request, 'product/product_register.html', {'form': product_form})
        # 여기에 추가한 페이지를 render 해 줄 수 있도록하기

    elif request.method == 'POST':
        # 상품을 등록하는 POST요청
        # 자료를 등록해준다.

        product_form = ProductForm(request.POST)
        name = request.POST.get('name')
        if ProductModel.objects.filter(name=name).exists():
            message = "같은 이름의 상품이 존재합니다. 다시 등록해주세요"
            return render(request, 'product/product_register.html', {'form': product_form, 'error_message': message})
        elif product_form.is_valid():
            product_form.save()
            return redirect('/product_list')
        else:
            message = "유효하지 않은 값입니다. 다시 등록해야되지롱"
            return render(request, 'product/product_register.html', {'form': product_form, 'error_message': message})


@login_required
def product_list(request):
    # 등록 된 상품의 리스트를 볼 수 있는 GET(사용자가 보는,)
    if request.method == 'GET':
        all_product = ProductModel.objects.all()
        return render(request, 'product/product_list.html', {'products': all_product})
    else:
        return HttpResponse("등록한거 안보여줄거지롱")


@ login_required
@ transaction.atomic
def inbound_product(request):
    # 상품 입고 view
    # 입고 기록 생성
    # updated_at / stock을 추가

    # 입고 수량 조정

    if request.method == 'GET':
        selected_product = ProductModel.objects.filter(
            name={product_list.name})
        selected_product.values_list('name', 'price', 'stock')
        print(selected_product)
        return render(request, 'product/product_register.html')
    elif request.method == 'POST':

        # 입고 수량 조정
        # 입고 기록 생성
        # updated_at / stock을 추가

        return redirect('/product_list/')


@ login_required
def outbound_create(request, product_id):
    # 상품 출고 view
    # 출고 기록 생성

    # 재고 수량 조정
    pass


# view
@ login_required
def inventory(request):
    """
    inbound_create, outbound_create view에서 만들어진 데이터를 합산합니다.
    Django ORM을 통하여 총 수량, 가격등을 계산할 수 있습니다.
    """
    # 총 입고 수량, 가격 계산

    # 총 출고 수량, 가격 계산
    pass
