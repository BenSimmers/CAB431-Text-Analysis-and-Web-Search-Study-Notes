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
</student>
```

- XML is essentially about content it does not describe how to present it
- HTML is about presentation

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