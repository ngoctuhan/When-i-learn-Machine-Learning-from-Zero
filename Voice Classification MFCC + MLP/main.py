import numpy as np
import matplotlib.pyplot as plt
import os
import sklearn
import wave


data = []
labels = []
path_name = "C:\Users\trung\Machine Learning basic\Voice Classification\recordings"
coef = 0
count = 0
for file_name in os.listdir(path_name):
    count += 1
    w = wave.open(os.path.join(path,file_name), 'r')
    data.append(w)
    labels.append(coef)
    if(count % 200 == 0):
        coef += 1
        
data = np.asanyarray(data)
labels = np.asanyarray(labels)
print("Number of voice datas: ",data.shape )
print("Shape of labels : ", labels.shape)

