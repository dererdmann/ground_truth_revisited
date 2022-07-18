import serial
ser = serial.Serial('/dev/cu.usbmodem14401', 115200) # I've verified that this is the proper COM port, second argument is baud rate, which I actually wasn't all that sure of, but I tried both 115200 and 9600 since they are both pretty common. I didn't bother tuning any other COM port settings.
ser.write(b'G28 X\n') # My second issue comes up when I'm not sure of the line ending character that the M2 expects (maybe \n, \r or even \r\n)
ser.close()