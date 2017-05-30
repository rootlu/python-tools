# coding: utf-8
# author：lu yf 
import numpy as np
from matplotlib import pyplot as plt

plt.rc('font', family='Times New Roman', size=11)  # 设置字体字号

def autolabel(rects,Num=1,rotation1=60,NN=1):
	for rect in rects:
		height = rect.get_height()
		plt.text(rect.get_x()-0.04+rect.get_width()/2., Num*height, '%s' % float(height*NN),rotation=rotation1)

# 直方图
def draw_Histogram():
	Y1 = [0.6676,1.2675,1.1204,1.0558]
	Y2 = [0.6768,1.2370,1.1499,1.1747]
	Y3 = [0.7158,1.1636,1.2191,0.9935]
	Y4 = [0.6369,1.1292,1.0384,0.9472]

	fig, ax = plt.subplots()  
	index = np.arange(4)+1  
	bar_width = 0.2
	opacity = 0.8
	rec1 = plt.bar(index,Y1,bar_width,alpha=opacity,facecolor = 'lightskyblue',edgecolor = 'white',label='data1')
	rec2 = plt.bar(index+bar_width,Y2,bar_width,alpha=opacity,facecolor = 'yellowgreen',edgecolor = 'white',label='data2')
	rec3 = plt.bar(index+bar_width*2,Y3,bar_width,alpha=opacity,facecolor = 'grey',edgecolor = 'white',label='data3')
	rec4 = plt.bar(index+bar_width*3,Y4,bar_width,alpha=opacity,facecolor = 'red',edgecolor = 'white',label='data4')

	autolabel(rec1)
	autolabel(rec2)
	autolabel(rec3)
	autolabel(rec4)


	plt.ylim(0,1.5)
	plt.xticks(index + bar_width, ('A', 'B', 'C', 'D')) 
	plt.xlabel('Data Set')  
	plt.ylabel('RMSE') 
	plt.legend()  
	plt.show() 

# 折线图
def draw_line_chart():
	#X轴，Y轴数据
	x = [20,40,60,80,90]
	y1 = [1.0924,1.0870,1.0751,1.0658,1.0543]
	y2 = [1.0810,1.0766,1.0647,1.0552,1.0425]
	y3 = [1.0689,1.0456,0.9968,0.9835,0.9724]
	y4 = [1.0340,1.0228,0.9907,0.9772,0.9682]

	plt.plot(x,y1,'gd-',alpha=0.8,color='lightskyblue',linewidth=2,label='A')   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
	plt.plot(x,y2,'g*-',alpha=0.8,color = 'yellowgreen',linewidth=2,label='B')
	plt.plot(x,y3,'gs-',alpha=0.8,color = 'grey',linewidth=2,label='C')
	plt.plot(x,y4,'g^-',alpha=0.8,color = 'red',linewidth=2,label='D')
	
	plt.xlim(20,90)
	# plt.ylim(0.6,0.9)
	plt.ylim(0.8,1.4)
	plt.xticks([20, 40, 60, 80, 90], [r'20%', r'40%', r'60%', r'80%', r'90%'])
	plt.xlabel("Different percentages od training data on Data Set") #X轴标签
	plt.ylabel("RMSE") 
	plt.grid(color='#95a5a6',linestyle='--', linewidth=1 ,axis='y',alpha=0.4)
	plt.legend()
	plt.show()  #显示图

draw_Histogram()
draw_line_chart()



