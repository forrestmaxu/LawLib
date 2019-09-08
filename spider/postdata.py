import proxy
from urllib.parse import urlencode
# 北京审判
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


# 北京审判
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



fabao_data_law={
    "法律":{
        "Db": "chl", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA0101", 
        "clust_db": "chl", 
        "Search_Mode": "", 
        "range": "name", 
        "hidtrsWhere": "377EF8C056C62113E3510356CD866D062CD82F4BD0A1F26B", 
        "menu_item": "law", 
        "EncodingName": "", 
        "time": "0.33334365989508274"
        },
    "法律问题决定":{
        "Db": "chl", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA0102", 
        "clust_db": "chl", 
        "Search_Mode": "", 
        "range": "name", 
        "hidtrsWhere": "377EF8C056C62113E3510356CD866D060D05B97CB32201EC", 
        "menu_item": "law", 
        "EncodingName": "", 
        "time": "0.046276305657811045"
    },
    "法律解释":{
         "Db": "chl", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA0103", 
        "clust_db": "chl", 
        "Search_Mode": "", 
        "range": "name", 
        "hidtrsWhere": "377EF8C056C62113E3510356CD866D065FD156F00AA28A15", 
        "menu_item": "law", 
        "EncodingName": "", 
        "time": "0.5167059243587152"
    },
    "工作答复":{
        "Db": "chl", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA0104", 
        "clust_db": "chl", 
        "Search_Mode": "", 
        "range": "name", 
        "hidtrsWhere": "377EF8C056C62113E3510356CD866D062CD82F4BD0A1F26B", 
        "menu_item": "law", 
        "EncodingName": "", 
        "time": "0.9804563335289227"
    },
    "条约批准":{
        "Db": "chl", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA0107", 
        "clust_db": "chl", 
        "Search_Mode": "", 
        "range": "name", 
        "hidtrsWhere": "377EF8C056C62113E3510356CD866D06E05682AFC9526AD9", 
        "menu_item": "law", 
        "EncodingName": "", 
        "time": "0.3843120586614167"
    },
    "工作文件":{
        "Db": "chl", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXA0105", 
        "clust_db": "chl", 
        "Search_Mode": "", 
        "range": "name", 
        "hidtrsWhere": "377EF8C056C62113E3510356CD866D06E05682AFC9526AD9", 
        "menu_item": "law", 
        "EncodingName": "", 
        "time": "0.5422217594261634"
        }
  
    }
        
fabao_data_xingzheng={
    "indexpage":{
        "Db": "chl", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXC02", 
        "clust_db": "chl", 
        "Search_Mode": "accurate", 
        "range": "name", 
        "menu_item": "law", 
        "EncodingName": "", 
        "time": "0.7739078123024671"
    },
    "otherpage":{
        "range": "name", 
        "Search_Mode": "accurate", 
        "menu_item": "law", 
        "Db": "chl,protocol,lawexplanation,whitebook,workreport,introduction", 
        "hidtrsWhere": "377EF8C056C621134FB3B8C2F520A66751E70D74A6607102", 
        "": "", 
        "nomap": "", 
        "clusterwhere": "%25e6%2595%2588%25e5%258a%259b%25e7%25ba%25a7%25e5%2588%25ab%253dXC02", 
        "aim_page": "1", 
        "page_count": "246", 
        "clust_db": "chl", 
        "EncodingName": "", 
        "time": "0.7160332822583595"
    }
    
}

if __name__=="__main__":
    print(postdata["刑事"])
    # print(url)
