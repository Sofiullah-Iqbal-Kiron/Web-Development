from django.http.response import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

# request.(method, path)

from django.http import HttpResponse
from .models import Question, Choice


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = 'polls/index.html'
    context = {'latest_question_list': latest_question_list}
    return render(request, template, context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    template = 'polls/detail.html'
    context = {'question': question}
    return render(request, template, context)


def results(requst, question_id):
    return HttpResponse(f"You're looking at results of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting at question {question_id}")
