from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("modelsProject")

def index(request):
     return render(request, 'modelsProject/index.html')

def base(request):
     return render(request, 'modelsProject/base.html')
