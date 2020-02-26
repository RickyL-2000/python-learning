# from https://blog.csdn.net/liuchengzimozigreat/article/details/84566650

import matplotlib.pyplot as plt
import math
from mpl_toolkits.basemap import Basemap
from pylab import *
import numpy as np
 
 
mpl.rcParams['font.sans-serif'] = ['SimHei']
 
for i in range(1,3):
	plt.subplot(2, 1, i)
	ax = plt.gca()
	wind = [x for x in range(1,9)]
	# angle = [45*x for x in range(0,8)]
	# lon = list(np.linspace(113.8, 114.6, 8))
	lat = list(np.linspace(22.4, 22.85, 8))
 
	# wind = [2]*8
	angle = [90]*8 # 为方便比较长度，箭头方向设置成一样
	lon = [114.27] * 8 # 为方便比较长度，箭头经度设置成一样
 
	# 指定地图范围、投影方式（projection）等  area_thresh是与湖泊等在地图上显示相关的参数
	m = Basemap(llcrnrlon=113.7, llcrnrlat=22.35, urcrnrlon=114.7, urcrnrlat=22.9,\
            rsphere=(6378137.00,6356752.3142),\
            resolution='l', area_thresh=1000., projection='lcc', lat_1=22.5, lat_0=22.5, lon_0=114,ax=ax)
	lon, lat = m(*(lon, lat))
 
	# 一系列的U、V
	ver = [-spd*math.sin(math.radians(agl)) for spd,agl in zip(wind, angle)] # U分量
	hriz = [-spd*math.cos(math.radians(agl)) for spd,agl in zip(wind, angle)] # V分量
	print(ver, '\n', hriz)
 
	ax=plt.gca()
	#下面两行是读取地图中的shape文件，即轮廓图
	# m.readshapefile(r'G:\深圳季风研究\gadm36_HKG_shp\gadm36_HKG_0', 'states',color='grey') #HongKong
	# # m.readshapefile(r'G:\深圳季风研究\gadm36_CHN_shp\gadm36_CHN_3', 'states',color='grey') #Mainland in given lon and lat
	# m.readshapefile(r'G:\深圳季风研究\gadm36_sz_shp\Bon_data\xzq_sz_pop', 'states', color='grey')
 
	m.scatter(lon, lat, s=2, color='goldenrod', marker="o") #根据经纬度，画出对应站点位置
	ax.set_title('风场')
	# ax.quiver(lon, lat, ver, hriz, units='width', scale=2, width=0.01, color='deepskyblue')
	ax.quiver(lon, lat, ver, hriz, color='deepskyblue', width=0.005, scale=30)
 
	for i, wspd in enumerate(wind):
		ax.annotate(str(wspd), (lon[i], lat[i]))
 
	# 在图上添加一些文字信息
	plt.text(0.6,0.9, r'$mean: $'+str(18) + '°', color='forestgreen',transform=ax.transAxes, fontweight='extra bold')
	plt.text(1.02,0.6, r'$S: $' + str(18) + '%', color='forestgreen',transform=ax.transAxes, fontweight='heavy')
	plt.text(1.02,0.4, r'$N: $', color='forestgreen',transform=ax.transAxes, fontweight=100)
 
	# 画经纬度网格
	m.drawmeridians([114.0,114.4], labels=[1,0,0,1]) # meridian：子午线，经线 arange指明范围和间隔
	m.drawparallels(np.arange(15, 30, 0.3), labels=[1,0,0,0])  # 画纬度平行线
 
	# 比例尺长度的U、V值和位置
	q_lon, q_lat = m(*(114.27, 22.75))
	spd = 2
	angle_all = 90
	ver_all = -spd*math.sin(math.radians(angle_all))
	hriz_all = -spd*math.cos(math.radians(angle_all))
	# ax.quiver(q_lon, q_lat, ver_all, hriz_all, color='g', pivot='mid') # mid是旋转枢纽在中间，默认在尾部
	ax.quiver(q_lon, q_lat, ver_all, hriz_all, color='g', scale=30)
 
	# 画比例尺
	plt.text(0.82,0.1, r'$scale:$', color='r',transform=ax.transAxes, fontweight=100, fontsize=8)
	plt.text(0.82,0.03, r'$2m/s$', color='r',transform=ax.transAxes, fontweight=100, fontsize=8)
	plt.quiver(95000, 3000, 3, hriz_all, color='r', width=0.005, scale=50)
	print(-ver_all, hriz_all)
 
	# 这一段与画箭头不相干，可忽略注释掉  画散点,为不同散点设置不同颜色
	# Colors=('#DDDDFF','#7D7DFF','#0000C6','#000079','#CEFFCE','#28FF28','#007500','#FFFF93')
	# sc = plt.scatter(lon, lat, s=100, color=Colors, marker="o") #根据经纬度，画出对应站点位置
	# for i,txt in enumerate(Colors):
	# 	ax.annotate(txt,(lon[i],lat[i]), fontsize=5)
 
plt.show()