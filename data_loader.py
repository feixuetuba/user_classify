#-*- coding:utf-8 -*-

def load(csv):
    import pandas as pd
    import numpy as np
    raw_data = pd.read_csv(csv)
    raw_data = raw_data.fillna(0)
    raw_data = raw_data.values

    data = raw_data[:, 2:]
    ids = raw_data[:, 0]
    labels = raw_data[:, 1]

    data = np.where(data > 0., 1, 0)
    rows, cols = data.shape
    #split dataset
    spliter = int(rows * 0.6)
    trian_d = data[:spliter, :]
    train_l = labels[:spliter]

    test_d = data[spliter:, :]
    test_l = labels[spliter:]
    return (trian_d, train_l),(test_d,test_l)