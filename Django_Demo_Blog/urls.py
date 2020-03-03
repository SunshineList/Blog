"""Django_Demo_Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from account.views import refresh_captcha, IndexView
from django.conf import settings
from django.views import static

urlpatterns = [
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    url('admin/', admin.site.urls),
    url('blog/', include('blog.urls', namespace='blog')),
    url('captcha/', include('captcha.urls')),
    url('refresh_captcha/', refresh_captcha),
    url('yzm', IndexView.as_view()),
    url('info/', include('account.urls', namespace='info')),

]
