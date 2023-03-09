# Cab431 - Text Analysis and Web Search

Everything written here is based off the QUT course content. However, there are at times parts of text that are taken from the QUT slides and most of the examples are directly from the course slides (these are referenced when done). This content is designed only for those currently studying an IT degree at QUT, do not share these resources with anyone outside of this community.

If any member of the QUT staff or a representative of such finds any issue with these guides please contact me and I will take this down without an argument. The last thing I want to do is cause any issues or damages to the QUT name or QUT resources. I am simply just trying to help students out with presenting the content in an easy to digest manor.

Disclaimer

Although these documents may provide a decent learning experience on their own it is highly advised that you use these in-part with the lectures notes and videos provided to you by your lecturer. This is mainly due to the fact that overtime these guides may become outdated as the units themselves get updated.

It is also important to remember that these guides are written by students and as part should always be taken with a grain of salt, always read further into topics you don't understand and always do your own research on topics. These guides are designed to give you a brief description on each topic giving you a nice overview of the unit and a solid exam time revision document.

A note for programming units, when it comes to programming the best way to learn is not by reading theory but by practising in a practical way. Follow along with the guides but customize the exercises to your liking and make an attempt to utilise the language being learnt in home projects of your own.


# Week 1 - Introduction

## Whats it all about?

- Query: Big Data
- Documents: information links Ads
- Ranking: results are ordered
- Serp: Search Engine Results Page

## What’s It All About? Cont.

### Web Search & Text analysis
- This unit uses a two-pronged approach to give you a deeper appreciation and understanding of Web search and text analysis
- Basic concepts and models for NLP (Natural Language Processing), IR (Information Retrieval) and Web search (Weeks 1-6)
- Techniques for Text Analysis (Weeks 7-13):
- Supervised text analysis
- Un-supervised text analysis
- To help you to understand search engines, text analysis, evaluation, designing and implementation of NLP systems.

### PART I: Web Search, NLP and IR Search-based problem solving
- Architecture of a search engine
- Basic concepts for natural language (text) processing (NLP)
- Information Retrieval (IR) models
- Evaluation of search results & IR models  

### PART II: Text Analysis AI-based problem solving
- Supervised methods
- Information filtering
- Text classification
- Relevant discovery
- Un-supervised techniques
- Text feature selection
- Topic modelling
- Sentiment analysis
- Document summarization

## Why is this important?

- Big data is a collection of data so large and complex that it becomes very difficult to process. It extends beyond structured data, including unstructured data: text, audio, video, click streams, log files and more.

- It is estimated that more than 80% of big data were stored in text format that contain a large amount of invaluable knowledge to be automatically extracted.

- The dramatic increase in the availability of massive text data from various sources is creating a number of issues and challenges for NLP & text analysis and such as the noisy and uncertain information, scalability and effectiveness.

- Big data is more than a challenge for enterprisers. It is also an opportunity to find insight in new and emerging types of data, to make business more agile, and to answer questions that, in the past, were beyond reach.

- Therefore, there is a significant need for more efficient and effective techniques to facilitate the process.

# Web Information & Data

- Search on the Web is a daily activity for many people throughout the world.
- The vast amount of information available on the Web has great potential to improve the quality of decisions and the productivity of consumers.
- In many cases, manual browsing through even a limited portion of the relevant information obtainable through search engines is no longer efficient.
- However, the Web’s large number of information sources and their different levels of accessibility, reliability, completeness, and associated costs present human decision makers with a complex information gathering planning problem that is too difficult to solve without high-level filtering of information

# The World Wide Web

- The Internet continues to blossom as millions of new sites come on line each month.
- The Web was developed as additional protocols to the three widely used Internet protocols (Telnet, SMTP, and FTP).
- The protocol developed was the HyperText Transport Protocol (HTTP). Each pointer become known as a Uniform Resource Locator (URL).
- Toward the end of 1990s, the WWW Consortium (W3C) developed XML to expand the realm of applications of the Web. Many of concepts from HTML carry over to XML.

HTML is a language for marking up text for presentation in web browsers - with a few extensions (originally HTML was about content, but presentation became incorporated)
- XML is a language for describing data - not necessarily for web-based presentation. Itis extensible i.e. no fixed set of elements like HTML.
- Example XML document:

```
<student>
  <name>John Doe</name>
  <age>30</age>
  <address>1234 Some Street, Brisbane, QLD, 4000</address>
```

- XML is essentially about content e.g. <name> Yuefeng Li </name> states this element is a name, it does not describe how to present it
- HTML is about presentation: e.g.
- <B> Yuefeng Li </B> states that the text “Yuefeng Li” should be presented bold – we do not know it’s a name!
- <A HREF="http://www.w3.org/">W3C</A> states a hyperlink and anchor text.


## XML: Extensible Markup Language
- what is xml
- xml is a markup language
- A common language for describing data using tree-like data structures
- Can be used for e.g. document representation (for storage and transfer), business to business communication, etc.
- Independent of platform and application
- Importantly XML is extensible
  - Does not impose a specific set of elements
  - Can be used to describe any data



## Accessing a web page
URLs can be resolved into Web documents by (e.g.) Web browsers 
- This is done by invoking a Web browser on a local machine and typing in a URL for the document
- The browser then uses the HTTP protocol to connect to a Web server on a distant machine corresponding to the location of the URL, and displays the document 
- By clicking on URLs embedded within the displayed document as hypertext links, the user can navigate from Web page to Web page

The Web browser sends the domain name to a Domain Name Servers, which returns the Internet Protocol (IP) address for the domain name. 
- Every machine on the Internet has a unique domain name and unique IP address (e.g., qut.edu.au, its IP is 131.181.196.203)


### Accessing Web Page example cont.
- The Web browser sends the file name to the Web server at IP address 128.8.128.80
- the Web server appends the name index.html because the given file was a directory and not a file.
- The contents of the file users/book/index.html are sent back to the Web browser and displayed to the user.
- Web server log files
  - Usually web servers record some of their transactions in a log file.
  -  Log files contain information on visits.
  - A typical example is a web server log which maintains a history of page requests

### Web Search and Information Retrieval
- Search and communication are some of the most popular uses of the computer
- Applications involving search are everywhere.
- The field of computer science that is most involved with R&D for search is information retrieval (IR) 
- It is a field concerned with the structure, analysis, organization, storage, searching, and retrieval of information. (Salton, 1968)
- General definition that can be applied to many types of information and search applications.
- The introduction of web search engines has boosted the need for very large-scale retrieval systems even further.

### What is a Document?
- Examples
  - Web pages, emails, books, news stories, scholarly papers etc

- Common properties
  - A Document is a collection of words
  - some structures such as an XML document might have a field for title, author, date etc.
  - A html file might contain links

### Documents vs. Database Records
- Database records (or tuples in relational databases) are typically made up of well-defined fields (or attributes)
- e.g., bank records with account numbers, balances, names, addresses, social security numbers, dates of birth, etc. 
- They are structured
  - Easy to compare fields with well-defined semantics to queries in order to find matches

- Text is more diffuse
  - No well-defined fields
  - No well-defined semantics
  - No well-defined structure
  - No well-defined way to compare to queries

### Comparing text
- Comparing the query text to the document text and determining how well they match is the core issue of information retrieval

- Exact matching of words is not good enough
- Many different ways to write the same thing in a “natural language” (like English).

### Dimensions of IR
- IR is more than just text, and more than just web search
  - although these are central
- People doing IR work with different media, different types of search applications, and different tasks

### Dimensions of IR cont.
Content Applications Tasks
Text Web search Ad hoc search
Images Vertical search Filtering
Video Enterprise search Classification
Scanned docs Desktop search Question answering
Audio  Forum search
Music P2P search
Literature search


### Big Issues in IR ()
#### Relevance
- What is it?
- Simple (and simplistic) definition: A relevant document contains the 
information that a person was looking for when they submitted a query to the 
search engine
- Many factors influence a person’s decision about what is relevant: e.g., task, 
context, novelty, style
- Topical relevance (same topics) vs. user relevance (everything else)



#### Evaluation
- Experimental procedures and measures for comparing system output with user expectations
- Originated in Cranfield experiments in the 60s
- IR evaluation methods now used in many fields such as machine learning and data mining. 
- Typically use test collection of documents, queries (or topics), and relevance judgments
- Most commonly used are TREC (Text REtrieval Conference) collections
- https://trec.nist.gov/
- Recall and precision are two examples of effectiveness measures



#### Users and Information Needs
- Search evaluation is user-centered.
- Keyword queries are often poor descriptions of actual information needs.
- Interaction and context are important for understanding user intent.
- Query refinement techniques such as query expansion, query suggestion, 
relevance feedback improve ranking (we will discuss these techniques in this 
unit).

### NLP, IR and Search Engines
- A search engine is the practical application of information retrieval techniques to 
large scale text collections
- Web search engines are best-known examples, but many others
- Open-source search engines are important for research and development
- e.g., Lucene, Lemur/Indri, Galago
- Recent ChatGPT
- Big issues include main IR issues but also some others



### Search Engine Issues
#### Performance
- Measuring and improving the efficiency of search 
- e.g., reducing response time, increasing query throughput,  increasing 
indexing speed
- Indexes are data structures designed to improve search efficiency
- designing and implementing them are major issues for search engines


#### Dynamic data
- The “collection” for most real applications is constantly changing in terms of 
updates, additions, deletions
- e.g., web pages
- Acquiring or “crawling” the documents is a major task
- Typical measures are coverage (how much has been indexed) and 
freshness (how recently was it indexed)
- Updating the indexes while processing queries is also a design issue


#### Scalability
- Making everything work with millions of users every day, and many terabytes 
of documents
- Distributed processing is essential
- Adaptability
- Changing and tuning search engine components such as ranking algorithm, 
indexing strategy, interface for different applications


## Text Analysis
- It is the process of deriving high quality information from a set of documents. 
- High-quality information is typically derived through the devising of topics, 
patterns and trends through means such as learning algorithms.
- Text mining (Text analytics) describes a set of linguistic, statistical, and machine 
learning techniques that model and structure text information for business 
intelligence, exploratory data analysis, research, or investigation.


_________

# Week 2  - NLP - Text Pre-Processing
## Processing Text
- Converting documents to index terms
- why?
  - Matching the exact string of characters typed by the user is not a good idea
    - it doesnt work well in terms of effectiveness
    - Not all words are equal value in a search
    - Sometimes not clear where words start and end
    - Not even clear what a word is in a different language e.g. Chinese, Korean, Japanese

## Text Statistics
Huge variety of words used in text but
- Many statistical characteristics of word occurrences are predictable
-  e.g., distribution of word counts
-  Retrieval models and ranking algorithms depend heavily on statistical properties of words
- e.g., important words occur often in documents but are not high frequency in collection


## Zipf’s Law
- Distribution of wor frequencies in a collection is very skewed
 - a few words can occur very often and many words occur very rarely

 e.g. two most common words are “the” and “of”  and make up about 10% of the words in a typical English text collection

## Vocabulary Growth
- As corpus grows, so does vocabulary size
  - Fewer new words when corpus is already large
- Observed relationship is Heaps’ Law
  - H = kN^b
  - H = vocabulary size
  - N = number of documents
  - k, b = parameters
  - b = 0.4 for English
  - k = 100 for English

## Web Example
- Heaps law with very large corpora
  - new words occurring even after seeing 30 million documents
  - paramter values differ than typical TREC (text retrieval conference) values
- New words come from a variety of sources
  - spelling errors, invented words e.g. product, company names, slang, etc. code, other languages, email, etc.
- Web Search must deal with these large and growing vocabularies


## Document Parsing 
- Document parsing involves the recognition of the content and structure of a document
- forming words from sequences of characters is called tokenization
- Surprisingly complex in english, can be harder in other languages
- **Definitions of words in early IR systems:**
  - any sequence of alphanumeric characters of length 3 or more
  - terminated by a space or other special character
  - upper-case changed to lower-case

## Tokenizing Example
- Example:
  - "Bigcorp's 2007 bi-annual report showed profits rose 10%." -> "bigcorp 2007 annual report showed profits rose"
- Too simple for search applications or even large-scale experiments
- why? Too much information lost
  - small decision in tokenizing can have major impact on effectiveness of some queries


## Tokenizing Problems
- Small words can be important in some queries, usually in combinations
  - xp, ma, pm, ben e king, el paso, master p, gm, j lo, world war II, VW (volkswagen), etc.
- Both hyphenated and non-hyphenated forms of many words are common.
- Sometimes hyphens are not needed
    - e.g. e-bay, wal-mart, active-x, cd-rom, t-shirts
- At other times, hyphens should be considered either as part of thw word or a word separator
   - e.g. winston-salem, mazda rx-7, e-cards, pre-diabetes t-mobile, spanish-speaking


## Tokenizing Problems cont.
- Special characters are an important part of tags, urls, code in documents.
- Capitalization can have different meaning from lower case words. e.g. Bush, Apple
- Apostrophes can be a part of a word, a part of a possessive or just a mistake, 
- rosie o'donnell, can't, don't, 80's, 1890's, men's straw hats, master's degree, england's ten largest cities, shriner’s.

## Tokenizing Problems
- Numbers can be important, including decimals
  - Nokia 3250, top 10 courses, united 93.
- Periods can occur in numbers, abbreviations, URLs, ends of sentences and other situations.
- I.B.M, Ph.D, F.E.A.R
- Note: tokenizing steps for queries must be identical to steps for documents

## Tokenizing Process
- First step is to use parser to identify apporpriate parts of the document tokenize 

- Defer complex decisions to other components
  - word is any sequence of alphanumeric characters, terminated by a space or special character with everything converted to lower case
  - everything indexed
  - Example: 92.3 -> 92 3 but search finds documents with 92 and 3 adjacent
  - incorporate some rules to reduce dependence on query transformation components
    - Examples of rules used with TREC
      - Apostrophes in words ignored
        - o'donnell -> odonnell
      Periods in abbreviations ignored
        - U.S.A. -> USA

## Example
```py
import string
line ="<p>The British Fashion Awards will be held on October 22 at London's Royal Albert Hall.</p>“
line = line.replace("<p>", "").replace("</p>", "")
line = line.translate(str.maketrans('','', string.digits)).translate(str.maketrans(string.punctuation, ' '*len(string.punctuation)))
words=line.split()
terms=[word.lower() for word in words if len(word)>2]
```

## Stopping
- Function words have little meaning on their own;
  - e.g., the, a, an, of, in, on, at, to, from, etc.
- High occurrence frequencies
- Treated as stopwords (ie removed )
  - reduce index space, improve response time, improve effectiveness
- can be important in combinations
  e.g. to be or not to be


## Stopwords cont.
- Stopword list can be treated from high-frequency words or based of a standard list
- Lists are customized for applications, domains and even parts of documents
    e.g. "Click" is a good stopword for anchor text
- **Best Policy** os tp index all words in documents, amke decisions about which words to use at query time.

## Stemming 
- Many morphological variants of a word have the same meaning
  - inflectional variants
    - e.g. run, runs, running, ran
  - derivational variants
    - e.g. verb, noun, adjective
- In most cases these have the same or very similar meanings
- stemmers attept to reduce morphological variants to a common stem 
  - e.g. running -> run
- This can be done at indexing time or as part of query processing (like stopwords)

## Stemming cont.
- generally, a small but significant effectiveness improvement
- can be crucial for some languages
e.g. 5-10% improvement for English, up to 50% for arabic

- Words with the Arabic root ktb
- Kitab (book)
- Kitabat (books)
- kitabi (my book)


## Stemming cont.
- two basic types
  - Dictionary-based
    - use a list of known words 
  - Agorithmic
    - uses programs to determine the related words

- Algorithmic stemmers
  - Suffix-s: remove 's' endings assuming plural
  e.g. cats -> cat
  - Many false negatives (have different stems): triangle -> triangular
  - Some false positives (have same stem): policy -> police

## Porter Stemmer
- Algorithmic stemmer used in IR since the 1970s
- Consists of a series of rules designed to the longest possible suffix at each step
- Effective in TREC
- Produces stems not words
- Makes a number of errors and difficult to modify
```py
import os
from stemming.porter2 import stem
os.chdir ('C:\\2023\\Python_code\\workshop_tutor\\wk_solutions')
os.getcwd()
stems=[stem(term) for term in terms]
# result is ['the', 'british', 'fashion', 'octob', 'royal', 'hall', 'will', 'albert', 'london', 'held', 'award']v
```



## Porter Stemmer 
Example step (1 of 5)
Step 1a:
- sses -> ss
- Delete s if the preceding word part contains a vowel not immediately preceded by a short s e.g. gaps -> gap but gas -> gas
- Replace ied or ies by i if proceeded by more than one letter otherwise by ie (so ties -> tie, cries -> cri, but die -> die, by -> by)
- if suffix is us or ss do nothing

step 1b:
- replace eed, eedly by ee if it is in the part of thw word after the first non-vowel following a vowel (so feed -> feed, agreed -> agree, but speed -> speed)
- Delete  ed, edly, ing, ingly if the proceeding word part contains a vowel, and then if the word ends in at, bl, iz, or if the word ends with a double and the word part before the double is not one of l, s, z, then add e

- Porter2 stemmer addresses some of these issues, e.g., stem('policy’) = ‘polici’, and stem('police’) =‘polic’ by using Porter2.

## Krovetz Stemmer
-  Hybrid Algorithmic stemmer
  - Word checked in dictionary
  - if present, either left alone or replaced with "exceptional" 
  - if not present, word is checked for suffixes that can be removed
  - if suffixes are removed, the word is checked in the dictionary again
- Produces words not stems
- Comparable effectiveness 
- lover false positives than Porter, somewhat higher false negatives

## Stemmer Comparison
- krovetz is the best stemmer for English

## Phrases and N-grams
- Mant queries are 2-3 word phrases
- phrases are 
  - more precise than single words 
    - e.g. documents containing "new york" are more likely to be relevant than those containing "new" or "york"
  - Less ambiguous
    - e.g. "big apple" is more likely to be "new york" than "apple"
- Can be difficult for ranking when we use them
- e.g. given query fishing supplies, how do we socre documents with:
  - exact phrase many times, exact phrase once, individual words in the same sentence, same paragraph, same document, variations on words

## Phrases
- Text processing issue - how are phrases recognized?
- three possible approaches
  - Identify syntatic phrases using a part-of-speech (POS) tagger
  - Use N-grams
  store word positions in indexes and use proximity operators in queries

## POS Tagging
- POS taggers use statistical models of text to predict syntactic tags of words
- Example tags
  - NN (singular noun), NNS (plural noun), VB (verb), VBD (verb, past
tense), VBN (verb, past participle), IN (preposition), JJ (adjective), CC
(conjunction, e.g., “and”, “or”), PRP (pronoun), and MD (modal auxiliary,
e.g., “can”, “will”).

- phrases can be then defined as simple noun groups, noun phrases, verb phrases, etc.

## Python nltk
- The POS tagger in the NLTK library outputs specific tags for words
- This is not a standard python library and therefore needs to be installed using pip: `pip3 install nltk`
```py
impor t nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = word_tokenize('''Document will describe marketing strategies carried out by U.S. companies for their agricultural chemicals, report predictions for market share of such chemicals, or report market statistics for agrochemicals, pesticide, herbicide, fungicide, insecticide, fertilizer, predicted sales, market share, stimulate demand, price cut, volume of sales.''')
text = [x for x in text if len(x)>1]
pos_results = nltk.pos_tag(text)
print(pos_results)
```

## Word N-grams
- POS tagging too slow for large collections 
- Simpler definition - phrase is any sequence of $n$ words - n-gram
  - bigram: 2 word sequence, trigram: 3 word sequence, unigram: single words
  - N-grams also used at character level for applications such as OCR
    - I.E. move n-word "window" one word at a time in document
```py
stems = ['the', 'british', 'fashion', 'octob', 'royal', 'hall', 'will', 'albert', 'london', 'held', 'award']
>>> bigrams = [stems[i]+' '+stems[i+1] for i in range(len(stems)-1)]
>>> bigrams
['the british', 'british fashion', 'fashion octob', 'octob royal', 'royal hall', 'hall will', 'will albert', 'albert london', 'london held', 'held award']
>>> trigrams = [stems[i]+' '+stems[i+1]+' '+stems[i+2] for i in range(len(stems)-2)]
>>> trigrams
['the british fashion', 'british fashion octob', 'fashion octob royal', 'octob royal hall', 'royal hall will', 'hall will albert', 'will albert london', 'albert london held', 'london held award']
```

## N-grams Cont.
- Frequent n-grams are more likely to be meaningful phrases
- N-grams form a Zipf distribution
  - better fit than words alone
- Could index all n-grams up to specified length
  - much faster than POS tagging
  - Uses alot of storage
    - e.g. document containing 1000 words would contain 3990 instnace word n-grams of length $2<=n<=5$

## Google N-Grams
- web search engines index n-grams
- Most frequent trigram in english is "all rights reserved"
- How to select a small set of n-grams [2]


## 2. Information Extraction
- Automatically extract structure from text
  - annotate document using tags to identify extracted structure
- Named entity recognition
  - identify words that refer to something of interest in a particular application
  - e.g., people, companies, locations, dates, product names, prices, etc.

## Named Entity Recognition
Fred Smith, a 32-year-old resident of New York, is a long time collector of tropical fish

<p><PersonName> Fred Smith </PersonName>, a <Number> 32-year-old </Number> resident of <LocationName> New York </LocationName>, is a long time collector of tropical fish </p>

- Example showing semantic annotation of text using xml tags
- Information extraction also includes document structure and more complex features such as relationships and events

## Approaches for Named Entity Recognition
- Rule-based
- Uses lexicons (lists of words and phrases) that categorize names
- e.g., locations, peoples’ names, organizations, etc.
- Rules also used to verify or find new entity names
- e.g., “<number> <word> street” for addresses
- “<street address>, <city>” or “in <city>” to verify city names
- “<street address>, <city>, <state>” to find new cities
- “<title> <name>” to find new names

- Rules either developed manually by trial or using machine learning techniques
- Statistical Approach
  - uses a probabilistic model to identify named entities
  - e.g., “<number> <word> street” for addresses
  - “<street address>, <city>” or “in <city>” to verify city names
  - probabilities estimated using training data
  - Hidden Markov Model (HMM) used to model the probability of a sequence of words

## HMM for Extraction
- Resolve ambiguity in a word using context (the words that surround it)
- e.g., “marathon” is a location or a sporting event, “boston marathon” is a
specific sporting event
- Model context using a generative model of the sequence of words
- Markov property: the next word in a sequence depends only on a small
number of the previous words

## HMM for Extraction cont.
- Markov model describes a process as a collection of states with transitions between states
  - each transition has a probability associated with it
  - next state depends only on current state and transition probabilities
- HMMs are a special case of Markov models
  - each state has a state of possible outputs 
  - outputs have probabilities

## Examples of MM and HMM
- See hmm.png 

## HMM for Extraction
- could generate sentences with this model
- to recognize named entities, find sequence of "labels", that give highest probability for the sentence
  - only the outputs(words) are visible or observed
  - states are hidden
  - e.g. ```<start><name><not-an-entity><location><not-an-entity><end>```
- can use Viterbi algorithm to find most likely sequence of states

## Inputs and output of HMM
- Inputs
- The observation space O, e.g., O is a set of words.
- The state space S , e.g., S includes entities, such as, “location”, “person”, “organization” and “not-an-entity”; and the initial probabilities p i of each state s i or entity.
- Transition matrix A, where A ij is the transition probability of transiting from state si to state s j .
- Emission matrix B, where B ij is the probability of observing o j from state s i
- a sequence of observation Y ( a sub-set of O in order)
- Output
- The most likely hidden state sequence X

## Named Entity Recognition
 Accurate recognition requires about 1M words of training data (1,500 news stories)
- may be more expensive than developing rules for some applications
- Both rule-based and statistical approaches can achieve about 90%
effectiveness for categories such as names, locations, organizations
- others, such as product name, can be much worse

## 3. Document Structure and Markup
- Some parts of documents are more important than others
- Document parser recognizes structure using markup like HTML tags
 - Headers, anchors, bolded text
 - Metadata can also be important
 - Links used for *Link analysis*

 ## Html tags
  - ```<html>``` - root tag
  - ```<head>``` - metadata
  - ```<body>``` - content
  - ```<title>``` - title of document
  - ```<h1>``` - header
  - ```<p>``` - paragraph
  - ```<a>``` - anchor
  - ```<b>``` - bold
  - ```<i>``` - italic
  - ```<img>``` - image
  - ```<table>``` - table
  - ```<tr>``` - table row
  - ```<td>``` - table cell

## Hyperlinks
- Links are a key component of the web
 - Important for navigation, but also for web search
 e.g.
  - ```<a href="http://www.cs.cmu.edu/~enron/">Enron</a>```
  Enron is the anchor text
  http://www.cs.cmu.edu/~enron/ is the link
  both are used by search engines

## Anchor Text
- Used as a description of the content of the destination page
- i.e., collection of anchor text in all links pointing to a page used as an
additional text field
- Anchor text tends to be short, descriptive, and similar to query text
- Retrieval experiments have shown that anchor text has significant impact on
effectiveness for some types of queries.

# Week 3 Search Engine Technology

# Week 4 Information Retrieval Models

# Week 5 - Document Representation

# Week 6 - Evaluation