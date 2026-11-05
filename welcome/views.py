from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django. Nice 2 meet u.")
def hello(request):
    return HttpResponse('<h1>hello</h1>')
def archive_view(request, year):
    return HttpResponse(f'你正在瀏覽 {year} 年的文章封存')