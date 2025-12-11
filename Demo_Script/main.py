from machine import Pin
from utime import sleep, ticks_ms, ticks_diff
import sys
import select

LED_ON = "LED ON"
LED_OFF = "LED OFF"

pin_led = Pin("LED", Pin.OUT)
pin_read = Pin(15, Pin.IN, Pin.PULL_DOWN)   # Use PULL_DOWN since button goes to 3V3

print("Init Finished")
poll_obj = select.poll()
poll_obj.register(sys.stdin, 1)
run = True

# --- Debounce variables ---
last_press_time = 0
debounce_ms = 150   # adjust if needed

while run:
    # --- Handle serial commands ---
    if poll_obj.poll(0):
        v = sys.stdin.readline().strip()
        if v == LED_ON:
            pin_led.on()
        if v == LED_OFF:
            pin_led.off()
        if v == "STOP":
            run = False

    # --- Button debounce ---
    if pin_read.value() == 1:   # button pressed
        now = ticks_ms()
        if ticks_diff(now, last_press_time) > debounce_ms:
            print("Button Pressed")
            last_press_time = now

    sleep(0.01)  # small delay to reduce CPU usage

pin_led.off()
print("Finished.")
