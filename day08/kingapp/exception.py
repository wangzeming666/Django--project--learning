from django.http import HttpResponse
#from django.utils.deprecation import MiddlewraeMixin

class MyException(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(request, response, exception):
        return HttpResponse("In Exception")
'''
class MyException(MiddlewareMixin):
    def process_exception(request, response, exception):
        return HttpResponse("In Exception")
'''
