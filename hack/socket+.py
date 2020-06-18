import socket
import os
import sys


def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)  # 设置超时
        s = socket.socket()
        s.connect((ip, port))  # 链接服务器和端口
        banner = s.recv(1024)  # 接受TCP套接字的最大数据量，一般1024
        return banner
    except:
        return


def checkVulns(banner, filename):
    f = open(filename, 'r')  # 打开文件遍历
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('[+] Server is vulnerable: ' + banner.strip('\n'))


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if not os.path.isfile(filename):  # 判断文件是否存在
            print('[-] ' + filename + ' does not exit.')
            exit(0)

        if not os.access(filename, os.R_OK):  # 判断是否有权限
            print('[-] ' + filename + ' access denied.')
            exit(0)

        # thisfile = './socket.py'
        # f = open(thisfile,mode = 'r',encoding = 'utf-8')
        # print(f.read())
        print(os.path.abspath(filename))
        print('[+] Reading From: ' + filename)

    else:
        print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')  # 没输入文件名
        exit(0)

    portList = [21, 22, 25, 80, 110, 443]
    # ip = '192.168.40.131'
    # ip = '192.168.3.199'  #self
    ip = '192.168.2.37'     #化宇
    for port in portList:
        banner = retBanner(ip, port)
        if banner:
            print('[+] ' + ip + ':' + str(port) + '--' + str(banner))
            if port == 21:
                checkVulns(banner, filename)


if __name__ == '__main__':
    main()
