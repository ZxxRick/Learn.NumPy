import numpy as np
'''
1.空数组
2.0数组
3.1数组
4.将列表转化为数组
5.范围数组
'''

#1.空数组
a=np.empty(shape=[3,4],dtype='int')
print(a)
print("\n")
#其数组元素为随机值，未被初始化


#2.0数组
b=np.zeros(5,int)			#默认为浮点数
print(b)
print("\n")


#3.1数组
c=np.ones([2,6],int)
print(c)
print("\n")

#4.将列表转化为数组
x=[1,2,3,4,5,6,7,8,9,10]
d=np.asarray(x)									#保持原有形状
print(d)
print("\n")


#5.范围数组###############################################################################
e=np.arange(1,7,1,dtype='int')
print(e)
print("\n")


