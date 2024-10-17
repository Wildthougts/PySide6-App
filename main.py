import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

from Frontend.Main.ui.MainWindow_ui import Ui_MainWindow

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self,):
        super().__init__()
        self.setupUi(self)









if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())








if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())