import requests
import execjs
import re
import sys
# from sqliteTool import EasySqlite
from pyquery import PyQuery as pq

def getcontent_js(url):
        # f=open(filename,'w')
    content=pq(url)
    title=content(".article_hd>.h3_22_m_blue")
    f=open('d:/lawdata/'+title.text(),'w')
    item=content("#cc")
    # for it in items:
    #     jstext=it.text()
    
    resulthtml=item.text()
    # f.write(resulthtml)
    midresult1=resulthtml.replace('''document.getElementById("cc").innerHTML''',"tmpval")
    midresult=midresult1.replace(";","")
    result=execjs.eval(midresult)
    # f.write(result)
    
    content=pq(result)
    resitems=content(".MsoNormal").items()
    for it in resitems:
        # print(it.text())
        f.write(it.text()+"\n")

if __name__ == "__main__":
    url='http://www.bjcourt.gov.cn/cpws/paperView.htm?id=100850257069&n=1'