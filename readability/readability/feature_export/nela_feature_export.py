import pickle
from readability.feature import stanford_feature
import numpy as np

if __name__ == '__main__':
    
    labels = np.genfromtxt('D:/master project/data/newsela/average_level.csv', delimiter=',')
    
    data = []
    
    for i in range(1, 6728):
        # load stanford annotation
        with open('D:/master project/data/newsela/standford_annotate/' + str(i), 'rb') as file:
            annotation = pickle.load(file)
        
        if type(annotation) is str:
            # It is most probably "CoreNLP request timed out. Your document may be too long."
            # Ignore this data for now.
            # TODO: solve (e.g. by increasing time out limit
            continue
        
        row = np.append(stanford_feature.get_features(annotation), labels[i-1][1])
        data.append(row)
        print(i)
    
    print(np.array(data))
    np.savetxt('D:/master project/data/newsela/data.csv', data, encoding='utf8')
    
