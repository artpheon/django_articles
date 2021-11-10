from django.http import HttpResponse

def index(request):
    return HttpResponse('Articles Page')

def test(request):
    return HttpResponse('Test Page')
