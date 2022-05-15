import pyfirmata



from cvzone.SerialModule import SerialObject
from time import sleep

arduino = SerialObject("/dev/ttyACM0")

def led(total):
    if total > 2:
        arduino.sendData([1])
        sleep(0.2)
        arduino.sendData([0])
  