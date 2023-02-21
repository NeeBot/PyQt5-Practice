import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("qTextEdit.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        # 버튼에 기능을 할당하는 코드
        self.btnPrintTextEdit.clicked.connect(self.printTextEdit)
        self.btnClearTextEdit.clicked.connect(self.clearTextEdit)
        self.btnSetFont.clicked.connect(self.setFont)
        self.bntSetFontItalic.clicked.connect(self.fontItalic)
        self.btnSetFontColorRed.clicked.connect(self.fontColorRed)
        self.bntFontSizeUp.clicked.connect(self.fontSizeUp)
        self.btnFontSizeDown.clicked.connect(self.fontSizeDown)

    def printTextEdit(self):
        print(self.textEdit.toPlainText())

    def clearTextEdit(self):
        self.textEdit.clear()

    def setFont(self):
        fontvar = QFont("Apple SD Gothic Neo", 10)
        self.textEdit.setCurrentFont(fontvar)

    def fontItalic(self):
        self.textEdit.setFontItalic(True)

    def fontColorRed(self):
        colorvar = QColor(255, 0, 0)
        self.textEdit.setTextColor(colorvar)

    def fontSizeUp(self):
        self.fontSize = self.fontSize + 1
        self.textEdit.setFontPointSize(self.fontSize)

    def fontSizeDown(self):
        self.fontSize = self.fontSize - 1
        self.textEdit.setFontPointSize(self.fontSize)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 