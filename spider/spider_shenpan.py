import requests
import urllib.request
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from pymongo import MongoClient
import uuid
import sys
import re,random
import logging
import js2py
import proxy
import postdata
from urllib.parse import urlencode
import time


# //mongodb database ip
SERVER_IP='127.0.0.1'
PORT=27017
logging.basicConfig(filename="test.log", filemode="w", format="%(asctime)s %(name)s:%(levelname)s:%(message)s", datefmt="%d-%M-%Y %H:%M:%S", level=logging.DEBUG)


# get url content,and extact the wenshu de link
def getUrl_links(doc):
    items=doc(".layer > .ul_news_long >.refushCpws >a").items()
    for it in items:
        print(it.attr('href'))
        saveUrl(it.attr('href'))




# save wenshu link to mongodb
def saveUrl(url):
    conn = MongoClient(SERVER_IP, PORT)
    db = conn.spider  
    my_set = db["urllist"]
    # print(baseurl)
    id=url.split('=')[1]
    # print(id)
    texturl="http://www.bjcourt.gov.cn"+url
    doc={
    	"id":id,
    	"url":texturl,
    	"isdownload":0,
    	"source":"BJSP",
    }
  
    result=my_set.find({"id":id})
    print("aa")

    if result.count()==0:
        my_set.insert(doc)
    else:
        print(result)
        print("the data exists")
    return True
   





#s使用代理访问 
def geturl(url):
    
    header,proxies=proxy.xundai()
    resp=requests.get(url,headers=header,proxies=proxies)
    # resp=requests.get(url)
    # print(resp.text)
    return resp

# 获取所有文书id
def getAllURL():
    conn = MongoClient(SERVER_IP, PORT)
    db = conn.spider  
    my_set = db.urllist
    result=my_set.find({"id":"100847665237"})
    for item in result:
        print(item["url"])
        parseContentByID(item["url"])
    # baseurl="http://www.bjcourt.gov.cn"
    # texturl=baseurl+"/cpws/paperView.htm?id="+id
    # print(texturl)

# 文书模型
# id
# title
# pubdate
# sllaw:      审理法院
# casetype:
# flag:
# texttype       文书总类
# caseNo:         案件号
# sldate         审理日期
# content:






def parseContentByID(texturl):
    try:
        resp=geturl(texturl)
        # f=open('text.html','w',encoding='utf-8')
        # f.write(resp.text)
        # print(type(resp.text))
        doc=pq(resp.text)
        obj=parseBody(doc,texturl)
        saveBody(obj)
        morelink=getRelLink(doc)
        nextRelPage(morelink)
        updateFlag(texturl)
    except:
        print(texturl+" is error ")

# 解析正文
def parseBody(doc,texturl):


    # title
    title=doc(".article_hd>.h3_22_m_blue").text()
    pubdate=doc(".article_hd>.p_date").text()
    #desc
    keys=doc(".fd-article-infor>table>tr>td>.fd-lable").items()
    values=doc(".fd-article-infor>table>tr>td>.fd-input").items()
    allvalues=[]
    for it in values:
        allvalues.append(it.attr('value'))
    print(allvalues)
    #body
    body=doc("#cc")
    # print(body)
    resulthtml=body.text()
    midresult1=resulthtml.replace('''document.getElementById("cc").innerHTML''',"tmpval")
    midresult=midresult1.replace(";","")
    # print(midresult)
    # result=execjs.eval(midresult)
    result = js2py.eval_js(midresult)
    # print(result)

    # f=open('d:/lawdata/'+title.text(),'w')
    content=pq(result)
    resitems=content(".MsoNormal").items()
    res=''
    for it in resitems:
        res+=it.text()
        # f.write(it.text()+"\n")
    # print(res)
    obj={
        "url":texturl,
        "title":title,
        "pubdate":pubdate,
        "sllaw":   allvalues[0],   
        "casetype": allvalues[1],
        "flag": allvalues[2],
        "texttype": allvalues[3] ,
        "caseNo": allvalues[4]     ,  
        "sldate": allvalues[5]   ,      
        "content":res
    }
    # print(obj)
    return obj

def getRelLink(doc):
    morelink=doc(".fd-list a:contains('更多')")
    print(morelink.attr('href'))
    # baseurl=""
    # alllinks=[]
    # for link in links:
    #     alllinks.append(link.attr('href'))
    # print(alllinks)
    return morelink.attr('href')

def parseRelLink(doc):
    # print(doc)
    links=doc(".refushCpws  a").items()
    print("########")
    print(links)
    for item in links:
        print('get the relation links')
        print(item.attr('href'))
        saveUrl(item.attr('href'))
    print('get the relation links is commplete on the page')
  

# 相关链接跳转
def nextRelPage(morelink):
    baseurl="http://www.bjcourt.gov.cn"
    url=baseurl+morelink
    # /cpws/index.htm?ay=劳动争议、人事争议
    key=morelink.split('=')[1]
    print(url)
    resp=geturl(url)
    # print(url)
    f=open('test.html','w',encoding='utf-8')
    
    doc=pq(resp.text)
    f.write(doc.text())
    # print(doc)
    flag=isCodePage(doc)
    # print('aa')
    if flag:
        print("the code page is happen")
    else:
        parseRelLink(doc)
    for i in range(2,20):
        newurl="http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&prompt=&dsrName=&ajmc=&ajlb=&jbfyId=&zscq=&ay="\
            +key+"&ah=&cwslbmc=&startCprq=&endCprq=&page="+str(i)
        resp=geturl(newurl)
        doc=pq(resp.text)
        flag=isCodePage(doc)
        if not flag:
            parseRelLink(doc)
        else:
            logging.error("the code page is occur")
        print("#########next page##############")
    

# save the url body content
def saveBody(doc):
    conn = MongoClient(SERVER_IP, PORT)
    db = conn.spider  
    my_set = db.bodycontent
    res=my_set.find({doc[url]})
    if res.count()==0:
        my_set.insert(doc)
    else:
        print("the url is exists")

# isdownload 1 :indict the url has downloaded;
def updateFlag(texturl):
    conn = MongoClient(SERVER_IP, PORT)
    db = conn.spider  
    my_set = db.urllist
    query={"url":texturl}
    value={"$set":{'isdownload':1}}

# 关键字搜索模块
def searchByKey(keyword):
    pass

# def creCollection(colName):
#     conn = MongoClient(SERVER_IP, PORT)
#     db = conn.splider 
#     my_set = db.colName
#     print("create collection "+colName+" success")
#     return True


def isCodePage(doc):
    # f=open('test.html','w',encoding='utf-8')
    # f.write(doc.text())
    # print(doc)
    code=doc(".authcode_flmc")
    # print(code)
    if code:
        print("valid code page")
        return True
    else:
        # print("the cotent is occu")
        return False

# spider the index page by the casetype
def postIndexBytype(type):
    data=postdata.postdata[type]
    print(data)
    # header,proxies=proxy.xundai()
    headers = {
        "Accept" : " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Accept-Encoding" : " gzip, deflate",
        "Accept-Language" : " en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Cache-Control" : " max-age=0",
        "Connection" : " keep-alive",
        "Content-Length" : " 94",
        "Content-Type" : " application/x-www-form-urlencoded",
        "Host" : " www.bjcourt.gov.cn",
        "If-None-Match" : "09ca584336a6d4b535f723fd653b05b10",
        "Origin" : " http",
        "Referer" : " http",
        "Upgrade-Insecure-Requests" : " 1",
        "User-Agent" : " Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        }
    baseurl="http://www.bjcourt.gov.cn/cpws/index.htm"
    resp=requests.post(baseurl,data=data,headers=headers)
    print(resp.text)
    if resp.status_code==200:
        print(resp.text)
        doc=pq(resp.text)
        return doc


# get the casetype next page
def nextPage(type): 
    
    for i in range(1,20):
        url=postdata.getTypePage(type)
        url=url+str(i)
        print(url)
        resp=geturl(url)
       
        # print(resp.text)
        doc=pq(resp.text)
        code=doc(".authcode_flmc")
        # f=open('code.hmlt','w',encoding='utf-8')
        # f.write(resp.text)

        if  code:
            print("the code ocuur")    
        else:
            getUrl_links(doc)
        time.sleep(10)

# start spider ,type parameter is case type
def run(type):
    
    nextPage(type)




if __name__=="__main__":
    # nextPage()
    # testfunc()
    # saveUrl("/cpws/paperView.htm?id=100889153269")
    # testurl="http://www.bjcourt.gov.cn/cpws/paperView.htm?id=100889916218"
    # parseContentByID(testurl)

    # full search
    # tilte=["民事","刑事","行政","执行", "赔偿","知识产权"]
    # for t in tilte:
    #     run(t)


    # spider the single link and extact the relation links;

    getAllURL()