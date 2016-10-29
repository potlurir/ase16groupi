#### 1. Paper:
How to Effectively Use Topic Models for Software Engineering Tasks? An Approach Based on Genetic Algorithms
Annibale Panichella1, Bogdan Dit2, Rocco Oliveto3, Massimilano Di Penta4, Denys Poshynanyk2, Andrea De Lucia1

Year - 2013

#### 2. Keywords:

ii1. *Latent Dirichlet allocation* : In natural language processing, latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar.

ii2. *LDA-GA* : Novel algorithm which uses Genetic Algorithms (GA) to determine a near-optimal configuration for LDA in the context of three different SE tasks: (1) traceability link recovery, (2) feature location, and (3) software  artifact labeling

ii3.  *Genetic Algoritms* - A genetic algorithm (GA) is a method for solving both constrained and unconstrained optimization problems based on a natural selection process that mimics biological evolution. The algorithm repeatedly modifies a population of individual solutions.

ii4. *LSI(Latent Semantic Indexing)* - Is a system used by Google and other major search engines. The contents of a webpage are crawled by a search engine and the most common words and phrases are collated and identified as the keywords for the page.

**iii. Brief Notes**

iii1. *Motivational statements* : Information Retrieval (IR) methods, and in particular topic models, have recently been used to support essential software engineering (SE) tasks, by enabling software textual retrieval and analysis. In all these approaches, topic models have been used on software artifacts in a similar manner as they were used on natural language documents (e.g., using the same settings and parameters) because the underlying assumption was that source code and natural language documents are similar. However, applying topic models on software data using the same settings as for natural language text did not always produce the expected results. Recent research investigated this assumption and showed that source code is much more repetitive and predictable as compared to the natural language text. Our paper builds on this new fundamental finding and proposes a novel solution to adapt, configure and effectively use a topic modeling technique, namely Latent Dirichlet Allocation (LDA), to achieve better (acceptable) performance across various SE tasks.

iii2. *Study Instruments * - The experiment has been conducted on software repositories from two projects, EasyClinic and eTour. EasyClinic is a system used to manage a doctor’s office, while eTour is an electronic touristic guide. The documentation, source code identifiers, and comments for both systems are written in Italian. Various components of the data are terms of type, number of source and target artifacts, as well as Kilo Lines of Code (KLOC). There is a table also reports the number of correct links between the source and target artifacts. These correct links, which are derived from the traceability matrix provided by the original developers, are used as an oracle to evaluate the accuracy of the proposed traceability recovery method.

iii3. *Statistical tests* : a) Box Plots - boxplots to highlight the variability of the average precision values across different configurations
						    
						    b) Precision and Recall graphs - Precision and recall are the basic measures used in evaluating search strategies. RECALL is the ratio of the number of relevant records retrieved to the total number of relevant records in the database. PRECISION is the ratio of the number of relevant records retrieved to the total number of irrelevant and relevant records retrieved. It is usually expressed as a percentage. For both EasyClinic and eTour data, LDA-GA was able to obtain a recovery accuracy close to the accuracy achieved by the optimal configuration across 1,000 and 2,000 different configurations executed in the combinatorial search. In particular, for EasyClinic LDA-GA returned exactly the configuration identified by the combinatorial search (i.e., the two curves are perfectly overlapped) while on eTour the two curves are comparable.

						    c) Wilcoxon test - The Wilcoxon signed-rank test is a non-parametric statistical hypothesis test used when comparing two related samples, matched samples, or repeated measurements on a single sample to assess whether their population mean ranks differ (i.e. it is a paired difference test).

iii4. *Future Work* : As mentioned in the paper the future work would be to corroborating the results reported in this paper on other datasets. We also plan to apply LDA-GA on other SE tasks that rely on text analysis using topic models.

**iv. Improvements**

iv1. LDA-GA's performance on various other documents sets must be evaluated. In this paper it is mentioned that it has performed better than LDA in documents LDA-GA was not intended for. Is this an anamoly of taking two specific datasets or is LDA-GA more universal and performs better on all documents? This question must be answered

iv2. The dataset description must be better and must be provided in the paper itself. Why these datasets are chosen in the first place?

iv3. Precision and Recall are the simplest tools to evaluate results. These results are natural language based. These results must be compared to results generated by humans and the results of LDA-GA being compared to LDA does not make much sense.

**v. References**

v1. [Latent Dirichlet allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)

v1. [Latent semantic indexing](https://www.searchenginejournal.com/what-is-latent-semantic-indexing-seo-defined/21642/)
