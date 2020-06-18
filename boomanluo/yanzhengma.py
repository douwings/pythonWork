# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time


def postsendsms(userphone):
    ssl._create_default_https_context = ssl._create_unverified_context

    sendsmspost_url = 'https://yy.cnns.net/api/sendsmsverify'

    t = time.time()
    sendsmsheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    sendsmsform_data = {
        'telno': userphone,
    }

    # 构建post请求
    request = urllib.request.Request(url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    print(dict_json)
    if dict_json['message'] == "验证码已发送。":
        return True
    else:
        return False




if __name__ == '__main__':
    # userphone = input("请输入电话：")
    userphone = 15173512106
    # userphone = 15374099873
    num = 1
    # for num in range(3):
    while True:
        # username = 'wing1020'
        print("第%s次发送"%(num))
        num += 1 
        result = postsendsms(userphone)
        if(result == False):
            break