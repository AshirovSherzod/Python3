from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setFont(QFont("calibri",18))
        self.setMaximumSize(350,475)
        self.setMinimumSize(350,475)
        self.setStyleSheet("background-color: Black;")

        # self.label = QLabel(self)
        # self.label.setGeometry(30,0,200,30)
        # self.label.setText("Ismni kiriting")

        self.line = QLineEdit(self)
        self.line.setGeometry(20,30,300,50)
        self.line.setFont(QFont("calibri",18))
        self.line.setStyleSheet("""
            color: White ;
            border-color: Black ;
            border-width: 4px""")
        self.line.setAlignment(Qt.AlignRight)

        self.btAC = QPushButton("AC",self)
        self.btAC.setGeometry(20,80,70,70)
        self.btAC.setFont(QFont("Consolas",18))
        self.btAC.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(169,169,169);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)

        self.btP = QPushButton("+/-",self)
        self.btP.setGeometry(100,80,70,70)
        self.btP.setFont(QFont("Consolas",18))
        self.btP.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(169,169,169);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        

        self.btF = QPushButton("%",self)
        self.btF.setGeometry(180,80,70,70)
        self.btF.setFont(QFont("Consolas",18))
        self.btF.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(169,169,169);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)

        self.btB = QPushButton("-:-",self)
        self.btB.setGeometry(260,80,70,70)
        self.btB.setFont(QFont("Consolas",18))
        self.btB.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(255, 165, 0);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btn7 = QPushButton("7",self)
        self.btn7.setGeometry(20,160,70,70)
        self.btn7.setFont(QFont("Consolas",18))
        self.btn7.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105,105,105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        self.btn7.clicked.connect(self.add_seven)

        self.btn8 = QPushButton("8",self)
        self.btn8.setGeometry(100,160,70,70)
        self.btn8.setFont(QFont("Consolas",18))
        self.btn8.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105,105,105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        self.btn8.clicked.connect(self.add_eight)
        self.btn9 = QPushButton("9",self)
        self.btn9.setGeometry(180,160,70,70)
        self.btn9.setFont(QFont("Consolas",18))
        self.btn9.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105,105,105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btX = QPushButton("x",self)
        self.btX.setGeometry(260,160,70,70)
        self.btX.setFont(QFont("Consolas",18))
        self.btX.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(255, 165, 0);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)

        self.btn4 = QPushButton("4",self)
        self.btn4.setGeometry(20,240,70,70)
        self.btn4.setFont(QFont("Consolas",18))
        self.btn4.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105,105,105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btn5 = QPushButton("5",self)
        self.btn5.setGeometry(100,240,70,70)
        self.btn5.setFont(QFont("Consolas",18))
        self.btn5.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105,105,105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btnB = QPushButton("6",self)
        self.btnB.setGeometry(180,240,70,70)
        self.btnB.setFont(QFont("Consolas",18))
        self.btnB.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105,105,105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btA = QPushButton("-",self)
        self.btA.setGeometry(260,240,70,70)
        self.btA.setFont(QFont("Consolas",18))
        self.btA.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(255, 165, 0);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btn1 = QPushButton("1",self)
        self.btn1.setGeometry(20,320,70,70)
        self.btn1.setFont(QFont("Consolas",18))
        self.btn1.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105, 105, 105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btn2 = QPushButton("2",self)
        self.btn2.setGeometry(100,320,70,70)
        self.btn2.setFont(QFont("Consolas",18))
        self.btn2.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105, 105, 105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btn3 = QPushButton("3",self)
        self.btn3.setGeometry(180,320,70,70)
        self.btn3.setFont(QFont("Consolas",18))
        self.btn3.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105, 105, 105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)

        self.btnQ = QPushButton("+",self)
        self.btnQ.setGeometry(260,320,70,70)
        self.btnQ.setFont(QFont("Consolas",18))
        self.btnQ.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(255, 165, 0);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)
        
        self.btn0 = QPushButton("0",self)
        self.btn0.setGeometry(20,400,150,70)
        self.btn0.setFont(QFont("Consolas",18))
        self.btn0.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105, 105, 105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """) 

        self.btV = QPushButton(",",self)
        self.btV.setGeometry(180,400,70,70)
        self.btV.setFont(QFont("Consolas",18))
        self.btV.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(105, 105, 105);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """)   

        self.btT = QPushButton("=",self)
        self.btT.setGeometry(260,400,70,70)
        self.btT.setFont(QFont("Consolas",18))
        self.btT.setStyleSheet("""
            color: rgb(0,0,0);
            background-color: rgb(255, 165, 0);
            border-color: rgb(0,0,0);
            border-width: 3px;
            border-style: solid;
            border-radius: 35%;
            """) 
        

app = QApplication(sys.argv)
project = Calculator()
project.show()
sys.exit(app.exec_())