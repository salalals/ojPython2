#!/usr/bin/python
# -*- coding: utf-8 -*-

# scikit learn 官方文档: http://scikit-learn.org/stable/index.html
# scikit learn 官方tutorial: http://scikit-learn.org/stable/tutorial/index.html



### 加载scikit有监督的样本数据
from sklearn import datasets

# sklearn有一些样例，digits是一个dataset
digits = datasets.load_digits()

# 大概查看一下digits的结构和数据, 这是一个手写识别的数据集
print type(digits), dir(digits)

# digits.data就是 X 矩阵, 有1797行，是numpy.ndarray类型
print type(digits.data), len(digits.data)

# digits.data 每个 x 向量有64列，是numpy.ndarray类型
print type(digits.data[0]), len(digits.data[0])

# digits.target 就是 y 向量, 0 - 9的手写数字的label
print type(digits.target), len(digits.target), digits.target

# digits.images 就是原始的8 x 8图像数据, 压平成1D向量后得到digits.data的每一个x向量
print type(digits.images[0]), digits.images[0]
print digits.data[0]



### 使用svm train
from sklearn import svm

# gamma等参数也可以用CV或grid search决定，这里随便填一个
svm_classifier = svm.SVC(gamma=0.001, C=100.0)

# 先 fit() , 然后 predict()
svm_classifier.fit(digits.data[:-5], digits.target[:-5])
print svm_classifier.predict(digits.data[-5:])



### 存储model到硬盘
# 可以使用python的pickle，但是scikit里面有joblib可以更快一些
from sklearn.externals import joblib

# bench路径下会多一个digits_svm_classifier.pkl文件
joblib.dump(svm_classifier, "digits_svm_classifier.pkl")

load_back = joblib.load("digits_svm_classifier.pkl")
print load_back.predict(digits.data[-5:])



### 再看一个无监督的kmean的例子
# http://scikit-learn.org/stable/tutorial/statistical_inference/unsupervised_learning.html
from sklearn import cluster
iris = datasets.load_iris()
X_iris = iris.data
y_iris = iris.target
k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X_iris)

# labels_就是聚类后的结果
print "k_means.labels_[1:100:12]: ", k_means.labels_[1:100:12]
print "y_iris[1:100:12]:", y_iris[1:100:12]


### pipeline 可以将training的多个数据处理步骤组合在一起
# 并且可配合 GridSearchCV 或 RandomizedSearchCV 使用
from sklearn import linear_model, decomposition
from sklearn.pipeline import Pipeline

# 第1步做PCA降维度
pca = decomposition.PCA(n_components=20)

# 第2步做logistics回归分类
logistics = linear_model.LogisticRegression(C=1)

# 组装pipeline
pipeline = Pipeline(steps=[('pca', pca), ("logistics", logistics)])

# 加载数据
digits = datasets.load_digits()
X_digits = digits.data
y_digits = digits.target

# train pipeline
pipeline.fit(X_digits, y_digits)

# predict 预测
print "test X[-5:]:", pipeline.predict(X_digits[-5:])
print "actual y[-5:]:", y_digits[-5:]

# 每一个estimator都有 score 接口
# score: test数据如果有label，也可以对estimator打分 (正确百分比)
print "score: ", pipeline.score(X_digits, y_digits)

# 利用pipeline将多个training model连起来，使用CV评分，搜索出比较好的参数
import numpy as np
from sklearn.model_selection import GridSearchCV
n_components = [20, 40, 64]
Cs = np.logspace(-4, 4, 3)

# 使用双下划线 __ 分割estimator和参数组
# n_components 和 Cs 做笛卡尔积组成所有可能的参数组，然后用CV做校验选出最好的参数组
grid_search_cv_estimator = GridSearchCV(pipeline, dict(pca__n_components=n_components, logistics__C=Cs))
grid_search_cv_estimator.fit(X_digits, y_digits)
print "grid_search_cv_estimator score:", grid_search_cv_estimator.score(X_digits, y_digits)

print "grid_search_cv_estimator full scores during grid search:"
print grid_search_cv_estimator.cv_results_











