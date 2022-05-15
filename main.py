#import serial.tools.list_ports
#ports = list(serial.tools.list_ports.comports())
#for p in ports:
 #   print(p)

from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("/dev/ttyACM0")

while True:
    arduino.sendData([1])
    sleep(1)
    arduino.sendData([0])
    sleep(1)