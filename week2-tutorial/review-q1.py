import matplotlib.pyplot as plt
import re

def review_question_1(filename):
    with open(filename, 'r') as f:
        file = f.readlines()
    doc = {}
    count = 0
    for line in file:
        line = re.sub('[^a-zA-Z0-9]', ' ', line.lower())
        for word in line.split():
            if len(word) > 2:
                doc[word] = doc.get(word, 0) + 1
                count += 1
                
    termsList = sorted(doc.items(), key=lambda x: x[1], reverse=True)
    print(f'Number of total terms: {count}')
    
    topTen = termsList[:10]
    x, y = zip(*topTen)
    plt.plot(x, y)
    plt.show()

if __name__ == '__main__':
    review_question_1('review1.xml')