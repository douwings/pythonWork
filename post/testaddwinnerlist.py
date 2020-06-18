# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time

def testtoken() : 
    sendsmspost_url = 'http://172.16.2.111:3999/version/versionUpdate'
    # sendsmspost_url = 'http://172.16.2.111:3999/product/productUpdate'
    # sendsmspost_url = 'http://172.16.2.111:3999/noticeMail/update'
    # sendsmspost_url = 'http://172.16.2.111:3999/product/productParamsUpdate'
    sendsmsheaders = {
        # 'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    sendsmsform_data = {
        # 'id' : 7,
        'version' : 'ios259',
        'product' : '测试包',
        'platform' : 'package',
        'channel' : '说明',
        'fileURL' : 'fileURL',
        'langs':'11,22,33',
        'notices' : '44, ,66',
        'releaseNotes' : ' , , ',
        # 'forceUpdate' : 1,
        # 'publishStatus' : 1,
        # 'packageId' : 3,
    }
    # sendsmsform_data = {
    #     # 'id' : 1,
    #     'name' : '紫翼测试222',
    #     'type' : 'software',
    #     'platform' : 'software',
    #     'channel' : 'channel2',
    #     'resourcesUrl' : 'resourcesUrl2',
    #     'iosUrl' : 'iosUrl2',
    #     'checkUsers' : '1,17,2',
    #     'mailUsers' : '1,17,2',
    # }
    # sendsmsform_data = {
    #     'id' : 23,
    #     'name' : '紫翼测试2',
    #     'mail' : '1111@zhiyun-test.com',
    #     'status' : 0,
    # }
    # sendsmsform_data = {
    #     'id' : 24,
    #     'title' : '紫翼测试·改',
    #     'functions' : 'fun1,fun2,fun3,fun4',
    # }

    # 构建post请求
    request = urllib.request.Request(url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    # dict_json = json.loads(response.read().decode())
    print(response.read().decode())
    print("####################")
    return 1

    



if __name__ == '__main__':
    testtoken()