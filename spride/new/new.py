# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import re
import time
import os
import sys
import requests
from bs4 import BeautifulSoup
import os
from aip import AipSpeech
import threading
import urllib.request
import urllib.parse

# 无界面模式
def ChromeDriverNOBrowser():
    __browser_url = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"
    chrome_options = Options()
    chrome_options.binary_location = __browser_url
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    prefs = {
        "profile.managed_default_content_settings.images": 1,
        "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    }
    chrome_options.add_experimental_option('prefs', prefs)
    caps = DesiredCapabilities.CHROME
    caps["goog:loggingPrefs"] = {"performance": "ALL"}
    driverChrome = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver", desired_capabilities=caps,
                                    chrome_options=chrome_options)
    return driverChrome


# # 有界面
# def ChromeDriverBrowser():
#     __browser_url = "C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe"
#     chrome_options = Options()
#     chrome_options.binary_location = __browser_url
#     prefs = {
#         "profile.managed_default_content_settings.images": 1,
#         "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
#         "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
#     }
#     chrome_options.add_experimental_option('prefs', prefs)
#     caps = DesiredCapabilities.CHROME
#     caps["goog:loggingPrefs"] = {"performance": "ALL"}
#     driverChrome = webdriver.Chrome(executable_path="D:\\chromedriver\\chromedriver",desired_capabilities=caps, chrome_options=chrome_options)
#     return driverChrome


# req_url = "https://www.ammmi.com/v_play/bXZfNTgyNzctbm1fMQ==.html"
# req_url = "https://www.google.com"

def main(req_url):
    url = req_url
    # data = {
    #     's': name,
    # }
    # query_string = urllib.parse.urlencode(data)
    # url += query_string

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }
    # get
    r = requests.get(url, headers=headers)
    # print("####################")
    # print(r)
    soup = BeautifulSoup(r.text, "html.parser")
    soupli = soup.find_all('li')
    for index in range(len(soupli)):
        print(soupli[index])
    # browser = ChromeDriverNOBrowser()
    # print('开始get')
    # browser.get(req_url)
    # for entry in browser.get_log('performance'):
    #     print(entry)
    # browser.quit()
    

if __name__ == '__main__':
    testreq_url = "https://www.gequge.pw/2"
    # testname = '雄兵连1.mp4'
    main(testreq_url)