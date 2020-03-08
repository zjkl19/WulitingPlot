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
    def __init__(self):
        self.MarkerList=['o','s','p','x','v','h']    #默认的MarkerList

    def _PlotChart(self,plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList):
        """
           绘制图形功能代码
        """

        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=self.MarkerList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList,rotation=90)    #自定义标签
        plt.xlabel(xlabelText)
        plt.ylabel(ylabelText)
        #plt.title(title)  # 设置标题
        plt.show()

    def PlotD1QDCJ(self):
        """
           绘制D匝道第1阶段桥墩沉降监测数据
        """

        title='D匝道桥墩沉降监测结果'
        xlabelText='时间'
        ylabelText='沉降（mm）'
        legendList=['D-QD-140','D-QD-141','D-QD-142','D-QD-143']
        xticksLabelList=['0729','1107','1114','1116','1118','1122','1128']
        yList=[
            np.array([0,0.21,-0.45,-0.44,-0.26,0.19,-0.11])
            ,np.array([0,0.05,-0.29,-0.25,-0.09,-0.09,-0.58])
            ,np.array([0,-0.18,-0.15,-0.18,-0.04,0.27,0.02])
            ,np.array([0,-0.17,-0.33,-0.27,-0.32,0.23,-0.06])]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotD2ZLWY(self):
        """
           绘制D匝道第2阶段主梁竖向位移
        """

        title='D匝道第二阶段主梁竖向位移监测结果'
        xlabelText='时间'
        ylabelText='竖向位移（mm）'
        legendList=['D-D1','D-D3']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','12月3日18:00','12月4日18:00','12月5日18:00']
        yList=[
            np.array([0,6.95,4.99,5.16,5.29,5.33])
            ,np.array([0,7.95,5.95,5.87,5.98,5.97])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotD2ZLYB(self):
        """
           绘制D匝道第二阶段主梁应变监测结果
        """

        title='D匝道第二阶段主梁应变监测结果'
        xlabelText='时间'
        ylabelText='应变值（με）'
        legendList=['E-Y1','E-Y2']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','12月3日18:00','12月4日18:00','12月5日18:00']        
        yList=[
            np.array([0,-24,-22,-18,-15,-16])
            ,np.array([0,-18,-17,-19,-16,-19])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotD3QDCJ(self):
        """
           绘制D匝道第3阶段桥墩沉降监测数据
        """

        title='D匝道第3阶段桥墩沉降监测结果'
        xlabelText='时间'
        ylabelText='沉降（mm）'
        legendList=['D-QD-140','D-QD-142','D-QD-143']
        xticksLabelList=['1210','1213','1222','0102','0105','0109','0113','0116','0126','0205','0208','0212','0216','0220','0224','0228','0303','0307','0310','0314','0317','0320','0324','0327','0407','0410']
        yList=[
            np.array([0.05,0.12,0.13,0.35,0.45,1.02,0.94,0.87,0.77,1.23,1.06,1.18,1.02,1.00,1.39,1.15,1.01,0.98,0.65,0.78,0.66,0.53,0.43,0.36,0.33,0.22])
            ,np.array([-0.01,-0.05,0.17,0.35,1.02,1.32,1.21,1.17,1.12,1.21,1.38,1.25,1.04,0.95,1.09,1.21,1.15,1.01,0.53,0.65,0.58,0.66,0.58,0.62,0.37,0.29])
            ,np.array([-0.11,-0.16,-0.35,-0.35,0.02,0.53,0.44,0.37,0.33,0.45,0.31,0.33,0.37,0.51,0.25,0.33,0.32,0.33,0.30,0.32,0.26,0.28,0.31,0.33,0.35,0.33])]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotD4ZLWY(self):
        """
           绘制D匝道第4阶段主梁竖向位移
        """

        title='D匝道第四阶段主梁竖向位移监测结果'
        xlabelText='时间'
        ylabelText='竖向位移（mm）'
        legendList=['D-D1','D-D3']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','4月12日18:00','4月13日18:00','4月14日18:00']
        yList=[
            np.array([3.44,10.87,6.32,6.34,6.26,6.32])
            ,np.array([4.12,11.45,6.82,6.79,6.71,6.77])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotD4ZLYB(self):
        """
           绘制D匝道第4阶段主梁应变监测结果
        """

        title='D匝道第四阶段主梁应变监测结果'
        xlabelText='时间'
        ylabelText='应变值（με）'
        legendList=['E-Y1','E-Y2']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','4月12日18:00','4月13日18:00','4月14日18:00']        
        yList=[
            np.array([0,-16,-16,-17,-16,-18])
            ,np.array([0,-21,-18,-19,-20,-16])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotD5QDCJ(self):
        """
           绘制D匝道第5阶段桥墩沉降监测数据
        """

        title='D匝道第五阶段桥墩沉降监测数据'
        xlabelText='时间'
        ylabelText='沉降（mm）'
        legendList=['110#','111#','112#新','113#新','114#','123#']
        xticksLabelList=['20170510','20170525','20170610','20170625','20170710','20170725','20170810','20170825','20170910','20170925','20171010','20171025','20171110'
            ,'20171125','20171210','20171225','20180110','20180125','20180210','20180225','20180310','20180325','20180410','20180425','20180510'
            ,'20180525','20180610','20180625','20180710']
        yList=[
            np.array([0.33,0.21,0.27,0.22,0.25,0.16,0.22,0.06,0.09,0.21,0.16,0.11,0.24,0.12,0.05,0.16,0.22,0.09,0.19,0.15,0.16,0.11,0.05,0.09,0.12,-0.02,0.09,0.08,0.15])
            ,np.array([0.05,0.03,-0.06,-0.04,-0.01,0.05,0.07,0.1,0.06,0.02,0.13,0.15,0.17,0.13,0.06,0.11,0.03,0.1,0.11,0.13,0.06,-0.03,0.1,0.08,0.13,0.11,0.06,0.08,0.05])
            ,np.array([0.29,0.22,0.23,0.36,0.41,0.33,0.31,0.38,0.29,0.42,0.4,0.38,0.39,0.31,0.23,0.29,0.26,0.31,0.25,0.22,0.36,0.3,0.28,0.29,0.22,0.25,0.25,0.27,0.23])
            ,np.array([0.39,0.32,0.33,0.27,0.36,0.31,0.29,0.3,0.25,0.21,0.31,0.33,0.25,0.28,0.31,0.33,0.25,0.19,0.12,0.06,0.16,0.12,0.25,0.12,0.21,0.22,0.05,0.07,0.15])     
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

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
        #plt.title('E匝道第一阶段桥墩沉降数据时程曲线图')  # 设置标题
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
        #plt.title('E匝道第二阶段主梁112#截面竖向位移监测结果')  # 设置标题
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
        #plt.title('E匝道第二阶段主梁113#截面竖向位移监测结果')  # 设置标题
        plt.show()

    def PlotE2ZLYB(self):
        """
           绘制E匝道第2阶段主梁应变监测结果
        """
        #以下两行防止乱码
        plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
        plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

        legendList=['E-Y1','E-Y2','E-Y3','E-Y4']
        xticksLabelList=['托换前','112#墩拖换过程最大值','112#墩千斤顶卸荷后','113#墩拖换过程最大值','2月28日18:00','3月1日18:00']
        x = np.array([1,2,3,4,5,6])
        yList=[
            np.array([0,-38,-27,-26,-24,-29])
            ,np.array([0,-17,-13,-15,-16,-18])
            ,np.array([0,-4,-2,-12,-12,-12])
            ,np.array([0,0,-1,-11,-17,-13])
        ]

        plt.figure()  # 使用plt.figure定义一个图像窗口.

        for i in range(0,len(yList)):
            plt.plot(x, yList[i],marker=self.MarkerList[i])

        plt.legend(legendList)
        plt.xticks(x, xticksLabelList)    #自定义标签
        plt.xlabel('时间')
        plt.ylabel('应变值（με）')
        #plt.title('E匝道第二阶段主梁应变监测结果')  # 设置标题
        plt.show()

    def PlotE3ZLWY(self):
        """
           绘制E匝道第3阶段主梁112#截面和113#截面竖向位移
        """

        title='E匝道第三阶段主梁112#、113#截面竖向位移监测结果'
        xlabelText='时间'
        ylabelText='竖向位移（mm）'
        legendList=['E-D1','E-D4','E-D2','E-D6']
        xticksLabelList=['0301','0310','0320','0324','0327','0401','0410','0415','0418','0424','0504','0515','0601','0610','0614']        
        yList=[
            np.array([5.98,5.89,5.65,5.37,4.98,4.41,4.42,4.02,3.97,3.99,3.54,3.21,3.04,3.07,2.98])
            ,np.array([6.13,6.54,6.14,5.99,5.72,5.68,5.43,5.01,4.92,4.57,4.33,4.07,3.87,3.81,3.72])
            ,np.array([3.78,3.68,3.99,-2.75,-4.3,-4.33,-4.68,-5.55,4.23,3.56,2.78,np.nan,np.nan,np.nan,np.nan])
            ,np.array([4.13,4.12,4.02,1.06,-1.54,-3.12,-3.76,-3.98,4.22,3.78,2.99,np.nan,np.nan,np.nan,np.nan])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotE4ZLWY112(self):
        """
           绘制E匝道第4阶段主梁112#竖向位移
        """

        title='E匝道112#墩第四阶段主梁竖向位移监测结果'
        xlabelText='时间'
        ylabelText='竖向位移（mm）'
        legendList=['E-D1','E-D4']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','6月16日18:00','6月17日18:00','6月18日18:00']        
        yList=[
            np.array([2.98,10.56,3.54,3.87,3.76,3.55])
            ,np.array([3.72,9.98,2.97,2.97,3.01,3.44])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotE4ZLWY113(self):
        """
           绘制E匝道第4阶段主梁113#竖向位移
        """

        title='E匝道113#墩第四阶段主梁竖向位移监测结果'
        xlabelText='时间'
        ylabelText='竖向位移（mm）'
        legendList=['E-D2','E-D6']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','5月6日18:00','5月7日18:00','5月8日18:00']
        yList=[
            np.array([2.78,10.76,3.24,3.37,3.48,3.57])
            ,np.array([2.99,11.35,3.56,3.35,3.61,3.58])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotE4ZLYB112(self):
        """
           绘制E匝道第4阶段主梁112#应变
        """

        title='E匝道112#墩第四阶段主梁竖向应变监测结果'
        xlabelText='时间'
        ylabelText='应变值（με）'
        legendList=['E-Y1','E-Y2']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','6月16日18:00','6月16日18:00','6月16日18:00']        
        yList=[
            np.array([0,-26,-22,-22,-21,-22])
            ,np.array([0,-18,-20,-22,-17,-20])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotE4ZLYB113(self):
        """
           绘制E匝道第4阶段主梁113#应变
        """

        title='E匝道112#墩第四阶段主梁竖向应变监测结果'
        xlabelText='时间'
        ylabelText='应变值（με）'
        legendList=['E-Y1','E-Y2']
        xticksLabelList=['托换前','千斤顶顶升最大高度时','千斤顶卸荷后','6月16日18:00','6月16日18:00','6月16日18:00']        
        yList=[
            np.array([0,-26,-22,-22,-21,-22])
            ,np.array([0,-18,-20,-22,-17,-20])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)

    def PlotE5QDCJ(self):
        """
           绘制E匝道第5阶段桥墩沉降监测数据
        """

        title='E匝道第五阶段桥墩沉降监测数据'
        xlabelText='时间'
        ylabelText='沉降（mm）'
        legendList=['110#','111#','112#新','113#新','114#','123#']
        xticksLabelList=['20170610','20170625','20170710','20170725','20170810','20170825','20170910','20170925','20171010','20171025','20171110'
            ,'20171125','20171210','20171225','20180110','20180125','20180210','20180225','20180310','20180325','20180410','20180425','20180510'
            ,'20180525','20180610','20180625','20180710']
        yList=[
            np.array([0.37,0.32,0.33,0.36,0.35,0.39,0.42,0.44,0.32,0.35,0.37,0.25,0.22,0.36,0.41,0.43,0.36,0.32,0.33,0.34,0.22,0.35,0.31,0.36,0.35,0.33,0.26])
            ,np.array([-1.76,-1.52,-1.66,-1.69,-1.72,-1.57,-1.62,-1.64,-1.71,-1.53,-1.62,-1.55,-1.66,-1.68,-1.78,-1.89,-1.98,-2.06,-2,-1.97,-1.82,-1.96,-1.91,-1.87,-1.89,-1.98,-2.06])
            ,np.array([0.03,0.01,0.02,-0.06,-0.05,-0.03,-0.12,-0.15,-0.08,-0.12,-0.06,-0.03,-0.09,-0.05,-0.09,-0.13,-0.15,-0.05,0.03,-0.08,-0.12,-0.07,-0.1,-0.11,-0.06,-0.05,-0.1])
            ,np.array([-0.09,-0.12,-0.07,-0.06,-0.09,-0.13,-0.15,-0.12,-0.11,-0.09,-0.06,-0.08,-0.11,-0.11,-0.19,-0.21,-0.17,-0.12,-0.16,-0.11,-0.16,-0.13,-0.21,-0.19,-0.12,-0.14,-0.22])
            ,np.array([-0.4,-0.35,-0.48,-0.44,-0.46,-0.52,-0.55,-0.53,-0.54,-0.57,-0.55,-0.52,-0.49,-0.56,-0.52,-0.57,-0.63,-0.55,-0.6,-0.63,-0.59,-0.53,-0.61,-0.55,-0.58,-0.57,-0.62])
            ,np.array([0.33,0.32,0.25,0.33,0.29,0.21,0.26,0.19,0.26,0.22,0.23,0.17,0.19,0.18,0.16,0.11,0.19,0.17,0.13,0.15,0.16,0.13,0.09,0.18,0.11,0.06,0.17])
        ]
        x = np.linspace(1, len(yList[0]), num=len(yList[0]))

        self._PlotChart(plt,x,yList,xlabelText,ylabelText,title,xticksLabelList,legendList)