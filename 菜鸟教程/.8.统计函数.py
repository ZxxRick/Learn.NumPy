import numpy as np
'''
最值
差值
中位数
平均数
加权平均数
标准差、方差
'''
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
print("\n")


#numpy.amin() numpy.amax()用于计算数组中的元素沿指定轴的最值。 如果未指定轴，则选取一个最值
print(np.amin(a,1))
print(np.amin(a))
print(np.amax(a,1))
print(np.amax(a))
print("\n")

#numpy.ptp()函数计算数组中元素最大值与最小值的差（最大值 - 最小值）。 也有方向选择
print(np.ptp(a,1))
print(np.ptp(a))
print("\n")

#numpy.median() 函数用于计算数组 a 中元素的中位数（中值）
print(np.median(a))
print(np.median(a,1))
print("\n")


#numpy.mean() 函数返回数组中元素的算术平均值。 如果提供了轴，则沿其计算。
print(np.mean(a))
print(np.mean(a,0))
print("\n")


#numpy.average() 函数根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值。



#标准差std、方差var
print(np.std(a)**2)
print(np.var(a))