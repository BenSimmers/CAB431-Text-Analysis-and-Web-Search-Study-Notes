from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
from pyparsing import line
import string

## review question 1
# def review_question_1(filename): # filename = 'review1.xml'
#   file = open(filename, 'r').readlines() # readlines() returns a list of lines
#   doc = {} # dictionary
#   count = 0 # number of total terms

#   # remove all non-alphanumeric characters
#   for line in file:
#     line = re.sub('[^a-zA-Z0-9]', ' ', line) # replace all non-alphanumeric characters with a space
#     line = line.lower() # convert all characters to lowercase
#     line = line.split() # split the line into a list of words
#     for word in line: # iterate through the list of words
#       if len(word) > 2: # if the word is longer than 2 characters
#         if word in doc: # if the word is already in the dictionary
#           doc[word] += 1 # increment the value of the word by 1
#         else: # if the word is not in the dictionary
#           doc[word] = 1 # add the word to the dictionary with a value of 1
#         count += 1 # increment the total number of terms by 1

#   termsList = doc.items() # convert the dictionary to a list of tuples
#   termsList = sorted(termsList, key=lambda x: x[1], reverse=True) # sort the list of tuples by the value of the tuple
#   print('Number of total terms: {}'.format(count)) # print the total number of terms

#   termsListContent = list(termsList) # convert the list of tuples to a list of lists
#   topTen = termsListContent[:10] # get the top 10 terms

#   x, y = zip(*topTen) # unzip the list of lists into two lists
#   plt.plot(x, y)
#   plt.show() 

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







#review question 2
'''
Which of the following is FALSE? and explain why it is FALSE.
(1) Stemming is a component of text processing that captures the relationships between
different variations of a word.
(2) Stemming reduces the different forms of a word that occur because of inflection (e.g.,
plurals, tenses) or derivation (e.g., making a verb into a noun by adding the suffixation)
to a common stem.
(3) In general, using a stemmer for search applications with English text produces a small but
noticeable improvement in the quality of results.
(4) A dictionary-based stemmer uses a small program to decide whether two words are
related, usually based on knowledge of word suffixes for a particular language

answer is 4 

stemming is a process of reducing inflected (or sometimes derived) words to their word stem, base or root form—generally a written word form.
a dictionary-based stemmer uses a dictionary of words to determine the stem of a word. it has no sense of logic or rules
'''

#review question 3 - n-grams

document = '''
Tropical fish are generally those fish found in aquatic tropical environments around the
world, including both freshwater and saltwater species. Fishkeepers often keep tropical
fish in freshwater and saltwater aquariums.
'''

#Please design a python program to print all bigrams and trigrams of the above document that
# contain at least one of the highlighted key words (‘fish’, ‘tropical’, ‘freshwater’, ‘saltwater’,‘aquariums’)


def is_highlight(gram, keywords):
    x = False
    for y in keywords:
        if y in gram:
            x = True
    return x

def create():
  line ="Tropical fish are generally those fish found in aquatic tropical environments around the world, \
  including both freshwater and saltwater species. Fishkeepers often keep tropical fish in freshwater and \
  saltwater aquariums."

  line = line.translate(str.maketrans('','', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
  words=line.split()
  stems = words
  bigrams = [stems[i]+' '+stems[i+1] for i in range(len(stems)-1)]
  trigrams = [stems[i]+' '+stems[i+1]+' '+stems[i+2] for i in range(len(stems)-2)]

  keywords = ['fish', 'tropical', 'freshwater', 'saltwater', 'aquariums']

  bigrams1 = [gram for gram in bigrams if is_highlight(gram, keywords)]
  trigrams1 = [gram for gram in trigrams if is_highlight(gram, keywords)]
  print(bigrams1)
  print(trigrams1)

if __name__ == '__main__':
  create()


