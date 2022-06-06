import config
import functions
import pandas as pd
import re
for ind in config.df_imports.index:      
      exec(config.df_imports[0][ind])
from login import *
import importlib

import mysql.connector as mysql

import pdb
import warnings
warnings.filterwarnings('ignore')
x_init = 0
sel_row = 0
class StandardItem(g.QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=g.QColor(0, 0, 0), color1=g.QColor(0, 0, 0)):
        super().__init__()

        fnt = g.QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setBackground(color1)
        self.setFont(fnt)
        self.setText(txt)
class MdiSubWindow(a.QMdiSubWindow):
    sigClosed = f.pyqtSignal(str)
    def closeEvent(self, event):
        self.sigClosed.emit(self.windowTitle())
        a.QMdiSubWindow.closeEvent(self, event)
class Window2(a.QMainWindow):                          
    count = 0
    def __init__(self):
        super().__init__()
        self.installEventFilter(self)
        self.quit = g.QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)
        self.mdi = a.QMdiArea()
        self.treeView = a.QTreeView()
        self.define_tree(self.treeView)
        widget = a.QWidget()
        self.setCentralWidget(widget)
        #self.setCentralWidget(a.QWidget(self))
        windowLayout = a.QHBoxLayout(widget)
        windowLayout.addWidget(self.treeView,  )
        windowLayout.addWidget(self.mdi, alignment=f.Qt.AlignmentFlag.AlignTop)
        #widget.setLayout(windowLayout)
        
        #self.centralWidget().setLayout(windowLayout)
        #self.setCentralWidget(self.mdi)
        
        self.toolbar = a.QToolBar("Documents")
        self.toolbar.setMovable(False)
        toolbar1 = a.QToolBar("Messages")
        self.toolbar.setIconSize(f.QSize(30,30))
        toolbar1.setIconSize(f.QSize(30,30))
        self.addToolBar(self.toolbar)
        
        self.new_action = g.QAction(g.QIcon(r"c:\crud\icons\document--plus.png"), "&New", self)
        self.new_action.setStatusTip("New Document")
        self.new_action.triggered.connect(self.onNewClick)
        #button_action.setCheckable(True)
        self.new_action.setShortcut(g.QKeySequence("Ctrl+p"))
      
        chg_action = g.QAction(g.QIcon(r"c:\crud\icons\document--pencil.png"), "&Change", self)
        chg_action.setStatusTip("Change Document")
        chg_action.triggered.connect(self.onClick)
        chg_action.setCheckable(True)
        self.toolbar.addAction(self.new_action)
        self.toolbar.addAction(chg_action)       
        
        self.addToolBar(toolbar1)
        inbox_action = g.QAction(g.QIcon(r"c:\crud\icons\inbox--plus.png"), "&Add Message", self)
        inbox_action.setStatusTip("Add Message")
        inbox_action.triggered.connect(self.onClick)
        inbox_action.setCheckable(True)
        inbox_action.setShortcut(g.QKeySequence("Ctrl+m"))
        inbox_action1 = g.QAction(g.QIcon(r"c:\crud\icons\inbox--minus.png"), "&Remove Message", self)
        inbox_action1.setStatusTip("Remove Message")
        inbox_action1.triggered.connect(self.onClick)
        inbox_action1.setCheckable(True)
        inbox_action1.setShortcut(g.QKeySequence("Ctrl+n"))
        exit_action = g.QAction(g.QIcon(r"c:\crud\icons\door-open-out.png"), "&Exit", self)
        exit_action.setStatusTip("Exit")
        exit_action.triggered.connect(self.onExitClick)
        exit_action.setShortcut(g.QKeySequence("Ctrl+x"))
        logout_action = g.QAction(g.QIcon(r"c:\crud\icons\door-open-out.png"), "&Logout", self)
        logout_action.setStatusTip("Logout")
        logout_action.triggered.connect(self.onLogoutClick)
        logout_action.setShortcut(g.QKeySequence("Ctrl+l"))
        toolbar1.addAction(inbox_action)
        toolbar1.addAction(inbox_action1)
        
        self.statusBar = a.QStatusBar()
        self.setStatusBar(self.statusBar)
        self.lbl_usr =  a.QLabel(config.gb_usr, self)
        self.lbl_tmr = a.QLabel()
        self.define_statusbar(self.statusBar, self.lbl_usr, self.lbl_tmr)
        timer = f.QTimer(self) 
        # adding action to timer
        timer.timeout.connect(self.showTime)  
        # update the timer every second
        timer.start(1000)                        
        
        
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
        file_menu.addSeparator()
        file_menu.addAction(logout_action)
        bar = self.menuBar()
		
        file = bar.addMenu("Window")
        file.addAction("Cascade")
        file.addAction("Tile")
        file.triggered[g.QAction].connect(self.click)
        
        tb = bar.addMenu("Toolbar")
        tb.addAction("Hide Documents Toolbar")
        tb.addAction("Unhide Documents Toolbar")
        tb.triggered[g.QAction].connect(self.click)
        tb0 = bar.addMenu("Admin")
        tb0_sub = tb0.addMenu("Users")
        tb0_sub.addAction("Create")
        tb0_sub.addAction("Update")
        tb0_sub.addAction("Display")
        tb0_sub.addAction("Delete")
        tb0.addAction("System Messsages")
        tb0.triggered[g.QAction].connect(self.onUserclick)
        tb1 = bar.addMenu("System")
        tb1.addAction("About This Template")
        tb1.triggered[g.QAction].connect(self.about)
        self.setGeometry(125,75,850,350)
        #windowLayout = QVBoxLayout(self)
        #windowLayout.addWidget(self.mdi, alignment=Qt.AlignmentFlag.AlignTop)
        self.setWindowTitle("The App System") 
    def showTime(self):
        global sel_row
        # getting current time
        current_time = f.QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
  
        # showing it to the label
        self.lbl_tmr.setText(label_time)
        if sel_row != 0:
           sel_row = sel_row - 1
           self.sub1.txtnam.setText(config.df[2][sel_row])
           self.sub1.txtemail.setText(config.df[4][sel_row])
           self.sub1.txtusr.setText(config.df[1][sel_row])
           sel_row = 0
           if config.user_crud == 'Delete':
              self.sub1.pbSave.setEnabled(True)
              self.sub1.pbSave.setText(config.user_crud)
    def define_statusbar(self, sbar, slbl, lblt):
        sbar.addPermanentWidget(slbl)
        slbl.move(30, 40)
        sbar.addPermanentWidget(lblt)
        lblt.move(20, 40)
        slbl.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblt.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        sbar.showMessage(("Ready " + config.gb_usr + "!"), 5000)
    def define_tree(self, tree):
        self.treeView.setHeaderHidden(True)
        
        treeModel = g.QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
        db = mysql.connect(
             host = config.host,
             user = config.user,
             passwd = config.passwd,
             database = config.database
        )
        cursor = db.cursor()
        
        query = "SELECT * FROM tbsidebar" 
        cursor.execute(query)
        records = cursor.fetchall()
        df = pd.DataFrame(records)
        for ind in df.index:   
            
            if df[2][ind] == 0:
               #pdb.set_trace()
               if ind != 0:
                  rootNode.appendRow(accnt)
               accnt = df[1][ind]
               accnt1 = df[1][ind]
               accnt = StandardItem(df[3][ind], 12, set_bold=True, color1=g.QColor('#4d88ff'))
            elif df[2][ind] == 1:
               node_name = df[4][ind]
               node_name_1 = df[4][ind]
               if accnt1 == df[1][ind]:
                  node_name = StandardItem((' ' + df[3][ind]), 10, color1=g.QColor('#80aaff'))
                  accnt.appendRow(node_name)
            elif df[2][ind] == 2:
               node_name1 = df[4][ind]
               if df[1][ind] == node_name_1:
                  node_name1 = StandardItem(('   '+ df[3][ind]), 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))
                  node_name.appendRow(node_name1)
        
        rootNode.appendRow(accnt)
        
        tree.setModel(treeModel)
        tree.expandAll()
        tree.doubleClicked.connect(self.getValue)
        tree.setIndentation(0)
        tree.setAlternatingRowColors(True)
        tree.setFixedSize(160,self.height()-25)
        

    def resizeEvent(self, event):
                  
           self.treeView.setFixedSize(160,self.height()-102)
              
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
            if config.logout_ind == True:
               functions.update_logout(False)
               from login import WindowApp
               self.login = WindowApp(self)
               self.login.show()
        else:
            event.ignore()
            functions.update_logout(False)
    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())
    def contextMenuEvent(self, event):
        menu = a.QMenu(self)
        menu.addAction(self.new_action)
        menu.exec(event.globalPos())        
    def onClick(self, s):
        print("click",s) 
    def onExitClick(self, s):
        
        self.quit 
        self.close()
    def onLogoutClick(self, s):
        functions.update_logout(True)
        #self.login = WindowApp(self)
        #self.login.show()

        self.close()        
    def about(self, s):
        aboutm = a.QMessageBox()
        aboutm.setIcon(a.QMessageBox.Icon.Information)
        aboutm.setWindowTitle('Software Information')
        aboutm.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        aboutm.setText("Title: Simple App Template \n Version: 1.00 \n Release Date: April 19, 2022")
        aboutm.setStandardButtons(a.QMessageBox.StandardButton.Ok)
        aboutm = aboutm.exec()         
    def onNewClick(self, s):       
        Window2.count = Window2.count+1
        sub = a.QMdiSubWindow()
        lbl1a =  a.QLabel('RECS', sub)
        lbl1a.setGeometry(25, 75, 50, 35)
        lbl1a.setStyleSheet('QLabel {background-color: #0E95A6; color: #d4d4d4;}')
        lbl1a.setAlignment(f.Qt.AlignmentFlag.AlignCenter)
        sub.setGeometry(25, 25, 200, 200)
        sub.setWindowTitle("subwindow"+str(Window2.count))
        self.mdi.addSubWindow(sub)
        sub.show()
    def on_text_changed(self):
        if config.user_crud != 'Delete': 
         self.sub1.pbSave.setEnabled(bool(self.sub1.txtusr.text()) and bool(self.sub1.txtnam.text()) and bool(self.sub1.txtipwd.text()))
    def on_click_usr_save(self):
        
        usr_regex = re.search("^(?![-._])(?!.*[_.-]{2})[\w.-]{6,30}(?<![-._])$", self.sub1.txtusr.text())
        if not usr_regex: 
           #print(pwd_regex)
           self.statusBar.showMessage(("Wrong User Name Required Format"), 5000)
           return None
        pwd_regex = re.search("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$", self.sub1.txtipwd.text())
        if not pwd_regex and config.user_crud == 'Create': 
           #print(pwd_regex)
           self.statusBar.showMessage(("Wrong Password Required Format"), 5000)
           return None
        email_regex = re.search("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", self.sub1.txtemail.text())
        if not email_regex: 
           #print(pwd_regex)
           self.statusBar.showMessage(("Wrong Email Format"), 5000)
           return None
        t1 = self.sub1.txtusr.text()   
        t2 = self.sub1.txtipwd.text()
        t2 = hashlib.pbkdf2_hmac("sha256", t2.encode(), config.salt, 100000)
        #print(t2)
        #t2 = repr(str(t2))
        t2 =  str(t2)
        #print(t2)
        #t1 = repr(str(t1))
        try:   
           db = mysql.connect(
             host = config.host,
             user = config.user,
             passwd = config.passwd,
             database = config.database
           )
           cursor = db.cursor()
        
        
           if config.user_crud == 'Create':
             sql = "INSERT INTO tbusr (username, Uname, userpassword, UEmail, USRGRP) VALUES (%s, %s, %s, %s, %s)"
             val = (t1, self.sub1.txtnam.text(), t2, self.sub1.txtemail.text(), 'USER')
             cursor.execute(sql, val)
           elif config.user_crud == 'Update':
             #t1 = repr(str(t1))
             sql = "UPDATE tbusr SET Uname = %s, UEmail = %s WHERE username = %s"
             val = (self.sub1.txtnam.text(), self.sub1.txtemail.text(), t1)
             cursor.execute(sql, val)
           elif config.user_crud == 'Delete':             
             sql = "DELETE FROM tbusr WHERE username = %s"
             val = (t1,)
             cursor.execute(sql, val)
           db.commit()
        except mysql.Error as e:
            print(str(e))
            self.statusBar.showMessage(str(e), 5000)
            return None
            
        if config.user_crud == 'Create':
          self.statusBar.showMessage(("User has been created!"), 5000)
        elif config.user_crud == 'Update':
          self.statusBar.showMessage(("User has been updated!"), 5000)
        elif config.user_crud == 'Delete': 
          self.statusBar.showMessage(("User has been deleted!"), 5000)        
        self.sub1.close()
    def on_click_canc(self):
        self.sub1.close()
    def on_click_Srch(self):
        
        self.buildSearchPopup()
    def buildSearchPopup(self):
        name = 'Lock Screen'
        self.exPopup = searchPopup(name)
        
        #self.exPopup.setGeometry(self.pos().x()+50, self.pos().y()+75, 300, 225)
        self.exPopup.move(self.pos().x()+75, self.pos().y()+75)
        self.exPopup.setFixedSize(350, 400)
        self.exPopup.show()

    def onUserclick(self, q): 
        if config.sub_open == True:
           return True
        functions.update_w_open(True)
        self.sub1 = MdiSubWindow()#a.QMdiSubWindow()
        lbl1a =  a.QLabel('Username', self.sub1)
        lbl1a.setGeometry(25, 50, 60, 25)
        lbl1a.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        self.sub1.txtusr = a.QLineEdit('', self.sub1) 
        self.sub1.txtusr.setGeometry(95, 50, 150, 25)
        
        if q.text() != "Create":
           
           
           pbSrch = a.QPushButton('...', self.sub1)
           pbSrch.setGeometry(250, 50, 30, 25)
           pbSrch.clicked.connect(self.on_click_Srch)
          
        lbl1b =  a.QLabel('Name', self.sub1) 
        lbl1b.setGeometry(25, 85, 60, 25)
        lbl1b.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        self.sub1.txtnam = a.QLineEdit('', self.sub1) 
        self.sub1.txtnam.setGeometry(95, 85, 200, 25)
        lbl1c =  a.QLabel('User Group', self.sub1)
        lbl1c.setGeometry(25, 120, 60, 25)
        lbl1c.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        txtgrp = a.QLineEdit('USER', self.sub1) 
        txtgrp.setGeometry(95, 120, 100, 25)
        txtgrp.setEnabled(False)
        lbl1d =  a.QLabel('Password', self.sub1)
        lbl1d.setGeometry(25, 155, 60, 25)
        lbl1d.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        self.sub1.txtipwd = a.QLineEdit('', self.sub1) 
        self.sub1.txtipwd.setGeometry(95, 155, 200, 25)
        self.sub1.txtipwd.setEchoMode(a.QLineEdit.EchoMode.Password)
        lbl1e =  a.QLabel('Email', self.sub1)
        lbl1e.setGeometry(25, 190, 60, 25)
        lbl1e.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        self.sub1.txtemail = a.QLineEdit('', self.sub1) 
        self.sub1.txtemail.setGeometry(95, 190, 200, 25)

        self.sub1.pbSave = a.QPushButton('Save', self.sub1)
        self.sub1.pbSave.setGeometry(205, 260, 75, 25)
        self.sub1.pbSave.setEnabled(False)
        self.sub1.pbSave.clicked.connect(self.on_click_usr_save)
        self.sub1.txtusr.textChanged.connect(self.on_text_changed)
        self.sub1.txtnam.textChanged.connect(self.on_text_changed)
        self.sub1.txtipwd.textChanged.connect(self.on_text_changed)
        pbCanc = a.QPushButton('Cancel', self.sub1)
        pbCanc.setGeometry(290, 260, 75, 25)
        pbCanc.clicked.connect(self.on_click_canc)
        if q.text() == "Display":
           functions.update_user_crud("Display")
           self.sub1.txtipwd.setEnabled(False)
           self.sub1.txtnam.setEnabled(False)
           self.sub1.txtemail.setEnabled(False)
           self.sub1.setWindowTitle("Display User")
        if q.text() == "Update":
           functions.update_user_crud("Update")
           self.sub1.txtipwd.setEnabled(False)
           self.sub1.txtipwd.setText('*')
           self.sub1.setWindowTitle("Update User")
        if q.text() == "Create":
           self.sub1.setWindowTitle("Create User")
           functions.update_user_crud("Create")
        if q.text() == "Delete":
           functions.update_user_crud("Delete")
           self.sub1.txtipwd.setEnabled(False)
           self.sub1.txtnam.setEnabled(False)
           self.sub1.txtemail.setEnabled(False)
           self.sub1.setWindowTitle("Delete User")
            
        self.sub1.setGeometry(25, 25, 400, 300)
        self.sub1.sigClosed.connect(self.windowclosed)
        self.mdi.addSubWindow(self.sub1)
        self.sub1.show()  
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
          
    #@f.pyqtSlot(str)
    def windowclosed(self, text):
        print(text)
        functions.update_w_open(False)
        
class searchPopup(a.QMainWindow):
    def __init__(self, name):
        super().__init__()        
        self.name = name
        #self.setGeometry(100, 100, 300, 350)
        self.setWindowFlags(f.Qt.WindowType.Window | f.Qt.WindowType.CustomizeWindowHint | f.Qt.WindowType.WindowStaysOnTopHint)
        self.initUI()

    def initUI(self):
        
        lblName = a.QLabel('Search Existing Users', self)
        lblName.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblName.setGeometry(5, 5, 200, 30)
        lblpwd =  a.QLabel('Username', self)
        lblpwd.setStyleSheet('QLabel {background-color: transparent; color: black;}')
        lblpwd.setGeometry(25, 50, 100, 30) 
        txtpwd = a.QLineEdit('', self) 
        txtpwd.setGeometry(110, 50, 150, 30) 
        self.createTable()
        
        pb4 = a.QPushButton('Ok', self)
        pb4.setGeometry(140, 365, 70, 25)
        
        pb4.clicked.connect(self.onClick_pb4)
        pb5 = a.QPushButton('Cancel', self)
        pb5.setGeometry(215, 365, 70, 25)
        pb5.clicked.connect(self.onClick_pb4)
        
  
    def onClick_pb4(self):
                
        self.close()
    def createTable(self):
          self.tableWidget = a.QTableWidget(self)
          self.tableWidget.viewport().installEventFilter(self)
          #self.tableWidget.installEventFilter(self)
          #self.tableWidget.setEditTriggers(QTreeView.NoEditTriggers) 
          self.tableWidget.setRowCount(24)
          self.tableWidget.setColumnCount(2)
          self.tableWidget.setFixedSize(280, 270)
          self.tableWidget.move(25, 85)
          self.tableWidget.setSelectionMode(a.QAbstractItemView.SelectionMode.SingleSelection)
          self.tableWidget.SelectionBehavior(a.QAbstractItemView.SelectionBehavior.SelectRows)
          stylesheet = "::section{Background-color:rgb(179, 179, 179);color: white; bor  der-radius:14px;}"
          self.tableWidget.horizontalHeader().setStyleSheet(stylesheet)
          self.tableWidget.setStyleSheet('QTableWidget {background-color: white; color: black;}')
          delegate = Delegate(self.tableWidget)
          self.tableWidget.setItemDelegate(delegate)
          #text = '100'
          #it = a.QTableWidgetItem(text)
          #self.tableWidget.setItem(3, 1, it)        
          try:
            db = mysql.connect(
              host = config.host,
              user = config.user,
              passwd = config.passwd,
              database = config.database,
              raise_on_warnings= True
            )
            cursor = db.cursor()                           
            query = "SELECT * FROM tbusr "                  
            cursor.execute(query)
            records = cursor.fetchall()
            functions.update_df(records)
            for ind in config.df.index:
               
               v =  config.df[1][ind]
               it = a.QTableWidgetItem(v)
               self.tableWidget.setItem(ind, 0, it)
               
               vv =  config.df[2][ind]
               it = a.QTableWidgetItem(vv)
               self.tableWidget.setItem(ind, 1, it)
          except mysql.Error as e:
            self.statusBar.showMessage("Error in MySql check connection", 5000)
            
        
        
          
          
          self.tableWidget.setHorizontalHeaderLabels(['User', 'Name'])
          self.tableWidget.horizontalHeader().setStretchLastSection(True)
          self.tableWidget.verticalHeader().setStretchLastSection(True)
        
    def eventFilter(self, source, event):
          global sel_row
          #if self.tableWidget.selectedIndexes() != []:
            
          if event.type() == f.QEvent.Type.MouseButtonDblClick:
                #if event.button() == QtCore.Qt.LeftButton:
            row = self.tableWidget.currentRow()
            col = self.tableWidget.currentColumn()
            if self.tableWidget.item(row, col) is not None:
                print(str(row) + " " + str(col) + " " + self.tableWidget.item(row, col).text())
                sel_row = row + 1
                #self.sub1.txtipwd.setText(config.df[row])
                #Window2.mdi.sub1.txtnam.setText(config.df[row])
                #Window2.mdi.sub1.txtemail.setText(config.df[row])
                #Window2.mdi.sub1.txtusr.setText(config.df[row])
                #Window2.mdi.tileSubWindows()
                self.close()
          return f.QObject.event(source, event)    
  
class Delegate(a.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        if index.data() == "100":
            return super(Delegate, self).createEditor(parent, option, index)
            
 
        
if __name__ == "__main__":       
    app = a.QApplication(s.argv)
 
    splash = Window2()
    splash.show()
    s.exit(app.exec())