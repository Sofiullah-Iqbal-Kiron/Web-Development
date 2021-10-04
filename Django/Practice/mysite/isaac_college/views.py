from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


# issac_college/
def index(request):
    template = 'isaac_college/index.html'
    return render(request, template)


# isaac_college/tutorials/
def tutorials(request):
    template = 'isaac_college/tutorials.html'
    return render(request, template)


# isaac_college/tutorials/html_form
def html_form(request):
    template = 'isaac_college/tutorials/html_form.html'
    context = {"form_elements": ["input: most used", "label", "select: drop-down menu list",
                                 "textarea", "button", "fieldset", "legend", "datalist", "output", "options", "optgroup"], "languages": ["C", "C++", "Java", "JavaScript", "Python"]}
    return render(request, template, context)
