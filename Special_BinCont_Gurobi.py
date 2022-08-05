import pyomo.environ as pyo, numpy as np
from pyomo.environ import *
from pyomo.opt import SolverFactory

#creation of the model and variables
model = pyo.ConcreteModel()
model.C = pyo.Var(range(1,4))
model.n = pyo.Var(range(1,4), within=Integers, bounds=(0,1000))
model.b = pyo.Var(within=Binary)
C = model.C
n = model.n
b = model.b

#objective function
model.obj = pyo.Objective(expr = pyo.summation(C))

#constraint
model.total = pyo.Constraint(expr = pyo.summation(n) == 2100)
model.C1 = pyo.Constraint(expr = C[1] == 2*n[1])
model.C2 = pyo.Constraint(expr = C[2] == b*(6*n[2]+1000))
model.C2n = pyo.Constraint(expr = n[2] <= b*1000)
model.C3 = pyo.Constraint(expr = C[3] == 7*n[3])

#solve
opt = SolverFactory('gurobi')
opt.solve(model)

#print
print('n1', pyo.value(n[1]))
print('n2', pyo.value(n[2]))
print('n3', pyo.value(n[3]))
print('nTotal', pyo.value(pyo.summation(n)))

print('C1', pyo.value(C[1]))
print('C2', pyo.value(C[2]))
print('C3', pyo.value(C[3]))
print('CTotal', pyo.value(pyo.summation(C)))

