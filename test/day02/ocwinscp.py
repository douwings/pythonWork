# import time
# ts = int(time.time() * 1000)
# print(ts)
import os

# 打开程序
os.system('start D:\web\client.html')

# kill进程
# os.system('taskkill /f /t /im Fiddler.exe')



# winscp 上传命令
# uname = 'app3'
# pwd = 'be5aff48-cb2f-4e8e-b173-118089748bb3'
# host = '118.24.109.62'
# port = '22051'
# fromfolder = 'C:\\Users\\Administrator\\Desktop\\nodejs\\nodejs\\testfolder'
# tofolder = '/data/app3/testfolder'

# os.system('winscp.exe /console /command "option batch continue" "option confirm off" "open sftp://app3:be5aff48-cb2f-4e8e-b173-118089748bb3@118.24.109.62:22051" "option transfer binary" "put C:\\Users\\Administrator\\Desktop\\nodejs\\nodejs\\testfolder /data/app3/testfolder" "exit"')
# os.system('winscp.exe /console /command "option batch continue" "option confirm off" "open sftp://%s:%s@%s:%s" "option transfer binary" "put %s %s" "exit"'%(uname,pwd,host,port,fromfolder,tofolder))