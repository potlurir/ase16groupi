**i. Paper**

A Topic-based Approach for Narrowing the Search Space of Buggy Files from a Bug Report - 2011
Anh Tuan Nguyen, Tung Thanh Nguyen, Jafar Al-Kofahi, Hung Viet Nguyen, Tien N. Nguyen

**ii. Keywords**

ii1. *Latent Dirichlet Allocation(LDA)* : Latent Dirichlet allocation (LDA) is a generative statistical model that allows sets of observations to be explained by unobserved groups that explain why some parts of the data are similar

ii2. *Bug report* : A bug report consists of details which explain how exaclty the code is broken or what is the bug exactly. It contains the information needed to reproduce and fix bugs

ii3. *S-component* : An LDA model which is generated based on a source file. The source file contains comments and identifiers which contribute to the words of the topics generated

ii4. *B-component* : An LDA model which is generated based on a bug report. The bug report consists of the technical description of the bug which helps identify the topic of the bug

**iii. Brief Notes**

iii1. *Motivational statements* : Locating bugs in source code based on bug reports is a time-consuming task, which prompts the requirement of an automated approach to help developers narrow the search space of source code files

iii2. *Baseline results* : The results of the BugScout tool desgined in the paper are as following :-
	
	I) The tool can recommend candidate buggy file correctly 33% of the cases 	with one single file 
	
	II) The tool can recommend candidate buggy file correctly 45% of the cases 	with a ranked list of 10 files

iii3. *Related work* : Bug localization using latent dirichlet allocation(S. K. Lukins, N. A. Kraft, and L. H. Etzkorn). This paper describes a method where the source files are indexed based on the topics detected from LDA. If a new bug report is filed, a textual query is formed from the report and a search via Vector space model is performed among the indexed source files. 

BugScout does not do any indexing and directly correlates the topics in source files and bug reports to find the buggy files

iii4. *Study instruments* : Datasets were collected from Jazz(an IBM development framework), Eclipse(an IDE), AspectJ(a compitler) and ArgoUML(a graphical editor). Each dataset consists of bug reports, source code files and the mapping between bug reports and source code files. In the case of Jazz, the developers recorded the fixed files and in other cases most of the mappings are found through change logs

**iv. Improvements**

iv1. Recently modified files have a higher probability of having bugs which can be included in ranking the files to predict buggy files
iv2. Depending on who the assignee for the bug is there is a possibility to better predict which file contains the bug based on which topic that assignee has developeds

**v. References**

v1. [Wikipedia for LDA](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation)

v2. [Bug report](http://usersnap.com/blog/what-is-a-bug-report/)

