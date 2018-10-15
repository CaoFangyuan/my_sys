import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setup(29,gpio.IN)
a = gpio.input(29)
print(a)
