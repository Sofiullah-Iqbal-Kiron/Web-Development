import datetime

from django.shortcuts import render
from django.http import HttpResponse

from newyear.settings import TEMPLATES

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    template = 'isnewyear/index.html'
    context = {'newyear': now.year == 1 and now.month == 1}
    return render(request, template, context)
