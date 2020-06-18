# -*- coding=utf-8 -*-
import urllib.request
import urllib.parse
import ssl
import json
import time


def postsendsms(userphone):
    ssl._create_default_https_context = ssl._create_unverified_context

    sendsmspost_url = 'https://ssl.zc.qq.com/cgi-bin/zc/sms_send'

    t = time.time()
    sendsmsheaders = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        ':authority': 'ssl.zc.qq.com',
        ':method': 'POST',
        ':path': '/cgi-bin/zc/sms_send',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'content-length': 57,
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        # 'cookie': 'pgv_pvi=5824080896;RK=lWalaMxpdp;ptcz=1b7d58710484cc405aaa96120d6a1e4ce693d63bf66b0d73a4844be449f42641;pgv_pvid=2032889190;eas_sid=t1H5I5e1S6y9u5l2y0I5r0k8U3;gaduid=5caaeee34c1b4;tvfe_boss_uuid=f004fb718243d56d;ptui_loginuin=3075537270;pgv_info=ssid=s9657032141;pac_uid=0_6c89142b40313;pgv_si=s8048512000;_qpsvr_localtk=0.6049335403430607;ptisp=ctc;zc_uid=1559125468_1053412824;zc_en_identifier=000DF4987B65E62C7F578F94F60B5AAC2182423F18B2713E69B00AB0;zc_chs_identifier=000DF4987B65E62C7F578F94F60B5AFA24F01FE25776BC4F64F24B38;zc_cht_identifier=000DF4987B65E62C7F578F94F60B5ADCF0F1A8D06468407446277D68;zc_phone_identifier=000DF4987B65E62C7F578F94F60B5A012CB451AB2DE5E3A3A7BCC4797A;ADTAG=;regkey=;machineCookie=35d6626bc0a2d744a8ae5510e02c3b6c6dd042be5d2b07de;sessionCookie=22453e365f1446e3dfca0dc4e18aa65e618148a3e57a915c;sessionStatus=c4e2327811a1e8ae261e9d643b5d51615bd909f05c62bf7cb277396c13494a1124be012ca174a45f',
        'origin': 'https://ssl.zc.qq.com',
        'referer': 'https://ssl.zc.qq.com/v3/index-chs.html?type=0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    sendsmsform_data = {
        'telno': userphone,
        'nick': "秀儿",
        'elevel': 3
    }

    # 构建post请求
    request = urllib.request.Request(
        url=sendsmspost_url, headers=sendsmsheaders)
    form_data = urllib.parse.urlencode(sendsmsform_data).encode()
    # 发送post请求
    response = urllib.request.urlopen(request, data=form_data)
    dict_json = json.loads(response.read().decode())
    print(dict_json)
    # if dict_json['message'] == "验证码已发送。":
    #     return True
    # else:
    #     return False


if __name__ == '__main__':
    # userphone = input("请输入电话：")
    # userphone = 15173512106
    userphone = '008615374099873'
    num = 1
    postsendsms(userphone)
    # for num in range(3):
    # while True:
    #     # username = 'wing1020'
    #     print("第%s次发送"%(num))
    #     num += 1
    #     result = postsendsms(userphone)
    #     if(result == False):
    #         break
# msiexec /package python-3.7.3.exe