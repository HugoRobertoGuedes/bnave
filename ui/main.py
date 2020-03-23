import sys
import json
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


qt_creator_file = "BnaveBrowser.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qt_creator_file)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.url = QLineEdit()
        self.urlbar.addWidget(self.url)

        


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()

