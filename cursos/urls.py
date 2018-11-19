from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    path('', views.profesor_list, name='profesor_list'),
    url(r'^profesor/nueva/$', views.profesor_nuevo, name='profesor_nuevo'),
]
