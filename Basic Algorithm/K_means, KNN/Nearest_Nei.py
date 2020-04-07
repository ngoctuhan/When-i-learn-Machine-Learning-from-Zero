# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 12:15:40 2018

@author: trung
"""

# CODE BO DU LIEU CIFAR-10

import numpy as np


""" dữ liệu huấn luyện / nhãn và dữ liệu / nhãn thử nghiệm """

class NearestNeighbor(object):
    
    def __init__(self):
        pass
    
    # train (X, y) : huấn luyện lấy dữ liệu và nhẫn để học hỏi X có nhãn y
    def train(self,X, y): 
        
        # X is ma matrix N * M
        self.Xtr = X
        self.Ytr = y
        
    def predict(self, X):
        
        num_test = X.shape[0]
        label_data = np.zeros(num_test, dtype = self.Ytr.dtype)
        
        for i in range(num_test):
            distance = np.sum( np.abs(self.Xtr - X[i,:]) , axis = 1)
            min_index = np.argmin(distance)
            label_data[i] = self.Ytr[min_index]
        return label_data
    
def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict    
'''
def load_CIFAR10(file):
    
    
Xtr, Ytr, Xte, Yte = load_CIFAR10('data/cifar10/') 

Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3) # Xtr_rows becomes 50000 x 3072
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3) # Xte_rows becomes 10000 x 3072

nn = NearestNeighbor() # create a Nearest Neighbor classifier class
nn.train(Xtr_rows, Ytr) # train the classifier on the training images and labels
Yte_predict = nn.predict(Xte_rows) # predict labels on the test images
# and now print the classification accuracy, which is the average number
# of examples that are correctly predicted (i.e. label matches)
print ('accuracy: %f' % ( np.mean(Yte_predict == Yte) ) )           
 '''      

print(unpickle("F:\DataML\cifar-10-python\cifar-10-batches-py\data_batch_1"))
