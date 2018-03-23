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
from execute import Interface
from execute import Result_Analyse
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
            run_interface_table.objects.filter(ICaseNo=caseid).delete()
        except:
            pass

    return JsonResponse({'res':1})


#执行测试－－暂未加多线程或协程
@csrf_exempt
@login_limit
def execute_test(request):

    for i in range(int(request.POST.get('counter'))):
        try:
            case_id = request.POST.get('caseid%d'%(i))
            case_table = case_interface_table.objects.get(id=case_id)
            ######
            data = case_table.ICase_Data
            url = case_table.ICaseURL
            method = int(case_table.ICaseMethod)
            ex_result = case_table.ICase_ExResult
            ######
            it = Interface(url,eval(data))
            if method==0:
                res = it.send_post_request #响应数据
                RA =Result_Analyse()
                ret_dict = RA.re_to_exre(res,ex_result,option=1)
                run_table = run_interface_table.objects.filter(ICaseNo=case_id)
                if ret_dict['key_exist']==True and ret_dict['equal']==True:

                    run_table.update(IRunResult='Passed')

                    return JsonResponse({'res':1})
                else:
                    run_table.update(IRunResult='Failed')
                    return JsonResponse({'res':0})

            else:
                res = it.send_get_request
                RA =Result_Analyse()
                ret_dict = RA.re_to_exre(res,ex_result,option=1)
                if ret_dict['key_exist']==True and ret_dict['equal']==True:
                    return JsonResponse({'res':1})
                else:
                    return JsonResponse({'res':0})
        except:
            pass

    #return JsonResponse({'res':0})