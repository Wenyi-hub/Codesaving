from sklearn import linear_model
import numpy as np
reg = linear_model.LinearRegression()
#假设数据是data
data=[1.71490784773981,2.71490784773981,3.71490784773981,4.71490784773981]
#对应序号是 range(len(data))
reg.fit (np.array(range(len(data))).reshape(-1,1),np.array(data).reshape(-1,1))
 
#斜率为
print(reg.coef_)
#截距为
print(reg.intercept_)