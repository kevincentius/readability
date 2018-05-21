
from readability.feature_export.feature_export import FeatureExport

if __name__ == '__main__':
    
    levels = ['KET', 'PET', 'FCE', 'CAE', 'CPE']
    num_articles = [64, 60, 71, 67, 69]
    
    fe = FeatureExport('D:/master project/data/CEPP/')
    
    for l in range(0, 5):
        print('working on level', l)
        for i in range(1, num_articles[l] + 1):
            print('working on text', i)
            fe.extract_features('stanford_annotate_' + levels[l] + '/' + str(i), l)
        
    fe.save()
    
