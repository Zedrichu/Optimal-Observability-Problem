from z3 import *

# Expected cost/reward of reaching the goal.
pi0 = Real('pi0')
pi1 = Real('pi1')
pi2 = Real('pi2')
pi3 = Real('pi3')
pi4 = Real('pi4')
pi5 = Real('pi5')
pi6 = Real('pi6')
pis = Real('pis')

# Choice of observations
y0 = Real('y0')
y1 = Real('y1')
y2 = Real('y2')
y4 = Real('y4')
y5 = Real('y5')
y6 = Real('y6')

# Rates of randomized strategies
xo0l = Real('xo0l')
xo0r = Real('xo0r')
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo4l = Real('xo4l')
xo4r = Real('xo4r')
xo5l = Real('xo5l')
xo5r = Real('xo5r')
xo6l = Real('xo6l')
xo6r = Real('xo6r')
xol = Real('xol')
xor = Real('xor')
e = Real('e')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=6, pi1>=4, pi2>=2, pi3>=0, pi4>=2, pi5>=4, pi6>=6, 
# Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + Q(1,2)*((1 - y0)*xor + y0*xo0r) * (1 + pi1) + Q(1,2)*((1 - y0)*xor + y0*xo0r) * (1 + pis), 
pi1== Q(1,2)*((1 - y1)*xol + y1*xo1l) * (1 + pi0) + Q(1,2)*((1 - y1)*xol + y1*xo1l) * (1 + pis) + Q(1,2)*((1 - y1)*xor + y1*xo1r) * (1 + pi2) + Q(1,2)*((1 - y1)*xor + y1*xo1r) * (1 + pis), 
pi2== Q(1,2)*((1 - y2)*xol + y2*xo2l) * (1 + pi1) + Q(1,2)*((1 - y2)*xol + y2*xo2l) * (1 + pis) + Q(1,2)*((1 - y2)*xor + y2*xo2r) * (1 + pi3) + Q(1,2)*((1 - y2)*xor + y2*xo2r) * (1 + pis), 
pi3 == 0, 
pi4== Q(1,2)*((1 - y4)*xol + y4*xo4l) * (1 + pi3) + Q(1,2)*((1 - y4)*xol + y4*xo4l) * (1 + pis) + Q(1,2)*((1 - y4)*xor + y4*xo4r) * (1 + pi5) + Q(1,2)*((1 - y4)*xor + y4*xo4r) * (1 + pis), 
pi5== Q(1,2)*((1 - y5)*xol + y5*xo5l) * (1 + pi4) + Q(1,2)*((1 - y5)*xol + y5*xo5l) * (1 + pis) + Q(1,2)*((1 - y5)*xor + y5*xo5r) * (1 + pi6) + Q(1,2)*((1 - y5)*xor + y5*xo5r) * (1 + pis), 
pi6== Q(1,2)*((1 - y6)*xol + y6*xo6l) * (1 + pi5) + Q(1,2)*((1 - y6)*xol + y6*xo6l) * (1 + pis) + ((1 - y6)*xor + y6*xo6r) * (1 + pi6), 
pis == (pis + 1),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold 4.0
(pi0+pi1+pi2+pi4+pi5+pi6) * Q(1,6) <= 4.0,
#e == (pi0+pi1+pi2+pi4+pi5+pi6) * Q(1,6),
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
xo4l <= 1,
xo4l >= 0,
xo4r <= 1,
xo4r >= 0,
xo4l + xo4r == 1,
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
xol <= 1,
xol >= 0,
xor <= 1,
xor >= 0,
xol + xor == 1,
# y is a function that should map every state N to some observable class M
Or (y0 == 0 , y0 == 1 ),
Or (y1 == 0 , y1 == 1 ),
Or (y2 == 0 , y2 == 1 ),
Or (y4 == 0 , y4 == 1 ),
Or (y5 == 0 , y5 == 1 ),
Or (y6 == 0 , y6 == 1 ),
y0 + y1 + y2 + y4 + y5 + y6 == 3
)
if solver.check() == sat:
    m = solver.model()
    print(solver)
    print('This is a solution:')
    print(m)
elif solver.check() == unsat:
    print('No solution!!!')
else:
    print('Unknown')
