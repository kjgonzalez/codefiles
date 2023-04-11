import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

class WIN(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

if(__name__ == '__main__'):
    app = QApplication(sys.argv)
    win = WIN()
    win.show()
    sys.exit(app.exec())

