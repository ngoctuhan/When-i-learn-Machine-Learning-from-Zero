# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 13:04:10 2018

@author: trung
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, neighbors
from sklearn.model_selection import train_test_split
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans


''' Load dữ liệu Iris vào hai mảng '''
iris = datasets.load_iris()

iris_data = iris.data
iris_target = iris.target

''' Phân dữ liệu ra 2 loại 100 để train và 50 để test '''

Xtrain, Xtest, Ytrain, Ytest = train_test_split(iris_data, iris_target, test_size = 50)

''' Phân 100 dữ liệu test ra để chia thành 3 cụm và kiểm tra hiệu quả '''
#chiều dài, chiều rộng đài hoa (sepal), và chiều dài, chiều rộng cánh hoa (petal).
# Khoi tạo các dữ liệ tại các cụm ban đầu 
K = 3 # 3 cluster

def init_centers_cluster(X, K):
   
    return (X[np.random.choice(X.shape[0], K, replace=False)])

def gan_nhan(X,center):
    
    D = cdist(X, center) 
    '''  100 test với mỗi test gồm 3 cột là k/c vs cụm 1 cụm 2 và cụm 3'''
    return np.argmin(D, axis = 1)
    ''' mảng gán nhãn cho các các test '''
def update_centers(X,label,K):
    center = np.zeros((K,X.shape[1]))
    for k in range(K):
        XK = X[label == k,:] 
        center[k,:] = np.mean(XK , axis = 0)
    return center
def stop(center, new_center):
    m = np.mean(center - new_center)
    if m == 0:
        return True
    return False
def Kmeans_Code(X, K):
    center = [init_centers_cluster(X,K)]
    lablel = []
    it = 0
    while True:
        lablel.append(gan_nhan(X,center[-1]))
        new_center = update_centers(X,lablel[-1],K)
        if stop(center[-1],new_center) == True:
            break
        center.append(new_center)
        it += 1
    return (center,lablel,it)
(centers, labels, it) = Kmeans_Code(Xtrain, K)
print("Cac center: ")
print(centers[-1])

from sklearn.metrics import accuracy_score
print ("Xac xuat : %.2f %%" %(100*accuracy_score(Ytrain, labels[-1])) )

#MAX Vai lan thu tam 89%

# dung thu vien

kmeans = KMeans(n_clusters=3, random_state=0).fit(Xtrain)
print('Centers found by scikit-learn:')
print(kmeans.cluster_centers_)

print ("Xac xuat: %.2f %%" %(100*accuracy_score(Ytrain, kmeans.predict(Xtrain))) )

        

    




