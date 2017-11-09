from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    herolist = HeroInfo.objects.all()
    context = {'herolist': herolist}
    return render(request, 'kingapp/index.html', context)

def index2(request):
    return render(request, 'kingapp/index2.html')

def bash(request):
    return render(request, 'kingapp/bash.html')