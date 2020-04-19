from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys

designFile = loadUi('project(main).ui')

class window(QtWidgets.QMainWindow , designFile):
    def __init__(self, parent = none):
        super(window, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    login = window()
    login.show()
    app.exec_()

if __name__ == '__main__':
    main()

