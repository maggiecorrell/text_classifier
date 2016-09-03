from django.conf.urls import url
from . import views
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register_user, name='register_user'),
    url(r'^login/$', views.login_user, name='login_user'),
    url(r'^logout/$', logout, {'next_page': '/login'}, name='logout'),
    url(r'^classifier/(?P<pk>[0-9]+)/$', views.classifier, name='classifier'),
    url(r'^category/(?P<classifier_id>[0-9]+)/$', views.category, name='category'),
    url(r'^text_input/(?P<classifier_id>[0-9]+)/$', views.text_input, name='text_input'),
    url(r'^predict/(?P<classifier_id>[0-9]+)/$', views.predict, name='predict')
    ]
