import pickle

if __name__ == '__main__':
    
    for i in range(1, 99999):
        with open('D:/master project/data/newsela/standford_annotate/' + str(i), 'rb') as file:
            annotation = pickle.load(file)
            if type(annotation) is str:
                print(i, annotation)
    
    pass