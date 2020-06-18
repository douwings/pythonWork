import urllib.request
import urllib.parse

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://www.baidu.com/'

# response = urllib.request.urlopen(url)

# print(response.read())
#构建请求对象 urllib.request.Request()

# 自己要伪装的头部
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

requset = urllib.request.Request(url = url , headers=headers)

response = urllib.request.urlopen(requset)

print(response.read())