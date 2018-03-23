# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict
import json

#自开发的包
from models import case_interface_table,run_interface_table
from pager import pageInfo
from modelHelp import ModelClass
from decorator import login_limit
# Create your views here.

#删除测试用例
@csrf_exempt
@login_limit
def case_delete_data(request):
    case_id = int(request.POST.get('caseid'))
    model_class = ModelClass(case_interface_table)
    model_class.delete_data(case_id)

    #run table
    run_table = run_interface_table.objects.filter(ICaseNo=case_id)
    if run_table:
        run_table[0].delete()
    '''
    #分页代码
    '''
    curPage = int(request.GET.get('page','1'))
    allCount = case_interface_table.objects.all().count()
    fpage = pageInfo(curPage,allCount,5)

    return HttpResponse(request,"OK")

#修改测试用例
@csrf_exempt
@login_limit
def case_modify_data(request):
    exresult = request.POST.get('exresult')
    mcaseid  = request.POST.get('caseid')
    MdfData = case_interface_table.objects.get(id=mcaseid)
    MdfData.ICaseURL = request.POST.get('url')
    MdfData.ICaseDescription = request.POST.get('desc')
    MdfData.ICaseMethod = request.POST.get('method')
    MdfData.ICase_Data = request.POST.get('data')
    MdfData.ICase_ExResult = exresult
    MdfData.save()
    #run table
    run_table = run_interface_table.objects.filter(ICaseNo=mcaseid)
    if run_table:
        run_table.update(IRunFiled1=request.POST.get('desc'))

    return HttpResponse(request,"ok")

#增加一条测试用例

@csrf_exempt
@login_limit
def case_add_data(request):
    insertData = {
                "ICaseDescription":request.POST.get('idesc'),
                "ICaseURL":request.POST.get('iurl'),
                "ICaseMethod":request.POST.get('imethod'),
                "ICase_Data":request.POST.get('idata'),
                "ICase_ExResult":request.POST.get('iresult'),
                "Icase_CreateUser":"yhleng",
                "IcaseFiled1":"",
                "IcaseFiled2":"",
                "IcaseFiled3":"",
                "IcaseFiled4":"",
                "IcaseFiled5":""
            }

    case_interface_table.objects.create(**insertData)

    return HttpResponse(request,"ok")

#查询单条数据
@csrf_exempt
@login_limit
def select_case_data(request):
    caseid = request.POST.get('caseid')
    #数据操作类
    model_class = ModelClass(case_interface_table)
    data = case_interface_table.objects.get(id=caseid)
    data_dict = model_to_dict(data)
    return JsonResponse(data_dict)


#查询测试用例-带分页
@csrf_exempt
@login_limit
def case_manage_iface(request):
    '''
    #分页代码
    '''
    curPage = int(request.GET.get('page','1'))
    allCount = case_interface_table.objects.all().count()
    fpage = pageInfo(curPage,allCount,10)
    fpageCount = fpage.pager()


    #数据操作类
    model_class = ModelClass(case_interface_table)
    posts = model_class.getDataAll(fpage) #获取所有数据，根据分页获取

    return render(request,"iface.html",{"posts":posts,"fpageCount":fpageCount['page_info'],"fpageDesc":fpageCount['page_desc'],})

#查询所有case数据
@csrf_exempt
@login_limit
def select_all_ajax(request):
    datadict={}

    alldata = case_interface_table.objects.all()
    k=0
    for i in alldata:
        datadict[k]= model_to_dict(i)
        k+=1

    js = json.dumps(datadict)

    return HttpResponse(js,content_type="application/json")


