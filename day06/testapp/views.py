from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'testapp/index.html')

def detail(request, id):
    context = {"id":id}
    return render(request, 'testapp/detail.html', context)