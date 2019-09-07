import proxy
from urllib.parse import urlencode
postdata={
    "民事":{
        "ajlb" : "2",
        "st" : "1",
        "jbfyId" : "",
        "sxnflx" : "0",
        "zscq" : "",
        "cwslbmc" : "",
        "prompt" : "",
        "dsrName" : "",
        "ajmc" : "",
        "ay" : "",
        "ah" : "",
        "startCprq" : "",
        "endCprq" : ""
    },
    "刑事":{
        "ajlb" : "1",
        "st" : "1",
        "jbfyId" : " ",
        "sxnflx" : " 0",
        "zscq" : "",
        "cwslbmc" : "",
        "prompt" : "",
        "dsrName" : "",
        "ajmc" : "",
        "ay" : "",
        "ah" : "",
        "startCprq" : "",
        "endCprq" : ""
    },
    "行政":{
        "ajlb" : "6",
        "st" : " 1",
        "jbfyId" : "",
        "sxnflx" : "0",
        "zscq" : "",
        "cwslbmc" : "",
        "prompt" : "",
        "dsrName" : "",
        "ajmc" : "",
        "ay" : "",
        "ah" : "",
        "startCprq" : "",
        "endCprq" : ""
    },
    "赔偿":{
        "ajlb" : "7",
        "st" : " 1",
        "jbfyId" : "",
        "sxnflx" : "0",
        "zscq" : "",
        "cwslbmc" : "",
        "prompt" : "",
        "dsrName" : "",
        "ajmc" : "",
        "ay" : "",
        "ah" : "",
        "startCprq" : "",
        "endCprq" : ""
    },
    "知识产权":{
        "ajlb" : "",
        "st" : " 1",
        "jbfyId" : "",
        "sxnflx" : "0",
        "zscq" : "1",
        "cwslbmc" : "",
        "prompt" : "",
        "dsrName" : "",
        "ajmc" : "",
        "ay" : "",
        "ah" : "",
        "startCprq" : "",
        "endCprq" : ""
    }

}



def getTypePage(key):
    url=''
    if key=="民事":
        url="http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&prompt=&dsrName=&ajmc=&ajlb=2&jbfyId=&zscq=&ay=&ah=&cwslbmc=&startCprq=&endCprq=&page="
    elif key=="刑事":
        url="http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&prompt=&dsrName=&ajmc=&ajlb=1&jbfyId=&zscq=&ay=&ah=&cwslbmc=&startCprq=&endCprq=&page="
    elif key=="行政":
        url="http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&prompt=&dsrName=&ajmc=&ajlb=6&jbfyId=&zscq=&ay=&ah=&cwslbmc=&startCprq=&endCprq=&page="
    elif key=="执行":
        url="http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&prompt=&dsrName=&ajmc=&ajlb=8&jbfyId=&zscq=&ay=&ah=&cwslbmc=&startCprq=&endCprq=&page="
    elif key=="赔偿":
        url="http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&prompt=&dsrName=&ajmc=&ajlb=7&jbfyId=&zscq=&ay=&ah=&cwslbmc=&startCprq=&endCprq=&page="
    elif key=="知识产权":
        url="http://www.bjcourt.gov.cn/cpws/index.htm?st=1&q=&sxnflx=0&prompt=&dsrName=&ajmc=&ajlb=&jbfyId=&zscq=1&ay=&ah=&cwslbmc=&startCprq=&endCprq=&page="
    else:
        return ''
    return url




if __name__=="__main__":
    print(postdata["刑事"])
    # print(url)
