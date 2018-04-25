#-*- coding:utf-8 -*-
import pandas as pd
import numpy as np
from data_loader import load
(X_train, Y_train), (X_test, Y_test) = load(r'D:\ZM\playground\classify\sample.csv')
print(X_train.shape)
data = X_train[np.where(Y_train[:] == 1)[0], :]

rows, cols = data.shape

col = 0
while col < data.shape[1]:
    values = data[:, col].T.tolist()
    valcat = set(values)
    if len(valcat) == 1:
       data = np.delete(data, col, axis=1)
    else:
        col += 1
print(data.shape)
