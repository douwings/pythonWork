import urllib.request
import urllib.parse
import time

post_url = 'http://fanyi.baidu.com/sug'

# word = input('in:')
# ts = int(time.time() * 1000)
word = 'wings'
# 构建post表单数据
form_data = {
    'kw' : word,
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