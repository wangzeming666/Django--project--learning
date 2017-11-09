from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *

def index(req):
    herolist = HeroInfo.objects.all()
    context = {'herolist':herolist}
    return render(req, 'kingapp/index.html', context)

def index2(req):
    return render(req, 'kingapp/index2.html')


def usercenter(req):
    return render(req, 'kingapp/user_center.html')

def userinfo(req):
    return render(req, 'kingapp/user_info.html')

# 测试ＨＴＭＬ转义
def index3(req):
    context = {'t1': '<h1>Index3</h1>'}
    return render(req, 'kingapp/index3.html', context)

#测试ＣＳＲＦ攻击
def csrf1(req):
    return render(req, 'kingapp/csrf1.html')


def csrf2(req):
    uname = req.POST['uname']
    return render(req, 'kingapp/csrf2.html', {'uname': uname})

@csrf_exempt
def csrf3(req):
    uname = req.POST['uname']
    return render(req, 'kingapp/csrf2.html', {'uname': uname})


#测试验证码
def login(req):
    return render(req, 'kingapp/login.html')


def verifyCode(req):
    from PIL import Image, ImageDraw, ImageFont
    import random
    #1.创建画布
    width = 100
    height = 25
    bgColor = (random.randrange(50,100),random.randrange(50,100),0)
    image = Image.new('RGB', (width, height),bgColor)
    #2.创建画笔
    draw = ImageDraw.Draw(image)
    #3.创建字体对象
    font = ImageFont.truetype('FreeMonoBold',24)
    #4. 随机生成验证码字符串,并将字符画到画布
    text = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    code = '' # 用于保存生成后的验证码
    for i in range(4):
        tmp = text[random.randrange(0, len(text))]
        rcolor = (random.randrange(0,255),random.randrange(0,255),random.randrange(0,255))
        draw.text((i*25,0),tmp,rcolor,font)
        code += tmp
    #5. 将生成的验证码存储在session中
    req.session['code'] = code
    #6.将生成的图片转码成二进制
    from io import BytesIO
    buf = BytesIO()
    image.save(buf, 'png')
    return HttpResponse(buf.getvalue(), 'image/png')

def login_handle(req):
    code1 = req.POST['code']
    code2 = req.session['code']
    if code1 == code2 :
        return HttpResponse('验证通过')
    else:
        return redirect('/kingapp/login/')













