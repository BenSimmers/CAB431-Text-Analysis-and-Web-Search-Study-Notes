
**Learning Objectives**

1. *Overview and Older IR Models*
   1. *Relevance*
   1. *Boolean Retrieval*
   1. *Vector Space Model*
1. Probabilistic Models
   1. Bayes classifier
   1. Binary independence model
   1. BM25
1. Language models
   1. Topics and Language Models
   1. Query-Likelihood Model
   1. Jelinek-Mercer Smoothing
1. *Relevance models*
- *Pseudo-Relevance Feedback*
- *KL-Divergence*
- RocchioAlgorithm
1. **Overview and Old IR Models**
- Information retrieval (IR) models provide a mathematical framework for defining the search process
  - includes explanation of assumptions
  - basis of many ranking algorithms
  - can be implicit
- For a given query *Q*, an IR model finds relevant documents to answer *Q*.
- Progress in IR models has corresponded with improvements in **effectiveness**.
- The key research issue is theories about relevance.

**Relevance**

- Complex concept that has been studied for some time
  - Many factors to consider 
  - People often disagree when making ***relevance judgments***
- IR models make various assumptions about relevance to **simplify problem**
  - e.g., ***topical*** vs. *user* relevance
    - A document is topically relevant to a query if it is judged to be on the same topic, i.e., the query and the document are about the same thing. 
    - User relevance considers all the other factors that go into a user’s judgment of relevance.
  - e.g., ***binary*** vs. *multi-valued* relevance

**Order IR Models**

- **Boolean Retrieval**
  - Two possible outcomes for query processing
    - TRUE and FALSE
    - “exact-match” retrieval
    - simplest form of ranking
  - Query usually specified using Boolean operators
    - AND, OR, NOT,  
    - Proximity operators (define constraints on the distance **between words**; e.g., requiring words to co-occur within a certain “window” (length) of text); and 
    - Wildcard characters (define the minimum string match required for **a word**) are also commonly used in Boolean queries. 

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

Searching by Numbers 6![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.004.png)

- It is the process of developing queries with a focus on the size of **the retrieved document set**. 
- It is a consequence of the limitations of the Boolean retrieval model.
- For example, sequence of queries driven by number of retrieved documents
  - e.g. “lincoln” search of news articles
  - president AND lincoln
  - president AND lincolnAND NOT (automobile OR car)
  - president AND lincolnAND biography AND life AND birthplace AND gettysburgAND NOT (automobile OR car)
  - president AND lincolnAND (biography OR life OR birthplace OR gettysburg) AND NOT (automobile OR car)

This will retrieve any document containing the words “president” and “lincoln”, along with any one of the words “biography”, “life”, “birthplace”, or “gettysburg” (and does not mention “automobile” or “car”).

CRICOS No.00213J


**Boolean Retrieval**

- Advantages
  - Results are predictable, relatively easy to explain to users
  - Many different features can be incorporated (e.g., document date or type)
  - Efficient processing since many documents can be eliminated from search
- Disadvantages
  - Effectiveness depends entirely on user queries (simple queries will not work well).
  - Complex queries are difficult that requires considerable experience.

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

**Vector Space Model** 8![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.004.png)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.005.jpeg)

- Documents and query represented by a vector of term weights

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.006.png)

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.007.png)

- A Collection of Documents can be represented by a matrix of **term weights**

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.008.jpeg)

- Example (in inverted indexing)  ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.009.jpeg)
- 3-d pictures useful, but can be misleading for high- dimensional space 

CRICOS No.00213J 

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
11

**Vector Space Model - similarity measure**

- Documents ranked by distance between points representing query and documents
  - *Similarity* measure more common than a distance or *dissimilarity* measure
  - e.g., Cosine correlation

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.010.jpeg)

CRICOS No.00213J![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.007.png)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.011.png)

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
13

Example of Similarity Calculation

•Consider two documents *D D* and a query *Q*

*1,  2* 

- *D* = (0.5, 0.8, 0.3), *D* = (0.9, 0.4, 0.2), *Q* = (1.5, 1.0, 0)

*1 2*

CRICOS No.00213J ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.012.jpeg)

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

**Document Representation - *Term Weights*** 11

- *Tf\*idf* weight
  - Term frequency weight measures importance of term *k* in document (*D*):

*i*

- Inverse document frequency measures importance in collection: ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.013.jpeg)
- Some heuristic modifications![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.014.png)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.015.png)

log + 1  log( / )

= ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.016.png)

∑ [ log + 1  log( / )]

Incorrect Eq in the text-book![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.017.jpeg)

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
17

**Vector Space Model cont.**

- Advantages
  - Simple computational framework for ranking.
  - Any similarity measure or term weighting scheme could be used.
- Disadvantages
  - Assumption of term independence.
  - No *predictions* about techniques for effective ranking. There is an **implicit assumption that relevance** is related to the similarity of query and document vectors.
2. **Probabilistic Models**
- It is hard to prove that an IR model will achieve better effectiveness than any other model since we are trying to formalize a complex human activity.
- The validity of a retrieval model generally has to be validated empirically, rather than theoretically.
- **Probability Ranking Principle** (early theoretical statement about effectiveness, Robertson (1977)). “Originally described as follow”: 
  - “If a reference retrieval system’s response to each request is a **ranking of the documents** in the collection in order of decreasing probability of relevance to the user who submitted the request, 
  - where **the probabilities** are estimated as accurately as possible on the basis of whatever data have been made available to the system for this purpose, 
  - the overall effectiveness of the system to its user will be the best that is obtainable on the basis of those data.”

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

IR as Classification **- Bayes Classifier** 14![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.004.png)

- Bayes Decision Rule![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.018.jpeg)
  - A document *D* is relevant if *P*(*R*|*D*) > *P*(*NR*|*D*)
- Estimating probabilities
  - use **Bayes Rule**

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.019.png)

- *P*(*R*) is the priori probability of  relevance
- classify document *D* as relevant if *P*(*R*|*D*) > 
- *P*(*R*|*D*) is a **conditional probability**  *P*(*NR*|*D*) , i.e., 

representing the probability of relevance  ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.020.jpeg)for the given  document *D*, and  

- *P*(*NR*|*D*) is the conditional probability of  • The left-hand side (lhs) is *likelihood ratio.* non-relevance.

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

Examples of Relevant and Non-relevant documents![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.021.png)

**Document ID Terms:  d Relevance to Q** 15

**ij**

**D1** GERMAN, VW 0     no 

**D2** US, US, ECONOM, SPY 1     yes

**D3** US, BILL, ECONOM, ESPIONAG 1     yes

**D4** US, ECONOM, ESPIONAG, BILL 1     yes

**D5** GERMAN, MAN, VW, ESPIONAG 0      no

**D6** GERMAN, GERMAN, MAN, VW, SPY 0      no

**D7** US, MAN, VW 0      no

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

- Let *Q* = {US, ECONOM, ESPIONAG} be a query
- ***C*** = {*D*1, *D*2, *D*3, *D*4, *D*5, *D*6, *D*7} be a collection of documents, where *D* = {GERMAN, VW} 

1

*D* = {US, US, ECONOM, SPY}

2

*D* = {US, BILL, ECONOM, ESPIONAG}

3

*D* = {US, ECONOM, ESPIONAG, BILL}

4

*D* = {GERMAN, MAN, VW, ESPIONAG}

5

*D* = {GERMAN, GERMAN, MAN, VW, SPY}

6

*D* = {US, MAN, VW}

7

- *P*(*R*|*D*5) = ?, *P*(*R*|*D*) = ?  Where *D* = {US, VW, ESPIONAG} = {*d*1, *d*2, *d*3}
- *P*(*R*|*D*)  = [P(R)/P(D)] *P*(*D*|*R*), how to calculate *P*(*D*|*R*)?

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

Estimating *P*(*D*|*R*)

- Assume independence
- *Binary independence model![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.022.jpeg)*
  - document represented by a vector of binary features indicating term occurrence (or non-occurrence). E.g., 
    - *T* = {US, BILL, ECONOM, ESPIONAG, GERMAN, MAN, VW, SPY }
    - *D* = {US, VW, ESPIONAG} 
    - The binary vector of *D* = (1, 0, 0, 1, 0, 0, 1, 0)
  - *pi* is probability that term *i* occurs (i.e., has value 1) in relevant documents, *si* is probability of occurrence in non-relevant documents.

**Binary Independence Model** 17![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.023.jpeg)

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.024.jpeg)

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.025.jpeg)

Where *i*:*di*= 1 means terms that have the value 1 (presence) in the document; and *i*:*di*= 0 means terms that have the value 0 (absence) in the document.

**Binary Independence Model cont**

- Scoring function is (if we ignore the common 2nd product)

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.026.jpeg)

- Query provides information about relevant documents
- If we assume *p* constant, *s* approximated by entire collection, get *idf*-like *i i*

weight:  

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.027.jpeg)

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

**Contingency Table** 19![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.004.png)

*ri*is the number of relevant documents containing term *i n![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.028.png)i* is the number of documents containing term *i*

*N* is the total number of documents in the collection 

*R* is the number of relevant documents for this query

*di*= 1 if term *i* is present in the document, and 0 otherwise Example: *term* 1 = ‘US’

**Relevant  Non-relevant Total**

**d1 = 1** r1 =      3 n1 –r1 =                                        1 n1 =     4 **d1 = 0** R- r1  =  0 (N-R)-( n1 –r1) = N- n1 –R +r1 =   3 N- n1 = 3 **Total** R =       3 N-R =                                         4 N =     7

` `![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.029.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.030.jpeg)

Putting these estimates into the scoring function:

CRICOS No.00213J![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.031.jpeg)

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

**BM25** 20

- Popular and effective ranking algorithm based on binary independence model
  - adds document and query term weights

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.032.jpeg)

- *fi* is the frequency of term i in the document; 
- *qfi* is the frequency of term i in the query;
- *k1, k2*  and *K* are parameters whose values are set empirically
- , *dl* is doc length and *avdl* is the average length of a document in the collection.![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.033.png)
- Typical TREC value for *k1* is 1.2, *k2*  varies from 0 to 1000, b = 0.75

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
31

**BM25 Example**

- Query with two terms, “president lincoln”, (*qf = 1)*
- No relevance information (*r and R are* zero)
- *N* = 500,000 documents
- *“president”* occurs in 40,000 documents (*n1* = 40, 000)
- *“lincoln”* occurs in 300 documents (*n2* = 300)
- “president” occurs 15 times in doc (*f1* = 15)
- *“lincoln”* occurs 25 times (*f2* = 25)
- document length is 90% of the average length (*dl/avdl* = .9) 
- *k1* = 1.2, *b* = 0.75, and *k2* = 100
- *K* = 1.2 · (0.25 + 0.75 · 0.9) = 1.11

**BM25  ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.034.jpeg)Example** 

**BM25 Example**

- Effect of term frequencies

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.035.jpeg)

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

3. **Language Models** 24
- *Unigram language model (a simple language model)*
  - probability distribution over the words in a language.
  - For example, if the documents in a collection contained just five different words (*w*1, *w*2, ..., *w*5), a possible language model for that collection might be 
    - (0.2, 0.1, 0.35, 0.25, 0.1)
    - where each number is the probability of a word occurring.
- N-gram language model
  - predicts words based on longer sequences are used. An *n*-gram model predicts a word based on the previous ***n* − 1 words.**
  - The most common n-gram models are bigram (predicting based on the previous *word*) and trigram (predicting based on the previous two words) models.

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
39

**Topics and Language Models**

- We can use language models to represent the topical content of a document.
- A topic is defined as a probability distribution over words – a language model. 
- A language model can be used to “generate” new text by sample words according to the probability distribution.
- A *topic* in a document or query can be represented as a language model
  - i.e., words that tend to occur often when discussing a topic will have high probabilities in the corresponding language model

LMs for Retrieval

- Three possibilities:
  - probability of generating the query text from a document language model
  - probability of generating the document text from a query language model
  - comparing the language models representing the query and document topics
- Models of topical relevance
  - The probability of query generation is the measure of how likely it is that a document is about the same topic as the query.

**Query-Likelihood Model**

- Rank documents by the probability that the query could be generated by the document model (i.e. same topic)
- Given query, start with *P*(*D*|*Q*)
- Using Bayes’ Rule ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.036.jpeg)
- Assuming priori is uniform, unigram model

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.037.jpeg)

Estimating Probabilities

- Obvious estimate for unigram probabilities is 

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.038.jpeg)

- where f is the number of times query word q occurs in document D. qi,D i
- If query words are missing from document, score will be zero
  - This is the major problem. 
  - E.g., missing 1 out of 4 query words same as missing 3 out of 4.
  - This is clearly not appropriate for longer queries.

Smoothing

- Document texts are a *sample* from the language model
  - Missing words should not have zero probability of occurring
- *Smoothing* is a technique for estimating probabilities for missing (or unseen) words
  - lower (or *discount*) the probability estimates for words that are seen in the document text
  - assign that “left-over” probability to the estimates for the words that are not seen in the text

Estimating Probabilities

- Estimate for unseen words in a document *D* is *α P*(*q*|*C*)

*D i*

- *P*(*qi*|*C*) is the probability for query word *i* in the *collection* language model for collection *C* (background probability)
- *α* is a parameter

*D*

- Then, the estimate for words that occur in *D* is

(1 − *αD*) *P*(*qi*|*D*) + *αD P*(*qi*|*C*)

- Different forms of estimation come from different *αD*

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
41

**Jelinek-Mercer Smoothing**

- *αD* is a constant, λ
- Gives estimate of

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.039.jpeg)

- where cqi is the number of times a query word occurs in C, and |C| is the total number of word occurrences in collection C.
- Ranking score![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.040.jpeg)
- Use logs for convenience 
  - accuracy problems multiplying small numbers

CRICOS No.00213J ![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.041.jpeg)

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 


4. **Relevance Models**
- A relevance model represents the **topics** covered by relevant documents.
  - *E.g.,* language model can be used to represent information need
    - query and relevant documents are samples of text generated from this model
- Document likelihood model
  - *P*(*D|R*) – is interpreted as the probability of generating the text in a document given a relevance model *R*.
  - less effective than query likelihood due to difficulties comparing across documents (often documents are large) of different lengths.
  - Note that a document with a model that is very similar to the relevance model is likely to be on the same topic.
  - how to compare two language models (one for documents and another for the relevant documents)?

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

**Pseudo-Relevance Feedback** 33

- Relevance feedback is to acquire user feedback on the output that are initially returned from a given query *Q*.
- The feedback describes user information needs, and users typically label relevant outputs for *Q* (unlabelled outputs can be considered non-relevant information).
- In practical applications, there are three types of feedback: explicit feedback, implicit feedback, and "pseudo" feedback.
- **Pseudo relevance feedback** (blind feedback) is a method of finding an initial set of most likely relevant documents. Normally, we assume that the top "*k*" ranked documents are relevant to *Q*.
- Pseudo relevance feedback can be used to estimate a ***relevance model*** from **query** *Q* and **top-k ranked documents.**
  - Then we can rank new documents by similarity of document model to this *relevance model*.
  - *Kullback-Leibler divergence* (KL-divergence) is a well-known measure of the **difference** between two probability distributions. It can be used to measure the **similarity** between a document model and a relevance model.

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
47

**KL-Divergence**

- Given the *true* probability distribution *P* and another distribution *Q* that is an *approximation* to *P*,

( )![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.042.png)

( || ) = − 

( )

- Use negative KL-divergence for ranking, and
- assume relevance model *R for the query* is the true distribution (not symmetric), and the approximation to be the document language model (*D*):  

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.043.jpeg)

*Please note the second term of this equation does not depend on the document and can be ignored for the purpose of ranking*.

**KL-Divergence cont.**

- Given a simple maximum likelihood estimate for *P*(*w* | *R*)*,* based on the frequency in the query text, ranking score for a document is

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.044.jpeg)

- *Q* can be expanded as *Q* + top-k ranked documents. 
- *P*(*w* |*D*) is rank-equivalent to query likelihood score (see page 31 for the definition of *p*(*qi* | *D*)).
- Query likelihood model is a special case of retrieval based on relevance model.

**Estimating the Relevance Model**

- Probability of pulling a word *w* out of the “bucket” representing the relevance model depends on the *n* query words we have just pulled out

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.045.jpeg)

- We view the probability of *w* is the conditional probability of observing *w* given that we just observed the query words *q*1 . . . *qn*
- By definition

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.046.jpeg)

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
49

**Estimating the Relevance Model cont.**

- Joint probability is![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.047.jpeg)
- Assume![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.048.jpeg)
- Gives![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.049.jpeg)
- *Where C* is the set of top-k ranked documents*; P*(*D*) is usually assumed to be uniform; 
- *P*(*w, q*1 *. . . qn*) is simply a weighted average of the language model probabilities for *w* in a set of documents, where the weights are the query likelihood scores for those documents
- Formal model for pseudo-relevance feedback

CRICOS No.00213J • query expansion technique 

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 


**Pseudo-Feedback Algorithm**

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.050.png)

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
51

**Example from Top 10 Docs**

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.051.jpeg)

**Example from Top 50 Docs**

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.052.jpeg)

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

**Rocchio Algorithm** 40

- It is developed based on Relevance Feedback (or Pseudo-Feedback).
- It is a technique for query modification 
- *Rocchio algorithm*
  - Maximizes the difference between the average vector representing the relevant documents and the average vector representing the non-relevant documents.
- Modifies query *Q* to *Q’* (optimal query) according to

![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.053.jpeg)

- *α*, *β*, and *γ* are parameters
  - Typical values 8, 16, 4
- *qj* is the initial weight of query term *j*,
- *dij* is the weight (if\*idf) of the *j*th term in document *i,*
- *Rel* is the set of identified relevant documents,
- *Nonrel* is the set of non-relevant documents,
- | . | gives the size of a set.

CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 

41

**References**

- Chapter 7 (sections 7.1, 7.2 and 7.3) in textbook - W. Bruce Croft, *Search Engines - Information retrieval in Practice*; Pearson, 2010.
- Chapter 1, "Probability", 1993, ISBN : 978-1-4612-6937-3, <https://qut.primo.exlibrisgroup.com/permalink/61QUT_INST/1g7tbfa/alma991010463496504001>
- Albishre K., Li Y., Xu Y. (2018) *Query-Based Automatic Training Set Selection for Microblog Retrieval*. In: Phung D., Tseng V., Webb G., Ho B., Ganji M., Rashidi L. (eds) Advances in Knowledge Discovery and Data Mining. PAKDD 2018. Lecture Notes in Computer Science, vol 10938. **DOI <https://doi.org/10.1007/978-3-319-93037-4_26>**
- Albishre, K., Li, Y. *et al.* Query-based unsupervised learning for improving social media search. *World Wide Web* **23,** 1791–1809 (2020). <https://doi.org/10.1007/s11280-019-00747-0>
CRICOS No.00213J

`  `**![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.002.jpeg)![](Aspose.Words.dc6bc90e-6f55-49fe-99e7-e3719a98c1bd.003.png)** 
