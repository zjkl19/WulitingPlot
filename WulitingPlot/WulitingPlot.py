# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt  # 使用import导入模块matplotlib.pyplot，并简写成plt  
import numpy as np  # 使用import导入模块numpy，并简写成np
x = np.linspace(-1, 1, 50)  # 使用np.linspace定义x：范围是(-1,1);个数是50.   
y = 2*x + 1  # 仿真一维数据组(x ,y)表示曲线1.
plt.figure()  # 使用plt.figure定义一个图像窗口. 
plt.plot(x, y)  # 使用plt.plot画(x ,y)曲线.
plt.title('fig1')  # 设置标题
plt.show()  #  使用plt.show显示图像.

