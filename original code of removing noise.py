import numpy as np
import matplotlib.pyplot as plt


X = np.empty((100,2))
X [:, 0] = np.random.uniform(0, 100, size = 100 )
X [:, 1] = 0.75 * X [:, 0] +3 + np.random.normal(0, 5, size = 100)

plt.scatter(X [:, 0], X [:, 1 ])
plt.show()

from sklearn.decomposition import PCA

pca = PCA(n_components=1)
pca.fit(X)
X_reduction = pca.transform(X)


# inverse_transform(低维数据)：将低维数据升为高维数据
X_restore = pca.inverse_transform(X_reduction)

plt.scatter(X_restore[:,0], X_restore[:,1])
plt.show()