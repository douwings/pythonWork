import requests
from bs4 import BeautifulSoup
import os
from threading import Thread
import time


if __name__ == '__main__':
    url = "http://www.miaomiaoxue.com/"
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    r = requests.get(url, headers=head)
    soup = BeautifulSoup(r.text, "html.parser")
    soupli = soup.find_all('ul')
    print(soupli[0])
    for i in soupli:
        if 'second-type' in str(i):
            j = i.find_all('ul')
            for k in j:
                print(k)
        
    # print(soupli)
    # list_url = []  # 用于存放所有小说的url
    # list_name = []  # 用于存放所有小说的名字
    # dic_name = {}  # 用于把名字和对应的url存放起来
    # try:
    #     os.makedirs('d://novel')  # 建立存储地址
    # except:
    #     pass
    # for i in soupli:
    #     j = i.find_all('a')
    #     for k in j:
    #         list_name.append(k.text)
    #         list_url.append(k.get('href'))
    # list_url = list_url[10:]  # 删去无用的错误网址
    # list_name = list_name[10:]  # 删去无用的错误名字
    # for i in range(0, len(list_name)):
    #     dic_name[list_name[i]] = list_url[i]
    # print('当前收录小说一共'+str(len(list_name))+'本')
    # temp = input('输入你想下载的小说:')
    # if temp in dic_name:
    #     print('小说下载地址为D://novel')
    #     print('此小说url为：' + str(dic_name[temp]))
    #     try:
    #         path = 'd://novel//' + str(temp)
    #         os.makedirs(path)  # 建立小说对应地址
    #     except:
    #         pass
    #     singlenovel(dic_name[temp])
    # else:
    #     print('暂时没有这本小说')
    # print('')
    # print('操作完成')
