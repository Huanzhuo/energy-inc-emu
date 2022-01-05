import time
import serial
ser = serial.Serial(
    port='/dev/ttyACM0',                   #端口号
    baudrate=115200,
    parity=serial.PARITY_ODD,      # 校验位 
    stopbits=serial.STOPBITS_TWO,  # 停止位
    bytesize=serial.SEVENBITS      # 数据位
)
data = ''
while True:
    data = ser.readline()
    t = time.time()
    ct = time.ctime(t)
    print(ct, ':')
    print(data)
    f = open('vnf_1.csv', 'a')#数据保存的路径
    f.writelines(ct)
    f.writelines(',')
    f.writelines(data.decode('utf-8'))
    f.close()