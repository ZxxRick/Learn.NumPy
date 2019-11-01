import numpy as np


'''修改数组形状

函数					描述
reshape					不改变数据的条件下修改形状
flat					数组元素迭代器
flatten					返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
ravel					返回展开数组
'''	

'''翻转数组

函数					描述
transpose				对换数组的维度
ndarray.T				和 self.transpose() 相同
rollaxis				向后滚动指定的轴
swapaxes				对换数组的两个轴
'''

'''连接数组

函数					描述
concatenate				连接沿现有轴的数组序列
stack					沿着新的轴加入一系列数组。
hstack					水平堆叠序列中的数组（列方向）
vstack					竖直堆叠序列中的数组（行方向）
'''