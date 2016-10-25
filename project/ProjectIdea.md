## Solving ‘Vehicle Routing Problem’ with Metaheuristic Algorithms.

### Vehicle Routing Problem :
The main goal of solving this problem is to answer this question: **"What is the optimal set of routes for a fleet of vehicles to traverse in order to deliver to a given set of customers?"**

A typical vehicle routing problem (VRP) aims to find a set of tours for several vehicles from a depot to a lot of customers and return to the depot without exceeding the capacity constraints of each vehicle at minimum cost. Since the customer combination is not restricted to the selection of vehicle routes, VRP is considered as a combinatorial optimization problem where the number of feasible solutions for the problem increases exponentially with the number of customers increasing.(Bell and McMullen, 2004). [1] 

We plan to add the following restrictions on the VRP problem:
    * Limited Capacity: The vehicles have limited carrying capacity of the goods that must be delivered.
    * Multiple Trips: The vehicles can do more than one route.
    * Time windows: The delivery locations have time windows within which the deliveries (or visits) must be made.
    
Some of the objective function that we plan to optimize are:

    * Minimize the global transportation cost based on the global distance travelled as well as the fixed costs associated with the used vehicles and drivers.
    * Minimize the number of vehicles needed to serve all customers.
    * Least variation in travel time and vehicle load.
    * Minimize penalties for low quality service.

Various heuristic algorithms have been used to solve VRPs. For this project, we plan to solve VRP by using Ant Colony Optimization (ACO) and Simulated Annealing (SA) and comment on the performance and results of the two algorithms. 
    
References: 

 [1] Yu Bin, Yang Zhong-Zhen, Yao Baozhen. 2008. An improved ant colony optimization for vehicle routing problem. European Journal of Operational Research 196 (2009) 171–176
 
 [2] Dorigo, M., Maniezzo, V., Colorni, A., 1996. Ant system: optimization by a colony of cooperating agents. IEEE Transactions on Systems, Mans, and Cybernetics 1 (26), 29–41.
 
 [3] Koulamas, C., Antony, S., Jaen, R., 1994. A survey of simulated annealing applications to operations research problems. Omega 22 (1), 41–56.