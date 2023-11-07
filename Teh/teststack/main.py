# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


#from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QApplication, QWidget


#class Ui_Dialog(object):
class MainWindow(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("screen1.ui", self)
        self.button.clicked.connect(self.gotoScreen2)

    def gotoScreen2(self): 
        screen2 = Screen2()
        widget.addWidget(screen2)  # Add an instance, not the class
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Screen2(QDialog):
    def __init__(self):
        super(Screen2, self).__init__()  # Use Screen2, not Ui_MainWindow
        loadUi("Screen2.ui", self)
        self.button.clicked.connect(self.gotoScreen1)

    def gotoScreen1(self):
        main_window=MainWindow()
        widget.addWidget(main_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main_window = MainWindow()  # Use a more descriptive variable name
    widget.addWidget(main_window)
    widget.setFixedHeight(720)
    widget.setFixedWidth(720)
    widget.show()
    sys.exit(app.exec_())


# main
#app = QApplication(sys.argv)


