# 导入模块
import pymysql
import threading
import time

class myDB():
    def __init__(self,host,user,password,port,db,charset):
        self.conn = pymysql.connect(host=host, user=user, password=password, port=port, db=db, charset=charset)
        # self.conn = pymysql.connect(host='localhost', user='root', password='xzlp1020',port = 3306, db='beforedata', charset='utf8')
        self.cursor = self.conn.cursor()  # cursor当前的程序到数据之间连接管道

local = myDB(host='localhost', user='root', password='xzlp1020',port = 3306, db='beforedata', charset='utf8mb4')
cloud = myDB(host='loghost', user='root', password='xzlp1020',port = 3306, db='zy_log', charset='utf8mb4')

class MyThread(threading.Thread):
    def __init__(self,dictdata):
        threading.Thread.__init__(self)
        self.dictdata = dictdata
    def run(self):
        with thread_max_num:
            doit(self.dictdata)

def doit(dictdata):
    try:
        cloud.cursor.execute(
            "select * from access_log_api where createAt between '{0}' and '{1}'".format(dictdata['data2'],dictdata['data1']))
        all = cloud.cursor.fetchall()
        print('当前i为', dictdata['i'])
        print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        print('时间间隔为',dictdata['data2'],dictdata['data1'])
        for i in range(0, len(all)):
            try:
                body = all[i][5]
                body = body.replace("'", " ")
                body = body.replace("\\", " ")
                sql = '''insert into beforedatatest (id,userId,method,url,headers,body,ip,createAt) values({0},{1},'{2}','{3}','{4}','{5}','{6}','{7}')'''.format(all[i][0],"NULL" if all[i][1] == None else all[i][1],all[i][2],all[i][3],all[i][4],body,all[i][6],all[i][7])

                local.cursor.execute(sql)
                local.conn.commit()
            except Exception as e:
                print('插入错误', e)
                print('mysql语句为',sql)
    except Exception as e:
        print('查询错误', e)

def beforeHours2Date(hours, date_format,starttime):
    hours = int(hours)
    timeArray = time.strptime(starttime, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))
    t = timeStamp - hours*60*60
    t = time.strftime(date_format, time.localtime(t))
    return t

if __name__ == "__main__":
    thread_max_num = threading.Semaphore(1)

    for i in range(5, 0, -1):
        data1 = beforeHours2Date(hours=i,date_format='%Y-%m-%d %H:%M:%S',starttime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        data2 = beforeHours2Date(hours=i+1, date_format='%Y-%m-%d %H:%M:%S',starttime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        dictdata = {
            'data1': data1,
            'data2': data2,
            'i': i,
        }
        # print(dictdata)
        th = MyThread(dictdata)
        th.start()
