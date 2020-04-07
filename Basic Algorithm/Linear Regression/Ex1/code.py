import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn import linear_model
import random

input = pd.read_csv('F:\Code Machine Learning\Linear Regression\Ex1\data.csv')

print (input.head(5))

# Xem chiều dài của df, tương đương shape[0]
print('Len:', len(input))
# Xem thông tin dataframe vừa đọc được
input.info()
# Xem kích thước của dataframe
print('Shape:', input.shape)

