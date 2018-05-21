
import pickle
import numpy as np
from readability.feature import stanford_feature

class FeatureExport(object):
    
    def __init__(self, base_path):
        self.data = []
        self.base_path = base_path
        self.log_file = open(self.base_path + 'fe_log.txt', 'a+')

    # To use this function you must pickle (save)
    #    the output of StanfordCoreNLP.annotate
    #    and give the path to it as sf_path
    #
    # This function creates a row and append it to the data set.
    #    This includes features and label of one training data.
    def extract_features(self, sf_path, label):
        # load stanford annotation
        with open(self.base_path + sf_path, 'rb') as file:
            annotation = pickle.load(file)
        
        if type(annotation) is str:
            # It is most probably "CoreNLP request timed out. Your document may be too long."
            # Ignore this data for now.
            # TODO: solve (e.g. by increasing time out limit
            print('skipped due to error:', sf_path)
            self.log_file.write('Skipped ' + sf_path + ' due to annotation error: ' + annotation + '\n')
            return
        
        row = np.append(stanford_feature.get_features(annotation), label)
        
        self.data.append(row)
    
    def save(self):
        np.savetxt(self.base_path + 'data.csv', self.data, encoding='utf8')