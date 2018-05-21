
from nltk.tokenize import word_tokenize
from nltk.parse import RecursiveDescentParser
import nltk

if __name__ == '__main__':
    #rd = RecursiveDescentParser(grammar)
    
    with open('D:/master project/data/newsela/text/1000.txt', 'r', encoding='utf8') as myfile:
        data = myfile.read()
    
    text = word_tokenize(data)
    
    print(text)
    print(nltk.parse)




