
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET

# read an xml file and common-english-words.txt (the list of stopping words)
# returns the number of words (word_count) and the number of terms (len(curr_doc))
# input: xml file, stopping words
# output: word_count, {docid:curr_doc}
def parse_doc(input, stops):
    curr_doc ={}
    word_count = 0
    with open(input) as f:
        soup = BeautifulSoup(f, 'lxml')
    for text in soup.find_all('text'):
        num_of_words = len(text.text.split())
        itemid = text.parent['itemid']
        word_count = num_of_words
        text = re.sub(r'[^\w\s]', '', text.text)
        text = re.sub(r'\d+', '', text)

        text = [word for word in text.split() if word not in stops]
        for word in text:
            if word in curr_doc:
                curr_doc[word] += 1
            else:
                curr_doc[word] = 1
        # print(curr_doc)
    return (word_count, {itemid:curr_doc})
# test
if __name__ == '__main__':
    # read stop words
    stops = open('common-english-words.txt', 'r').read().split() # stop words
    # parse a document
    input = '6146-1.xml'
    print(parse_doc(input, stops))
