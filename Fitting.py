import numpy as np
import matplotlib.pyplot as plt


class LinearRegression():
    def __init__(self):
        self.coef_ = 0
        self.intercept_ = 0
        self.X = None
        self.y = None
        self.y_pred = None
        self.sse = 0
        self.mse = 0
        self.rmse = 0
        self.mae = 0
        self.ssr = 0
        self.sst = 0
        self.r2 = 0

    def input_data(self, x, y):
        self.X = np.array(x)
        self.y = np.array(y)

    def solve(self):
        x = self.X
        y = self.y
        self.coef_ = sum((x - x.mean()) * (y - y.mean())) / sum((x - x.mean())**2)
        self.intercept_ = y.mean() - self.coef_ * x.mean()
        self.y_pred = np.array(x * self.coef_ + self.intercept_)

    def predict(self, x_new):
        return self.coef_ * x_new + self.intercept_

    def plot(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.X, self.y, marker='+', color='green')
        plt.plot(self.X, self.y_pred, '-r')
        plt.text(1, 7.9, 'a:  {0:.2f}'.format(self.coef_), weight='bold', color='black', fontsize=16)
        plt.text(1, 7.7, 'b:  {0:.2f}'.format(self.intercept_), weight='bold', color='black', fontsize=16)
        plt.text(1, 7.5, 'R2: {0:.2f}'.format(self.r2), weight='bold', color='black', fontsize=16)
        plt.text(1, 7.3, 'MSE:  {0:.2f}'.format(self.mse), weight='bold', color='black', fontsize=16)
        plt.show()

    def evaluate(self):
        self.sse = sum((self.y - self.y_pred) ** 2)
        self.mse = sum((self.y - self.y_pred) ** 2) / len(self.X)
        self.rmse = np.sqrt(self.mse)
        self.mae = np.mean(np.abs(self.y - self.y_pred))
        self.ssr = sum((self.y_pred - np.mean(self.y)) ** 2)
        self.sst = sum((self.y - np.mean(self.y)) ** 2)
        self.r2 = self.ssr / self.sst

# 训练数据
X = np.array([1, 3, 5, 7])
y = np.array([5, 6, 7, 8])

# 创建模型
lr = LinearRegression()
lr.input_data(X, y)

# 求解
lr.solve()
lr.evaluate()

# 预测
x = 10
print('当X = 10时，y =', lr.predict(x))

# 画图
lr.plot()

# 训练数据
X = np.array([1, 3, 5, 7, 4, 6, 8])
y = np.array([5, 6, 7, 8, 6, 8, 7])

# 创建模型
lr = LinearRegression()
lr.input_data(X, y)

# 求解
lr.solve()
lr.evaluate()

# 预测
x = 10
print('当X = 10时，y =', lr.predict(x))

# 画图
lr.plot()