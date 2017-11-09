from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def login(response):
    return HttpResponse('登陆成功')
