import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("radioButton.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.RB1.clicked.connect(self.groupboxRadFunction)
        self.RB2.clicked.connect(self.groupboxRadFunction)
        self.RB3.clicked.connect(self.groupboxRadFunction)
        self.RB4.clicked.connect(self.groupboxRadFunction)

    def groupboxRadFunction(self):
        if self.RB1.isChecked():
            print("GroupBox_RB1 Checked")
        elif self.RB2.isChecked():
            print("GroupBox_RB1 Checked")
        elif self.RB3.isChecked():
            print("GroupBox_RB1 Checked")
        elif self.RB4.isChecked():
            print("GroupBox_RB1 Checked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()