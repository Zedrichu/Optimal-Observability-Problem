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
pi9 = Real('pi9')
pi10 = Real('pi10')

# Choice of observations (e.g. ys01 = 1 means that in state 0, observable 1 is observed)
ys01 = Real('ys01')
ys02 = Real('ys02')
ys03 = Real('ys03')
ys04 = Real('ys04')
ys11 = Real('ys11')
ys12 = Real('ys12')
ys13 = Real('ys13')
ys14 = Real('ys14')
ys21 = Real('ys21')
ys22 = Real('ys22')
ys23 = Real('ys23')
ys24 = Real('ys24')
ys31 = Real('ys31')
ys32 = Real('ys32')
ys33 = Real('ys33')
ys34 = Real('ys34')
ys41 = Real('ys41')
ys42 = Real('ys42')
ys43 = Real('ys43')
ys44 = Real('ys44')
ys51 = Real('ys51')
ys52 = Real('ys52')
ys53 = Real('ys53')
ys54 = Real('ys54')
ys61 = Real('ys61')
ys62 = Real('ys62')
ys63 = Real('ys63')
ys64 = Real('ys64')
ys71 = Real('ys71')
ys72 = Real('ys72')
ys73 = Real('ys73')
ys74 = Real('ys74')
ys81 = Real('ys81')
ys82 = Real('ys82')
ys83 = Real('ys83')
ys84 = Real('ys84')
ys101 = Real('ys101')
ys102 = Real('ys102')
ys103 = Real('ys103')
ys104 = Real('ys104')

# Rates of randomized strategies
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
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=4, pi1>=3, pi2>=2, pi3>=3, pi4>=4, pi5>=5, pi6>=1, pi7>=5, pi8>=6, pi9>=0, pi10>=6, 
# Expected cost/reward equations
pi0 == (ys01*xo1l + ys02*xo2l + ys03*xo3l + ys04*xo4l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r + ys03*xo3r + ys04*xo4r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u + ys03*xo3u + ys04*xo4u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d + ys03*xo3d + ys04*xo4d) * (1 + pi5),
pi1 == (ys11*xo1l + ys12*xo2l + ys13*xo3l + ys14*xo4l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r + ys13*xo3r + ys14*xo4r) * (1 + pi2) + (ys11*xo1u + ys12*xo2u + ys13*xo3u + ys14*xo4u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d + ys13*xo3d + ys14*xo4d) * (1 + pi1),
pi2 == (ys21*xo1l + ys22*xo2l + ys23*xo3l + ys24*xo4l) * (1 + pi1) + (ys21*xo1r + ys22*xo2r + ys23*xo3r + ys24*xo4r) * (1 + pi3) + (ys21*xo1u + ys22*xo2u + ys23*xo3u + ys24*xo4u) * (1 + pi2) + (ys21*xo1d + ys22*xo2d + ys23*xo3d + ys24*xo4d) * (1 + pi6),
pi3 == (ys31*xo1l + ys32*xo2l + ys33*xo3l + ys34*xo4l) * (1 + pi2) + (ys31*xo1r + ys32*xo2r + ys33*xo3r + ys34*xo4r) * (1 + pi4) + (ys31*xo1u + ys32*xo2u + ys33*xo3u + ys34*xo4u) * (1 + pi3) + (ys31*xo1d + ys32*xo2d + ys33*xo3d + ys34*xo4d) * (1 + pi3),
pi4 == (ys41*xo1l + ys42*xo2l + ys43*xo3l + ys44*xo4l) * (1 + pi3) + (ys41*xo1r + ys42*xo2r + ys43*xo3r + ys44*xo4r) * (1 + pi4) + (ys41*xo1u + ys42*xo2u + ys43*xo3u + ys44*xo4u) * (1 + pi4) + (ys41*xo1d + ys42*xo2d + ys43*xo3d + ys44*xo4d) * (1 + pi7),
pi5 == (ys51*xo1l + ys52*xo2l + ys53*xo3l + ys54*xo4l) * (1 + pi5) + (ys51*xo1r + ys52*xo2r + ys53*xo3r + ys54*xo4r) * (1 + pi5) + (ys51*xo1u + ys52*xo2u + ys53*xo3u + ys54*xo4u) * (1 + pi0) + (ys51*xo1d + ys52*xo2d + ys53*xo3d + ys54*xo4d) * (1 + pi8),
pi6 == (ys61*xo1l + ys62*xo2l + ys63*xo3l + ys64*xo4l) * (1 + pi6) + (ys61*xo1r + ys62*xo2r + ys63*xo3r + ys64*xo4r) * (1 + pi6) + (ys61*xo1u + ys62*xo2u + ys63*xo3u + ys64*xo4u) * (1 + pi2) + (ys61*xo1d + ys62*xo2d + ys63*xo3d + ys64*xo4d) * (1 + pi9),
pi7 == (ys71*xo1l + ys72*xo2l + ys73*xo3l + ys74*xo4l) * (1 + pi7) + (ys71*xo1r + ys72*xo2r + ys73*xo3r + ys74*xo4r) * (1 + pi7) + (ys71*xo1u + ys72*xo2u + ys73*xo3u + ys74*xo4u) * (1 + pi4) + (ys71*xo1d + ys72*xo2d + ys73*xo3d + ys74*xo4d) * (1 + pi10),
pi8 == (ys81*xo1l + ys82*xo2l + ys83*xo3l + ys84*xo4l) * (1 + pi8) + (ys81*xo1r + ys82*xo2r + ys83*xo3r + ys84*xo4r) * (1 + pi8) + (ys81*xo1u + ys82*xo2u + ys83*xo3u + ys84*xo4u) * (1 + pi5) + (ys81*xo1d + ys82*xo2d + ys83*xo3d + ys84*xo4d) * (1 + pi8),
pi9 == 0, 
pi10 == (ys101*xo1l + ys102*xo2l + ys103*xo3l + ys104*xo4l) * (1 + pi10) + (ys101*xo1r + ys102*xo2r + ys103*xo3r + ys104*xo4r) * (1 + pi10) + (ys101*xo1u + ys102*xo2u + ys103*xo3u + ys104*xo4u) * (1 + pi7) + (ys101*xo1d + ys102*xo2d + ys103*xo3d + ys104*xo4d) * (1 + pi10),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= Q(39,10)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi10) * Q(1,10) <= Q(39,10),
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
xo3l>= 0,
xo3l<= 1,
xo3r>= 0,
xo3r<= 1,
xo3u>= 0,
xo3u<= 1,
xo3d>= 0,
xo3d<= 1,
xo4l>= 0,
xo4l<= 1,
xo4r>= 0,
xo4r<= 1,
xo4u>= 0,
xo4u<= 1,
xo4d>= 0,
xo4d<= 1,
xo1l + xo1r + xo1u + xo1d == 1,
xo2l + xo2r + xo2u + xo2d == 1,
xo3l + xo3r + xo3u + xo3d == 1,
xo4l + xo4r + xo4u + xo4d == 1,
# Deterministic Strategies activated
Or(xo1l == 0, xo1l == 1),
Or(xo1r == 0, xo1r == 1),
Or(xo1u == 0, xo1u == 1),
Or(xo1d == 0, xo1d == 1),
Or(xo2l == 0, xo2l == 1),
Or(xo2r == 0, xo2r == 1),
Or(xo2u == 0, xo2u == 1),
Or(xo2d == 0, xo2d == 1),
Or(xo3l == 0, xo3l == 1),
Or(xo3r == 0, xo3r == 1),
Or(xo3u == 0, xo3u == 1),
Or(xo3d == 0, xo3d == 1),
Or(xo4l == 0, xo4l == 1),
Or(xo4r == 0, xo4r == 1),
Or(xo4u == 0, xo4u == 1),
Or(xo4d == 0, xo4d == 1),
# ysNM is a function that should map every state N to some observable class M
Or(ys01== 0 , ys01== 1),
Or(ys02== 0 , ys02== 1),
Or(ys03== 0 , ys03== 1),
Or(ys04== 0 , ys04== 1),
Or(ys11== 0 , ys11== 1),
Or(ys12== 0 , ys12== 1),
Or(ys13== 0 , ys13== 1),
Or(ys14== 0 , ys14== 1),
Or(ys21== 0 , ys21== 1),
Or(ys22== 0 , ys22== 1),
Or(ys23== 0 , ys23== 1),
Or(ys24== 0 , ys24== 1),
Or(ys31== 0 , ys31== 1),
Or(ys32== 0 , ys32== 1),
Or(ys33== 0 , ys33== 1),
Or(ys34== 0 , ys34== 1),
Or(ys41== 0 , ys41== 1),
Or(ys42== 0 , ys42== 1),
Or(ys43== 0 , ys43== 1),
Or(ys44== 0 , ys44== 1),
Or(ys51== 0 , ys51== 1),
Or(ys52== 0 , ys52== 1),
Or(ys53== 0 , ys53== 1),
Or(ys54== 0 , ys54== 1),
Or(ys61== 0 , ys61== 1),
Or(ys62== 0 , ys62== 1),
Or(ys63== 0 , ys63== 1),
Or(ys64== 0 , ys64== 1),
Or(ys71== 0 , ys71== 1),
Or(ys72== 0 , ys72== 1),
Or(ys73== 0 , ys73== 1),
Or(ys74== 0 , ys74== 1),
Or(ys81== 0 , ys81== 1),
Or(ys82== 0 , ys82== 1),
Or(ys83== 0 , ys83== 1),
Or(ys84== 0 , ys84== 1),
Or(ys101== 0 , ys101== 1),
Or(ys102== 0 , ys102== 1),
Or(ys103== 0 , ys103== 1),
Or(ys104== 0 , ys104== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 + ys03 + ys04 == 1,
ys11 + ys12 + ys13 + ys14 == 1,
ys21 + ys22 + ys23 + ys24 == 1,
ys31 + ys32 + ys33 + ys34 == 1,
ys41 + ys42 + ys43 + ys44 == 1,
ys51 + ys52 + ys53 + ys54 == 1,
ys61 + ys62 + ys63 + ys64 == 1,
ys71 + ys72 + ys73 + ys74 == 1,
ys81 + ys82 + ys83 + ys84 == 1,
ys101 + ys102 + ys103 + ys104 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')