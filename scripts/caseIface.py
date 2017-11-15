#*_*coding=utf-8*_*
from django.http import request
from models import case_interface_table,run_interface_table
from django.db import models

def I_Case(request):
    @staticmethod
    def add_case(request):
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
            '''
            dic = {'ICaseDescription':desc,
                   'ICaseURL':url,
            }
            case_interface_table.objects.create(**dic)


