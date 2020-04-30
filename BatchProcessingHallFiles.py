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
    #print(i)
    with open(os.getcwd() + i) as file:
        next(file) # The text in the first line is skipped, and it will not be read again below. I should find a simple skip, Just skip not delete .
        lines = file.readlines()
    data = []
    b = []
    a = []
    for line in lines:
        data = line.split()
        a = list(map(float, data[2:])) # Skip the two columns of date and time, because it ca n’t be converted and it ’s not needed.
        b.append(a)

    B = []
    Ra = []
    Rb = []
    for c in b:
        B.append(c[4])
        Ra.append(c[len(a)-4])
        Rb.append(c[len(a)-3])
    RH = (np.array (Ra) + np.array(Rb))/2

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
    z = baseline_als(RH, 10, 0.0001) # parameter:(<Spectra Data>, lambdd<2nd derivative constraint>, P<Weighting of positive residuals>, maxit<Maximum number of iterations>

    peaks, _ = find_peaks(RH, height=0.1, prominence=40)
    RH *= 1
    peaks = peaks.tolist()
    peaks_float = []
    for num in peaks:
        peaks_float.append(float(num))
    #x1 = np.array(x)
    #y1 = np.array(y)
    plt.xlabel('$B\,\mathrm{(T)}$')
    plt.ylabel('$R_H\,\mathrm{(T)}$')
    plt.plot(B, RH, 'o')
    #plt.plot(x, z, '--')

plt.savefig('Batch processing Hall files.svg')

plt.show()






