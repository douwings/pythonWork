# -*-coding:utf-8-*-
import os
import time


# adb logcat|find "Displayed" >d:/logs.txt 记录app打开页面Activity

# 打开目标app
os.system('adb shell am start -n com.tomato.reading/com.bytedance.read.pages.splash.SplashActivity')
time.sleep(8)
# 切换到书架 位置待调
os.system('adb shell input tap 750 2030')
time.sleep(5)

# 打开第一本小说 位置待调
os.system('adb shell input tap 200 600')
time.sleep(5)

while 1:
    # position = 1000
    # os.system('adb shell input tap 110 %d'%(position))
    # time.sleep(1)

    for count in range(3600):
        time.sleep(3)
        # 手指从右向左滑动
        os.system('adb shell input swipe 500 800 100 800')

    # os.system('adb shell input tap 120 150')
    # time.sleep(1)

    # os.system('adb shell input tap 110 2030')
    # # os.system('adb shell input swipe 200 200 200 1800')
    # time.sleep(5)