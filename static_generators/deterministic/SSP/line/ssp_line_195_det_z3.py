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
pi121 = Real('pi121')
pi122 = Real('pi122')
pi123 = Real('pi123')
pi124 = Real('pi124')
pi125 = Real('pi125')
pi126 = Real('pi126')
pi127 = Real('pi127')
pi128 = Real('pi128')
pi129 = Real('pi129')
pi130 = Real('pi130')
pi131 = Real('pi131')
pi132 = Real('pi132')
pi133 = Real('pi133')
pi134 = Real('pi134')
pi135 = Real('pi135')
pi136 = Real('pi136')
pi137 = Real('pi137')
pi138 = Real('pi138')
pi139 = Real('pi139')
pi140 = Real('pi140')
pi141 = Real('pi141')
pi142 = Real('pi142')
pi143 = Real('pi143')
pi144 = Real('pi144')
pi145 = Real('pi145')
pi146 = Real('pi146')
pi147 = Real('pi147')
pi148 = Real('pi148')
pi149 = Real('pi149')
pi150 = Real('pi150')
pi151 = Real('pi151')
pi152 = Real('pi152')
pi153 = Real('pi153')
pi154 = Real('pi154')
pi155 = Real('pi155')
pi156 = Real('pi156')
pi157 = Real('pi157')
pi158 = Real('pi158')
pi159 = Real('pi159')
pi160 = Real('pi160')
pi161 = Real('pi161')
pi162 = Real('pi162')
pi163 = Real('pi163')
pi164 = Real('pi164')
pi165 = Real('pi165')
pi166 = Real('pi166')
pi167 = Real('pi167')
pi168 = Real('pi168')
pi169 = Real('pi169')
pi170 = Real('pi170')
pi171 = Real('pi171')
pi172 = Real('pi172')
pi173 = Real('pi173')
pi174 = Real('pi174')
pi175 = Real('pi175')
pi176 = Real('pi176')
pi177 = Real('pi177')
pi178 = Real('pi178')
pi179 = Real('pi179')
pi180 = Real('pi180')
pi181 = Real('pi181')
pi182 = Real('pi182')
pi183 = Real('pi183')
pi184 = Real('pi184')
pi185 = Real('pi185')
pi186 = Real('pi186')
pi187 = Real('pi187')
pi188 = Real('pi188')
pi189 = Real('pi189')
pi190 = Real('pi190')
pi191 = Real('pi191')
pi192 = Real('pi192')
pi193 = Real('pi193')
pi194 = Real('pi194')

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
y119 = Real('y119')
y120 = Real('y120')
y121 = Real('y121')
y122 = Real('y122')
y123 = Real('y123')
y124 = Real('y124')
y125 = Real('y125')
y126 = Real('y126')
y127 = Real('y127')
y128 = Real('y128')
y129 = Real('y129')
y130 = Real('y130')
y131 = Real('y131')
y132 = Real('y132')
y133 = Real('y133')
y134 = Real('y134')
y135 = Real('y135')
y136 = Real('y136')
y137 = Real('y137')
y138 = Real('y138')
y139 = Real('y139')
y140 = Real('y140')
y141 = Real('y141')
y142 = Real('y142')
y143 = Real('y143')
y144 = Real('y144')
y145 = Real('y145')
y146 = Real('y146')
y147 = Real('y147')
y148 = Real('y148')
y149 = Real('y149')
y150 = Real('y150')
y151 = Real('y151')
y152 = Real('y152')
y153 = Real('y153')
y154 = Real('y154')
y155 = Real('y155')
y156 = Real('y156')
y157 = Real('y157')
y158 = Real('y158')
y159 = Real('y159')
y160 = Real('y160')
y161 = Real('y161')
y162 = Real('y162')
y163 = Real('y163')
y164 = Real('y164')
y165 = Real('y165')
y166 = Real('y166')
y167 = Real('y167')
y168 = Real('y168')
y169 = Real('y169')
y170 = Real('y170')
y171 = Real('y171')
y172 = Real('y172')
y173 = Real('y173')
y174 = Real('y174')
y175 = Real('y175')
y176 = Real('y176')
y177 = Real('y177')
y178 = Real('y178')
y179 = Real('y179')
y180 = Real('y180')
y181 = Real('y181')
y182 = Real('y182')
y183 = Real('y183')
y184 = Real('y184')
y185 = Real('y185')
y186 = Real('y186')
y187 = Real('y187')
y188 = Real('y188')
y189 = Real('y189')
y190 = Real('y190')
y191 = Real('y191')
y192 = Real('y192')
y193 = Real('y193')
y194 = Real('y194')

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
xo30l = Real('xo30l')
xo30r = Real('xo30r')
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
xo61l = Real('xo61l')
xo61r = Real('xo61r')
xo62l = Real('xo62l')
xo62r = Real('xo62r')
xo63l = Real('xo63l')
xo63r = Real('xo63r')
xo64l = Real('xo64l')
xo64r = Real('xo64r')
xo65l = Real('xo65l')
xo65r = Real('xo65r')
xo66l = Real('xo66l')
xo66r = Real('xo66r')
xo67l = Real('xo67l')
xo67r = Real('xo67r')
xo68l = Real('xo68l')
xo68r = Real('xo68r')
xo69l = Real('xo69l')
xo69r = Real('xo69r')
xo70l = Real('xo70l')
xo70r = Real('xo70r')
xo71l = Real('xo71l')
xo71r = Real('xo71r')
xo72l = Real('xo72l')
xo72r = Real('xo72r')
xo73l = Real('xo73l')
xo73r = Real('xo73r')
xo74l = Real('xo74l')
xo74r = Real('xo74r')
xo75l = Real('xo75l')
xo75r = Real('xo75r')
xo76l = Real('xo76l')
xo76r = Real('xo76r')
xo77l = Real('xo77l')
xo77r = Real('xo77r')
xo78l = Real('xo78l')
xo78r = Real('xo78r')
xo79l = Real('xo79l')
xo79r = Real('xo79r')
xo80l = Real('xo80l')
xo80r = Real('xo80r')
xo81l = Real('xo81l')
xo81r = Real('xo81r')
xo82l = Real('xo82l')
xo82r = Real('xo82r')
xo83l = Real('xo83l')
xo83r = Real('xo83r')
xo84l = Real('xo84l')
xo84r = Real('xo84r')
xo85l = Real('xo85l')
xo85r = Real('xo85r')
xo86l = Real('xo86l')
xo86r = Real('xo86r')
xo87l = Real('xo87l')
xo87r = Real('xo87r')
xo88l = Real('xo88l')
xo88r = Real('xo88r')
xo89l = Real('xo89l')
xo89r = Real('xo89r')
xo90l = Real('xo90l')
xo90r = Real('xo90r')
xo91l = Real('xo91l')
xo91r = Real('xo91r')
xo92l = Real('xo92l')
xo92r = Real('xo92r')
xo93l = Real('xo93l')
xo93r = Real('xo93r')
xo94l = Real('xo94l')
xo94r = Real('xo94r')
xo95l = Real('xo95l')
xo95r = Real('xo95r')
xo96l = Real('xo96l')
xo96r = Real('xo96r')
xo98l = Real('xo98l')
xo98r = Real('xo98r')
xo99l = Real('xo99l')
xo99r = Real('xo99r')
xo100l = Real('xo100l')
xo100r = Real('xo100r')
xo101l = Real('xo101l')
xo101r = Real('xo101r')
xo102l = Real('xo102l')
xo102r = Real('xo102r')
xo103l = Real('xo103l')
xo103r = Real('xo103r')
xo104l = Real('xo104l')
xo104r = Real('xo104r')
xo105l = Real('xo105l')
xo105r = Real('xo105r')
xo106l = Real('xo106l')
xo106r = Real('xo106r')
xo107l = Real('xo107l')
xo107r = Real('xo107r')
xo108l = Real('xo108l')
xo108r = Real('xo108r')
xo109l = Real('xo109l')
xo109r = Real('xo109r')
xo110l = Real('xo110l')
xo110r = Real('xo110r')
xo111l = Real('xo111l')
xo111r = Real('xo111r')
xo112l = Real('xo112l')
xo112r = Real('xo112r')
xo113l = Real('xo113l')
xo113r = Real('xo113r')
xo114l = Real('xo114l')
xo114r = Real('xo114r')
xo115l = Real('xo115l')
xo115r = Real('xo115r')
xo116l = Real('xo116l')
xo116r = Real('xo116r')
xo117l = Real('xo117l')
xo117r = Real('xo117r')
xo118l = Real('xo118l')
xo118r = Real('xo118r')
xo119l = Real('xo119l')
xo119r = Real('xo119r')
xo120l = Real('xo120l')
xo120r = Real('xo120r')
xo121l = Real('xo121l')
xo121r = Real('xo121r')
xo122l = Real('xo122l')
xo122r = Real('xo122r')
xo123l = Real('xo123l')
xo123r = Real('xo123r')
xo124l = Real('xo124l')
xo124r = Real('xo124r')
xo125l = Real('xo125l')
xo125r = Real('xo125r')
xo126l = Real('xo126l')
xo126r = Real('xo126r')
xo127l = Real('xo127l')
xo127r = Real('xo127r')
xo128l = Real('xo128l')
xo128r = Real('xo128r')
xo129l = Real('xo129l')
xo129r = Real('xo129r')
xo130l = Real('xo130l')
xo130r = Real('xo130r')
xo131l = Real('xo131l')
xo131r = Real('xo131r')
xo132l = Real('xo132l')
xo132r = Real('xo132r')
xo133l = Real('xo133l')
xo133r = Real('xo133r')
xo134l = Real('xo134l')
xo134r = Real('xo134r')
xo135l = Real('xo135l')
xo135r = Real('xo135r')
xo136l = Real('xo136l')
xo136r = Real('xo136r')
xo137l = Real('xo137l')
xo137r = Real('xo137r')
xo138l = Real('xo138l')
xo138r = Real('xo138r')
xo139l = Real('xo139l')
xo139r = Real('xo139r')
xo140l = Real('xo140l')
xo140r = Real('xo140r')
xo141l = Real('xo141l')
xo141r = Real('xo141r')
xo142l = Real('xo142l')
xo142r = Real('xo142r')
xo143l = Real('xo143l')
xo143r = Real('xo143r')
xo144l = Real('xo144l')
xo144r = Real('xo144r')
xo145l = Real('xo145l')
xo145r = Real('xo145r')
xo146l = Real('xo146l')
xo146r = Real('xo146r')
xo147l = Real('xo147l')
xo147r = Real('xo147r')
xo148l = Real('xo148l')
xo148r = Real('xo148r')
xo149l = Real('xo149l')
xo149r = Real('xo149r')
xo150l = Real('xo150l')
xo150r = Real('xo150r')
xo151l = Real('xo151l')
xo151r = Real('xo151r')
xo152l = Real('xo152l')
xo152r = Real('xo152r')
xo153l = Real('xo153l')
xo153r = Real('xo153r')
xo154l = Real('xo154l')
xo154r = Real('xo154r')
xo155l = Real('xo155l')
xo155r = Real('xo155r')
xo156l = Real('xo156l')
xo156r = Real('xo156r')
xo157l = Real('xo157l')
xo157r = Real('xo157r')
xo158l = Real('xo158l')
xo158r = Real('xo158r')
xo159l = Real('xo159l')
xo159r = Real('xo159r')
xo160l = Real('xo160l')
xo160r = Real('xo160r')
xo161l = Real('xo161l')
xo161r = Real('xo161r')
xo162l = Real('xo162l')
xo162r = Real('xo162r')
xo163l = Real('xo163l')
xo163r = Real('xo163r')
xo164l = Real('xo164l')
xo164r = Real('xo164r')
xo165l = Real('xo165l')
xo165r = Real('xo165r')
xo166l = Real('xo166l')
xo166r = Real('xo166r')
xo167l = Real('xo167l')
xo167r = Real('xo167r')
xo168l = Real('xo168l')
xo168r = Real('xo168r')
xo169l = Real('xo169l')
xo169r = Real('xo169r')
xo170l = Real('xo170l')
xo170r = Real('xo170r')
xo171l = Real('xo171l')
xo171r = Real('xo171r')
xo172l = Real('xo172l')
xo172r = Real('xo172r')
xo173l = Real('xo173l')
xo173r = Real('xo173r')
xo174l = Real('xo174l')
xo174r = Real('xo174r')
xo175l = Real('xo175l')
xo175r = Real('xo175r')
xo176l = Real('xo176l')
xo176r = Real('xo176r')
xo177l = Real('xo177l')
xo177r = Real('xo177r')
xo178l = Real('xo178l')
xo178r = Real('xo178r')
xo179l = Real('xo179l')
xo179r = Real('xo179r')
xo180l = Real('xo180l')
xo180r = Real('xo180r')
xo181l = Real('xo181l')
xo181r = Real('xo181r')
xo182l = Real('xo182l')
xo182r = Real('xo182r')
xo183l = Real('xo183l')
xo183r = Real('xo183r')
xo184l = Real('xo184l')
xo184r = Real('xo184r')
xo185l = Real('xo185l')
xo185r = Real('xo185r')
xo186l = Real('xo186l')
xo186r = Real('xo186r')
xo187l = Real('xo187l')
xo187r = Real('xo187r')
xo188l = Real('xo188l')
xo188r = Real('xo188r')
xo189l = Real('xo189l')
xo189r = Real('xo189r')
xo190l = Real('xo190l')
xo190r = Real('xo190r')
xo191l = Real('xo191l')
xo191r = Real('xo191r')
xo192l = Real('xo192l')
xo192r = Real('xo192r')
xo193l = Real('xo193l')
xo193r = Real('xo193r')
xo194l = Real('xo194l')
xo194r = Real('xo194r')
xol = Real('xol')
xor = Real('xor')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=97, pi1>=96, pi2>=95, pi3>=94, pi4>=93, pi5>=92, pi6>=91, pi7>=90, pi8>=89, pi9>=88, pi10>=87, pi11>=86, pi12>=85, pi13>=84, pi14>=83, pi15>=82, pi16>=81, pi17>=80, pi18>=79, pi19>=78, pi20>=77, pi21>=76, pi22>=75, pi23>=74, pi24>=73, pi25>=72, pi26>=71, pi27>=70, pi28>=69, pi29>=68, pi30>=67, pi31>=66, pi32>=65, pi33>=64, pi34>=63, pi35>=62, pi36>=61, pi37>=60, pi38>=59, pi39>=58, pi40>=57, pi41>=56, pi42>=55, pi43>=54, pi44>=53, pi45>=52, pi46>=51, pi47>=50, pi48>=49, pi49>=48, pi50>=47, pi51>=46, pi52>=45, pi53>=44, pi54>=43, pi55>=42, pi56>=41, pi57>=40, pi58>=39, pi59>=38, pi60>=37, pi61>=36, pi62>=35, pi63>=34, pi64>=33, pi65>=32, pi66>=31, pi67>=30, pi68>=29, pi69>=28, pi70>=27, pi71>=26, pi72>=25, pi73>=24, pi74>=23, pi75>=22, pi76>=21, pi77>=20, pi78>=19, pi79>=18, pi80>=17, pi81>=16, pi82>=15, pi83>=14, pi84>=13, pi85>=12, pi86>=11, pi87>=10, pi88>=9, pi89>=8, pi90>=7, pi91>=6, pi92>=5, pi93>=4, pi94>=3, pi95>=2, pi96>=1, pi97>=0, pi98>=1, pi99>=2, pi100>=3, pi101>=4, pi102>=5, pi103>=6, pi104>=7, pi105>=8, pi106>=9, pi107>=10, pi108>=11, pi109>=12, pi110>=13, pi111>=14, pi112>=15, pi113>=16, pi114>=17, pi115>=18, pi116>=19, pi117>=20, pi118>=21, pi119>=22, pi120>=23, pi121>=24, pi122>=25, pi123>=26, pi124>=27, pi125>=28, pi126>=29, pi127>=30, pi128>=31, pi129>=32, pi130>=33, pi131>=34, pi132>=35, pi133>=36, pi134>=37, pi135>=38, pi136>=39, pi137>=40, pi138>=41, pi139>=42, pi140>=43, pi141>=44, pi142>=45, pi143>=46, pi144>=47, pi145>=48, pi146>=49, pi147>=50, pi148>=51, pi149>=52, pi150>=53, pi151>=54, pi152>=55, pi153>=56, pi154>=57, pi155>=58, pi156>=59, pi157>=60, pi158>=61, pi159>=62, pi160>=63, pi161>=64, pi162>=65, pi163>=66, pi164>=67, pi165>=68, pi166>=69, pi167>=70, pi168>=71, pi169>=72, pi170>=73, pi171>=74, pi172>=75, pi173>=76, pi174>=77, pi175>=78, pi176>=79, pi177>=80, pi178>=81, pi179>=82, pi180>=83, pi181>=84, pi182>=85, pi183>=86, pi184>=87, pi185>=88, pi186>=89, pi187>=90, pi188>=91, pi189>=92, pi190>=93, pi191>=94, pi192>=95, pi193>=96, pi194>=97, 
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
pi30== ((1 - y30)*xol + y30*xo30l) * (1 + pi29) + ((1 - y30)*xor + y30*xo30r) * (1 + pi31), 
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
pi60== ((1 - y60)*xol + y60*xo60l) * (1 + pi59) + ((1 - y60)*xor + y60*xo60r) * (1 + pi61), 
pi61== ((1 - y61)*xol + y61*xo61l) * (1 + pi60) + ((1 - y61)*xor + y61*xo61r) * (1 + pi62), 
pi62== ((1 - y62)*xol + y62*xo62l) * (1 + pi61) + ((1 - y62)*xor + y62*xo62r) * (1 + pi63), 
pi63== ((1 - y63)*xol + y63*xo63l) * (1 + pi62) + ((1 - y63)*xor + y63*xo63r) * (1 + pi64), 
pi64== ((1 - y64)*xol + y64*xo64l) * (1 + pi63) + ((1 - y64)*xor + y64*xo64r) * (1 + pi65), 
pi65== ((1 - y65)*xol + y65*xo65l) * (1 + pi64) + ((1 - y65)*xor + y65*xo65r) * (1 + pi66), 
pi66== ((1 - y66)*xol + y66*xo66l) * (1 + pi65) + ((1 - y66)*xor + y66*xo66r) * (1 + pi67), 
pi67== ((1 - y67)*xol + y67*xo67l) * (1 + pi66) + ((1 - y67)*xor + y67*xo67r) * (1 + pi68), 
pi68== ((1 - y68)*xol + y68*xo68l) * (1 + pi67) + ((1 - y68)*xor + y68*xo68r) * (1 + pi69), 
pi69== ((1 - y69)*xol + y69*xo69l) * (1 + pi68) + ((1 - y69)*xor + y69*xo69r) * (1 + pi70), 
pi70== ((1 - y70)*xol + y70*xo70l) * (1 + pi69) + ((1 - y70)*xor + y70*xo70r) * (1 + pi71), 
pi71== ((1 - y71)*xol + y71*xo71l) * (1 + pi70) + ((1 - y71)*xor + y71*xo71r) * (1 + pi72), 
pi72== ((1 - y72)*xol + y72*xo72l) * (1 + pi71) + ((1 - y72)*xor + y72*xo72r) * (1 + pi73), 
pi73== ((1 - y73)*xol + y73*xo73l) * (1 + pi72) + ((1 - y73)*xor + y73*xo73r) * (1 + pi74), 
pi74== ((1 - y74)*xol + y74*xo74l) * (1 + pi73) + ((1 - y74)*xor + y74*xo74r) * (1 + pi75), 
pi75== ((1 - y75)*xol + y75*xo75l) * (1 + pi74) + ((1 - y75)*xor + y75*xo75r) * (1 + pi76), 
pi76== ((1 - y76)*xol + y76*xo76l) * (1 + pi75) + ((1 - y76)*xor + y76*xo76r) * (1 + pi77), 
pi77== ((1 - y77)*xol + y77*xo77l) * (1 + pi76) + ((1 - y77)*xor + y77*xo77r) * (1 + pi78), 
pi78== ((1 - y78)*xol + y78*xo78l) * (1 + pi77) + ((1 - y78)*xor + y78*xo78r) * (1 + pi79), 
pi79== ((1 - y79)*xol + y79*xo79l) * (1 + pi78) + ((1 - y79)*xor + y79*xo79r) * (1 + pi80), 
pi80== ((1 - y80)*xol + y80*xo80l) * (1 + pi79) + ((1 - y80)*xor + y80*xo80r) * (1 + pi81), 
pi81== ((1 - y81)*xol + y81*xo81l) * (1 + pi80) + ((1 - y81)*xor + y81*xo81r) * (1 + pi82), 
pi82== ((1 - y82)*xol + y82*xo82l) * (1 + pi81) + ((1 - y82)*xor + y82*xo82r) * (1 + pi83), 
pi83== ((1 - y83)*xol + y83*xo83l) * (1 + pi82) + ((1 - y83)*xor + y83*xo83r) * (1 + pi84), 
pi84== ((1 - y84)*xol + y84*xo84l) * (1 + pi83) + ((1 - y84)*xor + y84*xo84r) * (1 + pi85), 
pi85== ((1 - y85)*xol + y85*xo85l) * (1 + pi84) + ((1 - y85)*xor + y85*xo85r) * (1 + pi86), 
pi86== ((1 - y86)*xol + y86*xo86l) * (1 + pi85) + ((1 - y86)*xor + y86*xo86r) * (1 + pi87), 
pi87== ((1 - y87)*xol + y87*xo87l) * (1 + pi86) + ((1 - y87)*xor + y87*xo87r) * (1 + pi88), 
pi88== ((1 - y88)*xol + y88*xo88l) * (1 + pi87) + ((1 - y88)*xor + y88*xo88r) * (1 + pi89), 
pi89== ((1 - y89)*xol + y89*xo89l) * (1 + pi88) + ((1 - y89)*xor + y89*xo89r) * (1 + pi90), 
pi90== ((1 - y90)*xol + y90*xo90l) * (1 + pi89) + ((1 - y90)*xor + y90*xo90r) * (1 + pi91), 
pi91== ((1 - y91)*xol + y91*xo91l) * (1 + pi90) + ((1 - y91)*xor + y91*xo91r) * (1 + pi92), 
pi92== ((1 - y92)*xol + y92*xo92l) * (1 + pi91) + ((1 - y92)*xor + y92*xo92r) * (1 + pi93), 
pi93== ((1 - y93)*xol + y93*xo93l) * (1 + pi92) + ((1 - y93)*xor + y93*xo93r) * (1 + pi94), 
pi94== ((1 - y94)*xol + y94*xo94l) * (1 + pi93) + ((1 - y94)*xor + y94*xo94r) * (1 + pi95), 
pi95== ((1 - y95)*xol + y95*xo95l) * (1 + pi94) + ((1 - y95)*xor + y95*xo95r) * (1 + pi96), 
pi96== ((1 - y96)*xol + y96*xo96l) * (1 + pi95) + ((1 - y96)*xor + y96*xo96r) * (1 + pi97), 
pi97 == 0, 
pi98== ((1 - y98)*xol + y98*xo98l) * (1 + pi97) + ((1 - y98)*xor + y98*xo98r) * (1 + pi99), 
pi99== ((1 - y99)*xol + y99*xo99l) * (1 + pi98) + ((1 - y99)*xor + y99*xo99r) * (1 + pi100), 
pi100== ((1 - y100)*xol + y100*xo100l) * (1 + pi99) + ((1 - y100)*xor + y100*xo100r) * (1 + pi101), 
pi101== ((1 - y101)*xol + y101*xo101l) * (1 + pi100) + ((1 - y101)*xor + y101*xo101r) * (1 + pi102), 
pi102== ((1 - y102)*xol + y102*xo102l) * (1 + pi101) + ((1 - y102)*xor + y102*xo102r) * (1 + pi103), 
pi103== ((1 - y103)*xol + y103*xo103l) * (1 + pi102) + ((1 - y103)*xor + y103*xo103r) * (1 + pi104), 
pi104== ((1 - y104)*xol + y104*xo104l) * (1 + pi103) + ((1 - y104)*xor + y104*xo104r) * (1 + pi105), 
pi105== ((1 - y105)*xol + y105*xo105l) * (1 + pi104) + ((1 - y105)*xor + y105*xo105r) * (1 + pi106), 
pi106== ((1 - y106)*xol + y106*xo106l) * (1 + pi105) + ((1 - y106)*xor + y106*xo106r) * (1 + pi107), 
pi107== ((1 - y107)*xol + y107*xo107l) * (1 + pi106) + ((1 - y107)*xor + y107*xo107r) * (1 + pi108), 
pi108== ((1 - y108)*xol + y108*xo108l) * (1 + pi107) + ((1 - y108)*xor + y108*xo108r) * (1 + pi109), 
pi109== ((1 - y109)*xol + y109*xo109l) * (1 + pi108) + ((1 - y109)*xor + y109*xo109r) * (1 + pi110), 
pi110== ((1 - y110)*xol + y110*xo110l) * (1 + pi109) + ((1 - y110)*xor + y110*xo110r) * (1 + pi111), 
pi111== ((1 - y111)*xol + y111*xo111l) * (1 + pi110) + ((1 - y111)*xor + y111*xo111r) * (1 + pi112), 
pi112== ((1 - y112)*xol + y112*xo112l) * (1 + pi111) + ((1 - y112)*xor + y112*xo112r) * (1 + pi113), 
pi113== ((1 - y113)*xol + y113*xo113l) * (1 + pi112) + ((1 - y113)*xor + y113*xo113r) * (1 + pi114), 
pi114== ((1 - y114)*xol + y114*xo114l) * (1 + pi113) + ((1 - y114)*xor + y114*xo114r) * (1 + pi115), 
pi115== ((1 - y115)*xol + y115*xo115l) * (1 + pi114) + ((1 - y115)*xor + y115*xo115r) * (1 + pi116), 
pi116== ((1 - y116)*xol + y116*xo116l) * (1 + pi115) + ((1 - y116)*xor + y116*xo116r) * (1 + pi117), 
pi117== ((1 - y117)*xol + y117*xo117l) * (1 + pi116) + ((1 - y117)*xor + y117*xo117r) * (1 + pi118), 
pi118== ((1 - y118)*xol + y118*xo118l) * (1 + pi117) + ((1 - y118)*xor + y118*xo118r) * (1 + pi119), 
pi119== ((1 - y119)*xol + y119*xo119l) * (1 + pi118) + ((1 - y119)*xor + y119*xo119r) * (1 + pi120), 
pi120== ((1 - y120)*xol + y120*xo120l) * (1 + pi119) + ((1 - y120)*xor + y120*xo120r) * (1 + pi121), 
pi121== ((1 - y121)*xol + y121*xo121l) * (1 + pi120) + ((1 - y121)*xor + y121*xo121r) * (1 + pi122), 
pi122== ((1 - y122)*xol + y122*xo122l) * (1 + pi121) + ((1 - y122)*xor + y122*xo122r) * (1 + pi123), 
pi123== ((1 - y123)*xol + y123*xo123l) * (1 + pi122) + ((1 - y123)*xor + y123*xo123r) * (1 + pi124), 
pi124== ((1 - y124)*xol + y124*xo124l) * (1 + pi123) + ((1 - y124)*xor + y124*xo124r) * (1 + pi125), 
pi125== ((1 - y125)*xol + y125*xo125l) * (1 + pi124) + ((1 - y125)*xor + y125*xo125r) * (1 + pi126), 
pi126== ((1 - y126)*xol + y126*xo126l) * (1 + pi125) + ((1 - y126)*xor + y126*xo126r) * (1 + pi127), 
pi127== ((1 - y127)*xol + y127*xo127l) * (1 + pi126) + ((1 - y127)*xor + y127*xo127r) * (1 + pi128), 
pi128== ((1 - y128)*xol + y128*xo128l) * (1 + pi127) + ((1 - y128)*xor + y128*xo128r) * (1 + pi129), 
pi129== ((1 - y129)*xol + y129*xo129l) * (1 + pi128) + ((1 - y129)*xor + y129*xo129r) * (1 + pi130), 
pi130== ((1 - y130)*xol + y130*xo130l) * (1 + pi129) + ((1 - y130)*xor + y130*xo130r) * (1 + pi131), 
pi131== ((1 - y131)*xol + y131*xo131l) * (1 + pi130) + ((1 - y131)*xor + y131*xo131r) * (1 + pi132), 
pi132== ((1 - y132)*xol + y132*xo132l) * (1 + pi131) + ((1 - y132)*xor + y132*xo132r) * (1 + pi133), 
pi133== ((1 - y133)*xol + y133*xo133l) * (1 + pi132) + ((1 - y133)*xor + y133*xo133r) * (1 + pi134), 
pi134== ((1 - y134)*xol + y134*xo134l) * (1 + pi133) + ((1 - y134)*xor + y134*xo134r) * (1 + pi135), 
pi135== ((1 - y135)*xol + y135*xo135l) * (1 + pi134) + ((1 - y135)*xor + y135*xo135r) * (1 + pi136), 
pi136== ((1 - y136)*xol + y136*xo136l) * (1 + pi135) + ((1 - y136)*xor + y136*xo136r) * (1 + pi137), 
pi137== ((1 - y137)*xol + y137*xo137l) * (1 + pi136) + ((1 - y137)*xor + y137*xo137r) * (1 + pi138), 
pi138== ((1 - y138)*xol + y138*xo138l) * (1 + pi137) + ((1 - y138)*xor + y138*xo138r) * (1 + pi139), 
pi139== ((1 - y139)*xol + y139*xo139l) * (1 + pi138) + ((1 - y139)*xor + y139*xo139r) * (1 + pi140), 
pi140== ((1 - y140)*xol + y140*xo140l) * (1 + pi139) + ((1 - y140)*xor + y140*xo140r) * (1 + pi141), 
pi141== ((1 - y141)*xol + y141*xo141l) * (1 + pi140) + ((1 - y141)*xor + y141*xo141r) * (1 + pi142), 
pi142== ((1 - y142)*xol + y142*xo142l) * (1 + pi141) + ((1 - y142)*xor + y142*xo142r) * (1 + pi143), 
pi143== ((1 - y143)*xol + y143*xo143l) * (1 + pi142) + ((1 - y143)*xor + y143*xo143r) * (1 + pi144), 
pi144== ((1 - y144)*xol + y144*xo144l) * (1 + pi143) + ((1 - y144)*xor + y144*xo144r) * (1 + pi145), 
pi145== ((1 - y145)*xol + y145*xo145l) * (1 + pi144) + ((1 - y145)*xor + y145*xo145r) * (1 + pi146), 
pi146== ((1 - y146)*xol + y146*xo146l) * (1 + pi145) + ((1 - y146)*xor + y146*xo146r) * (1 + pi147), 
pi147== ((1 - y147)*xol + y147*xo147l) * (1 + pi146) + ((1 - y147)*xor + y147*xo147r) * (1 + pi148), 
pi148== ((1 - y148)*xol + y148*xo148l) * (1 + pi147) + ((1 - y148)*xor + y148*xo148r) * (1 + pi149), 
pi149== ((1 - y149)*xol + y149*xo149l) * (1 + pi148) + ((1 - y149)*xor + y149*xo149r) * (1 + pi150), 
pi150== ((1 - y150)*xol + y150*xo150l) * (1 + pi149) + ((1 - y150)*xor + y150*xo150r) * (1 + pi151), 
pi151== ((1 - y151)*xol + y151*xo151l) * (1 + pi150) + ((1 - y151)*xor + y151*xo151r) * (1 + pi152), 
pi152== ((1 - y152)*xol + y152*xo152l) * (1 + pi151) + ((1 - y152)*xor + y152*xo152r) * (1 + pi153), 
pi153== ((1 - y153)*xol + y153*xo153l) * (1 + pi152) + ((1 - y153)*xor + y153*xo153r) * (1 + pi154), 
pi154== ((1 - y154)*xol + y154*xo154l) * (1 + pi153) + ((1 - y154)*xor + y154*xo154r) * (1 + pi155), 
pi155== ((1 - y155)*xol + y155*xo155l) * (1 + pi154) + ((1 - y155)*xor + y155*xo155r) * (1 + pi156), 
pi156== ((1 - y156)*xol + y156*xo156l) * (1 + pi155) + ((1 - y156)*xor + y156*xo156r) * (1 + pi157), 
pi157== ((1 - y157)*xol + y157*xo157l) * (1 + pi156) + ((1 - y157)*xor + y157*xo157r) * (1 + pi158), 
pi158== ((1 - y158)*xol + y158*xo158l) * (1 + pi157) + ((1 - y158)*xor + y158*xo158r) * (1 + pi159), 
pi159== ((1 - y159)*xol + y159*xo159l) * (1 + pi158) + ((1 - y159)*xor + y159*xo159r) * (1 + pi160), 
pi160== ((1 - y160)*xol + y160*xo160l) * (1 + pi159) + ((1 - y160)*xor + y160*xo160r) * (1 + pi161), 
pi161== ((1 - y161)*xol + y161*xo161l) * (1 + pi160) + ((1 - y161)*xor + y161*xo161r) * (1 + pi162), 
pi162== ((1 - y162)*xol + y162*xo162l) * (1 + pi161) + ((1 - y162)*xor + y162*xo162r) * (1 + pi163), 
pi163== ((1 - y163)*xol + y163*xo163l) * (1 + pi162) + ((1 - y163)*xor + y163*xo163r) * (1 + pi164), 
pi164== ((1 - y164)*xol + y164*xo164l) * (1 + pi163) + ((1 - y164)*xor + y164*xo164r) * (1 + pi165), 
pi165== ((1 - y165)*xol + y165*xo165l) * (1 + pi164) + ((1 - y165)*xor + y165*xo165r) * (1 + pi166), 
pi166== ((1 - y166)*xol + y166*xo166l) * (1 + pi165) + ((1 - y166)*xor + y166*xo166r) * (1 + pi167), 
pi167== ((1 - y167)*xol + y167*xo167l) * (1 + pi166) + ((1 - y167)*xor + y167*xo167r) * (1 + pi168), 
pi168== ((1 - y168)*xol + y168*xo168l) * (1 + pi167) + ((1 - y168)*xor + y168*xo168r) * (1 + pi169), 
pi169== ((1 - y169)*xol + y169*xo169l) * (1 + pi168) + ((1 - y169)*xor + y169*xo169r) * (1 + pi170), 
pi170== ((1 - y170)*xol + y170*xo170l) * (1 + pi169) + ((1 - y170)*xor + y170*xo170r) * (1 + pi171), 
pi171== ((1 - y171)*xol + y171*xo171l) * (1 + pi170) + ((1 - y171)*xor + y171*xo171r) * (1 + pi172), 
pi172== ((1 - y172)*xol + y172*xo172l) * (1 + pi171) + ((1 - y172)*xor + y172*xo172r) * (1 + pi173), 
pi173== ((1 - y173)*xol + y173*xo173l) * (1 + pi172) + ((1 - y173)*xor + y173*xo173r) * (1 + pi174), 
pi174== ((1 - y174)*xol + y174*xo174l) * (1 + pi173) + ((1 - y174)*xor + y174*xo174r) * (1 + pi175), 
pi175== ((1 - y175)*xol + y175*xo175l) * (1 + pi174) + ((1 - y175)*xor + y175*xo175r) * (1 + pi176), 
pi176== ((1 - y176)*xol + y176*xo176l) * (1 + pi175) + ((1 - y176)*xor + y176*xo176r) * (1 + pi177), 
pi177== ((1 - y177)*xol + y177*xo177l) * (1 + pi176) + ((1 - y177)*xor + y177*xo177r) * (1 + pi178), 
pi178== ((1 - y178)*xol + y178*xo178l) * (1 + pi177) + ((1 - y178)*xor + y178*xo178r) * (1 + pi179), 
pi179== ((1 - y179)*xol + y179*xo179l) * (1 + pi178) + ((1 - y179)*xor + y179*xo179r) * (1 + pi180), 
pi180== ((1 - y180)*xol + y180*xo180l) * (1 + pi179) + ((1 - y180)*xor + y180*xo180r) * (1 + pi181), 
pi181== ((1 - y181)*xol + y181*xo181l) * (1 + pi180) + ((1 - y181)*xor + y181*xo181r) * (1 + pi182), 
pi182== ((1 - y182)*xol + y182*xo182l) * (1 + pi181) + ((1 - y182)*xor + y182*xo182r) * (1 + pi183), 
pi183== ((1 - y183)*xol + y183*xo183l) * (1 + pi182) + ((1 - y183)*xor + y183*xo183r) * (1 + pi184), 
pi184== ((1 - y184)*xol + y184*xo184l) * (1 + pi183) + ((1 - y184)*xor + y184*xo184r) * (1 + pi185), 
pi185== ((1 - y185)*xol + y185*xo185l) * (1 + pi184) + ((1 - y185)*xor + y185*xo185r) * (1 + pi186), 
pi186== ((1 - y186)*xol + y186*xo186l) * (1 + pi185) + ((1 - y186)*xor + y186*xo186r) * (1 + pi187), 
pi187== ((1 - y187)*xol + y187*xo187l) * (1 + pi186) + ((1 - y187)*xor + y187*xo187r) * (1 + pi188), 
pi188== ((1 - y188)*xol + y188*xo188l) * (1 + pi187) + ((1 - y188)*xor + y188*xo188r) * (1 + pi189), 
pi189== ((1 - y189)*xol + y189*xo189l) * (1 + pi188) + ((1 - y189)*xor + y189*xo189r) * (1 + pi190), 
pi190== ((1 - y190)*xol + y190*xo190l) * (1 + pi189) + ((1 - y190)*xor + y190*xo190r) * (1 + pi191), 
pi191== ((1 - y191)*xol + y191*xo191l) * (1 + pi190) + ((1 - y191)*xor + y191*xo191r) * (1 + pi192), 
pi192== ((1 - y192)*xol + y192*xo192l) * (1 + pi191) + ((1 - y192)*xor + y192*xo192r) * (1 + pi193), 
pi193== ((1 - y193)*xol + y193*xo193l) * (1 + pi192) + ((1 - y193)*xor + y193*xo193r) * (1 + pi194), 
pi194== ((1 - y194)*xol + y194*xo194l) * (1 + pi193) + ((1 - y194)*xor + y194*xo194r) * (1 + pi194), 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= 49
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi98+pi99+pi100+pi101+pi102+pi103+pi104+pi105+pi106+pi107+pi108+pi109+pi110+pi111+pi112+pi113+pi114+pi115+pi116+pi117+pi118+pi119+pi120+pi121+pi122+pi123+pi124+pi125+pi126+pi127+pi128+pi129+pi130+pi131+pi132+pi133+pi134+pi135+pi136+pi137+pi138+pi139+pi140+pi141+pi142+pi143+pi144+pi145+pi146+pi147+pi148+pi149+pi150+pi151+pi152+pi153+pi154+pi155+pi156+pi157+pi158+pi159+pi160+pi161+pi162+pi163+pi164+pi165+pi166+pi167+pi168+pi169+pi170+pi171+pi172+pi173+pi174+pi175+pi176+pi177+pi178+pi179+pi180+pi181+pi182+pi183+pi184+pi185+pi186+pi187+pi188+pi189+pi190+pi191+pi192+pi193+pi194) * Q(1,194) <= 49,
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
xo30l <= 1,
xo30l >= 0,
xo30r <= 1,
xo30r >= 0,
xo30l + xo30r == 1,
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
xo61l <= 1,
xo61l >= 0,
xo61r <= 1,
xo61r >= 0,
xo61l + xo61r == 1,
xo62l <= 1,
xo62l >= 0,
xo62r <= 1,
xo62r >= 0,
xo62l + xo62r == 1,
xo63l <= 1,
xo63l >= 0,
xo63r <= 1,
xo63r >= 0,
xo63l + xo63r == 1,
xo64l <= 1,
xo64l >= 0,
xo64r <= 1,
xo64r >= 0,
xo64l + xo64r == 1,
xo65l <= 1,
xo65l >= 0,
xo65r <= 1,
xo65r >= 0,
xo65l + xo65r == 1,
xo66l <= 1,
xo66l >= 0,
xo66r <= 1,
xo66r >= 0,
xo66l + xo66r == 1,
xo67l <= 1,
xo67l >= 0,
xo67r <= 1,
xo67r >= 0,
xo67l + xo67r == 1,
xo68l <= 1,
xo68l >= 0,
xo68r <= 1,
xo68r >= 0,
xo68l + xo68r == 1,
xo69l <= 1,
xo69l >= 0,
xo69r <= 1,
xo69r >= 0,
xo69l + xo69r == 1,
xo70l <= 1,
xo70l >= 0,
xo70r <= 1,
xo70r >= 0,
xo70l + xo70r == 1,
xo71l <= 1,
xo71l >= 0,
xo71r <= 1,
xo71r >= 0,
xo71l + xo71r == 1,
xo72l <= 1,
xo72l >= 0,
xo72r <= 1,
xo72r >= 0,
xo72l + xo72r == 1,
xo73l <= 1,
xo73l >= 0,
xo73r <= 1,
xo73r >= 0,
xo73l + xo73r == 1,
xo74l <= 1,
xo74l >= 0,
xo74r <= 1,
xo74r >= 0,
xo74l + xo74r == 1,
xo75l <= 1,
xo75l >= 0,
xo75r <= 1,
xo75r >= 0,
xo75l + xo75r == 1,
xo76l <= 1,
xo76l >= 0,
xo76r <= 1,
xo76r >= 0,
xo76l + xo76r == 1,
xo77l <= 1,
xo77l >= 0,
xo77r <= 1,
xo77r >= 0,
xo77l + xo77r == 1,
xo78l <= 1,
xo78l >= 0,
xo78r <= 1,
xo78r >= 0,
xo78l + xo78r == 1,
xo79l <= 1,
xo79l >= 0,
xo79r <= 1,
xo79r >= 0,
xo79l + xo79r == 1,
xo80l <= 1,
xo80l >= 0,
xo80r <= 1,
xo80r >= 0,
xo80l + xo80r == 1,
xo81l <= 1,
xo81l >= 0,
xo81r <= 1,
xo81r >= 0,
xo81l + xo81r == 1,
xo82l <= 1,
xo82l >= 0,
xo82r <= 1,
xo82r >= 0,
xo82l + xo82r == 1,
xo83l <= 1,
xo83l >= 0,
xo83r <= 1,
xo83r >= 0,
xo83l + xo83r == 1,
xo84l <= 1,
xo84l >= 0,
xo84r <= 1,
xo84r >= 0,
xo84l + xo84r == 1,
xo85l <= 1,
xo85l >= 0,
xo85r <= 1,
xo85r >= 0,
xo85l + xo85r == 1,
xo86l <= 1,
xo86l >= 0,
xo86r <= 1,
xo86r >= 0,
xo86l + xo86r == 1,
xo87l <= 1,
xo87l >= 0,
xo87r <= 1,
xo87r >= 0,
xo87l + xo87r == 1,
xo88l <= 1,
xo88l >= 0,
xo88r <= 1,
xo88r >= 0,
xo88l + xo88r == 1,
xo89l <= 1,
xo89l >= 0,
xo89r <= 1,
xo89r >= 0,
xo89l + xo89r == 1,
xo90l <= 1,
xo90l >= 0,
xo90r <= 1,
xo90r >= 0,
xo90l + xo90r == 1,
xo91l <= 1,
xo91l >= 0,
xo91r <= 1,
xo91r >= 0,
xo91l + xo91r == 1,
xo92l <= 1,
xo92l >= 0,
xo92r <= 1,
xo92r >= 0,
xo92l + xo92r == 1,
xo93l <= 1,
xo93l >= 0,
xo93r <= 1,
xo93r >= 0,
xo93l + xo93r == 1,
xo94l <= 1,
xo94l >= 0,
xo94r <= 1,
xo94r >= 0,
xo94l + xo94r == 1,
xo95l <= 1,
xo95l >= 0,
xo95r <= 1,
xo95r >= 0,
xo95l + xo95r == 1,
xo96l <= 1,
xo96l >= 0,
xo96r <= 1,
xo96r >= 0,
xo96l + xo96r == 1,
xo98l <= 1,
xo98l >= 0,
xo98r <= 1,
xo98r >= 0,
xo98l + xo98r == 1,
xo99l <= 1,
xo99l >= 0,
xo99r <= 1,
xo99r >= 0,
xo99l + xo99r == 1,
xo100l <= 1,
xo100l >= 0,
xo100r <= 1,
xo100r >= 0,
xo100l + xo100r == 1,
xo101l <= 1,
xo101l >= 0,
xo101r <= 1,
xo101r >= 0,
xo101l + xo101r == 1,
xo102l <= 1,
xo102l >= 0,
xo102r <= 1,
xo102r >= 0,
xo102l + xo102r == 1,
xo103l <= 1,
xo103l >= 0,
xo103r <= 1,
xo103r >= 0,
xo103l + xo103r == 1,
xo104l <= 1,
xo104l >= 0,
xo104r <= 1,
xo104r >= 0,
xo104l + xo104r == 1,
xo105l <= 1,
xo105l >= 0,
xo105r <= 1,
xo105r >= 0,
xo105l + xo105r == 1,
xo106l <= 1,
xo106l >= 0,
xo106r <= 1,
xo106r >= 0,
xo106l + xo106r == 1,
xo107l <= 1,
xo107l >= 0,
xo107r <= 1,
xo107r >= 0,
xo107l + xo107r == 1,
xo108l <= 1,
xo108l >= 0,
xo108r <= 1,
xo108r >= 0,
xo108l + xo108r == 1,
xo109l <= 1,
xo109l >= 0,
xo109r <= 1,
xo109r >= 0,
xo109l + xo109r == 1,
xo110l <= 1,
xo110l >= 0,
xo110r <= 1,
xo110r >= 0,
xo110l + xo110r == 1,
xo111l <= 1,
xo111l >= 0,
xo111r <= 1,
xo111r >= 0,
xo111l + xo111r == 1,
xo112l <= 1,
xo112l >= 0,
xo112r <= 1,
xo112r >= 0,
xo112l + xo112r == 1,
xo113l <= 1,
xo113l >= 0,
xo113r <= 1,
xo113r >= 0,
xo113l + xo113r == 1,
xo114l <= 1,
xo114l >= 0,
xo114r <= 1,
xo114r >= 0,
xo114l + xo114r == 1,
xo115l <= 1,
xo115l >= 0,
xo115r <= 1,
xo115r >= 0,
xo115l + xo115r == 1,
xo116l <= 1,
xo116l >= 0,
xo116r <= 1,
xo116r >= 0,
xo116l + xo116r == 1,
xo117l <= 1,
xo117l >= 0,
xo117r <= 1,
xo117r >= 0,
xo117l + xo117r == 1,
xo118l <= 1,
xo118l >= 0,
xo118r <= 1,
xo118r >= 0,
xo118l + xo118r == 1,
xo119l <= 1,
xo119l >= 0,
xo119r <= 1,
xo119r >= 0,
xo119l + xo119r == 1,
xo120l <= 1,
xo120l >= 0,
xo120r <= 1,
xo120r >= 0,
xo120l + xo120r == 1,
xo121l <= 1,
xo121l >= 0,
xo121r <= 1,
xo121r >= 0,
xo121l + xo121r == 1,
xo122l <= 1,
xo122l >= 0,
xo122r <= 1,
xo122r >= 0,
xo122l + xo122r == 1,
xo123l <= 1,
xo123l >= 0,
xo123r <= 1,
xo123r >= 0,
xo123l + xo123r == 1,
xo124l <= 1,
xo124l >= 0,
xo124r <= 1,
xo124r >= 0,
xo124l + xo124r == 1,
xo125l <= 1,
xo125l >= 0,
xo125r <= 1,
xo125r >= 0,
xo125l + xo125r == 1,
xo126l <= 1,
xo126l >= 0,
xo126r <= 1,
xo126r >= 0,
xo126l + xo126r == 1,
xo127l <= 1,
xo127l >= 0,
xo127r <= 1,
xo127r >= 0,
xo127l + xo127r == 1,
xo128l <= 1,
xo128l >= 0,
xo128r <= 1,
xo128r >= 0,
xo128l + xo128r == 1,
xo129l <= 1,
xo129l >= 0,
xo129r <= 1,
xo129r >= 0,
xo129l + xo129r == 1,
xo130l <= 1,
xo130l >= 0,
xo130r <= 1,
xo130r >= 0,
xo130l + xo130r == 1,
xo131l <= 1,
xo131l >= 0,
xo131r <= 1,
xo131r >= 0,
xo131l + xo131r == 1,
xo132l <= 1,
xo132l >= 0,
xo132r <= 1,
xo132r >= 0,
xo132l + xo132r == 1,
xo133l <= 1,
xo133l >= 0,
xo133r <= 1,
xo133r >= 0,
xo133l + xo133r == 1,
xo134l <= 1,
xo134l >= 0,
xo134r <= 1,
xo134r >= 0,
xo134l + xo134r == 1,
xo135l <= 1,
xo135l >= 0,
xo135r <= 1,
xo135r >= 0,
xo135l + xo135r == 1,
xo136l <= 1,
xo136l >= 0,
xo136r <= 1,
xo136r >= 0,
xo136l + xo136r == 1,
xo137l <= 1,
xo137l >= 0,
xo137r <= 1,
xo137r >= 0,
xo137l + xo137r == 1,
xo138l <= 1,
xo138l >= 0,
xo138r <= 1,
xo138r >= 0,
xo138l + xo138r == 1,
xo139l <= 1,
xo139l >= 0,
xo139r <= 1,
xo139r >= 0,
xo139l + xo139r == 1,
xo140l <= 1,
xo140l >= 0,
xo140r <= 1,
xo140r >= 0,
xo140l + xo140r == 1,
xo141l <= 1,
xo141l >= 0,
xo141r <= 1,
xo141r >= 0,
xo141l + xo141r == 1,
xo142l <= 1,
xo142l >= 0,
xo142r <= 1,
xo142r >= 0,
xo142l + xo142r == 1,
xo143l <= 1,
xo143l >= 0,
xo143r <= 1,
xo143r >= 0,
xo143l + xo143r == 1,
xo144l <= 1,
xo144l >= 0,
xo144r <= 1,
xo144r >= 0,
xo144l + xo144r == 1,
xo145l <= 1,
xo145l >= 0,
xo145r <= 1,
xo145r >= 0,
xo145l + xo145r == 1,
xo146l <= 1,
xo146l >= 0,
xo146r <= 1,
xo146r >= 0,
xo146l + xo146r == 1,
xo147l <= 1,
xo147l >= 0,
xo147r <= 1,
xo147r >= 0,
xo147l + xo147r == 1,
xo148l <= 1,
xo148l >= 0,
xo148r <= 1,
xo148r >= 0,
xo148l + xo148r == 1,
xo149l <= 1,
xo149l >= 0,
xo149r <= 1,
xo149r >= 0,
xo149l + xo149r == 1,
xo150l <= 1,
xo150l >= 0,
xo150r <= 1,
xo150r >= 0,
xo150l + xo150r == 1,
xo151l <= 1,
xo151l >= 0,
xo151r <= 1,
xo151r >= 0,
xo151l + xo151r == 1,
xo152l <= 1,
xo152l >= 0,
xo152r <= 1,
xo152r >= 0,
xo152l + xo152r == 1,
xo153l <= 1,
xo153l >= 0,
xo153r <= 1,
xo153r >= 0,
xo153l + xo153r == 1,
xo154l <= 1,
xo154l >= 0,
xo154r <= 1,
xo154r >= 0,
xo154l + xo154r == 1,
xo155l <= 1,
xo155l >= 0,
xo155r <= 1,
xo155r >= 0,
xo155l + xo155r == 1,
xo156l <= 1,
xo156l >= 0,
xo156r <= 1,
xo156r >= 0,
xo156l + xo156r == 1,
xo157l <= 1,
xo157l >= 0,
xo157r <= 1,
xo157r >= 0,
xo157l + xo157r == 1,
xo158l <= 1,
xo158l >= 0,
xo158r <= 1,
xo158r >= 0,
xo158l + xo158r == 1,
xo159l <= 1,
xo159l >= 0,
xo159r <= 1,
xo159r >= 0,
xo159l + xo159r == 1,
xo160l <= 1,
xo160l >= 0,
xo160r <= 1,
xo160r >= 0,
xo160l + xo160r == 1,
xo161l <= 1,
xo161l >= 0,
xo161r <= 1,
xo161r >= 0,
xo161l + xo161r == 1,
xo162l <= 1,
xo162l >= 0,
xo162r <= 1,
xo162r >= 0,
xo162l + xo162r == 1,
xo163l <= 1,
xo163l >= 0,
xo163r <= 1,
xo163r >= 0,
xo163l + xo163r == 1,
xo164l <= 1,
xo164l >= 0,
xo164r <= 1,
xo164r >= 0,
xo164l + xo164r == 1,
xo165l <= 1,
xo165l >= 0,
xo165r <= 1,
xo165r >= 0,
xo165l + xo165r == 1,
xo166l <= 1,
xo166l >= 0,
xo166r <= 1,
xo166r >= 0,
xo166l + xo166r == 1,
xo167l <= 1,
xo167l >= 0,
xo167r <= 1,
xo167r >= 0,
xo167l + xo167r == 1,
xo168l <= 1,
xo168l >= 0,
xo168r <= 1,
xo168r >= 0,
xo168l + xo168r == 1,
xo169l <= 1,
xo169l >= 0,
xo169r <= 1,
xo169r >= 0,
xo169l + xo169r == 1,
xo170l <= 1,
xo170l >= 0,
xo170r <= 1,
xo170r >= 0,
xo170l + xo170r == 1,
xo171l <= 1,
xo171l >= 0,
xo171r <= 1,
xo171r >= 0,
xo171l + xo171r == 1,
xo172l <= 1,
xo172l >= 0,
xo172r <= 1,
xo172r >= 0,
xo172l + xo172r == 1,
xo173l <= 1,
xo173l >= 0,
xo173r <= 1,
xo173r >= 0,
xo173l + xo173r == 1,
xo174l <= 1,
xo174l >= 0,
xo174r <= 1,
xo174r >= 0,
xo174l + xo174r == 1,
xo175l <= 1,
xo175l >= 0,
xo175r <= 1,
xo175r >= 0,
xo175l + xo175r == 1,
xo176l <= 1,
xo176l >= 0,
xo176r <= 1,
xo176r >= 0,
xo176l + xo176r == 1,
xo177l <= 1,
xo177l >= 0,
xo177r <= 1,
xo177r >= 0,
xo177l + xo177r == 1,
xo178l <= 1,
xo178l >= 0,
xo178r <= 1,
xo178r >= 0,
xo178l + xo178r == 1,
xo179l <= 1,
xo179l >= 0,
xo179r <= 1,
xo179r >= 0,
xo179l + xo179r == 1,
xo180l <= 1,
xo180l >= 0,
xo180r <= 1,
xo180r >= 0,
xo180l + xo180r == 1,
xo181l <= 1,
xo181l >= 0,
xo181r <= 1,
xo181r >= 0,
xo181l + xo181r == 1,
xo182l <= 1,
xo182l >= 0,
xo182r <= 1,
xo182r >= 0,
xo182l + xo182r == 1,
xo183l <= 1,
xo183l >= 0,
xo183r <= 1,
xo183r >= 0,
xo183l + xo183r == 1,
xo184l <= 1,
xo184l >= 0,
xo184r <= 1,
xo184r >= 0,
xo184l + xo184r == 1,
xo185l <= 1,
xo185l >= 0,
xo185r <= 1,
xo185r >= 0,
xo185l + xo185r == 1,
xo186l <= 1,
xo186l >= 0,
xo186r <= 1,
xo186r >= 0,
xo186l + xo186r == 1,
xo187l <= 1,
xo187l >= 0,
xo187r <= 1,
xo187r >= 0,
xo187l + xo187r == 1,
xo188l <= 1,
xo188l >= 0,
xo188r <= 1,
xo188r >= 0,
xo188l + xo188r == 1,
xo189l <= 1,
xo189l >= 0,
xo189r <= 1,
xo189r >= 0,
xo189l + xo189r == 1,
xo190l <= 1,
xo190l >= 0,
xo190r <= 1,
xo190r >= 0,
xo190l + xo190r == 1,
xo191l <= 1,
xo191l >= 0,
xo191r <= 1,
xo191r >= 0,
xo191l + xo191r == 1,
xo192l <= 1,
xo192l >= 0,
xo192r <= 1,
xo192r >= 0,
xo192l + xo192r == 1,
xo193l <= 1,
xo193l >= 0,
xo193r <= 1,
xo193r >= 0,
xo193l + xo193r == 1,
xo194l <= 1,
xo194l >= 0,
xo194r <= 1,
xo194r >= 0,
xo194l + xo194r == 1,
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
Or(xo4l == 0 , xo4l == 1),
Or(xo4r == 0 , xo4r == 1),
Or(xo5l == 0 , xo5l == 1),
Or(xo5r == 0 , xo5r == 1),
Or(xo6l == 0 , xo6l == 1),
Or(xo6r == 0 , xo6r == 1),
Or(xo7l == 0 , xo7l == 1),
Or(xo7r == 0 , xo7r == 1),
Or(xo8l == 0 , xo8l == 1),
Or(xo8r == 0 , xo8r == 1),
Or(xo9l == 0 , xo9l == 1),
Or(xo9r == 0 , xo9r == 1),
Or(xo10l == 0 , xo10l == 1),
Or(xo10r == 0 , xo10r == 1),
Or(xo11l == 0 , xo11l == 1),
Or(xo11r == 0 , xo11r == 1),
Or(xo12l == 0 , xo12l == 1),
Or(xo12r == 0 , xo12r == 1),
Or(xo13l == 0 , xo13l == 1),
Or(xo13r == 0 , xo13r == 1),
Or(xo14l == 0 , xo14l == 1),
Or(xo14r == 0 , xo14r == 1),
Or(xo15l == 0 , xo15l == 1),
Or(xo15r == 0 , xo15r == 1),
Or(xo16l == 0 , xo16l == 1),
Or(xo16r == 0 , xo16r == 1),
Or(xo17l == 0 , xo17l == 1),
Or(xo17r == 0 , xo17r == 1),
Or(xo18l == 0 , xo18l == 1),
Or(xo18r == 0 , xo18r == 1),
Or(xo19l == 0 , xo19l == 1),
Or(xo19r == 0 , xo19r == 1),
Or(xo20l == 0 , xo20l == 1),
Or(xo20r == 0 , xo20r == 1),
Or(xo21l == 0 , xo21l == 1),
Or(xo21r == 0 , xo21r == 1),
Or(xo22l == 0 , xo22l == 1),
Or(xo22r == 0 , xo22r == 1),
Or(xo23l == 0 , xo23l == 1),
Or(xo23r == 0 , xo23r == 1),
Or(xo24l == 0 , xo24l == 1),
Or(xo24r == 0 , xo24r == 1),
Or(xo25l == 0 , xo25l == 1),
Or(xo25r == 0 , xo25r == 1),
Or(xo26l == 0 , xo26l == 1),
Or(xo26r == 0 , xo26r == 1),
Or(xo27l == 0 , xo27l == 1),
Or(xo27r == 0 , xo27r == 1),
Or(xo28l == 0 , xo28l == 1),
Or(xo28r == 0 , xo28r == 1),
Or(xo29l == 0 , xo29l == 1),
Or(xo29r == 0 , xo29r == 1),
Or(xo30l == 0 , xo30l == 1),
Or(xo30r == 0 , xo30r == 1),
Or(xo31l == 0 , xo31l == 1),
Or(xo31r == 0 , xo31r == 1),
Or(xo32l == 0 , xo32l == 1),
Or(xo32r == 0 , xo32r == 1),
Or(xo33l == 0 , xo33l == 1),
Or(xo33r == 0 , xo33r == 1),
Or(xo34l == 0 , xo34l == 1),
Or(xo34r == 0 , xo34r == 1),
Or(xo35l == 0 , xo35l == 1),
Or(xo35r == 0 , xo35r == 1),
Or(xo36l == 0 , xo36l == 1),
Or(xo36r == 0 , xo36r == 1),
Or(xo37l == 0 , xo37l == 1),
Or(xo37r == 0 , xo37r == 1),
Or(xo38l == 0 , xo38l == 1),
Or(xo38r == 0 , xo38r == 1),
Or(xo39l == 0 , xo39l == 1),
Or(xo39r == 0 , xo39r == 1),
Or(xo40l == 0 , xo40l == 1),
Or(xo40r == 0 , xo40r == 1),
Or(xo41l == 0 , xo41l == 1),
Or(xo41r == 0 , xo41r == 1),
Or(xo42l == 0 , xo42l == 1),
Or(xo42r == 0 , xo42r == 1),
Or(xo43l == 0 , xo43l == 1),
Or(xo43r == 0 , xo43r == 1),
Or(xo44l == 0 , xo44l == 1),
Or(xo44r == 0 , xo44r == 1),
Or(xo45l == 0 , xo45l == 1),
Or(xo45r == 0 , xo45r == 1),
Or(xo46l == 0 , xo46l == 1),
Or(xo46r == 0 , xo46r == 1),
Or(xo47l == 0 , xo47l == 1),
Or(xo47r == 0 , xo47r == 1),
Or(xo48l == 0 , xo48l == 1),
Or(xo48r == 0 , xo48r == 1),
Or(xo49l == 0 , xo49l == 1),
Or(xo49r == 0 , xo49r == 1),
Or(xo50l == 0 , xo50l == 1),
Or(xo50r == 0 , xo50r == 1),
Or(xo51l == 0 , xo51l == 1),
Or(xo51r == 0 , xo51r == 1),
Or(xo52l == 0 , xo52l == 1),
Or(xo52r == 0 , xo52r == 1),
Or(xo53l == 0 , xo53l == 1),
Or(xo53r == 0 , xo53r == 1),
Or(xo54l == 0 , xo54l == 1),
Or(xo54r == 0 , xo54r == 1),
Or(xo55l == 0 , xo55l == 1),
Or(xo55r == 0 , xo55r == 1),
Or(xo56l == 0 , xo56l == 1),
Or(xo56r == 0 , xo56r == 1),
Or(xo57l == 0 , xo57l == 1),
Or(xo57r == 0 , xo57r == 1),
Or(xo58l == 0 , xo58l == 1),
Or(xo58r == 0 , xo58r == 1),
Or(xo59l == 0 , xo59l == 1),
Or(xo59r == 0 , xo59r == 1),
Or(xo60l == 0 , xo60l == 1),
Or(xo60r == 0 , xo60r == 1),
Or(xo61l == 0 , xo61l == 1),
Or(xo61r == 0 , xo61r == 1),
Or(xo62l == 0 , xo62l == 1),
Or(xo62r == 0 , xo62r == 1),
Or(xo63l == 0 , xo63l == 1),
Or(xo63r == 0 , xo63r == 1),
Or(xo64l == 0 , xo64l == 1),
Or(xo64r == 0 , xo64r == 1),
Or(xo65l == 0 , xo65l == 1),
Or(xo65r == 0 , xo65r == 1),
Or(xo66l == 0 , xo66l == 1),
Or(xo66r == 0 , xo66r == 1),
Or(xo67l == 0 , xo67l == 1),
Or(xo67r == 0 , xo67r == 1),
Or(xo68l == 0 , xo68l == 1),
Or(xo68r == 0 , xo68r == 1),
Or(xo69l == 0 , xo69l == 1),
Or(xo69r == 0 , xo69r == 1),
Or(xo70l == 0 , xo70l == 1),
Or(xo70r == 0 , xo70r == 1),
Or(xo71l == 0 , xo71l == 1),
Or(xo71r == 0 , xo71r == 1),
Or(xo72l == 0 , xo72l == 1),
Or(xo72r == 0 , xo72r == 1),
Or(xo73l == 0 , xo73l == 1),
Or(xo73r == 0 , xo73r == 1),
Or(xo74l == 0 , xo74l == 1),
Or(xo74r == 0 , xo74r == 1),
Or(xo75l == 0 , xo75l == 1),
Or(xo75r == 0 , xo75r == 1),
Or(xo76l == 0 , xo76l == 1),
Or(xo76r == 0 , xo76r == 1),
Or(xo77l == 0 , xo77l == 1),
Or(xo77r == 0 , xo77r == 1),
Or(xo78l == 0 , xo78l == 1),
Or(xo78r == 0 , xo78r == 1),
Or(xo79l == 0 , xo79l == 1),
Or(xo79r == 0 , xo79r == 1),
Or(xo80l == 0 , xo80l == 1),
Or(xo80r == 0 , xo80r == 1),
Or(xo81l == 0 , xo81l == 1),
Or(xo81r == 0 , xo81r == 1),
Or(xo82l == 0 , xo82l == 1),
Or(xo82r == 0 , xo82r == 1),
Or(xo83l == 0 , xo83l == 1),
Or(xo83r == 0 , xo83r == 1),
Or(xo84l == 0 , xo84l == 1),
Or(xo84r == 0 , xo84r == 1),
Or(xo85l == 0 , xo85l == 1),
Or(xo85r == 0 , xo85r == 1),
Or(xo86l == 0 , xo86l == 1),
Or(xo86r == 0 , xo86r == 1),
Or(xo87l == 0 , xo87l == 1),
Or(xo87r == 0 , xo87r == 1),
Or(xo88l == 0 , xo88l == 1),
Or(xo88r == 0 , xo88r == 1),
Or(xo89l == 0 , xo89l == 1),
Or(xo89r == 0 , xo89r == 1),
Or(xo90l == 0 , xo90l == 1),
Or(xo90r == 0 , xo90r == 1),
Or(xo91l == 0 , xo91l == 1),
Or(xo91r == 0 , xo91r == 1),
Or(xo92l == 0 , xo92l == 1),
Or(xo92r == 0 , xo92r == 1),
Or(xo93l == 0 , xo93l == 1),
Or(xo93r == 0 , xo93r == 1),
Or(xo94l == 0 , xo94l == 1),
Or(xo94r == 0 , xo94r == 1),
Or(xo95l == 0 , xo95l == 1),
Or(xo95r == 0 , xo95r == 1),
Or(xo96l == 0 , xo96l == 1),
Or(xo96r == 0 , xo96r == 1),
Or(xo98l == 0 , xo98l == 1),
Or(xo98r == 0 , xo98r == 1),
Or(xo99l == 0 , xo99l == 1),
Or(xo99r == 0 , xo99r == 1),
Or(xo100l == 0 , xo100l == 1),
Or(xo100r == 0 , xo100r == 1),
Or(xo101l == 0 , xo101l == 1),
Or(xo101r == 0 , xo101r == 1),
Or(xo102l == 0 , xo102l == 1),
Or(xo102r == 0 , xo102r == 1),
Or(xo103l == 0 , xo103l == 1),
Or(xo103r == 0 , xo103r == 1),
Or(xo104l == 0 , xo104l == 1),
Or(xo104r == 0 , xo104r == 1),
Or(xo105l == 0 , xo105l == 1),
Or(xo105r == 0 , xo105r == 1),
Or(xo106l == 0 , xo106l == 1),
Or(xo106r == 0 , xo106r == 1),
Or(xo107l == 0 , xo107l == 1),
Or(xo107r == 0 , xo107r == 1),
Or(xo108l == 0 , xo108l == 1),
Or(xo108r == 0 , xo108r == 1),
Or(xo109l == 0 , xo109l == 1),
Or(xo109r == 0 , xo109r == 1),
Or(xo110l == 0 , xo110l == 1),
Or(xo110r == 0 , xo110r == 1),
Or(xo111l == 0 , xo111l == 1),
Or(xo111r == 0 , xo111r == 1),
Or(xo112l == 0 , xo112l == 1),
Or(xo112r == 0 , xo112r == 1),
Or(xo113l == 0 , xo113l == 1),
Or(xo113r == 0 , xo113r == 1),
Or(xo114l == 0 , xo114l == 1),
Or(xo114r == 0 , xo114r == 1),
Or(xo115l == 0 , xo115l == 1),
Or(xo115r == 0 , xo115r == 1),
Or(xo116l == 0 , xo116l == 1),
Or(xo116r == 0 , xo116r == 1),
Or(xo117l == 0 , xo117l == 1),
Or(xo117r == 0 , xo117r == 1),
Or(xo118l == 0 , xo118l == 1),
Or(xo118r == 0 , xo118r == 1),
Or(xo119l == 0 , xo119l == 1),
Or(xo119r == 0 , xo119r == 1),
Or(xo120l == 0 , xo120l == 1),
Or(xo120r == 0 , xo120r == 1),
Or(xo121l == 0 , xo121l == 1),
Or(xo121r == 0 , xo121r == 1),
Or(xo122l == 0 , xo122l == 1),
Or(xo122r == 0 , xo122r == 1),
Or(xo123l == 0 , xo123l == 1),
Or(xo123r == 0 , xo123r == 1),
Or(xo124l == 0 , xo124l == 1),
Or(xo124r == 0 , xo124r == 1),
Or(xo125l == 0 , xo125l == 1),
Or(xo125r == 0 , xo125r == 1),
Or(xo126l == 0 , xo126l == 1),
Or(xo126r == 0 , xo126r == 1),
Or(xo127l == 0 , xo127l == 1),
Or(xo127r == 0 , xo127r == 1),
Or(xo128l == 0 , xo128l == 1),
Or(xo128r == 0 , xo128r == 1),
Or(xo129l == 0 , xo129l == 1),
Or(xo129r == 0 , xo129r == 1),
Or(xo130l == 0 , xo130l == 1),
Or(xo130r == 0 , xo130r == 1),
Or(xo131l == 0 , xo131l == 1),
Or(xo131r == 0 , xo131r == 1),
Or(xo132l == 0 , xo132l == 1),
Or(xo132r == 0 , xo132r == 1),
Or(xo133l == 0 , xo133l == 1),
Or(xo133r == 0 , xo133r == 1),
Or(xo134l == 0 , xo134l == 1),
Or(xo134r == 0 , xo134r == 1),
Or(xo135l == 0 , xo135l == 1),
Or(xo135r == 0 , xo135r == 1),
Or(xo136l == 0 , xo136l == 1),
Or(xo136r == 0 , xo136r == 1),
Or(xo137l == 0 , xo137l == 1),
Or(xo137r == 0 , xo137r == 1),
Or(xo138l == 0 , xo138l == 1),
Or(xo138r == 0 , xo138r == 1),
Or(xo139l == 0 , xo139l == 1),
Or(xo139r == 0 , xo139r == 1),
Or(xo140l == 0 , xo140l == 1),
Or(xo140r == 0 , xo140r == 1),
Or(xo141l == 0 , xo141l == 1),
Or(xo141r == 0 , xo141r == 1),
Or(xo142l == 0 , xo142l == 1),
Or(xo142r == 0 , xo142r == 1),
Or(xo143l == 0 , xo143l == 1),
Or(xo143r == 0 , xo143r == 1),
Or(xo144l == 0 , xo144l == 1),
Or(xo144r == 0 , xo144r == 1),
Or(xo145l == 0 , xo145l == 1),
Or(xo145r == 0 , xo145r == 1),
Or(xo146l == 0 , xo146l == 1),
Or(xo146r == 0 , xo146r == 1),
Or(xo147l == 0 , xo147l == 1),
Or(xo147r == 0 , xo147r == 1),
Or(xo148l == 0 , xo148l == 1),
Or(xo148r == 0 , xo148r == 1),
Or(xo149l == 0 , xo149l == 1),
Or(xo149r == 0 , xo149r == 1),
Or(xo150l == 0 , xo150l == 1),
Or(xo150r == 0 , xo150r == 1),
Or(xo151l == 0 , xo151l == 1),
Or(xo151r == 0 , xo151r == 1),
Or(xo152l == 0 , xo152l == 1),
Or(xo152r == 0 , xo152r == 1),
Or(xo153l == 0 , xo153l == 1),
Or(xo153r == 0 , xo153r == 1),
Or(xo154l == 0 , xo154l == 1),
Or(xo154r == 0 , xo154r == 1),
Or(xo155l == 0 , xo155l == 1),
Or(xo155r == 0 , xo155r == 1),
Or(xo156l == 0 , xo156l == 1),
Or(xo156r == 0 , xo156r == 1),
Or(xo157l == 0 , xo157l == 1),
Or(xo157r == 0 , xo157r == 1),
Or(xo158l == 0 , xo158l == 1),
Or(xo158r == 0 , xo158r == 1),
Or(xo159l == 0 , xo159l == 1),
Or(xo159r == 0 , xo159r == 1),
Or(xo160l == 0 , xo160l == 1),
Or(xo160r == 0 , xo160r == 1),
Or(xo161l == 0 , xo161l == 1),
Or(xo161r == 0 , xo161r == 1),
Or(xo162l == 0 , xo162l == 1),
Or(xo162r == 0 , xo162r == 1),
Or(xo163l == 0 , xo163l == 1),
Or(xo163r == 0 , xo163r == 1),
Or(xo164l == 0 , xo164l == 1),
Or(xo164r == 0 , xo164r == 1),
Or(xo165l == 0 , xo165l == 1),
Or(xo165r == 0 , xo165r == 1),
Or(xo166l == 0 , xo166l == 1),
Or(xo166r == 0 , xo166r == 1),
Or(xo167l == 0 , xo167l == 1),
Or(xo167r == 0 , xo167r == 1),
Or(xo168l == 0 , xo168l == 1),
Or(xo168r == 0 , xo168r == 1),
Or(xo169l == 0 , xo169l == 1),
Or(xo169r == 0 , xo169r == 1),
Or(xo170l == 0 , xo170l == 1),
Or(xo170r == 0 , xo170r == 1),
Or(xo171l == 0 , xo171l == 1),
Or(xo171r == 0 , xo171r == 1),
Or(xo172l == 0 , xo172l == 1),
Or(xo172r == 0 , xo172r == 1),
Or(xo173l == 0 , xo173l == 1),
Or(xo173r == 0 , xo173r == 1),
Or(xo174l == 0 , xo174l == 1),
Or(xo174r == 0 , xo174r == 1),
Or(xo175l == 0 , xo175l == 1),
Or(xo175r == 0 , xo175r == 1),
Or(xo176l == 0 , xo176l == 1),
Or(xo176r == 0 , xo176r == 1),
Or(xo177l == 0 , xo177l == 1),
Or(xo177r == 0 , xo177r == 1),
Or(xo178l == 0 , xo178l == 1),
Or(xo178r == 0 , xo178r == 1),
Or(xo179l == 0 , xo179l == 1),
Or(xo179r == 0 , xo179r == 1),
Or(xo180l == 0 , xo180l == 1),
Or(xo180r == 0 , xo180r == 1),
Or(xo181l == 0 , xo181l == 1),
Or(xo181r == 0 , xo181r == 1),
Or(xo182l == 0 , xo182l == 1),
Or(xo182r == 0 , xo182r == 1),
Or(xo183l == 0 , xo183l == 1),
Or(xo183r == 0 , xo183r == 1),
Or(xo184l == 0 , xo184l == 1),
Or(xo184r == 0 , xo184r == 1),
Or(xo185l == 0 , xo185l == 1),
Or(xo185r == 0 , xo185r == 1),
Or(xo186l == 0 , xo186l == 1),
Or(xo186r == 0 , xo186r == 1),
Or(xo187l == 0 , xo187l == 1),
Or(xo187r == 0 , xo187r == 1),
Or(xo188l == 0 , xo188l == 1),
Or(xo188r == 0 , xo188r == 1),
Or(xo189l == 0 , xo189l == 1),
Or(xo189r == 0 , xo189r == 1),
Or(xo190l == 0 , xo190l == 1),
Or(xo190r == 0 , xo190r == 1),
Or(xo191l == 0 , xo191l == 1),
Or(xo191r == 0 , xo191r == 1),
Or(xo192l == 0 , xo192l == 1),
Or(xo192r == 0 , xo192r == 1),
Or(xo193l == 0 , xo193l == 1),
Or(xo193r == 0 , xo193r == 1),
Or(xo194l == 0 , xo194l == 1),
Or(xo194r == 0 , xo194r == 1),
Or(xol == 0 , xol == 1),
Or(xor == 0 , xor == 1),
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
Or (y119 == 0 , y119 == 1 ),
Or (y120 == 0 , y120 == 1 ),
Or (y121 == 0 , y121 == 1 ),
Or (y122 == 0 , y122 == 1 ),
Or (y123 == 0 , y123 == 1 ),
Or (y124 == 0 , y124 == 1 ),
Or (y125 == 0 , y125 == 1 ),
Or (y126 == 0 , y126 == 1 ),
Or (y127 == 0 , y127 == 1 ),
Or (y128 == 0 , y128 == 1 ),
Or (y129 == 0 , y129 == 1 ),
Or (y130 == 0 , y130 == 1 ),
Or (y131 == 0 , y131 == 1 ),
Or (y132 == 0 , y132 == 1 ),
Or (y133 == 0 , y133 == 1 ),
Or (y134 == 0 , y134 == 1 ),
Or (y135 == 0 , y135 == 1 ),
Or (y136 == 0 , y136 == 1 ),
Or (y137 == 0 , y137 == 1 ),
Or (y138 == 0 , y138 == 1 ),
Or (y139 == 0 , y139 == 1 ),
Or (y140 == 0 , y140 == 1 ),
Or (y141 == 0 , y141 == 1 ),
Or (y142 == 0 , y142 == 1 ),
Or (y143 == 0 , y143 == 1 ),
Or (y144 == 0 , y144 == 1 ),
Or (y145 == 0 , y145 == 1 ),
Or (y146 == 0 , y146 == 1 ),
Or (y147 == 0 , y147 == 1 ),
Or (y148 == 0 , y148 == 1 ),
Or (y149 == 0 , y149 == 1 ),
Or (y150 == 0 , y150 == 1 ),
Or (y151 == 0 , y151 == 1 ),
Or (y152 == 0 , y152 == 1 ),
Or (y153 == 0 , y153 == 1 ),
Or (y154 == 0 , y154 == 1 ),
Or (y155 == 0 , y155 == 1 ),
Or (y156 == 0 , y156 == 1 ),
Or (y157 == 0 , y157 == 1 ),
Or (y158 == 0 , y158 == 1 ),
Or (y159 == 0 , y159 == 1 ),
Or (y160 == 0 , y160 == 1 ),
Or (y161 == 0 , y161 == 1 ),
Or (y162 == 0 , y162 == 1 ),
Or (y163 == 0 , y163 == 1 ),
Or (y164 == 0 , y164 == 1 ),
Or (y165 == 0 , y165 == 1 ),
Or (y166 == 0 , y166 == 1 ),
Or (y167 == 0 , y167 == 1 ),
Or (y168 == 0 , y168 == 1 ),
Or (y169 == 0 , y169 == 1 ),
Or (y170 == 0 , y170 == 1 ),
Or (y171 == 0 , y171 == 1 ),
Or (y172 == 0 , y172 == 1 ),
Or (y173 == 0 , y173 == 1 ),
Or (y174 == 0 , y174 == 1 ),
Or (y175 == 0 , y175 == 1 ),
Or (y176 == 0 , y176 == 1 ),
Or (y177 == 0 , y177 == 1 ),
Or (y178 == 0 , y178 == 1 ),
Or (y179 == 0 , y179 == 1 ),
Or (y180 == 0 , y180 == 1 ),
Or (y181 == 0 , y181 == 1 ),
Or (y182 == 0 , y182 == 1 ),
Or (y183 == 0 , y183 == 1 ),
Or (y184 == 0 , y184 == 1 ),
Or (y185 == 0 , y185 == 1 ),
Or (y186 == 0 , y186 == 1 ),
Or (y187 == 0 , y187 == 1 ),
Or (y188 == 0 , y188 == 1 ),
Or (y189 == 0 , y189 == 1 ),
Or (y190 == 0 , y190 == 1 ),
Or (y191 == 0 , y191 == 1 ),
Or (y192 == 0 , y192 == 1 ),
Or (y193 == 0 , y193 == 1 ),
Or (y194 == 0 , y194 == 1 ),
y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 + y40 + y41 + y42 + y43 + y44 + y45 + y46 + y47 + y48 + y49 + y50 + y51 + y52 + y53 + y54 + y55 + y56 + y57 + y58 + y59 + y60 + y61 + y62 + y63 + y64 + y65 + y66 + y67 + y68 + y69 + y70 + y71 + y72 + y73 + y74 + y75 + y76 + y77 + y78 + y79 + y80 + y81 + y82 + y83 + y84 + y85 + y86 + y87 + y88 + y89 + y90 + y91 + y92 + y93 + y94 + y95 + y96 + y98 + y99 + y100 + y101 + y102 + y103 + y104 + y105 + y106 + y107 + y108 + y109 + y110 + y111 + y112 + y113 + y114 + y115 + y116 + y117 + y118 + y119 + y120 + y121 + y122 + y123 + y124 + y125 + y126 + y127 + y128 + y129 + y130 + y131 + y132 + y133 + y134 + y135 + y136 + y137 + y138 + y139 + y140 + y141 + y142 + y143 + y144 + y145 + y146 + y147 + y148 + y149 + y150 + y151 + y152 + y153 + y154 + y155 + y156 + y157 + y158 + y159 + y160 + y161 + y162 + y163 + y164 + y165 + y166 + y167 + y168 + y169 + y170 + y171 + y172 + y173 + y174 + y175 + y176 + y177 + y178 + y179 + y180 + y181 + y182 + y183 + y184 + y185 + y186 + y187 + y188 + y189 + y190 + y191 + y192 + y193 + y194 == 97
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')