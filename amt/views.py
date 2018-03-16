# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


#自开发的包
from decorator import login_limit
# Create your views here.


@login_limit
def index(request):
    return render(request,"index.html")


@csrf_exempt
@login_limit
def  scenario_manage(request):
    pass



#系统设置
@login_limit
def system(request):
    return render(request,"system.html")

#基础页
def base_page(request):
    return render(request,"base.html")





