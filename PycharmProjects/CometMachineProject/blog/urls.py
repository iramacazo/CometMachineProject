from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^logout/$', auth_views.logout, name='logout'),

    url(r'^$', views.index,  name='index'),

    url(r'^mainpage/$', views.mainpage, name='mainpage'),

]
