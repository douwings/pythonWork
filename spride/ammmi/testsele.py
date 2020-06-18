# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
import re
import time
import os
import sys

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

def main(req_url,name):
    browser = ChromeDriverNOBrowser()
    print('开始get')
    browser.get(req_url)
    m3u8urllist = []
    for entry in browser.get_log('performance'):
        if 'm3u8' in str(entry):
            m3u8url = 'https' + str(re.findall(".*https(.*)m3u8.*", str(entry))[0]) + 'm3u8'
            print(m3u8url)
            m3u8urllist.append(m3u8url)

    browser.quit()
    m3u8urllist2 = list(set(m3u8urllist))
    for m3u8url in m3u8urllist2:
        print(m3u8url)
    print('当前url为： ' + str(m3u8urllist2[0]))
    os.system('ffmpeg -i ' + m3u8urllist2[0] + ' ' + name)

if __name__ == '__main__':
    testreq_url = "https://www.ammmi.com/v_play/bXZfNTgyNzctbm1fMQ==.html"
    testname = '雄兵连1.mp4'
    main(testreq_url,testname)