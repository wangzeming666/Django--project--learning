from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserInfo
# Create your views here.

def index(request):
    response = HttpResponse("Hello")
    cookies = request.COOKIES
    if cookies.get('name'):
        response.write(cookies['name'])
    # response.set_cookie("name", "DanielGuo")
    return response

def login(request):
    if 'name' in request.COOKIES:
        return HttpResponseRedirect('/kingapp/index')
    return render(request, "kingapp/login.html")

def login_handle(request):
    name = request.POST['uname']
    pwd = request.POST['upwd']
    user = UserInfo.objects.get(uname=name)
    if user.upwd == pwd:
        redi = HttpResponseRedirect('/kingapp/index')
        redi.set_cookie('name', name)
        return redi
    else:
        return HttpResponse("登录失败")

def logup_handle(request):
    name = request.POST['uname']
    pwd = request.POST['upwd']
    user = UserInfo.objects.all()
    if name in user:
        redi = HttpResponseRedirect('/kingapp/logup_handle')
        return redi
    else:
        createU = UserInfo.objects.create(uname = name, upwd=pwd)
        createU.save()
        return HttpResponse('<h1>注册成功<h1>')

def register(request):
    name = request.POST['uname']
    pwd = request.POST['upwd']
    user = UserInfo.objects.all()
    if name in user:
        redi = HttpResponseRedirect('/kingapp/logup_handle')
        return redi
    else:
        createU = UserInfo.objects.create(uname=name, upwd=pwd)
        createU.save()
        return HttpResponse('<h1>注册成功<h1>')