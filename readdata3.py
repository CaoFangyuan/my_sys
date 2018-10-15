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
    rawdata = []
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 15600000 
    spi.mode = 0b00
    IRQ = gpio.input(29)
    #print(IRQ)
    resp = spi.xfer2([0x01,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    #print(BytesToHex(resp))
    #IRQ = gpio.input(29)
    #print(IRQ)
    resp = spi.xfer2([0x01,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    #print(BytesToHex(resp))
    try:
        data1 = [0x00,0,0,0,0,0,0,0,0,0,0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        resp1 = spi.xfer2(data1)
        print(BytesToHex(resp1))
        number = spi.xfer2([0x12,0])
        print(number)
        while True:
            if number[1] == 74:
                data2 = [0x00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                resp2 = spi.xfer2(data2)
                #print("raw_data..............")
                print(BytesToHex(resp2))
                number = spi.xfer2([0x12,0])
                #print(number)
            else:
                while number[1] < 74:
                    number = spi.xfer2([0x12,0])
                    #print(number)
    except KeyboardInterrupt:
        spi.close()
        gpio.cleanup()
        print("finish")
