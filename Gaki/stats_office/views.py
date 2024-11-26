from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'Gaki\index.html')

def sells(request):
    return render(request, 'Gaki\index.html')
