#!/usr/bin/env python
# coding: utf-8

# # Qubit chaining for 3-SAT

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

# In[1]:


print("hello!")


# In[ ]:

<<<<<<< HEAD
print("heehee")
=======
>>>>>>> 5db8f7756f728eb2a07cd9e8c9831fb5be7df60f



