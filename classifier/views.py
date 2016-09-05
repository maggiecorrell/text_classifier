from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from .models import Classifier, Category, Sample
import magic


def index(request):
    return render(request, 'index.html')


@login_required
def classifier(request, pk):
    pk = int(pk)
    user = request.user
    if user.pk != pk:
        return HttpResponseRedirect(reverse('classifier', kwargs={'pk': user.pk}))
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


@login_required
def category(request, classifier_id):
    classifier_id = int(classifier_id)
    user = request.user
    classifiers = Classifier.objects.filter(user=user)
    try:
        classifier = Classifier.objects.get(id=classifier_id)
    except:
        classifier = None
    if classifier not in classifiers:
        return HttpResponseRedirect(reverse('classifier', kwargs={'pk': user.pk}))
    if request.method == 'POST':
        category_name = request.POST.get('category-name', '')
        if category_name:
            category = Category(name=category_name, classifier=classifier)
            category.save()
    categories = Classifier.objects.get(id=classifier_id).category_set.all()
    context = {
        'classifier': classifier,
        'categories': categories
    }
    return render(request, 'category.html', context)


@login_required
def text_input(request, classifier_id):
    classifier_id = int(classifier_id)
    user = request.user
    classifiers = Classifier.objects.filter(user=user)
    try:
        classifier = Classifier.objects.get(id=classifier_id)
    except:
        classifier = None
    if classifier not in classifiers:
        return HttpResponseRedirect(reverse('classifier', kwargs={'pk': user.pk}))
    if request.method == 'POST':
        if request.FILES:
            fileform = UploadFileForm(request.POST, request.FILES)
            if fileform.is_valid():
                Sample.handle_uploaded_file(request.FILES['file'], classifier)
                return HttpResponseRedirect(reverse('classifier', kwargs={'pk': user.pk}))
        train = request.POST.get("train", "")
        if train:
            classifier.train()
            return HttpResponseRedirect(reverse('predict', kwargs={'classifier_id': classifier_id}))
        category_name = request.POST.get('category', "")
        sample_text = request.POST.get('sample-text', "")
        if category_name and sample_text:
            category = Category.objects.get(name=category_name)
            sample = Sample.objects.create(classifier=classifier, category=category, text=sample_text)
            sample.save()

    categories = Classifier.objects.get(id=classifier_id).category_set.all()
    fileform = UploadFileForm()
    context = {
        'classifier': classifier,
        'categories': categories,
        'fileform': fileform
    }
    return render(request, 'text_input.html', context)


@login_required
def predict(request, classifier_id):
    classifier_id = int(classifier_id)
    user = request.user
    classifiers = Classifier.objects.filter(user=user)
    prediction = None
    try:
        classifier = Classifier.objects.get(id=classifier_id)
    except:
        classifier = None
    if classifier not in classifiers:
        return HttpResponseRedirect(reverse('classifier', kwargs={'pk': user.pk}))
    if request.method == 'POST':
        predict_text = request.POST.get("predict-text", "")
        if predict_text:
            prediction = classifier.predict([predict_text])
            prediction = prediction[0]
    context = {
        'classifier': classifier,
        'prediction': prediction,
    }
    return render(request, 'predict.html', context)


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
            return HttpResponseRedirect(reverse('classifier', kwargs={'pk': user.pk}))
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
            return HttpResponseRedirect(reverse('classifier', kwargs={'pk': user.pk}))
        else:
            return render(request, 'registration/login.html')
    return render(request, 'registration/login.html')
