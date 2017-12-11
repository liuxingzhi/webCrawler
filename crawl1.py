# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:22:16 2017

@author: Pistachio
"""

import requests
from bs4 import BeautifulSoup 
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
#proxies = {
#    "http":"http://182.148.123.126",
#}
#port 8080
url = "https://bangumi.bilibili.com/jsonp/seasoninfo/6487.ver?callback=seasonListCallback&jsonp=jsonp&_=1512975796109"

def find_bilibili_links(url):
    response = requests.get(url,proxies=proxies, headers = headers,timeout = 0.5)
    text = response.text
    data_json = text.split("(")[1].split(")")[0]
    data = json.loads(data_json)
    episodes = data['result']['episodes']
    url_dic = {}
    for episode in episodes:
        url = episode['webplay_url']
        index = episode['index']
        url_dic[index] = url
    return url_dic



#response.status_code
    
url_ips = "http://www.kuaidaili.com/free/inha/"
def find_ips(url):
    response = requests.get(url, headers = headers,timeout = 10)
    text = response.text
    soup = BeautifulSoup(text,'html.parser')
    ips = soup.find_all("td",attrs={"data-title": "IP"})
    for ip in ips:
        proxy = {"http":"http://"+ip.get_text()}
#        print(type(ip.text))
#        print(ip.get_text())
#        print(type(ip.get_text()))
        try:
            response = requests.get("https://www.baidu.com/",proxies=proxy, headers = headers,timeout = 0.5)
        except Exception:
            continue
#        print(response.status_code)
        if response.status_code is 200:
            yield proxy
            
pro = find_ips(url_ips)
for p in find_ips(url_ips):
    print(p)
#print("===================")
#for p in find_ips(url_ips):
#    print(p)
#url_bilibili = "https://bangumi.bilibili.com/jsonp/seasoninfo/6487.ver?callback=seasonListCallback&jsonp=jsonp&_=1512975796109"
#for index,proxies in enumerate(find_ips(url_ips)):
#    try:
#        a = find_bilibili_links(url_bilibili)
#    except Exception:
#        continue
#    print(index)
#    print(a)
#    print(proxies)
#    break;