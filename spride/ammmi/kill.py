import os
import time

while True:
    try:
        # os.system('taskkill /im chromedriver.exe /F')
        # os.system('taskkill /im chrome.exe /F')
        # os.system('taskkill /im "360NewsPop.exe" /F')
        os.system('ntsd -c q -pn 360NewsPop.exe')
        time.sleep(1)
    except Exception:
        print(Exception)
    