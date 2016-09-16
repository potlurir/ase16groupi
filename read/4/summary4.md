**i. Paper**

Automatic Labeling of Multinomial Topic Models - 2007

Qiaozhu Mei, Xuehua Shen, Chengxiang Zhai

**ii. Keywords**

ii1. *Multinomial word distributions* : This is a 'bag of words model'. Eventhough there is not conditioning on preceding context, nevertheless still gives the probability of a particular ordering of terms. Any other ordering of the bag of words will also have the same probability. Hence the distribution is called the multinomial distribution of words.

ii2. *Topic model* : In NLP topic model is a statistical model for discovering the abstract 'topics' in a collection of documents. The 'topics' that are produced by topic modeling techniques are clusters of similar words.

ii3. *K-L divergence* : It is a measure of difference between two probability distributions P and Q. It is sometimes defined as the information gain achieved if P is used instead of Q 

ii4. *Topic label* : A topic label for a model is a sequence of words which is semantically meaningful and covers the latent meaning of the model

**iii. Brief Notes**

iii1. *Motivational statements* : A big challenge today is to label a multinomial topic so that a user can interpret the discovered topic. So far, these labels have been generated in a manual subjective way. The requirement for automating this and generating labels in an objective way is clear. Manual label generation can be biased towards users opinion. Relying manual labeling also makes it difficult to apply such topic models to online tasks such as summarizing search results.

iii2. *Baseline results* : These are the results comparing manually generate labels to automatically generated labels and we can observe that the automatic label generator comes pretty close to generating semantically meaningful labels and close to manual ones
	
	|   			  | SIGMOD 															   | AP 													 |
	|-----------------|-------------------------------------------------------------------:|--------------------------------------------------------:|
	| Automatic label | clustering algorithm | r tree | data streams | concurrency control | air  force | court appeals | dollar rates | iran contra |
	|:---------------:|:--------------------:|:------:|:------------:|:-------------------:|:----------:|:-------------:|:------------:|:-----------:|
	| Manaul Label | clustering algorithms | indexing methods | Stream data  management | transaction management | air plane crash | death sentence | international stock trading | iran contra trial |
	|:------------:|:---------------------:|:----------------:|:-----------------------:|:----------------------:|:---------------:|:--------------:|:---------------------------:|:-----------------:|
	| Theta | clustering clusters video dimensional cluster partitioning quality birch | tree trees spatial b r disk array cache | stream streams continuous monitoring multimedia network over ip | transaction concurrency transactions recovery control protocols locking log | plane air flight pilot crew force accident crash | court judge attorney prison his trial case convinced | dollar l yen from late gold down london | north case trial iran documents walsh reagan charges |
	|:-----:|:------------------------------------------------------------------------:|:---------------------------------------:|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|:------------------------------------------------:|:----------------------------------------------------:|:---------------------------------------:|:----------------------------------------------------:|

iii3. *Related work* : 

iii4. *Study instruments* : 

**iv. Improvements**

iv1. As we can observe that automatic label generally picks up labels from the words in the topic and cannot search for words outside the topic to generate labels. It would be better if there is way where the words that are not in the topic can be used to label these topics if they make more semantic sense
iv2. 

**v. References**

v1. [Multinomial word distribution](http://nlp.stanford.edu/IR-book/html/htmledition/multinomial-distributions-over-words-1.html)

v2. [KL divergence wikipedia](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)

