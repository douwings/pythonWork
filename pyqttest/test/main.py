import cgitb
import sys


from window.zywindow import zywindow
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    sys.excepthook = cgitb.Hook(1, None, 5, sys.stderr, 'text')
    app = QApplication(sys.argv)
    m = zywindow()
    sys.exit(app.exec_())