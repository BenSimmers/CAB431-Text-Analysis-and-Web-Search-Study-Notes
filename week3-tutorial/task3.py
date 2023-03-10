from task2 import main
from task1 import parse_doc
from bs4 import BeautifulSoup


def main():
    # Display the document’s terms and their frequencies, and sort
    # alphabetically by terms in ascending order.
    stops = open('common-english-words.txt', 'r').read().split() # stop words
    input = '6146-1.xml'
    word_count, curr_doc = parse_doc(input, stops)
    print('Document itemid: {} contains: {} words and {} terms'.format(list(curr_doc.keys())[0], word_count, len(curr_doc[list(curr_doc.keys())[0]])))
    print('Terms and their frequencies:')
    for key, value in sorted(curr_doc[list(curr_doc.keys())[0]].items()):
        print(key, value)

if __name__ == '__main__':
    main()
    
