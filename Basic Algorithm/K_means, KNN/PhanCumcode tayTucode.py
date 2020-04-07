# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 17:03:09 2018

@author: trung
"""

''' Bài toán đặt ra : 
    Một người hành vi người dùng dựa vào 2 yếu tố sở thích để đưa ra gọi ý về
    bài hát:
        1. thể loại hay sửa dụng ( số từ 1 -9)
        2. tâm trạng ( số từ 1 - 9)
    Phân loại các nhóm người dùng từ số liệu trên thành K nhóm ( K < 5)
    Đầu vào : Mảng X gồm các cặp dữ liệu
    Đầu ra  : Các center của các nhóm 
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

np.random.seed(11)
# Khởi tạo bộ sinh số ngẫu nhiên
# Input: 

mean = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
# Số dữ liệu mỗi loại dữ liệu
label = [0]*N + [1]*N + [2]*N

label = np.asarray(label)

# Chuyển từ mảng sang array để dùng các thuộc tính của array

K = 3 #cluster

Data_train1 = np.random.multivariate_normal(mean[0],cov,N) # label 1
Data_train2 = np.random.multivariate_normal(mean[1],cov,N) # label 2
Data_train3 = np.random.multivariate_normal(mean[2],cov,N) # label 3
# Sinh các bộ số từ phân phối chuẩn với giá trị trung bình là mean


Data = np.concatenate((Data_train1,Data_train2,Data_train3))
# Ghép các mảng dữ liệu theo chiều dọc

def display_matplot(Data,label):
    
     X0 = Data[label == 0,:] # blue
     X1 = Data[label == 1,:] # red
     X2 = Data[label == 2,:] # green
     
     plt.plot(X0[:,0] , X0[:,1],'b^',markersize = 4, alpha = .8)
     plt.plot(X1[:,0] , X1[:,1],'go',markersize = 4, alpha = .8)
     plt.plot(X2[:,0] , X2[:,1],'rs',markersize = 4, alpha = .8)
     
     plt.axis('equal') # giới hạn của mỗi tập dữ liệu khi đc biểu diễn trên đồ thị
     plt.show()

display_matplot(Data,label)     
    
# Thuật toán K-means

print("Sử dụng hàm có sẵn trong thư viện ")

kmeans = KMeans(n_clusters=3, random_state=0).fit(X)

print(kmeans.cluster_centers_)



# Code tay thuật toán


   
   



    



