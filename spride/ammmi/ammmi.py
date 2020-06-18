# coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from aip import AipSpeech
import threading
import time
import urllib.request
import urllib.parse
import testsele


# 打开该动漫分集播放页 下载当前分集
def getoneanimalweb(url):
    for i in range(0, len(url)):
        dictdata = {
            'oneurl': url[i],
            'thisname': name + str(i+1) + '.mp4',
        }
        testsele.main(dictdata['oneurl'],dictdata['thisname'])


# 打开该动漫分集页 获取每个分集
def getanimalweb(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    print(url)
    # get
    r = requests.get(url, headers=headers)
    print("####################")
    print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    soupallas = soup.find_all('a')
    oneurl = []
    for item in soupallas[:]:
        # print(item)
        if str(item).find("第") != -1 and str(item).find("集") != -1:
            oneurl.append(item.get('href'))
    getoneanimalweb(oneurl)


# 先获取该动漫分集页
def getwebbyname(name):
    url = 'https://www.ammmi.com/?'
    data = {
        's': name,
    }
    query_string = urllib.parse.urlencode(data)
    url += query_string

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    print(url)
    # get
    r = requests.get(url, headers=headers)
    # print("####################")
    # print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    soupli = soup.find_all('li')
    animalurl = ''
    for index in range(len(soupli)):
        if name in str(soupli[index]):
            allas = soupli[index].find_all('a')
            animalurl = allas[0].get('href')

    getanimalweb(animalurl)

class MyThread(threading.Thread):
    def __init__(self, dictdata):
        threading.Thread.__init__(self)
        self.dictdata = dictdata

    def run(self):
        with thread_max_num:
            testsele.main(self.dictdata['oneurl'],self.dictdata['thisname'])


name = ''
if __name__ == '__main__':
    thread_max_num = threading.Semaphore(1)
    name = input('输入你想下载的动漫:')
    # name = '雄兵连'
    getwebbyname(name)

    # name = ['雄兵连','灵笼','文豪野犬','笨女孩']
    # for onename in name:
    #     getwebbyname(onename)



