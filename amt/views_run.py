# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict

#自开发的包
from models import run_interface_table,case_interface_table
from pager import pageInfo
from modelHelp import ModelClass
from decorator import login_limit
# Create your views here.

@login_limit
def run_test(request):
    posts = run_interface_table.objects.filter(IRunUser=request.session['username'])
    return  render(request,"run_test.html",{"posts":posts,})

@csrf_exempt
@login_limit
def insert_data(request):

    for i in range(int(request.POST.get('counter'))):
        try:
            caseid = request.POST.get('caseid%d'%(i))
            case_table =case_interface_table.objects.get(id=caseid)

            rundata = {'ICaseNo':caseid,'IRunUser':request.session['username']}

            if not run_interface_table.objects.filter(**rundata):
                indata = {
                    "ICaseNo":caseid,
                    "IRunResult":"",
                    "IRunUser":request.session['username'],
                    "IRunReportName":"",
                    "IRunFiled1":case_table.ICaseDescription,
                    "IRunFiled2":"",
                    "IRunFiled3":"",
                    "IRunFiled4":"",
                    "IRunFiled5":""
                }

                run_interface_table.objects.create(**indata)
            else:
                return JsonResponse({'res':0})
        except Exception as Ex:
            pass

    return JsonResponse({'res':1})

#删除执行表中数据
@csrf_exempt
@login_limit
def delete_run_data(request):
    for i in range(int(request.POST.get('counter'))):
        try:
            caseid = request.POST.get('caseid%d'%(i))
            run_interface_table.objects.filter(id=caseid).delete()
        except:
            pass

    return JsonResponse({'res':1})