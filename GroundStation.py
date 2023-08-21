from PyQt5 import QtCore, QtGui, QtWidgets,uic
#from pyqtgraph import PlotWidget
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread,QObject,pyqtSignal
import re

class Ui_MainWindow(object):

        def __init__(self,app):
                self.app=app
                self.ui=uic.loadUi("GroundStationGUI.ui")

                self.ui.command_enter_button.clicked.connect(self.command)

                self.ui.show()
                self.run()
        
        #printing text from command input
        def command(self):
                #print(self.ui.command_input.toPlainText())
                current_cmd=self.ui.command_input.toPlainText()
                self.ui.command_input.clear()

                cmd=current_cmd.split(",")
                cmd=cmd[2:]
                print(cmd)
                print("Hello")
                #CX - Payload Telemetry On/Off Command
                if cmd[0]=="CX":
                        print("Hello")
                        if cmd[1]=="ON":
                               print("Transmitting")
                        elif cmd[1]=="OFF":
                              print("Not Transmitting")
                        else:
                              print("ERROR: INCORRECT INPUT")
                #ST - Set Time
                elif cmd[0]=="ST":
                        if re.match(r'^\d{2}-\d{2}-\d{4}$',cmd[1]):
                                print("New Time: ",cmd[1])
                        elif cmd[1]=="GPS":
                                print("New Time is GPS time")
                        else:
                                print("ERROR: INCORRECT INPUT")
                #SIM - Simulation Mode Control Command
                elif cmd[0]=="SIM":
                        if cmd[1]=="ENABLE":
                               print("Transmitting")
                        elif cmd[1]=="ACTIVATE":
                              print("Not Transmitting")
                        elif cmd[1]=="DISABLE":
                              print("Not Transmitting")
                        else:
                              print("ERROR: INCORRECT INPUT")
                #SIMP - Simulated Pressure Data (to be used in Simulation Mode only)
                elif cmd[0]=="SIMP":
                        sim_pressure=cmd[1]
                        pressure=sim_pressure*(10**(-3))
                        print("Pressure:",pressure)
                #CAL - Calibrate Altitude to Zero
                elif cmd[0]=="CAL":
                        altitude=0
                        print("altitude:",altitude)
                #BCN - Control Audio Beacon
                elif cmd[0]=="BCN":
                        if cmd[1]=="ON":
                                print("Audio Beacon ON")
                        elif cmd[1]=="OFF":
                                print("Audio Beacon OFF")
                        else:
                              print("ERROR: INCORRECT INPUT")
                else:
                        print("Error")




                       



        def run(self):
                self.app.exec_()

        ###

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow(app)