# -*-coding:utf-8-*-
import os
import time

os.system('adb shell am start -n com.maihan.tredian/com.maihan.tredian.activity.WelcomeActivity')
time.sleep(7)
os.system('adb shell input tap 120 2030')
time.sleep(5)

while 1:
    position = 600
    os.system('adb shell input tap 110 %d'%(position))
    time.sleep(2)
    os.system('adb shell input swipe 100 900 100 400')
    time.sleep(2)
    os.system('adb shell input tap 500 1850')
    time.sleep(2)

    for count in range(15):
        time.sleep(3)
        os.system('adb shell input swipe 100 900 100 400')

    os.system('adb shell input tap 120 150')
    time.sleep(1)

    os.system('adb shell input tap 110 2030')
    # os.system('adb shell input swipe 200 200 200 1800')
    time.sleep(5)