from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')

# Choice of observations
y0 = Real('y0')
y1 = Real('y1')
y3 = Real('y3')
y4 = Real('y4')

# Rates of randomized strategies
xo0l = Real('xo0l')
xo0r = Real('xo0r')
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo3l = Real('xo3l')
xo3r = Real('xo3r')
xo4l = Real('xo4l')
xo4r = Real('xo4r')
xol = Real('xol')
xor = Real('xor')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=2, pi1>=1, pi2>=0, pi3>=1, pi4>=2, 
# Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + ((1 - y0)*xor + y0*xo0r) * (1 + pi1), 
pi1== ((1 - y1)*xol + y1*xo1l) * (1 + pi0) + ((1 - y1)*xor + y1*xo1r) * (1 + pi2), 
pi2 == 0, 
pi3== ((1 - y3)*xol + y3*xo3l) * (1 + pi2) + ((1 - y3)*xor + y3*xo3r) * (1 + pi4), 
pi4== ((1 - y4)*xol + y4*xo4l) * (1 + pi3) + ((1 - y4)*xor + y4*xo4r) * (1 + pi4), 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 1.5
(pi0+pi1+pi3+pi4) * Q(1,4) <= Q(3,2),
# Randomised strategies (proper probability distributions)
xo0l <= 1,
xo0l >= 0,
xo0r <= 1,
xo0r >= 0,
xo0l + xo0r == 1,
xo1l <= 1,
xo1l >= 0,
xo1r <= 1,
xo1r >= 0,
xo1l + xo1r == 1,
xo3l <= 1,
xo3l >= 0,
xo3r <= 1,
xo3r >= 0,
xo3l + xo3r == 1,
xo4l <= 1,
xo4l >= 0,
xo4r <= 1,
xo4r >= 0,
xo4l + xo4r == 1,
xol <= 1,
xol >= 0,
xor <= 1,
xor >= 0,
xol + xor == 1,
#Deterministic strategies activated
Or(xo0l == 0 , xo0l == 1),
Or(xo0r == 0 , xo0r == 1),
Or(xo1l == 0 , xo1l == 1),
Or(xo1r == 0 , xo1r == 1),
Or(xo3l == 0 , xo3l == 1),
Or(xo3r == 0 , xo3r == 1),
Or(xo4l == 0 , xo4l == 1),
Or(xo4r == 0 , xo4r == 1),
Or(xol == 0 , xol == 1),
Or(xor == 0 , xor == 1),
# y is a function that should map every state N to some observable class M
Or (y0 == 0 , y0 == 1 ),
Or (y1 == 0 , y1 == 1 ),
Or (y3 == 0 , y3 == 1 ),
Or (y4 == 0 , y4 == 1 ),
y0 + y1 + y3 + y4 == 2
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')