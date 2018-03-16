# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#自开发的包
from models import User

# Create your views here.

#用户注册
def register(request):
    return render(request,"register.html")

@csrf_exempt
def user_register(request):
    uname = request.POST.get('username')
    password = request.POST.get('password')
    email=request.POST.get('email')
    try:
        user = User.objects.get(username=uname)
        tmp = "yes" #已被注册
    except Exception as Ex:
        tmp = "not"

    if tmp =='not':
        data ={
            'username':uname,
            'password':password,
            'e_mail':email
        }

        User.objects.create(**data)
        return JsonResponse({"res":1}) #1注册成功
    else:

        return JsonResponse({"res":0}) #0用户名已被注册
