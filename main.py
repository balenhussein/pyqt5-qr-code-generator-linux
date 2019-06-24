from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
import pyqrcode
from random import random
from subprocess import Popen
from os import path

class Ui_MainWindow(object):

    def generatePNG(self):
        url = pyqrcode.create(self.input.text())
        d = path.join(path.expanduser("~"), "Downloads")
        fn = path.join(d, str(random()) + ".png")
        url.png(fn, scale=8)
        print(url.terminal(quiet_zone=1))
        Popen(['notify-send', "PNG file generated to " + fn])
        pixmap = QPixmap(fn)
        self.preview.setPixmap(pixmap)
        return

    def generateSVG(self):
        url = pyqrcode.create(self.input.text())
        d = path.join(path.expanduser("~"), "Downloads")
        fn = path.join(d, str(random()) + ".svg")
        url.svg(fn, scale=8)
        print(url.terminal(quiet_zone=1))
        Popen(['notify-send', "SVG file generated to " + fn])
        pixmap = QPixmap(fn)
        self.preview.setPixmap(pixmap)
        return

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 510)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pngButton = QtWidgets.QPushButton(self.centralwidget)
        self.pngButton.setObjectName("pngButton")
        self.gridLayout.addWidget(self.pngButton, 0, 1, 1, 1)
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setObjectName("input")
        self.gridLayout.addWidget(self.input, 0, 0, 1, 1)
        self.preview = QtWidgets.QLabel(self.centralwidget)
        self.preview.setObjectName("preview")
        self.gridLayout.addWidget(self.preview, 1, 0, 1, 3)
        self.svgButton = QtWidgets.QPushButton(self.centralwidget)
        self.svgButton.setObjectName("svgButton")
        self.gridLayout.addWidget(self.svgButton, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pngButton.clicked.connect(self.generatePNG)
        self.svgButton.clicked.connect(self.generateSVG)
        MainWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR Code Generator | Roj Serbest"))
        self.pngButton.setText(_translate("MainWindow", "GENERATE PNG"))
        self.input.setPlaceholderText(_translate("MainWindow", "Enter text, url or email"))
        self.preview.setText(_translate("MainWindow", "The generated file will be here"))
        self.svgButton.setText(_translate("MainWindow", "GENERATE SVG"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
