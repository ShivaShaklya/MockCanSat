from PyQt5 import QtCore, QtGui, QtWidgets,uic
from pyqtgraph import PlotWidget
import csv
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread,QObject,pyqtSignal
import re

f=open("Simution_data.csv","r")
time=[]
altitude=[]
air_speed=[]
gps_altitude=[]
temperature=[]
voltage=[]
pressure=[]

r=csv.reader(f)
columns=next(r)
row=next(r)


class Ui_MainWindow(object):

        def __init__(self,app):
                self.app=app
                self.ui=uic.loadUi("GroundStationGUI.ui")

                self.ui.ALT.setTitle("Altitude V/s Time")
                self.ui.AST.setTitle("AIR_SPEED V/s Time")
                self.ui.TEMPT.setTitle("TEMPERATURE V/s Time")
                self.ui.VT.setTitle("VOLTAGE V/s Time")
                self.ui.PT.setTitle("PRESSURE V/s Time")
                self.ui.TT.setTitle("gps_altitude V/s Time")

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

                #CX - Payload Telemetry On/Off Command
                if cmd[0]=="CX":
                        if cmd[1]=="ON":
                                print("Transmitting")
                                self.plot_A2()

                        elif cmd[1]=="OFF":
                              print("Not Transmitting")
                              self.Pause()


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
                        flag1=False
                        flag2=False
                        if cmd[1]=="ENABLE":
                                flag1=True
                                print("Enabled")
                        elif cmd[1]=="ACTIVATE":
                                flag2=True
                                print("Activate")
                        elif cmd[1]=="DISABLE":
                                flag1=False
                                flag2=False
                                print("Disabled")
                        else:
                              print("ERROR: INCORRECT INPUT")

                        if flag1==True and flag2==True:
                                print("Simulation Mode Started")
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

        def plot_A2(self):
                def update_plot():
                        global row
                        try:
                                row=next(r)
                                #print(row)
                                time.append(float(row[21]))
                                altitude.append(float(row[5]))
                                air_speed.append(float(row[6]))
                                temperature.append(float(row[9]))
                                voltage.append(float(row[10]))
                                pressure.append(float(row[11]))
                                gps_altitude.append(float(row[13]))

                                self.refALT.setData(time,altitude)
                                self.refAIR_SPEED.setData(time,air_speed)
                                self.refTEMP.setData(time,temperature)
                                self.refVOLT.setData(time,voltage)
                                self.refPRESS.setData(time,pressure)
                                self.refT.setData(time,gps_altitude)

                                self.ui.L_MissionTime.setText(row[1])
                                self.ui.L_PacketCount.setText(row[2])
                                self.ui.L_Mode.setText(row[3])
                                self.ui.L_State.setText(row[4])
                                self.ui.L_altitude.setText(row[5])
                                self.ui.L_AirSpeed.setText(row[6])
                                self.ui.L_HS.setText(row[7])
                                self.ui.L_PS.setText(row[8])
                                self.ui.L_Temperature.setText(row[9])
                                self.ui.L_voltage.setText(row[10])
                                self.ui.L_AirPressure.setText(row[11])
                                self.ui.L_GPS_Time.setText(row[12])
                                self.ui.L_GPS_Altitude.setText(row[13])
                                self.ui.L_latitude.setText(row[14])
                                self.ui.L_longitude.setText(row[15])
                                self.ui.L_Sats.setText(row[16])
                                self.ui.L_tiltX.setText(row[17])
                                self.ui.L_tiltY.setText(row[18])
                                self.ui.L_rotZ.setText(row[19])
                                self.ui.L_echo.setText(row[20])
                        except Exception as exc:
                                print(exc)

                self.Timer=QtCore.QTimer()
                self.Timer.setInterval(1000)
                self.Timer.timeout.connect(update_plot)
                self.Timer.start()

                #ALTITUDE VS TIME
                self.refALT=self.ui.ALT.plot(time,altitude)

                #AIR_SPEED V/s Time
                self.refAIR_SPEED=self.ui.AST.plot(time,air_speed)

                #TEMPERATURE V/s Time
                self.refTEMP=self.ui.TEMPT.plot(time,temperature)

                #VOLTAGE V/s Time
                self.refVOLT=self.ui.VT.plot(time,voltage)

                #PRESSURE V/s Time
                self.refPRESS=self.ui.PT.plot(time,pressure)

                #Thrust V/s Time
                self.refT=self.ui.TT.plot(time,gps_altitude)

        def Pause(self):
                #print(row)
                self.Timer.stop() #PAUSES PLOTTING!!!!!!!!!!!!!!!!!!!!!
        
        def run(self):
                self.app.exec_()

        ###

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ui_MainWindow(app)