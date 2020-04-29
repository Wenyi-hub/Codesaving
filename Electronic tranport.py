### Module import ###
# coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import lines
from matplotlib import pyplot, spines
from datetime import datetime
import matplotlib.dates as mdates
from datetime import date
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter
from matplotlib.collections import LineCollection
import mpl_toolkits.axisartist as axisartist

### File reading, and arrange all the text in columns ###
with open("<filename>.txt") as file:
    next(file) # The text in the first line is skipped, and it will not be read again below. I should find a simple skip, Just skip not delete .
    lines = file.readlines()

### Data format, Split the data in each row, and convert string to float ###
data = []
b = []
for line in lines:
    data = line.split()  
    a = list(map(float, data[2:])) # Skip the two columns of date and time, because it ca n’t be converted and it ’s not needed.
    b.append(a)

### This part is a bit lengthy, I do n’t know how to simplify ###
Time = []
T = []
Vg = []
Ig = []
Rs = []
for c in b:
    Time.append(c[0])
    T.append(c[1])
    Vg.append(c[2])
    Ig.append(c[3])
    Rs.append(c[len(a)-1])

### Do some processing on the timestamp, it can be used as a parameter plotting ###
Time[:] = [(x - Time[0])/3600000 for x in Time]

### set a figure canvas ###
fig = plt.figure()

### plot first data ###
color = 'tab:blue' # set color
ax1 = fig.add_subplot(212) # set the position 
ax1.set_xlabel('Time (h)') 
#ax1.set_xlim([0,2.5])
ax1.set_ylabel('$V_G\,\mathrm{(V)}$', color=color) 
ax1.plot(Time, Vg, color=color) 
ax1.tick_params(axis='y', labelcolor=color, direction = 'in') 
ax1.tick_params(axis='x', direction = 'inout')

### plot second data ###
ax2 = ax1.twinx() # instantiate a second axes that shares the same x-axis 
color = 'tab:orange' 
ax2.set_ylabel('$I_G\,\mathrm{(A)}$', color=color) # we already handled the x-label with ax1 
ax2.plot(Time, Ig, color=color) 
ax2.tick_params(axis='y', labelcolor=color, direction = 'in') 

ax3 = fig.add_subplot(211)
color = 'black' 
#ax3.set_yscale("log") # use log Axis instead Liner
#ax3.set_xlim([0,2.5])
ax3.set_xticklabels([])
ax3.set_ylabel('$R_S\,\mathrm{(\Omega/\u25FB)}$', color=color) 
ax3.plot(Time, Rs, color=color) 
ax3.tick_params(axis='y', labelcolor=color, direction = 'in') 
ax3.tick_params(axis='x', which = 'both', direction = 'inout')


ax4 = ax3.twinx() # instantiate a second axes that shares the same x-axis 
color = 'tab:red' 
ax4.set_ylabel('$T\,\mathrm{(K)}$', color=color) # we already handled the x-label with ax3 
ax4.plot(Time, T, color=color) 
ax4.tick_params(axis='y', labelcolor=color, direction = 'in') 

### image output ###
fig.tight_layout() # 'otherwise the right y-label is slightly clipped' I just copy this but haven't found it worked 

#plt.savefig('<filename>.svg') # Seleting prefer file type   
plt.show()
plt.close()