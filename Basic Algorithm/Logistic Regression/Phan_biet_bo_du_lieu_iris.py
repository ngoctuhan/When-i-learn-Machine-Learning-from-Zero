# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:42:57 2019

@author: trung
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from sklearn import neighbors, datasets

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

cls = [[0],[1]]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
     iris_X, iris_y, test_size=50)

#Phân biệt hai loại hoa lan trong nhóm dữ liệu đã cho

def extract_data(X, y, cls): # chỉ lấy dữ liệu nhóm 1 và nhóm 2
    # Lấy vị trí các phần tử trong mảng mà có giá trị nhãn  = 0 và = 1
    y_res_id_zeros = []
    y_res_id_ones = []
    for i in range(len(y)):
        if y[i] == 1:
            y_res_id_ones.append(i)
        else:
            y_res_id_zeros.append(i)
    n0 = len(y_res_id_zeros)
    n1 = len(y_res_id_ones)
    y_res_id = np.hstack((y_res_id_zeros,y_res_id_ones))
    X_res = X[y_res_id,:]
    y_res = np.asarray([0]*n0 + [1]*n1)
    return (X_res, y_res)
    
(Xtrain, ytrain) = extract_data(X_train, y_train, cls)
(Xtest, ytest) = extract_data(X_test, y_test, cls)

print ("Training size: %d" %len(ytrain))
print ("Test size    : %d" %len(ytest))

lr = LogisticRegression(C = 1e5,solver='liblinear').fit(Xtrain, ytrain)

lr_predict = lr.predict(Xtest)

print("XAC XUAT CHUAN XAC", 100* accuracy_score(ytest, lr_predict.tolist() ) )


lr = LogisticRegression(C = 1e5,solver='lbfgs', multi_class = 'multinomial' ).fit(X_train, y_train)
lr_predict = lr.predict(X_test)
print("XAC XUAT CHUAN XAC", 100* accuracy_score(y_test, lr_predict.tolist() ) )
