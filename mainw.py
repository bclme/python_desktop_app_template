from imports import *
from login import *
import mysql.connector as mysql
import config
import functions
import pdb
x_init = 0
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
        
        self.setCentralWidget(a.QWidget(self))
        windowLayout = a.QHBoxLayout(self)
        windowLayout.addWidget(self.treeView,  )
        windowLayout.addWidget(self.mdi, alignment=f.Qt.AlignmentFlag.AlignTop)
        self.centralWidget().setLayout(windowLayout)
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
        bar = self.menuBar()
		
        file = bar.addMenu("Window")
        file.addAction("Cascade")
        file.addAction("Tile")
        file.triggered[g.QAction].connect(self.click)
        
        tb = bar.addMenu("Toolbar")
        tb.addAction("Hide Documents Toolbar")
        tb.addAction("Unhide Documents Toolbar")
        tb.triggered[g.QAction].connect(self.click)
        tb1 = bar.addMenu("System")
        tb1.addAction("About This Template")
        tb1.triggered[g.QAction].connect(self.about)
        self.setGeometry(125,75,850,350)
        #windowLayout = QVBoxLayout(self)
        #windowLayout.addWidget(self.mdi, alignment=Qt.AlignmentFlag.AlignTop)
        self.setWindowTitle("The App System") 
    def showTime(self):
  
        # getting current time
        current_time = f.QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
  
        # showing it to the label
        self.lbl_tmr.setText(label_time)
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
        #Accounts_Payable = StandardItem(' Accounts Payable', 10, color1=g.QColor('#80aaff'))
        #accnt.appendRow(Accounts_Payable)
        #Vendors = StandardItem('   Vendors', 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))
        #Incoming_Invoice = StandardItem('   Incoming Invoice', 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))
        #Purchases = StandardItem('   Purchases', 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))

        #Accounts_Payable.appendRow(Vendors)
        #Accounts_Payable.appendRow(Incoming_Invoice)
        #Accounts_Payable.appendRow(Purchases)


        #texas = StandardItem(' Accounts Receivable', 10, color1=g.QColor('#80aaff'))
        #accnt.appendRow(texas)

        #austin = StandardItem('   Customers', 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))
        #houston = StandardItem('   Outbound Invoices', 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))
        #cali = StandardItem('   Dunning', 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))
        #dallas = StandardItem('   Sales', 8, color=g.QColor('#3939ac'), color1=g.QColor('#b3ccff'))

        #texas.appendRow(austin)
        #texas.appendRow(houston)
        #texas.appendRow(cali)
        #texas.appendRow(dallas)


        # Canada 
        #canada = StandardItem('Logistics', 12, set_bold=True, color1=g.QColor('#4d88ff'))

        #alberta = StandardItem(' Inventory', 10, color1=g.QColor('#80aaff'))
        #bc = StandardItem(' Materials', 10, color1=g.QColor('#80aaff'))
        #ontario = StandardItem(' Deliveries', 10, color1=g.QColor('#80aaff'))
        #canada.appendRows([alberta, bc, ontario])


        #rootNode.appendRow(accnt)
        #rootNode.appendRow(canada)

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
        else:
            event.ignore()
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
if __name__ == "__main__":       
    app = a.QApplication(s.argv)
 
    splash = Window2()
    splash.show()
    s.exit(app.exec())