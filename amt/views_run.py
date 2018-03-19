# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from django.forms.models import model_to_dict

#自开发的包
from models import case_interface_table
from pager import pageInfo
from modelHelp import ModelClass
from decorator import login_limit
# Create your views here.

@login_limit
def run_test(request):
    return  render(request,"run_test.html")