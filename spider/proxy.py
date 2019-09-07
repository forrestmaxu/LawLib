
from pyquery import PyQuery as pq
import requests
import urllib.request
import time

def IPList_61():
    urls=[]
    for q in [1,2]:
        url='http://www.66ip.cn/'+str(q)+'.html'
        doc=pq(url)
        
        if doc!=None:
            #print(html)
            iplist=doc('.containerbox table tr:gt(0)').items()
            for tr in iplist:
                ip=tr.find('td:nth-child(1)').text()
                port=tr.find('td:nth-child(2)').text()
                # print(ip,port)
                urls.append(ip+":"+port)
            # i=2
            # for ip in iplist:
            #     if i<=0:
            #         loader=''
            #         #print(ip)
            #         j=0
            #         for ipport in ip.find_all('td',limit=2):
            #             if j==0:
            #                 loader+=ipport.text.strip()+':'
            #             else:
            #                 loader+=ipport.text.strip()
            #             j=j+1
            #         print(loader)    
            # i=i-1
        time.sleep(1)
    print(len(urls))
    return urls

def getproxy():
    urls=["111.231.90.122:8888","39.135.24.11:80","111.231.90.122:8888","111.231.92.21:8888",
        "101.4.136.34:81","140.206.203.56:9999"
    ]
    return urls


import hashlib
def xundai():
   
    orderno = "ZF2019940269dIfWJF"
    secret = "27b1e75d4f7c4a5fa42e640dfffe22c1"

    ip = "forward.xdaili.cn"
    port = "80"

    ip_port = ip + ":" + port

    timestamp = str(int(time.time()))              
    string = ""
    string = "orderno=" + orderno + "," + "secret=" + secret + "," + "timestamp=" + timestamp

    # if is_python3:                          
    string = string.encode()

    md5_string = hashlib.md5(string).hexdigest()                
    sign = md5_string.upper()                             
    print(sign)
    auth = "sign=" + sign + "&" + "orderno=" + orderno + "&" + "timestamp=" + timestamp
    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    headers = {"Proxy-Authorization": auth, "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36"}
    return (headers,proxy)

if __name__ == '__main__':
    header,proxy=xundai()
    print(header)
    print(type(str(proxy)))
    code='hhh'
    # print(u+code)