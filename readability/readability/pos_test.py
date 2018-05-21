from pycorenlp import StanfordCoreNLP



if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    
    for i in range(1, 17027):
        with open('D:/master project/data/newsela/text/' + str(i) + '.txt', 'r', encoding='utf8') as myfile:
            text = myfile.read()
        
        print(text)
        output = nlp.annotate(text, properties={
          'annotators': 'parse',
          'outputFormat': 'json'
        })
        
        print(i)
        print(output['sentences'][0]['parse']) # tagged output sentence