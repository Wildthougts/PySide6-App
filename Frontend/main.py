import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Main.ui.MainWindow_ui import Ui_MainWindow
from login import LoginForm

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)

        self.form = LoginForm()
        self.form.login_success.connect(self.show)
        self.form.show()







if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    

    sys.exit(app.exec())


