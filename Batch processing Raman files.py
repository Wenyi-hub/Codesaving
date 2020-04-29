import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import lines
import matplotlib.ticker as mtick
from matplotlib.ticker import FuncFormatter
from scipy import sparse
from scipy.sparse.linalg import spsolve
from scipy.signal import find_peaks
from sklearn.decomposition import PCA
import glob
import os

f = glob.glob(r'./*.txt')
fig = plt.figure()

for i in f:
    print(i)
    with open(os.getcwd()+i) as file:
        lines = file.readlines()
    data = []
    b = []
    c = []
    for line in lines:
        data = line.split()
        b.append(data)
    c = b[39:]

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

    plt.rcParams['xtick.direction'] = 'in'
    plt.yticks([])
    plt.xlabel('Raman shift$\,\mathrm{(cm^{-1})}$')

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
    z = baseline_als(y, 10, 0.0001) # parameter:(<Spectra Data>, lambdd<2nd derivative constraint>, P<Weighting of positive residuals>, maxit<Maximum number of iterations>

    peaks, _ = find_peaks(y, height=0.1, prominence=40)
    y *= 1
    peaks = peaks.tolist()
    peaks_float = []
    for num in peaks:
        peaks_float.append(float(num))
    x1 = np.array(x)
    y1 = np.array(y)
    plt.plot(x, y, '-')
    #plt.legend(handles = l, labels = i)
    #plt.plot(x, z, '--')
    #plt.plot(x,y-z)
    plt.plot(x1[peaks], y1[peaks], '*', ms = '10', c = 'r')
#plt.plot(x1[peaks], y1[peaks]-z[peaks], "*", ms ='10', c = 'r')

#plt.savefig('Contrast of InSe-81 Raman.svg')

plt.show()

plt.close()
'''
pca = PCA(n_components = 0.5)
pca.fit([y])
y_reduction = pca.transform([y])
y_restore = pca.inverse_transform(y_reduction)
x =np.arange(min(x), max(x), ((max(x)-min(x))/y_restore.size))
y = np.array(y_restore)
#plt.plot(x, y[0],)
'''





