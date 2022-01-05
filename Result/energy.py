import csv
import numpy as np
import matplotlib.pyplot as plt
with open('time_1.csv', 'r',encoding='utf-8')as f1: # time from Raspberry Pi
    f_1=csv.reader(f1)
    time = list(f_1)
    time_begin = [i[0] for i in time] 
    time_end = [i[1] for i in time] 

with open('vnf_1.csv', 'r',encoding='utf-8')as f2: # Power read by Arduino
    power = list(csv.reader(f2))
    power_t = [i[0] for i in power] 
    power_p = [i[1] for i in power]


for i in range(0,160):
    begin_pos=power_t.index(time_begin[i])
    end_pos=power_t.index(time_end[i])
    p_select=power_p[begin_pos:end_pos+1]
    p_select=list(map(float,p_select))
    p_mean=np.mean(p_select)
    energy=np.sum(p_select)*0.2
    #plt.plot(p_select)
    #plt.show()
    
    f = open('energy_1.csv', 'a')  # the file name
    f.writelines("{:.2f}".format(p_mean))
    f.writelines(',')
    f.writelines("{:.2f}".format(energy))
    f.writelines('\n')
    f.close()
    
    

