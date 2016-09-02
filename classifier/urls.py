from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$', views.index, name='index')
    url(r'^login/', views.signin, name='signin'),
    url(r'^logout/', views.signout, name='signout'),
    url(r'^register/', views.register, name='register'),
]
