#!/usr/bin/env python
# coding: utf-8

# #  Physics 280: A6

# # 1. Qubit chaining for 3-SAT

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


# In[ ]:




