from PyQt5 import QtCore, QtGui, QtWidgets,uic
#from pyqtgraph import PlotWidget
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread,QObject,pyqtSignal

class Ui_MainWindow(object):

        def __init__(self,app):
                self.app=app
                self.ui=uic.loadUi("GroundStationGUI.ui")

                self.ui.show()
                self.run()


        def run(self):
                self.app.exec_()

        ###

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow(app)