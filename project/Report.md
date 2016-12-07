# An Ant Colony Optimization Approach to the Software Release Planning. 

## Team Members 
* ### Raghavendra Prasad Potluri (rpotlur@ncsu.edu)
* ### Akshay Kumar Chaluvadi (achaluv@ncsu.edu) 
* ### Pritesh Ranjan (pranjan@ncsu.edu)


## Date: December 07, 2016



## Abstract 

Ant Colony Optimization (ACO) has been successfully employed to tackle a variety of hard combinatorial optimization problems, including the traveling salesman problem, vehicle routing, sequential ordering and timetabling. ACO, as a swarm intelligence framework, mimics the indirect communication strategy employed by real ants mediated by pheromone trails. Among the several algorithms following the ACO general framework, the Ant Colony System (ACS) has obtained convincing results in a range of problems. In Software Engineering, the effective application of ACO has been very narrow, being restricted to a few sparse problems. The goal is to show the results are better for ACO than D.E, by adapting the ACS algorithm to solve the well-known Software Next Release Planning problem in the presence of dependent requirements. The evaluation of the proposed approach is performed over randomly generated datasets and considered, besides ACO, the Genetic Algorithm and Differential Evolution. However, the results we obtained are better for D.E.

## Introduction 

The Search Based Software Engineering (SBSE) field has been benefiting from a number of general search methods, including, but not limited to, Genetic Algorithms, Simulated Annealing, Greedy Search, GRASP and Tabu Search. Surprisingly, even with the large applicability and the significant results obtained by the Ant Colony Optimization (ACO) metaheuristic, very little has been done regarding the employment of this strategy to tackle software engineering problems modeled as optimization problems. Ant System (AS) was the first algorithm to follow the ACO general framework. First applied to tackle small instances of the Traveling Salesman Problem (TSP), AS was not able to compete with state-of-the-art algorithms specifically designed for this traditional optimization problem, which stimulated the development of significant extensions to this algorithm. In particular, the Ant Colony System (ACS) algorithm improved AS by incorporating an elitist strategy to update pheromone trails and by changing the rule used by ants to select the next movement. These enhancements considerably increased the ability of the algorithm to generate precise solutions to hard and different combinatorial problems, including the TSP, vehicle routing, sequential ordering and timetabling.

## Background and Related Work 

In this section we provide background information. 
### Background 
## The Next Release problem

Given a software package, there is a set, C, of m customers whose requirements have to be considered in the development of the next release of this system. There is also a set, R, of n requirements to complete. In order to meet each requirement it is needed to expend a certain amount of resources, which can be transformed into an economical cost: the cost of satisfying the requirement. Additionally, different clients have different interests in the implementation of each requirement. The first component of the objective function expresses the weighted overall satisfaction of the stakeholders. The other component deals with risk management, expressing those requirements with higher risk should be implemented earlier. Finally, the two restrictions will, respectively, limit the implementation cost of requirements in each release and guarantee that the precedence among requirements will be respected.

     

### Related Work 

An ACO-based algorithm for error tracing and model checking is designed and implemented in [8]. In [9], the ACOhg metaheuristic, an ACO algorithm proposed to deal with large construction graphs, is combined with partial order reduction to reduce memory consumption. This combination is employed to find safety property violations in concurrent models

## Assumptions 

* We assume that more than one customer can be concerned with any requirement, and that all the requirements are not equally important for all the customers.
* We assume that atmost 20% of dependency between projects.

## Implementation 


### Implementation of Ant Colony Optimizer


### Implementing DE 


### Integrating DE with Spread and IGD


## Methodology 



## Results


### Sample Run of Ant Colony Optimizer 


### Improvement by DE 
  
 
## Threats to Validity

## Conclusion


## Acknowledgement 

We earnestly thank course instructor Dr. Tim Menzies, and teaching assistant George Mathew for giving us valuable advice in implementing the project.

## References 


