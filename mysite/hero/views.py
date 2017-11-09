from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
    # database.objects.all() 返回一个数据列表
    herolist = HeroInfo.objects.all()
    context = {'herolist': herolist}
    tmp = loader.get_template('blog/index.html')
    response = tmp.render(context)
    return HttpResponse(response)

#def sayHai(request):
#    return HttpResponse('Hai!')

def detail(response, id):
    hero = HeroInfo.objects.get(pk=id)
    context = {'hero':hero}
    # 简写方式
    # return render(request,'blog/detail.html', context)
    tmp = loader.get_template('blog/detail.html')
    response = tmp.render(context)
    return HttpResponse(response)

