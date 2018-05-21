'''
Created on May 16, 2018

@author: Eldemin
'''
from contractions import fix
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from pattern.en import tag, parsetree, Chunk

if __name__ == '__main__':
    # read file
    with open('D:/master project/data/test.txt', 'r', encoding='utf8') as myfile:
        text = myfile.read()
    
    print('test')
    
    # replace "isn't" with "is not", etc
    text = fix(text, slang=False)
    
    # get tokens etc
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    stop_words = [word for word in words if word in stopwords.words('english')]
    non_stop_words = [word for word in words if word not in stopwords.words('english')]
    complex_words = [word for word in words if len(word) > 4]
    sentences = sent_tokenize(text)
    pos_tags = tag(text)
    
    print(words)
    print(non_stop_words)
    print(complex_words)
    
    tree = parsetree(text)
    print(text)
    print('tree', tree)
    
    for sentence_tree in tree:
        print('stc_tree', sentence_tree, sentence_tree.words)
        for chunk in sentence_tree.chunks:
            print('chunk', chunk.type, chunk.words)
            if hasattr(chunk, 'chunks'):
                print('children', chunk.chunks)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    