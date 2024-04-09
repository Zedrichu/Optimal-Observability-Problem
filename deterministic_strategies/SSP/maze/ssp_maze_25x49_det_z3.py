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
pi61 = Real('pi61')
pi62 = Real('pi62')
pi63 = Real('pi63')
pi64 = Real('pi64')
pi65 = Real('pi65')
pi66 = Real('pi66')
pi67 = Real('pi67')
pi68 = Real('pi68')
pi69 = Real('pi69')
pi70 = Real('pi70')
pi71 = Real('pi71')
pi72 = Real('pi72')
pi73 = Real('pi73')
pi74 = Real('pi74')
pi75 = Real('pi75')
pi76 = Real('pi76')
pi77 = Real('pi77')
pi78 = Real('pi78')
pi79 = Real('pi79')
pi80 = Real('pi80')
pi81 = Real('pi81')
pi82 = Real('pi82')
pi83 = Real('pi83')
pi84 = Real('pi84')
pi85 = Real('pi85')
pi86 = Real('pi86')
pi87 = Real('pi87')
pi88 = Real('pi88')
pi89 = Real('pi89')
pi90 = Real('pi90')
pi91 = Real('pi91')
pi92 = Real('pi92')
pi93 = Real('pi93')
pi94 = Real('pi94')
pi95 = Real('pi95')
pi96 = Real('pi96')
pi97 = Real('pi97')
pi98 = Real('pi98')
pi99 = Real('pi99')
pi100 = Real('pi100')
pi101 = Real('pi101')
pi102 = Real('pi102')
pi103 = Real('pi103')
pi104 = Real('pi104')
pi105 = Real('pi105')
pi106 = Real('pi106')
pi107 = Real('pi107')
pi108 = Real('pi108')
pi109 = Real('pi109')
pi110 = Real('pi110')
pi111 = Real('pi111')
pi112 = Real('pi112')
pi113 = Real('pi113')
pi114 = Real('pi114')
pi115 = Real('pi115')
pi116 = Real('pi116')
pi117 = Real('pi117')
pi118 = Real('pi118')
pi119 = Real('pi119')
pi120 = Real('pi120')

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
y30 = Real('y30')
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
y61 = Real('y61')
y62 = Real('y62')
y63 = Real('y63')
y64 = Real('y64')
y65 = Real('y65')
y66 = Real('y66')
y67 = Real('y67')
y68 = Real('y68')
y69 = Real('y69')
y70 = Real('y70')
y71 = Real('y71')
y72 = Real('y72')
y73 = Real('y73')
y74 = Real('y74')
y75 = Real('y75')
y76 = Real('y76')
y77 = Real('y77')
y78 = Real('y78')
y79 = Real('y79')
y80 = Real('y80')
y81 = Real('y81')
y82 = Real('y82')
y83 = Real('y83')
y84 = Real('y84')
y85 = Real('y85')
y86 = Real('y86')
y87 = Real('y87')
y88 = Real('y88')
y89 = Real('y89')
y90 = Real('y90')
y91 = Real('y91')
y92 = Real('y92')
y93 = Real('y93')
y94 = Real('y94')
y95 = Real('y95')
y96 = Real('y96')
y97 = Real('y97')
y98 = Real('y98')
y99 = Real('y99')
y100 = Real('y100')
y101 = Real('y101')
y102 = Real('y102')
y103 = Real('y103')
y104 = Real('y104')
y105 = Real('y105')
y106 = Real('y106')
y107 = Real('y107')
y108 = Real('y108')
y109 = Real('y109')
y110 = Real('y110')
y111 = Real('y111')
y112 = Real('y112')
y113 = Real('y113')
y114 = Real('y114')
y115 = Real('y115')
y116 = Real('y116')
y117 = Real('y117')
y118 = Real('y118')
y120 = Real('y120')

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
xo8l = Real('xo8l')
xo8r = Real('xo8r')
xo8u = Real('xo8u')
xo8d = Real('xo8d')
xo9l = Real('xo9l')
xo9r = Real('xo9r')
xo9u = Real('xo9u')
xo9d = Real('xo9d')
xo10l = Real('xo10l')
xo10r = Real('xo10r')
xo10u = Real('xo10u')
xo10d = Real('xo10d')
xo11l = Real('xo11l')
xo11r = Real('xo11r')
xo11u = Real('xo11u')
xo11d = Real('xo11d')
xo12l = Real('xo12l')
xo12r = Real('xo12r')
xo12u = Real('xo12u')
xo12d = Real('xo12d')
xo13l = Real('xo13l')
xo13r = Real('xo13r')
xo13u = Real('xo13u')
xo13d = Real('xo13d')
xo14l = Real('xo14l')
xo14r = Real('xo14r')
xo14u = Real('xo14u')
xo14d = Real('xo14d')
xo15l = Real('xo15l')
xo15r = Real('xo15r')
xo15u = Real('xo15u')
xo15d = Real('xo15d')
xo16l = Real('xo16l')
xo16r = Real('xo16r')
xo16u = Real('xo16u')
xo16d = Real('xo16d')
xo17l = Real('xo17l')
xo17r = Real('xo17r')
xo17u = Real('xo17u')
xo17d = Real('xo17d')
xo18l = Real('xo18l')
xo18r = Real('xo18r')
xo18u = Real('xo18u')
xo18d = Real('xo18d')
xo19l = Real('xo19l')
xo19r = Real('xo19r')
xo19u = Real('xo19u')
xo19d = Real('xo19d')
xo20l = Real('xo20l')
xo20r = Real('xo20r')
xo20u = Real('xo20u')
xo20d = Real('xo20d')
xo21l = Real('xo21l')
xo21r = Real('xo21r')
xo21u = Real('xo21u')
xo21d = Real('xo21d')
xo22l = Real('xo22l')
xo22r = Real('xo22r')
xo22u = Real('xo22u')
xo22d = Real('xo22d')
xo23l = Real('xo23l')
xo23r = Real('xo23r')
xo23u = Real('xo23u')
xo23d = Real('xo23d')
xo24l = Real('xo24l')
xo24r = Real('xo24r')
xo24u = Real('xo24u')
xo24d = Real('xo24d')
xo25l = Real('xo25l')
xo25r = Real('xo25r')
xo25u = Real('xo25u')
xo25d = Real('xo25d')
xo26l = Real('xo26l')
xo26r = Real('xo26r')
xo26u = Real('xo26u')
xo26d = Real('xo26d')
xo27l = Real('xo27l')
xo27r = Real('xo27r')
xo27u = Real('xo27u')
xo27d = Real('xo27d')
xo28l = Real('xo28l')
xo28r = Real('xo28r')
xo28u = Real('xo28u')
xo28d = Real('xo28d')
xo29l = Real('xo29l')
xo29r = Real('xo29r')
xo29u = Real('xo29u')
xo29d = Real('xo29d')
xo30l = Real('xo30l')
xo30r = Real('xo30r')
xo30u = Real('xo30u')
xo30d = Real('xo30d')
xo31l = Real('xo31l')
xo31r = Real('xo31r')
xo31u = Real('xo31u')
xo31d = Real('xo31d')
xo32l = Real('xo32l')
xo32r = Real('xo32r')
xo32u = Real('xo32u')
xo32d = Real('xo32d')
xo33l = Real('xo33l')
xo33r = Real('xo33r')
xo33u = Real('xo33u')
xo33d = Real('xo33d')
xo34l = Real('xo34l')
xo34r = Real('xo34r')
xo34u = Real('xo34u')
xo34d = Real('xo34d')
xo35l = Real('xo35l')
xo35r = Real('xo35r')
xo35u = Real('xo35u')
xo35d = Real('xo35d')
xo36l = Real('xo36l')
xo36r = Real('xo36r')
xo36u = Real('xo36u')
xo36d = Real('xo36d')
xo37l = Real('xo37l')
xo37r = Real('xo37r')
xo37u = Real('xo37u')
xo37d = Real('xo37d')
xo38l = Real('xo38l')
xo38r = Real('xo38r')
xo38u = Real('xo38u')
xo38d = Real('xo38d')
xo39l = Real('xo39l')
xo39r = Real('xo39r')
xo39u = Real('xo39u')
xo39d = Real('xo39d')
xo40l = Real('xo40l')
xo40r = Real('xo40r')
xo40u = Real('xo40u')
xo40d = Real('xo40d')
xo41l = Real('xo41l')
xo41r = Real('xo41r')
xo41u = Real('xo41u')
xo41d = Real('xo41d')
xo42l = Real('xo42l')
xo42r = Real('xo42r')
xo42u = Real('xo42u')
xo42d = Real('xo42d')
xo43l = Real('xo43l')
xo43r = Real('xo43r')
xo43u = Real('xo43u')
xo43d = Real('xo43d')
xo44l = Real('xo44l')
xo44r = Real('xo44r')
xo44u = Real('xo44u')
xo44d = Real('xo44d')
xo45l = Real('xo45l')
xo45r = Real('xo45r')
xo45u = Real('xo45u')
xo45d = Real('xo45d')
xo46l = Real('xo46l')
xo46r = Real('xo46r')
xo46u = Real('xo46u')
xo46d = Real('xo46d')
xo47l = Real('xo47l')
xo47r = Real('xo47r')
xo47u = Real('xo47u')
xo47d = Real('xo47d')
xo48l = Real('xo48l')
xo48r = Real('xo48r')
xo48u = Real('xo48u')
xo48d = Real('xo48d')
xo49l = Real('xo49l')
xo49r = Real('xo49r')
xo49u = Real('xo49u')
xo49d = Real('xo49d')
xo50l = Real('xo50l')
xo50r = Real('xo50r')
xo50u = Real('xo50u')
xo50d = Real('xo50d')
xo51l = Real('xo51l')
xo51r = Real('xo51r')
xo51u = Real('xo51u')
xo51d = Real('xo51d')
xo52l = Real('xo52l')
xo52r = Real('xo52r')
xo52u = Real('xo52u')
xo52d = Real('xo52d')
xo53l = Real('xo53l')
xo53r = Real('xo53r')
xo53u = Real('xo53u')
xo53d = Real('xo53d')
xo54l = Real('xo54l')
xo54r = Real('xo54r')
xo54u = Real('xo54u')
xo54d = Real('xo54d')
xo55l = Real('xo55l')
xo55r = Real('xo55r')
xo55u = Real('xo55u')
xo55d = Real('xo55d')
xo56l = Real('xo56l')
xo56r = Real('xo56r')
xo56u = Real('xo56u')
xo56d = Real('xo56d')
xo57l = Real('xo57l')
xo57r = Real('xo57r')
xo57u = Real('xo57u')
xo57d = Real('xo57d')
xo58l = Real('xo58l')
xo58r = Real('xo58r')
xo58u = Real('xo58u')
xo58d = Real('xo58d')
xo59l = Real('xo59l')
xo59r = Real('xo59r')
xo59u = Real('xo59u')
xo59d = Real('xo59d')
xo60l = Real('xo60l')
xo60r = Real('xo60r')
xo60u = Real('xo60u')
xo60d = Real('xo60d')
xo61l = Real('xo61l')
xo61r = Real('xo61r')
xo61u = Real('xo61u')
xo61d = Real('xo61d')
xo62l = Real('xo62l')
xo62r = Real('xo62r')
xo62u = Real('xo62u')
xo62d = Real('xo62d')
xo63l = Real('xo63l')
xo63r = Real('xo63r')
xo63u = Real('xo63u')
xo63d = Real('xo63d')
xo64l = Real('xo64l')
xo64r = Real('xo64r')
xo64u = Real('xo64u')
xo64d = Real('xo64d')
xo65l = Real('xo65l')
xo65r = Real('xo65r')
xo65u = Real('xo65u')
xo65d = Real('xo65d')
xo66l = Real('xo66l')
xo66r = Real('xo66r')
xo66u = Real('xo66u')
xo66d = Real('xo66d')
xo67l = Real('xo67l')
xo67r = Real('xo67r')
xo67u = Real('xo67u')
xo67d = Real('xo67d')
xo68l = Real('xo68l')
xo68r = Real('xo68r')
xo68u = Real('xo68u')
xo68d = Real('xo68d')
xo69l = Real('xo69l')
xo69r = Real('xo69r')
xo69u = Real('xo69u')
xo69d = Real('xo69d')
xo70l = Real('xo70l')
xo70r = Real('xo70r')
xo70u = Real('xo70u')
xo70d = Real('xo70d')
xo71l = Real('xo71l')
xo71r = Real('xo71r')
xo71u = Real('xo71u')
xo71d = Real('xo71d')
xo72l = Real('xo72l')
xo72r = Real('xo72r')
xo72u = Real('xo72u')
xo72d = Real('xo72d')
xo73l = Real('xo73l')
xo73r = Real('xo73r')
xo73u = Real('xo73u')
xo73d = Real('xo73d')
xo74l = Real('xo74l')
xo74r = Real('xo74r')
xo74u = Real('xo74u')
xo74d = Real('xo74d')
xo75l = Real('xo75l')
xo75r = Real('xo75r')
xo75u = Real('xo75u')
xo75d = Real('xo75d')
xo76l = Real('xo76l')
xo76r = Real('xo76r')
xo76u = Real('xo76u')
xo76d = Real('xo76d')
xo77l = Real('xo77l')
xo77r = Real('xo77r')
xo77u = Real('xo77u')
xo77d = Real('xo77d')
xo78l = Real('xo78l')
xo78r = Real('xo78r')
xo78u = Real('xo78u')
xo78d = Real('xo78d')
xo79l = Real('xo79l')
xo79r = Real('xo79r')
xo79u = Real('xo79u')
xo79d = Real('xo79d')
xo80l = Real('xo80l')
xo80r = Real('xo80r')
xo80u = Real('xo80u')
xo80d = Real('xo80d')
xo81l = Real('xo81l')
xo81r = Real('xo81r')
xo81u = Real('xo81u')
xo81d = Real('xo81d')
xo82l = Real('xo82l')
xo82r = Real('xo82r')
xo82u = Real('xo82u')
xo82d = Real('xo82d')
xo83l = Real('xo83l')
xo83r = Real('xo83r')
xo83u = Real('xo83u')
xo83d = Real('xo83d')
xo84l = Real('xo84l')
xo84r = Real('xo84r')
xo84u = Real('xo84u')
xo84d = Real('xo84d')
xo85l = Real('xo85l')
xo85r = Real('xo85r')
xo85u = Real('xo85u')
xo85d = Real('xo85d')
xo86l = Real('xo86l')
xo86r = Real('xo86r')
xo86u = Real('xo86u')
xo86d = Real('xo86d')
xo87l = Real('xo87l')
xo87r = Real('xo87r')
xo87u = Real('xo87u')
xo87d = Real('xo87d')
xo88l = Real('xo88l')
xo88r = Real('xo88r')
xo88u = Real('xo88u')
xo88d = Real('xo88d')
xo89l = Real('xo89l')
xo89r = Real('xo89r')
xo89u = Real('xo89u')
xo89d = Real('xo89d')
xo90l = Real('xo90l')
xo90r = Real('xo90r')
xo90u = Real('xo90u')
xo90d = Real('xo90d')
xo91l = Real('xo91l')
xo91r = Real('xo91r')
xo91u = Real('xo91u')
xo91d = Real('xo91d')
xo92l = Real('xo92l')
xo92r = Real('xo92r')
xo92u = Real('xo92u')
xo92d = Real('xo92d')
xo93l = Real('xo93l')
xo93r = Real('xo93r')
xo93u = Real('xo93u')
xo93d = Real('xo93d')
xo94l = Real('xo94l')
xo94r = Real('xo94r')
xo94u = Real('xo94u')
xo94d = Real('xo94d')
xo95l = Real('xo95l')
xo95r = Real('xo95r')
xo95u = Real('xo95u')
xo95d = Real('xo95d')
xo96l = Real('xo96l')
xo96r = Real('xo96r')
xo96u = Real('xo96u')
xo96d = Real('xo96d')
xo97l = Real('xo97l')
xo97r = Real('xo97r')
xo97u = Real('xo97u')
xo97d = Real('xo97d')
xo98l = Real('xo98l')
xo98r = Real('xo98r')
xo98u = Real('xo98u')
xo98d = Real('xo98d')
xo99l = Real('xo99l')
xo99r = Real('xo99r')
xo99u = Real('xo99u')
xo99d = Real('xo99d')
xo100l = Real('xo100l')
xo100r = Real('xo100r')
xo100u = Real('xo100u')
xo100d = Real('xo100d')
xo101l = Real('xo101l')
xo101r = Real('xo101r')
xo101u = Real('xo101u')
xo101d = Real('xo101d')
xo102l = Real('xo102l')
xo102r = Real('xo102r')
xo102u = Real('xo102u')
xo102d = Real('xo102d')
xo103l = Real('xo103l')
xo103r = Real('xo103r')
xo103u = Real('xo103u')
xo103d = Real('xo103d')
xo104l = Real('xo104l')
xo104r = Real('xo104r')
xo104u = Real('xo104u')
xo104d = Real('xo104d')
xo105l = Real('xo105l')
xo105r = Real('xo105r')
xo105u = Real('xo105u')
xo105d = Real('xo105d')
xo106l = Real('xo106l')
xo106r = Real('xo106r')
xo106u = Real('xo106u')
xo106d = Real('xo106d')
xo107l = Real('xo107l')
xo107r = Real('xo107r')
xo107u = Real('xo107u')
xo107d = Real('xo107d')
xo108l = Real('xo108l')
xo108r = Real('xo108r')
xo108u = Real('xo108u')
xo108d = Real('xo108d')
xo109l = Real('xo109l')
xo109r = Real('xo109r')
xo109u = Real('xo109u')
xo109d = Real('xo109d')
xo110l = Real('xo110l')
xo110r = Real('xo110r')
xo110u = Real('xo110u')
xo110d = Real('xo110d')
xo111l = Real('xo111l')
xo111r = Real('xo111r')
xo111u = Real('xo111u')
xo111d = Real('xo111d')
xo112l = Real('xo112l')
xo112r = Real('xo112r')
xo112u = Real('xo112u')
xo112d = Real('xo112d')
xo113l = Real('xo113l')
xo113r = Real('xo113r')
xo113u = Real('xo113u')
xo113d = Real('xo113d')
xo114l = Real('xo114l')
xo114r = Real('xo114r')
xo114u = Real('xo114u')
xo114d = Real('xo114d')
xo115l = Real('xo115l')
xo115r = Real('xo115r')
xo115u = Real('xo115u')
xo115d = Real('xo115d')
xo116l = Real('xo116l')
xo116r = Real('xo116r')
xo116u = Real('xo116u')
xo116d = Real('xo116d')
xo117l = Real('xo117l')
xo117r = Real('xo117r')
xo117u = Real('xo117u')
xo117d = Real('xo117d')
xo118l = Real('xo118l')
xo118r = Real('xo118r')
xo118u = Real('xo118u')
xo118d = Real('xo118d')
xo119l = Real('xo119l')
xo119r = Real('xo119r')
xo119u = Real('xo119u')
xo119d = Real('xo119d')
xo120l = Real('xo120l')
xo120r = Real('xo120r')
xo120u = Real('xo120u')
xo120d = Real('xo120d')
xol = Real('xol')
xor = Real('xor')
xod = Real('xod')
xou = Real('xou')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=48, pi1>=47, pi2>=46, pi3>=45, pi4>=44, pi5>=43, pi6>=42, pi7>=41, pi8>=40, pi9>=39, pi10>=38, pi11>=37, pi12>=36, pi13>=35, pi14>=34, pi15>=33, pi16>=32, pi17>=31, pi18>=30, pi19>=29, pi20>=28, pi21>=27, pi22>=26, pi23>=25, pi24>=24, pi25>=25, pi26>=26, pi27>=27, pi28>=28, pi29>=29, pi30>=30, pi31>=31, pi32>=32, pi33>=33, pi34>=34, pi35>=35, pi36>=36, pi37>=37, pi38>=38, pi39>=39, pi40>=40, pi41>=41, pi42>=42, pi43>=43, pi44>=44, pi45>=45, pi46>=46, pi47>=47, pi48>=48, pi49>=49, pi50>=23, pi51>=49, pi52>=50, pi53>=22, pi54>=50, pi55>=51, pi56>=21, pi57>=51, pi58>=52, pi59>=20, pi60>=52, pi61>=53, pi62>=19, pi63>=53, pi64>=54, pi65>=18, pi66>=54, pi67>=55, pi68>=17, pi69>=55, pi70>=56, pi71>=16, pi72>=56, pi73>=57, pi74>=15, pi75>=57, pi76>=58, pi77>=14, pi78>=58, pi79>=59, pi80>=13, pi81>=59, pi82>=60, pi83>=12, pi84>=60, pi85>=61, pi86>=11, pi87>=61, pi88>=62, pi89>=10, pi90>=62, pi91>=63, pi92>=9, pi93>=63, pi94>=64, pi95>=8, pi96>=64, pi97>=65, pi98>=7, pi99>=65, pi100>=66, pi101>=6, pi102>=66, pi103>=67, pi104>=5, pi105>=67, pi106>=68, pi107>=4, pi108>=68, pi109>=69, pi110>=3, pi111>=69, pi112>=70, pi113>=2, pi114>=70, pi115>=71, pi116>=1, pi117>=71, pi118>=72, pi119>=0, pi120>=72, 
# Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + ((1 - y0)*xor + y0*xo0r) * (1 + pi1) + ((1 - y0)*xou + y0*xo0u) * (1 + pi0) + ((1 - y0)*xod + y0*xo0d) * (1 + pi49),
pi1== ((1 - y1)*xol + y1*xo1l) * (1 + pi0) + ((1 - y1)*xor + y1*xo1r) * (1 + pi2) + ((1 - y1)*xou + y1*xo1u) * (1 + pi1) + ((1 - y1)*xod + y1*xo1d) * (1 + pi1),
pi2== ((1 - y2)*xol + y2*xo2l) * (1 + pi1) + ((1 - y2)*xor + y2*xo2r) * (1 + pi3) + ((1 - y2)*xou + y2*xo2u) * (1 + pi2) + ((1 - y2)*xod + y2*xo2d) * (1 + pi2),
pi3== ((1 - y3)*xol + y3*xo3l) * (1 + pi2) + ((1 - y3)*xor + y3*xo3r) * (1 + pi4) + ((1 - y3)*xou + y3*xo3u) * (1 + pi3) + ((1 - y3)*xod + y3*xo3d) * (1 + pi3),
pi4== ((1 - y4)*xol + y4*xo4l) * (1 + pi3) + ((1 - y4)*xor + y4*xo4r) * (1 + pi5) + ((1 - y4)*xou + y4*xo4u) * (1 + pi4) + ((1 - y4)*xod + y4*xo4d) * (1 + pi4),
pi5== ((1 - y5)*xol + y5*xo5l) * (1 + pi4) + ((1 - y5)*xor + y5*xo5r) * (1 + pi6) + ((1 - y5)*xou + y5*xo5u) * (1 + pi5) + ((1 - y5)*xod + y5*xo5d) * (1 + pi5),
pi6== ((1 - y6)*xol + y6*xo6l) * (1 + pi5) + ((1 - y6)*xor + y6*xo6r) * (1 + pi7) + ((1 - y6)*xou + y6*xo6u) * (1 + pi6) + ((1 - y6)*xod + y6*xo6d) * (1 + pi6),
pi7== ((1 - y7)*xol + y7*xo7l) * (1 + pi6) + ((1 - y7)*xor + y7*xo7r) * (1 + pi8) + ((1 - y7)*xou + y7*xo7u) * (1 + pi7) + ((1 - y7)*xod + y7*xo7d) * (1 + pi7),
pi8== ((1 - y8)*xol + y8*xo8l) * (1 + pi7) + ((1 - y8)*xor + y8*xo8r) * (1 + pi9) + ((1 - y8)*xou + y8*xo8u) * (1 + pi8) + ((1 - y8)*xod + y8*xo8d) * (1 + pi8),
pi9== ((1 - y9)*xol + y9*xo9l) * (1 + pi8) + ((1 - y9)*xor + y9*xo9r) * (1 + pi10) + ((1 - y9)*xou + y9*xo9u) * (1 + pi9) + ((1 - y9)*xod + y9*xo9d) * (1 + pi9),
pi10== ((1 - y10)*xol + y10*xo10l) * (1 + pi9) + ((1 - y10)*xor + y10*xo10r) * (1 + pi11) + ((1 - y10)*xou + y10*xo10u) * (1 + pi10) + ((1 - y10)*xod + y10*xo10d) * (1 + pi10),
pi11== ((1 - y11)*xol + y11*xo11l) * (1 + pi10) + ((1 - y11)*xor + y11*xo11r) * (1 + pi12) + ((1 - y11)*xou + y11*xo11u) * (1 + pi11) + ((1 - y11)*xod + y11*xo11d) * (1 + pi11),
pi12== ((1 - y12)*xol + y12*xo12l) * (1 + pi11) + ((1 - y12)*xor + y12*xo12r) * (1 + pi13) + ((1 - y12)*xou + y12*xo12u) * (1 + pi12) + ((1 - y12)*xod + y12*xo12d) * (1 + pi12),
pi13== ((1 - y13)*xol + y13*xo13l) * (1 + pi12) + ((1 - y13)*xor + y13*xo13r) * (1 + pi14) + ((1 - y13)*xou + y13*xo13u) * (1 + pi13) + ((1 - y13)*xod + y13*xo13d) * (1 + pi13),
pi14== ((1 - y14)*xol + y14*xo14l) * (1 + pi13) + ((1 - y14)*xor + y14*xo14r) * (1 + pi15) + ((1 - y14)*xou + y14*xo14u) * (1 + pi14) + ((1 - y14)*xod + y14*xo14d) * (1 + pi14),
pi15== ((1 - y15)*xol + y15*xo15l) * (1 + pi14) + ((1 - y15)*xor + y15*xo15r) * (1 + pi16) + ((1 - y15)*xou + y15*xo15u) * (1 + pi15) + ((1 - y15)*xod + y15*xo15d) * (1 + pi15),
pi16== ((1 - y16)*xol + y16*xo16l) * (1 + pi15) + ((1 - y16)*xor + y16*xo16r) * (1 + pi17) + ((1 - y16)*xou + y16*xo16u) * (1 + pi16) + ((1 - y16)*xod + y16*xo16d) * (1 + pi16),
pi17== ((1 - y17)*xol + y17*xo17l) * (1 + pi16) + ((1 - y17)*xor + y17*xo17r) * (1 + pi18) + ((1 - y17)*xou + y17*xo17u) * (1 + pi17) + ((1 - y17)*xod + y17*xo17d) * (1 + pi17),
pi18== ((1 - y18)*xol + y18*xo18l) * (1 + pi17) + ((1 - y18)*xor + y18*xo18r) * (1 + pi19) + ((1 - y18)*xou + y18*xo18u) * (1 + pi18) + ((1 - y18)*xod + y18*xo18d) * (1 + pi18),
pi19== ((1 - y19)*xol + y19*xo19l) * (1 + pi18) + ((1 - y19)*xor + y19*xo19r) * (1 + pi20) + ((1 - y19)*xou + y19*xo19u) * (1 + pi19) + ((1 - y19)*xod + y19*xo19d) * (1 + pi19),
pi20== ((1 - y20)*xol + y20*xo20l) * (1 + pi19) + ((1 - y20)*xor + y20*xo20r) * (1 + pi21) + ((1 - y20)*xou + y20*xo20u) * (1 + pi20) + ((1 - y20)*xod + y20*xo20d) * (1 + pi20),
pi21== ((1 - y21)*xol + y21*xo21l) * (1 + pi20) + ((1 - y21)*xor + y21*xo21r) * (1 + pi22) + ((1 - y21)*xou + y21*xo21u) * (1 + pi21) + ((1 - y21)*xod + y21*xo21d) * (1 + pi21),
pi22== ((1 - y22)*xol + y22*xo22l) * (1 + pi21) + ((1 - y22)*xor + y22*xo22r) * (1 + pi23) + ((1 - y22)*xou + y22*xo22u) * (1 + pi22) + ((1 - y22)*xod + y22*xo22d) * (1 + pi22),
pi23== ((1 - y23)*xol + y23*xo23l) * (1 + pi22) + ((1 - y23)*xor + y23*xo23r) * (1 + pi24) + ((1 - y23)*xou + y23*xo23u) * (1 + pi23) + ((1 - y23)*xod + y23*xo23d) * (1 + pi23),
pi24== ((1 - y24)*xol + y24*xo24l) * (1 + pi23) + ((1 - y24)*xor + y24*xo24r) * (1 + pi25) + ((1 - y24)*xou + y24*xo24u) * (1 + pi24) + ((1 - y24)*xod + y24*xo24d) * (1 + pi50),
pi25== ((1 - y25)*xol + y25*xo25l) * (1 + pi24) + ((1 - y25)*xor + y25*xo25r) * (1 + pi26) + ((1 - y25)*xou + y25*xo25u) * (1 + pi25) + ((1 - y25)*xod + y25*xo25d) * (1 + pi25),
pi26== ((1 - y26)*xol + y26*xo26l) * (1 + pi25) + ((1 - y26)*xor + y26*xo26r) * (1 + pi27) + ((1 - y26)*xou + y26*xo26u) * (1 + pi26) + ((1 - y26)*xod + y26*xo26d) * (1 + pi26),
pi27== ((1 - y27)*xol + y27*xo27l) * (1 + pi26) + ((1 - y27)*xor + y27*xo27r) * (1 + pi28) + ((1 - y27)*xou + y27*xo27u) * (1 + pi27) + ((1 - y27)*xod + y27*xo27d) * (1 + pi27),
pi28== ((1 - y28)*xol + y28*xo28l) * (1 + pi27) + ((1 - y28)*xor + y28*xo28r) * (1 + pi29) + ((1 - y28)*xou + y28*xo28u) * (1 + pi28) + ((1 - y28)*xod + y28*xo28d) * (1 + pi28),
pi29== ((1 - y29)*xol + y29*xo29l) * (1 + pi28) + ((1 - y29)*xor + y29*xo29r) * (1 + pi30) + ((1 - y29)*xou + y29*xo29u) * (1 + pi29) + ((1 - y29)*xod + y29*xo29d) * (1 + pi29),
pi30== ((1 - y30)*xol + y30*xo30l) * (1 + pi29) + ((1 - y30)*xor + y30*xo30r) * (1 + pi31) + ((1 - y30)*xou + y30*xo30u) * (1 + pi30) + ((1 - y30)*xod + y30*xo30d) * (1 + pi30),
pi31== ((1 - y31)*xol + y31*xo31l) * (1 + pi30) + ((1 - y31)*xor + y31*xo31r) * (1 + pi32) + ((1 - y31)*xou + y31*xo31u) * (1 + pi31) + ((1 - y31)*xod + y31*xo31d) * (1 + pi31),
pi32== ((1 - y32)*xol + y32*xo32l) * (1 + pi31) + ((1 - y32)*xor + y32*xo32r) * (1 + pi33) + ((1 - y32)*xou + y32*xo32u) * (1 + pi32) + ((1 - y32)*xod + y32*xo32d) * (1 + pi32),
pi33== ((1 - y33)*xol + y33*xo33l) * (1 + pi32) + ((1 - y33)*xor + y33*xo33r) * (1 + pi34) + ((1 - y33)*xou + y33*xo33u) * (1 + pi33) + ((1 - y33)*xod + y33*xo33d) * (1 + pi33),
pi34== ((1 - y34)*xol + y34*xo34l) * (1 + pi33) + ((1 - y34)*xor + y34*xo34r) * (1 + pi35) + ((1 - y34)*xou + y34*xo34u) * (1 + pi34) + ((1 - y34)*xod + y34*xo34d) * (1 + pi34),
pi35== ((1 - y35)*xol + y35*xo35l) * (1 + pi34) + ((1 - y35)*xor + y35*xo35r) * (1 + pi36) + ((1 - y35)*xou + y35*xo35u) * (1 + pi35) + ((1 - y35)*xod + y35*xo35d) * (1 + pi35),
pi36== ((1 - y36)*xol + y36*xo36l) * (1 + pi35) + ((1 - y36)*xor + y36*xo36r) * (1 + pi37) + ((1 - y36)*xou + y36*xo36u) * (1 + pi36) + ((1 - y36)*xod + y36*xo36d) * (1 + pi36),
pi37== ((1 - y37)*xol + y37*xo37l) * (1 + pi36) + ((1 - y37)*xor + y37*xo37r) * (1 + pi38) + ((1 - y37)*xou + y37*xo37u) * (1 + pi37) + ((1 - y37)*xod + y37*xo37d) * (1 + pi37),
pi38== ((1 - y38)*xol + y38*xo38l) * (1 + pi37) + ((1 - y38)*xor + y38*xo38r) * (1 + pi39) + ((1 - y38)*xou + y38*xo38u) * (1 + pi38) + ((1 - y38)*xod + y38*xo38d) * (1 + pi38),
pi39== ((1 - y39)*xol + y39*xo39l) * (1 + pi38) + ((1 - y39)*xor + y39*xo39r) * (1 + pi40) + ((1 - y39)*xou + y39*xo39u) * (1 + pi39) + ((1 - y39)*xod + y39*xo39d) * (1 + pi39),
pi40== ((1 - y40)*xol + y40*xo40l) * (1 + pi39) + ((1 - y40)*xor + y40*xo40r) * (1 + pi41) + ((1 - y40)*xou + y40*xo40u) * (1 + pi40) + ((1 - y40)*xod + y40*xo40d) * (1 + pi40),
pi41== ((1 - y41)*xol + y41*xo41l) * (1 + pi40) + ((1 - y41)*xor + y41*xo41r) * (1 + pi42) + ((1 - y41)*xou + y41*xo41u) * (1 + pi41) + ((1 - y41)*xod + y41*xo41d) * (1 + pi41),
pi42== ((1 - y42)*xol + y42*xo42l) * (1 + pi41) + ((1 - y42)*xor + y42*xo42r) * (1 + pi43) + ((1 - y42)*xou + y42*xo42u) * (1 + pi42) + ((1 - y42)*xod + y42*xo42d) * (1 + pi42),
pi43== ((1 - y43)*xol + y43*xo43l) * (1 + pi42) + ((1 - y43)*xor + y43*xo43r) * (1 + pi44) + ((1 - y43)*xou + y43*xo43u) * (1 + pi43) + ((1 - y43)*xod + y43*xo43d) * (1 + pi43),
pi44== ((1 - y44)*xol + y44*xo44l) * (1 + pi43) + ((1 - y44)*xor + y44*xo44r) * (1 + pi45) + ((1 - y44)*xou + y44*xo44u) * (1 + pi44) + ((1 - y44)*xod + y44*xo44d) * (1 + pi44),
pi45== ((1 - y45)*xol + y45*xo45l) * (1 + pi44) + ((1 - y45)*xor + y45*xo45r) * (1 + pi46) + ((1 - y45)*xou + y45*xo45u) * (1 + pi45) + ((1 - y45)*xod + y45*xo45d) * (1 + pi45),
pi46== ((1 - y46)*xol + y46*xo46l) * (1 + pi45) + ((1 - y46)*xor + y46*xo46r) * (1 + pi47) + ((1 - y46)*xou + y46*xo46u) * (1 + pi46) + ((1 - y46)*xod + y46*xo46d) * (1 + pi46),
pi47== ((1 - y47)*xol + y47*xo47l) * (1 + pi46) + ((1 - y47)*xor + y47*xo47r) * (1 + pi48) + ((1 - y47)*xou + y47*xo47u) * (1 + pi47) + ((1 - y47)*xod + y47*xo47d) * (1 + pi47),
pi48== ((1 - y48)*xol + y48*xo48l) * (1 + pi47) + ((1 - y48)*xor + y48*xo48r) * (1 + pi48) + ((1 - y48)*xou + y48*xo48u) * (1 + pi48) + ((1 - y48)*xod + y48*xo48d) * (1 + pi51),
pi49== ((1 - y49)*xol + y49*xo49l) * (1 + pi49) + ((1 - y49)*xor + y49*xo49r) * (1 + pi49) + ((1 - y49)*xou + y49*xo49u) * (1 + pi0) + ((1 - y49)*xod + y49*xo49d) * (1 + pi52),
pi50== ((1 - y50)*xol + y50*xo50l) * (1 + pi50) + ((1 - y50)*xor + y50*xo50r) * (1 + pi50) + ((1 - y50)*xou + y50*xo50u) * (1 + pi24) + ((1 - y50)*xod + y50*xo50d) * (1 + pi53),
pi51== ((1 - y51)*xol + y51*xo51l) * (1 + pi51) + ((1 - y51)*xor + y51*xo51r) * (1 + pi51) + ((1 - y51)*xou + y51*xo51u) * (1 + pi48) + ((1 - y51)*xod + y51*xo51d) * (1 + pi54),
pi52== ((1 - y52)*xol + y52*xo52l) * (1 + pi52) + ((1 - y52)*xor + y52*xo52r) * (1 + pi52) + ((1 - y52)*xou + y52*xo52u) * (1 + pi49) + ((1 - y52)*xod + y52*xo52d) * (1 + pi55),
pi53== ((1 - y53)*xol + y53*xo53l) * (1 + pi53) + ((1 - y53)*xor + y53*xo53r) * (1 + pi53) + ((1 - y53)*xou + y53*xo53u) * (1 + pi50) + ((1 - y53)*xod + y53*xo53d) * (1 + pi56),
pi54== ((1 - y54)*xol + y54*xo54l) * (1 + pi54) + ((1 - y54)*xor + y54*xo54r) * (1 + pi54) + ((1 - y54)*xou + y54*xo54u) * (1 + pi51) + ((1 - y54)*xod + y54*xo54d) * (1 + pi57),
pi55== ((1 - y55)*xol + y55*xo55l) * (1 + pi55) + ((1 - y55)*xor + y55*xo55r) * (1 + pi55) + ((1 - y55)*xou + y55*xo55u) * (1 + pi52) + ((1 - y55)*xod + y55*xo55d) * (1 + pi58),
pi56== ((1 - y56)*xol + y56*xo56l) * (1 + pi56) + ((1 - y56)*xor + y56*xo56r) * (1 + pi56) + ((1 - y56)*xou + y56*xo56u) * (1 + pi53) + ((1 - y56)*xod + y56*xo56d) * (1 + pi59),
pi57== ((1 - y57)*xol + y57*xo57l) * (1 + pi57) + ((1 - y57)*xor + y57*xo57r) * (1 + pi57) + ((1 - y57)*xou + y57*xo57u) * (1 + pi54) + ((1 - y57)*xod + y57*xo57d) * (1 + pi60),
pi58== ((1 - y58)*xol + y58*xo58l) * (1 + pi58) + ((1 - y58)*xor + y58*xo58r) * (1 + pi58) + ((1 - y58)*xou + y58*xo58u) * (1 + pi55) + ((1 - y58)*xod + y58*xo58d) * (1 + pi61),
pi59== ((1 - y59)*xol + y59*xo59l) * (1 + pi59) + ((1 - y59)*xor + y59*xo59r) * (1 + pi59) + ((1 - y59)*xou + y59*xo59u) * (1 + pi56) + ((1 - y59)*xod + y59*xo59d) * (1 + pi62),
pi60== ((1 - y60)*xol + y60*xo60l) * (1 + pi60) + ((1 - y60)*xor + y60*xo60r) * (1 + pi60) + ((1 - y60)*xou + y60*xo60u) * (1 + pi57) + ((1 - y60)*xod + y60*xo60d) * (1 + pi63),
pi61== ((1 - y61)*xol + y61*xo61l) * (1 + pi61) + ((1 - y61)*xor + y61*xo61r) * (1 + pi61) + ((1 - y61)*xou + y61*xo61u) * (1 + pi58) + ((1 - y61)*xod + y61*xo61d) * (1 + pi64),
pi62== ((1 - y62)*xol + y62*xo62l) * (1 + pi62) + ((1 - y62)*xor + y62*xo62r) * (1 + pi62) + ((1 - y62)*xou + y62*xo62u) * (1 + pi59) + ((1 - y62)*xod + y62*xo62d) * (1 + pi65),
pi63== ((1 - y63)*xol + y63*xo63l) * (1 + pi63) + ((1 - y63)*xor + y63*xo63r) * (1 + pi63) + ((1 - y63)*xou + y63*xo63u) * (1 + pi60) + ((1 - y63)*xod + y63*xo63d) * (1 + pi66),
pi64== ((1 - y64)*xol + y64*xo64l) * (1 + pi64) + ((1 - y64)*xor + y64*xo64r) * (1 + pi64) + ((1 - y64)*xou + y64*xo64u) * (1 + pi61) + ((1 - y64)*xod + y64*xo64d) * (1 + pi67),
pi65== ((1 - y65)*xol + y65*xo65l) * (1 + pi65) + ((1 - y65)*xor + y65*xo65r) * (1 + pi65) + ((1 - y65)*xou + y65*xo65u) * (1 + pi62) + ((1 - y65)*xod + y65*xo65d) * (1 + pi68),
pi66== ((1 - y66)*xol + y66*xo66l) * (1 + pi66) + ((1 - y66)*xor + y66*xo66r) * (1 + pi66) + ((1 - y66)*xou + y66*xo66u) * (1 + pi63) + ((1 - y66)*xod + y66*xo66d) * (1 + pi69),
pi67== ((1 - y67)*xol + y67*xo67l) * (1 + pi67) + ((1 - y67)*xor + y67*xo67r) * (1 + pi67) + ((1 - y67)*xou + y67*xo67u) * (1 + pi64) + ((1 - y67)*xod + y67*xo67d) * (1 + pi70),
pi68== ((1 - y68)*xol + y68*xo68l) * (1 + pi68) + ((1 - y68)*xor + y68*xo68r) * (1 + pi68) + ((1 - y68)*xou + y68*xo68u) * (1 + pi65) + ((1 - y68)*xod + y68*xo68d) * (1 + pi71),
pi69== ((1 - y69)*xol + y69*xo69l) * (1 + pi69) + ((1 - y69)*xor + y69*xo69r) * (1 + pi69) + ((1 - y69)*xou + y69*xo69u) * (1 + pi66) + ((1 - y69)*xod + y69*xo69d) * (1 + pi72),
pi70== ((1 - y70)*xol + y70*xo70l) * (1 + pi70) + ((1 - y70)*xor + y70*xo70r) * (1 + pi70) + ((1 - y70)*xou + y70*xo70u) * (1 + pi67) + ((1 - y70)*xod + y70*xo70d) * (1 + pi73),
pi71== ((1 - y71)*xol + y71*xo71l) * (1 + pi71) + ((1 - y71)*xor + y71*xo71r) * (1 + pi71) + ((1 - y71)*xou + y71*xo71u) * (1 + pi68) + ((1 - y71)*xod + y71*xo71d) * (1 + pi74),
pi72== ((1 - y72)*xol + y72*xo72l) * (1 + pi72) + ((1 - y72)*xor + y72*xo72r) * (1 + pi72) + ((1 - y72)*xou + y72*xo72u) * (1 + pi69) + ((1 - y72)*xod + y72*xo72d) * (1 + pi75),
pi73== ((1 - y73)*xol + y73*xo73l) * (1 + pi73) + ((1 - y73)*xor + y73*xo73r) * (1 + pi73) + ((1 - y73)*xou + y73*xo73u) * (1 + pi70) + ((1 - y73)*xod + y73*xo73d) * (1 + pi76),
pi74== ((1 - y74)*xol + y74*xo74l) * (1 + pi74) + ((1 - y74)*xor + y74*xo74r) * (1 + pi74) + ((1 - y74)*xou + y74*xo74u) * (1 + pi71) + ((1 - y74)*xod + y74*xo74d) * (1 + pi77),
pi75== ((1 - y75)*xol + y75*xo75l) * (1 + pi75) + ((1 - y75)*xor + y75*xo75r) * (1 + pi75) + ((1 - y75)*xou + y75*xo75u) * (1 + pi72) + ((1 - y75)*xod + y75*xo75d) * (1 + pi78),
pi76== ((1 - y76)*xol + y76*xo76l) * (1 + pi76) + ((1 - y76)*xor + y76*xo76r) * (1 + pi76) + ((1 - y76)*xou + y76*xo76u) * (1 + pi73) + ((1 - y76)*xod + y76*xo76d) * (1 + pi79),
pi77== ((1 - y77)*xol + y77*xo77l) * (1 + pi77) + ((1 - y77)*xor + y77*xo77r) * (1 + pi77) + ((1 - y77)*xou + y77*xo77u) * (1 + pi74) + ((1 - y77)*xod + y77*xo77d) * (1 + pi80),
pi78== ((1 - y78)*xol + y78*xo78l) * (1 + pi78) + ((1 - y78)*xor + y78*xo78r) * (1 + pi78) + ((1 - y78)*xou + y78*xo78u) * (1 + pi75) + ((1 - y78)*xod + y78*xo78d) * (1 + pi81),
pi79== ((1 - y79)*xol + y79*xo79l) * (1 + pi79) + ((1 - y79)*xor + y79*xo79r) * (1 + pi79) + ((1 - y79)*xou + y79*xo79u) * (1 + pi76) + ((1 - y79)*xod + y79*xo79d) * (1 + pi82),
pi80== ((1 - y80)*xol + y80*xo80l) * (1 + pi80) + ((1 - y80)*xor + y80*xo80r) * (1 + pi80) + ((1 - y80)*xou + y80*xo80u) * (1 + pi77) + ((1 - y80)*xod + y80*xo80d) * (1 + pi83),
pi81== ((1 - y81)*xol + y81*xo81l) * (1 + pi81) + ((1 - y81)*xor + y81*xo81r) * (1 + pi81) + ((1 - y81)*xou + y81*xo81u) * (1 + pi78) + ((1 - y81)*xod + y81*xo81d) * (1 + pi84),
pi82== ((1 - y82)*xol + y82*xo82l) * (1 + pi82) + ((1 - y82)*xor + y82*xo82r) * (1 + pi82) + ((1 - y82)*xou + y82*xo82u) * (1 + pi79) + ((1 - y82)*xod + y82*xo82d) * (1 + pi85),
pi83== ((1 - y83)*xol + y83*xo83l) * (1 + pi83) + ((1 - y83)*xor + y83*xo83r) * (1 + pi83) + ((1 - y83)*xou + y83*xo83u) * (1 + pi80) + ((1 - y83)*xod + y83*xo83d) * (1 + pi86),
pi84== ((1 - y84)*xol + y84*xo84l) * (1 + pi84) + ((1 - y84)*xor + y84*xo84r) * (1 + pi84) + ((1 - y84)*xou + y84*xo84u) * (1 + pi81) + ((1 - y84)*xod + y84*xo84d) * (1 + pi87),
pi85== ((1 - y85)*xol + y85*xo85l) * (1 + pi85) + ((1 - y85)*xor + y85*xo85r) * (1 + pi85) + ((1 - y85)*xou + y85*xo85u) * (1 + pi82) + ((1 - y85)*xod + y85*xo85d) * (1 + pi88),
pi86== ((1 - y86)*xol + y86*xo86l) * (1 + pi86) + ((1 - y86)*xor + y86*xo86r) * (1 + pi86) + ((1 - y86)*xou + y86*xo86u) * (1 + pi83) + ((1 - y86)*xod + y86*xo86d) * (1 + pi89),
pi87== ((1 - y87)*xol + y87*xo87l) * (1 + pi87) + ((1 - y87)*xor + y87*xo87r) * (1 + pi87) + ((1 - y87)*xou + y87*xo87u) * (1 + pi84) + ((1 - y87)*xod + y87*xo87d) * (1 + pi90),
pi88== ((1 - y88)*xol + y88*xo88l) * (1 + pi88) + ((1 - y88)*xor + y88*xo88r) * (1 + pi88) + ((1 - y88)*xou + y88*xo88u) * (1 + pi85) + ((1 - y88)*xod + y88*xo88d) * (1 + pi91),
pi89== ((1 - y89)*xol + y89*xo89l) * (1 + pi89) + ((1 - y89)*xor + y89*xo89r) * (1 + pi89) + ((1 - y89)*xou + y89*xo89u) * (1 + pi86) + ((1 - y89)*xod + y89*xo89d) * (1 + pi92),
pi90== ((1 - y90)*xol + y90*xo90l) * (1 + pi90) + ((1 - y90)*xor + y90*xo90r) * (1 + pi90) + ((1 - y90)*xou + y90*xo90u) * (1 + pi87) + ((1 - y90)*xod + y90*xo90d) * (1 + pi93),
pi91== ((1 - y91)*xol + y91*xo91l) * (1 + pi91) + ((1 - y91)*xor + y91*xo91r) * (1 + pi91) + ((1 - y91)*xou + y91*xo91u) * (1 + pi88) + ((1 - y91)*xod + y91*xo91d) * (1 + pi94),
pi92== ((1 - y92)*xol + y92*xo92l) * (1 + pi92) + ((1 - y92)*xor + y92*xo92r) * (1 + pi92) + ((1 - y92)*xou + y92*xo92u) * (1 + pi89) + ((1 - y92)*xod + y92*xo92d) * (1 + pi95),
pi93== ((1 - y93)*xol + y93*xo93l) * (1 + pi93) + ((1 - y93)*xor + y93*xo93r) * (1 + pi93) + ((1 - y93)*xou + y93*xo93u) * (1 + pi90) + ((1 - y93)*xod + y93*xo93d) * (1 + pi96),
pi94== ((1 - y94)*xol + y94*xo94l) * (1 + pi94) + ((1 - y94)*xor + y94*xo94r) * (1 + pi94) + ((1 - y94)*xou + y94*xo94u) * (1 + pi91) + ((1 - y94)*xod + y94*xo94d) * (1 + pi97),
pi95== ((1 - y95)*xol + y95*xo95l) * (1 + pi95) + ((1 - y95)*xor + y95*xo95r) * (1 + pi95) + ((1 - y95)*xou + y95*xo95u) * (1 + pi92) + ((1 - y95)*xod + y95*xo95d) * (1 + pi98),
pi96== ((1 - y96)*xol + y96*xo96l) * (1 + pi96) + ((1 - y96)*xor + y96*xo96r) * (1 + pi96) + ((1 - y96)*xou + y96*xo96u) * (1 + pi93) + ((1 - y96)*xod + y96*xo96d) * (1 + pi99),
pi97== ((1 - y97)*xol + y97*xo97l) * (1 + pi97) + ((1 - y97)*xor + y97*xo97r) * (1 + pi97) + ((1 - y97)*xou + y97*xo97u) * (1 + pi94) + ((1 - y97)*xod + y97*xo97d) * (1 + pi100),
pi98== ((1 - y98)*xol + y98*xo98l) * (1 + pi98) + ((1 - y98)*xor + y98*xo98r) * (1 + pi98) + ((1 - y98)*xou + y98*xo98u) * (1 + pi95) + ((1 - y98)*xod + y98*xo98d) * (1 + pi101),
pi99== ((1 - y99)*xol + y99*xo99l) * (1 + pi99) + ((1 - y99)*xor + y99*xo99r) * (1 + pi99) + ((1 - y99)*xou + y99*xo99u) * (1 + pi96) + ((1 - y99)*xod + y99*xo99d) * (1 + pi102),
pi100== ((1 - y100)*xol + y100*xo100l) * (1 + pi100) + ((1 - y100)*xor + y100*xo100r) * (1 + pi100) + ((1 - y100)*xou + y100*xo100u) * (1 + pi97) + ((1 - y100)*xod + y100*xo100d) * (1 + pi103),
pi101== ((1 - y101)*xol + y101*xo101l) * (1 + pi101) + ((1 - y101)*xor + y101*xo101r) * (1 + pi101) + ((1 - y101)*xou + y101*xo101u) * (1 + pi98) + ((1 - y101)*xod + y101*xo101d) * (1 + pi104),
pi102== ((1 - y102)*xol + y102*xo102l) * (1 + pi102) + ((1 - y102)*xor + y102*xo102r) * (1 + pi102) + ((1 - y102)*xou + y102*xo102u) * (1 + pi99) + ((1 - y102)*xod + y102*xo102d) * (1 + pi105),
pi103== ((1 - y103)*xol + y103*xo103l) * (1 + pi103) + ((1 - y103)*xor + y103*xo103r) * (1 + pi103) + ((1 - y103)*xou + y103*xo103u) * (1 + pi100) + ((1 - y103)*xod + y103*xo103d) * (1 + pi106),
pi104== ((1 - y104)*xol + y104*xo104l) * (1 + pi104) + ((1 - y104)*xor + y104*xo104r) * (1 + pi104) + ((1 - y104)*xou + y104*xo104u) * (1 + pi101) + ((1 - y104)*xod + y104*xo104d) * (1 + pi107),
pi105== ((1 - y105)*xol + y105*xo105l) * (1 + pi105) + ((1 - y105)*xor + y105*xo105r) * (1 + pi105) + ((1 - y105)*xou + y105*xo105u) * (1 + pi102) + ((1 - y105)*xod + y105*xo105d) * (1 + pi108),
pi106== ((1 - y106)*xol + y106*xo106l) * (1 + pi106) + ((1 - y106)*xor + y106*xo106r) * (1 + pi106) + ((1 - y106)*xou + y106*xo106u) * (1 + pi103) + ((1 - y106)*xod + y106*xo106d) * (1 + pi109),
pi107== ((1 - y107)*xol + y107*xo107l) * (1 + pi107) + ((1 - y107)*xor + y107*xo107r) * (1 + pi107) + ((1 - y107)*xou + y107*xo107u) * (1 + pi104) + ((1 - y107)*xod + y107*xo107d) * (1 + pi110),
pi108== ((1 - y108)*xol + y108*xo108l) * (1 + pi108) + ((1 - y108)*xor + y108*xo108r) * (1 + pi108) + ((1 - y108)*xou + y108*xo108u) * (1 + pi105) + ((1 - y108)*xod + y108*xo108d) * (1 + pi111),
pi109== ((1 - y109)*xol + y109*xo109l) * (1 + pi109) + ((1 - y109)*xor + y109*xo109r) * (1 + pi109) + ((1 - y109)*xou + y109*xo109u) * (1 + pi106) + ((1 - y109)*xod + y109*xo109d) * (1 + pi112),
pi110== ((1 - y110)*xol + y110*xo110l) * (1 + pi110) + ((1 - y110)*xor + y110*xo110r) * (1 + pi110) + ((1 - y110)*xou + y110*xo110u) * (1 + pi107) + ((1 - y110)*xod + y110*xo110d) * (1 + pi113),
pi111== ((1 - y111)*xol + y111*xo111l) * (1 + pi111) + ((1 - y111)*xor + y111*xo111r) * (1 + pi111) + ((1 - y111)*xou + y111*xo111u) * (1 + pi108) + ((1 - y111)*xod + y111*xo111d) * (1 + pi114),
pi112== ((1 - y112)*xol + y112*xo112l) * (1 + pi112) + ((1 - y112)*xor + y112*xo112r) * (1 + pi112) + ((1 - y112)*xou + y112*xo112u) * (1 + pi109) + ((1 - y112)*xod + y112*xo112d) * (1 + pi115),
pi113== ((1 - y113)*xol + y113*xo113l) * (1 + pi113) + ((1 - y113)*xor + y113*xo113r) * (1 + pi113) + ((1 - y113)*xou + y113*xo113u) * (1 + pi110) + ((1 - y113)*xod + y113*xo113d) * (1 + pi116),
pi114== ((1 - y114)*xol + y114*xo114l) * (1 + pi114) + ((1 - y114)*xor + y114*xo114r) * (1 + pi114) + ((1 - y114)*xou + y114*xo114u) * (1 + pi111) + ((1 - y114)*xod + y114*xo114d) * (1 + pi117),
pi115== ((1 - y115)*xol + y115*xo115l) * (1 + pi115) + ((1 - y115)*xor + y115*xo115r) * (1 + pi115) + ((1 - y115)*xou + y115*xo115u) * (1 + pi112) + ((1 - y115)*xod + y115*xo115d) * (1 + pi118),
pi116== ((1 - y116)*xol + y116*xo116l) * (1 + pi116) + ((1 - y116)*xor + y116*xo116r) * (1 + pi116) + ((1 - y116)*xou + y116*xo116u) * (1 + pi113) + ((1 - y116)*xod + y116*xo116d) * (1 + pi119),
pi117== ((1 - y117)*xol + y117*xo117l) * (1 + pi117) + ((1 - y117)*xor + y117*xo117r) * (1 + pi117) + ((1 - y117)*xou + y117*xo117u) * (1 + pi114) + ((1 - y117)*xod + y117*xo117d) * (1 + pi120),
pi118== ((1 - y118)*xol + y118*xo118l) * (1 + pi118) + ((1 - y118)*xor + y118*xo118r) * (1 + pi118) + ((1 - y118)*xou + y118*xo118u) * (1 + pi115) + ((1 - y118)*xod + y118*xo118d) * (1 + pi118), 
pi119 == 0, 
pi120== ((1 - y120)*xol + y120*xo120l) * (1 + pi120) + ((1 - y120)*xor + y120*xo120r) * (1 + pi120) + ((1 - y120)*xou + y120*xo120u) * (1 + pi117) + ((1 - y120)*xod + y120*xo120d) * (1 + pi120), 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= Q(4956,120)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi99+pi100+pi101+pi102+pi103+pi104+pi105+pi106+pi107+pi108+pi109+pi110+pi111+pi112+pi113+pi114+pi115+pi116+pi117+pi118+pi120) * Q(1,120) <= Q(4956,120),
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
xo8l <= 1,
xo8l >= 0,
xo8r <= 1,
xo8r >= 0,
xo8u <= 1,
xo8u >= 0,
xo8d <= 1,
xo8d >= 0,
xo8l + xo8r + xo8u + xo8d == 1,
xo9l <= 1,
xo9l >= 0,
xo9r <= 1,
xo9r >= 0,
xo9u <= 1,
xo9u >= 0,
xo9d <= 1,
xo9d >= 0,
xo9l + xo9r + xo9u + xo9d == 1,
xo10l <= 1,
xo10l >= 0,
xo10r <= 1,
xo10r >= 0,
xo10u <= 1,
xo10u >= 0,
xo10d <= 1,
xo10d >= 0,
xo10l + xo10r + xo10u + xo10d == 1,
xo11l <= 1,
xo11l >= 0,
xo11r <= 1,
xo11r >= 0,
xo11u <= 1,
xo11u >= 0,
xo11d <= 1,
xo11d >= 0,
xo11l + xo11r + xo11u + xo11d == 1,
xo12l <= 1,
xo12l >= 0,
xo12r <= 1,
xo12r >= 0,
xo12u <= 1,
xo12u >= 0,
xo12d <= 1,
xo12d >= 0,
xo12l + xo12r + xo12u + xo12d == 1,
xo13l <= 1,
xo13l >= 0,
xo13r <= 1,
xo13r >= 0,
xo13u <= 1,
xo13u >= 0,
xo13d <= 1,
xo13d >= 0,
xo13l + xo13r + xo13u + xo13d == 1,
xo14l <= 1,
xo14l >= 0,
xo14r <= 1,
xo14r >= 0,
xo14u <= 1,
xo14u >= 0,
xo14d <= 1,
xo14d >= 0,
xo14l + xo14r + xo14u + xo14d == 1,
xo15l <= 1,
xo15l >= 0,
xo15r <= 1,
xo15r >= 0,
xo15u <= 1,
xo15u >= 0,
xo15d <= 1,
xo15d >= 0,
xo15l + xo15r + xo15u + xo15d == 1,
xo16l <= 1,
xo16l >= 0,
xo16r <= 1,
xo16r >= 0,
xo16u <= 1,
xo16u >= 0,
xo16d <= 1,
xo16d >= 0,
xo16l + xo16r + xo16u + xo16d == 1,
xo17l <= 1,
xo17l >= 0,
xo17r <= 1,
xo17r >= 0,
xo17u <= 1,
xo17u >= 0,
xo17d <= 1,
xo17d >= 0,
xo17l + xo17r + xo17u + xo17d == 1,
xo18l <= 1,
xo18l >= 0,
xo18r <= 1,
xo18r >= 0,
xo18u <= 1,
xo18u >= 0,
xo18d <= 1,
xo18d >= 0,
xo18l + xo18r + xo18u + xo18d == 1,
xo19l <= 1,
xo19l >= 0,
xo19r <= 1,
xo19r >= 0,
xo19u <= 1,
xo19u >= 0,
xo19d <= 1,
xo19d >= 0,
xo19l + xo19r + xo19u + xo19d == 1,
xo20l <= 1,
xo20l >= 0,
xo20r <= 1,
xo20r >= 0,
xo20u <= 1,
xo20u >= 0,
xo20d <= 1,
xo20d >= 0,
xo20l + xo20r + xo20u + xo20d == 1,
xo21l <= 1,
xo21l >= 0,
xo21r <= 1,
xo21r >= 0,
xo21u <= 1,
xo21u >= 0,
xo21d <= 1,
xo21d >= 0,
xo21l + xo21r + xo21u + xo21d == 1,
xo22l <= 1,
xo22l >= 0,
xo22r <= 1,
xo22r >= 0,
xo22u <= 1,
xo22u >= 0,
xo22d <= 1,
xo22d >= 0,
xo22l + xo22r + xo22u + xo22d == 1,
xo23l <= 1,
xo23l >= 0,
xo23r <= 1,
xo23r >= 0,
xo23u <= 1,
xo23u >= 0,
xo23d <= 1,
xo23d >= 0,
xo23l + xo23r + xo23u + xo23d == 1,
xo24l <= 1,
xo24l >= 0,
xo24r <= 1,
xo24r >= 0,
xo24u <= 1,
xo24u >= 0,
xo24d <= 1,
xo24d >= 0,
xo24l + xo24r + xo24u + xo24d == 1,
xo25l <= 1,
xo25l >= 0,
xo25r <= 1,
xo25r >= 0,
xo25u <= 1,
xo25u >= 0,
xo25d <= 1,
xo25d >= 0,
xo25l + xo25r + xo25u + xo25d == 1,
xo26l <= 1,
xo26l >= 0,
xo26r <= 1,
xo26r >= 0,
xo26u <= 1,
xo26u >= 0,
xo26d <= 1,
xo26d >= 0,
xo26l + xo26r + xo26u + xo26d == 1,
xo27l <= 1,
xo27l >= 0,
xo27r <= 1,
xo27r >= 0,
xo27u <= 1,
xo27u >= 0,
xo27d <= 1,
xo27d >= 0,
xo27l + xo27r + xo27u + xo27d == 1,
xo28l <= 1,
xo28l >= 0,
xo28r <= 1,
xo28r >= 0,
xo28u <= 1,
xo28u >= 0,
xo28d <= 1,
xo28d >= 0,
xo28l + xo28r + xo28u + xo28d == 1,
xo29l <= 1,
xo29l >= 0,
xo29r <= 1,
xo29r >= 0,
xo29u <= 1,
xo29u >= 0,
xo29d <= 1,
xo29d >= 0,
xo29l + xo29r + xo29u + xo29d == 1,
xo30l <= 1,
xo30l >= 0,
xo30r <= 1,
xo30r >= 0,
xo30u <= 1,
xo30u >= 0,
xo30d <= 1,
xo30d >= 0,
xo30l + xo30r + xo30u + xo30d == 1,
xo31l <= 1,
xo31l >= 0,
xo31r <= 1,
xo31r >= 0,
xo31u <= 1,
xo31u >= 0,
xo31d <= 1,
xo31d >= 0,
xo31l + xo31r + xo31u + xo31d == 1,
xo32l <= 1,
xo32l >= 0,
xo32r <= 1,
xo32r >= 0,
xo32u <= 1,
xo32u >= 0,
xo32d <= 1,
xo32d >= 0,
xo32l + xo32r + xo32u + xo32d == 1,
xo33l <= 1,
xo33l >= 0,
xo33r <= 1,
xo33r >= 0,
xo33u <= 1,
xo33u >= 0,
xo33d <= 1,
xo33d >= 0,
xo33l + xo33r + xo33u + xo33d == 1,
xo34l <= 1,
xo34l >= 0,
xo34r <= 1,
xo34r >= 0,
xo34u <= 1,
xo34u >= 0,
xo34d <= 1,
xo34d >= 0,
xo34l + xo34r + xo34u + xo34d == 1,
xo35l <= 1,
xo35l >= 0,
xo35r <= 1,
xo35r >= 0,
xo35u <= 1,
xo35u >= 0,
xo35d <= 1,
xo35d >= 0,
xo35l + xo35r + xo35u + xo35d == 1,
xo36l <= 1,
xo36l >= 0,
xo36r <= 1,
xo36r >= 0,
xo36u <= 1,
xo36u >= 0,
xo36d <= 1,
xo36d >= 0,
xo36l + xo36r + xo36u + xo36d == 1,
xo37l <= 1,
xo37l >= 0,
xo37r <= 1,
xo37r >= 0,
xo37u <= 1,
xo37u >= 0,
xo37d <= 1,
xo37d >= 0,
xo37l + xo37r + xo37u + xo37d == 1,
xo38l <= 1,
xo38l >= 0,
xo38r <= 1,
xo38r >= 0,
xo38u <= 1,
xo38u >= 0,
xo38d <= 1,
xo38d >= 0,
xo38l + xo38r + xo38u + xo38d == 1,
xo39l <= 1,
xo39l >= 0,
xo39r <= 1,
xo39r >= 0,
xo39u <= 1,
xo39u >= 0,
xo39d <= 1,
xo39d >= 0,
xo39l + xo39r + xo39u + xo39d == 1,
xo40l <= 1,
xo40l >= 0,
xo40r <= 1,
xo40r >= 0,
xo40u <= 1,
xo40u >= 0,
xo40d <= 1,
xo40d >= 0,
xo40l + xo40r + xo40u + xo40d == 1,
xo41l <= 1,
xo41l >= 0,
xo41r <= 1,
xo41r >= 0,
xo41u <= 1,
xo41u >= 0,
xo41d <= 1,
xo41d >= 0,
xo41l + xo41r + xo41u + xo41d == 1,
xo42l <= 1,
xo42l >= 0,
xo42r <= 1,
xo42r >= 0,
xo42u <= 1,
xo42u >= 0,
xo42d <= 1,
xo42d >= 0,
xo42l + xo42r + xo42u + xo42d == 1,
xo43l <= 1,
xo43l >= 0,
xo43r <= 1,
xo43r >= 0,
xo43u <= 1,
xo43u >= 0,
xo43d <= 1,
xo43d >= 0,
xo43l + xo43r + xo43u + xo43d == 1,
xo44l <= 1,
xo44l >= 0,
xo44r <= 1,
xo44r >= 0,
xo44u <= 1,
xo44u >= 0,
xo44d <= 1,
xo44d >= 0,
xo44l + xo44r + xo44u + xo44d == 1,
xo45l <= 1,
xo45l >= 0,
xo45r <= 1,
xo45r >= 0,
xo45u <= 1,
xo45u >= 0,
xo45d <= 1,
xo45d >= 0,
xo45l + xo45r + xo45u + xo45d == 1,
xo46l <= 1,
xo46l >= 0,
xo46r <= 1,
xo46r >= 0,
xo46u <= 1,
xo46u >= 0,
xo46d <= 1,
xo46d >= 0,
xo46l + xo46r + xo46u + xo46d == 1,
xo47l <= 1,
xo47l >= 0,
xo47r <= 1,
xo47r >= 0,
xo47u <= 1,
xo47u >= 0,
xo47d <= 1,
xo47d >= 0,
xo47l + xo47r + xo47u + xo47d == 1,
xo48l <= 1,
xo48l >= 0,
xo48r <= 1,
xo48r >= 0,
xo48u <= 1,
xo48u >= 0,
xo48d <= 1,
xo48d >= 0,
xo48l + xo48r + xo48u + xo48d == 1,
xo49l <= 1,
xo49l >= 0,
xo49r <= 1,
xo49r >= 0,
xo49u <= 1,
xo49u >= 0,
xo49d <= 1,
xo49d >= 0,
xo49l + xo49r + xo49u + xo49d == 1,
xo50l <= 1,
xo50l >= 0,
xo50r <= 1,
xo50r >= 0,
xo50u <= 1,
xo50u >= 0,
xo50d <= 1,
xo50d >= 0,
xo50l + xo50r + xo50u + xo50d == 1,
xo51l <= 1,
xo51l >= 0,
xo51r <= 1,
xo51r >= 0,
xo51u <= 1,
xo51u >= 0,
xo51d <= 1,
xo51d >= 0,
xo51l + xo51r + xo51u + xo51d == 1,
xo52l <= 1,
xo52l >= 0,
xo52r <= 1,
xo52r >= 0,
xo52u <= 1,
xo52u >= 0,
xo52d <= 1,
xo52d >= 0,
xo52l + xo52r + xo52u + xo52d == 1,
xo53l <= 1,
xo53l >= 0,
xo53r <= 1,
xo53r >= 0,
xo53u <= 1,
xo53u >= 0,
xo53d <= 1,
xo53d >= 0,
xo53l + xo53r + xo53u + xo53d == 1,
xo54l <= 1,
xo54l >= 0,
xo54r <= 1,
xo54r >= 0,
xo54u <= 1,
xo54u >= 0,
xo54d <= 1,
xo54d >= 0,
xo54l + xo54r + xo54u + xo54d == 1,
xo55l <= 1,
xo55l >= 0,
xo55r <= 1,
xo55r >= 0,
xo55u <= 1,
xo55u >= 0,
xo55d <= 1,
xo55d >= 0,
xo55l + xo55r + xo55u + xo55d == 1,
xo56l <= 1,
xo56l >= 0,
xo56r <= 1,
xo56r >= 0,
xo56u <= 1,
xo56u >= 0,
xo56d <= 1,
xo56d >= 0,
xo56l + xo56r + xo56u + xo56d == 1,
xo57l <= 1,
xo57l >= 0,
xo57r <= 1,
xo57r >= 0,
xo57u <= 1,
xo57u >= 0,
xo57d <= 1,
xo57d >= 0,
xo57l + xo57r + xo57u + xo57d == 1,
xo58l <= 1,
xo58l >= 0,
xo58r <= 1,
xo58r >= 0,
xo58u <= 1,
xo58u >= 0,
xo58d <= 1,
xo58d >= 0,
xo58l + xo58r + xo58u + xo58d == 1,
xo59l <= 1,
xo59l >= 0,
xo59r <= 1,
xo59r >= 0,
xo59u <= 1,
xo59u >= 0,
xo59d <= 1,
xo59d >= 0,
xo59l + xo59r + xo59u + xo59d == 1,
xo60l <= 1,
xo60l >= 0,
xo60r <= 1,
xo60r >= 0,
xo60u <= 1,
xo60u >= 0,
xo60d <= 1,
xo60d >= 0,
xo60l + xo60r + xo60u + xo60d == 1,
xo61l <= 1,
xo61l >= 0,
xo61r <= 1,
xo61r >= 0,
xo61u <= 1,
xo61u >= 0,
xo61d <= 1,
xo61d >= 0,
xo61l + xo61r + xo61u + xo61d == 1,
xo62l <= 1,
xo62l >= 0,
xo62r <= 1,
xo62r >= 0,
xo62u <= 1,
xo62u >= 0,
xo62d <= 1,
xo62d >= 0,
xo62l + xo62r + xo62u + xo62d == 1,
xo63l <= 1,
xo63l >= 0,
xo63r <= 1,
xo63r >= 0,
xo63u <= 1,
xo63u >= 0,
xo63d <= 1,
xo63d >= 0,
xo63l + xo63r + xo63u + xo63d == 1,
xo64l <= 1,
xo64l >= 0,
xo64r <= 1,
xo64r >= 0,
xo64u <= 1,
xo64u >= 0,
xo64d <= 1,
xo64d >= 0,
xo64l + xo64r + xo64u + xo64d == 1,
xo65l <= 1,
xo65l >= 0,
xo65r <= 1,
xo65r >= 0,
xo65u <= 1,
xo65u >= 0,
xo65d <= 1,
xo65d >= 0,
xo65l + xo65r + xo65u + xo65d == 1,
xo66l <= 1,
xo66l >= 0,
xo66r <= 1,
xo66r >= 0,
xo66u <= 1,
xo66u >= 0,
xo66d <= 1,
xo66d >= 0,
xo66l + xo66r + xo66u + xo66d == 1,
xo67l <= 1,
xo67l >= 0,
xo67r <= 1,
xo67r >= 0,
xo67u <= 1,
xo67u >= 0,
xo67d <= 1,
xo67d >= 0,
xo67l + xo67r + xo67u + xo67d == 1,
xo68l <= 1,
xo68l >= 0,
xo68r <= 1,
xo68r >= 0,
xo68u <= 1,
xo68u >= 0,
xo68d <= 1,
xo68d >= 0,
xo68l + xo68r + xo68u + xo68d == 1,
xo69l <= 1,
xo69l >= 0,
xo69r <= 1,
xo69r >= 0,
xo69u <= 1,
xo69u >= 0,
xo69d <= 1,
xo69d >= 0,
xo69l + xo69r + xo69u + xo69d == 1,
xo70l <= 1,
xo70l >= 0,
xo70r <= 1,
xo70r >= 0,
xo70u <= 1,
xo70u >= 0,
xo70d <= 1,
xo70d >= 0,
xo70l + xo70r + xo70u + xo70d == 1,
xo71l <= 1,
xo71l >= 0,
xo71r <= 1,
xo71r >= 0,
xo71u <= 1,
xo71u >= 0,
xo71d <= 1,
xo71d >= 0,
xo71l + xo71r + xo71u + xo71d == 1,
xo72l <= 1,
xo72l >= 0,
xo72r <= 1,
xo72r >= 0,
xo72u <= 1,
xo72u >= 0,
xo72d <= 1,
xo72d >= 0,
xo72l + xo72r + xo72u + xo72d == 1,
xo73l <= 1,
xo73l >= 0,
xo73r <= 1,
xo73r >= 0,
xo73u <= 1,
xo73u >= 0,
xo73d <= 1,
xo73d >= 0,
xo73l + xo73r + xo73u + xo73d == 1,
xo74l <= 1,
xo74l >= 0,
xo74r <= 1,
xo74r >= 0,
xo74u <= 1,
xo74u >= 0,
xo74d <= 1,
xo74d >= 0,
xo74l + xo74r + xo74u + xo74d == 1,
xo75l <= 1,
xo75l >= 0,
xo75r <= 1,
xo75r >= 0,
xo75u <= 1,
xo75u >= 0,
xo75d <= 1,
xo75d >= 0,
xo75l + xo75r + xo75u + xo75d == 1,
xo76l <= 1,
xo76l >= 0,
xo76r <= 1,
xo76r >= 0,
xo76u <= 1,
xo76u >= 0,
xo76d <= 1,
xo76d >= 0,
xo76l + xo76r + xo76u + xo76d == 1,
xo77l <= 1,
xo77l >= 0,
xo77r <= 1,
xo77r >= 0,
xo77u <= 1,
xo77u >= 0,
xo77d <= 1,
xo77d >= 0,
xo77l + xo77r + xo77u + xo77d == 1,
xo78l <= 1,
xo78l >= 0,
xo78r <= 1,
xo78r >= 0,
xo78u <= 1,
xo78u >= 0,
xo78d <= 1,
xo78d >= 0,
xo78l + xo78r + xo78u + xo78d == 1,
xo79l <= 1,
xo79l >= 0,
xo79r <= 1,
xo79r >= 0,
xo79u <= 1,
xo79u >= 0,
xo79d <= 1,
xo79d >= 0,
xo79l + xo79r + xo79u + xo79d == 1,
xo80l <= 1,
xo80l >= 0,
xo80r <= 1,
xo80r >= 0,
xo80u <= 1,
xo80u >= 0,
xo80d <= 1,
xo80d >= 0,
xo80l + xo80r + xo80u + xo80d == 1,
xo81l <= 1,
xo81l >= 0,
xo81r <= 1,
xo81r >= 0,
xo81u <= 1,
xo81u >= 0,
xo81d <= 1,
xo81d >= 0,
xo81l + xo81r + xo81u + xo81d == 1,
xo82l <= 1,
xo82l >= 0,
xo82r <= 1,
xo82r >= 0,
xo82u <= 1,
xo82u >= 0,
xo82d <= 1,
xo82d >= 0,
xo82l + xo82r + xo82u + xo82d == 1,
xo83l <= 1,
xo83l >= 0,
xo83r <= 1,
xo83r >= 0,
xo83u <= 1,
xo83u >= 0,
xo83d <= 1,
xo83d >= 0,
xo83l + xo83r + xo83u + xo83d == 1,
xo84l <= 1,
xo84l >= 0,
xo84r <= 1,
xo84r >= 0,
xo84u <= 1,
xo84u >= 0,
xo84d <= 1,
xo84d >= 0,
xo84l + xo84r + xo84u + xo84d == 1,
xo85l <= 1,
xo85l >= 0,
xo85r <= 1,
xo85r >= 0,
xo85u <= 1,
xo85u >= 0,
xo85d <= 1,
xo85d >= 0,
xo85l + xo85r + xo85u + xo85d == 1,
xo86l <= 1,
xo86l >= 0,
xo86r <= 1,
xo86r >= 0,
xo86u <= 1,
xo86u >= 0,
xo86d <= 1,
xo86d >= 0,
xo86l + xo86r + xo86u + xo86d == 1,
xo87l <= 1,
xo87l >= 0,
xo87r <= 1,
xo87r >= 0,
xo87u <= 1,
xo87u >= 0,
xo87d <= 1,
xo87d >= 0,
xo87l + xo87r + xo87u + xo87d == 1,
xo88l <= 1,
xo88l >= 0,
xo88r <= 1,
xo88r >= 0,
xo88u <= 1,
xo88u >= 0,
xo88d <= 1,
xo88d >= 0,
xo88l + xo88r + xo88u + xo88d == 1,
xo89l <= 1,
xo89l >= 0,
xo89r <= 1,
xo89r >= 0,
xo89u <= 1,
xo89u >= 0,
xo89d <= 1,
xo89d >= 0,
xo89l + xo89r + xo89u + xo89d == 1,
xo90l <= 1,
xo90l >= 0,
xo90r <= 1,
xo90r >= 0,
xo90u <= 1,
xo90u >= 0,
xo90d <= 1,
xo90d >= 0,
xo90l + xo90r + xo90u + xo90d == 1,
xo91l <= 1,
xo91l >= 0,
xo91r <= 1,
xo91r >= 0,
xo91u <= 1,
xo91u >= 0,
xo91d <= 1,
xo91d >= 0,
xo91l + xo91r + xo91u + xo91d == 1,
xo92l <= 1,
xo92l >= 0,
xo92r <= 1,
xo92r >= 0,
xo92u <= 1,
xo92u >= 0,
xo92d <= 1,
xo92d >= 0,
xo92l + xo92r + xo92u + xo92d == 1,
xo93l <= 1,
xo93l >= 0,
xo93r <= 1,
xo93r >= 0,
xo93u <= 1,
xo93u >= 0,
xo93d <= 1,
xo93d >= 0,
xo93l + xo93r + xo93u + xo93d == 1,
xo94l <= 1,
xo94l >= 0,
xo94r <= 1,
xo94r >= 0,
xo94u <= 1,
xo94u >= 0,
xo94d <= 1,
xo94d >= 0,
xo94l + xo94r + xo94u + xo94d == 1,
xo95l <= 1,
xo95l >= 0,
xo95r <= 1,
xo95r >= 0,
xo95u <= 1,
xo95u >= 0,
xo95d <= 1,
xo95d >= 0,
xo95l + xo95r + xo95u + xo95d == 1,
xo96l <= 1,
xo96l >= 0,
xo96r <= 1,
xo96r >= 0,
xo96u <= 1,
xo96u >= 0,
xo96d <= 1,
xo96d >= 0,
xo96l + xo96r + xo96u + xo96d == 1,
xo97l <= 1,
xo97l >= 0,
xo97r <= 1,
xo97r >= 0,
xo97u <= 1,
xo97u >= 0,
xo97d <= 1,
xo97d >= 0,
xo97l + xo97r + xo97u + xo97d == 1,
xo98l <= 1,
xo98l >= 0,
xo98r <= 1,
xo98r >= 0,
xo98u <= 1,
xo98u >= 0,
xo98d <= 1,
xo98d >= 0,
xo98l + xo98r + xo98u + xo98d == 1,
xo99l <= 1,
xo99l >= 0,
xo99r <= 1,
xo99r >= 0,
xo99u <= 1,
xo99u >= 0,
xo99d <= 1,
xo99d >= 0,
xo99l + xo99r + xo99u + xo99d == 1,
xo100l <= 1,
xo100l >= 0,
xo100r <= 1,
xo100r >= 0,
xo100u <= 1,
xo100u >= 0,
xo100d <= 1,
xo100d >= 0,
xo100l + xo100r + xo100u + xo100d == 1,
xo101l <= 1,
xo101l >= 0,
xo101r <= 1,
xo101r >= 0,
xo101u <= 1,
xo101u >= 0,
xo101d <= 1,
xo101d >= 0,
xo101l + xo101r + xo101u + xo101d == 1,
xo102l <= 1,
xo102l >= 0,
xo102r <= 1,
xo102r >= 0,
xo102u <= 1,
xo102u >= 0,
xo102d <= 1,
xo102d >= 0,
xo102l + xo102r + xo102u + xo102d == 1,
xo103l <= 1,
xo103l >= 0,
xo103r <= 1,
xo103r >= 0,
xo103u <= 1,
xo103u >= 0,
xo103d <= 1,
xo103d >= 0,
xo103l + xo103r + xo103u + xo103d == 1,
xo104l <= 1,
xo104l >= 0,
xo104r <= 1,
xo104r >= 0,
xo104u <= 1,
xo104u >= 0,
xo104d <= 1,
xo104d >= 0,
xo104l + xo104r + xo104u + xo104d == 1,
xo105l <= 1,
xo105l >= 0,
xo105r <= 1,
xo105r >= 0,
xo105u <= 1,
xo105u >= 0,
xo105d <= 1,
xo105d >= 0,
xo105l + xo105r + xo105u + xo105d == 1,
xo106l <= 1,
xo106l >= 0,
xo106r <= 1,
xo106r >= 0,
xo106u <= 1,
xo106u >= 0,
xo106d <= 1,
xo106d >= 0,
xo106l + xo106r + xo106u + xo106d == 1,
xo107l <= 1,
xo107l >= 0,
xo107r <= 1,
xo107r >= 0,
xo107u <= 1,
xo107u >= 0,
xo107d <= 1,
xo107d >= 0,
xo107l + xo107r + xo107u + xo107d == 1,
xo108l <= 1,
xo108l >= 0,
xo108r <= 1,
xo108r >= 0,
xo108u <= 1,
xo108u >= 0,
xo108d <= 1,
xo108d >= 0,
xo108l + xo108r + xo108u + xo108d == 1,
xo109l <= 1,
xo109l >= 0,
xo109r <= 1,
xo109r >= 0,
xo109u <= 1,
xo109u >= 0,
xo109d <= 1,
xo109d >= 0,
xo109l + xo109r + xo109u + xo109d == 1,
xo110l <= 1,
xo110l >= 0,
xo110r <= 1,
xo110r >= 0,
xo110u <= 1,
xo110u >= 0,
xo110d <= 1,
xo110d >= 0,
xo110l + xo110r + xo110u + xo110d == 1,
xo111l <= 1,
xo111l >= 0,
xo111r <= 1,
xo111r >= 0,
xo111u <= 1,
xo111u >= 0,
xo111d <= 1,
xo111d >= 0,
xo111l + xo111r + xo111u + xo111d == 1,
xo112l <= 1,
xo112l >= 0,
xo112r <= 1,
xo112r >= 0,
xo112u <= 1,
xo112u >= 0,
xo112d <= 1,
xo112d >= 0,
xo112l + xo112r + xo112u + xo112d == 1,
xo113l <= 1,
xo113l >= 0,
xo113r <= 1,
xo113r >= 0,
xo113u <= 1,
xo113u >= 0,
xo113d <= 1,
xo113d >= 0,
xo113l + xo113r + xo113u + xo113d == 1,
xo114l <= 1,
xo114l >= 0,
xo114r <= 1,
xo114r >= 0,
xo114u <= 1,
xo114u >= 0,
xo114d <= 1,
xo114d >= 0,
xo114l + xo114r + xo114u + xo114d == 1,
xo115l <= 1,
xo115l >= 0,
xo115r <= 1,
xo115r >= 0,
xo115u <= 1,
xo115u >= 0,
xo115d <= 1,
xo115d >= 0,
xo115l + xo115r + xo115u + xo115d == 1,
xo116l <= 1,
xo116l >= 0,
xo116r <= 1,
xo116r >= 0,
xo116u <= 1,
xo116u >= 0,
xo116d <= 1,
xo116d >= 0,
xo116l + xo116r + xo116u + xo116d == 1,
xo117l <= 1,
xo117l >= 0,
xo117r <= 1,
xo117r >= 0,
xo117u <= 1,
xo117u >= 0,
xo117d <= 1,
xo117d >= 0,
xo117l + xo117r + xo117u + xo117d == 1,
xo118l <= 1,
xo118l >= 0,
xo118r <= 1,
xo118r >= 0,
xo118u <= 1,
xo118u >= 0,
xo118d <= 1,
xo118d >= 0,
xo118l + xo118r + xo118u + xo118d == 1,
xo119l <= 1,
xo119l >= 0,
xo119r <= 1,
xo119r >= 0,
xo119u <= 1,
xo119u >= 0,
xo119d <= 1,
xo119d >= 0,
xo119l + xo119r + xo119u + xo119d == 1,
xo120l <= 1,
xo120l >= 0,
xo120r <= 1,
xo120r >= 0,
xo120u <= 1,
xo120u >= 0,
xo120d <= 1,
xo120d >= 0,
xo120l + xo120r + xo120u + xo120d == 1,
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
Or(xo8l == 0 , xo8l == 1),
Or(xo8r == 0 , xo8r == 1),
Or(xo8u == 0 , xo8u == 1),
Or(xo8d == 0 , xo8d == 1),
Or(xo9l == 0 , xo9l == 1),
Or(xo9r == 0 , xo9r == 1),
Or(xo9u == 0 , xo9u == 1),
Or(xo9d == 0 , xo9d == 1),
Or(xo10l == 0 , xo10l == 1),
Or(xo10r == 0 , xo10r == 1),
Or(xo10u == 0 , xo10u == 1),
Or(xo10d == 0 , xo10d == 1),
Or(xo11l == 0 , xo11l == 1),
Or(xo11r == 0 , xo11r == 1),
Or(xo11u == 0 , xo11u == 1),
Or(xo11d == 0 , xo11d == 1),
Or(xo12l == 0 , xo12l == 1),
Or(xo12r == 0 , xo12r == 1),
Or(xo12u == 0 , xo12u == 1),
Or(xo12d == 0 , xo12d == 1),
Or(xo13l == 0 , xo13l == 1),
Or(xo13r == 0 , xo13r == 1),
Or(xo13u == 0 , xo13u == 1),
Or(xo13d == 0 , xo13d == 1),
Or(xo14l == 0 , xo14l == 1),
Or(xo14r == 0 , xo14r == 1),
Or(xo14u == 0 , xo14u == 1),
Or(xo14d == 0 , xo14d == 1),
Or(xo15l == 0 , xo15l == 1),
Or(xo15r == 0 , xo15r == 1),
Or(xo15u == 0 , xo15u == 1),
Or(xo15d == 0 , xo15d == 1),
Or(xo16l == 0 , xo16l == 1),
Or(xo16r == 0 , xo16r == 1),
Or(xo16u == 0 , xo16u == 1),
Or(xo16d == 0 , xo16d == 1),
Or(xo17l == 0 , xo17l == 1),
Or(xo17r == 0 , xo17r == 1),
Or(xo17u == 0 , xo17u == 1),
Or(xo17d == 0 , xo17d == 1),
Or(xo18l == 0 , xo18l == 1),
Or(xo18r == 0 , xo18r == 1),
Or(xo18u == 0 , xo18u == 1),
Or(xo18d == 0 , xo18d == 1),
Or(xo19l == 0 , xo19l == 1),
Or(xo19r == 0 , xo19r == 1),
Or(xo19u == 0 , xo19u == 1),
Or(xo19d == 0 , xo19d == 1),
Or(xo20l == 0 , xo20l == 1),
Or(xo20r == 0 , xo20r == 1),
Or(xo20u == 0 , xo20u == 1),
Or(xo20d == 0 , xo20d == 1),
Or(xo21l == 0 , xo21l == 1),
Or(xo21r == 0 , xo21r == 1),
Or(xo21u == 0 , xo21u == 1),
Or(xo21d == 0 , xo21d == 1),
Or(xo22l == 0 , xo22l == 1),
Or(xo22r == 0 , xo22r == 1),
Or(xo22u == 0 , xo22u == 1),
Or(xo22d == 0 , xo22d == 1),
Or(xo23l == 0 , xo23l == 1),
Or(xo23r == 0 , xo23r == 1),
Or(xo23u == 0 , xo23u == 1),
Or(xo23d == 0 , xo23d == 1),
Or(xo24l == 0 , xo24l == 1),
Or(xo24r == 0 , xo24r == 1),
Or(xo24u == 0 , xo24u == 1),
Or(xo24d == 0 , xo24d == 1),
Or(xo25l == 0 , xo25l == 1),
Or(xo25r == 0 , xo25r == 1),
Or(xo25u == 0 , xo25u == 1),
Or(xo25d == 0 , xo25d == 1),
Or(xo26l == 0 , xo26l == 1),
Or(xo26r == 0 , xo26r == 1),
Or(xo26u == 0 , xo26u == 1),
Or(xo26d == 0 , xo26d == 1),
Or(xo27l == 0 , xo27l == 1),
Or(xo27r == 0 , xo27r == 1),
Or(xo27u == 0 , xo27u == 1),
Or(xo27d == 0 , xo27d == 1),
Or(xo28l == 0 , xo28l == 1),
Or(xo28r == 0 , xo28r == 1),
Or(xo28u == 0 , xo28u == 1),
Or(xo28d == 0 , xo28d == 1),
Or(xo29l == 0 , xo29l == 1),
Or(xo29r == 0 , xo29r == 1),
Or(xo29u == 0 , xo29u == 1),
Or(xo29d == 0 , xo29d == 1),
Or(xo30l == 0 , xo30l == 1),
Or(xo30r == 0 , xo30r == 1),
Or(xo30u == 0 , xo30u == 1),
Or(xo30d == 0 , xo30d == 1),
Or(xo31l == 0 , xo31l == 1),
Or(xo31r == 0 , xo31r == 1),
Or(xo31u == 0 , xo31u == 1),
Or(xo31d == 0 , xo31d == 1),
Or(xo32l == 0 , xo32l == 1),
Or(xo32r == 0 , xo32r == 1),
Or(xo32u == 0 , xo32u == 1),
Or(xo32d == 0 , xo32d == 1),
Or(xo33l == 0 , xo33l == 1),
Or(xo33r == 0 , xo33r == 1),
Or(xo33u == 0 , xo33u == 1),
Or(xo33d == 0 , xo33d == 1),
Or(xo34l == 0 , xo34l == 1),
Or(xo34r == 0 , xo34r == 1),
Or(xo34u == 0 , xo34u == 1),
Or(xo34d == 0 , xo34d == 1),
Or(xo35l == 0 , xo35l == 1),
Or(xo35r == 0 , xo35r == 1),
Or(xo35u == 0 , xo35u == 1),
Or(xo35d == 0 , xo35d == 1),
Or(xo36l == 0 , xo36l == 1),
Or(xo36r == 0 , xo36r == 1),
Or(xo36u == 0 , xo36u == 1),
Or(xo36d == 0 , xo36d == 1),
Or(xo37l == 0 , xo37l == 1),
Or(xo37r == 0 , xo37r == 1),
Or(xo37u == 0 , xo37u == 1),
Or(xo37d == 0 , xo37d == 1),
Or(xo38l == 0 , xo38l == 1),
Or(xo38r == 0 , xo38r == 1),
Or(xo38u == 0 , xo38u == 1),
Or(xo38d == 0 , xo38d == 1),
Or(xo39l == 0 , xo39l == 1),
Or(xo39r == 0 , xo39r == 1),
Or(xo39u == 0 , xo39u == 1),
Or(xo39d == 0 , xo39d == 1),
Or(xo40l == 0 , xo40l == 1),
Or(xo40r == 0 , xo40r == 1),
Or(xo40u == 0 , xo40u == 1),
Or(xo40d == 0 , xo40d == 1),
Or(xo41l == 0 , xo41l == 1),
Or(xo41r == 0 , xo41r == 1),
Or(xo41u == 0 , xo41u == 1),
Or(xo41d == 0 , xo41d == 1),
Or(xo42l == 0 , xo42l == 1),
Or(xo42r == 0 , xo42r == 1),
Or(xo42u == 0 , xo42u == 1),
Or(xo42d == 0 , xo42d == 1),
Or(xo43l == 0 , xo43l == 1),
Or(xo43r == 0 , xo43r == 1),
Or(xo43u == 0 , xo43u == 1),
Or(xo43d == 0 , xo43d == 1),
Or(xo44l == 0 , xo44l == 1),
Or(xo44r == 0 , xo44r == 1),
Or(xo44u == 0 , xo44u == 1),
Or(xo44d == 0 , xo44d == 1),
Or(xo45l == 0 , xo45l == 1),
Or(xo45r == 0 , xo45r == 1),
Or(xo45u == 0 , xo45u == 1),
Or(xo45d == 0 , xo45d == 1),
Or(xo46l == 0 , xo46l == 1),
Or(xo46r == 0 , xo46r == 1),
Or(xo46u == 0 , xo46u == 1),
Or(xo46d == 0 , xo46d == 1),
Or(xo47l == 0 , xo47l == 1),
Or(xo47r == 0 , xo47r == 1),
Or(xo47u == 0 , xo47u == 1),
Or(xo47d == 0 , xo47d == 1),
Or(xo48l == 0 , xo48l == 1),
Or(xo48r == 0 , xo48r == 1),
Or(xo48u == 0 , xo48u == 1),
Or(xo48d == 0 , xo48d == 1),
Or(xo49l == 0 , xo49l == 1),
Or(xo49r == 0 , xo49r == 1),
Or(xo49u == 0 , xo49u == 1),
Or(xo49d == 0 , xo49d == 1),
Or(xo50l == 0 , xo50l == 1),
Or(xo50r == 0 , xo50r == 1),
Or(xo50u == 0 , xo50u == 1),
Or(xo50d == 0 , xo50d == 1),
Or(xo51l == 0 , xo51l == 1),
Or(xo51r == 0 , xo51r == 1),
Or(xo51u == 0 , xo51u == 1),
Or(xo51d == 0 , xo51d == 1),
Or(xo52l == 0 , xo52l == 1),
Or(xo52r == 0 , xo52r == 1),
Or(xo52u == 0 , xo52u == 1),
Or(xo52d == 0 , xo52d == 1),
Or(xo53l == 0 , xo53l == 1),
Or(xo53r == 0 , xo53r == 1),
Or(xo53u == 0 , xo53u == 1),
Or(xo53d == 0 , xo53d == 1),
Or(xo54l == 0 , xo54l == 1),
Or(xo54r == 0 , xo54r == 1),
Or(xo54u == 0 , xo54u == 1),
Or(xo54d == 0 , xo54d == 1),
Or(xo55l == 0 , xo55l == 1),
Or(xo55r == 0 , xo55r == 1),
Or(xo55u == 0 , xo55u == 1),
Or(xo55d == 0 , xo55d == 1),
Or(xo56l == 0 , xo56l == 1),
Or(xo56r == 0 , xo56r == 1),
Or(xo56u == 0 , xo56u == 1),
Or(xo56d == 0 , xo56d == 1),
Or(xo57l == 0 , xo57l == 1),
Or(xo57r == 0 , xo57r == 1),
Or(xo57u == 0 , xo57u == 1),
Or(xo57d == 0 , xo57d == 1),
Or(xo58l == 0 , xo58l == 1),
Or(xo58r == 0 , xo58r == 1),
Or(xo58u == 0 , xo58u == 1),
Or(xo58d == 0 , xo58d == 1),
Or(xo59l == 0 , xo59l == 1),
Or(xo59r == 0 , xo59r == 1),
Or(xo59u == 0 , xo59u == 1),
Or(xo59d == 0 , xo59d == 1),
Or(xo60l == 0 , xo60l == 1),
Or(xo60r == 0 , xo60r == 1),
Or(xo60u == 0 , xo60u == 1),
Or(xo60d == 0 , xo60d == 1),
Or(xo61l == 0 , xo61l == 1),
Or(xo61r == 0 , xo61r == 1),
Or(xo61u == 0 , xo61u == 1),
Or(xo61d == 0 , xo61d == 1),
Or(xo62l == 0 , xo62l == 1),
Or(xo62r == 0 , xo62r == 1),
Or(xo62u == 0 , xo62u == 1),
Or(xo62d == 0 , xo62d == 1),
Or(xo63l == 0 , xo63l == 1),
Or(xo63r == 0 , xo63r == 1),
Or(xo63u == 0 , xo63u == 1),
Or(xo63d == 0 , xo63d == 1),
Or(xo64l == 0 , xo64l == 1),
Or(xo64r == 0 , xo64r == 1),
Or(xo64u == 0 , xo64u == 1),
Or(xo64d == 0 , xo64d == 1),
Or(xo65l == 0 , xo65l == 1),
Or(xo65r == 0 , xo65r == 1),
Or(xo65u == 0 , xo65u == 1),
Or(xo65d == 0 , xo65d == 1),
Or(xo66l == 0 , xo66l == 1),
Or(xo66r == 0 , xo66r == 1),
Or(xo66u == 0 , xo66u == 1),
Or(xo66d == 0 , xo66d == 1),
Or(xo67l == 0 , xo67l == 1),
Or(xo67r == 0 , xo67r == 1),
Or(xo67u == 0 , xo67u == 1),
Or(xo67d == 0 , xo67d == 1),
Or(xo68l == 0 , xo68l == 1),
Or(xo68r == 0 , xo68r == 1),
Or(xo68u == 0 , xo68u == 1),
Or(xo68d == 0 , xo68d == 1),
Or(xo69l == 0 , xo69l == 1),
Or(xo69r == 0 , xo69r == 1),
Or(xo69u == 0 , xo69u == 1),
Or(xo69d == 0 , xo69d == 1),
Or(xo70l == 0 , xo70l == 1),
Or(xo70r == 0 , xo70r == 1),
Or(xo70u == 0 , xo70u == 1),
Or(xo70d == 0 , xo70d == 1),
Or(xo71l == 0 , xo71l == 1),
Or(xo71r == 0 , xo71r == 1),
Or(xo71u == 0 , xo71u == 1),
Or(xo71d == 0 , xo71d == 1),
Or(xo72l == 0 , xo72l == 1),
Or(xo72r == 0 , xo72r == 1),
Or(xo72u == 0 , xo72u == 1),
Or(xo72d == 0 , xo72d == 1),
Or(xo73l == 0 , xo73l == 1),
Or(xo73r == 0 , xo73r == 1),
Or(xo73u == 0 , xo73u == 1),
Or(xo73d == 0 , xo73d == 1),
Or(xo74l == 0 , xo74l == 1),
Or(xo74r == 0 , xo74r == 1),
Or(xo74u == 0 , xo74u == 1),
Or(xo74d == 0 , xo74d == 1),
Or(xo75l == 0 , xo75l == 1),
Or(xo75r == 0 , xo75r == 1),
Or(xo75u == 0 , xo75u == 1),
Or(xo75d == 0 , xo75d == 1),
Or(xo76l == 0 , xo76l == 1),
Or(xo76r == 0 , xo76r == 1),
Or(xo76u == 0 , xo76u == 1),
Or(xo76d == 0 , xo76d == 1),
Or(xo77l == 0 , xo77l == 1),
Or(xo77r == 0 , xo77r == 1),
Or(xo77u == 0 , xo77u == 1),
Or(xo77d == 0 , xo77d == 1),
Or(xo78l == 0 , xo78l == 1),
Or(xo78r == 0 , xo78r == 1),
Or(xo78u == 0 , xo78u == 1),
Or(xo78d == 0 , xo78d == 1),
Or(xo79l == 0 , xo79l == 1),
Or(xo79r == 0 , xo79r == 1),
Or(xo79u == 0 , xo79u == 1),
Or(xo79d == 0 , xo79d == 1),
Or(xo80l == 0 , xo80l == 1),
Or(xo80r == 0 , xo80r == 1),
Or(xo80u == 0 , xo80u == 1),
Or(xo80d == 0 , xo80d == 1),
Or(xo81l == 0 , xo81l == 1),
Or(xo81r == 0 , xo81r == 1),
Or(xo81u == 0 , xo81u == 1),
Or(xo81d == 0 , xo81d == 1),
Or(xo82l == 0 , xo82l == 1),
Or(xo82r == 0 , xo82r == 1),
Or(xo82u == 0 , xo82u == 1),
Or(xo82d == 0 , xo82d == 1),
Or(xo83l == 0 , xo83l == 1),
Or(xo83r == 0 , xo83r == 1),
Or(xo83u == 0 , xo83u == 1),
Or(xo83d == 0 , xo83d == 1),
Or(xo84l == 0 , xo84l == 1),
Or(xo84r == 0 , xo84r == 1),
Or(xo84u == 0 , xo84u == 1),
Or(xo84d == 0 , xo84d == 1),
Or(xo85l == 0 , xo85l == 1),
Or(xo85r == 0 , xo85r == 1),
Or(xo85u == 0 , xo85u == 1),
Or(xo85d == 0 , xo85d == 1),
Or(xo86l == 0 , xo86l == 1),
Or(xo86r == 0 , xo86r == 1),
Or(xo86u == 0 , xo86u == 1),
Or(xo86d == 0 , xo86d == 1),
Or(xo87l == 0 , xo87l == 1),
Or(xo87r == 0 , xo87r == 1),
Or(xo87u == 0 , xo87u == 1),
Or(xo87d == 0 , xo87d == 1),
Or(xo88l == 0 , xo88l == 1),
Or(xo88r == 0 , xo88r == 1),
Or(xo88u == 0 , xo88u == 1),
Or(xo88d == 0 , xo88d == 1),
Or(xo89l == 0 , xo89l == 1),
Or(xo89r == 0 , xo89r == 1),
Or(xo89u == 0 , xo89u == 1),
Or(xo89d == 0 , xo89d == 1),
Or(xo90l == 0 , xo90l == 1),
Or(xo90r == 0 , xo90r == 1),
Or(xo90u == 0 , xo90u == 1),
Or(xo90d == 0 , xo90d == 1),
Or(xo91l == 0 , xo91l == 1),
Or(xo91r == 0 , xo91r == 1),
Or(xo91u == 0 , xo91u == 1),
Or(xo91d == 0 , xo91d == 1),
Or(xo92l == 0 , xo92l == 1),
Or(xo92r == 0 , xo92r == 1),
Or(xo92u == 0 , xo92u == 1),
Or(xo92d == 0 , xo92d == 1),
Or(xo93l == 0 , xo93l == 1),
Or(xo93r == 0 , xo93r == 1),
Or(xo93u == 0 , xo93u == 1),
Or(xo93d == 0 , xo93d == 1),
Or(xo94l == 0 , xo94l == 1),
Or(xo94r == 0 , xo94r == 1),
Or(xo94u == 0 , xo94u == 1),
Or(xo94d == 0 , xo94d == 1),
Or(xo95l == 0 , xo95l == 1),
Or(xo95r == 0 , xo95r == 1),
Or(xo95u == 0 , xo95u == 1),
Or(xo95d == 0 , xo95d == 1),
Or(xo96l == 0 , xo96l == 1),
Or(xo96r == 0 , xo96r == 1),
Or(xo96u == 0 , xo96u == 1),
Or(xo96d == 0 , xo96d == 1),
Or(xo97l == 0 , xo97l == 1),
Or(xo97r == 0 , xo97r == 1),
Or(xo97u == 0 , xo97u == 1),
Or(xo97d == 0 , xo97d == 1),
Or(xo98l == 0 , xo98l == 1),
Or(xo98r == 0 , xo98r == 1),
Or(xo98u == 0 , xo98u == 1),
Or(xo98d == 0 , xo98d == 1),
Or(xo99l == 0 , xo99l == 1),
Or(xo99r == 0 , xo99r == 1),
Or(xo99u == 0 , xo99u == 1),
Or(xo99d == 0 , xo99d == 1),
Or(xo100l == 0 , xo100l == 1),
Or(xo100r == 0 , xo100r == 1),
Or(xo100u == 0 , xo100u == 1),
Or(xo100d == 0 , xo100d == 1),
Or(xo101l == 0 , xo101l == 1),
Or(xo101r == 0 , xo101r == 1),
Or(xo101u == 0 , xo101u == 1),
Or(xo101d == 0 , xo101d == 1),
Or(xo102l == 0 , xo102l == 1),
Or(xo102r == 0 , xo102r == 1),
Or(xo102u == 0 , xo102u == 1),
Or(xo102d == 0 , xo102d == 1),
Or(xo103l == 0 , xo103l == 1),
Or(xo103r == 0 , xo103r == 1),
Or(xo103u == 0 , xo103u == 1),
Or(xo103d == 0 , xo103d == 1),
Or(xo104l == 0 , xo104l == 1),
Or(xo104r == 0 , xo104r == 1),
Or(xo104u == 0 , xo104u == 1),
Or(xo104d == 0 , xo104d == 1),
Or(xo105l == 0 , xo105l == 1),
Or(xo105r == 0 , xo105r == 1),
Or(xo105u == 0 , xo105u == 1),
Or(xo105d == 0 , xo105d == 1),
Or(xo106l == 0 , xo106l == 1),
Or(xo106r == 0 , xo106r == 1),
Or(xo106u == 0 , xo106u == 1),
Or(xo106d == 0 , xo106d == 1),
Or(xo107l == 0 , xo107l == 1),
Or(xo107r == 0 , xo107r == 1),
Or(xo107u == 0 , xo107u == 1),
Or(xo107d == 0 , xo107d == 1),
Or(xo108l == 0 , xo108l == 1),
Or(xo108r == 0 , xo108r == 1),
Or(xo108u == 0 , xo108u == 1),
Or(xo108d == 0 , xo108d == 1),
Or(xo109l == 0 , xo109l == 1),
Or(xo109r == 0 , xo109r == 1),
Or(xo109u == 0 , xo109u == 1),
Or(xo109d == 0 , xo109d == 1),
Or(xo110l == 0 , xo110l == 1),
Or(xo110r == 0 , xo110r == 1),
Or(xo110u == 0 , xo110u == 1),
Or(xo110d == 0 , xo110d == 1),
Or(xo111l == 0 , xo111l == 1),
Or(xo111r == 0 , xo111r == 1),
Or(xo111u == 0 , xo111u == 1),
Or(xo111d == 0 , xo111d == 1),
Or(xo112l == 0 , xo112l == 1),
Or(xo112r == 0 , xo112r == 1),
Or(xo112u == 0 , xo112u == 1),
Or(xo112d == 0 , xo112d == 1),
Or(xo113l == 0 , xo113l == 1),
Or(xo113r == 0 , xo113r == 1),
Or(xo113u == 0 , xo113u == 1),
Or(xo113d == 0 , xo113d == 1),
Or(xo114l == 0 , xo114l == 1),
Or(xo114r == 0 , xo114r == 1),
Or(xo114u == 0 , xo114u == 1),
Or(xo114d == 0 , xo114d == 1),
Or(xo115l == 0 , xo115l == 1),
Or(xo115r == 0 , xo115r == 1),
Or(xo115u == 0 , xo115u == 1),
Or(xo115d == 0 , xo115d == 1),
Or(xo116l == 0 , xo116l == 1),
Or(xo116r == 0 , xo116r == 1),
Or(xo116u == 0 , xo116u == 1),
Or(xo116d == 0 , xo116d == 1),
Or(xo117l == 0 , xo117l == 1),
Or(xo117r == 0 , xo117r == 1),
Or(xo117u == 0 , xo117u == 1),
Or(xo117d == 0 , xo117d == 1),
Or(xo118l == 0 , xo118l == 1),
Or(xo118r == 0 , xo118r == 1),
Or(xo118u == 0 , xo118u == 1),
Or(xo118d == 0 , xo118d == 1),
Or(xo119l == 0 , xo119l == 1),
Or(xo119r == 0 , xo119r == 1),
Or(xo119u == 0 , xo119u == 1),
Or(xo119d == 0 , xo119d == 1),
Or(xo120l == 0 , xo120l == 1),
Or(xo120r == 0 , xo120r == 1),
Or(xo120u == 0 , xo120u == 1),
Or(xo120d == 0 , xo120d == 1),
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
Or (y30 == 0 , y30 == 1 ),
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
Or (y61 == 0 , y61 == 1 ),
Or (y62 == 0 , y62 == 1 ),
Or (y63 == 0 , y63 == 1 ),
Or (y64 == 0 , y64 == 1 ),
Or (y65 == 0 , y65 == 1 ),
Or (y66 == 0 , y66 == 1 ),
Or (y67 == 0 , y67 == 1 ),
Or (y68 == 0 , y68 == 1 ),
Or (y69 == 0 , y69 == 1 ),
Or (y70 == 0 , y70 == 1 ),
Or (y71 == 0 , y71 == 1 ),
Or (y72 == 0 , y72 == 1 ),
Or (y73 == 0 , y73 == 1 ),
Or (y74 == 0 , y74 == 1 ),
Or (y75 == 0 , y75 == 1 ),
Or (y76 == 0 , y76 == 1 ),
Or (y77 == 0 , y77 == 1 ),
Or (y78 == 0 , y78 == 1 ),
Or (y79 == 0 , y79 == 1 ),
Or (y80 == 0 , y80 == 1 ),
Or (y81 == 0 , y81 == 1 ),
Or (y82 == 0 , y82 == 1 ),
Or (y83 == 0 , y83 == 1 ),
Or (y84 == 0 , y84 == 1 ),
Or (y85 == 0 , y85 == 1 ),
Or (y86 == 0 , y86 == 1 ),
Or (y87 == 0 , y87 == 1 ),
Or (y88 == 0 , y88 == 1 ),
Or (y89 == 0 , y89 == 1 ),
Or (y90 == 0 , y90 == 1 ),
Or (y91 == 0 , y91 == 1 ),
Or (y92 == 0 , y92 == 1 ),
Or (y93 == 0 , y93 == 1 ),
Or (y94 == 0 , y94 == 1 ),
Or (y95 == 0 , y95 == 1 ),
Or (y96 == 0 , y96 == 1 ),
Or (y97 == 0 , y97 == 1 ),
Or (y98 == 0 , y98 == 1 ),
Or (y99 == 0 , y99 == 1 ),
Or (y100 == 0 , y100 == 1 ),
Or (y101 == 0 , y101 == 1 ),
Or (y102 == 0 , y102 == 1 ),
Or (y103 == 0 , y103 == 1 ),
Or (y104 == 0 , y104 == 1 ),
Or (y105 == 0 , y105 == 1 ),
Or (y106 == 0 , y106 == 1 ),
Or (y107 == 0 , y107 == 1 ),
Or (y108 == 0 , y108 == 1 ),
Or (y109 == 0 , y109 == 1 ),
Or (y110 == 0 , y110 == 1 ),
Or (y111 == 0 , y111 == 1 ),
Or (y112 == 0 , y112 == 1 ),
Or (y113 == 0 , y113 == 1 ),
Or (y114 == 0 , y114 == 1 ),
Or (y115 == 0 , y115 == 1 ),
Or (y116 == 0 , y116 == 1 ),
Or (y117 == 0 , y117 == 1 ),
Or (y118 == 0 , y118 == 1 ),
Or (y120 == 0 , y120 == 1 ),
y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 + y40 + y41 + y42 + y43 + y44 + y45 + y46 + y47 + y48 + y49 + y50 + y51 + y52 + y53 + y54 + y55 + y56 + y57 + y58 + y59 + y60 + y61 + y62 + y63 + y64 + y65 + y66 + y67 + y68 + y69 + y70 + y71 + y72 + y73 + y74 + y75 + y76 + y77 + y78 + y79 + y80 + y81 + y82 + y83 + y84 + y85 + y86 + y87 + y88 + y89 + y90 + y91 + y92 + y93 + y94 + y95 + y96 + y97 + y98 + y99 + y100 + y101 + y102 + y103 + y104 + y105 + y106 + y107 + y108 + y109 + y110 + y111 + y112 + y113 + y114 + y115 + y116 + y117 + y118 + y120 == 72
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')
