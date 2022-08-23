import serial
import time
import jsonmodule as jm

setting = jm.get_secret("serial")
arduino = serial.Serial(setting["port"], setting["number"])

def writeSerial(data):
    arduino.write(bytes(data, 'utf-8'))
    time.sleep(0.05)
    return data

def readSerial():
    data = arduino.readline()
    data = data[:-2].decode()
    return data

if __name__ == "__main__":
    while True:
        print(readSerial())
        writeSerial("1")