# This code is using for plot

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import csv
import scipy.stats as st
import math
"""

with open('energy_pure_70.csv', 'r',encoding='utf-8')as f_0:
    f_0=csv.reader(f_0)
    e_0 = list(f_0)
    power_0 = [i[0] for i in e_0] 
    energy_0 = [i[1] for i in e_0] 
with open('energy_pure_71.csv', 'r',encoding='utf-8')as f_1:
    f_1=csv.reader(f_1)
    e_1 = list(f_1)
    power_1 = [i[0] for i in e_1] 
    energy_1 = [i[1] for i in e_1] 
with open('energy_pure_72.csv', 'r',encoding='utf-8')as f_2:
    f_2=csv.reader(f_2)
    e_2 = list(f_2)
    power_2 = [i[0] for i in e_2] 
    energy_2 = [i[1] for i in e_2] 
with open('energy_pure_73.csv', 'r',encoding='utf-8')as f_3:
    f_3=csv.reader(f_3)
    e_3 = list(f_3)
    power_3 = [i[0] for i in e_3] 
    energy_3 = [i[1] for i in e_3] 
with open('energy_pure_74.csv', 'r',encoding='utf-8')as f_4:
    f_4=csv.reader(f_4)
    e_4 = list(f_4)
    power_4 = [i[0] for i in e_4] 
    energy_4 = [i[1] for i in e_4] 
with open('energy_pure_75.csv', 'r',encoding='utf-8')as f_5:
    f_5=csv.reader(f_5)
    e_5 = list(f_5)
    power_5 = [i[0] for i in e_5] 
    energy_5 = [i[1] for i in e_5] 

"""
with open('energy_70.csv', 'r',encoding='utf-8')as f_0:
    f_0=csv.reader(f_0)
    e_0 = list(f_0)
    power_0 = [i[0] for i in e_0] 
    energy_0 = [i[1] for i in e_0] 
with open('energy_71.csv', 'r',encoding='utf-8')as f_1:
    f_1=csv.reader(f_1)
    e_1 = list(f_1)
    power_1 = [i[0] for i in e_1] 
    energy_1 = [i[1] for i in e_1] 
with open('energy_72.csv', 'r',encoding='utf-8')as f_2:
    f_2=csv.reader(f_2)
    e_2 = list(f_2)
    power_2 = [i[0] for i in e_2] 
    energy_2 = [i[1] for i in e_2] 
with open('energy_73.csv', 'r',encoding='utf-8')as f_3:
    f_3=csv.reader(f_3)
    e_3 = list(f_3)
    power_3 = [i[0] for i in e_3] 
    energy_3 = [i[1] for i in e_3] 
with open('energy_74.csv', 'r',encoding='utf-8')as f_4:
    f_4=csv.reader(f_4)
    e_4 = list(f_4)
    power_4 = [i[0] for i in e_4] 
    energy_4 = [i[1] for i in e_4] 
with open('energy_75.csv', 'r',encoding='utf-8')as f_5:
    f_5=csv.reader(f_5)
    e_5 = list(f_5)
    power_5 = [i[0] for i in e_5] 
    energy_5 = [i[1] for i in e_5] 

fig_width = 6.5
barwidth = 0.4
bardistance = barwidth * 1.7
colordict = {
            'compute_forward': '#0077BB',
            'store_forward': '#DDAA33',
            'store_forward_ia': '#009988',
            'orange': '#EE7733',
            'red': '#993C00',
            'blue': '#3340AD'}

markerdict = {
            'compute_forward': 'o',
            'store_forward': 'v',
            'store_forward_ia': 's'}

colorlist = ['#DDAA33', '#7ACFE5', '#3F9ABF',
            '#024B7A',  '#0077BB', '#009988']

markerlist = ['o', 'v', '^', '>', 'p', 's']

power_0=list(map(float,power_0))
power_1=list(map(float,power_1))
power_2=list(map(float,power_2))
power_3=list(map(float,power_3))
power_4=list(map(float,power_4))
power_5=list(map(float,power_5))

energy_0=list(map(float,energy_0))
energy_1=list(map(float,energy_1))
energy_2=list(map(float,energy_2))
energy_3=list(map(float,energy_3))
energy_4=list(map(float,energy_4))
energy_5=list(map(float,energy_5))
energy_0[:] = [x / 1000 for x in energy_0]
energy_1[:] = [x / 1000 for x in energy_1]
energy_2[:] = [x / 1000 for x in energy_2]
energy_3[:] = [x / 1000 for x in energy_3]
energy_4[:] = [x / 1000 for x in energy_4]
energy_5[:] = [x / 1000 for x in energy_5]
"""
box= plt.boxplot([energy_0[0:79],energy_1[0:79],energy_2[0:79],energy_3[0:79],\
                    energy_4[0:79],energy_5[0:79]], positions=np.arange(6), vert=True,\
                     widths=barwidth, showfliers=True, showmeans=False, patch_artist=True,
                  boxprops=dict(
                      color='black', facecolor=colorlist[0], lw=1),
                  medianprops=dict(color='black'),
                  capprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  flierprops=dict(
                      color=colorlist[0], markeredgecolor=colorlist[0], ms=4),
                  meanprops=dict(markerfacecolor='black', markeredgecolor='black'))
plt.title("The energy of CF model")
plt.xlabel("vnf number")
plt.ylabel("Energy(J)")
plt.show()
box= plt.boxplot([energy_0[80:159],energy_1[80:159],energy_2[80:159],energy_3[80:159],energy_4[80:159],energy_5[80:159]], positions=np.arange(6), vert=True, widths=barwidth, showfliers=True, showmeans=False, patch_artist=True, 
                  boxprops=dict(
                      color='black', facecolor=colorlist[0], lw=1),
                  medianprops=dict(color='black'),
                  capprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  flierprops=dict(
                      color=colorlist[0], markeredgecolor=colorlist[0], ms=4),
                  meanprops=dict(markerfacecolor='black', markeredgecolor='black'))
plt.title("The energy of SF model")
plt.xlabel("vnf number")
plt.ylabel("Energy(J)")
plt.show()
plt.show()

box= plt.boxplot([energy_0[0:49],energy_0[50:99],energy_1[0:49],energy_1[50:99],energy_2[0:49],energy_2[50:99],energy_3[0:49],energy_3[50:99],energy_4[0:49],energy_4[50:99],energy_5[0:49],energy_5[50:99]], positions=np.arange(12), vert=True, widths=barwidth, showfliers=True, showmeans=False, patch_artist=True,
                  boxprops=dict(
                      color='black', facecolor=colorlist[0], lw=1),
                  medianprops=dict(color='black'),
                  capprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  flierprops=dict(
                      color=colorlist[0], markeredgecolor=colorlist[0], ms=4),
                  meanprops=dict(markerfacecolor='black', markeredgecolor='black'))
plt.title("The energy of SF&CF model")
plt.xlabel("vnf number")
plt.ylabel("Energy(J)")
plt.ylim(top=15)
plt.show()
plt.show()
"""
box_1= plt.boxplot([energy_0[0:49],energy_1[0:49],energy_2[0:49],energy_3[0:49],energy_4[0:49],energy_5[0:49]], positions=[0.3,2.3,4.3,6.3,8.3,10.3], vert=True, widths=barwidth, showfliers=True, showmeans=False, patch_artist=True,
                  boxprops=dict(
                      color='black', facecolor=colorlist[0], lw=1, hatch = '///'),
                  medianprops=dict(color='black'),
                  capprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  flierprops=dict(
                      color=colorlist[0], markeredgecolor=colorlist[0], ms=4),
                  meanprops=dict(markerfacecolor='black', markeredgecolor='black'))

box_2= plt.boxplot([energy_0[50:99],energy_1[50:99],energy_2[50:99],energy_3[50:99],energy_4[50:99],energy_5[50:99]], positions=[0.7,2.7,4.7,6.7,8.7,10.7], vert=True, widths=barwidth, showfliers=True, showmeans=False, patch_artist=True,
                  boxprops=dict(
                      color='black', facecolor=colorlist[1], lw=1),
                  medianprops=dict(color='black'),
                  capprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  flierprops=dict(
                      color=colorlist[1], markeredgecolor=colorlist[0], ms=4),
                  meanprops=dict(markerfacecolor='black', markeredgecolor='black'))
#plt.title("Total energy")
plt.xlabel("VNF Number")
plt.ylabel("Energy(J)")
plt.ylim(top=240)   
plt.xticks((0.5,2.5,4.5,6.5,8.5,10.5), [0,1,2,3,4,5])
red_patch = mpatches.Patch(facecolor=colorlist[0], hatch = '///', label='CF')
blue_patch = mpatches.Patch(color=colorlist[1], label='SF')
plt.legend(handles=[red_patch, blue_patch],loc='upper left')
plt.show()

box_1= plt.boxplot([power_0[0:49],power_1[0:49],power_2[0:49],power_3[0:49],power_4[0:49],power_5[0:49]], positions=[0.3,2.3,4.3,6.3,8.3,10.3], vert=True, widths=barwidth, showfliers=True, showmeans=False, patch_artist=True,
                  boxprops=dict(
                      color='black', facecolor=colorlist[0], lw=1,  hatch = '///'),
                  medianprops=dict(color='black'),
                  capprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  flierprops=dict(
                      color=colorlist[0], markeredgecolor=colorlist[0], ms=4),
                  meanprops=dict(markerfacecolor='black', markeredgecolor='black'))

box_2= plt.boxplot([power_0[50:99],power_1[50:99],power_2[50:99],power_3[50:99],power_4[50:99],power_5[50:99]], positions=[0.7,2.7,4.7,6.7,8.7,10.7], vert=True, widths=barwidth, showfliers=True, showmeans=False, patch_artist=True,
                  boxprops=dict(
                      color='black', facecolor=colorlist[1], lw=1),
                  medianprops=dict(color='black'),
                  capprops=dict(color='black'),
                  whiskerprops=dict(color='black'),
                  flierprops=dict(
                      color=colorlist[1], markeredgecolor=colorlist[0], ms=4),
                  meanprops=dict(markerfacecolor='black', markeredgecolor='black'))
#plt.title("Power of pICA")
plt.xlabel("VNF Number")
plt.ylabel("Power(mW)")
plt.ylim(top=175)   
plt.xticks((0.5,2.5,4.5,6.5,8.5,10.5), [0,1,2,3,4,5])
red_patch = mpatches.Patch(facecolor=colorlist[0], hatch = '///', label='CF')
blue_patch = mpatches.Patch(color=colorlist[1], label='SF')
plt.legend(handles=[red_patch, blue_patch],loc='upper left')
plt.show()

"""

mean=(energy_0[0:79],energy_0[80:159],energy_1[0:79],energy_1[80:159],energy_2[0:79],energy_2[80:159],energy_3[0:79],energy_3[80:159],energy_4[0:79],energy_4[80:159],energy_5[0:79],energy_5[80:159])
mean_1=(power_0[0:79],power_0[80:159],power_1[0:79],power_1[80:159],power_2[0:79],power_2[80:159],power_3[0:79],power_3[80:159],power_4[0:79],power_4[80:159],power_5[0:79],power_5[80:159])
print(np.median(mean,axis=1))
print(np.mean(mean,axis=1))
print(np.median(mean_1,axis=1))
print(np.mean(mean_1,axis=1))
"""
