from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtCore, QtGui, QtWidgets, uic
import sys
import time
class SplashScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 350)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.counter = 0
        self.n = 100 
        self.initUI()
        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)
    def initUI(self):
        # layout to display splash scrren frame
        layout = QVBoxLayout()
        self.setLayout(layout)
        # splash screen frame
        self.frame = QFrame()
        layout.addWidget(self.frame)
        # splash screen title
        self.title_label = QLabel(self.frame)
        self.title_label.setObjectName('title_label')
        self.title_label.resize(690, 120)
        self.title_label.move(0, 5) # x, y
        self.title_label.setText('Your World Famous App')
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # splash screen title description
        self.description_label = QLabel(self.frame)
        self.description_label.resize(690, 40)
        self.description_label.move(0, self.title_label.height())
        self.description_label.setObjectName('desc_label')
        self.description_label.setText('<b>We build the systems and the apps.</b>')
        self.description_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # splash screen pogressbar
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, 180) # self.description_label.y()+130
        self.progressBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)
        # spash screen loading label
        self.loading_label = QLabel(self.frame)
        self.loading_label.resize(self.width() - 10, 50)
        self.loading_label.move(0, self.progressBar.y() + 70)
        self.loading_label.setObjectName('loading_label')
        self.loading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loading_label.setText('Loading...')
    def loading(self):
        # set progressbar value
        self.progressBar.setValue(self.counter)
        # stop progress if counter
        # is greater than n and
        # display main window app
        if self.counter >= self.n:
            self.timer.stop()
            self.close()
            time.sleep(1)
            self.WindowApp = WindowApp()
            self.WindowApp.show()
        self.counter += 1
class WindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(320, 245)
        self.move(400, 200) 
        self.quit = QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)
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
        self.w = Window2()       
        self.w.show()
        self.hide()
    def onClick_pb4(self):
        self.quit 
        self.close()      
class Window2(QMainWindow):                          
    count = 0
    def __init__(self):
        super().__init__()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.quit = QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)
        self.toolbar = QToolBar("Documents")
        self.toolbar.setMovable(False)
        toolbar1 = QToolBar("Messages")
        self.toolbar.setIconSize(QSize(30,30))
        toolbar1.setIconSize(QSize(30,30))
        self.addToolBar(self.toolbar)
        
        self.new_action = QAction(QIcon(r"c:\crud\icons\document--plus.png"), "&New", self)
        self.new_action.setStatusTip("New Document")
        self.new_action.triggered.connect(self.onNewClick)
        #button_action.setCheckable(True)
        self.new_action.setShortcut(QKeySequence("Ctrl+p"))
      
        chg_action = QAction(QIcon(r"c:\crud\icons\document--pencil.png"), "&Change", self)
        chg_action.setStatusTip("Change Document")
        chg_action.triggered.connect(self.onClick)
        chg_action.setCheckable(True)
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(chg_action)       
        
        self.addToolBar(toolbar1)
        inbox_action = QAction(QIcon(r"c:\crud\icons\inbox--plus.png"), "&Add Message", self)
        inbox_action.setStatusTip("Add Message")
        inbox_action.triggered.connect(self.onClick)
        inbox_action.setCheckable(True)
        inbox_action.setShortcut(QKeySequence("Ctrl+m"))
        inbox_action1 = QAction(QIcon(r"c:\crud\icons\inbox--minus.png"), "&Remove Message", self)
        inbox_action1.setStatusTip("Remove Message")
        inbox_action1.triggered.connect(self.onClick)
        inbox_action1.setCheckable(True)
        inbox_action1.setShortcut(QKeySequence("Ctrl+n"))
        exit_action = QAction(QIcon(r"c:\crud\icons\door-open-out.png"), "&Exit", self)
        exit_action.setStatusTip("Exit")
        exit_action.triggered.connect(self.onExitClick)
        exit_action.setShortcut(QKeySequence("Ctrl+x"))
        toolbar1.addAction(inbox_action)
        toolbar1.addAction(inbox_action1)
        
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        self.statusBar.showMessage("Ready", 3000)
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(self.new_action)
        file_menu.addAction(chg_action)
        file_menu.addSeparator()
        file_submenu = file_menu.addMenu("Messages")
        file_submenu.addAction(inbox_action)
        file_submenu.addAction(inbox_action1)
        file_menu.addSeparator()
        file_menu.addAction(exit_action)
        bar = self.menuBar()
		
        file = bar.addMenu("Window")
        file.addAction("Cascade")
        file.addAction("Tile")
        file.triggered[QAction].connect(self.click)
        
        tb = bar.addMenu("Toolbar")
        tb.addAction("Hide Documents Toolbar")
        tb.addAction("Unhide Documents Toolbar")
        tb.triggered[QAction].connect(self.click)
        
        tb1 = bar.addMenu("System")
        tb1.addAction("About This Template")
        tb1.triggered[QAction].connect(self.about)
        
        self.setWindowTitle("The App System")
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
    def contextMenuEvent(self, event):
        menu = QMenu(self)
        menu.addAction(self.new_action)
        menu.exec(event.globalPos())        
    def onClick(self, s):
        print("click",s) 
    def onExitClick(self, s):
        self.quit 
        self.close() 
    def about(self, s):
        aboutm = QMessageBox()
        aboutm.setIcon(QMessageBox.Icon.Information)
        aboutm.setWindowTitle('Software Information')
        aboutm.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        aboutm.setText("Title: Simple App Template \n Version: 1.00 \n Release Date: April 19, 2022")
        aboutm.setStandardButtons(QMessageBox.StandardButton.Ok)
        aboutm = aboutm.exec()         
    def onNewClick(self, s):       
        Window2.count = Window2.count+1
        sub = QMdiSubWindow()
        lbl1a =  QLabel('RECS', sub)
        lbl1a.setGeometry(25, 75, 50, 35)
        lbl1a.setStyleSheet('QLabel {background-color: #0E95A6; color: #d4d4d4;}')
        lbl1a.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub.setGeometry(25, 25, 200, 200)
        sub.setWindowTitle("subwindow"+str(Window2.count))
        self.mdi.addSubWindow(sub)
        sub.show()
    def click(self, q):                  
        if q.text() == "Cascade":
          self.mdi.cascadeSubWindows()
                    
        if q.text() == "Tile":
          self.mdi.tileSubWindows() 
          
        if q.text() == "Hide Documents Toolbar":
          self.toolbar.toggleViewAction().setChecked(True)
          self.toolbar.toggleViewAction().trigger() 
        if q.text() == "Unhide Documents Toolbar":
          self.toolbar.toggleViewAction().setChecked(False)
          self.toolbar.toggleViewAction().trigger()          
       
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
splash = SplashScreen()
splash.show()
sys.exit(app.exec())