import os
import time

# os.makedirs(r'E:\BaiduNetdiskDownload\wings\py\clockIn\test')
# 解锁手机
os.system('adb shell input keyevent 26')
time.sleep(1)
os.system('adb shell input swipe 500 1500 500 800')
time.sleep(1)

# 关闭所有进程
os.system('adb shell am force-stop com.alibaba.android.rimet')
time.sleep(1)

# 打开钉钉
os.system('adb shell am start -n com.alibaba.android.rimet/.biz.LaunchHomeActivity')
time.sleep(3)

# 模拟点击
# 下方位置点击两次 防止更新提示
os.system('adb shell input tap 545 1945')
time.sleep(5)
os.system('adb shell input tap 545 1945')
time.sleep(5)
# 点击考勤打卡位置
os.system('adb shell input tap 953 1002')
time.sleep(5)
# 点击下班打卡按钮
os.system('adb shell input tap 545 1252')
time.sleep(5)
# # 点击上班打卡按钮
# os.system('adb shell input tap 545 735')
# time.sleep(5)

# 关闭所有进程
os.system('adb shell am force-stop com.alibaba.android.rimet')
# os.system('adb shell input tap 300 2100')
# time.sleep(1)
# os.system('adb shell input swipe 500 1500 500 800')
time.sleep(1)
os.system('adb shell input keyevent 26')