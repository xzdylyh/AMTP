# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import request
# Create your views here.
def case_manage_page(request):
    return render(request,"casemanage.html")
