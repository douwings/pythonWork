#coding:utf-8

from PyQt5 import Qt

from PyQt5.QtWidgets import QLabel, QFrame,QTextEdit
class talk_label(QTextEdit):
    #对话栏
    def __init__(self,centralwidget):
        super().__init__(centralwidget)
        self.setup()

    def setup(self):

        # self.setText('你好')
        # self.adjustSize()
        # self.setFrameShape(QFrame.Box)
        # self.setAlignment(Qt.Qt.AlignLeft)
        # self.setWordWrap(1)
        self.setStyleSheet('border-width: 1px;padding-top:5px;border-style: solid;border-color: rgb(135,206,250);'+
                           'background-color: rgb(135,206,250);color:rgb(255,255,255);'+
                            'border-radius:10px; border-left:20px;padding-left:20px;'
                           )