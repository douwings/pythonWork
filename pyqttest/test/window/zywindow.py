#coding:utf-8
import json
import os
from PyQt5 import Qt, QtCore, QtWidgets
from window.showWindow import showWindow
from window.talk_label import talk_label
from window.ImageLabel import ImageLabel
# from PyQt5.Qt3DCore import QEntity, QTransform, QAspectEngine
# from PyQt5.Qt3DRender import QCamera, QCameraLens, QRenderAspect
# from PyQt5.Qt3DInput import QInputAspect
# from PyQt5.Qt3DExtras import QForwardRenderer, QPhongMaterial, QCylinderMesh, QSphereMesh, QTorusMesh, Qt3DWindow, QOrbitCameraController


import sys
import aiml


alice_path = 'D:\\python\\Lib\\site-packages\\aiml\\botdata\\alice'
os.chdir(alice_path)
alice = aiml.Kernel()
alice.learn("startup.xml")
alice.respond('LOAD ALICE')


class zywindow():
    def __init__(self):
        super().__init__()
        mainwindow = showWindow('main')  # 主窗口（蕾姆）
        talkwindow = showWindow('talk')  # 对话窗口
        self.centralwidget = QtWidgets.QWidget(mainwindow)  # 直译 核心部件 部件化此window 方便传入imagelabel中
        self.talkwidget = QtWidgets.QWidget(talkwindow)
        self.talk_label = talk_label(self.talkwidget)  # 对话栏
        # self.talk_label.setGeometry(QtCore.QRect(0, 80, 251, 91))
        self.talk_label.hide()

        mainwindow.setObjectName("mainwindow")
        mainwindow.resize(321, 558)
        mainwindow.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)  # 去边框
        mainwindow.setAttribute(Qt.Qt.WA_TranslucentBackground)  # 去背景 实现透明窗口
        mainwindow.setCentralWidget(self.centralwidget)

        talkwindow.resize(321, 558)
        talkwindow.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint | Qt.Qt.Tool)
        talkwindow.setAttribute(Qt.Qt.WA_TranslucentBackground)
        talkwindow.setCentralWidget(self.talkwidget)

        self.mainwindow = mainwindow
        self.talkwindow = talkwindow

        self.image_label = ImageLabel(self.centralwidget)
        self.image_label.setGeometry(QtCore.QRect(20, 120, 271, 391))
        self.image_label.talklabel = self.talk_label
        self.pic()

        self.talk_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.talk_edit.setGeometry(QtCore.QRect(20, 480, 201, 21))
        self.talk_edit.setObjectName("talk_edit")
        self.talk_edit.hide()
        self.image_label.input = self.talk_edit
        self.mainwindow.show()
        self.talkwindow.show()
        self.talk_edit.returnPressed.connect(self.talk)
        self.talkmodule = ''

    def pic(self):#看板娘图片
        self.image_label.showgif()

    def talk(self):
        try:
            msg = self.talk_edit.text()
            self.talk_edit.setText('')
            # 接入处理语言功能
            # 先处理各种talkmodule的
            print('self.talkmodule',self.talkmodule)
            if (self.talkmodule == 'init game'):
                if (msg == 'game path done'):
                    self.talkmodule = ''
                    self.say('已退出路径配置模式')
                    return 1
                result = addgamepath(msg)
                self.say(str(result))
                return 1
            if (self.talkmodule == ''):
                if (msg == 'init game path'):
                    self.talkmodule = 'init game'
                    self.say('请输入游戏启动项路径')
                    return 1
                # 再处理改变其他

                if(msg == '游戏模式'):
                    result = gamemodule()
                    self.say(str(result))
                    return 1
                if (msg == '办公模式'):
                    print('进入游戏模式')
                    return 1
                print('准备进入回答模式')
                print('msg',msg)
                outmsg = alice.respond(msg)
                print('outmsg', outmsg)
                self.say(outmsg)

        except Exception as e:
            print(e)


    def say(self,content):
        self.image_label.talk(content)



def gamemodule():
    # try:
        if not os.path.exists('game.txt'):
            print('没有文件')
            with open('game.txt', 'w+') as f:
                pass
        with open('game.txt', 'r') as f:
            txt = f.read()
            if len(txt) == 0:
                return '您尚未配置游戏路径 请输入 \'init game path\' 来进行配置'
                # os.system('start D:\web\client.html')
            j = json.loads(txt)
            for item in j:
                print('item', item)
                list = str(item).split('\\')
                print('list', list)
                newitem = ''
                for i in range(len(list)):
                    if i != 0:
                        list[i] = '"' + str(list[i]) + '"'
                        print(list[i])
                    newitem += list[i]
                    if i == len(list) - 1 :
                        break
                    newitem += '\\'
                print('newitem',newitem)
                os.system('start ' + str(newitem))
    # except Exception as e:
    #     print(e)


def addgamepath(msg):
    try:
        print('准备添加路径')
        print('msg', msg)
        data = []
        with open('game.txt', 'r+') as f:
            txt = f.read()
            print('txt',txt)
            if len(txt) > 0:
                j = json.loads(txt)
                if len(j) > 0:
                    data.extend(j)
        with open('game.txt', 'w+') as f2:
            print('beforedata', data)
            data.append(msg)
            print('afterdata', data)
            f2.write(json.dumps(data))
            return '路径添加成功 如添加完毕 请输入 \'game path done\' 来退出配置'
    except Exception as e:
        print(e)


