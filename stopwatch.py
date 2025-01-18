import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel,QVBoxLayout,QWidget,QPushButton,QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt ,QTime,QTimer

def main():
    class stop(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setGeometry(600,400,800,200)
            self.setWindowIcon(QIcon("C:\\Users\\pkush\\Downloads\\icons8-clock-50.png"))
            self.setWindowTitle("STOPWATCH")
            self.timer=QTimer(self)
            self.time=QTime(0,0,0,0)
            self.initUI()
        def initUI(self):
            self.label1=QLabel(self)
            central_w=QWidget()
            self.setCentralWidget(central_w)
            vbox=QVBoxLayout()
            vbox.addWidget(self.label1)
            central_w.setLayout(vbox)
            self.label1.setAlignment(Qt.AlignCenter)
            self.button1=QPushButton("Start",self)
            self.button2=QPushButton("Stop",self)
            self.button3=QPushButton("Reset",self)
            vbox.addWidget(self.button1)
            vbox.addWidget(self.button2)
            vbox.addWidget(self.button3)
            central_w.setLayout(vbox)
            hbox=QHBoxLayout()
            hbox.addWidget(self.button1)
            hbox.addWidget(self.button2)
            hbox.addWidget(self.button3)
            vbox.addLayout(hbox)
            self.setStyleSheet("""
                               QLabel{
                                   background-color:black;
                                   color:white;
                                   font-family:calibri;
                                   font-size:150px;}
                                QPushButton{
                                    font-family:calibri;
                                    font-size:50px;
                                    
                                }
                                """)
            
            self.button1.setStyleSheet("background-color:#21bbde;"
                                    "color:black;")
            
            self.button2.setStyleSheet("background-color:#eb3449;"
                                    "color:black")
            self.button3.setStyleSheet("background-color:#f54c0a;"
                                   "color:black")
            
            self.button1.clicked.connect(self.start)
            self.button2.clicked.connect(self.stop)
            self.button3.clicked.connect(self.reset)
            self.timer.timeout.connect(self.utime)
            
       
        def start(self):
            self.timer.start(10)
        
        def stop(self):
            self.timer.stop()
        
        def reset(self):
            self.timer.stop()
            self.time=QTime(0,0,0,0)
            self.label1.setText(self.format_time(self.time))
        
        def format_time(self,time):
            hours=time.hour()
            minutes=time.minute()
            seconds=time.second()
            milli=time.msec()//10
            return f"{hours:02}:{minutes:02}:{seconds:02}.{milli:02}"
        
        def utime(self):
            self.time=self.time.addMSecs(10)
            self.label1.setText(self.format_time(self.time))
            
  

    app=QApplication(sys.argv)
    w=stop()
    w.show()
    sys.argv(app.exec_())
    
    
if __name__=="__main__":
    main()      
        
    
    
    
    
    
    
