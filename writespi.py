import wiringpi
import time

spichannel = 0
print(1)
spispeed = 7812500
print(2)
wiringpi.wiringPiSetupGpio()
print(3)
wiringpi.wiringPiSPISetup(spichannel, spispeed)
print(4)
wiringpi.wiringPiSPISetupMode(spichannel,spispeed,0)
print(5)
senddata=str(4772)
print(senddata)
while True:
    a = wiringpi.wiringPiSPIDataRW(0,senddata)
    print(a)
    time.sleep(1)
