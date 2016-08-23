####1. Paper:
Anh Tuan Nguyen, Tung Thanh Nguyen, Tien N. Nguyen, David Lo and Chengnian Sun. 2012. Duplicate Bug Report Detection with a Combination of Information Retrieval and Topic Modeling.

####2. Keywords:

*2.1. Duplicate Bug Detection*: Figuring out if different reports of a bug (by different people at different times) refer to a same issue in the software

*2.2. Latent Dirichlet Allocation (LDA)*: Latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar

*2.3. Topic Model*: A topic model is a type of statistical model for discovering the abstract "topics" that occur in a collection of documents

*2.4. Information Retrieval*: Information retrieval (IR) is the activity of obtaining information resources relevant to an information need from a collection of information resources.

####3) Brief Notes:

*3.1. Motivational Statements*: The ability to detect whether two (or more) reported bugs are duplicates has many benefits; like it saves developers’ efforts pondering over the same bug. Moreover, it points out the bugs which have not been fixed (partially or completely).

*3.2. Related Work*: Different approaches have been taken for duplicate bugs detection. 
Information Retrieval - Using Tf-Idf coupled with NLP techniques to enhance the  accuracy of the results.
Machine Learning - Different approaches using machine learning algorithms have been studied - like binary classifier, SVM - but ML approaches tend to be less time efficient. On the other hand, it has been showed that advanced IR approaches outperform state-of-the-art ML approaches in accuracy and efficiency.
The authors’ prior work ‘BugScout’ 

*3.3. Data*: 

|Project| Time period | Report|  Dup| Train| Test|
|---------|----------------|----------|-------|--------|-----|
|OpenOffice| 01/01/2008 - 12/21/2010| 31,138| 3,371| 200| 3,171|
|Mozilla |01/01/2010 - 12/31/2010 |75,653| 6,925| 200 |6,725|
|Eclipse |01/01/2008 - 12/31/2008 |45,234| 3,080 |200 |2,880|

*3.4. New results*: 
The authors’ applied their DBTM approach on 3 project’s bug databases - Eclipse, OpenOffice and Mozilla.

*Sensitivity Analysis*: The authors ran DBTM for number of topics (K) ranging from 20 to 400. The best results were achieved for K between 60 to 380. Although this range varies for different projects.

*Accuracy Comparison*: For project Eclipse, DBTM detects a duplicate bug with just a single recommendation in 57% of the cases; with top-5 matches in 76% of the cases and with top-10 reports it correctly predicts in 82% of the cases. For OpenOffice and Mozilla the results are similarly accurate.

*Time Efficiency*: The training and predicting time increase approximately linearly with the project size. The authors conclude that DBTM is scalable and efficient to be used interactively in detecting duplicate bugs.

####4. Improvements:
As the authors have mentioned the results are based on only 3 projects which have fairly standard bug reporting. The algorithms should be applied to other projects (opensource and commercial) to check the generality of the approach.


####5. References:
*5.1. [Wikipedia definition for Topic Model](https://en.wikipedia.org/wiki/Topic_model)*

*5.2. [Wikipedia definition for Information Retrieval](https://en.wikipedia.org/wiki/Information_retrieval)*

*5.3. [Wikipedia definition for Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)*
