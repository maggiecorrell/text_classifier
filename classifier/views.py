from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def classifier(request):
    return render(request, 'classifier.html')


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
            return HttpResponseRedirect(reverse('index'))
    else:
        uf = UserCreationForm(prefix='user')
    context = {'userform': uf}
    return render(request, 'registration/register.html', context)
