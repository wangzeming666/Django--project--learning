# coding=utf-8
from django.shortcuts import render
from .models import *
from guoyuan import settings
from django.http import HttpResponse
# Create your views here.

def login_handle(request):
    username = request.POST['username']
    users = User.objects.all()
    if username in users:
        user = User.objects.get(username=username)
        if user.password == request.POST['password']:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session['user_gender'] = user.gender
            request.COOKIES['user_id'] = user.id
            request.COOKIES['user_name'] = user.username
            request.COOKIES['user_gender'] = user.gender
            render(request, 'index.html')
        else:
            context = {'msg': '登陆错误'}
            render(request, 'login.html', context)

def register_handler(request):
    username = request.POST['user_name']
    password = request.POST['pwd']
    email = request.POST['email']
    userObj = User()
    userObj.username = username
    userObj.password = password
    userObj.email = email
    userObj.save()
    return HttpResponse("<h1>注册成功</h1>")

def cart(request):
    if not request.session['user_id']:
        return render(request, 'login.html')
    user_id = request.session['user_id']
    cargoods = Shoppingcar.objects.filter(user=user_id)
    goodslist = []
    i = -1
    for carObj in cargoods:
        i += 1
        goods_id = carObj.goods_id
        goodsObj = Goods.objects.get(id=goods_id)
        name = goodsObj.title
        price = goodsObj.price
        picture = goodsObj.picture
        desc = goodsObj.desc
        goodslist.append({'name': name})
        goodslist[i]['price'] = price
        goodslist[i]['picture'] = picture
        goodslist[i]['desc'] = desc
    context = {'goodslist': goodslist}
    return render(request, 'cart.html', context)

def index():

