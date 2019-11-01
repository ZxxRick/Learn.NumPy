#菜鸟教程3
import numpy as np

a=np.array([1,2,3],int)
''' 
通过array来构建一个数组对象。参数包括一个基本的数组，
									dtype类型,(包括int、float、uint、bool、complex)
									order创建数组的样式，C为行方向，F为列方向，A为任意方向
									subok默认返回一个与基类类型一样致的数组
									ndmin指定生成数组的最小维度

'''

print(a)


