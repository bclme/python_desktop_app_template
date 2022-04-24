from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtCore, QtGui, QtWidgets, uic
from mainw import Window2
import sys
import time

class WindowApp(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(320, 245)
        self.quit = QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)
        self.move(400, 200) 
        lblusr =  QLabel('UserName', self)
        lblusr.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblusr.setGeometry(25, 55, 100, 30) 
        txtusr = QLineEdit(' ', self) 
        txtusr.setGeometry(100, 55, 150, 30)  
        lblpwd =  QLabel('Password', self)
        lblpwd.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblpwd.setGeometry(25, 100, 100, 30) 
        txtpwd = QLineEdit(' ', self) 
        txtpwd.setGeometry(100, 100, 150, 30)    
        pblogin = QPushButton('Login', self)
        pblogin.setGeometry(100, 165, 65, 25)
        pblogin.clicked.connect(self.onClick_pb3)  
        pbcanc = QPushButton('Cancel', self)
        pbcanc.setGeometry(180, 165, 65, 25)
        pbcanc.clicked.connect(self.onClick_pb4)        
        self.show()
    def closeEvent(self, event):
        close = QMessageBox()
        close.setIcon(QMessageBox.Icon.Question)
        close.setWindowTitle('Pls confirm')
        close.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        close.setText("Do you really want to quit?")
        close.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
        close = close.exec()

        if close == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    def onClick_pb3(self):
        self.showWindow2()
        #self.w = Window2()       
        #self.w.show()
        self.hide()
    def showWindow2(self):
        self.mdiwindow = Window2()
        self.mdiwindow.show()
    def onClick_pb4(self):
        self.quit 
        self.close()    
          
if __name__ == "__main__":       
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        #title_label {
            font-size: 50px;
            color: #F0B21A;
        }
        #desc_label {
            font-size: 15px;
            color: #F0B21A;
        }
        #loading_label {
            font-size: 20px;
            color: #F0B21A;
        }
        QFrame {
            background-color: #2F339B;
            color: #c8c8c8;
        }
        QProgressBar {
            background-color: #000000;
            color: #9B2F6A;
            border-style: none;
            border-radius: 5px;
            text-align: center;
            font-size: 25px;
        }
        QProgressBar::chunk {
            border-radius: 7px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #E1F01A);
        }
    ''')
    splash = WindowApp()
    splash.show()
    sys.exit(app.exec())