# -*-coding:utf-8-*-
import os
import time

os.system('adb shell am start -n com.jifen.qukan/com.jifen.qkbase.main.MainActivity')
time.sleep(5)
os.system('adb shell input tap 110 2030')
time.sleep(5)

while 1:
    position = 1000
    os.system('adb shell input tap 110 %d'%(position))
    time.sleep(1)

    for count in range(55):
        time.sleep(3)
        os.system('adb shell input swipe 100 600 100 400')

    os.system('adb shell input tap 120 150')
    time.sleep(1)

    os.system('adb shell input tap 110 2030')
    # os.system('adb shell input swipe 200 200 200 1800')
    time.sleep(5)