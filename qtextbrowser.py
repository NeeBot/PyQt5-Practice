import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("qtextbrowser.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #버튼에 기능을 할당하는 코드
        self.btnPrint.clicked.connect(self.printTextFunction)
        self.btnSetText.clicked.connect(self.changeTextFunction)
        self.btnAppendText.clicked.connect(self.appendTextFunction)
        self.btnClear.clicked.connect(self.clearTextFunction)

    def printTextFunction(self):
        #self.Textbrowser이름.toPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        print(self.textBrowser.toPlainText())

    def changeTextFunction(self):
        #self.Textbrowser이름.setPlainText()
        self.textBrowser.setPlainText("This is Textbrowser - Change Text")
    
    def appendTextFunction(self):
        #self.Textbrowser이름.append()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.textBrowser.append("Append Text")

    def clearTextFunction(self):
        #self.Textbrowser.clear()
        #Textbrowser에 있는 글자를 지우는 메서드
        self.textBrowser.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()