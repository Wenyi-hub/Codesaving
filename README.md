# Codesaving

---

1. [doping program](C:\Users\wywu\OneDrive\文档\代码\Electronic tranport.py)，如何读取文件，数据预处理的一些代码。

2. [I-V curve](C:\Users\wywu\OneDrive - RLS ,inc\JOB\Data\PhD DATA\Transportation\InSe\2019_12_26_InSe-236)，设置十字坐标系，线条颜色渐变。

3. [Raman data ](C:\Users\wywu\OneDrive\文档\代码\Raman data fitting include original data.py)Raman数据的读取，自动寻峰，去除baseline。

   > 如果使用`plt.plot`输出image，刻度线朝向的代码为`plt.rcParams['xtick.direction'] = 'in'`
   >
   > 如果使用`ax`输出image，可以使用`ax.ticks_params(axis = 'x', labelcolor = color, direction = 'in')`来设置，
   >
   > **这里的`color`在设置画布时，就可以用 `color  = tab:blue`来设置。**

4. [一张图导入多个.txt文件]()，以[Raman](C:\Users\wywu\OneDrive\文档\代码\Batch processing Raman files.py)以及[Hall](C:\Users\wywu\OneDrive\文档\代码\Batch processing Hall files.py)为例，输出多条数据，包含了读取该文件夹地址，读取一个文件夹内多个文件的代码。

5. [同时处理多个.txt文件]

6. [Hall测试](C:\Users\wywu\OneDrive\文档\代码\HallMeasurement.py)，清洗数据的时候将噪点赋空值（还没有实现）。

7. [将一个文件夹里的图片写入到ppt中]

8. [AFM](C:\Users\wywu\OneDrive\文档\代码)，包含了倒序列表的方法，图片中插入文本的方法。