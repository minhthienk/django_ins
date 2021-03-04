from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("This is the homepage")