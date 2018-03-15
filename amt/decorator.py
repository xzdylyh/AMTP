#coding=utf8

from django.shortcuts import render,render_to_response,HttpResponseRedirect

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

