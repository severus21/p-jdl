from django.urls import re_path

from . import views

app_name = 'jdl_web'

urlpatterns = [
    re_path(r'^$', views.index, name='index'), 
    re_path(r'^contact$', views.contact, name='contact'), 
    re_path(r'^informations$', views.informations, name='informations'), 
    re_path(r'^methode$', views.method, name='method'), 
    re_path(r'^carte$', views.map, name='map'), 
    re_path(r'^remerciements$', views.thanks, name='thanks'), 
]
