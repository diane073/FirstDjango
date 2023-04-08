from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponse


def signup(request):
    # 회원 가입 view
    # user/views.py
    if request.method == 'GET':  # GET 메서드로 요청이 들어 올 경우
        return render(request, 'user/signup.html')
    elif request.method == 'POST':  # POST 메서드로 요청이 들어 올 경우
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password2 = request.POST.get('password2', None)

        if password != password2:
            return render(request, '/sign-up/')
        else:
            exist_user = auth.get_user_model().objects.filter(username=username)
            if exist_user:
                # 사용자가 존재하기 때문에 사용자를 저장하지 않고 회원가입 페이지를 다시 띄움
                return render(request, 'user/signup.html')
            else:
                UserModel.objects.create(
                    username=username, password=password)
                return redirect('/sign-in')


@csrf_exempt
def signin(request):
    # 로그인 view
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        call_user = auth.authenticate(
            request, username=username, password=password)
        print(call_user)

        if call_user is None:
            return HttpResponse("잘못된 로그인 요청이지롱")

        auth.login(request, call_user)
        return redirect("/product_list")

    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:  # 로그인이 되어 있다면
            return redirect('/product_list')
        else:  # 로그인이 되어 있지 않다면
            return render(request, 'user/signin.html')


@login_required
def user_logout(request):
    auth.logout(request)
    return redirect('/sign-in')
