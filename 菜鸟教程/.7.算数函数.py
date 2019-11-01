import numpy as np

#NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。

#需要注意的是数组必须具有相同的形状或符合数组广播规则。


a=np.arange(1,10,dtype=np.float).reshape(3,3)
b=np.array([10,100,1000])
print(a)
print(b)
print("\n")

#加、减、乘、除				#################################################################
print(np.add(a,b))#加法
print("\n")

print(np.subtract(a,b))#减法
print("\n")

print(np.multiply(a,b))#乘法
print("\n")

print(np.divide(a,b))#除法
print("\n")


#reciprocal倒数函数,将元素逐个转化为倒数         #################################################
print(np.reciprocal(a))
print("\n")

#power()函数 将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。
print(np.power(a,2))
print("\n")

#numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果。
print(np.mod(a,2))