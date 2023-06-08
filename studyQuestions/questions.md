# Review Questions
Review questions for the exam
## Week 2 Review Questions
### Question 1. 
Please open a text or an XML file (e.g., 6146.xml) and represent it as a list of paragraphs or sentences, text. You may remove any non-relevant information (e.g ‘<p>’, ‘</p>’, \‘n'). After that, you need to find all terms and their frequencies (the number of occurrences in the file) if their length > 2, represent them using a dictionary, doc; and print the number of total terms (e.g., 137). Then print the top-10 terms in doc in a descending order, e.g., [('the', 8), ('technical', 2), ('bounce', 2), ('said', 2), ('and', 2), ('not', 2), ('due', 2), ('rose', 2), ("argentina's", 2), ('argentine', 1)]

```python
import re

def get_terms(text): # text is a list of paragraphs or sentences
    terms = {}
    for term in text:
        if len(term) > 2: # if the length of the term > 2
            if term in terms: # if the term is in the dictionary
                terms[term] += 1 # increase the frequency by 1
            else:
                terms[term] = 1 # add the term to the dictionary
    return terms

def get_text(filename): # filename is a string
    with open(filename, 'r') as f:# open the file
        text = f.read() # read the file
        text = re.sub(r'<[^>]+>', '', text) # remove any non-relevant information
        text = re.sub(r'\n', '', text) # remove any non-relevant information
        text = re.sub(r'\s+', ' ', text) # remove any non-relevant information (e.g., ‘<p>’, ‘</p>’, ‘\n’)
        text = text.split(' ') # split the text into a list of paragraphs or sentences
        return text # return the list of paragraphs or sentences

text = get_text('6146.xml') # get the text
terms = get_terms(text) # get the terms and their frequencies
print(len(terms)) # print the number of total terms
print(sorted(terms.items(), key=lambda x: x[1], reverse=True)[:10]) # print the top-10 terms in a descending order
```
### Question 2. 
Which of the following is FALSE? and explain why it is FALSE.
1. Stemming is a component of text processing that captures the relationships between different variations of a word.
2.Stemming reduces the different forms of a word that occur because of inflection (e.g., plurals, tenses) or derivation (e.g., making a verb into a noun by adding the suffixation) to a common stem.
3.In general, using a stemmer for search applications with English text produces a small but noticeable improvement in the quality of results.
4. A dictionary-based stemmer uses a small program to decide whether two words are related, usually based on knowledge of word suffixes for a particular language.

Answer: 4, a dictionary contains no program, it is a a data structure that maps keys to values. it relies on some pre made dictionary to decide whether two words are related. a more appropriate answer would be an algorithm based stemmer which uses a small program to decide whether two words are related, usually based on knowledge of word suffixes for a particular language.



### Question 3 N-grams
Typically, n-grams are formed from overlapping sequences of words., i.e. move n-word “window” one word at a time in a document. For example, bigrams are 2 words sequences, and trigrams are 3 words sequences.

The definition of Tropical fish is described in the following document:
```
Tropical fish are generally those fish found in aquatic tropical environments around the
world, including both freshwater and saltwater species. Fishkeepers often keep tropical
fish in freshwater and saltwater aquariums.
```

Please design a python program to print all bigrams and trigrams of the above document that contain at least one of the highlighted key words (‘fish’, ‘tropical’, ‘freshwater’, ‘saltwater’, ‘aquariums’).

```python
import re
import string

myText - '''
Tropical fish are generally those fish found in aquatic tropical environments around the
world, including both freshwater and saltwater species. Fishkeepers often keep tropical
fish in freshwater and saltwater aquariums.
'''
keywords = ['fish', 'tropical', 'freshwater', 'saltwater', 'aquariums']

def get_ngrams(text, n):
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text) # remove any non-relevant information
    text = re.sub(r'\n', '', text) # remove any non-relevant information
    text = text.split(' ') # split the text into a list of paragraphs or sentences
    ngrams = []
    for i in range(len(text) - n + 1): # for each ngram
        ngram = text[i:i+n] # get the ngram
        ngrams.append(ngram) # add the ngram to the list of ngrams
    return ngrams

for keyword in keywords: # for each keyword
    print('keyword: ', keyword) # print the keyword
    bigrams = get_ngrams(myText, 2) # get the bigrams
    trigrams = get_ngrams(myText, 3) # get the trigrams
    for bigram in bigrams: # for each bigram
        if keyword in bigram: # if the keyword is in the bigram
            print(bigram) # print the bigram
    for trigram in trigrams: # for each trigram
        if keyword in trigram: # if the keyword is in the trigram
            print(trigram) # print the trigram

```

### Question 4. (Markov chain)
Assume when John is sad today, which isn't very usual: he either goes for a run, gobbles down ice cream or takes a nap next day. The Markov Chain depicted in the following state diagram has 3 possible states: “Sleep”, “Run”, and “Ice Cream”.

![image](markov.png)
Here is also the transition matrix for the Markov Chain:
![image](transistionMatrix.png)

1. According to the above diagram, if John spent sleeping a sad day away, what is the probability of the will likely go for a run next day?
- 0.6 or 60%

2. The transition matrix will be 3 ´ 3 matrix. To simple represent the matrix, we can use the following variables, for example:

```
SS - sleep -> sleep
SR - sleep -> run
SI - sleep -> ice cream
```

as a matrix representation in python aka (list of lists) as follows:

```
transition_matrix = [
    [SS, SR, SI],
    [RS, RR, RI],
    [IS, IR, II]
]
```

Please write the corresponding transition matrix for probabilities in a list of lists.
- Take the values above and replace the letters with the probabilities (e.g. SS = 0.2, SR = 0.6, SI = 0.2) and put them in a list of lists.
```
transition_matrix = [
    [0.2, 0.6, 0.2],
    [0.1, 0.6, 0.3],
    [0.2, 0.7, 0.1]
]
```


### Question 6.
Design a python program to extract all hyperlinks (or destination links) in a html file. You can use HTMLParser python package.
  
  ```python
  from html.parser import HTMLParser

  def get_links(html):
      class MyHTMLParser(HTMLParser): # create a class that inherits from HTMLParser
          def __init__(self): # define the constructor
              HTMLParser.__init__(self) # call the constructor of the parent class
              self.links = []
          def handle_starttag(self, tag, attrs): # define the handle_starttag method
              if tag == 'a': # if the tag is an anchor tag
                  for attr in attrs: # for each attribute
                      if attr[0] == 'href': # if the attribute is a hyperlink
                          self.links.append(attr[1]) # add the hyperlink to the list of links
      parser = MyHTMLParser()
      parser.feed(html)
      return parser.links

  html = '''
  <html>
  <head>
  <title>Page title</title>
  </head>
  <body>
  <a href="http://example.com/">Link text</a>
  </body>
  </html>
  '''
```

## Week 3 Review Questions


## Week 4 Review Questions
## Week 5 Review Questions
## Week 6 Review Questions
## Week 6 Review Questions
## Week 7 Review Questions
## Week 8 Review Questions
## Week 9 Review Questions
## Week 10 Review Questions
## Week 11 Review Questions