'''
Created on May 16, 2018

@author: Eldemin
'''
import pickle
import time

from contractions import fix
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

from pycorenlp.corenlp import StanfordCoreNLP
from nltk.tree import Tree


def print_debug(annotation):
    sentence = annotation['sentences'][0]
    tree = Tree.fromstring(sentence['parse'])
    tree.pretty_print()
    
    for pos in tree.treepositions():
        node = tree[pos]
        if type(node) is str:
            # leave node (single word)
            #print(tree[pos], len(pos))
            pass
        elif type(node[0]) is str:
            # label of leave node (single word label)
            print(node[0], len(pos))
            assert(len(node) == 1)
        else:
            # subtree (phrase label)
            print(tree[pos].label(), len(pos))
            if type(node[0]) is str:
                print('next to leave')

if __name__ == '__main__':
    
    clause_labels = ['S', 'SBAR', 'SBARQ', 'SINV', 'SQ']
    phrase_labels = ['ADJP', 'ADVP', 'CONJP', 'FRAG', 'INTJ', 'LST', 'NAC', 'NP', 'NX', 'PP', 'PRN', 'PRT', 'QP', 'RRC', 'UCP', 'VP', 'WHADJP', 'WHADVP', 'WHNP', 'WHPP', 'X']
    word_labels = ['CC', 'CD', 'DT', 'EX', 'FW', 'IN', 'JJ', 'JJR', 'JJS', 'LS', 'MD', 'NN', 'NNS', 'NNP', 'NNPS', 'PDT', 'POS', 'PRP', 'PRP$', 'RB', 'RBR', 'RBS', 'RP', 'SYM', 'TO', 'UH', 'VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ', 'WDT', 'WP', 'WP$', 'WRB']
    terminal_count = {}
    non_terminal_count = {}
    
    for i in range(1, 360):
        with open('D:/master project/data/newsela/standford_annotate/' + str(i), 'rb') as file:
            annotation = pickle.load(file)
        
        #print_debug(annotation)
        
        for sentence in annotation['sentences']:
            tree = Tree.fromstring(sentence['parse'])
            #tree.pretty_print()
            for pos in tree.treepositions():
                node = tree[pos]
                if type(node) is str:
                    # ignore leave node, which is a word/token (string)
                    continue
                
                label = node.label().split('-')[0]
                
                if type(node[0]) is str:
                    # label of leave node (single word label)
                    if label in terminal_count:
                        terminal_count[label] += 1
                    else:
                        terminal_count[label] = 1
                    
                    if len(node) != 1:
                        tree.pretty_print()
                        node.pretty_print()
                else:
                    # subtree (phrase label)
                    if label in non_terminal_count:
                        non_terminal_count[label] += 1
                    else:
                        non_terminal_count[label] = 1
        
    print(terminal_count)
    print(non_terminal_count)
    
    print(sorted(terminal_count.keys()))
    print(sorted(non_terminal_count.keys()))
    
    print('unknown word labels:', [k for k in terminal_count.keys() if k not in word_labels])
    print('unknown phrase labels:', [k for k in non_terminal_count.keys() if k not in phrase_labels and k not in clause_labels])
    