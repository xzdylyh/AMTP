#coding=utf-8

from models import case_interface_table

#select

class ModelClass(object):
    def __init__(self,tableObject):
        self.tableObject = getattr(tableObject,"objects")

    #获取table中所有数据，按参数分页
    '''

    '''
    def getDataAll(self,fpage):
        start_page =getattr(fpage,'start')
        end_page= getattr(fpage,'end')
        all_data = self.tableObject.all()[start_page:end_page]
        return all_data

    #根据id获取获取数据
    def getDataById(self,val_str):
        return self.tableObject.get(id=val_str)

    #根据id删除数据
    def delete_data(self,val_str):
        self.tableObject.filter(id=val_str).delete()


    #修改数据
    def modify_data(self,**kwargs):
        data_by_id = self.tableObject.get(id=kwargs.pop('id'))
        try:
            for key in kwargs.keys():

                #getattr(data_by_id,key)
                setattr(data_by_id,key,kwargs[key])
            data_by_id.save()
        except AttributeError as ex:
            print ex

    #insert Data
    def insert_data(self,**kwargs):
        self.tableObject.create(**kwargs)