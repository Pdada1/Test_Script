from machine import Pin
from utime import sleep
import sys
import select

LED_ON = "LED ON"
LED_OFF = "LED OFF"

pin = Pin("LED", Pin.OUT)
print("Init Finished")
poll_obj=select.poll()
poll_obj.register(sys.stdin,1)
run=True

while run:
    if poll_obj.poll(0):
        v = sys.stdin.readline().strip()
        if v == LED_ON:
            pin.on()
        if v == LED_OFF:
            pin.off() 
        if v == "STOP":
            run=False
pin.off()
print("Finished.")
