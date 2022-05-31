import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from MainWindow import MainWindow
from ChildWindow import ChildWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_win = MainWindow(self)
        self.main_win.show()
#        QTimer.singleShot(5000, self.showChildWindow)
#

#    def showChildWindow(self):
#        self.child_win = ChildWindow(self)
#        self.child_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())