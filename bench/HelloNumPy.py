#!/usr/bin/python
# -*- coding: utf-8 -*-

# NumPy Quickstart 官方文档 v1.13
# https://docs.scipy.org/doc/numpy-dev/user/quickstart.html


import numpy as np

# 创建ndarray 多维数组，类似于一个matrix
a = np.arange(12)
print a

# 转换为3*4的二维ndarray
b = a.reshape(3, 4)
print a     # a不变
print b     # b为3*4

# 根据指定Python list，创建ndarray
a = np.array([1,2,3,4,5,6]).reshape(2, 3)
print a

# 创建全0矩阵，注意给入的shape参数是一个tuple
z = np.zeros((3, 5))
print z

# 创建全1矩阵
o = np.ones((2, 4))
print o

# 创建随机矩阵: 元素来自 [0, 1) 的均匀分布.
r = np.random.rand(2, 3)
print r

# rand()和randome()区别是什么？还不清楚
r = np.random.random((5, 5))
print r

# 创建未初始化的矩阵, 数字接近0，不可用
e = np.empty((3, 3))
print e


# 创建等差数列后，转换成矩阵:
# 第一个元素是0， 最后一个元素是5，共16个元素
a = np.linspace(0, 5, 16).reshape(4, 4)
print a



### 基本操作

a = np.arange(12).reshape(3,4)
b = np.linspace(0, 1, 12).reshape(3, 4)
print a
print b

# element-wise 相加, 元素类型变成精度更高的类型(int to float)
print a + b

# element-wise 相乘
print a * b

# element-wise 乘以常数
print a * 2

# 返回True/False ndarray
print a < 6

A = np.array([1,2,3,4]).reshape(2,2)
B = np.array([1,0,0,1]).reshape(2,2)

print A
print B

# 矩阵乘法
print A.dot(B)

# 生成对角单位矩阵
print np.diag([1,1,1,1,1,1,1,1])

# 获取一个矩阵的对角向量
print np.diag(A)

a = np.arange(12).reshape(3,4)
print a

# 矩阵按 列 运算
print a.sum(axis=0)
# 矩阵按 行 运算
print a.sum(axis=1)
print a.max(axis=1)

# 一些universal function 简称ufunc
print np.exp([0,1,2])



### Indexing 和 Slicing

# 先看python原生的list支持的操作
a = [1,2,3,4,5,6,7,8,9]
print a[:6:2]   # 打印[1,3,5] 不支持赋值
a = [[1,2],[3,4]]
print a[1][1]   # 打印4 不支持赋值

# 看下ndarray支持的更多的操作
a = np.arange(1, 10, 1)

# 可以使用slicing做赋值操作
a[:6:2] = 99
print a

A = np.arange(12).reshape(3, 4)
print A

# 使用[m,n]访问index在m行n列元素
print A[1,2]

# 第3列(index = 2)全部赋值为99
A[:, 2] = 99
print A

# 最后一行全部赋值100
A[-1, :] = 100
print A


### shape 操作
A = np.arange(16).reshape(4, 4)
print A
print A.reshape(2, 8)

# A矩阵的转置矩阵
print A.T

# reshape()返回新矩阵，resize()做原位修改
A.resize(16, 1)
print A

# 矩阵水平叠加与垂直叠加
A = np.diag([1,1])
B = np.diag([2,2])
print np.vstack((A, B))
print np.hstack((A, B))

# 使用newaxis 将行向量转换成 2D列向量
a = np.arange(2)
print a[:, np.newaxis]

# 生成一个[1,2,3] ndarray
print np.r_[1,2,3]

# 生成一个[[1,2,3]] 2D ndarray
print np.c_[1,2,3]

# 使用hsplit分割矩阵
A = np.arange(16).reshape(2, 8)
print A

# 把A水平分成2个矩阵
print np.hsplit(A, 2)

# 把A水平分成3个矩阵，index=1之前为第一个，index=1-3的列为第二个，之后从index=4到最后为第三个
print np.hsplit(A, (1, 4))



### copy 操作
A = np.array([[1,2,3], [4,5,6]])

# 矩阵深复制
B = A.copy()
print A is B



### Fancy indexing 更多的关于index
A = np.array([1,2,3,4,5,6,7,8,9,0]) ** 2
print A     # [ 1  4  9 16 25 36 49 64 81  0]

ind = np.array([[3,4], [7,9]])
print A[ind]    # [[16 25] [64  0]]




### Linear Algebra 线性代数
A = np.array([[1,2], [3,4]])
print A

# A的转置
print A.T
print A.transpose()

# 逆矩阵
print np.linalg.inv(A)

# 生成单位矩阵
print np.eye(5)

# 矩阵相乘
print np.dot(A, A.T)


# 矩阵的迹trace
print np.trace(A)

# 矩阵的特征值 eigenvalues 与 特征向量 eigenvectors
print np.linalg.eig(np.eye(3))

### 一点简单的作图
import matplotlib.pyplot as plt
v = np.random.normal(2, 0.5, 1000)
plt.hist(v, bins=50, normed=1)

# 打开以下作图语句，会弹出作图窗口
# plt.show()