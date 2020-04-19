from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
import sys

designFile = loadUi('project(main).ui')

class window(QtWidgets.QMainWindow , designFile):
    pass
    


