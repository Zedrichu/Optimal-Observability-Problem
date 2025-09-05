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
y4 = Real('y4')
y5 = Real('y5')
y6 = Real('y6')
y7 = Real('y7')

# Rates of randomized strategies
xo0l = Real('xo0l')
xo0r = Real('xo0r')
xo0u = Real('xo0u')
xo0d = Real('xo0d')
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo2u = Real('xo2u')
xo2d = Real('xo2d')
xo3l = Real('xo3l')
xo3r = Real('xo3r')
xo3u = Real('xo3u')
xo3d = Real('xo3d')
xo4l = Real('xo4l')
xo4r = Real('xo4r')
xo4u = Real('xo4u')
xo4d = Real('xo4d')
xo5l = Real('xo5l')
xo5r = Real('xo5r')
xo5u = Real('xo5u')
xo5d = Real('xo5d')
xo6l = Real('xo6l')
xo6r = Real('xo6r')
xo6u = Real('xo6u')
xo6d = Real('xo6d')
xo7l = Real('xo7l')
xo7r = Real('xo7r')
xo7u = Real('xo7u')
xo7d = Real('xo7d')
xol = Real('xol')
xor = Real('xor')
xod = Real('xod')
xou = Real('xou')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=3, pi4>=2, pi5>=1, pi6>=2, pi7>=1, pi8>=0, # Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + ((1 - y0)*xor + y0*xo0r) * (1 + pi1) + ((1 - y0)*xou + y0*xo0u) * (1 + pi0) + ((1 - y0)*xod + y0*xo0d) * (1 + pi3),
 pi1== ((1 - y1)*xol + y1*xo1l) * (1 + pi0) + ((1 - y1)*xor + y1*xo1r) * (1 + pi2) + ((1 - y1)*xou + y1*xo1u) * (1 + pi1) + ((1 - y1)*xod + y1*xo1d) * (1 + pi4),
 pi2== ((1 - y2)*xol + y2*xo2l) * (1 + pi1) + ((1 - y2)*xor + y2*xo2r) * (1 + pi3) + ((1 - y2)*xou + y2*xo2u) * (1 + pi2) + ((1 - y2)*xod + y2*xo2d) * (1 + pi5),
 pi3== ((1 - y3)*xol + y3*xo3l) * (1 + pi2) + ((1 - y3)*xor + y3*xo3r) * (1 + pi4) + ((1 - y3)*xou + y3*xo3u) * (1 + pi0) + ((1 - y3)*xod + y3*xo3d) * (1 + pi6),
 pi4== ((1 - y4)*xol + y4*xo4l) * (1 + pi3) + ((1 - y4)*xor + y4*xo4r) * (1 + pi5) + ((1 - y4)*xou + y4*xo4u) * (1 + pi1) + ((1 - y4)*xod + y4*xo4d) * (1 + pi7),
 pi5== ((1 - y5)*xol + y5*xo5l) * (1 + pi4) + ((1 - y5)*xor + y5*xo5r) * (1 + pi6) + ((1 - y5)*xou + y5*xo5u) * (1 + pi2) + ((1 - y5)*xod + y5*xo5d) * (1 + pi8),
 pi6== ((1 - y6)*xol + y6*xo6l) * (1 + pi5) + ((1 - y6)*xor + y6*xo6r) * (1 + pi7) + ((1 - y6)*xou + y6*xo6u) * (1 + pi3) + ((1 - y6)*xod + y6*xo6d) * (1 + pi6), 
pi7== ((1 - y7)*xol + y7*xo7l) * (1 + pi6) + ((1 - y7)*xor + y7*xo7r) * (1 + pi8) + ((1 - y7)*xou + y7*xo7u) * (1 + pi4) + ((1 - y7)*xod + y7*xo7d) * (1 + pi7), 
pi8 == 0, 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= Q(9,4)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7) * Q(1,8) <= Q(9,4),
# Randomised strategies (proper probability distributions)
xo0l <= 1,
xo0l >= 0,
xo0r <= 1,
xo0r >= 0,
xo0u <= 1,
xo0u >= 0,
xo0d <= 1,
xo0d >= 0,
xo0l + xo0r + xo0u + xo0d == 1,
xo1l <= 1,
xo1l >= 0,
xo1r <= 1,
xo1r >= 0,
xo1u <= 1,
xo1u >= 0,
xo1d <= 1,
xo1d >= 0,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l <= 1,
xo2l >= 0,
xo2r <= 1,
xo2r >= 0,
xo2u <= 1,
xo2u >= 0,
xo2d <= 1,
xo2d >= 0,
xo2l + xo2r + xo2u + xo2d == 1,
xo3l <= 1,
xo3l >= 0,
xo3r <= 1,
xo3r >= 0,
xo3u <= 1,
xo3u >= 0,
xo3d <= 1,
xo3d >= 0,
xo3l + xo3r + xo3u + xo3d == 1,
xo4l <= 1,
xo4l >= 0,
xo4r <= 1,
xo4r >= 0,
xo4u <= 1,
xo4u >= 0,
xo4d <= 1,
xo4d >= 0,
xo4l + xo4r + xo4u + xo4d == 1,
xo5l <= 1,
xo5l >= 0,
xo5r <= 1,
xo5r >= 0,
xo5u <= 1,
xo5u >= 0,
xo5d <= 1,
xo5d >= 0,
xo5l + xo5r + xo5u + xo5d == 1,
xo6l <= 1,
xo6l >= 0,
xo6r <= 1,
xo6r >= 0,
xo6u <= 1,
xo6u >= 0,
xo6d <= 1,
xo6d >= 0,
xo6l + xo6r + xo6u + xo6d == 1,
xo7l <= 1,
xo7l >= 0,
xo7r <= 1,
xo7r >= 0,
xo7u <= 1,
xo7u >= 0,
xo7d <= 1,
xo7d >= 0,
xo7l + xo7r + xo7u + xo7d == 1,
xol <= 1,
xol >= 0,
xor <= 1,
xor >= 0,
xou <= 1,
xou >= 0,
xod <= 1,
xod >= 0,
xol + xor + xou + xod == 1,
#Deterministic strategies activated
Or(xo0l == 0 , xo0l == 1),
Or(xo0r == 0 , xo0r == 1),
Or(xo0u == 0 , xo0u == 1),
Or(xo0d == 0 , xo0d == 1),
Or(xo1l == 0 , xo1l == 1),
Or(xo1r == 0 , xo1r == 1),
Or(xo1u == 0 , xo1u == 1),
Or(xo1d == 0 , xo1d == 1),
Or(xo2l == 0 , xo2l == 1),
Or(xo2r == 0 , xo2r == 1),
Or(xo2u == 0 , xo2u == 1),
Or(xo2d == 0 , xo2d == 1),
Or(xo3l == 0 , xo3l == 1),
Or(xo3r == 0 , xo3r == 1),
Or(xo3u == 0 , xo3u == 1),
Or(xo3d == 0 , xo3d == 1),
Or(xo4l == 0 , xo4l == 1),
Or(xo4r == 0 , xo4r == 1),
Or(xo4u == 0 , xo4u == 1),
Or(xo4d == 0 , xo4d == 1),
Or(xo5l == 0 , xo5l == 1),
Or(xo5r == 0 , xo5r == 1),
Or(xo5u == 0 , xo5u == 1),
Or(xo5d == 0 , xo5d == 1),
Or(xo6l == 0 , xo6l == 1),
Or(xo6r == 0 , xo6r == 1),
Or(xo6u == 0 , xo6u == 1),
Or(xo6d == 0 , xo6d == 1),
Or(xo7l == 0 , xo7l == 1),
Or(xo7r == 0 , xo7r == 1),
Or(xo7u == 0 , xo7u == 1),
Or(xo7d == 0 , xo7d == 1),
Or(xol == 0 , xol == 1),
Or(xor == 0 , xor == 1),
Or(xou == 0 , xou == 1),
Or(xod == 0 , xod == 1),
# y is a function that should map every state N to some observable class M
Or (y0 == 0 , y0 == 1 ),
Or (y1 == 0 , y1 == 1 ),
Or (y2 == 0 , y2 == 1 ),
Or (y3 == 0 , y3 == 1 ),
Or (y4 == 0 , y4 == 1 ),
Or (y5 == 0 , y5 == 1 ),
Or (y6 == 0 , y6 == 1 ),
Or (y7 == 0 , y7 == 1 ),
y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 == 2
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')