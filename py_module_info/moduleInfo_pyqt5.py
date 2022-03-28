'''
General Instructions:
1. you MUST create an environment. install "pyqt5-tools"
2. find QtDesigner at */venv/Lib/site-packages/qt5_applicatoins/Qt/bin/designer.exe
3. generally, for a basic widget, make a new form >> "Widget"
4. modify as desired, save as *.ui file
5. convert each *.ui to *.py: */venv/Scripts/pyuic5.exe form.ui -o form.py
6. create a file that will now use interface, e.g. this file (moduleInfo_pyqt5.py)
7. add following code as shown below (somewhat boilerplate)
'''

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from form import Ui_Form as UF

class Form(UF, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.wBT_combine.clicked.connect(self.printout) # need a button called "wBT_combine"
    def printout(self):
        a = self.wEN_txt1.displayText() # need a line text entry called "wEN_txt1"
        b = self.wEN_txt2.displayText() # need a line text entry called "wEN_txt2"
        self.wLB_out.setText(a+b)       # need a label  called "wLB_out"

if(__name__ == '__main__'):
    app = QtWidgets.QApplication(sys.argv)
    gui = Form()
    sys.exit(app.exec_())

# eof
