#coding:utf-8

from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtCore import QTimer, QThread
from PyQt5.QtGui import QPixmap, QFontMetrics,QMovie
from PyQt5.QtWidgets import QLabel, QMenu, QAction, QApplication
import os


# def get_module_dir(name):
#     path = getattr(sys.modules[name], '__file__', None)
#     if not path:
#         raise AttributeError('module %s has not attribute __file__' % name)
#     return os.path.dirname(os.path.abspath(path))



foodboy = 'E:\\BaiduNetdiskDownload\\wings\\py\\flask\\pyqt\\19-08-23\\test2\\test\\icon\\food_boy.gif'
leimu1 = 'E:\\BaiduNetdiskDownload\\wings\\py\\flask\\pyqt\\19-08-23\\test2\\test\\icon\\action1.png'
leimu2 = 'E:\\BaiduNetdiskDownload\\wings\\py\\flask\\pyqt\\19-08-23\\test2\\test\\icon\\action2.png'


class tcThread(QThread):

    def __init__(self):
        super().__init__()

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        while 1:
            try:
                os.system('taskkill /im QQ.exe /F')
                # os.system('taskkill /im "360NewsPop.exe" /F')
                # os.system('ntsd -c q -pn 360NewsPop.exe')
                self.sleep(2)
            except Exception:
                pass
                # print(Exception)
        # pass






class ImageLabel(QLabel):
    #图片加载控件
    def __init__(self,centralwidget,talklabel=0):
        #传入窗体
        super().__init__(centralwidget)
        self.stone = 1
        self.tcmodule = False
        self.talklabel = talklabel
        self.window = centralwidget
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
        self.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.input=''

        self.setAcceptDrops(True)

    def mouseDoubleClickEvent(self, *args, **kwargs):
        if self.input!='':
            self.input.show()
            self.input.setFocus()
            try:
                self.myTimer('mouseDouble',self.inputhide, 60000)
            except Exception as e:
                print(e)


    def talk(self,content,time=2000):
        # print(self.window.x())
        # print(self.talklabel.y())
        if self.talklabel:
            # self.talklabel.setGeometry(QtCore.QRect(250, 80, 251, 91))
            # self.talklabel.move(self.window.x()+150,self.window.y()+100)
            self.talklabel.show()
            index = 0
            temp = ''
            for i in content:
                if index > 5:
                    i += '\n'
                    index = 0
                temp += i
            self.talklabel.setText(temp)
            try:
                self.myTimer('talk',self.hide,4000)
            except Exception as e:
                print(e)


    def hide(self):
        self.talklabel.hide()

    def inputhide(self):
        self.input.hide()

    def myTimer(self,name,function,time=2000):
        try:
            if name == 'talk':
                self.talktimer = QTimer()  # 初始化一个定时器
                self.talktimer.timeout.connect(function)  # 计时结束调用operate()方法
                self.talktimer.start(time)  # 设置计时间隔并启动
            elif name == 'animation':
                self.animationtimer = QTimer()  # 初始化一个定时器
                self.animationtimer.timeout.connect(function)  # 计时结束调用operate()方法
                self.animationtimer.start(time)  # 设置计时间隔并启动
            elif name == 'mouseDouble':
                self.mouseDoubletimer = QTimer()  # 初始化一个定时器
                self.mouseDoubletimer.timeout.connect(function)  # 计时结束调用operate()方法
                self.mouseDoubletimer.start(time)  # 设置计时间隔并启动
        except Exception as e:
            print(e)


    def showgif(self):
        self.gif = QMovie(foodboy)
        self.setMovie(self.gif)
        self.gif.start()

    def animation(self,cmd):
        if cmd == 'none' :
            pix = QPixmap(leimu2)
            self.setPixmap(pix)
            self.myTimer('animation',self.normal)
        # else if

    def normal(self):
        self.gif = QMovie(foodboy)
        self.setMovie(self.gif)
        self.gif.start()
        # pix = QPixmap('icon/action1.png')
        # self.setPixmap(pix)

    # 右键菜单
    def rightMenuShow(self, point):
        self.popMenu = QMenu()
        tj=QAction(u'聊天功能', self)
        sc=QAction(u'删除', self)
        # tc = QAction(u'弹窗', self)
        xg = QAction(u'退出', self)
        self.popMenu.addAction(tj)
        self.popMenu.addAction(sc)
        # self.popMenu.addAction(tc)
        self.popMenu.addAction(xg)
        tj.triggered.connect(lambda: self.chat_server())
        sc.triggered.connect(lambda: self.mes('请不要删除我！'))
        # tc.triggered.connect(lambda: self.tanchuang())
        xg.triggered.connect(lambda: self.shut())
        try:
            self.showContextMenu(QtGui.QCursor.pos())
        except Exception as e:
            print(e)


    def mes(self,content):
        try:
            self.talk(content)
        except Exception as e:
            print(e)


    def tanchuang(self):
        # todo 用线程开启
        # 创建一个新的线程

        print('进入弹窗模式')
        # print('self.tcmodule', self.tcmodule)
        self.tcmodule = True if self.tcmodule == False else False
        print('self.tcmodule', self.tcmodule)
        tcthread = tcThread()
        if self.tcmodule:
            tcthread.start()
        else:
            tcthread.__del__()


    def chat_server(self):
        # 此处接入微软小冰或者小爱等

        self.talk('双击打开对话框和我聊天吧~')

    def shut(self):
        QApplication.quit()

    def showContextMenu(self, pos):
        '''''
        右键点击时调用的函数来定位到鼠标旁边
        '''
        # 菜单显示前，将它移动到鼠标点击的位置
        self.animation('none')
        self.popMenu.exec_(pos)
        self.popMenu.show()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            try:
                event.setDropAction(Qt.Qt.CopyAction)
            except Exception as e:
                print(e)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        try:
            if event.mimeData().hasUrls:
                event.setDropAction(Qt.Qt.CopyAction)
                event.accept()
                links = []
                for url in event.mimeData().urls():
                    path=str(url.toLocalFile())
                    data={'filename':path.split(r'/')[-1],'path':path}
                    self.file_type_check(data)
                print(links)
            else:
                event.ignore()
        except Exception as e:
            print(e)

    def file_type_check(self,data):
        if data['filename'].split('.')[-1] == 'py':
            from plug.run_python.lib.run_py_script import run_that
            try:
                print(data['path'].replace('\\', '/'))
                res = run_that('python '+data['path'].replace('\\', '/'))  # 正在施工

                self.talk(res,8000)
            except:
                self.talk('脚本里有错误哦')
        else:
            from plug.run_python.lib.run_py_script import run_that
            res = run_that(data['path'].replace('\\', '/'))  # 正在施工
            # links.append(data)