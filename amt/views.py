# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import case_interface_table,run_interface_table
from django.shortcuts import render,render_to_response
from django.http import request
# Create your views here.
def case_manage_page(request):
    return render(request,"casemanage.html")

def case_manage_iface(request):
    posts = case_interface_table.objects.all()
    if request.method=='POST':
        desc = request.POST.get('idesc')
        url = request.POST.get('iurl')
        '''
        增
        models.UserInfo.objects.create(user='yangmv',pwd='123456')
        或者
        obj = models.UserInfo(user='yangmv',pwd='123456')
        obj.save()
        或者
        dic = {'user':'yangmv','pwd':'123456'}
        models.UserInfo.objects.create(**dic)
        '''
    return render(request,"iface.html",{"posts":posts,})