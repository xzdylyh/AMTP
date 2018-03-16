# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#用例表－接口
class case_interface_table(models.Model):
    ICaseNo = models.AutoField #用例编号
    ICaseDescription = models.CharField(max_length=150) #描述
    ICaseURL = models.CharField(max_length=150) #url
    ICaseMethod = models.CharField(max_length=150) #post or get
    ICase_Data = models.TextField() #data=dict{}
    ICase_ExResult = models.TextField() #ExResult
    Icase_CreateUser = models.CharField(max_length=150) #Case Create User
    IcaseFiled1 = models.CharField(max_length=500)
    IcaseFiled2 = models.CharField(max_length=500)
    IcaseFiled3 = models.CharField(max_length=500)
    IcaseFiled4 = models.CharField(max_length=500)
    IcaseFiled5 = models.CharField(max_length=500)

#接口执行表
class run_interface_table(models.Model):
    IRunNo = models.AutoField #执行编号
    ICaseNo = models.IntegerField #用例编号
    IRunDateTime = models.DateTimeField() #执行日期时间
    IRunResult = models.CharField(max_length=150) #执行结果
    IRunUser = models.CharField(max_length=150) #执行用户
    IRunReportName = models.CharField(max_length=150) #执行报告名称
    IRunFiled1 = models.CharField(max_length=500) #备用字段1
    IRunFiled2 = models.CharField(max_length=500)
    IRunFiled3 = models.CharField(max_length=500)
    IRunFiled4 = models.CharField(max_length=500)
    IRunFiled5 = models.CharField(max_length=500)

#用户表
class User(models.Model):
    user_id = models.AutoField #用户id
    username = models.CharField(max_length=50) #用户名称
    password = models.CharField(max_length=50) #密码
    create_time = models.DateTimeField("创建日期",auto_now_add=True) #第一次创建时间，之后更新model不会更改
    e_mail =models.CharField(max_length=150) #e-mail
    #status = models.ManyToManyField('User_Status',null=True)

'''
#用户状态表
class User_Status(models.Model):
    status = models.CharField(max_length=20)
'''