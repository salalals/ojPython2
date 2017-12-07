#!/usr/bin/python
# -*- coding: utf-8 -*-

# SciPy 官方tutorial文档
# https://docs.scipy.org/doc/scipy/reference/tutorial/


# 一般通过下面3条import把 numpy和matplotlib引入
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# SciPy一般通过引用其sub package，比如以下引入linalg
from scipy import linalg


# 类似于matlab，python可以使用np.info() 来查看方法的文档
print np.info(linalg.inv)

# 使用dir查看module的属性和方法
print dir(linalg)



### 单变量多项式
from numpy import poly1d
plus_1_cub_func = poly1d([1,3,3,1])
print plus_1_cub_func

# 计算(5 + 1)的立方
print plus_1_cub_func(5)

# 给入向量也可以
print plus_1_cub_func([1,2,3])



### 方法向量化
def add_scalar(a, b):
    return a + b

# 会返回[1,2,3,1,2,3], 违反原意
print add_scalar([1,2,3], [1,2,3])

# 返回[2,4,6]
print add_scalar(np.array([1,2,3]), np.array([1,2,3]))

# 方法的向量化:
add_scalar_vec = np.vectorize(add_scalar)
# 使用向量化的方法，返回[2,4,6]
print add_scalar_vec([1,2,3], [1,2,3])






# 为了兼容matlab的输入格式，np.mat返回一个matrix，文档中说尽量使用np.ndarray,不要使用matrix
A = np.mat('[1 2;3 4]')
print A


### scipy.linalg包含所有np.linalg的方法, 而且相对快一些
# 所以如果西药使用linalg这个subpackage,尽量使用scipy.linalg
A = np.array([[1,2], [3,4]])
print A
# 使用np计算
print np.linalg.inv(A)
print A.dot(np.linalg.inv(A))

# 使用scipy计算
print linalg.inv(A)
print A.dot(linalg.inv(A))

# 更多的关于scipy.linalg，可以看官方文档，有更多的例子。
# https://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html


