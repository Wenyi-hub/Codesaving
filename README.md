# Codesaving

---

<center>

<img src = 'https://raw.githubusercontent.com/Wenyi-hub/ImageCloudSaving/master/image/Interior-of-a-Kitchen-1815-Martin-Drolling-oil-painting-1.jpg'
style = 1%
alig = center>

</center>

1. [doping program](https://github.com/Wenyi-hub/Codesaving/blob/master/ElectronicTranport.py)，如何读取文件，数据预处理的一些代码。

2. [I-V curve]()，设置十字坐标系，线条颜色渐变。

3. [Raman data](https://github.com/Wenyi-hub/Codesaving/blob/master/RamanDataFittingIncludeOriginalData.py)Raman数据的读取，自动寻峰，去除baseline。

   > 如果使用`plt.plot`输出image，刻度线朝向的代码为`plt.rcParams['xtick.direction'] = 'in'`
   >
   > 如果使用`ax`输出image，可以使用`ax.ticks_params(axis = 'x', labelcolor = color, direction = 'in')`来设置，
   >
   > **这里的`color`在设置画布时，就可以用 `color  = tab:blue`来设置。**

4. 以[Raman](https://github.com/Wenyi-hub/Codesaving/blob/master/BatchProcessingRamanFiles.py)以及[Hall](https://github.com/Wenyi-hub/Codesaving/blob/master/BatchProcessingHallFiles.py)为例，同时处理多个.txt文件，输出多条数据，包含了读取该文件夹地址，读取一个文件夹内多个文件的代码。

5. [Hall测试](C:\Users\wywu\OneDrive\文档\代码\HallMeasurement.py)，清洗数据的时候将噪点赋空值（还没有实现）。

6. [将一个文件夹里的图片写入到ppt中](https://github.com/Wenyi-hub/Codesaving/blob/master/WriteImageIntoPptx.py)

   > Python os.chdir() 方法，可以改变当前路径到指定地址`os.chdir(path)`

7. [AFM]([C:\Users\wywu\OneDrive\文档\代码](https://github.com/Wenyi-hub/Codesaving/blob/220929806b8222f063cc7b320366540e2d146f83/AFM.py))，包含了倒序列表的方法，图片中插入文本的方法。

---
