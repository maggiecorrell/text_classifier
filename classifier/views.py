from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def classifier(request):
    return render(request, 'classifier.html')

def text_input(request):
    return render(request, 'text_input.html')
