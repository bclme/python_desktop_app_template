
import mainw 
import subprocess
import importlib
import sys
import os
from PyQt6.QtWidgets import QApplication,  QWidget, QPushButton, QTextEdit, QRadioButton, QButtonGroup
from PyQt6.QtGui import QFont
class Window_dev(QWidget):

    def __init__(self):
        super(Window_dev, self).__init__()

        self.initUI()

    def initUI(self):
 
        
        pb1 = QPushButton('Check Syntax', self)
        pb1.setGeometry(110, 5, 100, 30)        
        pb1.clicked.connect(self.onClick_pb1)
        pb2 = QPushButton('Recompile', self)
        pb2.setGeometry(5, 5, 100, 30)        
        pb2.clicked.connect(self.onClick_pb2)
        self.stext = QTextEdit(self)          
        self.stext.setGeometry(5, 450, 890, 40)
        self.stext.setStyleSheet('QTextEdit {background-color: white; color: black;}')
        
        
        self.etext = QTextEdit(self)      
        self.etext.setGeometry(5, 40, 890, 400)
        self.etext.setStyleSheet('QTextEdit {background-color: white; color: black;}')
        new_font = QFont("Courier", 9)
        self.etext.setFont(new_font)
        text=open('mainw.py').read()
        self.etext.setPlainText(text)
        #self.etext.setLineWrapColumnOrWidth(256)
        self.etext.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
        self.setGeometry(25, 45, 900, 500)
        self.setWindowTitle('System IDE')
        self.show()
        
    def onClick_pb1(self):
          otext=self.etext.toPlainText()
          with open('mainw_tmp.py', 'w') as ff:
            ff.write(otext)    
          cmdCommand = "python -m py_compile mainw_tmp.py"   #specify your cmd command
          process = subprocess.getoutput(cmdCommand.split())                  
          self.stext.setPlainText(process)
           
    def onClick_pb2(self):
          otext=self.etext.toPlainText()
          with open('mainw_tmp.py', 'w') as ff:
            ff.write(otext)    
          cmdCommand = "python -m py_compile mainw_tmp.py"   #specify your cmd command
          process = subprocess.getoutput(cmdCommand.split())
          self.stext.setPlainText(process)          
          if process == '':       
             otext=self.etext.toPlainText()
             with open('mainw.py', 'w') as ff:
                 ff.write(otext)
             importlib.reload(mainw)
             self.mdiwindow = mainw.Window2()
             self.mdiwindow.show()
   


    
def onClick_pb1():
    exit()

def main():

    app = QApplication(sys.argv)
    ex = Window_dev()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()