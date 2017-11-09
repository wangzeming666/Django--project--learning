from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from django.template import loader
# from .models import *

def index(request):
    response = HttpResponse("hello")
    cookies = request.COOKIES
    if cookies.has_key('name'):
        response.write(cookies['name'])
    return response
