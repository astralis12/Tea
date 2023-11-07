import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()   #for the stuffs instide the window
        self.setGeometry(250, 250, 500, 500)     #xposition, yposition, width, height
        self.setWindowTitle("Test Tea")

    #def __init__(self, parent: QWidget | None = ..., flags: WindowFlags | WindowType = ...) -> None:
        # super().__init__(parent, flags)

    def initUI(self):
        self.label = QtWidgets.QLabel(self)      #create a label, set where the label will be shown/onto itself
        self.label.setText("Wtf")
        self.label.move(50,50)       #position (xpos, ypos)

        self.b1 = QtWidgets.QPushButton(self)   #create the button
        self.b1.setText("Try this!")
        self.b1.clicked.connect(self.clicked)   #a way to trigger the next step

    def clicked(self):
     self.label.setText("Pressed the button")

    def update(self):
       self.label.adjustSize()  

def window():
    app = QApplication(sys.argv)  #getting the application 
    win = MyWindow()           # displayed window


    win.show() 
    sys.exit(app.exec_())   #clean exit

window()


