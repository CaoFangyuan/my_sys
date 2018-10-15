import spidev
import time 
import numpy as np
import RPi.GPIO as gpio

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

def readdata():
    spi = spidev.SpiDev()
    spi.open(0,0)
    spi.max_speed_hz = 7800000
    spi.mode = 0b00
    data = []
    interrupt = []
    uart_chanel0 = 0
    uart_chanel1 = 1
    #data1 = [0x00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    data1 = [0x00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    resp1 = spi.xfer2(data1)
    data.append(resp1)
    print("raw_data_____________________________________________________")
    #print(data)
    print(BytesToHex(resp1))
    globalIRQ = spi.xfer2([0x1F,0])
    print("global IRQ information________________________________________________________________")
    #print(BytesToHex(globalIRQ))
    interrupt.append(globalIRQ)
    print(interrupt[0][0])

    '''while interrupt[0][0] == 15:
        interrupt = []
        globalIRQ = spi.xfer2([0x1F,0])
        #print(BytesToHex(globalIRQ))
        interrupt.append(globalIRQ)
        #print(interrupt[0][0])
        
    if interrupt[0][0] != 15:
        # read ISR to clear IRQ
        if interrupt[0][0] == 14:
            #data1 = [0x00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            data1 = [0x00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            resp1 = spi.xfer2(data1)
            data.append(resp1)
            print("raw_data_____________________________________________________")
            #print(data)
            print(BytesToHex(resp1))
            # read ISR to clear IRQ
            ISR = spi.xfer2([0x02,0])
            print(BytesToHex(ISR))
        elif interrupt[0][0] == 13:
            ISR = spi.xfer2([0x22,0])
            print(BytesToHex(ISR))'''

    spi.close()
    return data

def process(raw_data):
    print("process function_________________________________________________")
    print(raw_data)

if __name__ == "__main__":
    gpio.setmode(gpio.BOARD)
    gpio.setup(29,gpio.IN)
    #gpio.setup(24,gpio.OUT)
    #b = gpio.output(24,gpio.HIGH)
    rawdata = []
    #print(b)
    read_flag = 1
    while read_flag < 12:
        IRQ = gpio.input(29)
        while IRQ == 1:
            IRQ = gpio.input(29)
            print(IRQ)
        if IRQ == 0:
            read_flag = read_flag + 1
            rawdata = readdata()
           # process(rawdata)
            #gpio.add_event_detect(29,gpio.FALLING,callback = readdata)
    gpio.cleanup()
