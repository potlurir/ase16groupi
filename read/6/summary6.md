**i. Paper**

Finding scientific topics - 2004

T. L. Griffiths and M. Steyvers

**ii. Keywords**

ii1. *Gibbs Sampling* : In statistics, Gibbs sampling or a Gibbs sampler is a Markov chain Monte Carlo (MCMC) algorithm for obtaining a sequence of observations which are approximated from a specified multivariate probability distribution, when direct sampling is difficult..

ii2. *Generative models* : In probability and statistics, a generative model is a model for randomly generating observable data values, typically given some hidden parameters. It specifies a joint probability distribution over observation and label sequences. Generative models are used in machine learning for either modeling data directly, or as an intermediate step to forming a conditional probability density function.

ii3.*Latent Dirichlet allocation* : In natural language processing, latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar.

ii4. *Markov chain Monte Carlo* : In statistics, Markov chain Monte Carlo (MCMC) methods are a class of algorithms for sampling from a probability distribution based on constructing a Markov chain that has the desired distribution as its equilibrium distribution.

**iii. Brief Notes**

iii1. *Motivational statements* : A first step in identifying the content of a document is determining which topics that document addresses. When scientists decide to write a paper, one of the first things they do is identify an interesting subset of the many possible topics of scientific investigation. The topics addressed by a paper are also one of the first pieces of information a person tries to extract when reading a scientific abstract. Scientific experts know which topics are pursued in their field, and this information plays a role in their assessments of whether papers are relevant to their interests, which research areas are rising or falling in popularity, and how papers relate to one another. This paper provides a statistical method for automatically extracting a representation of documents that provides a first-order approximation to the kind of knowledge available to domain experts.

iii2. *Study instruments* : Generated a small dataset in which the output of the algorithm can be shown graphically. The dataset consisted of a set of 2,000 images, each containing 25 pixels in a 5 × 5 grid. The intensity of any pixel is specified by an integer value between zero and infinity. This dataset is of exactly the same form as a word-document co-occurrence matrix constructed from a database of documents, with each image being a document, with each pixel being a word, and with the intensity of a pixel being its frequency. They divided the dataset into 1,000 training images and 1,000 test images and ran each algorithm four times, using the same initial conditions for all three algorithms on a given run.

iii3.  *Hypotheses* : The topics recovered by this algorithm pick out meaningful aspects of the structure of science and reveal some of the relationships between scientific papers in different disciplines. The results of this algorithm have several interesting applications that can make it easier for people to understand the information contained in large knowledge domains, including exploring topic dynamics and indicating the role that words play in the semantic content of documents. This algorithm can be used to gain insight into the content of scientific documents. 

iii4. *Future work* : They intend to extend this work by exploring both more complex models and more sophisticated algorithms. Discovering the topics underlying the structure of datasets is the first step to being able to visualize their content and discover meaningful trends. Hence there can be visualization algorithms that can be built on this algorithm


**iv. Improvements**

iv1. Instead of using just topic modeling, entity modeling can be included in understanding the knowledge represented by documents. 

iv2. In this article they have focused on the analysis of scientific documents, as represented by the articles published in PNAS, the methods and applications we have presented are relevant to a variety of other knowledge domains

**v. References**

v1. [Gibbs Sampling](https://en.wikipedia.org/wiki/Gibbs_sampling)

v2. [Latent Dirichlet allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)

