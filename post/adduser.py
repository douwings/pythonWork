# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time

def postadduser():
    ssl._create_default_https_context = ssl._create_unverified_context

    sendsmspost_url = 'http://172.16.2.111:3999/user/roleEdit'
    sendsmsheaders = {
        # 'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    sendsmsform_data = {
        "roleId" : 22,
        "rolekey" : 'wingchange',
        "rolename" : '紫色的翼修改',
        "description" : '紫翼专属角色修改',
        'permissionId' : '1,2',
        # 'role' : '1,2',
    }

    # 构建post请求
    request = urllib.request.Request(url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    print(dict_json)
    # print(len(dict_json['list']))
    print("####################")
    return dict_json



if __name__ == '__main__':
    
    postadduser()
   