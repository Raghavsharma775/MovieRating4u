from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'movie/index.html')

def about(request):
    return render(request,'movie/index.html')

def contact(request):
    return render(request,'movie/index.html')

def actors(request):
    return render(request,'movie/index.html')

def bollywood(request):
    return render(request,'movie/index.html')

def hollywood(request):
    return render(request,'movie/index.html')


def movieview(request):
    return render(request,'movie/index.html')


def search(request):
    return render(request,'movie/index.html')
