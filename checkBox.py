import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("checkBox.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #GroupBox밖에 있는 CheckBox에 기능 연결
        self.cB1.stateChanged.connect(self.chkFunction)
        self.cB2.stateChanged.connect(self.chkFunction)
        self.cB3.stateChanged.connect(self.chkFunction)
        self.cB4.stateChanged.connect(self.chkFunction)

        #GroupBox안에 있는 CheckBox에 기능 연결
        self.gCB1.stateChanged.connect(self.groupChkFunction)
        self.gCB2.stateChanged.connect(self.groupChkFunction)
        self.gCB3.stateChanged.connect(self.groupChkFunction)
        self.gCB4.stateChanged.connect(self.groupChkFunction)

    def chkFunction(self):
        # CheckBox는 여러개가 선택될 수 있기 때문에 elif를 사용하지 않습니다.
        if self.cB1.isChecked() : print("cB1 is Checked")
        if self.cB2.isChecked() : print("cB2 is Checked")
        if self.cB3.isChecked() : print("cB3 is Checked")
        if self.cB4.isChecked() : print("cB4 is Checked")

    def groupChkFunction(self):
        if self.gCB1.isChecked(): print("groupCB1 is Checked")
        if self.gCB2.isChecked(): print("groupCB2 is Checked")
        if self.gCB3.isChecked(): print("groupCB3 is Checked")
        if self.gCB4.isChecked(): print("groupCB4 is Checked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()