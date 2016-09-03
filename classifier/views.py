from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Classifier


def index(request):
    return render(request, 'index.html')


@login_required
def classifier(request):
    user = request.user
    if request.method == 'POST':
        classifier_name = request.POST.get('classifier-name', '')
        if classifier_name:
            classifier = Classifier(name=classifier_name, user=user)
            classifier.save()
    classifiers = Classifier.objects.filter(user=user)
    context = {
        'classifiers': classifiers
    }
    return render(request, 'classifier.html', context)


def text_input(request):
    return render(request, 'text_input.html')


def register_user(request):
    if request.method == 'POST':
        uf = UserCreationForm(request.POST, prefix='user')
        if uf.is_valid():
            user = uf.save(commit=False)
            user.save()
            user = authenticate(username=uf.cleaned_data['username'],
                                password=uf.cleaned_data['password1'],
                                )
            login(request, user)
            return HttpResponseRedirect(reverse('classifier'))
    else:
        uf = UserCreationForm(prefix='user')
    context = {'userform': uf}
    return render(request, 'registration/register.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('classifier'))
        else:
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')
