from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hat cho gio ra choi ma troi mua roi nhu ngay em khong thay nang")