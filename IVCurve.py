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

Time = []
T = []
Vds = []
I = []
for c in b:
    Time.append(c[0])
    T.append(c[1])
    I.append(c[2])
    Vds.append(c[3])

plt.style.use('ggplot')
###画布预设置###
fig = plt.figure()#figsize=(4, 4), dpi=200
#ax = axisartist.Subplot(fig, 111) 
#fig.add_axes(ax)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
#ax.axis[:].set_visible(False)#通过set_visible方法设置绘图区所有坐标轴隐藏
#ax.axis["x"] = ax.new_floating_axis(0,0)#ax.new_floating_axis代表添加新的坐标轴
#ax.axis["x"].set_axisline_style("->", size = 2.0)#给x坐标轴加上箭头
#添加y坐标轴，且加上箭头
#ax.axis["y"] = ax.new_floating_axis(1,0)
#ax.axis["y"].set_axisline_style("->", size = 2.0)
#设置x、y轴上刻度显示方向
#ax.axis["x"].set_axis_direction("bottom")
#ax.axis["y"].set_axis_direction("left")
#plt.rcParams['xtick.direction'] = 'in'
#plt.rcParams['ytick.direction'] = 'in'
#数据导入
plt.plot(Vds[:], I[:], 'k', ls = "-", alpha = 0.8 ) #c = 'tab:orange',

#设置取值范围
#plt.xlim([-11, 11])
plt.ylim(min(I)*1.1, max(I)*1.1)

#设置显示坐标轴刻度
#plt.xticks([-2, -1, 1, 2],[r'-2', r'-1', r'1', r'2'])
#plt.yticks([-300, #-200, 
#-100, 100, #200, 
#300],['-300', #'-200', 
#'-100', '100', #'200', 
#'300'])

#设置坐标轴刻度
#my_x_ticks = np.linspace(-10, 10, 6) #如果这里用了np.arrange，最后一个数字取不到
#my_y_ticks = np.arange(2)
#plt.xticks(my_x_ticks)
#plt.yticks(my_y_ticks)

#文字
#plt.text(1.5, 0.5e-8, "Forward", c = "tab:orange")
#plt.text(0.5, 1.5e-8, 'Backward', c= "tab:blue")   
#plt.text(-2, 2.5e-8, '$V_{G1}=+2\,\mathrm{V}, V_{G2}=-2\,\mathrm{V}$', c= "k")   

T=np.array(T)
ax = fig.add_subplot()
ax.tick_params(direction='in')

points = np.array([Vds, I]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize(min(T), max(T))
lc = LineCollection(segments, cmap='viridis')##viridis##
# Set the values used for colormapping
lc.set_array(T)
line = ax.add_collection(lc)
lc.set_linewidth(.5)
fig.colorbar(line)
plt.xlim(-1, 1)
plt.ylim(min(I), max(I))

plt.xlabel("$V_{DS}\,\mathrm{(V)}$")
plt.ylabel('$I_{DS}\,\mathrm{(A)}$')

#图片输出
plt.savefig('<filename>.svg')
plt.show()