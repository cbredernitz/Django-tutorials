# from django.template import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404

# Can do the following and get rid of lines 1, 2, & 4.
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def owner(request):
   return HttpResponse("Hello, world. Christopher Bredernitz / 70efdf2e is the polls index.")

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
