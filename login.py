from imports import *
from mainw import Window2

TIME_LIMIT = 100
class WindowApp(a.QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(320, 245)
        self.quit = g.QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)
        self.move(400, 200) 
        lblusr =  a.QLabel('UserName', self)
        lblusr.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblusr.setGeometry(25, 55, 100, 30) 
        txtusr = a.QLineEdit('', self) 
        txtusr.setGeometry(100, 55, 150, 30)  
        lblpwd =  a.QLabel('Password', self)
        lblpwd.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblpwd.setGeometry(25, 100, 100, 30) 
        txtpwd = a.QLineEdit('', self) 
        txtusr.setPlaceholderText("Enter Username Here")
        txtpwd.setPlaceholderText("Enter Password Here")
        txtpwd.setGeometry(100, 100, 150, 30) 
        txtpwd.setEchoMode(a.QLineEdit.EchoMode.Password)        
        pblogin = a.QPushButton('Login', self)
        pblogin.setGeometry(100, 165, 65, 25)
        pblogin.clicked.connect(self.onClick_pb3)  
        pbcanc = a.QPushButton('Cancel', self)
        pbcanc.setGeometry(180, 165, 65, 25)
        pbcanc.clicked.connect(self.onClick_pb4)  
        self.statusBar = a.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready", 5000)        
        #self.show()
        
        self.progressBar = a.QProgressBar()
        self.progressBar.setStyleSheet("""QProgressBar {
            background-color: transparent;
            color: #9B2F6A;
            border-style: none;
            border-radius: 5px;
            text-align: center;
            font-size: 10px;
        }
        QProgressBar::chunk {
            border-radius: 5px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #E1F01A);
        }""")
        self.statusBar.addPermanentWidget(self.progressBar)
        self.progressBar.move(30, 40)
        self.progressBar.setFixedSize(120, 20)
        #self.progressBar.setValue(100)
    def closeEvent(self, event):
        close = a.QMessageBox()
        close.setIcon(a.QMessageBox.Icon.Question)
        close.setWindowTitle('Pls confirm')
        close.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        close.setText("Do you really want to quit?")
        close.setStandardButtons(a.QMessageBox.StandardButton.Yes | a.QMessageBox.StandardButton.Cancel)
        close = close.exec()

        if close == a.QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    def onClick_pb3(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            t.sleep(0.01)
            self.progressBar.setValue(count)
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
    app = a.QApplication(s.argv)
    app.setStyleSheet('''        
        QProgressBar {
            background-color: #000000;
            color: #9B2F6A;
            border-style: none;
            border-radius: 4px;
            text-align: center;
            font-size: 10px;
        }
        QProgressBar::chunk {
            border-radius: 4px;
            background-color: qlineargradient(spread:pad x1:0, x2:1, y1:0.511364, y2:0.523, stop:0 #E1F01A);
        }
    ''')
    splash = WindowApp()
    splash.show()
    s.exit(app.exec())