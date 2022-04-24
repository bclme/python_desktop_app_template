from PyQt6.QtWidgets import * 
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6 import QtCore, QtGui, QtWidgets, uic
import sys
import time
class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0), color1=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setBackground(color1)
        self.setFont(fnt)
        self.setText(txt)
class Window2(QMainWindow):                          
    count = 0
    def __init__(self):
        super().__init__()
        self.quit = QAction("Quit", self)
        self.quit.triggered.connect(self.closeEvent)
        self.mdi = QMdiArea()
        self.treeView = QTreeView()
        self.treeView.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
        america = StandardItem('Accounting', 12, set_bold=True, color1=QColor('#4d88ff'))

        california = StandardItem(' Accounts Payable', 10, color1=QColor('#80aaff'))
        america.appendRow(california)

        oakland = StandardItem('   Vendors', 8, color=QColor('#3939ac'), color1=QColor('#b3ccff'))
        sanfrancisco = StandardItem('   Incoming Invoice', 8, color=QColor('#3939ac'), color1=QColor('#b3ccff'))
        sanjose = StandardItem('   Purchases', 8, color=QColor('#3939ac'), color1=QColor('#b3ccff'))

        california.appendRow(oakland)
        california.appendRow(sanfrancisco)
        california.appendRow(sanjose)


        texas = StandardItem(' Accounts Receivable', 10, color1=QColor('#80aaff'))
        america.appendRow(texas)

        austin = StandardItem('   Customers', 8, color=QColor('#3939ac'), color1=QColor('#b3ccff'))
        houston = StandardItem('   Outbound Invoices', 8, color=QColor('#3939ac'), color1=QColor('#b3ccff'))
        cali = StandardItem('   Dunning', 8, color=QColor('#3939ac'), color1=QColor('#b3ccff'))
        dallas = StandardItem('   Sales', 8, color=QColor('#3939ac'), color1=QColor('#b3ccff'))

        texas.appendRow(austin)
        texas.appendRow(houston)
        texas.appendRow(cali)
        texas.appendRow(dallas)


        # Canada 
        canada = StandardItem('Logistics', 12, set_bold=True, color1=QColor('#4d88ff'))

        alberta = StandardItem(' Inventory', 10, color1=QColor('#80aaff'))
        bc = StandardItem(' Materials', 10, color1=QColor('#80aaff'))
        ontario = StandardItem(' Deliveries', 10, color1=QColor('#80aaff'))
        canada.appendRows([alberta, bc, ontario])


        rootNode.appendRow(america)
        rootNode.appendRow(canada)

        self.treeView.setModel(treeModel)
        self.treeView.expandAll()
        self.treeView.doubleClicked.connect(self.getValue)
        self.treeView.setIndentation(0)
        self.treeView.setAlternatingRowColors(True)
        self.treeView.setFixedSize(160,self.height()-25)
        self.setCentralWidget(QWidget(self))
        windowLayout = QHBoxLayout(self)
        windowLayout.addWidget(self.treeView, alignment=Qt.AlignmentFlag.AlignTop)
        windowLayout.addWidget(self.mdi, alignment=Qt.AlignmentFlag.AlignTop)
        self.centralWidget().setLayout(windowLayout)
        #self.setCentralWidget(self.mdi)
        
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
        self.setGeometry(125,75,850,350)
        #windowLayout = QVBoxLayout(self)
        #windowLayout.addWidget(self.mdi, alignment=Qt.AlignmentFlag.AlignTop)
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
    def getValue(self, val):
        print(val.data())
        print(val.row())
        print(val.column())
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
    splash = Window2()
    splash.show()
    sys.exit(app.exec())