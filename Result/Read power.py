import time
import serial
ser = serial.Serial(
    port='/dev/ttyACM0',                   
    baudrate=115200,
    parity=serial.PARITY_ODD,      
    stopbits=serial.STOPBITS_TWO,  
    bytesize=serial.SEVENBITS      
)
data = ''
while True:
    data = ser.readline()
    t = time.time()
    ct = time.ctime(t)
    print(ct, ':')
    print(data)
    f = open('vnf_1.csv', 'a')
    f.writelines(ct)
    f.writelines(',')
    f.writelines(data.decode('utf-8'))
    f.close()
