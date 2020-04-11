#!/usr/bin/env python
# coding: utf-8

# #  Physics 280: A6

# ### 1. Qubit chaining for 3-SAT

# In class we described a minor-embedding procedure to
# implement 3-qubit 3-SAT (logical qubits a, b, c) with 4 physical qubits (q0, q1, q4, q5).
# The procedure assumed b = q0 = q5 so that it required q0 and q5 to be “chained” in
# the same state. We concluded that the required QUBO was:
# 
# E(q) = 1/3(q0 + q5) − 1/3(q1 + q4) + 2/3(q0q4 + q1q4 + q1q5) − (q0q5). 
# 
# Using your “classical” CPU, write down a python code that generates the energy table
# for all values of q and explain that this QUBO does indeed implement 3-SAT as the
# lowest energy state of the quantum system.
# Hint: Use the sampler ExactSolver from dimod to generate a list of all possibilities.
# 

# In[2]:


#import dwave stuff
import dimod


# In[6]:


#like normal implementation except using cpu (exactsolver) instead of qpu (the other sampler)
#use chaining to lock q0,q5 and set biases and strengths

#look at it classically, map to chimera using 4 qubits (lecture notes 'Minor Embedding')
#since b=q0=q5 do i need all 4 or just three? Doing it classically so we don't have to worry about chaining
#look at blue handwriting in notes for equation (q0=q5)

#(format it nice from notes) bias of a,c = -1/3; bias of b = 1/3
biases = {(0,0): -1/3, (1,1): -1/3, (4,4): -1/3} #, (5,5): 1/3}
#(5,0) should have a high strength (so really low number) bc they're bonded together
strengths = {(0,4): 2/3, (1,4): 2/3, (1,0): 2/3} #, (0,5): -1}

#dictionary of qubit biases and strengths
Q = dict(biases)
Q.update(strengths)

#implement on "classical" exact solver
classical_result = dimod.ExactSolver().sample_qubo(Q)
print(classical_result)


# Energy Table (all possible values of q) From Leap IDE:
# 
# () q0, q1,  q4,  energy,  num_oc.
# 
# 1:  1,  0,  0, -0.333,       1
# 
# 3:  0,  1,  0, -0.333,       1
# 
# 7:  0,  0,  1, -0.333,       1
# 
# 0:  0,  0,  0,    0.0,       1
# 
# 2:  1,  1,  0,    0.0,       1
# 
# 4:  0,  1,  1,    0.0,       1
# 
# 6:  1,  0,  1,    0.0,       1
# 
# 5:  1,  1,  1,    1.0,       1
# 
# ['BINARY', 8 rows, 8 samples, 3 variables]
# 
# From the above table, the lowest energy state of the quantum system is -0.333 when either q0, q1, or q4 equals 1, and the other two equal zero. That is, the lowest energy state corresponds to when one of the logical qubits (a,b,c) is satisfied and the other two are not. By definition, that is the solution to a 3 qubit 3-SAT problem. Therefore, this QUBO does implement 3-SAT as the lowest energy state of the quantum system. 
# 
# Furthermore, We can show this is true by manually checking all vales of z = (a,b,c) in E(z) = (a + b + c - 1) and showing that E(z)=0 if and only if z = [(0,0,1), (0,1,0), (1,0,0)]

# ## 2. 10-qubit 3-SAT

# Implement a 10-qubit 3-SAT subject to the following eight clauses:
# 
# C1(0, 1, 2), C2(1, 2, 3), C3(2, 3, 4), C4(3, 4, 5), C5(4, 5, 6), C6(5, 6, 7), C7(6, 7, 8),
# C8(7, 8, 9).
# 
# Note that ’0’, ’1’, ’2’ , ... represent binary variables, and each
# clause is satisfied (True) if only one of the three variables is 1 and the other two are 0.
# 
# (a) Run the brute force function ExactSolver to find all possible answers.
# 
# (b) Run the algorithm in the QPU. How many correct answers do you get?
# 
# Hint: Use dwavebinarycsp. Define a function sat3(a,b,c) that returns
# True when a,b,c satisfies the constraint, and add each clause using e.g.
# csp.add constraint(sat3, [’0’, ’1’, ’2’]). Apart from this, the code is quite
# similar to the map coloring code.

# In[ ]:


#import packages
import dwavebinarycsp
from dwave.system import DWaveSampler, EmbeddingComposite
import networkx as nx
import matplotlib.pyplot as plt
import dwave.inspector


# In[2]:


#build 10 qubit graph (not weighted)
logic_qubits = list(range(0,10))
#edges = ???

#create binary constraint satisfaction problem
csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)


# In[6]:


#function for add_constraint method to check variables with. returns true if constraint satisfied.
#Parameters: 3 logical qubits with value either 0 or 1.
def sat3(a,b,c):
    if a==1 and b==0 and c==0:
        return True
    elif a==0 and b==1 and c==0:
        return True
    elif a==0 and b==0 and c==1:
        return True
    else:
        return False
    
#add clauses as constraints
for i in range(8):
    csp.add_constraint(sat3, ['i', 'i+1', 'i+2'])
        
# Convert the binary constraint satisfaction problem to a binary quadratic model
bqm = dwavebinarycsp.stitch(csp)

# Set up a solver using the local system’s default D-Wave Cloud Client configuration file
# and sample 1000 times
sampler = EmbeddingComposite(dimod.ExactSolver())
sampleset = dimod.ExactSolver().sample(bqm)
print(sampleset)
#sampleset = sampler.sample(bqm)


# In[ ]:




