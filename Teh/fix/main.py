import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("screen1.ui", self)


class VisionWindow(QDialog):
    def __init__(self):
        super(VisionWindow, self).__init__()
        loadUi("screen2.ui", self)

# main
app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
visionwindow = VisionWindow()
widget.addWidget(mainwindow)
widget.addWidget(visionwindow)
widget.setFixedHeight(720)
widget.setFixedWidth(720)
widget.show()

try:
    sys.exit(app.exec_())  # Corrected 'exec_' function name
except Exception as e:  # Be more specific about the exception
    print("Exit due to:", e)
