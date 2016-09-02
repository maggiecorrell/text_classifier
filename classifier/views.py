from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html')

def classifier(request):
    return render(request, 'classifier.html')

def category(request):
    return render(request, 'category.html')
