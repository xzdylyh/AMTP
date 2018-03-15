#coding=utf8
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from models import case_interface_table,run_interface_table,User
from pager import pageInfo
from modelHelp import ModelClass

#验证登录跳转页面
def login_limit(func):
    def war(request):
        try:
            request.session['username']
            ret = func(request)
            return ret
        except:
            return HttpResponseRedirect('/')
    return war

