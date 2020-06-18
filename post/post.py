# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time

def postsendsms():
    ssl._create_default_https_context = ssl._create_unverified_context

    sendsmspost_url = 'http://172.16.2.111:3000/v1/login_by_wx'
    
    t = time.time()
    sendsmsheaders = {
        # 'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    sendsmsform_data = {
        'userwxcode': '043Ow9h228nyXU0IPFi22wbMg22Ow9h2',
        'encryptedData' : '76uQW81eWiIo8JCsRTUWf4QuR3PkgctOfF3rvAcTx2jXHRfauzia0XggmMANUYK0WylpOp6Ms3YXkOTqNWvQJ4ualQkpZiowJzrL71p1AXCCdpGlDo7YiB9Qt0K5In/h0mme0Jzw99LCyPTac2dwepNle0LRe1HCNmKlYyyyF5kpgB/ZD8BSBSGw8VFpufXWagZb+iQ88T25iPnPrTMhpJRDun7F/JROcNERmjCHlSzYADYMxaOqaj17tk1mKRe5lt2tphxARR++ZfWaTqqSESJn/ywYZr+3XATsZZ/Ve7rgieoQshb6drQTEhCUDoUB2bz3XVHNsm6X8wiv7rCBBe4Gm6MEguKCJxeXcS41kYaKS+caZarcLJ3JD5sstrQ6zx6pKaGhIja5AvBWWyBtyMgn3tvXeh28Glt5qrOK2GuvWK5BoKC71tQSi6iz8OQhCS3P3hdGfNf/tSH6Eb3krzZOaV19jQGAgVI+wNpVvDY=',
        'iv' : 'kDJKkS9g6mFXputhbNouMw==',
    }

    # 构建post请求
    request = urllib.request.Request(url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    print(dict_json)
    print("####################")
    return dict_json

def testtoken(data) : 
    print(data['errcode'])
    ssl._create_default_https_context = ssl._create_unverified_context

    sendsmspost_url = 'http://172.16.2.44:3000/v1/sforeignlogin'
    
    t = time.time()
    sendsmsheaders = {
        # 'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    authData = {
        'openid' : data['openid'],
        'access_token' : data['access_token'],
    }
    sendsmsform_data = {
        'platform': 'weixin',
        'authData' : json.dumps(authData),
    }

    # 构建post请求
    request = urllib.request.Request(url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    print(dict_json)
    print("####################")
    return dict_json


def get_wx_userinfo():
    url = 'http://172.16.2.44:3000/v1/app/get_wx_userinfo?'
    data = {
        'code' : '0231512s1uGMOk0kWY0s1bDV1s11512o',
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
    # get_wx_userinfo()
    # testtoken(postsendsms())
    postsendsms()
    # data = postsendsms()
    # testtoken(data)
    # testtoken(data)
    # testtoken(data)

    # 23_BgsyJbTUfekU4pynn0EbQpC1T0jCOiwUEtSJhF6FghVFFLcgXyXflYQx5wAv1-qqBfGcYLZE6KfBUk3oPt9ELrDkA6lB_tgiVJG6hRI7V0_20jaPvkHbL_eG9PgPIKbADAZSU
    # 23_BgsyJbTUfekU4pynn0EbQpC1T0jCOiwUEtSJhF6FghVFFLcgXyXflYQx5wAv1-qqBfGcYLZE6KfBUk3oPt9ELrDkA6lB_tgiVJG6hRI7V0_20jaPvkHbL_eG9PgPIKbADAZSU
    # 23_bej0j1-r1VKCVYNB7ZDi05kRhrN1J3jXlVXjrsmClv7s_azAgShoybtG99VoCh3791R4Yp3i4d7o2FcmmQ5kLuLehdfSfKPMnKw79x3f0ke_-XE7hkG5irujGjEoKI9ZNeGhaOaadKDNeqhVGRBdAFAJUE
    # 23_bej0j1-r1VKCVYNB7ZDi05kRhrN1J3jXlVXjrsmClv7s_azAgShoybtG99VoCh3791R4Yp3i4d7o2FcmmQ5kLuLehdfSfKPMnKw79x3f0ke_-XE7hkG5irujGjEoKI9ZNeGhaOaadKDNeqhVGRBdAFAJUE
    # { params: { userwxcode: '011oLiaZ1Vnt5U0aF98Z17ZDaZ1oLiah' } }
    # simpleForeignLogin