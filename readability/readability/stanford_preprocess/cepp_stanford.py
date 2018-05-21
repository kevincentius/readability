'''
This script is meant to run StanfordCoreNLP parser and save the results for a whole data set.

This is a preparation step for feature extraction that takes a long time,
    so it is a good idea to separate this from the other steps.  
'''
import pickle
import time

from contractions import fix
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

from pycorenlp.corenlp import StanfordCoreNLP
from nltk.tree import Tree


if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    
    levels = ['KET', 'PET', 'FCE', 'CAE', 'CPE']
    num_articles = [64, 60, 71, 67, 69]
    
    start = time.time()
    for l in range(0, len(levels)):
        level_start = time.time()
        
        for i in range(1, num_articles[l] + 1):
            doc_start = time.time()
            # read file
            with open('D:/master project/data/CEPP/' + levels[l] + '/' + str(i) + '.txt', 'r', encoding='utf8') as myfile:
                text = myfile.read()
            
            annotation = nlp.annotate(text, properties={
                'annotators': 'tokenize,ssplit,pos,depparse,parse',
                'outputFormat': 'json'
            })
            
            with open('D:/master project/data/CEPP/stanford_annotate_' + levels[l] + '/' + str(i), 'wb') as file:
                pickle.dump(annotation, file)
            
            print('doc %i, %.2f seconds (%.0f total))' % (i, time.time() - doc_start, time.time() - start))
        
        print('level %i, %.2f seconds (%.0f total))' % (i, time.time() - level_start, time.time() - start))
    
    
    
    
    