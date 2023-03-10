from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
from pyparsing import line
import string



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

# Takes a string gram and a list of keywords keywords as input. It returns True if any of the keywords appear in the gram string, and False otherwise.
def is_highlight(gram, keywords):

    x = False
    for y in keywords:
        if y in gram:
            x = True
    return x


# defines a string variable line and applies some processing to it. First, it removes any digits in the string using the translate() method. 
# Then, it removes any punctuation using the translate() method again, this time replacing each punctuation character with a space of the same length. 
# The resulting string is split into individual words using the split() method.
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

    # bigrams1 and trigrams1 only contain bigrams and trigrams that contain at least one keyword. 
    # # This is achieved by calling the is_highlight() function for each bigram and trigram and only keeping those that return True.

  bigrams1 = [gram for gram in bigrams if is_highlight(gram, keywords)]
  trigrams1 = [gram for gram in trigrams if is_highlight(gram, keywords)]
  print(bigrams1)
  print(trigrams1)

if __name__ == '__main__':
  create()


