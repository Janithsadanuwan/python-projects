from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyGui(QMainWindow):
    def __init__(self):
        super(MyGui, self).__init__()
        uic.loadUi('window.ui', self)
        self.show()

        self.setWindowTitle('Notepad')

        # Change font size
        self.action12pt.triggered.connect(lambda: self.change_font_size(12))
        self.action18pt.triggered.connect(lambda: self.change_font_size(18))
        self.action24pt.triggered.connect(lambda: self.change_font_size(24))

        # Open file
        self.actionOpen.triggered.connect(self.open_file)
        # Save file
        self.actionSave.triggered.connect(self.save_file)
        # Close application
        self.actionClose.triggered.connect(exit)

    def change_font_size(self, size):
        self.plainTextEdit.setFont(QFont('Arial', size))

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, 'Open file', '', 'Text Files (*.txt);;Python Files (*.py)', options=options)
        if filename != '':
            with open(filename, 'r') as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, 'Save file', '', 'Text Files (*.txt);;Python Files (*.py)', options=options)
        if filename != '':
            with open(filename, 'w') as f:
                f.write(self.plainTextEdit.toPlainText())

    def closeEvent(self, event):
        dialog = QMessageBox()
        dialog.setText('Do you want to save changes?')
        dialog.addButton(QMessageBox.Yes)
        dialog.addButton(QMessageBox.No)
        dialog.addButton(QMessageBox.Cancel)

        answer = dialog.exec()
        if answer == QMessageBox.Yes:
            self.save_file()
            event.accept()
        elif answer == QMessageBox.Cancel:
            event.ignore()

def main():
    app = QApplication([])
    gui = MyGui()
    app.exec_()

if __name__ == '__main__':
    main()
