from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')
pi5 = Real('pi5')
pi6 = Real('pi6')
pi7 = Real('pi7')
pi8 = Real('pi8')

# Choice of observations
y0 = Real('y0')
y1 = Real('y1')
y2 = Real('y2')
y3 = Real('y3')
y5 = Real('y5')
y6 = Real('y6')
y7 = Real('y7')
y8 = Real('y8')

# Rates of randomized strategies
xo0l = Real('xo0l')
xo0r = Real('xo0r')
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo3l = Real('xo3l')
xo3r = Real('xo3r')
xo5l = Real('xo5l')
xo5r = Real('xo5r')
xo6l = Real('xo6l')
xo6r = Real('xo6r')
xo7l = Real('xo7l')
xo7r = Real('xo7r')
xo8l = Real('xo8l')
xo8r = Real('xo8r')
xol = Real('xol')
xor = Real('xor')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=1, pi4>=0, pi5>=1, pi6>=2, pi7>=3, pi8>=4, 
# Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + ((1 - y0)*xor + y0*xo0r) * (1 + pi1), 
pi1== ((1 - y1)*xol + y1*xo1l) * (1 + pi0) + ((1 - y1)*xor + y1*xo1r) * (1 + pi2), 
pi2== ((1 - y2)*xol + y2*xo2l) * (1 + pi1) + ((1 - y2)*xor + y2*xo2r) * (1 + pi3), 
pi3== ((1 - y3)*xol + y3*xo3l) * (1 + pi2) + ((1 - y3)*xor + y3*xo3r) * (1 + pi4), 
pi4 == 0, 
pi5== ((1 - y5)*xol + y5*xo5l) * (1 + pi4) + ((1 - y5)*xor + y5*xo5r) * (1 + pi6), 
pi6== ((1 - y6)*xol + y6*xo6l) * (1 + pi5) + ((1 - y6)*xor + y6*xo6r) * (1 + pi7), 
pi7== ((1 - y7)*xol + y7*xo7l) * (1 + pi6) + ((1 - y7)*xor + y7*xo7r) * (1 + pi8), 
pi8== ((1 - y8)*xol + y8*xo8l) * (1 + pi7) + ((1 - y8)*xor + y8*xo8r) * (1 + pi8), 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 2.5
(pi0+pi1+pi2+pi3+pi5+pi6+pi7+pi8) * Q(1,8) <= Q(5,2),
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
xo2l <= 1,
xo2l >= 0,
xo2r <= 1,
xo2r >= 0,
xo2l + xo2r == 1,
xo3l <= 1,
xo3l >= 0,
xo3r <= 1,
xo3r >= 0,
xo3l + xo3r == 1,
xo5l <= 1,
xo5l >= 0,
xo5r <= 1,
xo5r >= 0,
xo5l + xo5r == 1,
xo6l <= 1,
xo6l >= 0,
xo6r <= 1,
xo6r >= 0,
xo6l + xo6r == 1,
xo7l <= 1,
xo7l >= 0,
xo7r <= 1,
xo7r >= 0,
xo7l + xo7r == 1,
xo8l <= 1,
xo8l >= 0,
xo8r <= 1,
xo8r >= 0,
xo8l + xo8r == 1,
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
Or(xo2l == 0 , xo2l == 1),
Or(xo2r == 0 , xo2r == 1),
Or(xo3l == 0 , xo3l == 1),
Or(xo3r == 0 , xo3r == 1),
Or(xo5l == 0 , xo5l == 1),
Or(xo5r == 0 , xo5r == 1),
Or(xo6l == 0 , xo6l == 1),
Or(xo6r == 0 , xo6r == 1),
Or(xo7l == 0 , xo7l == 1),
Or(xo7r == 0 , xo7r == 1),
Or(xo8l == 0 , xo8l == 1),
Or(xo8r == 0 , xo8r == 1),
Or(xol == 0 , xol == 1),
Or(xor == 0 , xor == 1),
# y is a function that should map every state N to some observable class M
Or (y0 == 0 , y0 == 1 ),
Or (y1 == 0 , y1 == 1 ),
Or (y2 == 0 , y2 == 1 ),
Or (y3 == 0 , y3 == 1 ),
Or (y5 == 0 , y5 == 1 ),
Or (y6 == 0 , y6 == 1 ),
Or (y7 == 0 , y7 == 1 ),
Or (y8 == 0 , y8 == 1 ),
y0 + y1 + y2 + y3 + y5 + y6 + y7 + y8 == 4
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')