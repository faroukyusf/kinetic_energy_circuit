#!/usr/bin/env python
# coding: utf-8

# In[5]:


import matplotlib.pyplot as plt
import numpy as np
from math import pi
from qiskit import *
from qiskit import QuantumCircuit,execute,Aer,IBMQ
from qiskit import IBMQ, Aer, transpile, assemble,execute
from qiskit import ClassicalRegister, QuantumRegister
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.compiler import transpile,assemble


# ##=================== KE function ===================##
# 
# For 3 qubits [q0, q1, q2], we first use q0 & q1 simulantously to undergo the kinetic circuit. 
# 
# Then, we use q1 & q2. The pattern goes on for bigger systems.
# 
# Typically,
# 
# 1) q0 is a control for X and q1 is a traget
# 
# 2) Rz(- pi /2) on q0
# 
# 3) q1 is a control for X and q0 is a traget
# 
# 4) Ry(- hopping angle) on q0
# 
# 5) q1 is a control for X and q0 is a traget
# 
# 6) Ry(+ hopping angle) on q0
# 
# 7) Rz(+ pi/2) on q0
# 
# 8) q0 is a control for X and q1 is a traget
# 
# 
# This makes sense because the kinetic term is just hopping from one location to the next.
# So, in general for n qubits, we will connect the i-th qubit with the i-th + 1 qubit..
# 
# It would be function of qc, hopping angle (hopping parameter h*dt), and the number of qubits.

# In[6]:


def Kinetic_Eenergy(qc, hopping_angle, num_qubits):
    for i in range(num_qubits - 1):
        qc.cx(i, i + 1)
        qc.rz(-np.pi/2.0, i)
        qc.cx(i + 1, i)
        qc.ry(-hopping_angle, i)
        qc.cx(i + 1, i)
        qc.ry(hopping_angle, i)
        qc.rz(np.pi/2.0, i)
        qc.cx(i, i + 1)

    
psi = QuantumCircuit(3)
Kinetic_Eenergy(psi, 0.002, 3)
psi.draw(output="mpl")


# In[ ]:




