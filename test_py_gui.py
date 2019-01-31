from PyQt5 import QtWidgets, uic
import sys
app = QtWidgets.QApplication([])
win = uic.loadUi("\\Users\\Jimmy_Bainbridge\\Desktop\\test_qt_gui.ui")
win.show()
sys.exit(app.exec())
