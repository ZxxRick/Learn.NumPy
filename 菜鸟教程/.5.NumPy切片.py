import numpy as np
#关于数组的切片挺深的
'''
ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，
并设置 start, stop 及 step参数进行，从原数组中切割出一个新数组。
'''
a=np.arange(10)
print(a)
print("\n")

s=slice(2,7,2)					#通过内置的slice函数切片
print(a[s])
print("\n")

b=a[2:7:2]
print(b)
