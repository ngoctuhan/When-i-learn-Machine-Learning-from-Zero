# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:11:59 2018

@author: trung
"""
# Iris flower dataset có sẵn trong thư viện scikit-learn.
import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors, datasets

iris = datasets.load_iris()
# load du lieu 

iris_x = iris.data 

iris_y = iris.target

print(iris_x.shape)
print(iris_y)

#Mỗi dữ liệu nằm trên một hàng của ma trận và 4 cột

print ('Number of classes: %d' %len(np.unique(iris_y)) ) 

print ('Number of data points: %d' %len(iris_y))

X0 = iris_x[iris_y == 0,:]
X0 = iris_x[iris_y == 1,:]
X0 = iris_x[iris_y == 2,:]


# thu vien có sẵn hỗ trợ cho việc chia dữ liệu ra thành hai loại test và train
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=50)

# Hàm tách dữ liệu trainig và dữ liệu test được hỗ trợ sẵn bằng cách cắt ngẫu nhiên 

print ("Training size: %d" %len(y_train))
print ("Test size    : %d" %len(y_test))

#TH K = 1

#Tìm hàng xóm gần nhát (1n)

nei = neighbors.KNeighborsClassifier(n_neighbors = 1, p = 2).fit(X_train,y_train)
res_ = nei.predict(X_test)
print("Du lieu nhan nhan dk khi dung thuat toan :")
print(res_)
print("Du lieu đúng : ")
print(y_test)

count = 0

for i in range(res_.size):
    if res_[i] ==  y_test[i]:
        count += 1
xs = count / res_.size
print("Xac xuat : ")
print(xs)

from sklearn.metrics import accuracy_score
print ("Xac xuat of 1NN: %.2f %%" %(100*accuracy_score(y_test, res_)) )

# Lay 10 diem gan nhat
nei = neighbors.KNeighborsClassifier(n_neighbors = 10, p = 2).fit(X_train,y_train)
res_ = nei.predict(X_test)
from sklearn.metrics import accuracy_score
print ("Xac xuat of 10NN: %.2f %%" %(100*accuracy_score(y_test, res_)) )


# Cai tien them khi lay ra 10 đ các điểm gần đánh trọng số cao hơn

nei = neighbors.KNeighborsClassifier(n_neighbors = 10, p = 2, weights = "distance").fit(X_train, y_train)
y_pred = nei.predict(X_test)
print ("Accuracy of 10NN (1/distance weights): %.2f %%" %(100*accuracy_score(y_test, y_pred)))

# Code tay thuat toan tren:
def neighborss(test,data_train, data_target):
    
    num = test.shape[0]
    print(num)
    res = np.ones(test.shape[0],dtype = data_target.dtype)
    
    for i in range(num):
        distance = np.sum(np.abs(data_train - test[i,:]),axis = 1)
        min_index = np.argmin(distance)
        res[i] = data_target[min_index]
    return res

res = (neighborss(X_test, X_train, y_train))
print(res)
print ("Xac xuat of 1NN: %.2f %%" %(100*accuracy_score(y_test, res)) )

from sklearn.svm import SVC
clf = SVC(gamma='auto').fit(X_train, y_train)
pre = clf.predict(X_test)
print ("Xac xuat : %.2f %%" %(100*accuracy_score(y_test, pre.tolist())) )

from sklearn import linear_model
clf = linear_model.SGDClassifier(max_iter=10000, tol = 1e-3).fit(X_train, y_train)
pre = clf.predict(X_test)
print(clf.n_iter_)
print ("Xac xuat SGD : %.2f %%" %(100*accuracy_score(y_test, pre.tolist())) )