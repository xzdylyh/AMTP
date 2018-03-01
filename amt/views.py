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

    curPage = int(request.GET.get('page','1'))
    allPage = case_interface_table.objects.all().count()
    fpage = pageInfo(curPage,allPage)
    fpageCount = fpage.pager()

    posts = case_interface_table.objects.all()[fpage.start:fpage.end]
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
        posts = case_interface_table.objects.all()[fpage.start:fpage.end]

    return render(request,"iface.html",{"posts":posts,"editPosts":editData,"fpageCount":fpageCount,})


def  scenario_manage(request):
    pass


def login_ajax(request):
    return render(request,"login.html")


class pageInfo(object):
    def __init__(self,curpage,allpage):
        self.curpage = int(curpage)
        self.allpage = allpage

    @property
    def start(self):
        return (self.curpage -1) * 5

    @property
    def end(self):
        return self.curpage * 5


    def pager(self):

        page,pct = divmod(self.allpage,5) #总共可以分多少页
        if pct == 0:
            page =page
        else:
            page = page + 1

        tmplist =[]
        tmp=''

        for i in range(page):
            if self.curpage !=i:
                tmp += "<li><a href='/iface?page=%d'>%d</a></li>"%(i+1,i+1,)

            else:
                tmp ="<li class='active'><a href='/iface?page=%d'>%d</a></li>"%(i+1,i+1,)
            tmplist.append(tmp)
        return ''.join(tmplist)