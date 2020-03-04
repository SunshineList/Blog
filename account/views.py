from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.urls import reverse

from .models import UserToken, Info
from rest_framework.views import APIView
from django.views.generic import View
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
from django.http import HttpResponse
import json
import time


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    usr = request.POST.get('username')
    pas = request.POST.get('password')
    make_password(pas)
    obj = Info.objects.filter(username=usr).first()
    if not obj:
        return render(request, 'error.html', {
            'msg': '用户不存在'
        })
    check_pas = Info.objects.filter(username=usr).values('password')[0]['password']
    cp = check_password(pas, check_pas)
    if not cp:
        return render(request, 'error.html', {
            'msg': '账号密码不匹配'
        })
    token = str(time.time()) + usr
    UserToken.objects.update_or_create(username=obj, defaults={'token': token})
    capt = request.POST.get("yzm")  # 用户提交的验证码
    key = request.POST.get("hash")  # 验证码答案
    if not jarge_captcha(capt, key):
        return render(request, 'login/login.html', {
            'code': 0,
            'msg': '验证码不正确'
        })
    return render(request, 'blog/index.html')


def register(request):
    if request.method == 'GET':
        return render(request, 'login/register.html')
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    passpwd = make_password(pwd)
    tel = request.POST.get('telphone')
    obj = Info.objects.filter(username=user)
    if not obj:
        user = Info.objects.create(username=user, password=passpwd, telphone=tel)
        if not user:
            return render(request, 'error.html', {'msg': '创建用户失败'})
    capt = request.POST.get("yzm")  # 用户提交的验证码
    key = request.POST.get("hash")  # 验证码答案
    if not jarge_captcha(capt, key):
        return render(request, 'login/register.html', {
            'code': 0,
            'msg': '验证码不正确'
        })
    return render(request, 'login/register.html', {'code': 1, 'msg': '注册成功'})


# 创建验证码
def captcha():
    ret = {}
    hashkey = CaptchaStore.generate_key()  # 验证码答案
    ret['hashkey'] = hashkey
    image_url = captcha_image_url(hashkey)  # 验证码地址
    ret['image_url'] = image_url
    # captcha = {'hashkey': hashkey, 'image_url': image_url}
    return JsonResponse(ret)


# 刷新验证码
def refresh_captcha(request):
    return HttpResponse(json.dumps(captcha()), content_type='application/json')


# 验证验证码
def jarge_captcha(captchaStr, captchaHashkey):
    if captchaStr and captchaHashkey:
        try:
            # 获取根据hashkey获取数据库中的response值
            get_captcha = CaptchaStore.objects.get(hashkey=captchaHashkey)
            if get_captcha.response == captchaStr.lower():  # 如果验证码匹配
                return True
        except:
            return False
    else:
        return False


class IndexView(View):
    def get(self, request):
        ret = {}
        hashkey = CaptchaStore.generate_key()  # 验证码答案
        ret['hashkey'] = hashkey
        image_url = captcha_image_url(hashkey)  # 验证码地址
        ret['image_url'] = image_url
        return JsonResponse(ret)
