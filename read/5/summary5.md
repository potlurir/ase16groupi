**i. Paper**

Statistical Entity-Topic Models - 2006

David Newman, Chaitanya Chemudugunta, Padhraic Smyth

**ii. Keywords**

ii1. *Entity* : Documents contain, in addition to ordinary words, additional classes of words which are referred to as entities. For example entitiy can be persons(eg George Bush) or organizations(eg NFL) etc

ii2. *Topic model* : In NLP topic model is a statistical model for discovering the abstract 'topics' in a collection of documents. The 'topics' that are produced by topic modeling techniques are clusters of similar words.

ii3. *Switch LDA* : This model includes a Binomial distribution which control the fraction of entities in topics as an addition to CI-LDA model 

ii4. *Latent Dirichlet allocation* : In natural language processing, latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar.

**iii. Brief Notes**

iii1. *Motivational statements* : News articles aim to convey information about who, what, when and where. Statistical topic models can not distinguish between these different categories and produce topical descriptions that are mixtures of whos, whats, whens and wheres. But in many applications it is important for these different concepts to be explicitly modeled. Hence in this paper the problem of modeling text corpora where documents contain, in addition to ordinary words, additional classes of words called entities. The focus is on modeling entities and making predictions about entities based on learning that uses entities and wordsIn language modeling and information extraction, there is growing interest in finding and analyzing entities mentioned in text.

iii2. *Study Instruments* : The first data set is a collection of New York Times news articles taken from the Linguistic Data Consortium’s English Gigaword Second Edition corpus. All articles of type “story” from 2000 through 2002. These include articles from the NY Times daily newspaper publication as well as a sample of news from other urban and regional US newspapers. The second data set are articles from the Foreign Broadcast Information Service (FBIS), . FBIS articles come from around the globe, and include English translations of a variety of foreign news. FBIS articles spanning Feb 1999 to Nov 2000 were used

iii3. *Baseline results* : In the entity prediction task, the models are first trained on words and entities. The models then make predictions about entities in the test set using the words in the test set. In the entity-pair classification task, models are trained on words and entities or just entities. The models then make predictions about whether an entity pair is actual or fabricated. The proposed CorrLDA2 model gives a 7% improvement in average best rank, and a 4% improvement in average median rank over the standard LDA model for the NY Times 2 data. This average is computed over 11,000 test documents.

| model     | avg best rank | ang median rank |
|-----------|---------------|-----------------|
| LDA       | 19.4          | 435.2           |
| CI-LDA    | 19.4          | 433.5           |
| SwitchLDA | 18.3          | 433.7           |
| CorrLDA1  | 18.6          | 419.5           |
| CorrLDA2  | 18.1          | 417.5           |




iii4. *Future work* : These new algorithms designed could be extended to medical literature (e.g. PubMed) where one could create entity-topic models where the entities are genes and proteins mentioned in the text

**iv. Improvements**

iv1. Since this is a generalized algorithm, this is not at its optimal performance. By including human understanding of different contexts of data which in this case is news articles will improve the performance of this algorithm

iv2. Although this algorithm has worked on a couple of data sets with marginal improvements this algorithm must be tested on other data sets which are not explicit to news and which belong to a larger data set

**v. References**

v1. [Latent Dirichlet allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)

