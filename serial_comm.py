from serial import Serial
import time
import threading

def reader(ser):
    """Background reader to show what the Pico prints back."""
    while True:
        line = ser.readline()
        if line:
            print("Pico:", line.decode(errors="replace").rstrip())

ser = Serial(port="COM3", baudrate=115200, timeout=0.1)

# Start background reader so we can see what Pico prints
threading.Thread(target=reader, args=(ser,), daemon=True).start()

l_on  = b"LED ON\r\n"
l_off = b"LED OFF\r\n"
stop = b"STOP\r\n"
count=0
while count<=5:
    print("PC: sending LED ON")
    ser.write(l_on)
    ser.flush()
    time.sleep(1)

    print("PC: sending LED OFF")
    ser.write(l_off)
    ser.flush()
    time.sleep(1)
    if count == 5:
        ser.write(stop)
        ser.flush()
    count+=1
time.sleep(2)

