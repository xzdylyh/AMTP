# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import case_interface_table,run_interface_table,User
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict

from pager import pageInfo
from modelHelp import ModelClass

# Create your views here.
def index(request):
    return render(request,"index.html")


#删除测试用例
@csrf_exempt
def case_delete_data(request):
    case_id = int(request.POST.get('caseid'))
    model_class = ModelClass(case_interface_table)
    model_class.delete_data(case_id)
    '''
    #分页代码
    '''
    curPage = int(request.GET.get('page','1'))
    allCount = case_interface_table.objects.all().count()
    fpage = pageInfo(curPage,allCount,5)

    return HttpResponse(request,"OK")

#修改测试用例
@csrf_exempt
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
    return HttpResponse(request,"ok")

#增加一条测试用例
@csrf_exempt
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
def select_case_data(request):
    caseid = request.POST.get('caseid')
    #数据操作类
    model_class = ModelClass(case_interface_table)
    data = case_interface_table.objects.get(id=caseid)
    data_dict = model_to_dict(data)
    return JsonResponse(data_dict)


#查询测试用例
def case_manage_iface(request):
    '''
    #分页代码
    '''
    curPage = int(request.GET.get('page','1'))
    allCount = case_interface_table.objects.all().count()
    fpage = pageInfo(curPage,allCount,5)
    fpageCount = fpage.pager()

    #数据操作类
    model_class = ModelClass(case_interface_table)
    posts = model_class.getDataAll(fpage) #获取所有数据，根据分页获取

    return render(request,"iface.html",{"posts":posts,"fpageCount":fpageCount,})



def  scenario_manage(request):
    pass

#登录页
def login_ajax(request):
    return render(request,"login.html")


@csrf_exempt
def login_validation(request):
    uname = request.POST.get('username')
    password = request.POST.get('password')

    try:
        user = User.objects.get(username=uname)
        if uname==user.username and password==user.password:
            request.session['username']=uname
            request.session.set_expiry(600) #session过期时间
            return render(request,'index.html')
    except Exception as ex:
        return JsonResponse({'res':'用记名或密码错误'})

#用户注册
def register(request):
    return render(request,"register.html")

@csrf_exempt
def user_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    email=request.POST.get('email')
    data ={
        username,
        password,
        email
    }
    try:
        User.objects.create(**data)
        return HttpResponseRedirect("/login_ajax/")
    except Exception as Ex:
        return JsonResponse({"res":"用户注册失败，请与管理员联系"})

#基础页
def base_page(request):
    return render(request,"base.html")




