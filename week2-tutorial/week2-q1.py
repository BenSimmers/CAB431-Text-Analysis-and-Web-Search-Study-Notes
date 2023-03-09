from bs4 import BeautifulSoup


## Initial Solution ##
# def extract_xml(filename):
#   soup = BeautifulSoup(open(filename), 'lxml')
#   texts = soup.find_all('text')
#   for item in texts:
#     num_of_words = len(item.text.split())
#     itemid = item.parent['itemid']
#   # print('Item ID: ' + itemid + ' Number of words: ' + str(num_of_words))
#     print('Item ID: {} Number of words: {}'.format(itemid, num_of_words))


## Refined Solution ##
def extract_xml(filename):
    with open(filename) as f:
        soup = BeautifulSoup(f, 'lxml')
    for text in soup.find_all('text'):
        num_of_words = len(text.text.split())
        itemid = text.parent['itemid']
        print(f'Item ID: {itemid} Number of words: {num_of_words}')

if __name__ == '__main__':
    extract_xml('main.xml')