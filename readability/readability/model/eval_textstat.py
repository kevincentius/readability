'''
Created on May 16, 2018

@author: Eldemin
'''
from textstat.textstat import textstat
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    labels = np.genfromtxt('D:/master project/data/newsela/average_level.csv', delimiter=',')
    
    p = []
    
    for i in range(1, 1000):
        with open('D:/master project/data/newsela/text/' + str(i) + '.txt', 'r', encoding='utf8') as myfile:
            text = myfile.read()
        
        p.append(textstat.flesch_reading_ease(text))
        print(i)
    
    y = labels[0:len(p), 1]
    print(y)
    print(p)
    plt.scatter(y, p)
    plt.show()



