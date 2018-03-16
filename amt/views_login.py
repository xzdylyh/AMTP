# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

#自开发的包
from models import User
from decorator import login_limit
# Create your views here.

#登录页
def login_ajax(request):
    return render(request,"login.html")


#注销登录
@login_limit
def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/')

@csrf_exempt
def login_validation(request):
    uname = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=uname)
        if uname==user.username and password==user.password:
            request.session['username']=uname
            request.session.set_expiry(0) #session过期时间 0用户关闭浏览器，即失效
            return JsonResponse({'res':1}) #1验证成功
        else:
            return JsonResponse({'res':0}) #0验证失败
    except Exception as ex:
        return JsonResponse({'res':0}) #0验证失败

#重置密码页
@login_limit
def reset_secret(request):
    return render(request,'secret.html')

#重置密码
@csrf_exempt
@login_limit
def reset_password(request):
    new_pwd = request.POST.get('newpwd')
    uname = request.session['username']
    user = User.objects.get(username=uname)
    if new_pwd==user.password:
        return JsonResponse({'res':0})  #0代表新密码与原密码相同
    else:
        user.password=new_pwd
        user.save()
        return JsonResponse({'res':1}) #1密码修改成功
