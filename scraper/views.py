from django.http import HttpResponse
from django.shortcuts import render

def homepage(request): #when someone looks for this home page, it will send this request. Which url they are looking
    return HttpResponse("<h1>Homepage</h1>")

def eggs(request):
    return HttpResponse("<h1>Eggs are great</h1>")
