from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def func(Request):
    return HttpResponse("Hello World")
