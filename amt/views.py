# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import case_interface_table,run_interface_table
from django.shortcuts import render,render_to_response
from django.http import request
from django.db import models

# Create your views here.
def case_manage_page(request):
    return render(request,"casemanage.html")

def case_manage_iface(request):
    posts = case_interface_table.objects.all()
    editData = ""
    if request.method=='POST':
        caseid = request.POST.get('caseid')
        namebtn =request.POST.get("dbtn")
        confirmCase =request.POST.get("confirmCase")
        if namebtn == "删除":
            case_interface_table.objects.filter(id=caseid).delete()
        elif namebtn =="修改":
            editData = case_interface_table.objects.get(id=caseid)
        elif confirmCase != None:
            desc = request.POST.get('edesc')
            eurl = request.POST.get('eurl')
            method = request.POST.get('emethod')
            data = request.POST.get('edata')
            Exresult= request.POST.get('eresult')
            mcaseid = caseid = request.POST.get('mcaseid')
            MdfData = case_interface_table.objects.get(id=mcaseid)
            MdfData.ICaseURL = eurl
            MdfData.ICaseDescription = desc
            MdfData.ICaseMethod = method
            MdfData.ICase_Data = data
            MdfData.ICase_ExResult = Exresult
            MdfData.save()
        else: #插入
            desc = request.POST.get('idesc')
            url = request.POST.get('iurl')
            method = request.POST.get('imethod')
            itype = request.POST.get('itype')
            data = request.POST.get('idata')
            Exresult= request.POST.get('iresult')
            insertData = {
                "ICaseDescription":desc,
                "ICaseURL":url,
                "ICaseMethod":method,
                "ICase_Data":data,
                "ICase_ExResult":Exresult,
                "Icase_CreateUser":"yhleng",
                "IcaseFiled1":"",
                "IcaseFiled2":"",
                "IcaseFiled3":"",
                "IcaseFiled4":"",
                "IcaseFiled5":""
            }
            case_interface_table.objects.create(**insertData)
        posts = case_interface_table.objects.all()

    return render(request,"iface.html",{"posts":posts,"editPosts":editData,})


def  scenario_manage(request):
    pass
