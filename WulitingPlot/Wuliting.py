# -*- coding: utf-8 -*-
"""
五里亭用于作图的各个模块
"""
import matplotlib.pyplot as plt  # 使用import导入模块matplotlib.pyplot，并简写成plt  
import numpy as np  # 使用import导入模块numpy，并简写成np
class Wuliting(object):
    """
       Wuliting五里亭用于作图的各个模块
    """

    def PlotE1QDCJ(self):
        """
           绘制E匝道第1阶段桥墩沉降
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

        legendList=['E-QD111','E-QD112','E-QD113','E-QD114','E-QD115','E-QD123']
        markerList=['o','s','p','x','v','h']
        xticksLabelList=['20161105','20161206','20161213','20161225','20170108','20170116','20170205','20170212','20170224']
        x = np.array([1,2,3,4,5,6,7,8,9])
        yList=[
            np.array([0,0.21,0.02,-1.32,-1.34,-1.11,-1.33,-1.52,-1.65])
            ,np.array([0,-0.18,-0.23,-0.23,-1.93,-1.96,-2.67,-2.78,-2.58])
            ,np.array([0,-0.33,-0.47,-1.02,-1.55,-1.42,-1.63,-1.82,-1.68])
            ,np.array([0,0.31,-0.32,-0.62,-0.72,-0.63,-0.53,-0.35,-0.36])
            ,np.array([0,0.11,0.29,0.25,0.22,0.19,0.12,0.35,0.21])
            ,np.array([0,0.14,0.33,0.29,0.12,0.27,0.27,0.13,0.21])
        ]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('时间')
        plt.ylabel('沉降（mm）')
        plt.title('E匝道第一阶段桥墩沉降数据时程曲线图')  # 设置标题
        plt.show()

    def PlotE2ZL112(self):
        """
           绘制E匝道第2阶段主梁112#截面竖向位移
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

        legendList=['E-D1','E-D4']
        markerList=['o','s']
        xticksLabelList=['托换前','顶升至最大高度','千斤顶卸荷后','托换过程最大值','2月28日18:00','3月1日18:00']
        x = np.array([1,2,3,4,5,6])
        yList=[
            np.array([0,10.78,5.11,6.02,5.89,5.98])
            ,np.array([0,7.94,5.23,5.3,6.54,6.13])
        ]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('时间')
        plt.ylabel('竖向位移（mm）')
        plt.title('E匝道第二阶段主梁112#截面竖向位移监测结果')  # 设置标题
        plt.show()

    def PlotE2ZL113(self):
        """
           绘制E匝道第2阶段主梁113#截面竖向位移
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

        legendList=['E-D2','E-D6']
        markerList=['o','s']
        xticksLabelList=['托换前','顶升至最大高度','千斤顶卸荷后','2月28日18:00','3月1日18:00','3月2日18:00']
        x = np.array([1,2,3,4,5,6])
        yList=[
            np.array([0,5.18,3.49,3.21,3.68,3.78])
            ,np.array([0,5.98,4.85,4.63,4.12,4.13])
        ]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('时间')
        plt.ylabel('竖向位移（mm）')
        plt.title('E匝道第二阶段主梁113#截面竖向位移监测结果')  # 设置标题
        plt.show()

    def PlotE2YB(self):
        """
           绘制E匝道第2阶段主梁应变监测结果
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

        legendList=['E-D2','E-D6']
        markerList=['o','s']
        xticksLabelList=['托换前','顶升至最大高度','千斤顶卸荷后','2月28日18:00','3月1日18:00','3月2日18:00']
        x = np.array([1,2,3,4,5,6])
        yList=[
            np.array([0,5.18,3.49,3.21,3.68,3.78])
            ,np.array([0,5.98,4.85,4.63,4.12,4.13])
        ]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=markerList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('时间')
        plt.ylabel('竖向位移（mm）')
        plt.title('E匝道第二阶段主梁113#截面竖向位移监测结果')  # 设置标题
        plt.show()