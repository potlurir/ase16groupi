#### 1. Paper:
Automated triaging of very large bug repositories

Sean Banerjeea, Zahid Syedb Jordan Helmickc, Mark Culpd, Kenneth Ryand, Bojan Cukic

Year - 2016

#### 2. Keywords:

ii1. *Bug tracking system* - A bug tracking system or defect tracking system is a software application that keeps track of reported software bugs in software development projects. It may be regarded as a type of issue tracking system.

ii2. *Bug report* - A software bug is an error, flaw, failure, or fault in a computer program or system that causes it to produce an incorrect or unexpected result or to behave in unintended ways. A report which explains what exaclty the bug is or how the system is broken

ii3. *Triaging bugs* - Assign degrees of urgency to bugs in bug repositories.

ii4. *Tokenization* - Is the process by which each bug report is reduced to a simpler form by removing punctuation marks and converting all uppercase characters to lowercase characters. 

**iii. Brief Notes**

iii1. *Motivational statements* : Limited research has been done in developing a fully automated triager, one that can first ascertain if a problem report is original or duplicate, and then provide a list of 20 potential matches for a duplicate report. Manual triaging of bug reports is both challenging and time consuming. The very nature of the English language entails that two people can use vastly different language to describe the same 
issue. 

iii2. *Study Instruments* - The datasets are chosen as they represent a diverse group of software applications used by a diverse group of users. For Eclipse, Firefox and Open Office we collected data until the end of 2011, June of  2012 and March of 2014 respectively. Each dataset spans over 10 years of data.

iii3. *Statistical tests* : 
						    
a) True Positive Rate (TPR) - ratio between correctly classified originals over the total number of originals

b) True Negative Rate (TNR) - ratio between correctly classified duplicates over the total number of duplicates

c) False Negative Rate (FNR) - the ratio between the number of originals classified as a duplicate divided by the total number of originals

d) False Positive Rate (FPR) - the ratio between the number of duplicates classified as an original divided by the total number of duplicates

d) ROC Curve (Receiver Operating Characteristic curve) - is a parametric curve that plots TPR versus FPR across a range of random forest (or other classifier) thresholds

All these tests are used when the training data set is skewed and contains more of True cases or contains more of False cases by a huge margin

iii4. *Future Work* : The analysis of the individual contribution. Investigate the effects of feature selection, as well as the inclusion of additional features that can assist in differentiating between originals and duplicates

**iv. Improvements**

iv1. The limitaiton of overfitting due to adding 24 similarity measures instead of one must be evaluated in the paper

iv2. Although the author himself has decided on the variability in the datasets he has used, full-proofing using further datasets is necessary

**v. References**

v1. [Bug tracking system](https://en.wikipedia.org/wiki/Bug_tracking_system)

v1. [Bug report](http://usersnap.com/blog/what-is-a-bug-report/)