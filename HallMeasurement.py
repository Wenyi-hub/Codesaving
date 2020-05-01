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

### This part is a bit lengthy, I do n’t know how to simplify 
# if only plot Hall effect measurement, just read B, Ra and Rb###
B = []
Ra = []
Rb = []
for c in b:
    B.append(c[4])
    Ra.append(c[len(a)-4])
    Rb.append(c[len(a)-3])

### set a figure canvas ###
fig = plt.figure()

RH = (np.array (Ra) + np.array(Rb))/2
#plt.ylim()
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.xlabel('B$\,\mathrm{(T)}$')
plt.ylabel('$R_H\,\mathrm{(\Omega)}$')
plt.plot(B, RH, 'o')

### image output ###
fig.tight_layout() # 'otherwise the right y-label is slightly clipped' I just copy this but haven't found it worked 
plt.savefig('<filename>.svg') # Seleting prefer file type   
plt.show()
plt.close()