# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.
def upload(request):
    return render(request, 'upload.html')

def tryone(request):
    h = Hero()
    h.picture = request.File['picture']
    h.save()
    return HttpResponse("<h1>上传图片成功</h1>")

def heros(request):
    herolength = len(Hero.objects.all())
    herolist = []
    rangelist = [i for i in range(herolength)]
    for i in range(herolength):
        hero = Hero.objects.get(pk=i+1)
        # 第一次append创建了索引
        herolist.append({'name':hero.name})
        # 以后的添加需要使用索引i 直接赋值
        herolist[i]['id'] = i+1
        herolist[i]['picture'] = 'media/' + str(hero.picture)
    context = {'herolist': herolist, 'rangelist': rangelist}
    return render(request, 'app/heroshow.html', context)
#    herolength = len(Hero.objects.all())
#    herolist = {}
#    herolist['range'] = [str(i) for i in range(herolength)]
#    uselist = []
#    for i in range(herolength):
#        hero = Hero.objects.get(pk=int(i)+1)
#        use = []
#        use.append({'id': i+1})
#        use.append({'name': hero.name})
#        use.append({'picture': hero.picture})
        #herolist[str(i)]['id'] = int(i) + 1
        #herolist[str(i)]['name'] = hero.name
        #herolist[str(i)]['picture'] = hero.picture.url
#        uselist[i] = use
#    context = {'herolist': herolist, 'uselist':uselist}
#    return render(request, 'app/heroshow.html', context)

def heroList(request):
    # 取出数据库中所有英雄信息
    herolist = Hero.objects.all()
    # 这里不知道直接给一个<QuerySet>行不行，先试试
#    list = {}
 #   list['id'] = herolist[0]
  #  list['gender'] = herolist[1]
   # list['date'] = herolist[2]
   # list['user_num'] = herolist[3]
   # list['price'] = herolist[4]
   # list['desc'] = herolist[5]
    context = {'herolist': herolist}
    render(request, 'app/herolist.html', context)

def heroDesc(request, id):
    hero = Hero.objects.get(pk=id)
    herodesc = {}
    herodesc['name'] = hero.name
    herodesc['id'] = hero.id
    herodesc['desc'] = hero.desc
    herodesc['picture'] = 'media/' + str(hero.picture)
    # 判断英雄是否已经购买，如果已购买，返回一个可判定的值
    # 如果未购买，也返回一个可判定的值
    # 这个值在浏览器中判定是否添加购买按钮
    if request.session['user_id']:
        user_id = request.session['user_id']
        user_get = User_GET.objects.filter(user=user_id)
        looptimes = 0
        looplength = len(user_get)
        herohad = 0
        for getone in user_get:
            hero_id = getone.heros
            if hero_id == id:
                herohad = 1
                break
            else:
                looptimes += 1
        if looptimes == looplength:
            herohad = 0
        # 当用户没有拥有此英雄时
        # 查询购物车中是否加入过此商品，返回对应的herohad值
        if herohad == 0:
            user_shoppingcar = Shopping_cart.objects.filter(user=user_id)
            looptimes = 0
            looplength = len(user_shoppingcar)
            for goods in user_shoppingcar:
                if goods.heros == hero.id:
                    herohad = 1
                    break
                else:
                    looptimes += 1
                if looplength == looptimes:
                    herohad = 0
        # 这句话编辑器报错，但我觉得OK
        herodesc['herohad'] = herohad
    else:
        herohad = 0
        herodesc['herohad'] = herohad

    skins = Skin.objects.filter(hero=id)
    skinlist = []
    rangelist = [i for i in range(len(skins))]
    skinhad = 0
    for i in rangelist:
        # 取到id为i+1的皮肤对象sObj
        sObj = skins[i]
        skinlist.append({'id':sObj.id})
        skinlist[i]['name'] = sObj.name
        skinlist[i]['picture'] = 'media/' + str(sObj.picture)
        # 判定此皮肤当前用户是否拥有，如果未拥有，提供一个值供模板判定是否显示加入购物车按钮
        if request.session['user_id']:
            user_id = request.session['user_id']
            user_get = User_GET.objects.filter(user=user_id)
            looptimes = 0
            looplength = len(user_get)
            for getone in user_get:
                skin_id = getone.skins
                if skin_id == sObj.id:
                    skinhad = 1
                    break
                else:
                    looptimes += 1
            if looptimes == looplength:
                skinhad = 0
            # 查询购物车中是否加入过此商品，返回对应的herohad值
            # 如果用户已拥有，就不必要再查了
            if skinhad == 0:
                user_shoppingcar = Shopping_cart.objects.filter(user=user_id)
                for goods in user_shoppingcar:
                    if goods.skins == sObj.id:
                        skinhad = 1
                        break
                    else:
                        skinhad = 0
            skinlist[i]['skinhad'] = skinhad
        else:
            skinhad = 0
            skinlist[i]['skinhad'] = skinhad
    context = {'heroDesc': heroDesc, 'skinlist': skinlist, 'rangelist': rangelist}
    render(request, 'app/heroDesc.html', context)

def heroInsert(request):
    name = request.POST['name']
    gender = request.POST['gender']
    user_num = request.POST['user_num']
    h = Hero()
    h.name = name
    h.gender = gender
    h.user_num = user_num
    h.save()
    return HttpResponse("<h1>添加成功</h1>")

def heroSkin(request):
    id = request.POST['id']
    desc = request.POST['desc']
    picture = request.POST['picture']
    name = request.POST['name']
    hObj = Hero.objects.get(pk=id)
    sObj = Skin()
    sObj.hero = hObj
    sObj.desc = desc
    sObj.picture = picture
    sObj.save()
    return HttpResponse("<h1>添加成功</h1>")

def addtoshoppingcar(request, id, byetype):
    if request.session['user_id']:
        user_id = request.session['user_id']
        # 获取购物车对象
        shoppingcar = Shopping_cart()
        # 加入购买商品
        shoppingcar.user = user_id
        # byetype为商品购买类型，皮肤or英雄
        if byetype == 'hero':
            try:
                carObj = Shopping_cart.objects.get(hero=id)
                return HttpResponse("此商品已在购物车中")
            except Exception as e:
                shoppingcar.heros = id
                shoppingcar.save()
                return HttpResponse("添加购物车成功")
        elif byetype == 'skin':
            try:
                carObj = Shopping_cart.objects.get()
                return HttpResponse("此商品已在购物车中")
            except Exception as e:
                shoppingcar.skins = id
                shoppingcar.save()
                return HttpResponse("添加购物车成功")

def shoppingcar(request):
    try:
        user_id = request.session['user_id']
    except Exception as e:
        return redirect('app/login.html')
        pass
        pass
        pass
# 重定向需要确认无错
    goodslist = Shopping_cart.objects.filter(user=user_id)
    carlist = []
    i = -1
    for goods in goodslist:
        i += 1
        if goods.heros:
            heroObj = Hero.objects.get(pk=goods.heros)
            carlist.append({'goods_id': goods.heros})
            carlist[i]['name'] = heroObj.name
            carlist[i]['price'] = heroObj.price
        elif goods.skins:
            carlist.append({'goods': goods.skins})
            carlist[i]['name'] = heroObj.name
            carlist[i]['price'] = heroObj.price
    context = {'carlist': carlist}
    # 添加到字典中，提交给购物车模板
    return render(request, 'app/addtoshoppingcar.html', context)

# 登录视图
def login(request, msg):
    usename = request.POST['usename']
    password = request.POST['password']
    try:
        userObj = User.objects.get(user_name=usename)
        userinfo = {}
        userinfo['username'] = userObj.name
        userinfo["userlevel"] = userObj.level
        userinfo['userpicture'] = userObj.picture
        userinfo['userdesc'] = userObj.desc
        context = {'userinfo': userinfo}
        return render(request, 'app/heroDesc.html', context)
    except Exception as e:
        # 重定向返回错误信息
        # 如果登录错误信息
        # if msg:
        request.COOKIES['msg'] = '登录错误'
        return render(request, 'app/login.html')
        # return HttpResponseRedirect('app/login/?msg=error')



# 注册视图

#def re
#    gender = request.POST['gender']

# 个人账号信息页面
