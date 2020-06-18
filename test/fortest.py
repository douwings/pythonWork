# test = '中文'
# test2 = 'English'

# print('这个是{},{}'.format(test,test2))

# import time

# if __name__ == "__main__":
#     # for i in range(0, 5 * 5):
#     #     print(i)
#     str = "I'm Iron Man!"
#     str = str.replace("'"," ")

#     print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


#     # 372039
#     # 328466

#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os
from aip import AipSpeech
import threading
import time

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}


if __name__ == "__main__":
    # url = 'https://www.gequge.pw/Video2//asian?page=2'
    url = 'https://www.gequge.pw/2'
    r = requests.get(url, headers=head)
    soup = BeautifulSoup(r.text, "html.parser")
    soupli = soup.find_all('li')
    for oneli in soupli:
        print(soupli)