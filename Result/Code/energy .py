
# This code is using for calculate the energy and mean power with the sampling data

import csv
import numpy as np
import matplotlib.pyplot as plt
with open('time_75.csv', 'r',encoding='utf-8')as f1: # time from Raspberry Pi
    f_1=csv.reader(f1)
    time = list(f_1)
    time_begin = [i[0] for i in time] 
    time_end = [i[1] for i in time] 

with open('vnf_75.csv', 'r',encoding='utf-8')as f2: # Power read by Arduino
    power = list(csv.reader(f2))
    power_t = [i[0] for i in power] 
    power_p = [i[1] for i in power]

p_basis=power_p[46750:50000]                        #Select the number of basic power
p_basis=list(map(float,p_basis))
#print(np.mean(p_basis))

p_mean_b=np.mean(p_basis)
plt.xlabel("time(s)")
plt.ylabel("power(mW)")
#L1=plt.plot(np.arange(3250)/5,p_basis,label='power')
#L2=plt.plot(np.arange(3250)/5,np.ones(3250)*p_mean_b,color='black',linestyle='dashdot',label='mean power of basis')
plt.legend()
#plt.show()
t=np.ones(50)
for i in range(51,100):
    begin_pos=power_t.index(time_begin[i])
    end_pos=power_t.index(time_end[i])
    p_select=power_p[begin_pos:end_pos+1]
    p_select=list(map(float,p_select))
    t[i-50]=(end_pos-begin_pos+1)*0.2
    #p_mean=np.mean(p_select)-np.mean(p_basis)
    #energy=np.sum(p_select-np.mean(p_basis))*0.2
    p_mean=np.mean(p_select)
    energy=np.sum(p_select)*0.2
    plt.xlabel("time(s)")
    plt.ylabel("power(mW)")
    #L1=plt.plot(np.arange(360)/5,p_select,label='power')
    L2=plt.plot(np.arange(360)/5,np.ones(360)*p_mean,color='red',linestyle='--',label='mean power')
    L3=plt.plot(np.arange(360)/5,np.ones(360)*p_mean_b,color='black',linestyle='dashdot',label='mean power of basis')
    plt.legend()
    #plt.show()
    """
    f = open('energy_pure_75.csv', 'a')  # the file name
    f.writelines("{:.2f}".format(p_mean))
    f.writelines(',')
    f.writelines("{:.2f}".format(energy))
    f.writelines('\n')
    f.close()
    
    """

print(np.mean(t))