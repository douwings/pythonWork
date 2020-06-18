import urllib.request

# url = 'http://www.baidu.com'
# 完整的url
# http://www.baidu.com:80/index.html?name=goudan&password=123#lala
# 协议  地址          端口号  目标文件   get所带参数             锚点
# response = urllib.request.urlopen(url)

# print(response)
# print(response.read().decode())
# print(response)
# with open('baidu.html','w',encoding='utf8') as fp:
#     fp.write(response.read().decode()) 
# with open('baidu.html','wb') as fp:
#     fp.write(response.read())



# 下载图片
image_url = 'http://attach.bbs.miui.com/forum/201811/30/170643gagw36nxag3g3swj.jpg'

# response = urllib.request.urlopen(image_url)

# # 图片只能写入本地二进制的格式
# with open('man.jpg','wb') as fp:
#     fp.write(response.read())

urllib.request.urlretrieve(image_url,'man2.jpg')