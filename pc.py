#coding=utf-8
import requests
import os
import re
import time
import threading
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf8')
req_header={'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'UM_distinctid=1610846938256ad-04fa96f99a8432-78107f7f-1fa400-1610846938c6520; bdshare_firstime=1516262335301; jieqiVisitTime=jieqiArticlesearchTime%3D1516262362; jieqiVisitId=article_articleviews%3D123442%7C5663%7C1588; jieqiHistoryBooks=%5B%7B%22articleid%22%3A%221711%22%2C%22articlename%22%3A%22%u5927%u4E3B%u5BB0%22%2C%22chapterid%22%3A%22578806%22%2C%22chaptername%22%3A%22%u7AE0%u8282%u76EE%u5F55%20%u6211%u7684%u7B2C%u56DB%u672C%u4E66%uFF0C%u6B22%u8FCE%u5927%u5BB6%u3002%22%7D%5D; CNZZDATA1267947244=693318347-1516262299-%7C1516262299',
'Host':'www.96xs.com',
'Referer':'http://www.96xs.com/',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4399.400 QQBrowser/9.6.12856.400'
}
req_url_base = 'http://www.96xs.com/'  #小说主网址
req_url = req_url_base+'1711/'      #小说的列表
txt_section = '578808.html'         #小说章节页面

#请求当前章节页面  params为请求参数
r=requests.get(req_url+str(txt_section),params=req_header)
#soup转换
soup=BeautifulSoup(r.text,'html.parser')
#获取章节名称
section_name=soup.select('#wrapper #container .mainnav #directs .bookInfo .jieqi_title')[0]
#获取章节文本
section_text=soup.select('#wrapper #container .mainnav #directs .bookInfo #content')[0].text
#for ss in section_text.select('script'):   #删除无用项
#    ss.decompose()
#按照指定格式替换章节内容，运用正则表达式
#section_text=re.sub('\s+','\r\n\t',section_text.text).strip('\r\n')

print req_url
print '章节名称：'+str(section_name)
print '章节内容：\n'+str(section_text)

