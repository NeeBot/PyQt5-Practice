import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("qlabel.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼에 기능을 할당하는 코드
        self.btnChangeText.clicked.connect(self.changeTextFunction)
        self.btnPrintText.clicked.connect(self.printTextFunction)
    
    def changeTextFunction(self):
        #self.Label이름.setText("String")
        #Label에 글자를 바꾸는 메서드
        self.label.setText("This is Label - Change Text")

    def printTextFunction(self):
        #sef.Label이름.text()
        #Label에 있는 글자를 가져오는 메서드
        print(self.label.text())

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()