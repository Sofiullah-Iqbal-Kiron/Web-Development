from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Welcome to our weblog. Making queries learning purpose.")