import serial
from geopy.geocoders import ArcGIS
import folium
def read_data():
    arduino_data=serial.Serial("COM4",9600);
    while True:
        while arduino_data.inWaiting()==0:
            print("Hello")
            pass
        print(arduino_data)
        '''arduino_string=arduino_data.raedline()
        data=arduino_string.split(",")
        print(data)'''
def send_data():
    # Define the serial port and baud rate (make sure to set these to match your setup)
    serial_port = "COM3"  # Change this to your XBee's serial port
    baud_rate = 9600
    try:
        # Open the serial connection
        ser = serial.Serial(serial_port, baud_rate, timeout=1)
        print(f"Connected to {serial_port} at {baud_rate} baud")

        # Define the data to send
        data_to_send = b"Hello, XBee!"

        # Send the data
        ser.write(data_to_send)
        print(f"Sent: {data_to_send}")

        # Close the serial connection
        ser.close()
        print("Serial connection closed")

    except serial.SerialException as e:
        print(f"Error: {e}")
#
read_data()