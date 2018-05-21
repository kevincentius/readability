'''
This script is meant to run pattern.en.treeparse and save the results for a whole data set.

This is a preparation step for feature extraction that takes a long time,
    so it is a good idea to separate this from the other steps.  
'''
import pickle
import time

from contractions import fix
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

from pattern.en import tag, parsetree, Chunk


if __name__ == '__main__':
    start = time.time()
    for i in range(1, 17028):
        # read file
        with open('D:/master project/data/newsela/text/' + str(i) + '.txt', 'r', encoding='utf8') as myfile:
            text = myfile.read()
        
        tree = parsetree(text)
        
        with open('D:/master project/data/newsela/pattern_parsetree/' + str(i), 'wb') as file:
            pickle.dump(tree, file)
    
        print(i, time.time() - start, 'seconds')
    
    
    
    
    
    
    