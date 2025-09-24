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

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys01 = Real('ys01')
ys02 = Real('ys02')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys21 = Real('ys21')
ys22 = Real('ys22')
ys31 = Real('ys31')
ys32 = Real('ys32')
ys41 = Real('ys41')
ys42 = Real('ys42')
ys51 = Real('ys51')
ys52 = Real('ys52')
ys61 = Real('ys61')
ys62 = Real('ys62')
ys71 = Real('ys71')
ys72 = Real('ys72')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo1u = Real('xo1u')
xo1d = Real('xo1d')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo2u = Real('xo2u')
xo2d = Real('xo2d')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=3, pi4>=2, pi5>=1, pi6>=2, pi7>=1, pi8>=0, 
# Expected cost/reward equations
pi0 == (ys01*xo1l + ys02*xo2l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d) * (1 + pi3),
pi1 == (ys11*xo1l + ys12*xo2l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r) * (1 + pi2) + (ys11*xo1u + ys12*xo2u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d) * (1 + pi4),
pi2 == (ys21*xo1l + ys22*xo2l) * (1 + pi1) + (ys21*xo1r + ys22*xo2r) * (1 + pi2) + (ys21*xo1u + ys22*xo2u) * (1 + pi2) + (ys21*xo1d + ys22*xo2d) * (1 + pi5),
pi3 == (ys31*xo1l + ys32*xo2l) * (1 + pi3) + (ys31*xo1r + ys32*xo2r) * (1 + pi4) + (ys31*xo1u + ys32*xo2u) * (1 + pi0) + (ys31*xo1d + ys32*xo2d) * (1 + pi6),
pi4 == (ys41*xo1l + ys42*xo2l) * (1 + pi3) + (ys41*xo1r + ys42*xo2r) * (1 + pi5) + (ys41*xo1u + ys42*xo2u) * (1 + pi1) + (ys41*xo1d + ys42*xo2d) * (1 + pi7),
pi5 == (ys51*xo1l + ys52*xo2l) * (1 + pi4) + (ys51*xo1r + ys52*xo2r) * (1 + pi5) + (ys51*xo1u + ys52*xo2u) * (1 + pi2) + (ys51*xo1d + ys52*xo2d) * (1 + pi8),
pi6 == (ys61*xo1l + ys62*xo2l) * (1 + pi6) + (ys61*xo1r + ys62*xo2r) * (1 + pi7) + (ys61*xo1u + ys62*xo2u) * (1 + pi3) + (ys61*xo1d + ys62*xo2d) * (1 + pi6),
pi7 == (ys71*xo1l + ys72*xo2l) * (1 + pi6) + (ys71*xo1r + ys72*xo2r) * (1 + pi8) + (ys71*xo1u + ys72*xo2u) * (1 + pi4) + (ys71*xo1d + ys72*xo2d) * (1 + pi7),
pi8 == 0, 
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= Q(9,4)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7) * Q(1,8) <= Q(9,4),
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo1u>= 0,
xo1u<= 1,
xo1d>= 0,
xo1d<= 1,
xo2l>= 0,
xo2l<= 1,
xo2r>= 0,
xo2r<= 1,
xo2u>= 0,
xo2u<= 1,
xo2d>= 0,
xo2d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l + xo2r + xo2u + xo2d == 1,
# Deterministic Strategies activated
Or(xo1l == 0, xo1l == 1),
Or(xo1r == 0, xo1r == 1),
Or(xo1u == 0, xo1u == 1),
Or(xo1d == 0, xo1d == 1),
Or(xo2l == 0, xo2l == 1),
Or(xo2r == 0, xo2r == 1),
Or(xo2u == 0, xo2u == 1),
Or(xo2d == 0, xo2d == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys21== 0 , ys21== 1),
Or(ys22== 0 , ys22== 1),
Or(ys31== 0 , ys31== 1),
Or(ys32== 0 , ys32== 1),
Or(ys41== 0 , ys41== 1),
Or(ys42== 0 , ys42== 1),
Or(ys51== 0 , ys51== 1),
Or(ys52== 0 , ys52== 1),
Or(ys61== 0 , ys61== 1),
Or(ys62== 0 , ys62== 1),
Or(ys71== 0 , ys71== 1),
Or(ys72== 0 , ys72== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 == 1,
ys11 + ys12 == 1,
ys21 + ys22 == 1,
ys31 + ys32 == 1,
ys41 + ys42 == 1,
ys51 + ys52 == 1,
ys61 + ys62 == 1,
ys71 + ys72 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')