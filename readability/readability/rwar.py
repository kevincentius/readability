'''
Created on May 20, 2018

@author: Eldemin
'''
import pickle

from nltk.tree import Tree


if __name__ == '__main__':
    for i in range(1, 27000):
        if i % 100 == 0:
            print(i)
        
        with open('D:/master project/data/newsela/standford_annotate/' + str(i), 'rb') as file:
            annotation = pickle.load(file)
        
        if type(annotation) is str:
            print('skipped: ' + annotation)
            continue
        
        sentence_trees = [Tree.fromstring(sentence['parse']) for sentence in annotation['sentences']]
        
        for tree in sentence_trees:
            for pos in tree.treepositions():
                node = tree[pos]
                if type(node) is Tree and type(node[0]) is str and len(node) > 1:
                    node.pretty_print()
    
    pass