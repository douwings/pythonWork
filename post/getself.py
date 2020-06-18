# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time


def get():
    url = 'http://127.0.0.1:80'
    # data = {
    #     'code' : '0231512s1uGMOk0kWY0s1bDV1s11512o',
    # }
    # query_string = urllib.parse.urlencode(data)

    # url += query_string

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    # get
    requset = urllib.request.Request(url = url , headers=headers)
    response = urllib.request.urlopen(requset)
    print("####################")
    print(response.read().decode())


if __name__ == '__main__':
    get()