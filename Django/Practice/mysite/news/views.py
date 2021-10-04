from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter

# Create your views here.

# request.(method, path)


def index(request):
    return HttpResponse(f'News app: {request.path}')


def reporters(request):
    template = 'news/reporters.html'
    reporters = Reporter.objects.all()
    reporters_name = []
    for r in reporters:
        reporters_name.append(r.full_name)
    reporters_name.sort()
    context = {'reporters_name': reporters_name}
    return render(request, template, context)
