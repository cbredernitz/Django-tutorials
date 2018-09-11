from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Christopher Bredernitz / 9bf31c7f is the polls index.")
