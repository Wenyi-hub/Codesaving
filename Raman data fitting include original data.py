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

### File reading, and arrange all the text in columns ###
with open("<filename>.txt") as file:
    lines = file.readlines()

### Data format, Split the data in each row, and convert string to float ###
data = []
b = []
c = []
for line in lines:
    data = line.split()  
    b.append(data)
c = b[39:]

### selet parameters ###
x = []
y = []
for d in c:
    x.append(d[0])
    y.append(d[1])

### convert x,y to float type ###
x_float = []
for num in x:
    x_float.append(float(num))
x = x_float
y_float = []
for num in y:
    y_float.append(float(num))
y = y_float

### plot orignal data### 
fig = plt.figure()
plt.xlabel('Raman shift$\,\mathrm{(cm^{-1})}$')
plt.plot(x, y, '-')

### use asymmtric least squre fit Raman data ###
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
z = baseline_als(y, 1000, 0.01) # parameter:(<Spectra Data>, lambdd<2nd derivative constraint>, P<Weighting of positive residuals>, maxit<Maximum number of iterations>

plt.plot(x,z) # plot fitting line
plt.plot(x,y-z) # plot Raman data fitting 

### peaks searching ###
peaks, _ = find_peaks(y, height=0.1, prominence=40)
y *= 1 # set positive peaks searching
peaks = peaks.tolist()
peaks_float = []
for num in peaks:
    peaks_float.append(float(num))
x = np.array(x)
y = np.array(y)

### mark peaks in both data###
plt.plot(x[peaks], y[peaks], '*', ms = '10', c = 'r')
plt.plot(x[peaks], y[peaks]-z[peaks], "*", ms ='10', c = 'r')

### image output###
plt.savefig('<filename>.svg')
plt.show()
