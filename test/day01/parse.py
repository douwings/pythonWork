import urllib.parse

# img_rul = 'http://i0.hdslb.com/bfs/article/bf4734ecc00607c5322d8eb2118236f7e47db283.jpg'
url = 'http://baidu.com/index.html?name=紫翼&pwd=1020763068'

# http%3A//baidu.com/index.html%3Fname%3D%E7%B4%AB%E7%BF%BC%26pwd%3D1020763068
ret = urllib.parse.quote(url)
# http://baidu.com/index.html?name=紫翼&pwd=1020763068
re = urllib.parse.unquote(ret)
print(ret)