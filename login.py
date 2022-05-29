from imports import *
import mysql.connector as mysql
import hashlib
import hmac

from mainw import Window2
import config
import functions


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
        self.txtusr = a.QLineEdit('', self) 
        
        self.txtusr.setGeometry(100, 55, 150, 30)  
        lblpwd =  a.QLabel('Password', self)
        lblpwd.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblpwd.setGeometry(25, 100, 100, 30) 
        self.txtpwd = a.QLineEdit('', self) 
        self.txtusr.setPlaceholderText("Enter Username Here")
        self.txtpwd.setPlaceholderText("Enter Password Here")
        self.txtpwd.setGeometry(100, 100, 150, 30) 
        self.txtpwd.setEchoMode(a.QLineEdit.EchoMode.Password)        
        self.pblogin = a.QPushButton('Login', self)
        self.pblogin.setEnabled(False)
        self.pblogin.setGeometry(100, 165, 65, 25)
        self.pblogin.clicked.connect(self.onClick_pb3)  
        self.txtpwd.textChanged.connect(self.on_text_changed)
        self.txtusr.textChanged.connect(self.on_text_changed)
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
    def on_text_changed(self):
        self.pblogin.setEnabled(bool(self.txtusr.text()) and bool(self.txtpwd.text()))
        
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
        db = mysql.connect(
             host = config.host,
             user = config.user,
             passwd = config.passwd,
             database = config.database
        )
        cursor = db.cursor()
        t1 = self.txtusr.text()
        t2 = self.txtpwd.text() # Appl3Tr33.456
        #salt = b'4\xa8y\x8e\xca\xfb\x7f\x8e\xd5\x97v\x14\xc7[Z\xd0'
        print(t2)
        t2 = hashlib.pbkdf2_hmac("sha256", t2.encode(), config.salt, 100000)
        
        t1 = repr(str(t1))
        t2 = repr(str(t2))
        print(t2)
        query = "SELECT * FROM tbusr where username = %s and userpassword  = %s" %(t1, t2)
        cursor.execute(query)
        records = cursor.fetchall()
        df = pd.DataFrame(records) 
        count = 0
        while count < TIME_LIMIT:
            count += 1
            t.sleep(0.01)
            self.progressBar.setValue(count)
        if df.empty:    
            self.statusBar.showMessage("User not found!", 5000)
            self.txtusr.setStyleSheet('QLineEdit {background-color: #ffe6e6; color: black;}')
            self.txtusr.repaint()
            t.sleep(2.5)  
            self.txtusr.setStyleSheet('QLineEdit {background-color: white; color: black;}')
            self.progressBar.setValue(0)
            self.txtusr.repaint()
        else:
            gb_usr = self.txtusr.text()
            functions.update_usr(gb_usr)
            self.statusBar.showMessage("User found!", 5000)
            self.statusBar.repaint()
            t.sleep(2)
            self.showWindow2()
            
            self.hide()
            
        #self.w = Window2()       
        #self.w.show()
        
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