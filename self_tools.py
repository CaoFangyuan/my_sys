import spidev
import time
import numpy as np


IRQ_RX_THRESHOLD = 16
MAX_FIFO_LEN = 128
MAX_QUAD_UART_MSG_LEN = 129

def BytesToHex(Bytes):
    return ''.join(["0x%02X " % x for x in Bytes]).strip()

def initializedQuardUart():
    resp = spi.xfer2([0x81,0x00])
    resp1 = spi.xfer2([0x88,0x20])
    resp2 = spi.xfer2([0x89,0x80])
    resp3 = spi.xfer2([0x8B,0x03])
    resp4 = spi.xfer2([0x90,0x2F])
    resp5 = spi.xfer2([

