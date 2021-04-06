# This Python file uses the following encoding: utf-8
import sys
import os
from MainWindow import *

import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets




if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
