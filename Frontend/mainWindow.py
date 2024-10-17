import sys
from PySide6 import QtCore as qtc
from PySide6.QtWidgets import  QFileDialog
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg


from ui.MainWindow_ui import Ui_MainWindow

class MainWindow(qtw.QMainWindow, Ui_MainWindow, qtw.QWidget):
    


    def __init__(self):
        super().__init__()
        self.setupUi(self)

     
        self.pb_uploadaccounts.clicked.connect(self.upload_file)
        

    @qtc.Slot()
    def upload_file(self):
        # Open a file dialog to select a .txt file
        file_path, _ = QFileDialog.getOpenFileName(self, "Select a .txt file", "", "Text Files (*.txt)")

        # Check if a file was selected
        if file_path:
            # Display the file path in the line edit
            self.ui.le_accounts.setText(file_path)
            

        






if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
