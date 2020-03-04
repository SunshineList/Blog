from django.contrib import admin
from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url('^index/$', views.Blog_index, name='index'),
    url('^article/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url('^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url('^edit/action$', views.edit_action, name='edit_action'),
    url('^index/(?P<article_id>[0-9]+)$', views.del_page, name='del_page'),
]
