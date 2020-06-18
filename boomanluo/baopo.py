# -*- coding=utf-8 -*-

# for num in range(10000):
#     if len(str(num)) < 4:
#         for time in range(4 - len(str(num))):
#             num = '0' + str(num)

#     print(num)
import urllib.request
import urllib.parse
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

post_url = 'https://yy.cnns.net/api/sendsmsverify'
# url = 'https://yy.cnns.net/api/queryuserexist?'
# username=10201020@qq.com
#  参数写成字典
data = {
    'username' : '18675747894',
}

form_data = {
    'telno' : "18675747894",
}

# query_string = urllib.parse.urlencode(data)

# url += query_string

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

#get
# requset = urllib.request.Request(url = url , headers=headers)
# response = urllib.request.urlopen(requset)
# 构建post请求
request = urllib.request.Request(url = post_url,headers = headers)
form_data = urllib.parse.urlencode(form_data).encode()
# 发送post请求
response = urllib.request.urlopen(request,data = form_data)

print(response.read().decode())