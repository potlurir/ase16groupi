# Homework6: coding homework: Generic Experiments

## What to Hand in

From the following, show the output of running sa, mws on Schaffer, Osyczka2, Kursawe.

### To Do

Rewrite your SA and MWS code such that you can run the following loop:
```
for model in [Schaffer, Osyczka2, Kursawe]:
    for optimizer in [sa, mws]:
           optimizer(model())
```
This is the generic experiment loop that allows for rapid extension to handle more models and more optimizers.

## Solutions
Code [main.py](https://github.com/rpotluri12/ase16groupi/blob/master/code/6/main.py) Note: it requires tabulate python package


Summary result: 

![alt tag](https://github.com/rpotluri12/ase16groupi/blob/master/code/6/Screenshots/summaryResult.JPG)
