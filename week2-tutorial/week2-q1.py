from bs4 import BeautifulSoup

# Open the file and parse it using BeautifulSoup
# Find all the text tags and loop through them
# Count the number of words in each text tag
# Print the itemid and the number of words
## Note: this uses beautiful soup 4 # its not showing up in docs
def extract_xml(filename):
    with open(filename) as f:
        soup = BeautifulSoup(f, 'lxml')
    for text in soup.find_all('text'):
        num_of_words = len(text.text.split())
        itemid = text.parent['itemid']
        print(f'Item ID: {itemid} Number of words: {num_of_words}')

if __name__ == '__main__':
    extract_xml('main.xml')