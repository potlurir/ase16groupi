# Implementing and Analyzing the  Integrated Project Model Defect Flow Chain 

## Team Members 
* ### Raghavendra Prasad Potluri (rpotlur@ncsu.edu)
* ### Akshay Kumar Chaluvadi (achaluv@ncsu.edu) 
* ### Pritesh Ranjan (pranjan@ncsu.edu)


## Date: December 07, 2016



## Abstract 

Ant Colony Optimization (ACO) has been successfully employed to tackle a variety of hard combinatorial optimization problems, including the traveling salesman problem, vehicle routing, sequential ordering and timetabling. ACO, as a swarm intelligence framework, mimics the indirect communication strategy employed by real ants mediated by pheromone trails. Among the several algorithms following the ACO general framework, the Ant Colony System (ACS) has obtained convincing results in a range of problems. In Software Engineering, the effective application of ACO has been very narrow, being restricted to a few sparse problems. The goal is to show the results are better for ACO than D.E, by adapting the ACS algorithm to solve the well-known Software Release Planning problem in the presence of dependent requirements. The evaluation of the proposed approach is performed over randomly generated datasets and considered, besides ACO, the Genetic Algorithm and Differential Evolution. But the results we obtained are better for D.E.

## Introduction 

The Search Based Software Engineering (SBSE) field has been benefiting from a number of general search methods, including, but not limited to, Genetic Algorithms, Simulated Annealing, Greedy Search, GRASP and Tabu Search. Surprisingly, even with the large applicability and the significant results obtained by the Ant Colony Optimization (ACO) metaheuristic, very little has been done regarding the employment of this strategy to tackle software engineering problems modeled as optimization problems.

## Background and Related Work 

In this section we provide background information and prior academic work related to our project. 
### Background 
 

### Related Work 
  


## Assumptions 


## Implementation 


### Implementation of Ant Colony Optimizer


### Implementing DE 


### Integrating DE with Spread and IGD


## Methodology 



## Results


### Sample Run of Ant Colony Optimizer 


### Improvement by DE 
  
 
## Threats to Validity

We discuss the limitations of our study as following: 

* Use of synthetic values for the used auxiliaries 
* We did not consider all auxiliaries that are part of a bigger model 
* We did not consider the complete model 
* The equations used for auxiliaries are generated from regression using a sample of values that are less than 10 in size. 
* We ran the integrated model for 365 days that is equivalent to one year. In real world software projects tend to vary in duration usually in months, or years. 
* The base of our assumption that connects the top and bottom part of the model is based on the notations of Abdel-Hamid and Madnick’s book. We have not thoroughly verified this assumption.  
* In our project we considered only one differential algorithm that is DE. We did not include other genetic algorithms such as GALE, max walk sat or NSGA II.   
 
## Future Work 
We leave the following actions as scope for future work: 

* Future work can consider all auxiliaries in the model   
* Future work can implement the complete model that includes all the sectors of interest  
* Future work can verify the equations used for auxiliaries _MultiplierWorkforce_, _FractionEscapingErrors_, _MultiplierToRegeneration_, _MultiplierSchedulePressure_, and _ActiveErrorsRetiringFractions_ for real world values. 
* Future work can run the complete model, and the optimizer for real world software project duration and contextual factors. 
* Future work can perform analysis of the complete model and compare the findings with that of Madachy’s implementation available on Internet [6]. 
* Future work can include other genetic algorithms such as simulated annealing, max walk sat or NSGA II.

## Conclusion


## Acknowledgement 

We earnestly thank course instructor Dr. Tim Menzies, and teaching assistant George Mathew for giving us valuable advice in implementing the project.

## References 


