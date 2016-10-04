
# coding: utf-8

# # Modelling Finite State Machines.

# In this workshop we code up a small world model in python. This model is called Snowrush. The rules are as follows:
# * You start of at home with some energy "E". 
# * It is snowing outside and you go out.
# * Once outside, there are three possible scenarios.
#    * You step on snow, slip and fall down and loose some energy.
#    * You step on grass, take rest and gain some energy.
#    * You fall in a pit and die.
#    
# So can we represent this model as a state diagram?

# <img src="snowrush.png" width=700/>

# In[1]:

from __future__ import print_function, division

import pdb
import random

# TODO 1: Fill in your unity ID
__name__ = "pranjan"

def kv(d):
    """
    Pretty Print the dictionary.
    """
    return '(' + ','.join(['%s: %s'%(k, d[k]) for k in sorted(d.keys()) if k[0] != "_"]) + ')'


def shuffle(lst):
    """
    Shuffle a list and return it.
    """
    random.shuffle(lst)
    return lst

## Function to get the random value between a lower and upper bound. 
randint = random.randint

class O(object):
    """
    Basic Class which every other class inherits
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    # def __repr__(self):
    #     return self.__class__.__name__ + kv(self.__dict__)
    
print("Hello %s"%__name__)


# In[ ]:

class State(O):
    """
    State object
    """
    visit_limit = 5
    def __init__(self, name):
        """
        Initialize a state.
        @param name: Name of the state
        @return: State object with
            name: Name of the state
            out: List of transitions 
            visits: Number of times the state was visited if not declared as a loop
        """
        O.__init__(self, name=name, out=[], visits = 0)
        
    def is_stop(self):
        """
        Check if state is a stop state
        """
        return self.name[-1] == "."
    
    def is_loop(self):
        """
        Check if state is a possible loop state
        """
        return self.name[0] == "#"
    
    def arrive(self):
        """
        Move to the state if not a loop
        """
        if not self.is_loop():
            self.visits += 1
            assert self.visits <= State.visit_limit, "Loop Encountered"
            
    def next(self, record):
        """
        Move to next state from a list of possible transitions
        """
        #pdb.set_trace()
        for trans in shuffle(self.out):
            if trans.guard(record, trans):
                return trans.there
        return self
        


# In[ ]:

class Trans(O):
    # Transition Class
    def __init__(self, here, guard, there):
        """
        @param here: starting state
        @param guard: transfer function
        @param there: ending state
        """
        O.__init__(self, here = here, guard = guard, there = there)


# In[ ]:

class Machine(O):
    def __init__(self, label, data=0):
        """
        Create an instance of machine.
        @param label: Label representing the machine
        @param data: Data used to describe the machine. In case of this world model, data represents energy
        """
        O.__init__(self, label = label, # Label of the machine
                   states = {}, # Possible state of the machine
                   here = None, # Current state of the machine
                   data = data) # Data used to describe the machine
        
    def add_state(self, name):
        # TODO 2: 
        # Add a state to the machine.
        # Create an instance of state, add it to the states map. Also if 
        # the current state is None, set it to this state.
        # Also return the state
        state = State(name)
        self.states[name] = state
        self.here = state if self.here is None else self.here
        return state
        
    def add_trans(self, *trans):
        # TODO 3: For every transition in the list *trans, add the
        # transition to the "out" list in the "here" state
        for transition in trans:
            transition.here.out.append(transition)

    def step(self):
        # TODO 4: Move the machine to the next state if it is currently not in the stop state.
        if not self.here.is_stop():
            self.here = self.here.next(self)
            self.here.arrive()


# In[ ]:

class Factory(O):
    """
    Factory that generates machines.
    """
    def __init__(self):
        """
        Initialize the factory.
        """
        O.__init__(self, machines = [])
        
    def make_machine(self, label, data=0):
        # TODO 5: Create a new machine and add it to
        # the list "machines" and return the machine
        machine = Machine(label, data)
        self.machines.append(machine)
        return machine
    
    def run(self, seed=1, ticks=100):
        """
        Run all the machines
        """
        print('Seed : ', seed)
        random.seed(seed)
        for _ in xrange(ticks):
            alive = False
            for machine in shuffle(self.machines):
                if not machine.here.is_stop():
                    alive = True
                    machine.step()
                    self.report(machine.label)
                    break
            if not alive: break
                
    def report(self, name):
        """
        Report the runs
        """
        max_len = 50
        lst = [0]*(max_len + 1)
        for machine in self.machines:
            lst[machine.data] += machine.label
        show = lambda x: str(x if x else '.')
        print(name, " | ", " ".join(map(show, lst)))
    


# In[ ]:

snow_chance = 0.55
grass_chance = 0.55
pit_chance = 0.1

def snow(m, t):
    """
    Transition Function for snow
    @param m: instance of Machine
    @param t: instance of Trans 
    
    """
    # TODO 6: If chance < snow_chance, reduce the machine's energy
    # to a random integer between [1, 5] and return True. Else return False
    if random.random() < snow_chance:
        m.data -= randint(1,5)
        return True
    return False

def grass(m, t):
    """
    Transition Function for grass
    @param m: instance of Machine
    @param t: instance of Trans
    """
    # TODO 7: If chance < grass_chance, increase the machine's energy
    # to a random integer between [1, 5] and return True. Else return False
    if random.random() < grass_chance:
        m.data += random.randint(1,5)
        return True
    return False
        
def pit(m, t):
    """
    Return if chance < pit_chance.
    """
    return random.random() < pit_chance
 

def walk(m, t):
    """
    Walk from a state
    :param m: machine
    :param t: trans object
    :return:
    """
    return True


# In[ ]:

def fsm(factory, label, data):
    m = factory.make_machine(label, data)
    # TODO 8: Using the functions and classes defined above code up the
    # state machine in the figure at the top of the page.

    start = m.add_state('start')
    outside = m.add_state('#outside')
    dead = m.add_state('dead.')
    T1 = Trans(start, walk, outside)
    T2 = Trans(outside, snow, outside)
    T3 = Trans(outside, grass, outside)
    T4 = Trans(outside, pit, dead)
    m.add_trans(T1, T2, T3, T4)
    return m


# In[ ]:

f = Factory()
fsm(f, 1, 25)
fsm(f, 2, 25)
fsm(f, 4, 25)
f.run(seed=1, ticks=100)


# In[ ]:

# TODO 9 : Suggest an upgrade to the model by adding more transitions/states and check out the results
# At some low probability, lives can be added, to counteract the 'pit'

