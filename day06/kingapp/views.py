from django.shortcuts import render, redirect
from .models import UserInfo
from hashlib import sha1

def registe(request):
    return render(request, 'kingapp/register.html')


def login(request):
    #如果用户已经登录,去index
    if 'user_id' in request.session:
        return redirect('/')
    #否则去登录
    else:
        return render(request, 'kingapp/login.html')


def registe_handle(request):
    #1. 获取用户输入的信息
    post = request.POST;
    name = post['user_name']
    pwd = post['password']
    #2. 构造UserInfo对象
    user = UserInfo()
    user.uname = name
    #2.1 处理密码（加密）
    pwd_jm = sha1(pwd.encode('utf-8')).hexdigest()
    print(pwd_jm)
    user.upwd = pwd_jm
    #3. 保存到数据库
    user.save()

    return redirect('/login/')


def login_handle(request):
    # 1. 获取用户输入的信息
    post = request.POST;
    name = post['user_name']
    pwd = post['password']
    pwd_jm = sha1(pwd.encode('utf-8')).hexdigest()
    # 2. 判断用户是否存在或密码是否正确
    list = UserInfo.objects.filter(uname=name)
    # 用户是存在的并且密码是正确的
    if len(list) == 1 and list[0].upwd == pwd_jm:
        # 将用户登录成功的状态记录下来
        user = list[0]
        request.session['user_id'] = user.id
        request.session['user_name'] = user.uname
        #当浏览器关闭时过期
        request.session.set_expiry(0)
        return redirect('/')
    else:
        return redirect('/login/')


def index(request):
    user_id = request.session['user_id']
    user = UserInfo.objects.get(pk=user_id)
    context = {'user':user, 'products':['AK47','DF41']}
    return render(request, 'kingapp/index.html', context)


def product(request, id):
# session中有一个key是"products"的列表
    session = request.session
    if 'products' in session:
        products = session['products']
        if id not in products:
            products.append(id)
    else:
        session['products'] = [id,]

    return render(request, 'kingapp/shoppingcart.html')


def testfor(request):
    #userlist = UserInfo.objects.exclude(uname__startswith='t')
    userlist = UserInfo.objects.filter(uname__startswith='d')
    context = {'userlist': userlist}
    return render(request, 'kingapp/testfor.html', context)






