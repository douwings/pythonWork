# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time

def postsms():
    ssl._create_default_https_context = ssl._create_unverified_context

    # sendsmspost_url = 'http://172.16.2.101:3999/site/transcode'
    sendsmspost_url = 'http://172.16.2.111:3999/site/transcode'
    # sendsmspost_url = 'http://172.16.2.111:3999/site/queryjoblist'
    # sendsmspost_url = 'http://172.16.2.111:3999/site/queryfile'
    t = time.time()
    sendsmsheaders = {
        # 'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    sendsmsform_data = {
        'fromBucket':'zhiyundata',
        # 'from':'/zymediao/compress_test/big_buck_bunny.mp4',
        # 'to':'/compress_test/big_buck_bunny.mp4',
        'region':'oss-cn-hangzhou',
        'queryfilebucket':'zymediapr',
        # 'region':'oss-cn-shenzhen',
        # 'queryfilebucket':'zhiyundata',
        # 'JobIds':'cf12ac3cfe484a78b0ca3cc8ade66710',
        'inputObject': 'kmstest/5S3lab.mp4',
        'outputObject' : 'kmstest/5S3lab1.mp4', #xxxxxxetag 22D4465143ACDC6F64AFB06B47D6331D
        # 'outputObject' : 'kmstest/5S3labxxxx.mp4', #xxxxetag 22D4465143ACDC6F64AFB06B47D6331D
    }
# 'zhiyundata::kmstest/5S3lab.mp4',
# 'zhiyundata::kmstest/5S3labxxx.mp4',
    # 构建post请求
    request = urllib.request.Request(url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    print(dict_json)
    print("####################")
    return dict_json

def getlogin():
    url = 'http://172.16.2.111:3999/login?'
    data = {
        # 'code' : '0231512s1uGMOk0kWY0s1bDV1s11512o',
    }
    query_string = urllib.parse.urlencode(data)

    url += query_string

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    # get
    requset = urllib.request.Request(url = url , headers=headers)
    response = urllib.request.urlopen(requset)
    print("####################")
    print(response.read().decode())



if __name__ == '__main__':
    postsms()
    # getlogin()
   