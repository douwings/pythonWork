import json

import os
from PyQt5 import Qt

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow, QApplication


class showWindow(QMainWindow):
    def __init__(self,name=''):
        super().__init__()
        self.name=name
        try:
            self.load_location()
        except:
            self.save_location()

    def save_location(self):
        print('save_location event')
        with open('window_location_%s.txt'%self.name, 'w') as f:
            data = {'x': self.x(), 'y': self.y()}
            f.write(json.dumps(data))

    def load_location(self):
        with open('window_location_%s.txt'%self.name, 'r') as f:
            txt = f.read()
            print('%s位置'%self.name)
            print(txt)
            j = json.loads(txt)
            if j['x']>QApplication.desktop().width():
                self.move(int(QApplication.desktop().screenGeometry(0).width())-100,j['y'])
            else:
                self.move(j['x'],j['y'])

    def show(self):
        super().show()
        try:
            if os.path.exists('window_location_%s.txt'%self.name):
                self.load_location()
            else:
                self.save_location()
        except Exception as e:
            print(e)

    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.Qt.LeftButton:
                self.m_flag = True
                self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
                event.accept()
                self.setCursor(QCursor(Qt.Qt.OpenHandCursor))  # 更改鼠标图标
        except Exception as e:
            print(e)


    def mouseMoveEvent(self, QMouseEvent):
        try:
            if Qt.Qt.LeftButton and self.m_flag:
                self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
                QMouseEvent.accept()
        except Exception as e:
            print(e)


    def mouseReleaseEvent(self, QMouseEvent):
        try:
            self.m_flag = False
            self.save_location()
            self.setCursor(QCursor(Qt.Qt.ArrowCursor))
        except Exception as e:
            print(e)

