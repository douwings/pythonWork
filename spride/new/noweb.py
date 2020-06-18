#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from aip import AipSpeech
import threading
import time

testreq_url = "https://www.gequge.pw/2"
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    

def getVideoUrl(checkword) :
    videoUrlList = []
    for i in range(1,10):
        print(i)
        thisurl = 'https://www.gequge.pw/Video2/asian?page={}'.format(i)
        print(thisurl)
        r = requests.get(thisurl, headers=head)
        soup = BeautifulSoup(r.text, "html.parser")
        soupli = soup.find_all('li')
        print('soupli',soupli)
        for oneli in soupli:
            if '''href="/Video2/video''' in str(oneli):
                if '''{}'''.format(checkword) in str(oneli):
                    onea = oneli.find_all('a')
                    videoUrlList.append('https://www.gequge.pw' + onea[0].get('href'))
                    # https://www.gequge.pw/Video2//asian?page=2
    return videoUrlList

if __name__ == '__main__':
    # checkword = input('请输入关键字：')
    checkword = '中文'
    videoUrlList = getVideoUrl(checkword)
    print(videoUrlList)
    r = requests.get(videoUrlList[0], headers=head)
    soup = BeautifulSoup(r.text, "html.parser")
    soupli = soup.find_all('li')
    print(soupli)