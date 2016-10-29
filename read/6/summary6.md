#### 1. Paper:
Generating Duplicate Bug Datasets
Alina Lazar, Sarah Ritchey, Bonita Sharif

Year - 2014

#### 2. Keywords:

ii1. *Bugzilla* : Bugzilla is a web-based general-purpose bugtracker and testing tool originally developed and used by the Mozilla project, and licensed under the Mozilla Public License.

ii2. *Bug* : A software bug is an error, flaw, failure, or fault in a computer program or system that causes it to produce an incorrect or unexpected result or to behave in unintended ways

ii3.  *Bug report* - A report which explains what exaclty the bug is or how the system is broken

ii4. *Data repository* : Data repository is a somewhat general term used to refer to a destination designated for data storage. A partitioning of data, where partitioned data types are stored together. It is also commonly called data warehousing. 

**iii. Brief Notes**

iii1. *Motivational statements* : Open source software projects usually have a bug or issue tracking system associated with them. These projects have been around for more than a decade, thus the total number of bugs reported has grown significantly. Many times, the same bug is reported by different people, using different words and sometimes in different contexts. Triaging bugs is usually a manual process and time intensive in itself. Having duplicate bugs makes the problem even worse and is a waste of the triager’s time.

iii2. *Study Instruments* : The datasets presented in this paper contain bug information downloaded from the Bugzilla websites of the following open source products: Eclipse, Open Office, Mozilla and NetBeans. 

iii3. *Commentary* : First, a Scrapy script was used to download the data into mongoDB. Next, a Python script was run to perform all the cleaning steps described. Finally, another Python script generated all the groups of duplicates and saved them in a list. 
					
iii4. *Checklists* : a) Web Crawling - The web crawling Python framework Scrapy [8] was used to collect the data

b) Cleaning and Preprocessing : clean and preprocess it specifically to the problem of detecting duplicate bug reports.

c) Identifying Groups and Pairs of Bugs - First, they organized the bugs in groups. All bugs representing the same defect (bug) were included into the same group, based on their dup_id. One bug per group is designated as the master
bug and then the final results are displayed

**iv. Improvements**

iv1. Add intelligence to the algorithm by including the commit data in the evaluation parameters. This will help produce better resutls

iv2. By simple modifications this paper can also add bug severity and bug priority to its results based on the analysis done

**v. References**

v1. [Bugzilla](https://en.wikipedia.org/wiki/Bugzilla)

v1. [Data repository](https://www.techopedia.com/definition/23341/data-repository)