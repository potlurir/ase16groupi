#### 1. Paper:
H. U. Asuncion, A. U. Asuncion, and R. N. Taylor. Software traceability
with topic modeling. In ICSE 10, pages 95-104. ACM Press, 2010.

#### 2. Keywords:

*2.1. Automated Software Traceability* : The goal of automatically discovering relationships between software artifacts (e.g. requirement documents, design documents, code, bug reports, test cases) to facilitate efficient retrieval of relevant information.

*2.2. Topic Modeling*: A popular Machine Learning technique for automatically inferring semantic topics from a text corpus.

*2.3. Retrospective traceability*: Artifact relationships are inferred from a static set of artifacts that have been generated in the past. Information Retrieval techniques are good at retrospective traceability.

*2.4. Prospective traceability*: This method generates trace links as soon as the artifacts are created and modified during the development process.

#### 3. Brief Notes:

*3.1. Motivational Statements*: s Managing the relationships that exist between different software artifacts is a challenge for software developers. Automating this process is a non-trivial task and the authors propose a model that allows for the semantic categorization of artifacts and the topical visualization of a software system.

*3.2. Related Work*: Earlier approaches to Topic Modeling have employed Latent Dirichlet Allocation(LDA) to generate models. These works have focused retrospective traceability using software artifacts including source codes, while the authors focus mainly on prospective traceability using on text-based artifacts such as requirements/design documents; but not source codes.

*3.3. Baseline Results*: 

The existing retrospective techniques provide the following features:
    - Generates candidate links based on textual similarity.
    - Generates links across several heterogenous artifacts.
    - Detects topics from artifacts automatically.
    
The existing prospective traceability provides the following features:
    - Generates links based on user interaction.
    - Adds links in an online, incremental fashion.
    
*3.4. New Results*:

The solution provided by the authors provide all the above features in addition to the following:
    - Generates links across several heterogenous artifacts.
    - Uses fully probabilistic interpretation of semantic topics.
    - Visualizes semantic topics on the architectural mashup.

Furthermore, the following results have been reported by the authors:
    - As the number of software artifacts increases, a higher quality model is learned.
    - There is a linear time increase in computation time as the number of artifacts increases.
    - LDA performs better than LSI on the EasyCLinic data set, in terms of precision-recall.

#### 4. Scope of Improvement:

4.1. As suggested, the topics can be provided at finer levels of granularity to minimize the number of components to examine.

4.2. The representation of topics should be made clearer because similar high-probability words appeared in more than one topic.

