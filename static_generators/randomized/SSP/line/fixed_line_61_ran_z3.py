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
pi21 = Real('pi21')
pi22 = Real('pi22')
pi23 = Real('pi23')
pi24 = Real('pi24')
pi25 = Real('pi25')
pi26 = Real('pi26')
pi27 = Real('pi27')
pi28 = Real('pi28')
pi29 = Real('pi29')
pi30 = Real('pi30')
pi31 = Real('pi31')
pi32 = Real('pi32')
pi33 = Real('pi33')
pi34 = Real('pi34')
pi35 = Real('pi35')
pi36 = Real('pi36')
pi37 = Real('pi37')
pi38 = Real('pi38')
pi39 = Real('pi39')
pi40 = Real('pi40')
pi41 = Real('pi41')
pi42 = Real('pi42')
pi43 = Real('pi43')
pi44 = Real('pi44')
pi45 = Real('pi45')
pi46 = Real('pi46')
pi47 = Real('pi47')
pi48 = Real('pi48')
pi49 = Real('pi49')
pi50 = Real('pi50')
pi51 = Real('pi51')
pi52 = Real('pi52')
pi53 = Real('pi53')
pi54 = Real('pi54')
pi55 = Real('pi55')
pi56 = Real('pi56')
pi57 = Real('pi57')
pi58 = Real('pi58')
pi59 = Real('pi59')
pi60 = Real('pi60')

# Choice of observations
y0 = Real('y0')
y1 = Real('y1')
y2 = Real('y2')
y3 = Real('y3')
y4 = Real('y4')
y5 = Real('y5')
y6 = Real('y6')
y7 = Real('y7')
y8 = Real('y8')
y9 = Real('y9')
y10 = Real('y10')
y11 = Real('y11')
y12 = Real('y12')
y13 = Real('y13')
y14 = Real('y14')
y15 = Real('y15')
y16 = Real('y16')
y17 = Real('y17')
y18 = Real('y18')
y19 = Real('y19')
y20 = Real('y20')
y21 = Real('y21')
y22 = Real('y22')
y23 = Real('y23')
y24 = Real('y24')
y25 = Real('y25')
y26 = Real('y26')
y27 = Real('y27')
y28 = Real('y28')
y29 = Real('y29')
y31 = Real('y31')
y32 = Real('y32')
y33 = Real('y33')
y34 = Real('y34')
y35 = Real('y35')
y36 = Real('y36')
y37 = Real('y37')
y38 = Real('y38')
y39 = Real('y39')
y40 = Real('y40')
y41 = Real('y41')
y42 = Real('y42')
y43 = Real('y43')
y44 = Real('y44')
y45 = Real('y45')
y46 = Real('y46')
y47 = Real('y47')
y48 = Real('y48')
y49 = Real('y49')
y50 = Real('y50')
y51 = Real('y51')
y52 = Real('y52')
y53 = Real('y53')
y54 = Real('y54')
y55 = Real('y55')
y56 = Real('y56')
y57 = Real('y57')
y58 = Real('y58')
y59 = Real('y59')
y60 = Real('y60')

# Rates of randomized strategies
xo0l = Real('xo0l')
xo0r = Real('xo0r')
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
xo3l = Real('xo3l')
xo3r = Real('xo3r')
xo4l = Real('xo4l')
xo4r = Real('xo4r')
xo5l = Real('xo5l')
xo5r = Real('xo5r')
xo6l = Real('xo6l')
xo6r = Real('xo6r')
xo7l = Real('xo7l')
xo7r = Real('xo7r')
xo8l = Real('xo8l')
xo8r = Real('xo8r')
xo9l = Real('xo9l')
xo9r = Real('xo9r')
xo10l = Real('xo10l')
xo10r = Real('xo10r')
xo11l = Real('xo11l')
xo11r = Real('xo11r')
xo12l = Real('xo12l')
xo12r = Real('xo12r')
xo13l = Real('xo13l')
xo13r = Real('xo13r')
xo14l = Real('xo14l')
xo14r = Real('xo14r')
xo15l = Real('xo15l')
xo15r = Real('xo15r')
xo16l = Real('xo16l')
xo16r = Real('xo16r')
xo17l = Real('xo17l')
xo17r = Real('xo17r')
xo18l = Real('xo18l')
xo18r = Real('xo18r')
xo19l = Real('xo19l')
xo19r = Real('xo19r')
xo20l = Real('xo20l')
xo20r = Real('xo20r')
xo21l = Real('xo21l')
xo21r = Real('xo21r')
xo22l = Real('xo22l')
xo22r = Real('xo22r')
xo23l = Real('xo23l')
xo23r = Real('xo23r')
xo24l = Real('xo24l')
xo24r = Real('xo24r')
xo25l = Real('xo25l')
xo25r = Real('xo25r')
xo26l = Real('xo26l')
xo26r = Real('xo26r')
xo27l = Real('xo27l')
xo27r = Real('xo27r')
xo28l = Real('xo28l')
xo28r = Real('xo28r')
xo29l = Real('xo29l')
xo29r = Real('xo29r')
xo31l = Real('xo31l')
xo31r = Real('xo31r')
xo32l = Real('xo32l')
xo32r = Real('xo32r')
xo33l = Real('xo33l')
xo33r = Real('xo33r')
xo34l = Real('xo34l')
xo34r = Real('xo34r')
xo35l = Real('xo35l')
xo35r = Real('xo35r')
xo36l = Real('xo36l')
xo36r = Real('xo36r')
xo37l = Real('xo37l')
xo37r = Real('xo37r')
xo38l = Real('xo38l')
xo38r = Real('xo38r')
xo39l = Real('xo39l')
xo39r = Real('xo39r')
xo40l = Real('xo40l')
xo40r = Real('xo40r')
xo41l = Real('xo41l')
xo41r = Real('xo41r')
xo42l = Real('xo42l')
xo42r = Real('xo42r')
xo43l = Real('xo43l')
xo43r = Real('xo43r')
xo44l = Real('xo44l')
xo44r = Real('xo44r')
xo45l = Real('xo45l')
xo45r = Real('xo45r')
xo46l = Real('xo46l')
xo46r = Real('xo46r')
xo47l = Real('xo47l')
xo47r = Real('xo47r')
xo48l = Real('xo48l')
xo48r = Real('xo48r')
xo49l = Real('xo49l')
xo49r = Real('xo49r')
xo50l = Real('xo50l')
xo50r = Real('xo50r')
xo51l = Real('xo51l')
xo51r = Real('xo51r')
xo52l = Real('xo52l')
xo52r = Real('xo52r')
xo53l = Real('xo53l')
xo53r = Real('xo53r')
xo54l = Real('xo54l')
xo54r = Real('xo54r')
xo55l = Real('xo55l')
xo55r = Real('xo55r')
xo56l = Real('xo56l')
xo56r = Real('xo56r')
xo57l = Real('xo57l')
xo57r = Real('xo57r')
xo58l = Real('xo58l')
xo58r = Real('xo58r')
xo59l = Real('xo59l')
xo59r = Real('xo59r')
xo60l = Real('xo60l')
xo60r = Real('xo60r')
xol = Real('xol')
xor = Real('xor')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=30, pi1>=29, pi2>=28, pi3>=27, pi4>=26, pi5>=25, pi6>=24, pi7>=23, pi8>=22, pi9>=21, pi10>=20, pi11>=19, pi12>=18, pi13>=17, pi14>=16, pi15>=15, pi16>=14, pi17>=13, pi18>=12, pi19>=11, pi20>=10, pi21>=9, pi22>=8, pi23>=7, pi24>=6, pi25>=5, pi26>=4, pi27>=3, pi28>=2, pi29>=1, pi30>=0, pi31>=1, pi32>=2, pi33>=3, pi34>=4, pi35>=5, pi36>=6, pi37>=7, pi38>=8, pi39>=9, pi40>=10, pi41>=11, pi42>=12, pi43>=13, pi44>=14, pi45>=15, pi46>=16, pi47>=17, pi48>=18, pi49>=19, pi50>=20, pi51>=21, pi52>=22, pi53>=23, pi54>=24, pi55>=25, pi56>=26, pi57>=27, pi58>=28, pi59>=29, pi60>=30, 
# Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + ((1 - y0)*xor + y0*xo0r) * (1 + pi1), 
pi1== ((1 - y1)*xol + y1*xo1l) * (1 + pi0) + ((1 - y1)*xor + y1*xo1r) * (1 + pi2), 
pi2== ((1 - y2)*xol + y2*xo2l) * (1 + pi1) + ((1 - y2)*xor + y2*xo2r) * (1 + pi3), 
pi3== ((1 - y3)*xol + y3*xo3l) * (1 + pi2) + ((1 - y3)*xor + y3*xo3r) * (1 + pi4), 
pi4== ((1 - y4)*xol + y4*xo4l) * (1 + pi3) + ((1 - y4)*xor + y4*xo4r) * (1 + pi5), 
pi5== ((1 - y5)*xol + y5*xo5l) * (1 + pi4) + ((1 - y5)*xor + y5*xo5r) * (1 + pi6), 
pi6== ((1 - y6)*xol + y6*xo6l) * (1 + pi5) + ((1 - y6)*xor + y6*xo6r) * (1 + pi7), 
pi7== ((1 - y7)*xol + y7*xo7l) * (1 + pi6) + ((1 - y7)*xor + y7*xo7r) * (1 + pi8), 
pi8== ((1 - y8)*xol + y8*xo8l) * (1 + pi7) + ((1 - y8)*xor + y8*xo8r) * (1 + pi9), 
pi9== ((1 - y9)*xol + y9*xo9l) * (1 + pi8) + ((1 - y9)*xor + y9*xo9r) * (1 + pi10), 
pi10== ((1 - y10)*xol + y10*xo10l) * (1 + pi9) + ((1 - y10)*xor + y10*xo10r) * (1 + pi11), 
pi11== ((1 - y11)*xol + y11*xo11l) * (1 + pi10) + ((1 - y11)*xor + y11*xo11r) * (1 + pi12), 
pi12== ((1 - y12)*xol + y12*xo12l) * (1 + pi11) + ((1 - y12)*xor + y12*xo12r) * (1 + pi13), 
pi13== ((1 - y13)*xol + y13*xo13l) * (1 + pi12) + ((1 - y13)*xor + y13*xo13r) * (1 + pi14), 
pi14== ((1 - y14)*xol + y14*xo14l) * (1 + pi13) + ((1 - y14)*xor + y14*xo14r) * (1 + pi15), 
pi15== ((1 - y15)*xol + y15*xo15l) * (1 + pi14) + ((1 - y15)*xor + y15*xo15r) * (1 + pi16), 
pi16== ((1 - y16)*xol + y16*xo16l) * (1 + pi15) + ((1 - y16)*xor + y16*xo16r) * (1 + pi17), 
pi17== ((1 - y17)*xol + y17*xo17l) * (1 + pi16) + ((1 - y17)*xor + y17*xo17r) * (1 + pi18), 
pi18== ((1 - y18)*xol + y18*xo18l) * (1 + pi17) + ((1 - y18)*xor + y18*xo18r) * (1 + pi19), 
pi19== ((1 - y19)*xol + y19*xo19l) * (1 + pi18) + ((1 - y19)*xor + y19*xo19r) * (1 + pi20), 
pi20== ((1 - y20)*xol + y20*xo20l) * (1 + pi19) + ((1 - y20)*xor + y20*xo20r) * (1 + pi21), 
pi21== ((1 - y21)*xol + y21*xo21l) * (1 + pi20) + ((1 - y21)*xor + y21*xo21r) * (1 + pi22), 
pi22== ((1 - y22)*xol + y22*xo22l) * (1 + pi21) + ((1 - y22)*xor + y22*xo22r) * (1 + pi23), 
pi23== ((1 - y23)*xol + y23*xo23l) * (1 + pi22) + ((1 - y23)*xor + y23*xo23r) * (1 + pi24), 
pi24== ((1 - y24)*xol + y24*xo24l) * (1 + pi23) + ((1 - y24)*xor + y24*xo24r) * (1 + pi25), 
pi25== ((1 - y25)*xol + y25*xo25l) * (1 + pi24) + ((1 - y25)*xor + y25*xo25r) * (1 + pi26), 
pi26== ((1 - y26)*xol + y26*xo26l) * (1 + pi25) + ((1 - y26)*xor + y26*xo26r) * (1 + pi27), 
pi27== ((1 - y27)*xol + y27*xo27l) * (1 + pi26) + ((1 - y27)*xor + y27*xo27r) * (1 + pi28), 
pi28== ((1 - y28)*xol + y28*xo28l) * (1 + pi27) + ((1 - y28)*xor + y28*xo28r) * (1 + pi29), 
pi29== ((1 - y29)*xol + y29*xo29l) * (1 + pi28) + ((1 - y29)*xor + y29*xo29r) * (1 + pi30), 
pi30 == 0, 
pi31== ((1 - y31)*xol + y31*xo31l) * (1 + pi30) + ((1 - y31)*xor + y31*xo31r) * (1 + pi32), 
pi32== ((1 - y32)*xol + y32*xo32l) * (1 + pi31) + ((1 - y32)*xor + y32*xo32r) * (1 + pi33), 
pi33== ((1 - y33)*xol + y33*xo33l) * (1 + pi32) + ((1 - y33)*xor + y33*xo33r) * (1 + pi34), 
pi34== ((1 - y34)*xol + y34*xo34l) * (1 + pi33) + ((1 - y34)*xor + y34*xo34r) * (1 + pi35), 
pi35== ((1 - y35)*xol + y35*xo35l) * (1 + pi34) + ((1 - y35)*xor + y35*xo35r) * (1 + pi36), 
pi36== ((1 - y36)*xol + y36*xo36l) * (1 + pi35) + ((1 - y36)*xor + y36*xo36r) * (1 + pi37), 
pi37== ((1 - y37)*xol + y37*xo37l) * (1 + pi36) + ((1 - y37)*xor + y37*xo37r) * (1 + pi38), 
pi38== ((1 - y38)*xol + y38*xo38l) * (1 + pi37) + ((1 - y38)*xor + y38*xo38r) * (1 + pi39), 
pi39== ((1 - y39)*xol + y39*xo39l) * (1 + pi38) + ((1 - y39)*xor + y39*xo39r) * (1 + pi40), 
pi40== ((1 - y40)*xol + y40*xo40l) * (1 + pi39) + ((1 - y40)*xor + y40*xo40r) * (1 + pi41), 
pi41== ((1 - y41)*xol + y41*xo41l) * (1 + pi40) + ((1 - y41)*xor + y41*xo41r) * (1 + pi42), 
pi42== ((1 - y42)*xol + y42*xo42l) * (1 + pi41) + ((1 - y42)*xor + y42*xo42r) * (1 + pi43), 
pi43== ((1 - y43)*xol + y43*xo43l) * (1 + pi42) + ((1 - y43)*xor + y43*xo43r) * (1 + pi44), 
pi44== ((1 - y44)*xol + y44*xo44l) * (1 + pi43) + ((1 - y44)*xor + y44*xo44r) * (1 + pi45), 
pi45== ((1 - y45)*xol + y45*xo45l) * (1 + pi44) + ((1 - y45)*xor + y45*xo45r) * (1 + pi46), 
pi46== ((1 - y46)*xol + y46*xo46l) * (1 + pi45) + ((1 - y46)*xor + y46*xo46r) * (1 + pi47), 
pi47== ((1 - y47)*xol + y47*xo47l) * (1 + pi46) + ((1 - y47)*xor + y47*xo47r) * (1 + pi48), 
pi48== ((1 - y48)*xol + y48*xo48l) * (1 + pi47) + ((1 - y48)*xor + y48*xo48r) * (1 + pi49), 
pi49== ((1 - y49)*xol + y49*xo49l) * (1 + pi48) + ((1 - y49)*xor + y49*xo49r) * (1 + pi50), 
pi50== ((1 - y50)*xol + y50*xo50l) * (1 + pi49) + ((1 - y50)*xor + y50*xo50r) * (1 + pi51), 
pi51== ((1 - y51)*xol + y51*xo51l) * (1 + pi50) + ((1 - y51)*xor + y51*xo51r) * (1 + pi52), 
pi52== ((1 - y52)*xol + y52*xo52l) * (1 + pi51) + ((1 - y52)*xor + y52*xo52r) * (1 + pi53), 
pi53== ((1 - y53)*xol + y53*xo53l) * (1 + pi52) + ((1 - y53)*xor + y53*xo53r) * (1 + pi54), 
pi54== ((1 - y54)*xol + y54*xo54l) * (1 + pi53) + ((1 - y54)*xor + y54*xo54r) * (1 + pi55), 
pi55== ((1 - y55)*xol + y55*xo55l) * (1 + pi54) + ((1 - y55)*xor + y55*xo55r) * (1 + pi56), 
pi56== ((1 - y56)*xol + y56*xo56l) * (1 + pi55) + ((1 - y56)*xor + y56*xo56r) * (1 + pi57), 
pi57== ((1 - y57)*xol + y57*xo57l) * (1 + pi56) + ((1 - y57)*xor + y57*xo57r) * (1 + pi58), 
pi58== ((1 - y58)*xol + y58*xo58l) * (1 + pi57) + ((1 - y58)*xor + y58*xo58r) * (1 + pi59), 
pi59== ((1 - y59)*xol + y59*xo59l) * (1 + pi58) + ((1 - y59)*xor + y59*xo59r) * (1 + pi60), 
pi60== ((1 - y60)*xol + y60*xo60l) * (1 + pi59) + ((1 - y60)*xor + y60*xo60r) * (1 + pi60), 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= Q(31,2)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60) * Q(1,60) <= Q(31,2),
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
xo9l <= 1,
xo9l >= 0,
xo9r <= 1,
xo9r >= 0,
xo9l + xo9r == 1,
xo10l <= 1,
xo10l >= 0,
xo10r <= 1,
xo10r >= 0,
xo10l + xo10r == 1,
xo11l <= 1,
xo11l >= 0,
xo11r <= 1,
xo11r >= 0,
xo11l + xo11r == 1,
xo12l <= 1,
xo12l >= 0,
xo12r <= 1,
xo12r >= 0,
xo12l + xo12r == 1,
xo13l <= 1,
xo13l >= 0,
xo13r <= 1,
xo13r >= 0,
xo13l + xo13r == 1,
xo14l <= 1,
xo14l >= 0,
xo14r <= 1,
xo14r >= 0,
xo14l + xo14r == 1,
xo15l <= 1,
xo15l >= 0,
xo15r <= 1,
xo15r >= 0,
xo15l + xo15r == 1,
xo16l <= 1,
xo16l >= 0,
xo16r <= 1,
xo16r >= 0,
xo16l + xo16r == 1,
xo17l <= 1,
xo17l >= 0,
xo17r <= 1,
xo17r >= 0,
xo17l + xo17r == 1,
xo18l <= 1,
xo18l >= 0,
xo18r <= 1,
xo18r >= 0,
xo18l + xo18r == 1,
xo19l <= 1,
xo19l >= 0,
xo19r <= 1,
xo19r >= 0,
xo19l + xo19r == 1,
xo20l <= 1,
xo20l >= 0,
xo20r <= 1,
xo20r >= 0,
xo20l + xo20r == 1,
xo21l <= 1,
xo21l >= 0,
xo21r <= 1,
xo21r >= 0,
xo21l + xo21r == 1,
xo22l <= 1,
xo22l >= 0,
xo22r <= 1,
xo22r >= 0,
xo22l + xo22r == 1,
xo23l <= 1,
xo23l >= 0,
xo23r <= 1,
xo23r >= 0,
xo23l + xo23r == 1,
xo24l <= 1,
xo24l >= 0,
xo24r <= 1,
xo24r >= 0,
xo24l + xo24r == 1,
xo25l <= 1,
xo25l >= 0,
xo25r <= 1,
xo25r >= 0,
xo25l + xo25r == 1,
xo26l <= 1,
xo26l >= 0,
xo26r <= 1,
xo26r >= 0,
xo26l + xo26r == 1,
xo27l <= 1,
xo27l >= 0,
xo27r <= 1,
xo27r >= 0,
xo27l + xo27r == 1,
xo28l <= 1,
xo28l >= 0,
xo28r <= 1,
xo28r >= 0,
xo28l + xo28r == 1,
xo29l <= 1,
xo29l >= 0,
xo29r <= 1,
xo29r >= 0,
xo29l + xo29r == 1,
xo31l <= 1,
xo31l >= 0,
xo31r <= 1,
xo31r >= 0,
xo31l + xo31r == 1,
xo32l <= 1,
xo32l >= 0,
xo32r <= 1,
xo32r >= 0,
xo32l + xo32r == 1,
xo33l <= 1,
xo33l >= 0,
xo33r <= 1,
xo33r >= 0,
xo33l + xo33r == 1,
xo34l <= 1,
xo34l >= 0,
xo34r <= 1,
xo34r >= 0,
xo34l + xo34r == 1,
xo35l <= 1,
xo35l >= 0,
xo35r <= 1,
xo35r >= 0,
xo35l + xo35r == 1,
xo36l <= 1,
xo36l >= 0,
xo36r <= 1,
xo36r >= 0,
xo36l + xo36r == 1,
xo37l <= 1,
xo37l >= 0,
xo37r <= 1,
xo37r >= 0,
xo37l + xo37r == 1,
xo38l <= 1,
xo38l >= 0,
xo38r <= 1,
xo38r >= 0,
xo38l + xo38r == 1,
xo39l <= 1,
xo39l >= 0,
xo39r <= 1,
xo39r >= 0,
xo39l + xo39r == 1,
xo40l <= 1,
xo40l >= 0,
xo40r <= 1,
xo40r >= 0,
xo40l + xo40r == 1,
xo41l <= 1,
xo41l >= 0,
xo41r <= 1,
xo41r >= 0,
xo41l + xo41r == 1,
xo42l <= 1,
xo42l >= 0,
xo42r <= 1,
xo42r >= 0,
xo42l + xo42r == 1,
xo43l <= 1,
xo43l >= 0,
xo43r <= 1,
xo43r >= 0,
xo43l + xo43r == 1,
xo44l <= 1,
xo44l >= 0,
xo44r <= 1,
xo44r >= 0,
xo44l + xo44r == 1,
xo45l <= 1,
xo45l >= 0,
xo45r <= 1,
xo45r >= 0,
xo45l + xo45r == 1,
xo46l <= 1,
xo46l >= 0,
xo46r <= 1,
xo46r >= 0,
xo46l + xo46r == 1,
xo47l <= 1,
xo47l >= 0,
xo47r <= 1,
xo47r >= 0,
xo47l + xo47r == 1,
xo48l <= 1,
xo48l >= 0,
xo48r <= 1,
xo48r >= 0,
xo48l + xo48r == 1,
xo49l <= 1,
xo49l >= 0,
xo49r <= 1,
xo49r >= 0,
xo49l + xo49r == 1,
xo50l <= 1,
xo50l >= 0,
xo50r <= 1,
xo50r >= 0,
xo50l + xo50r == 1,
xo51l <= 1,
xo51l >= 0,
xo51r <= 1,
xo51r >= 0,
xo51l + xo51r == 1,
xo52l <= 1,
xo52l >= 0,
xo52r <= 1,
xo52r >= 0,
xo52l + xo52r == 1,
xo53l <= 1,
xo53l >= 0,
xo53r <= 1,
xo53r >= 0,
xo53l + xo53r == 1,
xo54l <= 1,
xo54l >= 0,
xo54r <= 1,
xo54r >= 0,
xo54l + xo54r == 1,
xo55l <= 1,
xo55l >= 0,
xo55r <= 1,
xo55r >= 0,
xo55l + xo55r == 1,
xo56l <= 1,
xo56l >= 0,
xo56r <= 1,
xo56r >= 0,
xo56l + xo56r == 1,
xo57l <= 1,
xo57l >= 0,
xo57r <= 1,
xo57r >= 0,
xo57l + xo57r == 1,
xo58l <= 1,
xo58l >= 0,
xo58r <= 1,
xo58r >= 0,
xo58l + xo58r == 1,
xo59l <= 1,
xo59l >= 0,
xo59r <= 1,
xo59r >= 0,
xo59l + xo59r == 1,
xo60l <= 1,
xo60l >= 0,
xo60r <= 1,
xo60r >= 0,
xo60l + xo60r == 1,
xol <= 1,
xol >= 0,
xor <= 1,
xor >= 0,
xol + xor == 1,
# y is a function that should map every state N to some observable class M
Or (y0 == 0 , y0 == 1 ),
Or (y1 == 0 , y1 == 1 ),
Or (y2 == 0 , y2 == 1 ),
Or (y3 == 0 , y3 == 1 ),
Or (y4 == 0 , y4 == 1 ),
Or (y5 == 0 , y5 == 1 ),
Or (y6 == 0 , y6 == 1 ),
Or (y7 == 0 , y7 == 1 ),
Or (y8 == 0 , y8 == 1 ),
Or (y9 == 0 , y9 == 1 ),
Or (y10 == 0 , y10 == 1 ),
Or (y11 == 0 , y11 == 1 ),
Or (y12 == 0 , y12 == 1 ),
Or (y13 == 0 , y13 == 1 ),
Or (y14 == 0 , y14 == 1 ),
Or (y15 == 0 , y15 == 1 ),
Or (y16 == 0 , y16 == 1 ),
Or (y17 == 0 , y17 == 1 ),
Or (y18 == 0 , y18 == 1 ),
Or (y19 == 0 , y19 == 1 ),
Or (y20 == 0 , y20 == 1 ),
Or (y21 == 0 , y21 == 1 ),
Or (y22 == 0 , y22 == 1 ),
Or (y23 == 0 , y23 == 1 ),
Or (y24 == 0 , y24 == 1 ),
Or (y25 == 0 , y25 == 1 ),
Or (y26 == 0 , y26 == 1 ),
Or (y27 == 0 , y27 == 1 ),
Or (y28 == 0 , y28 == 1 ),
Or (y29 == 0 , y29 == 1 ),
Or (y31 == 0 , y31 == 1 ),
Or (y32 == 0 , y32 == 1 ),
Or (y33 == 0 , y33 == 1 ),
Or (y34 == 0 , y34 == 1 ),
Or (y35 == 0 , y35 == 1 ),
Or (y36 == 0 , y36 == 1 ),
Or (y37 == 0 , y37 == 1 ),
Or (y38 == 0 , y38 == 1 ),
Or (y39 == 0 , y39 == 1 ),
Or (y40 == 0 , y40 == 1 ),
Or (y41 == 0 , y41 == 1 ),
Or (y42 == 0 , y42 == 1 ),
Or (y43 == 0 , y43 == 1 ),
Or (y44 == 0 , y44 == 1 ),
Or (y45 == 0 , y45 == 1 ),
Or (y46 == 0 , y46 == 1 ),
Or (y47 == 0 , y47 == 1 ),
Or (y48 == 0 , y48 == 1 ),
Or (y49 == 0 , y49 == 1 ),
Or (y50 == 0 , y50 == 1 ),
Or (y51 == 0 , y51 == 1 ),
Or (y52 == 0 , y52 == 1 ),
Or (y53 == 0 , y53 == 1 ),
Or (y54 == 0 , y54 == 1 ),
Or (y55 == 0 , y55 == 1 ),
Or (y56 == 0 , y56 == 1 ),
Or (y57 == 0 , y57 == 1 ),
Or (y58 == 0 , y58 == 1 ),
Or (y59 == 0 , y59 == 1 ),
Or (y60 == 0 , y60 == 1 ),
y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 + y40 + y41 + y42 + y43 + y44 + y45 + y46 + y47 + y48 + y49 + y50 + y51 + y52 + y53 + y54 + y55 + y56 + y57 + y58 + y59 + y60 == 30
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')