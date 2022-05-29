from imports import *
from splash import SplashScreen
class App(a.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle("")
        self.do_logging()
        self.setFixedSize(0, 0)
        self.hide()
        t.sleep(1)
        self.splash1 = SplashScreen()
        self.splash1.show() 
    def do_logging(self):
        print("Do something here...")
 
        
def main():

    app = a.QApplication(s.argv)
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
    ''')
    ex = App()
    s.exit(app.exec())


if __name__ == '__main__':
    main()