# -*- coding: utf-8 -*-

import requests
from requests import Session
import json

#请求发送模块
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
    def re_to_exre(self,result,ex_result,option=1):
        ret_result = {}
        retVal= ''
        if option==0: #字符串对比
            if str(result).strip()==str(ex_result).strip():
                retVal = 'passed'
            else:
                retVal = 'failed'
        elif option==1: #深度对比
            result =eval(result)
            ex_result = eval(ex_result)
            dict_ret = self.qc(result,ex_result)

        else:
            retVal = '其它比对功能还在开发中…………；option请输入0(字符串比对)或1(深度比对，字典核对)'


        ret_result['retVal']=retVal #比对方式0，反回结果
        ret_result['equal'] = dict_ret['equal'] #key值不同
        ret_result['key_exist'] = dict_ret['key_exist'] #key数量是否存在并相同

        return ret_result

    #
    def qc(self,result,ex_result):
        ret ={}
        equal = True #预期与结果，key值是相等的
        key_exist = True #预期中的key值在结果中是存在的

        if result.__len__()==ex_result.__len__() or result.__len__()<ex_result.__len__():
            iter_dict=ex_result
            iter_dict2 = result
        else:
            iter_dict = result
            iter_dict2 = ex_result

        for key in iter_dict:
            if iter_dict2.has_key(key): #判断结果里是否存在预期的key
                if str(iter_dict[key]).strip() == str(iter_dict2[key]).strip(): #比对，预期与结果value
                    pass
                else:
                    equal =False #此条用例，结果failed
            else:#预期结果与结果不同，预期中的key在结果中不存在
                key_exist = False

        ret['equal']=equal
        ret['key_exist']=key_exist

        return ret


if __name__=="__main__":

    result="{'username':'qcbin','password':'q1234561','abc':'123'}"
    ex_result ="{'username':'qcbin','password':'q1234561'}"

    RA = Result_Analyse()
    dict_ret = RA.re_to_exre(result,ex_result,option=1)
    print dict_ret