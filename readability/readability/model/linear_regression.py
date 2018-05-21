
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection._validation import cross_validate, cross_val_score
from sklearn.utils.class_weight import compute_sample_weight

import numpy as np
from sklearn.linear_model.ridge import Ridge

import matplotlib.pyplot as plt
from pattern.metrics import flesch_reading_ease

def read_csv_data(data_path):
    data = np.loadtxt(data_path)
    
    num_features = len(data[0]) - 1
    
    x = data[:, 0:num_features]
    y = data[:, num_features]
    
    return x, y


if __name__ == '__main__':
    nela = 'D:/master project/data/newsela/data.csv'
    cepp = 'D:/master project/data/CEPP/data.csv'
    
    x, y = read_csv_data(nela)
    
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, shuffle=True, random_state=0)
    
    regr = linear_model.LinearRegression(normalize=True)
    #regr = linear_model.Ridge(alpha=0.001, normalize=True)
    
    regr.fit(x_train, y_train)
    predict = regr.predict(x_test)
    
    scores = cross_val_score(regr, x_test, y_test, scoring='neg_mean_squared_error')
    print(scores.mean())
    
    print(y_test)
    print(predict)
    
    plt.scatter(y_test, predict)
    plt.show()
    