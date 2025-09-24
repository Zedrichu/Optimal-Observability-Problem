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
pi11 = Real('pi11')
pi12 = Real('pi12')
pi13 = Real('pi13')
pi14 = Real('pi14')
pi15 = Real('pi15')
pi16 = Real('pi16')
pi17 = Real('pi17')
pi18 = Real('pi18')
pi19 = Real('pi19')
pi20 = Real('pi20')

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
ys91 = Real('ys91')
ys92 = Real('ys92')
ys93 = Real('ys93')
ys94 = Real('ys94')
ys101 = Real('ys101')
ys102 = Real('ys102')
ys103 = Real('ys103')
ys104 = Real('ys104')
ys111 = Real('ys111')
ys112 = Real('ys112')
ys113 = Real('ys113')
ys114 = Real('ys114')
ys121 = Real('ys121')
ys122 = Real('ys122')
ys123 = Real('ys123')
ys124 = Real('ys124')
ys131 = Real('ys131')
ys132 = Real('ys132')
ys133 = Real('ys133')
ys134 = Real('ys134')
ys141 = Real('ys141')
ys142 = Real('ys142')
ys143 = Real('ys143')
ys144 = Real('ys144')
ys151 = Real('ys151')
ys152 = Real('ys152')
ys153 = Real('ys153')
ys154 = Real('ys154')
ys161 = Real('ys161')
ys162 = Real('ys162')
ys163 = Real('ys163')
ys164 = Real('ys164')
ys171 = Real('ys171')
ys172 = Real('ys172')
ys173 = Real('ys173')
ys174 = Real('ys174')
ys181 = Real('ys181')
ys182 = Real('ys182')
ys183 = Real('ys183')
ys184 = Real('ys184')
ys201 = Real('ys201')
ys202 = Real('ys202')
ys203 = Real('ys203')
ys204 = Real('ys204')

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
pi0>=8, pi1>=7, pi2>=6, pi3>=5, pi4>=4, pi5>=5, pi6>=6, pi7>=7, pi8>=8, pi9>=9, pi10>=3, pi11>=9, pi12>=10, pi13>=2, pi14>=10, pi15>=11, pi16>=1, pi17>=11, pi18>=12, pi19>=0, pi20>=12, 
# Expected cost/reward equations
pi0 == (ys01*xo1l + ys02*xo2l + ys03*xo3l + ys04*xo4l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r + ys03*xo3r + ys04*xo4r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u + ys03*xo3u + ys04*xo4u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d + ys03*xo3d + ys04*xo4d) * (1 + pi9),
pi1 == (ys11*xo1l + ys12*xo2l + ys13*xo3l + ys14*xo4l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r + ys13*xo3r + ys14*xo4r) * (1 + pi2) + (ys11*xo1u + ys12*xo2u + ys13*xo3u + ys14*xo4u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d + ys13*xo3d + ys14*xo4d) * (1 + pi1),
pi2 == (ys21*xo1l + ys22*xo2l + ys23*xo3l + ys24*xo4l) * (1 + pi1) + (ys21*xo1r + ys22*xo2r + ys23*xo3r + ys24*xo4r) * (1 + pi3) + (ys21*xo1u + ys22*xo2u + ys23*xo3u + ys24*xo4u) * (1 + pi2) + (ys21*xo1d + ys22*xo2d + ys23*xo3d + ys24*xo4d) * (1 + pi2),
pi3 == (ys31*xo1l + ys32*xo2l + ys33*xo3l + ys34*xo4l) * (1 + pi2) + (ys31*xo1r + ys32*xo2r + ys33*xo3r + ys34*xo4r) * (1 + pi4) + (ys31*xo1u + ys32*xo2u + ys33*xo3u + ys34*xo4u) * (1 + pi3) + (ys31*xo1d + ys32*xo2d + ys33*xo3d + ys34*xo4d) * (1 + pi3),
pi4 == (ys41*xo1l + ys42*xo2l + ys43*xo3l + ys44*xo4l) * (1 + pi3) + (ys41*xo1r + ys42*xo2r + ys43*xo3r + ys44*xo4r) * (1 + pi5) + (ys41*xo1u + ys42*xo2u + ys43*xo3u + ys44*xo4u) * (1 + pi4) + (ys41*xo1d + ys42*xo2d + ys43*xo3d + ys44*xo4d) * (1 + pi10),
pi5 == (ys51*xo1l + ys52*xo2l + ys53*xo3l + ys54*xo4l) * (1 + pi4) + (ys51*xo1r + ys52*xo2r + ys53*xo3r + ys54*xo4r) * (1 + pi6) + (ys51*xo1u + ys52*xo2u + ys53*xo3u + ys54*xo4u) * (1 + pi5) + (ys51*xo1d + ys52*xo2d + ys53*xo3d + ys54*xo4d) * (1 + pi5),
pi6 == (ys61*xo1l + ys62*xo2l + ys63*xo3l + ys64*xo4l) * (1 + pi5) + (ys61*xo1r + ys62*xo2r + ys63*xo3r + ys64*xo4r) * (1 + pi7) + (ys61*xo1u + ys62*xo2u + ys63*xo3u + ys64*xo4u) * (1 + pi6) + (ys61*xo1d + ys62*xo2d + ys63*xo3d + ys64*xo4d) * (1 + pi6),
pi7 == (ys71*xo1l + ys72*xo2l + ys73*xo3l + ys74*xo4l) * (1 + pi6) + (ys71*xo1r + ys72*xo2r + ys73*xo3r + ys74*xo4r) * (1 + pi8) + (ys71*xo1u + ys72*xo2u + ys73*xo3u + ys74*xo4u) * (1 + pi7) + (ys71*xo1d + ys72*xo2d + ys73*xo3d + ys74*xo4d) * (1 + pi7),
pi8 == (ys81*xo1l + ys82*xo2l + ys83*xo3l + ys84*xo4l) * (1 + pi7) + (ys81*xo1r + ys82*xo2r + ys83*xo3r + ys84*xo4r) * (1 + pi8) + (ys81*xo1u + ys82*xo2u + ys83*xo3u + ys84*xo4u) * (1 + pi8) + (ys81*xo1d + ys82*xo2d + ys83*xo3d + ys84*xo4d) * (1 + pi11),
pi9 == (ys91*xo1l + ys92*xo2l + ys93*xo3l + ys94*xo4l) * (1 + pi9) + (ys91*xo1r + ys92*xo2r + ys93*xo3r + ys94*xo4r) * (1 + pi9) + (ys91*xo1u + ys92*xo2u + ys93*xo3u + ys94*xo4u) * (1 + pi0) + (ys91*xo1d + ys92*xo2d + ys93*xo3d + ys94*xo4d) * (1 + pi12),
pi10 == (ys101*xo1l + ys102*xo2l + ys103*xo3l + ys104*xo4l) * (1 + pi10) + (ys101*xo1r + ys102*xo2r + ys103*xo3r + ys104*xo4r) * (1 + pi10) + (ys101*xo1u + ys102*xo2u + ys103*xo3u + ys104*xo4u) * (1 + pi4) + (ys101*xo1d + ys102*xo2d + ys103*xo3d + ys104*xo4d) * (1 + pi13),
pi11 == (ys111*xo1l + ys112*xo2l + ys113*xo3l + ys114*xo4l) * (1 + pi11) + (ys111*xo1r + ys112*xo2r + ys113*xo3r + ys114*xo4r) * (1 + pi11) + (ys111*xo1u + ys112*xo2u + ys113*xo3u + ys114*xo4u) * (1 + pi8) + (ys111*xo1d + ys112*xo2d + ys113*xo3d + ys114*xo4d) * (1 + pi14),
pi12 == (ys121*xo1l + ys122*xo2l + ys123*xo3l + ys124*xo4l) * (1 + pi12) + (ys121*xo1r + ys122*xo2r + ys123*xo3r + ys124*xo4r) * (1 + pi12) + (ys121*xo1u + ys122*xo2u + ys123*xo3u + ys124*xo4u) * (1 + pi9) + (ys121*xo1d + ys122*xo2d + ys123*xo3d + ys124*xo4d) * (1 + pi15),
pi13 == (ys131*xo1l + ys132*xo2l + ys133*xo3l + ys134*xo4l) * (1 + pi13) + (ys131*xo1r + ys132*xo2r + ys133*xo3r + ys134*xo4r) * (1 + pi13) + (ys131*xo1u + ys132*xo2u + ys133*xo3u + ys134*xo4u) * (1 + pi10) + (ys131*xo1d + ys132*xo2d + ys133*xo3d + ys134*xo4d) * (1 + pi16),
pi14 == (ys141*xo1l + ys142*xo2l + ys143*xo3l + ys144*xo4l) * (1 + pi14) + (ys141*xo1r + ys142*xo2r + ys143*xo3r + ys144*xo4r) * (1 + pi14) + (ys141*xo1u + ys142*xo2u + ys143*xo3u + ys144*xo4u) * (1 + pi11) + (ys141*xo1d + ys142*xo2d + ys143*xo3d + ys144*xo4d) * (1 + pi17),
pi15 == (ys151*xo1l + ys152*xo2l + ys153*xo3l + ys154*xo4l) * (1 + pi15) + (ys151*xo1r + ys152*xo2r + ys153*xo3r + ys154*xo4r) * (1 + pi15) + (ys151*xo1u + ys152*xo2u + ys153*xo3u + ys154*xo4u) * (1 + pi12) + (ys151*xo1d + ys152*xo2d + ys153*xo3d + ys154*xo4d) * (1 + pi18),
pi16 == (ys161*xo1l + ys162*xo2l + ys163*xo3l + ys164*xo4l) * (1 + pi16) + (ys161*xo1r + ys162*xo2r + ys163*xo3r + ys164*xo4r) * (1 + pi16) + (ys161*xo1u + ys162*xo2u + ys163*xo3u + ys164*xo4u) * (1 + pi13) + (ys161*xo1d + ys162*xo2d + ys163*xo3d + ys164*xo4d) * (1 + pi19),
pi17 == (ys171*xo1l + ys172*xo2l + ys173*xo3l + ys174*xo4l) * (1 + pi17) + (ys171*xo1r + ys172*xo2r + ys173*xo3r + ys174*xo4r) * (1 + pi17) + (ys171*xo1u + ys172*xo2u + ys173*xo3u + ys174*xo4u) * (1 + pi14) + (ys171*xo1d + ys172*xo2d + ys173*xo3d + ys174*xo4d) * (1 + pi20),
pi18 == (ys181*xo1l + ys182*xo2l + ys183*xo3l + ys184*xo4l) * (1 + pi18) + (ys181*xo1r + ys182*xo2r + ys183*xo3r + ys184*xo4r) * (1 + pi18) + (ys181*xo1u + ys182*xo2u + ys183*xo3u + ys184*xo4u) * (1 + pi15) + (ys181*xo1d + ys182*xo2d + ys183*xo3d + ys184*xo4d) * (1 + pi18),
pi19 == 0, 
pi20 == (ys201*xo1l + ys202*xo2l + ys203*xo3l + ys204*xo4l) * (1 + pi20) + (ys201*xo1r + ys202*xo2r + ys203*xo3r + ys204*xo4r) * (1 + pi20) + (ys201*xo1u + ys202*xo2u + ys203*xo3u + ys204*xo4u) * (1 + pi17) + (ys201*xo1d + ys202*xo2d + ys203*xo3d + ys204*xo4d) * (1 + pi20),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= Q(146,20)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi20) * Q(1,20) <= Q(146,20),
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
Or(ys91== 0 , ys91== 1),
Or(ys92== 0 , ys92== 1),
Or(ys93== 0 , ys93== 1),
Or(ys94== 0 , ys94== 1),
Or(ys101== 0 , ys101== 1),
Or(ys102== 0 , ys102== 1),
Or(ys103== 0 , ys103== 1),
Or(ys104== 0 , ys104== 1),
Or(ys111== 0 , ys111== 1),
Or(ys112== 0 , ys112== 1),
Or(ys113== 0 , ys113== 1),
Or(ys114== 0 , ys114== 1),
Or(ys121== 0 , ys121== 1),
Or(ys122== 0 , ys122== 1),
Or(ys123== 0 , ys123== 1),
Or(ys124== 0 , ys124== 1),
Or(ys131== 0 , ys131== 1),
Or(ys132== 0 , ys132== 1),
Or(ys133== 0 , ys133== 1),
Or(ys134== 0 , ys134== 1),
Or(ys141== 0 , ys141== 1),
Or(ys142== 0 , ys142== 1),
Or(ys143== 0 , ys143== 1),
Or(ys144== 0 , ys144== 1),
Or(ys151== 0 , ys151== 1),
Or(ys152== 0 , ys152== 1),
Or(ys153== 0 , ys153== 1),
Or(ys154== 0 , ys154== 1),
Or(ys161== 0 , ys161== 1),
Or(ys162== 0 , ys162== 1),
Or(ys163== 0 , ys163== 1),
Or(ys164== 0 , ys164== 1),
Or(ys171== 0 , ys171== 1),
Or(ys172== 0 , ys172== 1),
Or(ys173== 0 , ys173== 1),
Or(ys174== 0 , ys174== 1),
Or(ys181== 0 , ys181== 1),
Or(ys182== 0 , ys182== 1),
Or(ys183== 0 , ys183== 1),
Or(ys184== 0 , ys184== 1),
Or(ys201== 0 , ys201== 1),
Or(ys202== 0 , ys202== 1),
Or(ys203== 0 , ys203== 1),
Or(ys204== 0 , ys204== 1),
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
ys91 + ys92 + ys93 + ys94 == 1,
ys101 + ys102 + ys103 + ys104 == 1,
ys111 + ys112 + ys113 + ys114 == 1,
ys121 + ys122 + ys123 + ys124 == 1,
ys131 + ys132 + ys133 + ys134 == 1,
ys141 + ys142 + ys143 + ys144 == 1,
ys151 + ys152 + ys153 + ys154 == 1,
ys161 + ys162 + ys163 + ys164 == 1,
ys171 + ys172 + ys173 + ys174 == 1,
ys181 + ys182 + ys183 + ys184 == 1,
ys201 + ys202 + ys203 + ys204 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')