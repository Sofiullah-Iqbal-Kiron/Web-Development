from django.shortcuts import render, HttpResponse
from .models import Student

# Create your views here.


def index(request):
    size = Student.objects.count()
    # Sort those students according to the first_name.
    students = Student.objects.order_by('first_name')[:size]
    template = 'Info/index.html'
    context = {'students': students, 'num_of_students': size}
    return render(request, template, context)
