from django.shortcuts import render, redirect

from day08 import settings
from .models import *


def index(req):
    herolist = HeroInfo.objects.all()
    return render(req, 'kingapp/index.html', {'herolist': herolist})

def detail(req, id):
    s = 'abc'
    a = int(s) #会出现异常

    hero = HeroInfo.objects.get(pk=id)
    return render(req, 'kingapp/detail.html', {'hero':hero})

#处理文件上传
def upload(req):
    hid = req.POST['hid']
    hero = HeroInfo.objects.get(pk=hid)
    f1 = req.FILES['picture']
    #准备一个文件名，带路径:/static/media/heros/girl.jpeg
    hero.hpicture = 'heros/%s'%f1.name
    hero.save()
    fname = '%s/heros/%s' % (settings.MEDIA_ROOT, f1.name)

    with open(fname, 'wb') as pic:
        #不断从上传文件中读取数据，写入准备好的文件中
        for c in f1.chunks():
            pic.write(c)
    return redirect('/kingapp/detail/%s'%hid)





