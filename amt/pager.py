#coding=utf-8



#分页类
'''
--参数--
curpage:当前页
alldata:总共数据条数，以便记算分页
showCount：每页多少条数据
--descripts--

'''

class pageInfo(object):
    def __init__(self,curpage,alldata,showCount):
        self.curpage = int(curpage)
        self.alldata = int(alldata)
        self.showCount = int(showCount)
    @property
    def start(self):
        return (self.curpage -1) * self.showCount

    @property
    def end(self):
        return self.curpage * self.showCount


    def pager(self):

        #总共可以分多少页，如果有余数，说明最后一页不足5条，在商基础上加1.
        page,pct = divmod(self.alldata,self.showCount)
        if pct == 0:
            page =page
        else:
            page = page + 1

        #页数描述文本
        descPage ='<li><a>当前第<l>%d</l>页；共%d页，每页最多显示%d条数据，共%d条数据。</a></li>'%(self.curpage,page,5,self.alldata)
        #上一页
        if self.curpage >1:
            upPage ='<li><a href="/iface?page=%d">&laquo;</a></li>'%(self.curpage-1,)
        else:
            upPage ='<li><a href="#">&laquo;</a></li>'

        #将页数描述文本显示到最前边
        tmplist =[]
        tmplist.append(descPage)
        tmplist.append(upPage)


        #循环显示所有页数
        for i in range(page):
            if self.curpage -1 ==i:
                tmp ="<li class='active'><a href='/iface?page=%d'>%d</a></li>"%(self.curpage,self.curpage,)
            else:
                tmp = "<li><a href='/iface?page=%d'>%d</a></li>"%(i+1,i+1,)
            tmplist.append(tmp)

        #下一页
        if self.curpage +1 <= page:
            downPage ='<li><a href="/iface?page=%d">&raquo;</a></li>'%(self.curpage+1,)
        else:
            downPage ='<li><a href="#">&raquo;</a></li>'
        tmplist.append(downPage)

        return ''.join(tmplist)
