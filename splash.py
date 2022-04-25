from imports import *
from login import WindowApp
class SplashScreen(a.QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setFixedSize(700, 350)
        self.setWindowFlag(f.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(f.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.counter = 0
        self.n = 100 
        self.initUI()
        self.timer = f.QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(30)
    def initUI(self):
        # layout to display splash scrren frame
        layout = a.QVBoxLayout()
        self.setLayout(layout)
        # splash screen frame
        self.frame = a.QFrame()
        layout.addWidget(self.frame)
        # splash screen title
        self.title_label = a.QLabel(self.frame)
        self.title_label.setObjectName('title_label')
        self.title_label.resize(690, 120)
        self.title_label.move(0, 5) # x, y
        self.title_label.setText('Your World Famous App')
        self.title_label.setAlignment(f.Qt.AlignmentFlag.AlignCenter)
        # splash screen title description
        self.description_label = a.QLabel(self.frame)
        self.description_label.resize(690, 40)
        self.description_label.move(0, self.title_label.height())
        self.description_label.setObjectName('desc_label')
        self.description_label.setText('<b>We build the systems and the apps.</b>')
        self.description_label.setAlignment(f.Qt.AlignmentFlag.AlignCenter)
        # splash screen pogressbar
        self.progressBar = a.QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 - 10, 50)
        self.progressBar.move(100, 180) # self.description_label.y()+130
        self.progressBar.setAlignment(f.Qt.AlignmentFlag.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)
        self.progressBar.setStyleSheet("""QProgressBar {
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
        }""")
        # spash screen loading label
        self.loading_label = a.QLabel(self.frame)
        self.loading_label.resize(self.width() - 10, 50)
        self.loading_label.move(0, self.progressBar.y() + 70)
        self.loading_label.setObjectName('loading_label')
        self.loading_label.setAlignment(f.Qt.AlignmentFlag.AlignCenter)
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
            t.sleep(1)
            self.showLogin()
        self.counter += 1
    def showLogin(self):
        self.login = WindowApp(self)
        self.login.show()    

if __name__ == "__main__":       
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
    splash = SplashScreen()
    splash.show()
    s.exit(app.exec())