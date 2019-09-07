import requests
import urllib.request
from urllib.parse import urlencode
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import uuid
import sys
import re
from pymongo import MongoClient
import proxy
import random

url='http://www.pkulaw.cn/cluster_form.aspx?Db=chl&menu_item=law&EncodingName=&keyword=&range=name&'
def get_content(link):
    # headers = {
	#     "Accept-Language": "zh-CN,zh;q=0.8", 
	#     "Accept-Encoding": "gzip, deflate, sdch", 
	#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
	#     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36", 
	#     "Host": "www.pkulaw.cn", 
	#     "Cookie": "bdyh_record=1970324860086081%2C1970324860087844%2C1970324860087837%2C1970324860087907%2C1970324860085114%2C1970324860087657%2C1970324860087697%2C1970324860087631%2C1970324860087701%2C1970324860087851%2C1970324860086614%2C1970324860000764%2C1970324845231811%2C1970324860004991%2C1970324860002384%2C1970324845231794%2C1970324845231624%2C1970324860002207%2C1970324860046814%2C1970324860046704%2C; CheckIPAuto=0; CheckIPDate=2016-10-15 10:03:46; gm3jc5afyl35gm2yt55kc4m1isIPlogin=1; ASP.NET_SessionId=davttbjhikxhqyn1lj5alhsb; Hm_lvt_58c470ff9657d300e66c7f33590e53a8=1476497011,1476498348,1476498528,1476499578; Hm_lpvt_58c470ff9657d300e66c7f33590e53a8=1476499578; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1476497011,1476498348,1476498528,1476499578; Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1476499578; CookieId=gm3jc5afyl35gm2yt55kc4m1; FWinCookie=1", 
	#     "Upgrade-Insecure-Requests": "1", 
	#     "Proxy-Connection": "keep-alive"
	# }
    # html=requests.get(url,headers=headers).text
    # print(html)
    # f=open('content.html','w')
	# f.write('hh')
	pass

headers = {
	"Accept-Language": "zh-CN,zh;q=0.8", 
	"Accept-Encoding": "gzip, deflate, sdch", 
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", 
	"User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36", 
	"Host": "www.pkulaw.cn", 
	"Cookie": "bdyh_record=1970324860086081%2C1970324860087844%2C1970324860087837%2C1970324860087907%2C1970324860085114%2C1970324860087657%2C1970324860087697%2C1970324860087631%2C1970324860087701%2C1970324860087851%2C1970324860086614%2C1970324860000764%2C1970324845231811%2C1970324860004991%2C1970324860002384%2C1970324845231794%2C1970324845231624%2C1970324860002207%2C1970324860046814%2C1970324860046704%2C; CheckIPAuto=0; CheckIPDate=2016-10-15 10:03:46; gm3jc5afyl35gm2yt55kc4m1isIPlogin=1; ASP.NET_SessionId=davttbjhikxhqyn1lj5alhsb; Hm_lvt_58c470ff9657d300e66c7f33590e53a8=1476497011,1476498348,1476498528,1476499578; Hm_lpvt_58c470ff9657d300e66c7f33590e53a8=1476499578; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1476497011,1476498348,1476498528,1476499578; Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1476499578; CookieId=gm3jc5afyl35gm2yt55kc4m1; FWinCookie=1", 
	"Upgrade-Insecure-Requests": "1", 
	"Proxy-Connection": "keep-alive"
}


postdata={
	# 法律首页postda	
	"lawindex":{
		'Db': 'chl',
		'clusterwhere': '%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA01',
		'clust_db': 'chl',
		'range': 'name',
		'Search_Mode': '',
		'menu_item': 'law',
		'EncodingName': ''
	  	},
	"lawpage":{
		"range": "name",
		"check_hide_xljb": 1,
		"Db": "chl",
		"check_gaojijs": "1",
		"orderby": "%E5%8F%91%E5%B8%83%E6%97%A5%E6%9C%9F",
		"fdep_id":" ",
		"pdep_id":" ",
		"shixiao_id": "",
		"xiaoli_id": "",
		"sort_id": "",
		"hidtrsWhere": "377EF8C056C62113E3510356CD866D062CD82F4BD0A1F26B",
		"nomap": "",
		"clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA01",
		"aim_page": "1",
		"page_count": "69",
		"clust_db": "chl",
		"menu_item": "law",
		"EncodingName": ""
	}
}

SERVER_IP='127.0.0.1'
PORT=27017
DBNAME="splider"



# 抽取北大法宝url
def getUrl(params):
	i=random.randint(0, 24)
	urls=proxy.IPList_61()
	pro_item=urls[i]
	print(pro_item)
	proxies={ "http": "http://"+pro_item }

	baseurl="http://www.pkulaw.cn/doSearch.ashx"
	# 爬取首页url
	resp=requests.post(baseurl,headers=headers,data=params,proxies=proxies)
	fo=open('tmp.html','w',encoding='utf-8')
	fo.write(resp.text)



def parseContent():	
	fi=open('tmp.html','r',encoding='utf-8')
	# print(type(resp.text))
	reg=r'(.*) href=\"(fulltext_form.aspx\?Db=chl&Gid=.*)\" target=\"_blank\"'
	# line=" onclick=\"clickcss(this);\" href=\"fulltext_form.aspx?Db=chl&Gid=d8db5e659bc282b9bdfb&keyword=&EncodingName=&Search_Mode=&Search_IsTitle=0\" 中华人民共和国城市房地产管理法(2019修正)</a></td>"
	links=[]
	for line in fi.readlines():
		# print(line)
		matchobj=re.match(reg,line)
		if  matchobj:
			print(matchobj.group(2))
			# saveUrl(matchobj.group(2))
	
def saveUrl(url):
	conn = MongoClient(SERVER_IP, PORT)
	db = conn.splider  
	my_set = db.urlist
	reg=r'(.*Db=chi1&)(Gid=.*)&(.*)'
	matchobj=re.match(reg,url)
	if matchobj:
		id=matchobj.group(1)
	else:
		id=''
	doc={
		"id":id,
		"url":url,
		"isdownload":0,
		"source":"FB",
	}
	try:
		my_set.insert(doc)
		return True
	except:
		return False




def run():
	getUrl(postdata["lawindex"])
	parseContent()
	for i in range(1,69,10):
		postdata["lawpage"]["aim_page"]=i
		getUrl(postdata["lawpage"])
		parseContent()




if __name__ == "__main__":
    run()