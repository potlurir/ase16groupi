#### 1. Paper:
A Statistical Semantic Language Model for Source Code
Tung Thanh Nguyen, Anh Tuan Nguyen, Hoan Anh Nguyen, Tien N. Nguyen

Year - 2013

#### 2. Keywords:

ii1. *n-gram Model* : In the fields of computational linguistics and probability, an n-gram is a contiguous sequence of n items from a given sequence of text or speech.

ii2. *Lexical Code Token* : A lexical code token is a unit in the textual representation of source code and associated with a lexical token type including identifier, keyword, or symbol, specified by the programming language.

ii3.  *Lexeme* - The lexeme of a token is a sequence of characters representing its lexical value.

ii4. *Lexical Code Sequence* - A lexical code sequence is a sequence of consecutive code tokens representing a portion of source code.

**iii. Brief Notes**

iii1. *Motivational statements* : Recent research has successfully applied the statistical ngram language model to show that source code exhibits a good level of repetition. The n-gram model is shown to have good predictability in supporting code suggestion and completion. However, the state-of-the-art n-gram approach to capture source code regularities/patterns is based only on the lexical information in a local context of the code units. Based on SLAMC,
we developed a new code suggestion method, which is empirically evaluated on several projects to have relatively 18–68% higher accuracy than the state-of-the-art approach. 

iii2. *Study Instruments* -  The data set consists of nine systems with a total of more than 2,039KLOCs. For comparison, they collected the same data set of Java projects.  To evaluate on C# code, they also collected nine C# projects.

iii3. *Statistical tests* : a) Accuracy - The quality or state of being correct or precise. The simple metric to compare two algorithm results by the metric of correct results.

b) Training Time Comparison : Important to compare the training time for Machine Learning algorithms since sometimes the data availabale is limited and the algorithm which trains on lesser data is more favorable.

iii4. *Future Work* : Extend this algorithm to support scripting languages for code prediciton

**iv. Improvements**

iv1. The dataset description must be better and must be provided in the paper itself. Only two languages are chose while there are innumerable languages being used today. These results must be evaluated on non-mainstream languages also

iv2. Accuracy and training time are not the best evaluators of performance. This new environment must be used by a practical user. The user must judge if this new environment helps him code better based on the predictions the SLAMC algorithm has provided

**v. References**

v1. [n-gram model](https://en.wikipedia.org/wiki/N-gram)