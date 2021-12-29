from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

# Some sort of nonsense names that are useful as a string for testing purpose.
tasks = ["foo", "bar", "baaz"]


def index(request):
    template = "tasks/index.html"
    context = {'tasks': tasks}
    return render(request, template, context)


def add(request):
    template = 'tasks/add.html'
    return render(request, template)
