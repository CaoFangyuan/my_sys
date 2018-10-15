import spidev
import time 
import numpy as np
import RPi.GPIO as gpio
import sys

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    gpio.setup(29,gpio.IN)
    #gpio.setup(24,gpio.OUT)
    #b = gpio.output(24,gpio.HIGH)
    rawdata = []
    #print(b)
    read_flag = 1
    total_data = []
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 15600000 
    spi.mode = 0b00
    resp = spi.xfer2([0x01,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print(BytesToHex(resp))
    resp = spi.xfer2([0x01,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print(BytesToHex(resp))
    try:
        number = spi.xfer2([0x12,0])
        print(number)
        while True:
            if number[1] == 16:
                #number = spi.xfer2([0x12,0])
                #print(number)
                #data1 = [0x00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                data1 = [0x00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                resp1 = spi.xfer2(data1)
                print("raw_data..............")
                print(BytesToHex(resp1))
                number = spi.xfer2([0x12,0])
                print(number)
            else:
                number = spi.xfer2([0x12,0])
                print(number)
                while number[1] !=  16:
                    number = spi.xfer2([0x12,0])
                    #print(number)
    except KeyboardInterrupt:
        spi.close()
        gpio.cleanup()
        print("finish")
