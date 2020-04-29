### Module import ###
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import lines
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import find_peaks
from numpy import *

### File reading, and arrange all the text in columns ###
with open("<filename>.txt") as file:
    next(file)
    lines = file.readlines()

### Data format, Split the data in each row, and convert string to float ###
data = []
b = []
for line in lines:
    data = line.split()  
    a = list(map(float, data)) #  convert to float
    b.append(a)

### selet parameters ###
x = []
y = []
for d in b:
    x.append(d[0])
    y.append(d[1])

### define a asymmtric least squre fuction###
def baseline_als(Y, lam, p, niter=10):
    L = len(Y)
    D = sparse.csc_matrix(np.diff(np.eye(L), 2))
    w = np.ones(L)
    for i in range(niter):
      W = sparse.spdiags(w, 0, L, L)
      Z = W + lam * D.dot(D.transpose())
      z = spsolve(Z, w*Y)
      w = p * (Y > z) + (1-p) * (Y < z)
    return z

### use asymmtric least squre fit AFM data, select two stage fitting straght line and selet these two lines range to plug in [:]###
z1 = baseline_als(y[:], 1000, 0.01) # parameter:(<Spectra Data>, lambdd<2nd derivative constraint>, P<Weighting of positive residuals>, maxit<Maximum number of iterations>
z2 = baseline_als(y[:], 1000, 0.01) # parameter:(<Spectra Data>, lambdd<2nd derivative constraint>, P<Weighting of positive residuals>, maxit<Maximum number of iterations>

### get averge of two fitting lines ###
z1 = (z1[::1] + z1[::-1])/2
z2 = (z2[::1] + z2[::-1])/2

### plot orignal data### 
fig = plt.figure()
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.xlabel('Distance$\,\mathrm{(\mu m)}$')
plt.ylabel('Height$\,\mathrm{(nm)}$')
plt.plot(x, y, '-')

### plot fitting data, x need has same range with z1/z2 ###
plt.plot(x[:],z1, color = 'orange', ls = '--')
plt.plot(x[:],z2, color = 'orange', ls = '--')

### annote the height ###
text = str(round(abs(np.mean(z1)-np.mean(z2)),2))+r'$\,\mathrm{nm}$' # plug in the height result and its unit as text for marking figure
plt.text(3, 1, text, fontsize=15) # Choose the right location and fontsize

### image output ###
plt.savefig('<filename>.svg')
plt.show()
