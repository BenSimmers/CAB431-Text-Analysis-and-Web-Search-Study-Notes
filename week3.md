# Week 3 Search Engine Technology
## 1.0 Search Engine Architecture
- The architecture of a search engine involves software components, their interfaces, and how they relate to each other. It is a way to describe the system at a specific level of abstraction. The requirements for a search engine's architecture are effectiveness (quality of results), efficiency (response time and throughput), and the major functions of indexing and query processes.

<!-- add image here -->

## 2.0 Indexing Process
<!-- add image here -->

- Indexing has 3 main steps:
  - Text acquisition where it identifies and stores documents to be indexed.
  - Text Transformation - where the documents are transformed into index terms or features.
  - Index Creation - where it takes the index terms and creates a data structure (some list of indexes) that can be used to answer queries. ( fast searching )


## Details of Text Acquisition
- Use a of a Crawler
  - A **crawler** identifies and stores documents to be indexed for a search engine.
  - There are many types of crawlers used for a variety of purposes:
    - One example is a **web crawler** that is used to index the web.
      - A web crawler must efficiently find huge numbers of web pages and keep them up to date. (This is called coverage and freshness)

    - Another Example is a **single site** crawler that is used to index a single site.
    - Another is **Topical or focused crawler** used for vertical search (e.g. news, images, videos, etc.)

    - **Document crawlers** are used for enterprise and desktop search.
      - This is used to index documents on a local machine or a network. ( e.g. Scanning directories and files and example of this is the windows search engine or the mac spotlight search engine)

    - **Feed Crawlers** are used to index RSS feeds.
      - This is used to index RSS feeds. (e.g. Google news), also web feeds and social media feeds but RSS is the most common. For example RSS can provide new XML docs to a search engine to index.


### Coversion
  - This isnt a traditional step in the indexing process but it is a step that is often used to convert the documents into a format that is more suitable for indexing. (e.g. PDF to text), including the documents metadata.
    - HTML, XML, Word, PDF, etc. → XML → Indexing → Index → Query → Results 

  - This is a method called encoding, where UTF-8 is a unicode standard which helps in text encoding for different languages. (e.g. Chinese, Japanese, Korean, etc.)



## Text Acquisition continued.
  - **Document Data Store**
    - Document storage stores the text, metadata, and other information about the documents.

  - **What is Metadata?**
    - Metadata is data about data. It is data that describes other data. (e.g. Title, Author, Date, etc.)
    - Any other content links, images, anchors, etc. are also considered metadata.

  - Document Storage provides fast access to documents for search engines:
    - e.g. a list result generation: a search engine needs to retrieve the document data for each document in the list.

  - An alternative is using a Relational Database Management System (RDBMS) to store the document data.
    - a Simpler, more efficicent storage system is used for the document data store.
    - Only issue is relational databases struggle with scale, which is why many have moved to processes like neon to store data. (e.g. Google uses neon to store data)





## Text Transformation
- A parser is used to process a sequence of text tokens in the document to recognize structural elements such as paragraphs, headings, lists, tables, etc.

- The tokenizer can recognize the words in the text
  - However you must consider capitalization, punctuation, hyphensm apostrophes, etc.

- A markup language is used to identify the structural elements in the document.
  - e.g. HTML, XML, etc.
  - Through a markup language we can specify the structure of the document.
  e..g HTML has tags such as 
  ```html
    <p> for paragraph </p>
    <h1> for heading <h1>
    <li> for list item</li>
  ```

- A Document parser uses syntax of markup language (or other formatting) to identify structure


#### - Stopping
  - Remove common words that are not useful for indexing (e.g. the, a, an, etc.)
  - Some impact on effectiveness and efficiency
  - Can be a problem for queries that use these words (e.g. "the cat in the hat")

#### - Stemming
  - Stemming is where group words are derived from a common root (e.g. "stemming", "stemmed", "stems", "stemmer")
  - usually done by removing suffixes (e.g. "ing", "ed", "s", "er")
  - Somewhat effective but still not perfect
  - Benefits vary for different languages


#### - Link Analysis
  - Make use of links between documents to improve indexing
  - e.g. if a document is linked to by many other documents, it is probably important
    - Link analysis identifies the importance or popularity of a document
  - Anchor text can signifcantly enhance the representation of pages pointed by links
  - This can have a significant impact on the effectiveness of web search
    - less importance in other types of search (e.g. enterprise search)


#### Information extraction
- Information Extraction helps identify index terms that are important for some applications.
- e.g. for a news search engine, it is important to identify the names of people, places, and organizations in the document.

#### Classifier 
  - Identfies class related metadata for a document
    - ie assings labels to documents based on their content (e.g. sports, politics, etc.)
    - its use varies depending on the application


### Index Creation
#### Document statistics
  - Document statistics are used to identify the most important terms in a document.
  - Often a ranking algorithm is used to identify the most important terms

#### Weighting 
  - Weighting computes the weight for index terms in a document.
  - this is used within the ranking algorithm.
  - e.g. TF-IDF (Term Frequency - Inverse Document Frequency)

### Inversion
  - Inversion is the process of creating an index from the document statistics.
  - This is the process of creating a data structure that can be used to answer queries.
  - e.g. a list of index terms and the documents that contain them.

  - Core component of the indexing process
  - Converts the document-term information to a term-document information
    - This method is good however it is not the most efficient method and falls apart with large data sets.

  - Format of an inverted file is design for fast query processing (e.g. fast searching)
    - it must handle updates efficiently
    - compression is important for large collections


###  Index Distribution
- Distributes indexes across multiple computers and/or multiple sites
- Essential for fast query processing with large numbers of documents
- Many variations
- Document distribution, term distribution, replication
- P2P and distributed IR involve search across multiple sites



## 3.0 Query Process
<!-- Image here -->


- User Interaction - supports a creation and refning of queries
  - e.g. a search box, a search button, a search history, etc.

- Ranking - uses querying and indexing to rank the documents in the index
  - e.g. TF-IDF, PageRank, etc.

- Evaluation - monitors and measures the effectiveness of the search engine
  - e.g. precision, recall, etc.


#### User Interaction
##### Query Input 
  - Provides an interface and parser for the user to enter a query
  - Most web queries are very simple, other applications might use forms or other interfaces
  - e.g. a search box, a search button, a search history, etc.

  - Query Languages are used to describe more complex queries and large results of query tansformation
    - e.g. Boolean queries, Indri and Galago query languages
    - Very similar to SQL 
    - IR query languages allow content and structure to be specified in a single query but focus on the content of the query


##### Query Transformation
- Improves the quality of the query before and after it is submitted
  - e.g. spelling correction, query expansion, etc.
- Includes text transformations techniques such as stemming and stopping on the documents
- query expansion and relevance feedback are used to improve the quality of the query
  - e.g. query expansion is used to add terms to the query to improve the quality of the results
  - e.g. relevance feedback is used to improve the quality of the query by adding terms that are relevant to the user

##### Results Output
- Constructsd the display of the results
  - e.g. a list of results, a list of snippets, etc.
  - Generate snippets to show how the query matches the document
  - Highlight important terms in the document
  - Retrives appropriate metadata for the document and advertisements connected to the document
  - May provide clustering and other visualizations tools

#### Ranking
 - Scoring - calculates scores for documents using a ranking algorithm
 - Core component of a search engine - determines the order of the results
 - Basic form of of a score is $\sum (q_i * d_i)$ where $q_i$ is the weight of the query term and $d_i$ is the weight of the document term
 - Many variations of ranking algorithms and retrieval models




#### Link Analysis
- Billions of web pages are linked to each other, and some are more important than others
- Links can be viewed as information about the importance of a page
  - Often another part of the ranking algorithm
- Inlink (links pointing to a page) count could be used as simple measure
- Link analysis algorithms like PageRank provide more reliable ratings 
  - less susceptible to spamming


## Random Surfer Model
- what is the probability that a random surfer will visit a page?
- The probability that a random surfer will visit a page is proportional to the number of inlinks to that page

- Browse the web using the follwing algorithm 
  - Choose a random number $r$ between 0 and 1
  if $r < \lambda $ then
    - go to a random page
  if $r => \lambda $ then
    - go to a page that is linked to the current page
  - Start again

  Implementation in python
  ```python
  def randomSurferModel(graph, start, lambda, numSteps):
    # start is the starting page
    # lambda is the probability of choosing a random page
    # numSteps is the number of steps to take
    # graph is a dictionary of pages and links
    # returns a dictionary of pages and the number of times visited
    pages = graph.keys()
    visits = {}
    for page in pages:
      visits[page] = 0
    visits[start] = 1
    for i in range(numSteps):
      r = random.random()
      if r < lambda:
        # choose a random page
        page = random.choice(pages)
      else:
        # choose a page that is linked to the current page
        page = random.choice(graph[start])
      visits[page] += 1
      start = page
    return visits
  ```

  - PageRank of a page is the probability tha the random surfer will visit that page
  - PageRank is the probability that a random surfer will visit a page it points to

## Dangling Links 
 - Random jump prevents getting stuck on pages that have no outlinks, contains only outlinks to pages that have no outlinks, etc. Or have a link forming a cycle (loop)

- Links that point to the frist two types of pages are called dangling links
- They may also be links to pages that have not yet been crawled


## PageRank

- Formula:
  - $PR(u) = \sum_{v \in B_u} \frac{PR(v)}{L_v}$

  - $PR(u)$ is the PageRank of page $u$
  - $B_u$ is the set of pages that link to page $u$
  - $PR(v)$ is the PageRank of page $v$
  - $L_v$ is the number of outlinks from page $v$

  <!-- add photo and equation here -->

  Example:
  - We dont know the PageRank of any page (values at the start)
  - Therefore we assume equal values, in this example we have 3 pages so we assume each page has a PageRank of 1/3

  First Iteration:
  $PR(C) = 0.33/2 + 0.33 = 0.5, PR(A) = 0.33,  PR(B) = 0.17$

  Second Iteration:
  $PR(C) = 0.33/2 + 0.17 = 0.33, PR(A) = 0.5, PR(B) = 0.17$

  Third Iteration:
    $PR(C) = 0.42, PR(A) = 0.33, PR(B) = 0.25$

  Convergence:
  $ PR(C) = 0.4, PR(A) = 0.4, and PR(B) = 0.2$

- Taking a random page jump into account, theres is a 1/3 chanceof going to any page when $r < \lambda$
$PR(C) = λ/3 + (1 − λ) · (PR(A)/2 + PR(B)/1)$

More General Form:
$PR(C) = λ/N + (1 − λ) · \sum_{v \in B_u} \frac{PR(v)}{L_v}$

- $N$ is the number of pages in the graph
- $λ$ is the probability of choosing a random page
- $B_u$ is the set of pages that link to page $u$
- $PR(v)$ is the PageRank of page $v$
- $L_v$ is the number of outlinks from page $v$



### Page Rank Algorithm
<!-- add image here -->

### Ranking cont.
- Opttimization 
  - We can design ranking algorithms for more efficient processing 
    - Term at a time vs document at a time
    - Safe vs unsafe optimizations


- Distribution 
  - Processing queries on a single machine is not scalable therefore we need to distribute the processing
  - Query Broker - distributes the query to the appropriate servers
  - Caching is a form of distributed searching


## Evaluation
Logging
- Logging user queries and interaction is crucial for improving search effectiveness and efficiency
- Query logs and clickthrough data used for query suggestion, spell checking, query caching, ranking, advertising search, and other components such as:
  - Ranking analysis
  - Measuring and tuning ranking effectiveness
  - Performance analysis
  - Measuring and tuning system efficiency


### Web Crawler
- A web crawler is a program that browses the web automatically
- It Finds a URL, fetches the page, extracts links, and repeats the process
- Crawlers are used to build search engines and to maintain up-to-date copies of web pages

- Since the web is huge and dynamic and constantly growing, it is not under the control of search engine providers

- Webpages are constantly changing and the line between static and dynamic pages is becoming blurred
- Websites and desktop apps are also going in this direction with tools such as Electron with JS and Tauri with Rust

- Crawlers also used for other types of data
- Sites that are difficult to find are collectivel referred to as the deep web which is not indexed by search engines and is much larger than the conventional web we use search engines for.

<!-- Add image here -->

#### Retrieving Web Pages
- Web pages are retrieved using the HTTP protocol
- Every page a a unique URL (Uniform Resource Locator) which describes the web page.

- The URL is a string that contains the protocol(scheme), host, and path to the resource

e.g.
- https://www.google.com/search?q=web+crawler

<!-- break this down in a table -->
| Protocol | Host | Path |
| --- | --- | --- |
| https | www.google.com | /search?q=web+crawler |

- Web pages are stored on web servers that use the HTTP protocol to communicate with web browsers or client software

- Most URLs used on the web have the scheme http indicating that the page is retrieved using the HTTP protocol. Even though the page is retrieved using the HTTP protocol, the page is sent to the browser using the HTTPS protocol which is a secure version of HTTP and should always be used when possible.

- The Host is the name of the server that stores the web page
- The Path is the path to the resource on the server these are commonly files stored on the same server as the base site


- Web browsers and web crawlers fetch web pages in the same way. Both first connect to a DNS server to translate the hostname into an IP address. Then they attempt to connect to the server computer with that IP address to request a page using an HTTP GET request. The web server sends the contents of the requested file back to the client.


#### Web Crawling Algorithms
- The crawler starts with a set of seed URLs and adds them to a request queue. It then fetches pages from the queue and parses them to find links that may contain useful URLs. The crawler adds these new URLs to its request queue, which may be ordered so that important pages are prioritized. The process continues until there are no more new URLs or the disk is full.

An implementation in Python
```python
import requests
from bs4 import BeautifulSoup

# Set the seed URLs
seeds = ["https://www.example.com"]

# Initialize the request queue with the seed URLs
queue = seeds.copy()

# Initialize a set to keep track of visited URLs
visited = set()

# Set the maximum number of pages to crawl
max_pages = 100

# Initialize a counter for the number of crawled pages
count = 0

# Loop through the request queue
while queue and count < max_pages:
    # Get the next URL from the queue
    url = queue.pop(0)
    
    # Skip URLs that have already been visited
    if url in visited:
        continue
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Add the URL to the visited set
    visited.add(url)
    
    # Increment the count of crawled pages
    count += 1
    
    # Print the title of the page
    print(soup.title.string)
    
    # Find all the links on the page
    for link in soup.find_all("a"):
        # Get the URL of the link
        href = link.get("href")
        
        # Check if the URL is valid and not already visited
        if href and href not in visited and href not in queue:
            # Add the URL to the end of the queue
            queue.append(href)
```


#### Politeness Policies
- Web crawlers spend alot of time waiting for responses to requests
To reduce this inefficiency, web crawlers use threads and fetch hundreds of
pages at once
- Crawlers could potentially flood sites with requests for pages
- To avoid this problem, web crawlers use politeness policies
- e.g., delay between requests to same web server


#### Controlling Crawling
- Even crawling a site slowly will anger some web server administrators, who object to any copying of their data

- Robots.txt file can be used to control crawlers

- 6he quick way to prevent robots visiting your site is put these two lines into the /robots.txt


### Freshness
- Web pages are constantly being added, deleted, and modified so search engines need to keep their indexes up-to-date

- web crawker must continuously revisit pages to check for changes to see if they need to be updated in the index

- Stale copies no longer reflect the real contents of the web apge

-  HTTP protocol has a special request type called HEAD that makes it easy to
check for page changes

- returns information about page, not page itself

- Not possible to constantly check all pages
- must check important pages and pages that change frequently
- Freshness is the proportion of pages that are fresh
- Optimizing for this metric can lead to bad decisions, such as not crawling popular sites
- Age is a better metric


#### Focused Crawling
- A focused crawler attempts to download only those pages that are about a particular topic. This type of crawler is commonly used by vertical search applications. Focused crawlers rely on the fact that pages about a topic tend to have links to other pages on the same topic. Popular pages for a topic are typically used as seeds. The crawler uses a text classifier to decide whether a page is on topic or not.



#### Sitemaps
- Sitemaps are files that contain lists of URLs and data about those URLs, such as modification time and frequency of modification. These files are generated by web server administrators and provide crawlers with information about pages they might not otherwise find. Sitemaps also give crawlers a hint about when to check a page for changes, based on the modification frequency indicated in the sitemap.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://www.example.com/page1.html</loc>
    <lastmod>2022-02-15</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://www.example.com/page2.html</loc>
    <lastmod>2022-02-20</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.6</priority>
  </url>
  <url>
    <loc>https://www.example.com/page3.html</loc>
    <lastmod>2022-01-01</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.4</priority>
  </url>
</urlset>
```

### Document Feeds
- published documents from a single source can be ordered in a sequence called a document feed, which can be either push or pull feeds. The most common format for pull feeds is RSS (Really Simple Syndication), which is a standardized XML format for publishing frequently updated content such as news articles, blog posts, and podcasts. RSS allows subscribers to receive new content automatically as soon as it is published, without having to visit the website manually.
### Storing the Documents
- The given information highlights the reasons to store converted document text, which include saving crawling time when the page is not updated, providing efficient access to text for snippet generation and information extraction, and enabling the use of database systems for document storage. Web search engines often use customized document storage systems that have requirements such as random access based on the URL, compression of large files, and the ability to handle large volumes of new and modified documents while adding new anchor text. The document storage system should also be capable of efficiently reducing storage requirements and enabling efficient access to the stored content.
### Large Files
To optimize storage and access efficiency, it is recommended to store many documents in large files instead of storing each document in a separate file. This approach reduces the overhead in opening and closing files and also improves the seek time relative to read time. Compound documents formats, such as TREC Web, can be used to store multiple documents in a single file.

Compression techniques can be applied to reduce the size of text files, as the text is highly redundant and predictable. Popular compression algorithms such as DEFLATE (zip, gzip) and LZW (UNIX compress, PDF) can compress HTML and XML text by up to 80%. Large files may be compressed in blocks to make access faster. It is important to note that compression of indexes will be covered later.

### BigTable
• Google’s document storage system
• Customized for storing, finding, and updating web pages
• Handles large collection sizes using inexpensive computers
• No query language, no complex queries to optimize
• Only row-level transactions
• Tablets are stored in a replicated file system that is accessible by all BigTable servers
• Any changes to a BigTable tablet are recorded to a transaction log, which is also stored in a shared file system
• If any tablet server crashes, another server can immediately read the tablet data and transaction log from the
file system and take over
### BigTable row
- Logically organized into rows
- A row stores data for a single web page
- Combination of a row key, a column key, and a timestamp point to a single cell
in the ro
### Detecting Duplicates
BigTable can have a huge number of columns per row
• all rows have the same column groups (families)
• not all rows have the same columns
• important for reducing disk reads to access document data
• Rows are partitioned into tablets based on their row keys
• simplifies determining which server is appropriate


### Duplicate Detection
• Duplicate and near-duplicate documents occur in many situations
• Copies, versions, plagiarism, spam, mirror sites
• 30% of the web pages in a large crawl are exact or near duplicates of pages in the other 70%
• Duplicates consume significant resources during crawling, indexing, and search
• Little value to most users

### Near-Duplicate Detection
• Exact duplicate detection is relatively easy
• Checksum techniques
• A checksum is a value that is computed based on the content of the document
• e.g., sum of the bytes in the document file
• Possible for files with different text to have same checksum
• Functions such as a cyclic redundancy check (CRC), have been developed that consider the positions of the bytes

### Fingerprints
1. The html is pared into words, non word content such as punctuation, tags etc is removed

2. The words are grouped into contiguous n-grams for some n. these are usually overlapping sequences of words, although some techniques use non overlapping sequences

3. Some of the n-grams selected to represent the document.

4. The selected n-grams are hashed to improve efficiency and further reduce the size of the representation

5. The hash values are stored in an inverted index

6. Documents are compared using overlap fingerprints 
### Example
```python
def generate_trigrams(text):
    otext = text.split()
    trigrams = [otext[i]+' '+otext[i+1]+' '+otext[i+2] for i in range(len(otext)-2)]
    return trigrams
```
```python
otext ='Tropical fish include fish found in tropical environments around the world including both freshwater and salt water species'
trigrams = generate_trigrams(otext)
print(trigrams)
```
```python
# Output
['Tropical fish include', 'fish include fish', 'include fish found', 'fish found in', 'found in tropical', 'in tropical environments', 'tropical environments around', 'environments around the', 'around the world', 'the world including', 'world including both', 'including both freshwater', 'both freshwater and', 'freshwater and salt', 'and salt water', 'salt water species']
```


### Removing Noise
### Finding Content Blocks