import numpy as np
'''
1.一维等差数组
'''

#1.一维等差数组
'''
												endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
												retstep		如果为 True 时，生成的数组中会显示间距，反之不显示。
												'''
a=np.linspace(1,9,9,retstep=True)							#默认生成个数为50
print(a)

aa =np.linspace(1,10,10).reshape([10,1])
print(aa)
print("\n")



#一维等比数组
'''
参数							描述
start							序列的起始值为：base ** start
stop							序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
num								要生成的等步长的样本数量，默认为50
endpoint						该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
base							对数 log 的底数。
'''
b=np.logspace(1,10,num=20,base=2)									
print(b)												