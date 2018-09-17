import pandas as pd
import scipy
from scipy import io
import matplotlib.pyplot as plt
import numpy as np

data1 = scipy.io.loadmat('E:\EMGDATA\DB1\S1_A1_E1')
# data2 = scipy.io.loadmat('E:\EMGDATA\DB1\S2_A1_E1')
# data3 = scipy.io.loadmat('E:\EMGDATA\DB1\S3_A1_E1')
# data4 = scipy.io.loadmat('E:\EMGDATA\DB1\S4_A1_E1')
# data5 = scipy.io.loadmat('E:\EMGDATA\DB1\S5_A1_E1')

data1 = data1['emg']
# data2 = data2['emg']
# data3 = data3['emg']
# data4 = data4['emg']
# data5 = data5['emg']

data1 = pd.DataFrame(data1)
# data2 = pd.DataFrame(data2)
# data3 = pd.DataFrame(data3)
# data4 = pd.DataFrame(data4)
# data5 = pd.DataFrame(data5)

# 合并前五个数据集
#data = np.vstack((data1, data2, data3, data4, data5))#垂直组合np.vstack() 水平组合np.hstack()
#data = pd.DataFrame(data)
#feature = data.apply(lambda x: (x - x.mean())/(x.std()))

# 对第一个数据集进行处理
inp = data1[0]

inp_min = min(inp)
print(inp_min)
x = range(0, len(inp))
plt.figure(1)
plt.clf()
plt.plot(x, inp)

#inp = inp.apply(lambda x: (x - x.mean())/(x.std()))

# inp_std = np.std(inp)
for i in range(0, len(inp)):
    inp[i] = round(inp[i]*1000-2.4)
print(inp)
data1_captured_point = []
data1_captured = []

i = 0
j = 0

while i < len(inp):
    if(inp[i] > 0) and (inp[i+1] > 0):
        while True:
            data1_captured_point.append(i)
            i = i + 1
            if(inp[i] == 0) and (inp[i+1] == 0) and (inp[i+2] == 0):
                j = j + 1
                break
    else:
        i = i + 1
print(j)
print(data1_captured_point)
for i in range(0, len(data1_captured_point)):
    data1_captured.append(inp[data1_captured_point[i]])

x = range(0, len(data1_captured))
plt.figure(2)
plt.clf()
plt.plot(x, data1_captured)

# x = range(0, len(inp))
# plt.figure(2)
# plt.clf()
# plt.plot(x, inp)
plt.show()
