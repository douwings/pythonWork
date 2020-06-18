import os


def run_that(command):
    # os.popen('chcp 65001')
    # locale.setlocale(locale.LC_ALL, 'zh_CN.GBK')
    res = os.popen(command, 'r', 1)
    data = ''
    for i in res.read():
        try:
            data += i
        except:
            pass
    return data

# if __name__=='__main__':
#     data=run_that('python C:/Users/pc/Desktop/jiaoyimao.py'.replace('\\','/'))
#     print(data)
