# -*- coding: utf-8 -*-

import requests
from requests import Session
import json

#
class Interface(object):
    def __init__(self,url,data_dict):
        self.session = Session()
        self.url = url
        self.data_dict = data_dict

    #post发送数据
    @property
    def send_post_request(self):
        res = self.session.post(self.url,self.data_dict)
        return json.dumps(res.text)

    #get
    @property
    def send_get_request(self):
        res = self.session.get(self.url,self.data_dict)
        return json.dumps(res.text)


#结果比对
class Result_Analyse(object):
    def __init__(self):
        pass

    #args:0字符串对比，1深度对比，字典每一项对比。
    @staticmethod
    def re_to_exre(result,ex_result,option=0):

        if option==0: #字符串对比
            if str(result).strip()==str(ex_result).strip():
                retVal = 'passed'
            else:
                retVal = 'failed'
        elif option==1: #深度对比
            result =eval(result)
            ex_result = eval(ex_result)
        else:
            retVal = '其它比对功能还在开发中…………；option请输入0(字符串比对)或1(深度比对，字典核对)'
