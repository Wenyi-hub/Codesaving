import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

np.random.seed(0)

Y = np.zeros(1000)

# insert @deinonychusaur's peaker function here

#peaks, _ = find_peaks(Y, height=1, distance=100)

# make data noisy
Y = Y + 10e-4 * np.random.randn(len(Y))
# find_peaks gets the maxima, so we multiply our signal by -1
#Y *= -1 
# get the actual peaks
peaks, _ = find_peaks(Y, height=0.002, distance=100)
print(peaks)
print(Y[peaks])
peaks = np
# multiply back for plotting purposes
Y *= 1
plt.plot(Y)
plt.plot(peaks, Y[peaks], "x")
plt.show(h)