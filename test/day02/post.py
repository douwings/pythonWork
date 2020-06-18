import urllib.request
import urllib.parse
import time

post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule HTTP/1.1'

# word = input('in:')
ts = int(time.time() * 1000)
word = 'wings'
# 构建post表单数据
form_data = {
    'i' : word,
    'from' : 'AUTO',
    'to' : 'AUTO',
    'smartresult' : 'dict',
    'salt' : str(ts) + '8',
    'sign' : '6849f47642c016c6d8db1a9f75f2796d',
    'ts' : ts,
    'bv' : '1e9538f95b23257ede9acdc941c8e1f8',
    'doctype' : 'json',
    'version' : '2.1',
    'keyfrom' : 'fanyi.web',
    'action' : 'FY_BY_REALTlME',
    'typoResult' : 'false',
}
# 模拟浏览器头
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}
# 构建请求对象

request = urllib.request.Request(url = post_url,headers = headers)
form_data = urllib.parse.urlencode(form_data).encode()
# 发送post请求

response = urllib.request.urlopen(request,data = form_data)

print(response.read().decode())