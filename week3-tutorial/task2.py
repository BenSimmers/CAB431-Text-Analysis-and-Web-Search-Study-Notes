from bs4 import BeautifulSoup
from task1 import parse_doc

# read an xml file and common-english-words.txt (the list of stopping words)
# returns the number of words (word_count) and the number of terms (len(curr_doc))
def main():
    stops = open('common-english-words.txt', 'r').read().split() # stop words
    input = '6146-1.xml'
    word_count, curr_doc = parse_doc(input, stops)
    print('Document itemid: {} contains: {} words and {} terms'.format(list(curr_doc.keys())[0], word_count, len(curr_doc[list(curr_doc.keys())[0]])))

if __name__ == '__main__':
    main()
    
    