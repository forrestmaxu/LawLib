from selenium import webdriver

browser = webdriver.Chrome()
url="http://www.pkulaw.cn/cluster_form.aspx?Db=chl&menu_item=law&EncodingName=&clust_param=0/XA01&keyword=&range=name&"
browser.get(url)
f=open('tmp.html','w',encoding='utf-8')
f.write(browser.page_source)
# print(browser.page_source)
browser.close() 