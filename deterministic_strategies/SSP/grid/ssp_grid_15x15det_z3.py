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
pi195 = Real('pi195')
pi196 = Real('pi196')
pi197 = Real('pi197')
pi198 = Real('pi198')
pi199 = Real('pi199')
pi200 = Real('pi200')
pi201 = Real('pi201')
pi202 = Real('pi202')
pi203 = Real('pi203')
pi204 = Real('pi204')
pi205 = Real('pi205')
pi206 = Real('pi206')
pi207 = Real('pi207')
pi208 = Real('pi208')
pi209 = Real('pi209')
pi210 = Real('pi210')
pi211 = Real('pi211')
pi212 = Real('pi212')
pi213 = Real('pi213')
pi214 = Real('pi214')
pi215 = Real('pi215')
pi216 = Real('pi216')
pi217 = Real('pi217')
pi218 = Real('pi218')
pi219 = Real('pi219')
pi220 = Real('pi220')
pi221 = Real('pi221')
pi222 = Real('pi222')
pi223 = Real('pi223')
pi224 = Real('pi224')

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
y195 = Real('y195')
y196 = Real('y196')
y197 = Real('y197')
y198 = Real('y198')
y199 = Real('y199')
y200 = Real('y200')
y201 = Real('y201')
y202 = Real('y202')
y203 = Real('y203')
y204 = Real('y204')
y205 = Real('y205')
y206 = Real('y206')
y207 = Real('y207')
y208 = Real('y208')
y209 = Real('y209')
y210 = Real('y210')
y211 = Real('y211')
y212 = Real('y212')
y213 = Real('y213')
y214 = Real('y214')
y215 = Real('y215')
y216 = Real('y216')
y217 = Real('y217')
y218 = Real('y218')
y219 = Real('y219')
y220 = Real('y220')
y221 = Real('y221')
y222 = Real('y222')
y223 = Real('y223')

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
xo121l = Real('xo121l')
xo121r = Real('xo121r')
xo121u = Real('xo121u')
xo121d = Real('xo121d')
xo122l = Real('xo122l')
xo122r = Real('xo122r')
xo122u = Real('xo122u')
xo122d = Real('xo122d')
xo123l = Real('xo123l')
xo123r = Real('xo123r')
xo123u = Real('xo123u')
xo123d = Real('xo123d')
xo124l = Real('xo124l')
xo124r = Real('xo124r')
xo124u = Real('xo124u')
xo124d = Real('xo124d')
xo125l = Real('xo125l')
xo125r = Real('xo125r')
xo125u = Real('xo125u')
xo125d = Real('xo125d')
xo126l = Real('xo126l')
xo126r = Real('xo126r')
xo126u = Real('xo126u')
xo126d = Real('xo126d')
xo127l = Real('xo127l')
xo127r = Real('xo127r')
xo127u = Real('xo127u')
xo127d = Real('xo127d')
xo128l = Real('xo128l')
xo128r = Real('xo128r')
xo128u = Real('xo128u')
xo128d = Real('xo128d')
xo129l = Real('xo129l')
xo129r = Real('xo129r')
xo129u = Real('xo129u')
xo129d = Real('xo129d')
xo130l = Real('xo130l')
xo130r = Real('xo130r')
xo130u = Real('xo130u')
xo130d = Real('xo130d')
xo131l = Real('xo131l')
xo131r = Real('xo131r')
xo131u = Real('xo131u')
xo131d = Real('xo131d')
xo132l = Real('xo132l')
xo132r = Real('xo132r')
xo132u = Real('xo132u')
xo132d = Real('xo132d')
xo133l = Real('xo133l')
xo133r = Real('xo133r')
xo133u = Real('xo133u')
xo133d = Real('xo133d')
xo134l = Real('xo134l')
xo134r = Real('xo134r')
xo134u = Real('xo134u')
xo134d = Real('xo134d')
xo135l = Real('xo135l')
xo135r = Real('xo135r')
xo135u = Real('xo135u')
xo135d = Real('xo135d')
xo136l = Real('xo136l')
xo136r = Real('xo136r')
xo136u = Real('xo136u')
xo136d = Real('xo136d')
xo137l = Real('xo137l')
xo137r = Real('xo137r')
xo137u = Real('xo137u')
xo137d = Real('xo137d')
xo138l = Real('xo138l')
xo138r = Real('xo138r')
xo138u = Real('xo138u')
xo138d = Real('xo138d')
xo139l = Real('xo139l')
xo139r = Real('xo139r')
xo139u = Real('xo139u')
xo139d = Real('xo139d')
xo140l = Real('xo140l')
xo140r = Real('xo140r')
xo140u = Real('xo140u')
xo140d = Real('xo140d')
xo141l = Real('xo141l')
xo141r = Real('xo141r')
xo141u = Real('xo141u')
xo141d = Real('xo141d')
xo142l = Real('xo142l')
xo142r = Real('xo142r')
xo142u = Real('xo142u')
xo142d = Real('xo142d')
xo143l = Real('xo143l')
xo143r = Real('xo143r')
xo143u = Real('xo143u')
xo143d = Real('xo143d')
xo144l = Real('xo144l')
xo144r = Real('xo144r')
xo144u = Real('xo144u')
xo144d = Real('xo144d')
xo145l = Real('xo145l')
xo145r = Real('xo145r')
xo145u = Real('xo145u')
xo145d = Real('xo145d')
xo146l = Real('xo146l')
xo146r = Real('xo146r')
xo146u = Real('xo146u')
xo146d = Real('xo146d')
xo147l = Real('xo147l')
xo147r = Real('xo147r')
xo147u = Real('xo147u')
xo147d = Real('xo147d')
xo148l = Real('xo148l')
xo148r = Real('xo148r')
xo148u = Real('xo148u')
xo148d = Real('xo148d')
xo149l = Real('xo149l')
xo149r = Real('xo149r')
xo149u = Real('xo149u')
xo149d = Real('xo149d')
xo150l = Real('xo150l')
xo150r = Real('xo150r')
xo150u = Real('xo150u')
xo150d = Real('xo150d')
xo151l = Real('xo151l')
xo151r = Real('xo151r')
xo151u = Real('xo151u')
xo151d = Real('xo151d')
xo152l = Real('xo152l')
xo152r = Real('xo152r')
xo152u = Real('xo152u')
xo152d = Real('xo152d')
xo153l = Real('xo153l')
xo153r = Real('xo153r')
xo153u = Real('xo153u')
xo153d = Real('xo153d')
xo154l = Real('xo154l')
xo154r = Real('xo154r')
xo154u = Real('xo154u')
xo154d = Real('xo154d')
xo155l = Real('xo155l')
xo155r = Real('xo155r')
xo155u = Real('xo155u')
xo155d = Real('xo155d')
xo156l = Real('xo156l')
xo156r = Real('xo156r')
xo156u = Real('xo156u')
xo156d = Real('xo156d')
xo157l = Real('xo157l')
xo157r = Real('xo157r')
xo157u = Real('xo157u')
xo157d = Real('xo157d')
xo158l = Real('xo158l')
xo158r = Real('xo158r')
xo158u = Real('xo158u')
xo158d = Real('xo158d')
xo159l = Real('xo159l')
xo159r = Real('xo159r')
xo159u = Real('xo159u')
xo159d = Real('xo159d')
xo160l = Real('xo160l')
xo160r = Real('xo160r')
xo160u = Real('xo160u')
xo160d = Real('xo160d')
xo161l = Real('xo161l')
xo161r = Real('xo161r')
xo161u = Real('xo161u')
xo161d = Real('xo161d')
xo162l = Real('xo162l')
xo162r = Real('xo162r')
xo162u = Real('xo162u')
xo162d = Real('xo162d')
xo163l = Real('xo163l')
xo163r = Real('xo163r')
xo163u = Real('xo163u')
xo163d = Real('xo163d')
xo164l = Real('xo164l')
xo164r = Real('xo164r')
xo164u = Real('xo164u')
xo164d = Real('xo164d')
xo165l = Real('xo165l')
xo165r = Real('xo165r')
xo165u = Real('xo165u')
xo165d = Real('xo165d')
xo166l = Real('xo166l')
xo166r = Real('xo166r')
xo166u = Real('xo166u')
xo166d = Real('xo166d')
xo167l = Real('xo167l')
xo167r = Real('xo167r')
xo167u = Real('xo167u')
xo167d = Real('xo167d')
xo168l = Real('xo168l')
xo168r = Real('xo168r')
xo168u = Real('xo168u')
xo168d = Real('xo168d')
xo169l = Real('xo169l')
xo169r = Real('xo169r')
xo169u = Real('xo169u')
xo169d = Real('xo169d')
xo170l = Real('xo170l')
xo170r = Real('xo170r')
xo170u = Real('xo170u')
xo170d = Real('xo170d')
xo171l = Real('xo171l')
xo171r = Real('xo171r')
xo171u = Real('xo171u')
xo171d = Real('xo171d')
xo172l = Real('xo172l')
xo172r = Real('xo172r')
xo172u = Real('xo172u')
xo172d = Real('xo172d')
xo173l = Real('xo173l')
xo173r = Real('xo173r')
xo173u = Real('xo173u')
xo173d = Real('xo173d')
xo174l = Real('xo174l')
xo174r = Real('xo174r')
xo174u = Real('xo174u')
xo174d = Real('xo174d')
xo175l = Real('xo175l')
xo175r = Real('xo175r')
xo175u = Real('xo175u')
xo175d = Real('xo175d')
xo176l = Real('xo176l')
xo176r = Real('xo176r')
xo176u = Real('xo176u')
xo176d = Real('xo176d')
xo177l = Real('xo177l')
xo177r = Real('xo177r')
xo177u = Real('xo177u')
xo177d = Real('xo177d')
xo178l = Real('xo178l')
xo178r = Real('xo178r')
xo178u = Real('xo178u')
xo178d = Real('xo178d')
xo179l = Real('xo179l')
xo179r = Real('xo179r')
xo179u = Real('xo179u')
xo179d = Real('xo179d')
xo180l = Real('xo180l')
xo180r = Real('xo180r')
xo180u = Real('xo180u')
xo180d = Real('xo180d')
xo181l = Real('xo181l')
xo181r = Real('xo181r')
xo181u = Real('xo181u')
xo181d = Real('xo181d')
xo182l = Real('xo182l')
xo182r = Real('xo182r')
xo182u = Real('xo182u')
xo182d = Real('xo182d')
xo183l = Real('xo183l')
xo183r = Real('xo183r')
xo183u = Real('xo183u')
xo183d = Real('xo183d')
xo184l = Real('xo184l')
xo184r = Real('xo184r')
xo184u = Real('xo184u')
xo184d = Real('xo184d')
xo185l = Real('xo185l')
xo185r = Real('xo185r')
xo185u = Real('xo185u')
xo185d = Real('xo185d')
xo186l = Real('xo186l')
xo186r = Real('xo186r')
xo186u = Real('xo186u')
xo186d = Real('xo186d')
xo187l = Real('xo187l')
xo187r = Real('xo187r')
xo187u = Real('xo187u')
xo187d = Real('xo187d')
xo188l = Real('xo188l')
xo188r = Real('xo188r')
xo188u = Real('xo188u')
xo188d = Real('xo188d')
xo189l = Real('xo189l')
xo189r = Real('xo189r')
xo189u = Real('xo189u')
xo189d = Real('xo189d')
xo190l = Real('xo190l')
xo190r = Real('xo190r')
xo190u = Real('xo190u')
xo190d = Real('xo190d')
xo191l = Real('xo191l')
xo191r = Real('xo191r')
xo191u = Real('xo191u')
xo191d = Real('xo191d')
xo192l = Real('xo192l')
xo192r = Real('xo192r')
xo192u = Real('xo192u')
xo192d = Real('xo192d')
xo193l = Real('xo193l')
xo193r = Real('xo193r')
xo193u = Real('xo193u')
xo193d = Real('xo193d')
xo194l = Real('xo194l')
xo194r = Real('xo194r')
xo194u = Real('xo194u')
xo194d = Real('xo194d')
xo195l = Real('xo195l')
xo195r = Real('xo195r')
xo195u = Real('xo195u')
xo195d = Real('xo195d')
xo196l = Real('xo196l')
xo196r = Real('xo196r')
xo196u = Real('xo196u')
xo196d = Real('xo196d')
xo197l = Real('xo197l')
xo197r = Real('xo197r')
xo197u = Real('xo197u')
xo197d = Real('xo197d')
xo198l = Real('xo198l')
xo198r = Real('xo198r')
xo198u = Real('xo198u')
xo198d = Real('xo198d')
xo199l = Real('xo199l')
xo199r = Real('xo199r')
xo199u = Real('xo199u')
xo199d = Real('xo199d')
xo200l = Real('xo200l')
xo200r = Real('xo200r')
xo200u = Real('xo200u')
xo200d = Real('xo200d')
xo201l = Real('xo201l')
xo201r = Real('xo201r')
xo201u = Real('xo201u')
xo201d = Real('xo201d')
xo202l = Real('xo202l')
xo202r = Real('xo202r')
xo202u = Real('xo202u')
xo202d = Real('xo202d')
xo203l = Real('xo203l')
xo203r = Real('xo203r')
xo203u = Real('xo203u')
xo203d = Real('xo203d')
xo204l = Real('xo204l')
xo204r = Real('xo204r')
xo204u = Real('xo204u')
xo204d = Real('xo204d')
xo205l = Real('xo205l')
xo205r = Real('xo205r')
xo205u = Real('xo205u')
xo205d = Real('xo205d')
xo206l = Real('xo206l')
xo206r = Real('xo206r')
xo206u = Real('xo206u')
xo206d = Real('xo206d')
xo207l = Real('xo207l')
xo207r = Real('xo207r')
xo207u = Real('xo207u')
xo207d = Real('xo207d')
xo208l = Real('xo208l')
xo208r = Real('xo208r')
xo208u = Real('xo208u')
xo208d = Real('xo208d')
xo209l = Real('xo209l')
xo209r = Real('xo209r')
xo209u = Real('xo209u')
xo209d = Real('xo209d')
xo210l = Real('xo210l')
xo210r = Real('xo210r')
xo210u = Real('xo210u')
xo210d = Real('xo210d')
xo211l = Real('xo211l')
xo211r = Real('xo211r')
xo211u = Real('xo211u')
xo211d = Real('xo211d')
xo212l = Real('xo212l')
xo212r = Real('xo212r')
xo212u = Real('xo212u')
xo212d = Real('xo212d')
xo213l = Real('xo213l')
xo213r = Real('xo213r')
xo213u = Real('xo213u')
xo213d = Real('xo213d')
xo214l = Real('xo214l')
xo214r = Real('xo214r')
xo214u = Real('xo214u')
xo214d = Real('xo214d')
xo215l = Real('xo215l')
xo215r = Real('xo215r')
xo215u = Real('xo215u')
xo215d = Real('xo215d')
xo216l = Real('xo216l')
xo216r = Real('xo216r')
xo216u = Real('xo216u')
xo216d = Real('xo216d')
xo217l = Real('xo217l')
xo217r = Real('xo217r')
xo217u = Real('xo217u')
xo217d = Real('xo217d')
xo218l = Real('xo218l')
xo218r = Real('xo218r')
xo218u = Real('xo218u')
xo218d = Real('xo218d')
xo219l = Real('xo219l')
xo219r = Real('xo219r')
xo219u = Real('xo219u')
xo219d = Real('xo219d')
xo220l = Real('xo220l')
xo220r = Real('xo220r')
xo220u = Real('xo220u')
xo220d = Real('xo220d')
xo221l = Real('xo221l')
xo221r = Real('xo221r')
xo221u = Real('xo221u')
xo221d = Real('xo221d')
xo222l = Real('xo222l')
xo222r = Real('xo222r')
xo222u = Real('xo222u')
xo222d = Real('xo222d')
xo223l = Real('xo223l')
xo223r = Real('xo223r')
xo223u = Real('xo223u')
xo223d = Real('xo223d')
xol = Real('xol')
xor = Real('xor')
xod = Real('xod')
xou = Real('xou')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=28, pi1>=27, pi2>=26, pi3>=25, pi4>=24, pi5>=23, pi6>=22, pi7>=21, pi8>=20, pi9>=19, pi10>=18, pi11>=17, pi12>=16, pi13>=15, pi14>=14, pi15>=27, pi16>=26, pi17>=25, pi18>=24, pi19>=23, pi20>=22, pi21>=21, pi22>=20, pi23>=19, pi24>=18, pi25>=17, pi26>=16, pi27>=15, pi28>=14, pi29>=13, pi30>=26, pi31>=25, pi32>=24, pi33>=23, pi34>=22, pi35>=21, pi36>=20, pi37>=19, pi38>=18, pi39>=17, pi40>=16, pi41>=15, pi42>=14, pi43>=13, pi44>=12, pi45>=25, pi46>=24, pi47>=23, pi48>=22, pi49>=21, pi50>=20, pi51>=19, pi52>=18, pi53>=17, pi54>=16, pi55>=15, pi56>=14, pi57>=13, pi58>=12, pi59>=11, pi60>=24, pi61>=23, pi62>=22, pi63>=21, pi64>=20, pi65>=19, pi66>=18, pi67>=17, pi68>=16, pi69>=15, pi70>=14, pi71>=13, pi72>=12, pi73>=11, pi74>=10, pi75>=23, pi76>=22, pi77>=21, pi78>=20, pi79>=19, pi80>=18, pi81>=17, pi82>=16, pi83>=15, pi84>=14, pi85>=13, pi86>=12, pi87>=11, pi88>=10, pi89>=9, pi90>=22, pi91>=21, pi92>=20, pi93>=19, pi94>=18, pi95>=17, pi96>=16, pi97>=15, pi98>=14, pi99>=13, pi100>=12, pi101>=11, pi102>=10, pi103>=9, pi104>=8, pi105>=21, pi106>=20, pi107>=19, pi108>=18, pi109>=17, pi110>=16, pi111>=15, pi112>=14, pi113>=13, pi114>=12, pi115>=11, pi116>=10, pi117>=9, pi118>=8, pi119>=7, pi120>=20, pi121>=19, pi122>=18, pi123>=17, pi124>=16, pi125>=15, pi126>=14, pi127>=13, pi128>=12, pi129>=11, pi130>=10, pi131>=9, pi132>=8, pi133>=7, pi134>=6, pi135>=19, pi136>=18, pi137>=17, pi138>=16, pi139>=15, pi140>=14, pi141>=13, pi142>=12, pi143>=11, pi144>=10, pi145>=9, pi146>=8, pi147>=7, pi148>=6, pi149>=5, pi150>=18, pi151>=17, pi152>=16, pi153>=15, pi154>=14, pi155>=13, pi156>=12, pi157>=11, pi158>=10, pi159>=9, pi160>=8, pi161>=7, pi162>=6, pi163>=5, pi164>=4, pi165>=17, pi166>=16, pi167>=15, pi168>=14, pi169>=13, pi170>=12, pi171>=11, pi172>=10, pi173>=9, pi174>=8, pi175>=7, pi176>=6, pi177>=5, pi178>=4, pi179>=3, pi180>=16, pi181>=15, pi182>=14, pi183>=13, pi184>=12, pi185>=11, pi186>=10, pi187>=9, pi188>=8, pi189>=7, pi190>=6, pi191>=5, pi192>=4, pi193>=3, pi194>=2, pi195>=15, pi196>=14, pi197>=13, pi198>=12, pi199>=11, pi200>=10, pi201>=9, pi202>=8, pi203>=7, pi204>=6, pi205>=5, pi206>=4, pi207>=3, pi208>=2, pi209>=1, pi210>=14, pi211>=13, pi212>=12, pi213>=11, pi214>=10, pi215>=9, pi216>=8, pi217>=7, pi218>=6, pi219>=5, pi220>=4, pi221>=3, pi222>=2, pi223>=1, pi224>=0, # Expected cost/reward equations
pi0== ((1 - y0)*xol + y0*xo0l) * (1 + pi0) + ((1 - y0)*xor + y0*xo0r) * (1 + pi1) + ((1 - y0)*xou + y0*xo0u) * (1 + pi0) + ((1 - y0)*xod + y0*xo0d) * (1 + pi15),
 pi1== ((1 - y1)*xol + y1*xo1l) * (1 + pi0) + ((1 - y1)*xor + y1*xo1r) * (1 + pi2) + ((1 - y1)*xou + y1*xo1u) * (1 + pi1) + ((1 - y1)*xod + y1*xo1d) * (1 + pi16),
 pi2== ((1 - y2)*xol + y2*xo2l) * (1 + pi1) + ((1 - y2)*xor + y2*xo2r) * (1 + pi3) + ((1 - y2)*xou + y2*xo2u) * (1 + pi2) + ((1 - y2)*xod + y2*xo2d) * (1 + pi17),
 pi3== ((1 - y3)*xol + y3*xo3l) * (1 + pi2) + ((1 - y3)*xor + y3*xo3r) * (1 + pi4) + ((1 - y3)*xou + y3*xo3u) * (1 + pi3) + ((1 - y3)*xod + y3*xo3d) * (1 + pi18),
 pi4== ((1 - y4)*xol + y4*xo4l) * (1 + pi3) + ((1 - y4)*xor + y4*xo4r) * (1 + pi5) + ((1 - y4)*xou + y4*xo4u) * (1 + pi4) + ((1 - y4)*xod + y4*xo4d) * (1 + pi19),
 pi5== ((1 - y5)*xol + y5*xo5l) * (1 + pi4) + ((1 - y5)*xor + y5*xo5r) * (1 + pi6) + ((1 - y5)*xou + y5*xo5u) * (1 + pi5) + ((1 - y5)*xod + y5*xo5d) * (1 + pi20),
 pi6== ((1 - y6)*xol + y6*xo6l) * (1 + pi5) + ((1 - y6)*xor + y6*xo6r) * (1 + pi7) + ((1 - y6)*xou + y6*xo6u) * (1 + pi6) + ((1 - y6)*xod + y6*xo6d) * (1 + pi21),
 pi7== ((1 - y7)*xol + y7*xo7l) * (1 + pi6) + ((1 - y7)*xor + y7*xo7r) * (1 + pi8) + ((1 - y7)*xou + y7*xo7u) * (1 + pi7) + ((1 - y7)*xod + y7*xo7d) * (1 + pi22),
 pi8== ((1 - y8)*xol + y8*xo8l) * (1 + pi7) + ((1 - y8)*xor + y8*xo8r) * (1 + pi9) + ((1 - y8)*xou + y8*xo8u) * (1 + pi8) + ((1 - y8)*xod + y8*xo8d) * (1 + pi23),
 pi9== ((1 - y9)*xol + y9*xo9l) * (1 + pi8) + ((1 - y9)*xor + y9*xo9r) * (1 + pi10) + ((1 - y9)*xou + y9*xo9u) * (1 + pi9) + ((1 - y9)*xod + y9*xo9d) * (1 + pi24),
 pi10== ((1 - y10)*xol + y10*xo10l) * (1 + pi9) + ((1 - y10)*xor + y10*xo10r) * (1 + pi11) + ((1 - y10)*xou + y10*xo10u) * (1 + pi10) + ((1 - y10)*xod + y10*xo10d) * (1 + pi25),
 pi11== ((1 - y11)*xol + y11*xo11l) * (1 + pi10) + ((1 - y11)*xor + y11*xo11r) * (1 + pi12) + ((1 - y11)*xou + y11*xo11u) * (1 + pi11) + ((1 - y11)*xod + y11*xo11d) * (1 + pi26),
 pi12== ((1 - y12)*xol + y12*xo12l) * (1 + pi11) + ((1 - y12)*xor + y12*xo12r) * (1 + pi13) + ((1 - y12)*xou + y12*xo12u) * (1 + pi12) + ((1 - y12)*xod + y12*xo12d) * (1 + pi27),
 pi13== ((1 - y13)*xol + y13*xo13l) * (1 + pi12) + ((1 - y13)*xor + y13*xo13r) * (1 + pi14) + ((1 - y13)*xou + y13*xo13u) * (1 + pi13) + ((1 - y13)*xod + y13*xo13d) * (1 + pi28),
 pi14== ((1 - y14)*xol + y14*xo14l) * (1 + pi13) + ((1 - y14)*xor + y14*xo14r) * (1 + pi15) + ((1 - y14)*xou + y14*xo14u) * (1 + pi14) + ((1 - y14)*xod + y14*xo14d) * (1 + pi29),
 pi15== ((1 - y15)*xol + y15*xo15l) * (1 + pi14) + ((1 - y15)*xor + y15*xo15r) * (1 + pi16) + ((1 - y15)*xou + y15*xo15u) * (1 + pi0) + ((1 - y15)*xod + y15*xo15d) * (1 + pi30),
 pi16== ((1 - y16)*xol + y16*xo16l) * (1 + pi15) + ((1 - y16)*xor + y16*xo16r) * (1 + pi17) + ((1 - y16)*xou + y16*xo16u) * (1 + pi1) + ((1 - y16)*xod + y16*xo16d) * (1 + pi31),
 pi17== ((1 - y17)*xol + y17*xo17l) * (1 + pi16) + ((1 - y17)*xor + y17*xo17r) * (1 + pi18) + ((1 - y17)*xou + y17*xo17u) * (1 + pi2) + ((1 - y17)*xod + y17*xo17d) * (1 + pi32),
 pi18== ((1 - y18)*xol + y18*xo18l) * (1 + pi17) + ((1 - y18)*xor + y18*xo18r) * (1 + pi19) + ((1 - y18)*xou + y18*xo18u) * (1 + pi3) + ((1 - y18)*xod + y18*xo18d) * (1 + pi33),
 pi19== ((1 - y19)*xol + y19*xo19l) * (1 + pi18) + ((1 - y19)*xor + y19*xo19r) * (1 + pi20) + ((1 - y19)*xou + y19*xo19u) * (1 + pi4) + ((1 - y19)*xod + y19*xo19d) * (1 + pi34),
 pi20== ((1 - y20)*xol + y20*xo20l) * (1 + pi19) + ((1 - y20)*xor + y20*xo20r) * (1 + pi21) + ((1 - y20)*xou + y20*xo20u) * (1 + pi5) + ((1 - y20)*xod + y20*xo20d) * (1 + pi35),
 pi21== ((1 - y21)*xol + y21*xo21l) * (1 + pi20) + ((1 - y21)*xor + y21*xo21r) * (1 + pi22) + ((1 - y21)*xou + y21*xo21u) * (1 + pi6) + ((1 - y21)*xod + y21*xo21d) * (1 + pi36),
 pi22== ((1 - y22)*xol + y22*xo22l) * (1 + pi21) + ((1 - y22)*xor + y22*xo22r) * (1 + pi23) + ((1 - y22)*xou + y22*xo22u) * (1 + pi7) + ((1 - y22)*xod + y22*xo22d) * (1 + pi37),
 pi23== ((1 - y23)*xol + y23*xo23l) * (1 + pi22) + ((1 - y23)*xor + y23*xo23r) * (1 + pi24) + ((1 - y23)*xou + y23*xo23u) * (1 + pi8) + ((1 - y23)*xod + y23*xo23d) * (1 + pi38),
 pi24== ((1 - y24)*xol + y24*xo24l) * (1 + pi23) + ((1 - y24)*xor + y24*xo24r) * (1 + pi25) + ((1 - y24)*xou + y24*xo24u) * (1 + pi9) + ((1 - y24)*xod + y24*xo24d) * (1 + pi39),
 pi25== ((1 - y25)*xol + y25*xo25l) * (1 + pi24) + ((1 - y25)*xor + y25*xo25r) * (1 + pi26) + ((1 - y25)*xou + y25*xo25u) * (1 + pi10) + ((1 - y25)*xod + y25*xo25d) * (1 + pi40),
 pi26== ((1 - y26)*xol + y26*xo26l) * (1 + pi25) + ((1 - y26)*xor + y26*xo26r) * (1 + pi27) + ((1 - y26)*xou + y26*xo26u) * (1 + pi11) + ((1 - y26)*xod + y26*xo26d) * (1 + pi41),
 pi27== ((1 - y27)*xol + y27*xo27l) * (1 + pi26) + ((1 - y27)*xor + y27*xo27r) * (1 + pi28) + ((1 - y27)*xou + y27*xo27u) * (1 + pi12) + ((1 - y27)*xod + y27*xo27d) * (1 + pi42),
 pi28== ((1 - y28)*xol + y28*xo28l) * (1 + pi27) + ((1 - y28)*xor + y28*xo28r) * (1 + pi29) + ((1 - y28)*xou + y28*xo28u) * (1 + pi13) + ((1 - y28)*xod + y28*xo28d) * (1 + pi43),
 pi29== ((1 - y29)*xol + y29*xo29l) * (1 + pi28) + ((1 - y29)*xor + y29*xo29r) * (1 + pi30) + ((1 - y29)*xou + y29*xo29u) * (1 + pi14) + ((1 - y29)*xod + y29*xo29d) * (1 + pi44),
 pi30== ((1 - y30)*xol + y30*xo30l) * (1 + pi29) + ((1 - y30)*xor + y30*xo30r) * (1 + pi31) + ((1 - y30)*xou + y30*xo30u) * (1 + pi15) + ((1 - y30)*xod + y30*xo30d) * (1 + pi45),
 pi31== ((1 - y31)*xol + y31*xo31l) * (1 + pi30) + ((1 - y31)*xor + y31*xo31r) * (1 + pi32) + ((1 - y31)*xou + y31*xo31u) * (1 + pi16) + ((1 - y31)*xod + y31*xo31d) * (1 + pi46),
 pi32== ((1 - y32)*xol + y32*xo32l) * (1 + pi31) + ((1 - y32)*xor + y32*xo32r) * (1 + pi33) + ((1 - y32)*xou + y32*xo32u) * (1 + pi17) + ((1 - y32)*xod + y32*xo32d) * (1 + pi47),
 pi33== ((1 - y33)*xol + y33*xo33l) * (1 + pi32) + ((1 - y33)*xor + y33*xo33r) * (1 + pi34) + ((1 - y33)*xou + y33*xo33u) * (1 + pi18) + ((1 - y33)*xod + y33*xo33d) * (1 + pi48),
 pi34== ((1 - y34)*xol + y34*xo34l) * (1 + pi33) + ((1 - y34)*xor + y34*xo34r) * (1 + pi35) + ((1 - y34)*xou + y34*xo34u) * (1 + pi19) + ((1 - y34)*xod + y34*xo34d) * (1 + pi49),
 pi35== ((1 - y35)*xol + y35*xo35l) * (1 + pi34) + ((1 - y35)*xor + y35*xo35r) * (1 + pi36) + ((1 - y35)*xou + y35*xo35u) * (1 + pi20) + ((1 - y35)*xod + y35*xo35d) * (1 + pi50),
 pi36== ((1 - y36)*xol + y36*xo36l) * (1 + pi35) + ((1 - y36)*xor + y36*xo36r) * (1 + pi37) + ((1 - y36)*xou + y36*xo36u) * (1 + pi21) + ((1 - y36)*xod + y36*xo36d) * (1 + pi51),
 pi37== ((1 - y37)*xol + y37*xo37l) * (1 + pi36) + ((1 - y37)*xor + y37*xo37r) * (1 + pi38) + ((1 - y37)*xou + y37*xo37u) * (1 + pi22) + ((1 - y37)*xod + y37*xo37d) * (1 + pi52),
 pi38== ((1 - y38)*xol + y38*xo38l) * (1 + pi37) + ((1 - y38)*xor + y38*xo38r) * (1 + pi39) + ((1 - y38)*xou + y38*xo38u) * (1 + pi23) + ((1 - y38)*xod + y38*xo38d) * (1 + pi53),
 pi39== ((1 - y39)*xol + y39*xo39l) * (1 + pi38) + ((1 - y39)*xor + y39*xo39r) * (1 + pi40) + ((1 - y39)*xou + y39*xo39u) * (1 + pi24) + ((1 - y39)*xod + y39*xo39d) * (1 + pi54),
 pi40== ((1 - y40)*xol + y40*xo40l) * (1 + pi39) + ((1 - y40)*xor + y40*xo40r) * (1 + pi41) + ((1 - y40)*xou + y40*xo40u) * (1 + pi25) + ((1 - y40)*xod + y40*xo40d) * (1 + pi55),
 pi41== ((1 - y41)*xol + y41*xo41l) * (1 + pi40) + ((1 - y41)*xor + y41*xo41r) * (1 + pi42) + ((1 - y41)*xou + y41*xo41u) * (1 + pi26) + ((1 - y41)*xod + y41*xo41d) * (1 + pi56),
 pi42== ((1 - y42)*xol + y42*xo42l) * (1 + pi41) + ((1 - y42)*xor + y42*xo42r) * (1 + pi43) + ((1 - y42)*xou + y42*xo42u) * (1 + pi27) + ((1 - y42)*xod + y42*xo42d) * (1 + pi57),
 pi43== ((1 - y43)*xol + y43*xo43l) * (1 + pi42) + ((1 - y43)*xor + y43*xo43r) * (1 + pi44) + ((1 - y43)*xou + y43*xo43u) * (1 + pi28) + ((1 - y43)*xod + y43*xo43d) * (1 + pi58),
 pi44== ((1 - y44)*xol + y44*xo44l) * (1 + pi43) + ((1 - y44)*xor + y44*xo44r) * (1 + pi45) + ((1 - y44)*xou + y44*xo44u) * (1 + pi29) + ((1 - y44)*xod + y44*xo44d) * (1 + pi59),
 pi45== ((1 - y45)*xol + y45*xo45l) * (1 + pi44) + ((1 - y45)*xor + y45*xo45r) * (1 + pi46) + ((1 - y45)*xou + y45*xo45u) * (1 + pi30) + ((1 - y45)*xod + y45*xo45d) * (1 + pi60),
 pi46== ((1 - y46)*xol + y46*xo46l) * (1 + pi45) + ((1 - y46)*xor + y46*xo46r) * (1 + pi47) + ((1 - y46)*xou + y46*xo46u) * (1 + pi31) + ((1 - y46)*xod + y46*xo46d) * (1 + pi61),
 pi47== ((1 - y47)*xol + y47*xo47l) * (1 + pi46) + ((1 - y47)*xor + y47*xo47r) * (1 + pi48) + ((1 - y47)*xou + y47*xo47u) * (1 + pi32) + ((1 - y47)*xod + y47*xo47d) * (1 + pi62),
 pi48== ((1 - y48)*xol + y48*xo48l) * (1 + pi47) + ((1 - y48)*xor + y48*xo48r) * (1 + pi49) + ((1 - y48)*xou + y48*xo48u) * (1 + pi33) + ((1 - y48)*xod + y48*xo48d) * (1 + pi63),
 pi49== ((1 - y49)*xol + y49*xo49l) * (1 + pi48) + ((1 - y49)*xor + y49*xo49r) * (1 + pi50) + ((1 - y49)*xou + y49*xo49u) * (1 + pi34) + ((1 - y49)*xod + y49*xo49d) * (1 + pi64),
 pi50== ((1 - y50)*xol + y50*xo50l) * (1 + pi49) + ((1 - y50)*xor + y50*xo50r) * (1 + pi51) + ((1 - y50)*xou + y50*xo50u) * (1 + pi35) + ((1 - y50)*xod + y50*xo50d) * (1 + pi65),
 pi51== ((1 - y51)*xol + y51*xo51l) * (1 + pi50) + ((1 - y51)*xor + y51*xo51r) * (1 + pi52) + ((1 - y51)*xou + y51*xo51u) * (1 + pi36) + ((1 - y51)*xod + y51*xo51d) * (1 + pi66),
 pi52== ((1 - y52)*xol + y52*xo52l) * (1 + pi51) + ((1 - y52)*xor + y52*xo52r) * (1 + pi53) + ((1 - y52)*xou + y52*xo52u) * (1 + pi37) + ((1 - y52)*xod + y52*xo52d) * (1 + pi67),
 pi53== ((1 - y53)*xol + y53*xo53l) * (1 + pi52) + ((1 - y53)*xor + y53*xo53r) * (1 + pi54) + ((1 - y53)*xou + y53*xo53u) * (1 + pi38) + ((1 - y53)*xod + y53*xo53d) * (1 + pi68),
 pi54== ((1 - y54)*xol + y54*xo54l) * (1 + pi53) + ((1 - y54)*xor + y54*xo54r) * (1 + pi55) + ((1 - y54)*xou + y54*xo54u) * (1 + pi39) + ((1 - y54)*xod + y54*xo54d) * (1 + pi69),
 pi55== ((1 - y55)*xol + y55*xo55l) * (1 + pi54) + ((1 - y55)*xor + y55*xo55r) * (1 + pi56) + ((1 - y55)*xou + y55*xo55u) * (1 + pi40) + ((1 - y55)*xod + y55*xo55d) * (1 + pi70),
 pi56== ((1 - y56)*xol + y56*xo56l) * (1 + pi55) + ((1 - y56)*xor + y56*xo56r) * (1 + pi57) + ((1 - y56)*xou + y56*xo56u) * (1 + pi41) + ((1 - y56)*xod + y56*xo56d) * (1 + pi71),
 pi57== ((1 - y57)*xol + y57*xo57l) * (1 + pi56) + ((1 - y57)*xor + y57*xo57r) * (1 + pi58) + ((1 - y57)*xou + y57*xo57u) * (1 + pi42) + ((1 - y57)*xod + y57*xo57d) * (1 + pi72),
 pi58== ((1 - y58)*xol + y58*xo58l) * (1 + pi57) + ((1 - y58)*xor + y58*xo58r) * (1 + pi59) + ((1 - y58)*xou + y58*xo58u) * (1 + pi43) + ((1 - y58)*xod + y58*xo58d) * (1 + pi73),
 pi59== ((1 - y59)*xol + y59*xo59l) * (1 + pi58) + ((1 - y59)*xor + y59*xo59r) * (1 + pi60) + ((1 - y59)*xou + y59*xo59u) * (1 + pi44) + ((1 - y59)*xod + y59*xo59d) * (1 + pi74),
 pi60== ((1 - y60)*xol + y60*xo60l) * (1 + pi59) + ((1 - y60)*xor + y60*xo60r) * (1 + pi61) + ((1 - y60)*xou + y60*xo60u) * (1 + pi45) + ((1 - y60)*xod + y60*xo60d) * (1 + pi75),
 pi61== ((1 - y61)*xol + y61*xo61l) * (1 + pi60) + ((1 - y61)*xor + y61*xo61r) * (1 + pi62) + ((1 - y61)*xou + y61*xo61u) * (1 + pi46) + ((1 - y61)*xod + y61*xo61d) * (1 + pi76),
 pi62== ((1 - y62)*xol + y62*xo62l) * (1 + pi61) + ((1 - y62)*xor + y62*xo62r) * (1 + pi63) + ((1 - y62)*xou + y62*xo62u) * (1 + pi47) + ((1 - y62)*xod + y62*xo62d) * (1 + pi77),
 pi63== ((1 - y63)*xol + y63*xo63l) * (1 + pi62) + ((1 - y63)*xor + y63*xo63r) * (1 + pi64) + ((1 - y63)*xou + y63*xo63u) * (1 + pi48) + ((1 - y63)*xod + y63*xo63d) * (1 + pi78),
 pi64== ((1 - y64)*xol + y64*xo64l) * (1 + pi63) + ((1 - y64)*xor + y64*xo64r) * (1 + pi65) + ((1 - y64)*xou + y64*xo64u) * (1 + pi49) + ((1 - y64)*xod + y64*xo64d) * (1 + pi79),
 pi65== ((1 - y65)*xol + y65*xo65l) * (1 + pi64) + ((1 - y65)*xor + y65*xo65r) * (1 + pi66) + ((1 - y65)*xou + y65*xo65u) * (1 + pi50) + ((1 - y65)*xod + y65*xo65d) * (1 + pi80),
 pi66== ((1 - y66)*xol + y66*xo66l) * (1 + pi65) + ((1 - y66)*xor + y66*xo66r) * (1 + pi67) + ((1 - y66)*xou + y66*xo66u) * (1 + pi51) + ((1 - y66)*xod + y66*xo66d) * (1 + pi81),
 pi67== ((1 - y67)*xol + y67*xo67l) * (1 + pi66) + ((1 - y67)*xor + y67*xo67r) * (1 + pi68) + ((1 - y67)*xou + y67*xo67u) * (1 + pi52) + ((1 - y67)*xod + y67*xo67d) * (1 + pi82),
 pi68== ((1 - y68)*xol + y68*xo68l) * (1 + pi67) + ((1 - y68)*xor + y68*xo68r) * (1 + pi69) + ((1 - y68)*xou + y68*xo68u) * (1 + pi53) + ((1 - y68)*xod + y68*xo68d) * (1 + pi83),
 pi69== ((1 - y69)*xol + y69*xo69l) * (1 + pi68) + ((1 - y69)*xor + y69*xo69r) * (1 + pi70) + ((1 - y69)*xou + y69*xo69u) * (1 + pi54) + ((1 - y69)*xod + y69*xo69d) * (1 + pi84),
 pi70== ((1 - y70)*xol + y70*xo70l) * (1 + pi69) + ((1 - y70)*xor + y70*xo70r) * (1 + pi71) + ((1 - y70)*xou + y70*xo70u) * (1 + pi55) + ((1 - y70)*xod + y70*xo70d) * (1 + pi85),
 pi71== ((1 - y71)*xol + y71*xo71l) * (1 + pi70) + ((1 - y71)*xor + y71*xo71r) * (1 + pi72) + ((1 - y71)*xou + y71*xo71u) * (1 + pi56) + ((1 - y71)*xod + y71*xo71d) * (1 + pi86),
 pi72== ((1 - y72)*xol + y72*xo72l) * (1 + pi71) + ((1 - y72)*xor + y72*xo72r) * (1 + pi73) + ((1 - y72)*xou + y72*xo72u) * (1 + pi57) + ((1 - y72)*xod + y72*xo72d) * (1 + pi87),
 pi73== ((1 - y73)*xol + y73*xo73l) * (1 + pi72) + ((1 - y73)*xor + y73*xo73r) * (1 + pi74) + ((1 - y73)*xou + y73*xo73u) * (1 + pi58) + ((1 - y73)*xod + y73*xo73d) * (1 + pi88),
 pi74== ((1 - y74)*xol + y74*xo74l) * (1 + pi73) + ((1 - y74)*xor + y74*xo74r) * (1 + pi75) + ((1 - y74)*xou + y74*xo74u) * (1 + pi59) + ((1 - y74)*xod + y74*xo74d) * (1 + pi89),
 pi75== ((1 - y75)*xol + y75*xo75l) * (1 + pi74) + ((1 - y75)*xor + y75*xo75r) * (1 + pi76) + ((1 - y75)*xou + y75*xo75u) * (1 + pi60) + ((1 - y75)*xod + y75*xo75d) * (1 + pi90),
 pi76== ((1 - y76)*xol + y76*xo76l) * (1 + pi75) + ((1 - y76)*xor + y76*xo76r) * (1 + pi77) + ((1 - y76)*xou + y76*xo76u) * (1 + pi61) + ((1 - y76)*xod + y76*xo76d) * (1 + pi91),
 pi77== ((1 - y77)*xol + y77*xo77l) * (1 + pi76) + ((1 - y77)*xor + y77*xo77r) * (1 + pi78) + ((1 - y77)*xou + y77*xo77u) * (1 + pi62) + ((1 - y77)*xod + y77*xo77d) * (1 + pi92),
 pi78== ((1 - y78)*xol + y78*xo78l) * (1 + pi77) + ((1 - y78)*xor + y78*xo78r) * (1 + pi79) + ((1 - y78)*xou + y78*xo78u) * (1 + pi63) + ((1 - y78)*xod + y78*xo78d) * (1 + pi93),
 pi79== ((1 - y79)*xol + y79*xo79l) * (1 + pi78) + ((1 - y79)*xor + y79*xo79r) * (1 + pi80) + ((1 - y79)*xou + y79*xo79u) * (1 + pi64) + ((1 - y79)*xod + y79*xo79d) * (1 + pi94),
 pi80== ((1 - y80)*xol + y80*xo80l) * (1 + pi79) + ((1 - y80)*xor + y80*xo80r) * (1 + pi81) + ((1 - y80)*xou + y80*xo80u) * (1 + pi65) + ((1 - y80)*xod + y80*xo80d) * (1 + pi95),
 pi81== ((1 - y81)*xol + y81*xo81l) * (1 + pi80) + ((1 - y81)*xor + y81*xo81r) * (1 + pi82) + ((1 - y81)*xou + y81*xo81u) * (1 + pi66) + ((1 - y81)*xod + y81*xo81d) * (1 + pi96),
 pi82== ((1 - y82)*xol + y82*xo82l) * (1 + pi81) + ((1 - y82)*xor + y82*xo82r) * (1 + pi83) + ((1 - y82)*xou + y82*xo82u) * (1 + pi67) + ((1 - y82)*xod + y82*xo82d) * (1 + pi97),
 pi83== ((1 - y83)*xol + y83*xo83l) * (1 + pi82) + ((1 - y83)*xor + y83*xo83r) * (1 + pi84) + ((1 - y83)*xou + y83*xo83u) * (1 + pi68) + ((1 - y83)*xod + y83*xo83d) * (1 + pi98),
 pi84== ((1 - y84)*xol + y84*xo84l) * (1 + pi83) + ((1 - y84)*xor + y84*xo84r) * (1 + pi85) + ((1 - y84)*xou + y84*xo84u) * (1 + pi69) + ((1 - y84)*xod + y84*xo84d) * (1 + pi99),
 pi85== ((1 - y85)*xol + y85*xo85l) * (1 + pi84) + ((1 - y85)*xor + y85*xo85r) * (1 + pi86) + ((1 - y85)*xou + y85*xo85u) * (1 + pi70) + ((1 - y85)*xod + y85*xo85d) * (1 + pi100),
 pi86== ((1 - y86)*xol + y86*xo86l) * (1 + pi85) + ((1 - y86)*xor + y86*xo86r) * (1 + pi87) + ((1 - y86)*xou + y86*xo86u) * (1 + pi71) + ((1 - y86)*xod + y86*xo86d) * (1 + pi101),
 pi87== ((1 - y87)*xol + y87*xo87l) * (1 + pi86) + ((1 - y87)*xor + y87*xo87r) * (1 + pi88) + ((1 - y87)*xou + y87*xo87u) * (1 + pi72) + ((1 - y87)*xod + y87*xo87d) * (1 + pi102),
 pi88== ((1 - y88)*xol + y88*xo88l) * (1 + pi87) + ((1 - y88)*xor + y88*xo88r) * (1 + pi89) + ((1 - y88)*xou + y88*xo88u) * (1 + pi73) + ((1 - y88)*xod + y88*xo88d) * (1 + pi103),
 pi89== ((1 - y89)*xol + y89*xo89l) * (1 + pi88) + ((1 - y89)*xor + y89*xo89r) * (1 + pi90) + ((1 - y89)*xou + y89*xo89u) * (1 + pi74) + ((1 - y89)*xod + y89*xo89d) * (1 + pi104),
 pi90== ((1 - y90)*xol + y90*xo90l) * (1 + pi89) + ((1 - y90)*xor + y90*xo90r) * (1 + pi91) + ((1 - y90)*xou + y90*xo90u) * (1 + pi75) + ((1 - y90)*xod + y90*xo90d) * (1 + pi105),
 pi91== ((1 - y91)*xol + y91*xo91l) * (1 + pi90) + ((1 - y91)*xor + y91*xo91r) * (1 + pi92) + ((1 - y91)*xou + y91*xo91u) * (1 + pi76) + ((1 - y91)*xod + y91*xo91d) * (1 + pi106),
 pi92== ((1 - y92)*xol + y92*xo92l) * (1 + pi91) + ((1 - y92)*xor + y92*xo92r) * (1 + pi93) + ((1 - y92)*xou + y92*xo92u) * (1 + pi77) + ((1 - y92)*xod + y92*xo92d) * (1 + pi107),
 pi93== ((1 - y93)*xol + y93*xo93l) * (1 + pi92) + ((1 - y93)*xor + y93*xo93r) * (1 + pi94) + ((1 - y93)*xou + y93*xo93u) * (1 + pi78) + ((1 - y93)*xod + y93*xo93d) * (1 + pi108),
 pi94== ((1 - y94)*xol + y94*xo94l) * (1 + pi93) + ((1 - y94)*xor + y94*xo94r) * (1 + pi95) + ((1 - y94)*xou + y94*xo94u) * (1 + pi79) + ((1 - y94)*xod + y94*xo94d) * (1 + pi109),
 pi95== ((1 - y95)*xol + y95*xo95l) * (1 + pi94) + ((1 - y95)*xor + y95*xo95r) * (1 + pi96) + ((1 - y95)*xou + y95*xo95u) * (1 + pi80) + ((1 - y95)*xod + y95*xo95d) * (1 + pi110),
 pi96== ((1 - y96)*xol + y96*xo96l) * (1 + pi95) + ((1 - y96)*xor + y96*xo96r) * (1 + pi97) + ((1 - y96)*xou + y96*xo96u) * (1 + pi81) + ((1 - y96)*xod + y96*xo96d) * (1 + pi111),
 pi97== ((1 - y97)*xol + y97*xo97l) * (1 + pi96) + ((1 - y97)*xor + y97*xo97r) * (1 + pi98) + ((1 - y97)*xou + y97*xo97u) * (1 + pi82) + ((1 - y97)*xod + y97*xo97d) * (1 + pi112),
 pi98== ((1 - y98)*xol + y98*xo98l) * (1 + pi97) + ((1 - y98)*xor + y98*xo98r) * (1 + pi99) + ((1 - y98)*xou + y98*xo98u) * (1 + pi83) + ((1 - y98)*xod + y98*xo98d) * (1 + pi113),
 pi99== ((1 - y99)*xol + y99*xo99l) * (1 + pi98) + ((1 - y99)*xor + y99*xo99r) * (1 + pi100) + ((1 - y99)*xou + y99*xo99u) * (1 + pi84) + ((1 - y99)*xod + y99*xo99d) * (1 + pi114),
 pi100== ((1 - y100)*xol + y100*xo100l) * (1 + pi99) + ((1 - y100)*xor + y100*xo100r) * (1 + pi101) + ((1 - y100)*xou + y100*xo100u) * (1 + pi85) + ((1 - y100)*xod + y100*xo100d) * (1 + pi115),
 pi101== ((1 - y101)*xol + y101*xo101l) * (1 + pi100) + ((1 - y101)*xor + y101*xo101r) * (1 + pi102) + ((1 - y101)*xou + y101*xo101u) * (1 + pi86) + ((1 - y101)*xod + y101*xo101d) * (1 + pi116),
 pi102== ((1 - y102)*xol + y102*xo102l) * (1 + pi101) + ((1 - y102)*xor + y102*xo102r) * (1 + pi103) + ((1 - y102)*xou + y102*xo102u) * (1 + pi87) + ((1 - y102)*xod + y102*xo102d) * (1 + pi117),
 pi103== ((1 - y103)*xol + y103*xo103l) * (1 + pi102) + ((1 - y103)*xor + y103*xo103r) * (1 + pi104) + ((1 - y103)*xou + y103*xo103u) * (1 + pi88) + ((1 - y103)*xod + y103*xo103d) * (1 + pi118),
 pi104== ((1 - y104)*xol + y104*xo104l) * (1 + pi103) + ((1 - y104)*xor + y104*xo104r) * (1 + pi105) + ((1 - y104)*xou + y104*xo104u) * (1 + pi89) + ((1 - y104)*xod + y104*xo104d) * (1 + pi119),
 pi105== ((1 - y105)*xol + y105*xo105l) * (1 + pi104) + ((1 - y105)*xor + y105*xo105r) * (1 + pi106) + ((1 - y105)*xou + y105*xo105u) * (1 + pi90) + ((1 - y105)*xod + y105*xo105d) * (1 + pi120),
 pi106== ((1 - y106)*xol + y106*xo106l) * (1 + pi105) + ((1 - y106)*xor + y106*xo106r) * (1 + pi107) + ((1 - y106)*xou + y106*xo106u) * (1 + pi91) + ((1 - y106)*xod + y106*xo106d) * (1 + pi121),
 pi107== ((1 - y107)*xol + y107*xo107l) * (1 + pi106) + ((1 - y107)*xor + y107*xo107r) * (1 + pi108) + ((1 - y107)*xou + y107*xo107u) * (1 + pi92) + ((1 - y107)*xod + y107*xo107d) * (1 + pi122),
 pi108== ((1 - y108)*xol + y108*xo108l) * (1 + pi107) + ((1 - y108)*xor + y108*xo108r) * (1 + pi109) + ((1 - y108)*xou + y108*xo108u) * (1 + pi93) + ((1 - y108)*xod + y108*xo108d) * (1 + pi123),
 pi109== ((1 - y109)*xol + y109*xo109l) * (1 + pi108) + ((1 - y109)*xor + y109*xo109r) * (1 + pi110) + ((1 - y109)*xou + y109*xo109u) * (1 + pi94) + ((1 - y109)*xod + y109*xo109d) * (1 + pi124),
 pi110== ((1 - y110)*xol + y110*xo110l) * (1 + pi109) + ((1 - y110)*xor + y110*xo110r) * (1 + pi111) + ((1 - y110)*xou + y110*xo110u) * (1 + pi95) + ((1 - y110)*xod + y110*xo110d) * (1 + pi125),
 pi111== ((1 - y111)*xol + y111*xo111l) * (1 + pi110) + ((1 - y111)*xor + y111*xo111r) * (1 + pi112) + ((1 - y111)*xou + y111*xo111u) * (1 + pi96) + ((1 - y111)*xod + y111*xo111d) * (1 + pi126),
 pi112== ((1 - y112)*xol + y112*xo112l) * (1 + pi111) + ((1 - y112)*xor + y112*xo112r) * (1 + pi113) + ((1 - y112)*xou + y112*xo112u) * (1 + pi97) + ((1 - y112)*xod + y112*xo112d) * (1 + pi127),
 pi113== ((1 - y113)*xol + y113*xo113l) * (1 + pi112) + ((1 - y113)*xor + y113*xo113r) * (1 + pi114) + ((1 - y113)*xou + y113*xo113u) * (1 + pi98) + ((1 - y113)*xod + y113*xo113d) * (1 + pi128),
 pi114== ((1 - y114)*xol + y114*xo114l) * (1 + pi113) + ((1 - y114)*xor + y114*xo114r) * (1 + pi115) + ((1 - y114)*xou + y114*xo114u) * (1 + pi99) + ((1 - y114)*xod + y114*xo114d) * (1 + pi129),
 pi115== ((1 - y115)*xol + y115*xo115l) * (1 + pi114) + ((1 - y115)*xor + y115*xo115r) * (1 + pi116) + ((1 - y115)*xou + y115*xo115u) * (1 + pi100) + ((1 - y115)*xod + y115*xo115d) * (1 + pi130),
 pi116== ((1 - y116)*xol + y116*xo116l) * (1 + pi115) + ((1 - y116)*xor + y116*xo116r) * (1 + pi117) + ((1 - y116)*xou + y116*xo116u) * (1 + pi101) + ((1 - y116)*xod + y116*xo116d) * (1 + pi131),
 pi117== ((1 - y117)*xol + y117*xo117l) * (1 + pi116) + ((1 - y117)*xor + y117*xo117r) * (1 + pi118) + ((1 - y117)*xou + y117*xo117u) * (1 + pi102) + ((1 - y117)*xod + y117*xo117d) * (1 + pi132),
 pi118== ((1 - y118)*xol + y118*xo118l) * (1 + pi117) + ((1 - y118)*xor + y118*xo118r) * (1 + pi119) + ((1 - y118)*xou + y118*xo118u) * (1 + pi103) + ((1 - y118)*xod + y118*xo118d) * (1 + pi133),
 pi119== ((1 - y119)*xol + y119*xo119l) * (1 + pi118) + ((1 - y119)*xor + y119*xo119r) * (1 + pi120) + ((1 - y119)*xou + y119*xo119u) * (1 + pi104) + ((1 - y119)*xod + y119*xo119d) * (1 + pi134),
 pi120== ((1 - y120)*xol + y120*xo120l) * (1 + pi119) + ((1 - y120)*xor + y120*xo120r) * (1 + pi121) + ((1 - y120)*xou + y120*xo120u) * (1 + pi105) + ((1 - y120)*xod + y120*xo120d) * (1 + pi135),
 pi121== ((1 - y121)*xol + y121*xo121l) * (1 + pi120) + ((1 - y121)*xor + y121*xo121r) * (1 + pi122) + ((1 - y121)*xou + y121*xo121u) * (1 + pi106) + ((1 - y121)*xod + y121*xo121d) * (1 + pi136),
 pi122== ((1 - y122)*xol + y122*xo122l) * (1 + pi121) + ((1 - y122)*xor + y122*xo122r) * (1 + pi123) + ((1 - y122)*xou + y122*xo122u) * (1 + pi107) + ((1 - y122)*xod + y122*xo122d) * (1 + pi137),
 pi123== ((1 - y123)*xol + y123*xo123l) * (1 + pi122) + ((1 - y123)*xor + y123*xo123r) * (1 + pi124) + ((1 - y123)*xou + y123*xo123u) * (1 + pi108) + ((1 - y123)*xod + y123*xo123d) * (1 + pi138),
 pi124== ((1 - y124)*xol + y124*xo124l) * (1 + pi123) + ((1 - y124)*xor + y124*xo124r) * (1 + pi125) + ((1 - y124)*xou + y124*xo124u) * (1 + pi109) + ((1 - y124)*xod + y124*xo124d) * (1 + pi139),
 pi125== ((1 - y125)*xol + y125*xo125l) * (1 + pi124) + ((1 - y125)*xor + y125*xo125r) * (1 + pi126) + ((1 - y125)*xou + y125*xo125u) * (1 + pi110) + ((1 - y125)*xod + y125*xo125d) * (1 + pi140),
 pi126== ((1 - y126)*xol + y126*xo126l) * (1 + pi125) + ((1 - y126)*xor + y126*xo126r) * (1 + pi127) + ((1 - y126)*xou + y126*xo126u) * (1 + pi111) + ((1 - y126)*xod + y126*xo126d) * (1 + pi141),
 pi127== ((1 - y127)*xol + y127*xo127l) * (1 + pi126) + ((1 - y127)*xor + y127*xo127r) * (1 + pi128) + ((1 - y127)*xou + y127*xo127u) * (1 + pi112) + ((1 - y127)*xod + y127*xo127d) * (1 + pi142),
 pi128== ((1 - y128)*xol + y128*xo128l) * (1 + pi127) + ((1 - y128)*xor + y128*xo128r) * (1 + pi129) + ((1 - y128)*xou + y128*xo128u) * (1 + pi113) + ((1 - y128)*xod + y128*xo128d) * (1 + pi143),
 pi129== ((1 - y129)*xol + y129*xo129l) * (1 + pi128) + ((1 - y129)*xor + y129*xo129r) * (1 + pi130) + ((1 - y129)*xou + y129*xo129u) * (1 + pi114) + ((1 - y129)*xod + y129*xo129d) * (1 + pi144),
 pi130== ((1 - y130)*xol + y130*xo130l) * (1 + pi129) + ((1 - y130)*xor + y130*xo130r) * (1 + pi131) + ((1 - y130)*xou + y130*xo130u) * (1 + pi115) + ((1 - y130)*xod + y130*xo130d) * (1 + pi145),
 pi131== ((1 - y131)*xol + y131*xo131l) * (1 + pi130) + ((1 - y131)*xor + y131*xo131r) * (1 + pi132) + ((1 - y131)*xou + y131*xo131u) * (1 + pi116) + ((1 - y131)*xod + y131*xo131d) * (1 + pi146),
 pi132== ((1 - y132)*xol + y132*xo132l) * (1 + pi131) + ((1 - y132)*xor + y132*xo132r) * (1 + pi133) + ((1 - y132)*xou + y132*xo132u) * (1 + pi117) + ((1 - y132)*xod + y132*xo132d) * (1 + pi147),
 pi133== ((1 - y133)*xol + y133*xo133l) * (1 + pi132) + ((1 - y133)*xor + y133*xo133r) * (1 + pi134) + ((1 - y133)*xou + y133*xo133u) * (1 + pi118) + ((1 - y133)*xod + y133*xo133d) * (1 + pi148),
 pi134== ((1 - y134)*xol + y134*xo134l) * (1 + pi133) + ((1 - y134)*xor + y134*xo134r) * (1 + pi135) + ((1 - y134)*xou + y134*xo134u) * (1 + pi119) + ((1 - y134)*xod + y134*xo134d) * (1 + pi149),
 pi135== ((1 - y135)*xol + y135*xo135l) * (1 + pi134) + ((1 - y135)*xor + y135*xo135r) * (1 + pi136) + ((1 - y135)*xou + y135*xo135u) * (1 + pi120) + ((1 - y135)*xod + y135*xo135d) * (1 + pi150),
 pi136== ((1 - y136)*xol + y136*xo136l) * (1 + pi135) + ((1 - y136)*xor + y136*xo136r) * (1 + pi137) + ((1 - y136)*xou + y136*xo136u) * (1 + pi121) + ((1 - y136)*xod + y136*xo136d) * (1 + pi151),
 pi137== ((1 - y137)*xol + y137*xo137l) * (1 + pi136) + ((1 - y137)*xor + y137*xo137r) * (1 + pi138) + ((1 - y137)*xou + y137*xo137u) * (1 + pi122) + ((1 - y137)*xod + y137*xo137d) * (1 + pi152),
 pi138== ((1 - y138)*xol + y138*xo138l) * (1 + pi137) + ((1 - y138)*xor + y138*xo138r) * (1 + pi139) + ((1 - y138)*xou + y138*xo138u) * (1 + pi123) + ((1 - y138)*xod + y138*xo138d) * (1 + pi153),
 pi139== ((1 - y139)*xol + y139*xo139l) * (1 + pi138) + ((1 - y139)*xor + y139*xo139r) * (1 + pi140) + ((1 - y139)*xou + y139*xo139u) * (1 + pi124) + ((1 - y139)*xod + y139*xo139d) * (1 + pi154),
 pi140== ((1 - y140)*xol + y140*xo140l) * (1 + pi139) + ((1 - y140)*xor + y140*xo140r) * (1 + pi141) + ((1 - y140)*xou + y140*xo140u) * (1 + pi125) + ((1 - y140)*xod + y140*xo140d) * (1 + pi155),
 pi141== ((1 - y141)*xol + y141*xo141l) * (1 + pi140) + ((1 - y141)*xor + y141*xo141r) * (1 + pi142) + ((1 - y141)*xou + y141*xo141u) * (1 + pi126) + ((1 - y141)*xod + y141*xo141d) * (1 + pi156),
 pi142== ((1 - y142)*xol + y142*xo142l) * (1 + pi141) + ((1 - y142)*xor + y142*xo142r) * (1 + pi143) + ((1 - y142)*xou + y142*xo142u) * (1 + pi127) + ((1 - y142)*xod + y142*xo142d) * (1 + pi157),
 pi143== ((1 - y143)*xol + y143*xo143l) * (1 + pi142) + ((1 - y143)*xor + y143*xo143r) * (1 + pi144) + ((1 - y143)*xou + y143*xo143u) * (1 + pi128) + ((1 - y143)*xod + y143*xo143d) * (1 + pi158),
 pi144== ((1 - y144)*xol + y144*xo144l) * (1 + pi143) + ((1 - y144)*xor + y144*xo144r) * (1 + pi145) + ((1 - y144)*xou + y144*xo144u) * (1 + pi129) + ((1 - y144)*xod + y144*xo144d) * (1 + pi159),
 pi145== ((1 - y145)*xol + y145*xo145l) * (1 + pi144) + ((1 - y145)*xor + y145*xo145r) * (1 + pi146) + ((1 - y145)*xou + y145*xo145u) * (1 + pi130) + ((1 - y145)*xod + y145*xo145d) * (1 + pi160),
 pi146== ((1 - y146)*xol + y146*xo146l) * (1 + pi145) + ((1 - y146)*xor + y146*xo146r) * (1 + pi147) + ((1 - y146)*xou + y146*xo146u) * (1 + pi131) + ((1 - y146)*xod + y146*xo146d) * (1 + pi161),
 pi147== ((1 - y147)*xol + y147*xo147l) * (1 + pi146) + ((1 - y147)*xor + y147*xo147r) * (1 + pi148) + ((1 - y147)*xou + y147*xo147u) * (1 + pi132) + ((1 - y147)*xod + y147*xo147d) * (1 + pi162),
 pi148== ((1 - y148)*xol + y148*xo148l) * (1 + pi147) + ((1 - y148)*xor + y148*xo148r) * (1 + pi149) + ((1 - y148)*xou + y148*xo148u) * (1 + pi133) + ((1 - y148)*xod + y148*xo148d) * (1 + pi163),
 pi149== ((1 - y149)*xol + y149*xo149l) * (1 + pi148) + ((1 - y149)*xor + y149*xo149r) * (1 + pi150) + ((1 - y149)*xou + y149*xo149u) * (1 + pi134) + ((1 - y149)*xod + y149*xo149d) * (1 + pi164),
 pi150== ((1 - y150)*xol + y150*xo150l) * (1 + pi149) + ((1 - y150)*xor + y150*xo150r) * (1 + pi151) + ((1 - y150)*xou + y150*xo150u) * (1 + pi135) + ((1 - y150)*xod + y150*xo150d) * (1 + pi165),
 pi151== ((1 - y151)*xol + y151*xo151l) * (1 + pi150) + ((1 - y151)*xor + y151*xo151r) * (1 + pi152) + ((1 - y151)*xou + y151*xo151u) * (1 + pi136) + ((1 - y151)*xod + y151*xo151d) * (1 + pi166),
 pi152== ((1 - y152)*xol + y152*xo152l) * (1 + pi151) + ((1 - y152)*xor + y152*xo152r) * (1 + pi153) + ((1 - y152)*xou + y152*xo152u) * (1 + pi137) + ((1 - y152)*xod + y152*xo152d) * (1 + pi167),
 pi153== ((1 - y153)*xol + y153*xo153l) * (1 + pi152) + ((1 - y153)*xor + y153*xo153r) * (1 + pi154) + ((1 - y153)*xou + y153*xo153u) * (1 + pi138) + ((1 - y153)*xod + y153*xo153d) * (1 + pi168),
 pi154== ((1 - y154)*xol + y154*xo154l) * (1 + pi153) + ((1 - y154)*xor + y154*xo154r) * (1 + pi155) + ((1 - y154)*xou + y154*xo154u) * (1 + pi139) + ((1 - y154)*xod + y154*xo154d) * (1 + pi169),
 pi155== ((1 - y155)*xol + y155*xo155l) * (1 + pi154) + ((1 - y155)*xor + y155*xo155r) * (1 + pi156) + ((1 - y155)*xou + y155*xo155u) * (1 + pi140) + ((1 - y155)*xod + y155*xo155d) * (1 + pi170),
 pi156== ((1 - y156)*xol + y156*xo156l) * (1 + pi155) + ((1 - y156)*xor + y156*xo156r) * (1 + pi157) + ((1 - y156)*xou + y156*xo156u) * (1 + pi141) + ((1 - y156)*xod + y156*xo156d) * (1 + pi171),
 pi157== ((1 - y157)*xol + y157*xo157l) * (1 + pi156) + ((1 - y157)*xor + y157*xo157r) * (1 + pi158) + ((1 - y157)*xou + y157*xo157u) * (1 + pi142) + ((1 - y157)*xod + y157*xo157d) * (1 + pi172),
 pi158== ((1 - y158)*xol + y158*xo158l) * (1 + pi157) + ((1 - y158)*xor + y158*xo158r) * (1 + pi159) + ((1 - y158)*xou + y158*xo158u) * (1 + pi143) + ((1 - y158)*xod + y158*xo158d) * (1 + pi173),
 pi159== ((1 - y159)*xol + y159*xo159l) * (1 + pi158) + ((1 - y159)*xor + y159*xo159r) * (1 + pi160) + ((1 - y159)*xou + y159*xo159u) * (1 + pi144) + ((1 - y159)*xod + y159*xo159d) * (1 + pi174),
 pi160== ((1 - y160)*xol + y160*xo160l) * (1 + pi159) + ((1 - y160)*xor + y160*xo160r) * (1 + pi161) + ((1 - y160)*xou + y160*xo160u) * (1 + pi145) + ((1 - y160)*xod + y160*xo160d) * (1 + pi175),
 pi161== ((1 - y161)*xol + y161*xo161l) * (1 + pi160) + ((1 - y161)*xor + y161*xo161r) * (1 + pi162) + ((1 - y161)*xou + y161*xo161u) * (1 + pi146) + ((1 - y161)*xod + y161*xo161d) * (1 + pi176),
 pi162== ((1 - y162)*xol + y162*xo162l) * (1 + pi161) + ((1 - y162)*xor + y162*xo162r) * (1 + pi163) + ((1 - y162)*xou + y162*xo162u) * (1 + pi147) + ((1 - y162)*xod + y162*xo162d) * (1 + pi177),
 pi163== ((1 - y163)*xol + y163*xo163l) * (1 + pi162) + ((1 - y163)*xor + y163*xo163r) * (1 + pi164) + ((1 - y163)*xou + y163*xo163u) * (1 + pi148) + ((1 - y163)*xod + y163*xo163d) * (1 + pi178),
 pi164== ((1 - y164)*xol + y164*xo164l) * (1 + pi163) + ((1 - y164)*xor + y164*xo164r) * (1 + pi165) + ((1 - y164)*xou + y164*xo164u) * (1 + pi149) + ((1 - y164)*xod + y164*xo164d) * (1 + pi179),
 pi165== ((1 - y165)*xol + y165*xo165l) * (1 + pi164) + ((1 - y165)*xor + y165*xo165r) * (1 + pi166) + ((1 - y165)*xou + y165*xo165u) * (1 + pi150) + ((1 - y165)*xod + y165*xo165d) * (1 + pi180),
 pi166== ((1 - y166)*xol + y166*xo166l) * (1 + pi165) + ((1 - y166)*xor + y166*xo166r) * (1 + pi167) + ((1 - y166)*xou + y166*xo166u) * (1 + pi151) + ((1 - y166)*xod + y166*xo166d) * (1 + pi181),
 pi167== ((1 - y167)*xol + y167*xo167l) * (1 + pi166) + ((1 - y167)*xor + y167*xo167r) * (1 + pi168) + ((1 - y167)*xou + y167*xo167u) * (1 + pi152) + ((1 - y167)*xod + y167*xo167d) * (1 + pi182),
 pi168== ((1 - y168)*xol + y168*xo168l) * (1 + pi167) + ((1 - y168)*xor + y168*xo168r) * (1 + pi169) + ((1 - y168)*xou + y168*xo168u) * (1 + pi153) + ((1 - y168)*xod + y168*xo168d) * (1 + pi183),
 pi169== ((1 - y169)*xol + y169*xo169l) * (1 + pi168) + ((1 - y169)*xor + y169*xo169r) * (1 + pi170) + ((1 - y169)*xou + y169*xo169u) * (1 + pi154) + ((1 - y169)*xod + y169*xo169d) * (1 + pi184),
 pi170== ((1 - y170)*xol + y170*xo170l) * (1 + pi169) + ((1 - y170)*xor + y170*xo170r) * (1 + pi171) + ((1 - y170)*xou + y170*xo170u) * (1 + pi155) + ((1 - y170)*xod + y170*xo170d) * (1 + pi185),
 pi171== ((1 - y171)*xol + y171*xo171l) * (1 + pi170) + ((1 - y171)*xor + y171*xo171r) * (1 + pi172) + ((1 - y171)*xou + y171*xo171u) * (1 + pi156) + ((1 - y171)*xod + y171*xo171d) * (1 + pi186),
 pi172== ((1 - y172)*xol + y172*xo172l) * (1 + pi171) + ((1 - y172)*xor + y172*xo172r) * (1 + pi173) + ((1 - y172)*xou + y172*xo172u) * (1 + pi157) + ((1 - y172)*xod + y172*xo172d) * (1 + pi187),
 pi173== ((1 - y173)*xol + y173*xo173l) * (1 + pi172) + ((1 - y173)*xor + y173*xo173r) * (1 + pi174) + ((1 - y173)*xou + y173*xo173u) * (1 + pi158) + ((1 - y173)*xod + y173*xo173d) * (1 + pi188),
 pi174== ((1 - y174)*xol + y174*xo174l) * (1 + pi173) + ((1 - y174)*xor + y174*xo174r) * (1 + pi175) + ((1 - y174)*xou + y174*xo174u) * (1 + pi159) + ((1 - y174)*xod + y174*xo174d) * (1 + pi189),
 pi175== ((1 - y175)*xol + y175*xo175l) * (1 + pi174) + ((1 - y175)*xor + y175*xo175r) * (1 + pi176) + ((1 - y175)*xou + y175*xo175u) * (1 + pi160) + ((1 - y175)*xod + y175*xo175d) * (1 + pi190),
 pi176== ((1 - y176)*xol + y176*xo176l) * (1 + pi175) + ((1 - y176)*xor + y176*xo176r) * (1 + pi177) + ((1 - y176)*xou + y176*xo176u) * (1 + pi161) + ((1 - y176)*xod + y176*xo176d) * (1 + pi191),
 pi177== ((1 - y177)*xol + y177*xo177l) * (1 + pi176) + ((1 - y177)*xor + y177*xo177r) * (1 + pi178) + ((1 - y177)*xou + y177*xo177u) * (1 + pi162) + ((1 - y177)*xod + y177*xo177d) * (1 + pi192),
 pi178== ((1 - y178)*xol + y178*xo178l) * (1 + pi177) + ((1 - y178)*xor + y178*xo178r) * (1 + pi179) + ((1 - y178)*xou + y178*xo178u) * (1 + pi163) + ((1 - y178)*xod + y178*xo178d) * (1 + pi193),
 pi179== ((1 - y179)*xol + y179*xo179l) * (1 + pi178) + ((1 - y179)*xor + y179*xo179r) * (1 + pi180) + ((1 - y179)*xou + y179*xo179u) * (1 + pi164) + ((1 - y179)*xod + y179*xo179d) * (1 + pi194),
 pi180== ((1 - y180)*xol + y180*xo180l) * (1 + pi179) + ((1 - y180)*xor + y180*xo180r) * (1 + pi181) + ((1 - y180)*xou + y180*xo180u) * (1 + pi165) + ((1 - y180)*xod + y180*xo180d) * (1 + pi195),
 pi181== ((1 - y181)*xol + y181*xo181l) * (1 + pi180) + ((1 - y181)*xor + y181*xo181r) * (1 + pi182) + ((1 - y181)*xou + y181*xo181u) * (1 + pi166) + ((1 - y181)*xod + y181*xo181d) * (1 + pi196),
 pi182== ((1 - y182)*xol + y182*xo182l) * (1 + pi181) + ((1 - y182)*xor + y182*xo182r) * (1 + pi183) + ((1 - y182)*xou + y182*xo182u) * (1 + pi167) + ((1 - y182)*xod + y182*xo182d) * (1 + pi197),
 pi183== ((1 - y183)*xol + y183*xo183l) * (1 + pi182) + ((1 - y183)*xor + y183*xo183r) * (1 + pi184) + ((1 - y183)*xou + y183*xo183u) * (1 + pi168) + ((1 - y183)*xod + y183*xo183d) * (1 + pi198),
 pi184== ((1 - y184)*xol + y184*xo184l) * (1 + pi183) + ((1 - y184)*xor + y184*xo184r) * (1 + pi185) + ((1 - y184)*xou + y184*xo184u) * (1 + pi169) + ((1 - y184)*xod + y184*xo184d) * (1 + pi199),
 pi185== ((1 - y185)*xol + y185*xo185l) * (1 + pi184) + ((1 - y185)*xor + y185*xo185r) * (1 + pi186) + ((1 - y185)*xou + y185*xo185u) * (1 + pi170) + ((1 - y185)*xod + y185*xo185d) * (1 + pi200),
 pi186== ((1 - y186)*xol + y186*xo186l) * (1 + pi185) + ((1 - y186)*xor + y186*xo186r) * (1 + pi187) + ((1 - y186)*xou + y186*xo186u) * (1 + pi171) + ((1 - y186)*xod + y186*xo186d) * (1 + pi201),
 pi187== ((1 - y187)*xol + y187*xo187l) * (1 + pi186) + ((1 - y187)*xor + y187*xo187r) * (1 + pi188) + ((1 - y187)*xou + y187*xo187u) * (1 + pi172) + ((1 - y187)*xod + y187*xo187d) * (1 + pi202),
 pi188== ((1 - y188)*xol + y188*xo188l) * (1 + pi187) + ((1 - y188)*xor + y188*xo188r) * (1 + pi189) + ((1 - y188)*xou + y188*xo188u) * (1 + pi173) + ((1 - y188)*xod + y188*xo188d) * (1 + pi203),
 pi189== ((1 - y189)*xol + y189*xo189l) * (1 + pi188) + ((1 - y189)*xor + y189*xo189r) * (1 + pi190) + ((1 - y189)*xou + y189*xo189u) * (1 + pi174) + ((1 - y189)*xod + y189*xo189d) * (1 + pi204),
 pi190== ((1 - y190)*xol + y190*xo190l) * (1 + pi189) + ((1 - y190)*xor + y190*xo190r) * (1 + pi191) + ((1 - y190)*xou + y190*xo190u) * (1 + pi175) + ((1 - y190)*xod + y190*xo190d) * (1 + pi205),
 pi191== ((1 - y191)*xol + y191*xo191l) * (1 + pi190) + ((1 - y191)*xor + y191*xo191r) * (1 + pi192) + ((1 - y191)*xou + y191*xo191u) * (1 + pi176) + ((1 - y191)*xod + y191*xo191d) * (1 + pi206),
 pi192== ((1 - y192)*xol + y192*xo192l) * (1 + pi191) + ((1 - y192)*xor + y192*xo192r) * (1 + pi193) + ((1 - y192)*xou + y192*xo192u) * (1 + pi177) + ((1 - y192)*xod + y192*xo192d) * (1 + pi207),
 pi193== ((1 - y193)*xol + y193*xo193l) * (1 + pi192) + ((1 - y193)*xor + y193*xo193r) * (1 + pi194) + ((1 - y193)*xou + y193*xo193u) * (1 + pi178) + ((1 - y193)*xod + y193*xo193d) * (1 + pi208),
 pi194== ((1 - y194)*xol + y194*xo194l) * (1 + pi193) + ((1 - y194)*xor + y194*xo194r) * (1 + pi195) + ((1 - y194)*xou + y194*xo194u) * (1 + pi179) + ((1 - y194)*xod + y194*xo194d) * (1 + pi209),
 pi195== ((1 - y195)*xol + y195*xo195l) * (1 + pi194) + ((1 - y195)*xor + y195*xo195r) * (1 + pi196) + ((1 - y195)*xou + y195*xo195u) * (1 + pi180) + ((1 - y195)*xod + y195*xo195d) * (1 + pi210),
 pi196== ((1 - y196)*xol + y196*xo196l) * (1 + pi195) + ((1 - y196)*xor + y196*xo196r) * (1 + pi197) + ((1 - y196)*xou + y196*xo196u) * (1 + pi181) + ((1 - y196)*xod + y196*xo196d) * (1 + pi211),
 pi197== ((1 - y197)*xol + y197*xo197l) * (1 + pi196) + ((1 - y197)*xor + y197*xo197r) * (1 + pi198) + ((1 - y197)*xou + y197*xo197u) * (1 + pi182) + ((1 - y197)*xod + y197*xo197d) * (1 + pi212),
 pi198== ((1 - y198)*xol + y198*xo198l) * (1 + pi197) + ((1 - y198)*xor + y198*xo198r) * (1 + pi199) + ((1 - y198)*xou + y198*xo198u) * (1 + pi183) + ((1 - y198)*xod + y198*xo198d) * (1 + pi213),
 pi199== ((1 - y199)*xol + y199*xo199l) * (1 + pi198) + ((1 - y199)*xor + y199*xo199r) * (1 + pi200) + ((1 - y199)*xou + y199*xo199u) * (1 + pi184) + ((1 - y199)*xod + y199*xo199d) * (1 + pi214),
 pi200== ((1 - y200)*xol + y200*xo200l) * (1 + pi199) + ((1 - y200)*xor + y200*xo200r) * (1 + pi201) + ((1 - y200)*xou + y200*xo200u) * (1 + pi185) + ((1 - y200)*xod + y200*xo200d) * (1 + pi215),
 pi201== ((1 - y201)*xol + y201*xo201l) * (1 + pi200) + ((1 - y201)*xor + y201*xo201r) * (1 + pi202) + ((1 - y201)*xou + y201*xo201u) * (1 + pi186) + ((1 - y201)*xod + y201*xo201d) * (1 + pi216),
 pi202== ((1 - y202)*xol + y202*xo202l) * (1 + pi201) + ((1 - y202)*xor + y202*xo202r) * (1 + pi203) + ((1 - y202)*xou + y202*xo202u) * (1 + pi187) + ((1 - y202)*xod + y202*xo202d) * (1 + pi217),
 pi203== ((1 - y203)*xol + y203*xo203l) * (1 + pi202) + ((1 - y203)*xor + y203*xo203r) * (1 + pi204) + ((1 - y203)*xou + y203*xo203u) * (1 + pi188) + ((1 - y203)*xod + y203*xo203d) * (1 + pi218),
 pi204== ((1 - y204)*xol + y204*xo204l) * (1 + pi203) + ((1 - y204)*xor + y204*xo204r) * (1 + pi205) + ((1 - y204)*xou + y204*xo204u) * (1 + pi189) + ((1 - y204)*xod + y204*xo204d) * (1 + pi219),
 pi205== ((1 - y205)*xol + y205*xo205l) * (1 + pi204) + ((1 - y205)*xor + y205*xo205r) * (1 + pi206) + ((1 - y205)*xou + y205*xo205u) * (1 + pi190) + ((1 - y205)*xod + y205*xo205d) * (1 + pi220),
 pi206== ((1 - y206)*xol + y206*xo206l) * (1 + pi205) + ((1 - y206)*xor + y206*xo206r) * (1 + pi207) + ((1 - y206)*xou + y206*xo206u) * (1 + pi191) + ((1 - y206)*xod + y206*xo206d) * (1 + pi221),
 pi207== ((1 - y207)*xol + y207*xo207l) * (1 + pi206) + ((1 - y207)*xor + y207*xo207r) * (1 + pi208) + ((1 - y207)*xou + y207*xo207u) * (1 + pi192) + ((1 - y207)*xod + y207*xo207d) * (1 + pi222),
 pi208== ((1 - y208)*xol + y208*xo208l) * (1 + pi207) + ((1 - y208)*xor + y208*xo208r) * (1 + pi209) + ((1 - y208)*xou + y208*xo208u) * (1 + pi193) + ((1 - y208)*xod + y208*xo208d) * (1 + pi223),
 pi209== ((1 - y209)*xol + y209*xo209l) * (1 + pi208) + ((1 - y209)*xor + y209*xo209r) * (1 + pi210) + ((1 - y209)*xou + y209*xo209u) * (1 + pi194) + ((1 - y209)*xod + y209*xo209d) * (1 + pi224),
 pi210== ((1 - y210)*xol + y210*xo210l) * (1 + pi209) + ((1 - y210)*xor + y210*xo210r) * (1 + pi211) + ((1 - y210)*xou + y210*xo210u) * (1 + pi195) + ((1 - y210)*xod + y210*xo210d) * (1 + pi210), 
pi211== ((1 - y211)*xol + y211*xo211l) * (1 + pi210) + ((1 - y211)*xor + y211*xo211r) * (1 + pi212) + ((1 - y211)*xou + y211*xo211u) * (1 + pi196) + ((1 - y211)*xod + y211*xo211d) * (1 + pi211), 
pi212== ((1 - y212)*xol + y212*xo212l) * (1 + pi211) + ((1 - y212)*xor + y212*xo212r) * (1 + pi213) + ((1 - y212)*xou + y212*xo212u) * (1 + pi197) + ((1 - y212)*xod + y212*xo212d) * (1 + pi212), 
pi213== ((1 - y213)*xol + y213*xo213l) * (1 + pi212) + ((1 - y213)*xor + y213*xo213r) * (1 + pi214) + ((1 - y213)*xou + y213*xo213u) * (1 + pi198) + ((1 - y213)*xod + y213*xo213d) * (1 + pi213), 
pi214== ((1 - y214)*xol + y214*xo214l) * (1 + pi213) + ((1 - y214)*xor + y214*xo214r) * (1 + pi215) + ((1 - y214)*xou + y214*xo214u) * (1 + pi199) + ((1 - y214)*xod + y214*xo214d) * (1 + pi214), 
pi215== ((1 - y215)*xol + y215*xo215l) * (1 + pi214) + ((1 - y215)*xor + y215*xo215r) * (1 + pi216) + ((1 - y215)*xou + y215*xo215u) * (1 + pi200) + ((1 - y215)*xod + y215*xo215d) * (1 + pi215), 
pi216== ((1 - y216)*xol + y216*xo216l) * (1 + pi215) + ((1 - y216)*xor + y216*xo216r) * (1 + pi217) + ((1 - y216)*xou + y216*xo216u) * (1 + pi201) + ((1 - y216)*xod + y216*xo216d) * (1 + pi216), 
pi217== ((1 - y217)*xol + y217*xo217l) * (1 + pi216) + ((1 - y217)*xor + y217*xo217r) * (1 + pi218) + ((1 - y217)*xou + y217*xo217u) * (1 + pi202) + ((1 - y217)*xod + y217*xo217d) * (1 + pi217), 
pi218== ((1 - y218)*xol + y218*xo218l) * (1 + pi217) + ((1 - y218)*xor + y218*xo218r) * (1 + pi219) + ((1 - y218)*xou + y218*xo218u) * (1 + pi203) + ((1 - y218)*xod + y218*xo218d) * (1 + pi218), 
pi219== ((1 - y219)*xol + y219*xo219l) * (1 + pi218) + ((1 - y219)*xor + y219*xo219r) * (1 + pi220) + ((1 - y219)*xou + y219*xo219u) * (1 + pi204) + ((1 - y219)*xod + y219*xo219d) * (1 + pi219), 
pi220== ((1 - y220)*xol + y220*xo220l) * (1 + pi219) + ((1 - y220)*xor + y220*xo220r) * (1 + pi221) + ((1 - y220)*xou + y220*xo220u) * (1 + pi205) + ((1 - y220)*xod + y220*xo220d) * (1 + pi220), 
pi221== ((1 - y221)*xol + y221*xo221l) * (1 + pi220) + ((1 - y221)*xor + y221*xo221r) * (1 + pi222) + ((1 - y221)*xou + y221*xo221u) * (1 + pi206) + ((1 - y221)*xod + y221*xo221d) * (1 + pi221), 
pi222== ((1 - y222)*xol + y222*xo222l) * (1 + pi221) + ((1 - y222)*xor + y222*xo222r) * (1 + pi223) + ((1 - y222)*xou + y222*xo222u) * (1 + pi207) + ((1 - y222)*xod + y222*xo222d) * (1 + pi222), 
pi223== ((1 - y223)*xol + y223*xo223l) * (1 + pi222) + ((1 - y223)*xor + y223*xo223r) * (1 + pi224) + ((1 - y223)*xou + y223*xo223u) * (1 + pi208) + ((1 - y223)*xod + y223*xo223d) * (1 + pi223), 
pi224 == 0, 
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= Q(3150,224)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi99+pi100+pi101+pi102+pi103+pi104+pi105+pi106+pi107+pi108+pi109+pi110+pi111+pi112+pi113+pi114+pi115+pi116+pi117+pi118+pi119+pi120+pi121+pi122+pi123+pi124+pi125+pi126+pi127+pi128+pi129+pi130+pi131+pi132+pi133+pi134+pi135+pi136+pi137+pi138+pi139+pi140+pi141+pi142+pi143+pi144+pi145+pi146+pi147+pi148+pi149+pi150+pi151+pi152+pi153+pi154+pi155+pi156+pi157+pi158+pi159+pi160+pi161+pi162+pi163+pi164+pi165+pi166+pi167+pi168+pi169+pi170+pi171+pi172+pi173+pi174+pi175+pi176+pi177+pi178+pi179+pi180+pi181+pi182+pi183+pi184+pi185+pi186+pi187+pi188+pi189+pi190+pi191+pi192+pi193+pi194+pi195+pi196+pi197+pi198+pi199+pi200+pi201+pi202+pi203+pi204+pi205+pi206+pi207+pi208+pi209+pi210+pi211+pi212+pi213+pi214+pi215+pi216+pi217+pi218+pi219+pi220+pi221+pi222+pi223) * Q(1,224) <= Q(3150,224),
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
xo121l <= 1,
xo121l >= 0,
xo121r <= 1,
xo121r >= 0,
xo121u <= 1,
xo121u >= 0,
xo121d <= 1,
xo121d >= 0,
xo121l + xo121r + xo121u + xo121d == 1,
xo122l <= 1,
xo122l >= 0,
xo122r <= 1,
xo122r >= 0,
xo122u <= 1,
xo122u >= 0,
xo122d <= 1,
xo122d >= 0,
xo122l + xo122r + xo122u + xo122d == 1,
xo123l <= 1,
xo123l >= 0,
xo123r <= 1,
xo123r >= 0,
xo123u <= 1,
xo123u >= 0,
xo123d <= 1,
xo123d >= 0,
xo123l + xo123r + xo123u + xo123d == 1,
xo124l <= 1,
xo124l >= 0,
xo124r <= 1,
xo124r >= 0,
xo124u <= 1,
xo124u >= 0,
xo124d <= 1,
xo124d >= 0,
xo124l + xo124r + xo124u + xo124d == 1,
xo125l <= 1,
xo125l >= 0,
xo125r <= 1,
xo125r >= 0,
xo125u <= 1,
xo125u >= 0,
xo125d <= 1,
xo125d >= 0,
xo125l + xo125r + xo125u + xo125d == 1,
xo126l <= 1,
xo126l >= 0,
xo126r <= 1,
xo126r >= 0,
xo126u <= 1,
xo126u >= 0,
xo126d <= 1,
xo126d >= 0,
xo126l + xo126r + xo126u + xo126d == 1,
xo127l <= 1,
xo127l >= 0,
xo127r <= 1,
xo127r >= 0,
xo127u <= 1,
xo127u >= 0,
xo127d <= 1,
xo127d >= 0,
xo127l + xo127r + xo127u + xo127d == 1,
xo128l <= 1,
xo128l >= 0,
xo128r <= 1,
xo128r >= 0,
xo128u <= 1,
xo128u >= 0,
xo128d <= 1,
xo128d >= 0,
xo128l + xo128r + xo128u + xo128d == 1,
xo129l <= 1,
xo129l >= 0,
xo129r <= 1,
xo129r >= 0,
xo129u <= 1,
xo129u >= 0,
xo129d <= 1,
xo129d >= 0,
xo129l + xo129r + xo129u + xo129d == 1,
xo130l <= 1,
xo130l >= 0,
xo130r <= 1,
xo130r >= 0,
xo130u <= 1,
xo130u >= 0,
xo130d <= 1,
xo130d >= 0,
xo130l + xo130r + xo130u + xo130d == 1,
xo131l <= 1,
xo131l >= 0,
xo131r <= 1,
xo131r >= 0,
xo131u <= 1,
xo131u >= 0,
xo131d <= 1,
xo131d >= 0,
xo131l + xo131r + xo131u + xo131d == 1,
xo132l <= 1,
xo132l >= 0,
xo132r <= 1,
xo132r >= 0,
xo132u <= 1,
xo132u >= 0,
xo132d <= 1,
xo132d >= 0,
xo132l + xo132r + xo132u + xo132d == 1,
xo133l <= 1,
xo133l >= 0,
xo133r <= 1,
xo133r >= 0,
xo133u <= 1,
xo133u >= 0,
xo133d <= 1,
xo133d >= 0,
xo133l + xo133r + xo133u + xo133d == 1,
xo134l <= 1,
xo134l >= 0,
xo134r <= 1,
xo134r >= 0,
xo134u <= 1,
xo134u >= 0,
xo134d <= 1,
xo134d >= 0,
xo134l + xo134r + xo134u + xo134d == 1,
xo135l <= 1,
xo135l >= 0,
xo135r <= 1,
xo135r >= 0,
xo135u <= 1,
xo135u >= 0,
xo135d <= 1,
xo135d >= 0,
xo135l + xo135r + xo135u + xo135d == 1,
xo136l <= 1,
xo136l >= 0,
xo136r <= 1,
xo136r >= 0,
xo136u <= 1,
xo136u >= 0,
xo136d <= 1,
xo136d >= 0,
xo136l + xo136r + xo136u + xo136d == 1,
xo137l <= 1,
xo137l >= 0,
xo137r <= 1,
xo137r >= 0,
xo137u <= 1,
xo137u >= 0,
xo137d <= 1,
xo137d >= 0,
xo137l + xo137r + xo137u + xo137d == 1,
xo138l <= 1,
xo138l >= 0,
xo138r <= 1,
xo138r >= 0,
xo138u <= 1,
xo138u >= 0,
xo138d <= 1,
xo138d >= 0,
xo138l + xo138r + xo138u + xo138d == 1,
xo139l <= 1,
xo139l >= 0,
xo139r <= 1,
xo139r >= 0,
xo139u <= 1,
xo139u >= 0,
xo139d <= 1,
xo139d >= 0,
xo139l + xo139r + xo139u + xo139d == 1,
xo140l <= 1,
xo140l >= 0,
xo140r <= 1,
xo140r >= 0,
xo140u <= 1,
xo140u >= 0,
xo140d <= 1,
xo140d >= 0,
xo140l + xo140r + xo140u + xo140d == 1,
xo141l <= 1,
xo141l >= 0,
xo141r <= 1,
xo141r >= 0,
xo141u <= 1,
xo141u >= 0,
xo141d <= 1,
xo141d >= 0,
xo141l + xo141r + xo141u + xo141d == 1,
xo142l <= 1,
xo142l >= 0,
xo142r <= 1,
xo142r >= 0,
xo142u <= 1,
xo142u >= 0,
xo142d <= 1,
xo142d >= 0,
xo142l + xo142r + xo142u + xo142d == 1,
xo143l <= 1,
xo143l >= 0,
xo143r <= 1,
xo143r >= 0,
xo143u <= 1,
xo143u >= 0,
xo143d <= 1,
xo143d >= 0,
xo143l + xo143r + xo143u + xo143d == 1,
xo144l <= 1,
xo144l >= 0,
xo144r <= 1,
xo144r >= 0,
xo144u <= 1,
xo144u >= 0,
xo144d <= 1,
xo144d >= 0,
xo144l + xo144r + xo144u + xo144d == 1,
xo145l <= 1,
xo145l >= 0,
xo145r <= 1,
xo145r >= 0,
xo145u <= 1,
xo145u >= 0,
xo145d <= 1,
xo145d >= 0,
xo145l + xo145r + xo145u + xo145d == 1,
xo146l <= 1,
xo146l >= 0,
xo146r <= 1,
xo146r >= 0,
xo146u <= 1,
xo146u >= 0,
xo146d <= 1,
xo146d >= 0,
xo146l + xo146r + xo146u + xo146d == 1,
xo147l <= 1,
xo147l >= 0,
xo147r <= 1,
xo147r >= 0,
xo147u <= 1,
xo147u >= 0,
xo147d <= 1,
xo147d >= 0,
xo147l + xo147r + xo147u + xo147d == 1,
xo148l <= 1,
xo148l >= 0,
xo148r <= 1,
xo148r >= 0,
xo148u <= 1,
xo148u >= 0,
xo148d <= 1,
xo148d >= 0,
xo148l + xo148r + xo148u + xo148d == 1,
xo149l <= 1,
xo149l >= 0,
xo149r <= 1,
xo149r >= 0,
xo149u <= 1,
xo149u >= 0,
xo149d <= 1,
xo149d >= 0,
xo149l + xo149r + xo149u + xo149d == 1,
xo150l <= 1,
xo150l >= 0,
xo150r <= 1,
xo150r >= 0,
xo150u <= 1,
xo150u >= 0,
xo150d <= 1,
xo150d >= 0,
xo150l + xo150r + xo150u + xo150d == 1,
xo151l <= 1,
xo151l >= 0,
xo151r <= 1,
xo151r >= 0,
xo151u <= 1,
xo151u >= 0,
xo151d <= 1,
xo151d >= 0,
xo151l + xo151r + xo151u + xo151d == 1,
xo152l <= 1,
xo152l >= 0,
xo152r <= 1,
xo152r >= 0,
xo152u <= 1,
xo152u >= 0,
xo152d <= 1,
xo152d >= 0,
xo152l + xo152r + xo152u + xo152d == 1,
xo153l <= 1,
xo153l >= 0,
xo153r <= 1,
xo153r >= 0,
xo153u <= 1,
xo153u >= 0,
xo153d <= 1,
xo153d >= 0,
xo153l + xo153r + xo153u + xo153d == 1,
xo154l <= 1,
xo154l >= 0,
xo154r <= 1,
xo154r >= 0,
xo154u <= 1,
xo154u >= 0,
xo154d <= 1,
xo154d >= 0,
xo154l + xo154r + xo154u + xo154d == 1,
xo155l <= 1,
xo155l >= 0,
xo155r <= 1,
xo155r >= 0,
xo155u <= 1,
xo155u >= 0,
xo155d <= 1,
xo155d >= 0,
xo155l + xo155r + xo155u + xo155d == 1,
xo156l <= 1,
xo156l >= 0,
xo156r <= 1,
xo156r >= 0,
xo156u <= 1,
xo156u >= 0,
xo156d <= 1,
xo156d >= 0,
xo156l + xo156r + xo156u + xo156d == 1,
xo157l <= 1,
xo157l >= 0,
xo157r <= 1,
xo157r >= 0,
xo157u <= 1,
xo157u >= 0,
xo157d <= 1,
xo157d >= 0,
xo157l + xo157r + xo157u + xo157d == 1,
xo158l <= 1,
xo158l >= 0,
xo158r <= 1,
xo158r >= 0,
xo158u <= 1,
xo158u >= 0,
xo158d <= 1,
xo158d >= 0,
xo158l + xo158r + xo158u + xo158d == 1,
xo159l <= 1,
xo159l >= 0,
xo159r <= 1,
xo159r >= 0,
xo159u <= 1,
xo159u >= 0,
xo159d <= 1,
xo159d >= 0,
xo159l + xo159r + xo159u + xo159d == 1,
xo160l <= 1,
xo160l >= 0,
xo160r <= 1,
xo160r >= 0,
xo160u <= 1,
xo160u >= 0,
xo160d <= 1,
xo160d >= 0,
xo160l + xo160r + xo160u + xo160d == 1,
xo161l <= 1,
xo161l >= 0,
xo161r <= 1,
xo161r >= 0,
xo161u <= 1,
xo161u >= 0,
xo161d <= 1,
xo161d >= 0,
xo161l + xo161r + xo161u + xo161d == 1,
xo162l <= 1,
xo162l >= 0,
xo162r <= 1,
xo162r >= 0,
xo162u <= 1,
xo162u >= 0,
xo162d <= 1,
xo162d >= 0,
xo162l + xo162r + xo162u + xo162d == 1,
xo163l <= 1,
xo163l >= 0,
xo163r <= 1,
xo163r >= 0,
xo163u <= 1,
xo163u >= 0,
xo163d <= 1,
xo163d >= 0,
xo163l + xo163r + xo163u + xo163d == 1,
xo164l <= 1,
xo164l >= 0,
xo164r <= 1,
xo164r >= 0,
xo164u <= 1,
xo164u >= 0,
xo164d <= 1,
xo164d >= 0,
xo164l + xo164r + xo164u + xo164d == 1,
xo165l <= 1,
xo165l >= 0,
xo165r <= 1,
xo165r >= 0,
xo165u <= 1,
xo165u >= 0,
xo165d <= 1,
xo165d >= 0,
xo165l + xo165r + xo165u + xo165d == 1,
xo166l <= 1,
xo166l >= 0,
xo166r <= 1,
xo166r >= 0,
xo166u <= 1,
xo166u >= 0,
xo166d <= 1,
xo166d >= 0,
xo166l + xo166r + xo166u + xo166d == 1,
xo167l <= 1,
xo167l >= 0,
xo167r <= 1,
xo167r >= 0,
xo167u <= 1,
xo167u >= 0,
xo167d <= 1,
xo167d >= 0,
xo167l + xo167r + xo167u + xo167d == 1,
xo168l <= 1,
xo168l >= 0,
xo168r <= 1,
xo168r >= 0,
xo168u <= 1,
xo168u >= 0,
xo168d <= 1,
xo168d >= 0,
xo168l + xo168r + xo168u + xo168d == 1,
xo169l <= 1,
xo169l >= 0,
xo169r <= 1,
xo169r >= 0,
xo169u <= 1,
xo169u >= 0,
xo169d <= 1,
xo169d >= 0,
xo169l + xo169r + xo169u + xo169d == 1,
xo170l <= 1,
xo170l >= 0,
xo170r <= 1,
xo170r >= 0,
xo170u <= 1,
xo170u >= 0,
xo170d <= 1,
xo170d >= 0,
xo170l + xo170r + xo170u + xo170d == 1,
xo171l <= 1,
xo171l >= 0,
xo171r <= 1,
xo171r >= 0,
xo171u <= 1,
xo171u >= 0,
xo171d <= 1,
xo171d >= 0,
xo171l + xo171r + xo171u + xo171d == 1,
xo172l <= 1,
xo172l >= 0,
xo172r <= 1,
xo172r >= 0,
xo172u <= 1,
xo172u >= 0,
xo172d <= 1,
xo172d >= 0,
xo172l + xo172r + xo172u + xo172d == 1,
xo173l <= 1,
xo173l >= 0,
xo173r <= 1,
xo173r >= 0,
xo173u <= 1,
xo173u >= 0,
xo173d <= 1,
xo173d >= 0,
xo173l + xo173r + xo173u + xo173d == 1,
xo174l <= 1,
xo174l >= 0,
xo174r <= 1,
xo174r >= 0,
xo174u <= 1,
xo174u >= 0,
xo174d <= 1,
xo174d >= 0,
xo174l + xo174r + xo174u + xo174d == 1,
xo175l <= 1,
xo175l >= 0,
xo175r <= 1,
xo175r >= 0,
xo175u <= 1,
xo175u >= 0,
xo175d <= 1,
xo175d >= 0,
xo175l + xo175r + xo175u + xo175d == 1,
xo176l <= 1,
xo176l >= 0,
xo176r <= 1,
xo176r >= 0,
xo176u <= 1,
xo176u >= 0,
xo176d <= 1,
xo176d >= 0,
xo176l + xo176r + xo176u + xo176d == 1,
xo177l <= 1,
xo177l >= 0,
xo177r <= 1,
xo177r >= 0,
xo177u <= 1,
xo177u >= 0,
xo177d <= 1,
xo177d >= 0,
xo177l + xo177r + xo177u + xo177d == 1,
xo178l <= 1,
xo178l >= 0,
xo178r <= 1,
xo178r >= 0,
xo178u <= 1,
xo178u >= 0,
xo178d <= 1,
xo178d >= 0,
xo178l + xo178r + xo178u + xo178d == 1,
xo179l <= 1,
xo179l >= 0,
xo179r <= 1,
xo179r >= 0,
xo179u <= 1,
xo179u >= 0,
xo179d <= 1,
xo179d >= 0,
xo179l + xo179r + xo179u + xo179d == 1,
xo180l <= 1,
xo180l >= 0,
xo180r <= 1,
xo180r >= 0,
xo180u <= 1,
xo180u >= 0,
xo180d <= 1,
xo180d >= 0,
xo180l + xo180r + xo180u + xo180d == 1,
xo181l <= 1,
xo181l >= 0,
xo181r <= 1,
xo181r >= 0,
xo181u <= 1,
xo181u >= 0,
xo181d <= 1,
xo181d >= 0,
xo181l + xo181r + xo181u + xo181d == 1,
xo182l <= 1,
xo182l >= 0,
xo182r <= 1,
xo182r >= 0,
xo182u <= 1,
xo182u >= 0,
xo182d <= 1,
xo182d >= 0,
xo182l + xo182r + xo182u + xo182d == 1,
xo183l <= 1,
xo183l >= 0,
xo183r <= 1,
xo183r >= 0,
xo183u <= 1,
xo183u >= 0,
xo183d <= 1,
xo183d >= 0,
xo183l + xo183r + xo183u + xo183d == 1,
xo184l <= 1,
xo184l >= 0,
xo184r <= 1,
xo184r >= 0,
xo184u <= 1,
xo184u >= 0,
xo184d <= 1,
xo184d >= 0,
xo184l + xo184r + xo184u + xo184d == 1,
xo185l <= 1,
xo185l >= 0,
xo185r <= 1,
xo185r >= 0,
xo185u <= 1,
xo185u >= 0,
xo185d <= 1,
xo185d >= 0,
xo185l + xo185r + xo185u + xo185d == 1,
xo186l <= 1,
xo186l >= 0,
xo186r <= 1,
xo186r >= 0,
xo186u <= 1,
xo186u >= 0,
xo186d <= 1,
xo186d >= 0,
xo186l + xo186r + xo186u + xo186d == 1,
xo187l <= 1,
xo187l >= 0,
xo187r <= 1,
xo187r >= 0,
xo187u <= 1,
xo187u >= 0,
xo187d <= 1,
xo187d >= 0,
xo187l + xo187r + xo187u + xo187d == 1,
xo188l <= 1,
xo188l >= 0,
xo188r <= 1,
xo188r >= 0,
xo188u <= 1,
xo188u >= 0,
xo188d <= 1,
xo188d >= 0,
xo188l + xo188r + xo188u + xo188d == 1,
xo189l <= 1,
xo189l >= 0,
xo189r <= 1,
xo189r >= 0,
xo189u <= 1,
xo189u >= 0,
xo189d <= 1,
xo189d >= 0,
xo189l + xo189r + xo189u + xo189d == 1,
xo190l <= 1,
xo190l >= 0,
xo190r <= 1,
xo190r >= 0,
xo190u <= 1,
xo190u >= 0,
xo190d <= 1,
xo190d >= 0,
xo190l + xo190r + xo190u + xo190d == 1,
xo191l <= 1,
xo191l >= 0,
xo191r <= 1,
xo191r >= 0,
xo191u <= 1,
xo191u >= 0,
xo191d <= 1,
xo191d >= 0,
xo191l + xo191r + xo191u + xo191d == 1,
xo192l <= 1,
xo192l >= 0,
xo192r <= 1,
xo192r >= 0,
xo192u <= 1,
xo192u >= 0,
xo192d <= 1,
xo192d >= 0,
xo192l + xo192r + xo192u + xo192d == 1,
xo193l <= 1,
xo193l >= 0,
xo193r <= 1,
xo193r >= 0,
xo193u <= 1,
xo193u >= 0,
xo193d <= 1,
xo193d >= 0,
xo193l + xo193r + xo193u + xo193d == 1,
xo194l <= 1,
xo194l >= 0,
xo194r <= 1,
xo194r >= 0,
xo194u <= 1,
xo194u >= 0,
xo194d <= 1,
xo194d >= 0,
xo194l + xo194r + xo194u + xo194d == 1,
xo195l <= 1,
xo195l >= 0,
xo195r <= 1,
xo195r >= 0,
xo195u <= 1,
xo195u >= 0,
xo195d <= 1,
xo195d >= 0,
xo195l + xo195r + xo195u + xo195d == 1,
xo196l <= 1,
xo196l >= 0,
xo196r <= 1,
xo196r >= 0,
xo196u <= 1,
xo196u >= 0,
xo196d <= 1,
xo196d >= 0,
xo196l + xo196r + xo196u + xo196d == 1,
xo197l <= 1,
xo197l >= 0,
xo197r <= 1,
xo197r >= 0,
xo197u <= 1,
xo197u >= 0,
xo197d <= 1,
xo197d >= 0,
xo197l + xo197r + xo197u + xo197d == 1,
xo198l <= 1,
xo198l >= 0,
xo198r <= 1,
xo198r >= 0,
xo198u <= 1,
xo198u >= 0,
xo198d <= 1,
xo198d >= 0,
xo198l + xo198r + xo198u + xo198d == 1,
xo199l <= 1,
xo199l >= 0,
xo199r <= 1,
xo199r >= 0,
xo199u <= 1,
xo199u >= 0,
xo199d <= 1,
xo199d >= 0,
xo199l + xo199r + xo199u + xo199d == 1,
xo200l <= 1,
xo200l >= 0,
xo200r <= 1,
xo200r >= 0,
xo200u <= 1,
xo200u >= 0,
xo200d <= 1,
xo200d >= 0,
xo200l + xo200r + xo200u + xo200d == 1,
xo201l <= 1,
xo201l >= 0,
xo201r <= 1,
xo201r >= 0,
xo201u <= 1,
xo201u >= 0,
xo201d <= 1,
xo201d >= 0,
xo201l + xo201r + xo201u + xo201d == 1,
xo202l <= 1,
xo202l >= 0,
xo202r <= 1,
xo202r >= 0,
xo202u <= 1,
xo202u >= 0,
xo202d <= 1,
xo202d >= 0,
xo202l + xo202r + xo202u + xo202d == 1,
xo203l <= 1,
xo203l >= 0,
xo203r <= 1,
xo203r >= 0,
xo203u <= 1,
xo203u >= 0,
xo203d <= 1,
xo203d >= 0,
xo203l + xo203r + xo203u + xo203d == 1,
xo204l <= 1,
xo204l >= 0,
xo204r <= 1,
xo204r >= 0,
xo204u <= 1,
xo204u >= 0,
xo204d <= 1,
xo204d >= 0,
xo204l + xo204r + xo204u + xo204d == 1,
xo205l <= 1,
xo205l >= 0,
xo205r <= 1,
xo205r >= 0,
xo205u <= 1,
xo205u >= 0,
xo205d <= 1,
xo205d >= 0,
xo205l + xo205r + xo205u + xo205d == 1,
xo206l <= 1,
xo206l >= 0,
xo206r <= 1,
xo206r >= 0,
xo206u <= 1,
xo206u >= 0,
xo206d <= 1,
xo206d >= 0,
xo206l + xo206r + xo206u + xo206d == 1,
xo207l <= 1,
xo207l >= 0,
xo207r <= 1,
xo207r >= 0,
xo207u <= 1,
xo207u >= 0,
xo207d <= 1,
xo207d >= 0,
xo207l + xo207r + xo207u + xo207d == 1,
xo208l <= 1,
xo208l >= 0,
xo208r <= 1,
xo208r >= 0,
xo208u <= 1,
xo208u >= 0,
xo208d <= 1,
xo208d >= 0,
xo208l + xo208r + xo208u + xo208d == 1,
xo209l <= 1,
xo209l >= 0,
xo209r <= 1,
xo209r >= 0,
xo209u <= 1,
xo209u >= 0,
xo209d <= 1,
xo209d >= 0,
xo209l + xo209r + xo209u + xo209d == 1,
xo210l <= 1,
xo210l >= 0,
xo210r <= 1,
xo210r >= 0,
xo210u <= 1,
xo210u >= 0,
xo210d <= 1,
xo210d >= 0,
xo210l + xo210r + xo210u + xo210d == 1,
xo211l <= 1,
xo211l >= 0,
xo211r <= 1,
xo211r >= 0,
xo211u <= 1,
xo211u >= 0,
xo211d <= 1,
xo211d >= 0,
xo211l + xo211r + xo211u + xo211d == 1,
xo212l <= 1,
xo212l >= 0,
xo212r <= 1,
xo212r >= 0,
xo212u <= 1,
xo212u >= 0,
xo212d <= 1,
xo212d >= 0,
xo212l + xo212r + xo212u + xo212d == 1,
xo213l <= 1,
xo213l >= 0,
xo213r <= 1,
xo213r >= 0,
xo213u <= 1,
xo213u >= 0,
xo213d <= 1,
xo213d >= 0,
xo213l + xo213r + xo213u + xo213d == 1,
xo214l <= 1,
xo214l >= 0,
xo214r <= 1,
xo214r >= 0,
xo214u <= 1,
xo214u >= 0,
xo214d <= 1,
xo214d >= 0,
xo214l + xo214r + xo214u + xo214d == 1,
xo215l <= 1,
xo215l >= 0,
xo215r <= 1,
xo215r >= 0,
xo215u <= 1,
xo215u >= 0,
xo215d <= 1,
xo215d >= 0,
xo215l + xo215r + xo215u + xo215d == 1,
xo216l <= 1,
xo216l >= 0,
xo216r <= 1,
xo216r >= 0,
xo216u <= 1,
xo216u >= 0,
xo216d <= 1,
xo216d >= 0,
xo216l + xo216r + xo216u + xo216d == 1,
xo217l <= 1,
xo217l >= 0,
xo217r <= 1,
xo217r >= 0,
xo217u <= 1,
xo217u >= 0,
xo217d <= 1,
xo217d >= 0,
xo217l + xo217r + xo217u + xo217d == 1,
xo218l <= 1,
xo218l >= 0,
xo218r <= 1,
xo218r >= 0,
xo218u <= 1,
xo218u >= 0,
xo218d <= 1,
xo218d >= 0,
xo218l + xo218r + xo218u + xo218d == 1,
xo219l <= 1,
xo219l >= 0,
xo219r <= 1,
xo219r >= 0,
xo219u <= 1,
xo219u >= 0,
xo219d <= 1,
xo219d >= 0,
xo219l + xo219r + xo219u + xo219d == 1,
xo220l <= 1,
xo220l >= 0,
xo220r <= 1,
xo220r >= 0,
xo220u <= 1,
xo220u >= 0,
xo220d <= 1,
xo220d >= 0,
xo220l + xo220r + xo220u + xo220d == 1,
xo221l <= 1,
xo221l >= 0,
xo221r <= 1,
xo221r >= 0,
xo221u <= 1,
xo221u >= 0,
xo221d <= 1,
xo221d >= 0,
xo221l + xo221r + xo221u + xo221d == 1,
xo222l <= 1,
xo222l >= 0,
xo222r <= 1,
xo222r >= 0,
xo222u <= 1,
xo222u >= 0,
xo222d <= 1,
xo222d >= 0,
xo222l + xo222r + xo222u + xo222d == 1,
xo223l <= 1,
xo223l >= 0,
xo223r <= 1,
xo223r >= 0,
xo223u <= 1,
xo223u >= 0,
xo223d <= 1,
xo223d >= 0,
xo223l + xo223r + xo223u + xo223d == 1,
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
Or(xo121l == 0 , xo121l == 1),
Or(xo121r == 0 , xo121r == 1),
Or(xo121u == 0 , xo121u == 1),
Or(xo121d == 0 , xo121d == 1),
Or(xo122l == 0 , xo122l == 1),
Or(xo122r == 0 , xo122r == 1),
Or(xo122u == 0 , xo122u == 1),
Or(xo122d == 0 , xo122d == 1),
Or(xo123l == 0 , xo123l == 1),
Or(xo123r == 0 , xo123r == 1),
Or(xo123u == 0 , xo123u == 1),
Or(xo123d == 0 , xo123d == 1),
Or(xo124l == 0 , xo124l == 1),
Or(xo124r == 0 , xo124r == 1),
Or(xo124u == 0 , xo124u == 1),
Or(xo124d == 0 , xo124d == 1),
Or(xo125l == 0 , xo125l == 1),
Or(xo125r == 0 , xo125r == 1),
Or(xo125u == 0 , xo125u == 1),
Or(xo125d == 0 , xo125d == 1),
Or(xo126l == 0 , xo126l == 1),
Or(xo126r == 0 , xo126r == 1),
Or(xo126u == 0 , xo126u == 1),
Or(xo126d == 0 , xo126d == 1),
Or(xo127l == 0 , xo127l == 1),
Or(xo127r == 0 , xo127r == 1),
Or(xo127u == 0 , xo127u == 1),
Or(xo127d == 0 , xo127d == 1),
Or(xo128l == 0 , xo128l == 1),
Or(xo128r == 0 , xo128r == 1),
Or(xo128u == 0 , xo128u == 1),
Or(xo128d == 0 , xo128d == 1),
Or(xo129l == 0 , xo129l == 1),
Or(xo129r == 0 , xo129r == 1),
Or(xo129u == 0 , xo129u == 1),
Or(xo129d == 0 , xo129d == 1),
Or(xo130l == 0 , xo130l == 1),
Or(xo130r == 0 , xo130r == 1),
Or(xo130u == 0 , xo130u == 1),
Or(xo130d == 0 , xo130d == 1),
Or(xo131l == 0 , xo131l == 1),
Or(xo131r == 0 , xo131r == 1),
Or(xo131u == 0 , xo131u == 1),
Or(xo131d == 0 , xo131d == 1),
Or(xo132l == 0 , xo132l == 1),
Or(xo132r == 0 , xo132r == 1),
Or(xo132u == 0 , xo132u == 1),
Or(xo132d == 0 , xo132d == 1),
Or(xo133l == 0 , xo133l == 1),
Or(xo133r == 0 , xo133r == 1),
Or(xo133u == 0 , xo133u == 1),
Or(xo133d == 0 , xo133d == 1),
Or(xo134l == 0 , xo134l == 1),
Or(xo134r == 0 , xo134r == 1),
Or(xo134u == 0 , xo134u == 1),
Or(xo134d == 0 , xo134d == 1),
Or(xo135l == 0 , xo135l == 1),
Or(xo135r == 0 , xo135r == 1),
Or(xo135u == 0 , xo135u == 1),
Or(xo135d == 0 , xo135d == 1),
Or(xo136l == 0 , xo136l == 1),
Or(xo136r == 0 , xo136r == 1),
Or(xo136u == 0 , xo136u == 1),
Or(xo136d == 0 , xo136d == 1),
Or(xo137l == 0 , xo137l == 1),
Or(xo137r == 0 , xo137r == 1),
Or(xo137u == 0 , xo137u == 1),
Or(xo137d == 0 , xo137d == 1),
Or(xo138l == 0 , xo138l == 1),
Or(xo138r == 0 , xo138r == 1),
Or(xo138u == 0 , xo138u == 1),
Or(xo138d == 0 , xo138d == 1),
Or(xo139l == 0 , xo139l == 1),
Or(xo139r == 0 , xo139r == 1),
Or(xo139u == 0 , xo139u == 1),
Or(xo139d == 0 , xo139d == 1),
Or(xo140l == 0 , xo140l == 1),
Or(xo140r == 0 , xo140r == 1),
Or(xo140u == 0 , xo140u == 1),
Or(xo140d == 0 , xo140d == 1),
Or(xo141l == 0 , xo141l == 1),
Or(xo141r == 0 , xo141r == 1),
Or(xo141u == 0 , xo141u == 1),
Or(xo141d == 0 , xo141d == 1),
Or(xo142l == 0 , xo142l == 1),
Or(xo142r == 0 , xo142r == 1),
Or(xo142u == 0 , xo142u == 1),
Or(xo142d == 0 , xo142d == 1),
Or(xo143l == 0 , xo143l == 1),
Or(xo143r == 0 , xo143r == 1),
Or(xo143u == 0 , xo143u == 1),
Or(xo143d == 0 , xo143d == 1),
Or(xo144l == 0 , xo144l == 1),
Or(xo144r == 0 , xo144r == 1),
Or(xo144u == 0 , xo144u == 1),
Or(xo144d == 0 , xo144d == 1),
Or(xo145l == 0 , xo145l == 1),
Or(xo145r == 0 , xo145r == 1),
Or(xo145u == 0 , xo145u == 1),
Or(xo145d == 0 , xo145d == 1),
Or(xo146l == 0 , xo146l == 1),
Or(xo146r == 0 , xo146r == 1),
Or(xo146u == 0 , xo146u == 1),
Or(xo146d == 0 , xo146d == 1),
Or(xo147l == 0 , xo147l == 1),
Or(xo147r == 0 , xo147r == 1),
Or(xo147u == 0 , xo147u == 1),
Or(xo147d == 0 , xo147d == 1),
Or(xo148l == 0 , xo148l == 1),
Or(xo148r == 0 , xo148r == 1),
Or(xo148u == 0 , xo148u == 1),
Or(xo148d == 0 , xo148d == 1),
Or(xo149l == 0 , xo149l == 1),
Or(xo149r == 0 , xo149r == 1),
Or(xo149u == 0 , xo149u == 1),
Or(xo149d == 0 , xo149d == 1),
Or(xo150l == 0 , xo150l == 1),
Or(xo150r == 0 , xo150r == 1),
Or(xo150u == 0 , xo150u == 1),
Or(xo150d == 0 , xo150d == 1),
Or(xo151l == 0 , xo151l == 1),
Or(xo151r == 0 , xo151r == 1),
Or(xo151u == 0 , xo151u == 1),
Or(xo151d == 0 , xo151d == 1),
Or(xo152l == 0 , xo152l == 1),
Or(xo152r == 0 , xo152r == 1),
Or(xo152u == 0 , xo152u == 1),
Or(xo152d == 0 , xo152d == 1),
Or(xo153l == 0 , xo153l == 1),
Or(xo153r == 0 , xo153r == 1),
Or(xo153u == 0 , xo153u == 1),
Or(xo153d == 0 , xo153d == 1),
Or(xo154l == 0 , xo154l == 1),
Or(xo154r == 0 , xo154r == 1),
Or(xo154u == 0 , xo154u == 1),
Or(xo154d == 0 , xo154d == 1),
Or(xo155l == 0 , xo155l == 1),
Or(xo155r == 0 , xo155r == 1),
Or(xo155u == 0 , xo155u == 1),
Or(xo155d == 0 , xo155d == 1),
Or(xo156l == 0 , xo156l == 1),
Or(xo156r == 0 , xo156r == 1),
Or(xo156u == 0 , xo156u == 1),
Or(xo156d == 0 , xo156d == 1),
Or(xo157l == 0 , xo157l == 1),
Or(xo157r == 0 , xo157r == 1),
Or(xo157u == 0 , xo157u == 1),
Or(xo157d == 0 , xo157d == 1),
Or(xo158l == 0 , xo158l == 1),
Or(xo158r == 0 , xo158r == 1),
Or(xo158u == 0 , xo158u == 1),
Or(xo158d == 0 , xo158d == 1),
Or(xo159l == 0 , xo159l == 1),
Or(xo159r == 0 , xo159r == 1),
Or(xo159u == 0 , xo159u == 1),
Or(xo159d == 0 , xo159d == 1),
Or(xo160l == 0 , xo160l == 1),
Or(xo160r == 0 , xo160r == 1),
Or(xo160u == 0 , xo160u == 1),
Or(xo160d == 0 , xo160d == 1),
Or(xo161l == 0 , xo161l == 1),
Or(xo161r == 0 , xo161r == 1),
Or(xo161u == 0 , xo161u == 1),
Or(xo161d == 0 , xo161d == 1),
Or(xo162l == 0 , xo162l == 1),
Or(xo162r == 0 , xo162r == 1),
Or(xo162u == 0 , xo162u == 1),
Or(xo162d == 0 , xo162d == 1),
Or(xo163l == 0 , xo163l == 1),
Or(xo163r == 0 , xo163r == 1),
Or(xo163u == 0 , xo163u == 1),
Or(xo163d == 0 , xo163d == 1),
Or(xo164l == 0 , xo164l == 1),
Or(xo164r == 0 , xo164r == 1),
Or(xo164u == 0 , xo164u == 1),
Or(xo164d == 0 , xo164d == 1),
Or(xo165l == 0 , xo165l == 1),
Or(xo165r == 0 , xo165r == 1),
Or(xo165u == 0 , xo165u == 1),
Or(xo165d == 0 , xo165d == 1),
Or(xo166l == 0 , xo166l == 1),
Or(xo166r == 0 , xo166r == 1),
Or(xo166u == 0 , xo166u == 1),
Or(xo166d == 0 , xo166d == 1),
Or(xo167l == 0 , xo167l == 1),
Or(xo167r == 0 , xo167r == 1),
Or(xo167u == 0 , xo167u == 1),
Or(xo167d == 0 , xo167d == 1),
Or(xo168l == 0 , xo168l == 1),
Or(xo168r == 0 , xo168r == 1),
Or(xo168u == 0 , xo168u == 1),
Or(xo168d == 0 , xo168d == 1),
Or(xo169l == 0 , xo169l == 1),
Or(xo169r == 0 , xo169r == 1),
Or(xo169u == 0 , xo169u == 1),
Or(xo169d == 0 , xo169d == 1),
Or(xo170l == 0 , xo170l == 1),
Or(xo170r == 0 , xo170r == 1),
Or(xo170u == 0 , xo170u == 1),
Or(xo170d == 0 , xo170d == 1),
Or(xo171l == 0 , xo171l == 1),
Or(xo171r == 0 , xo171r == 1),
Or(xo171u == 0 , xo171u == 1),
Or(xo171d == 0 , xo171d == 1),
Or(xo172l == 0 , xo172l == 1),
Or(xo172r == 0 , xo172r == 1),
Or(xo172u == 0 , xo172u == 1),
Or(xo172d == 0 , xo172d == 1),
Or(xo173l == 0 , xo173l == 1),
Or(xo173r == 0 , xo173r == 1),
Or(xo173u == 0 , xo173u == 1),
Or(xo173d == 0 , xo173d == 1),
Or(xo174l == 0 , xo174l == 1),
Or(xo174r == 0 , xo174r == 1),
Or(xo174u == 0 , xo174u == 1),
Or(xo174d == 0 , xo174d == 1),
Or(xo175l == 0 , xo175l == 1),
Or(xo175r == 0 , xo175r == 1),
Or(xo175u == 0 , xo175u == 1),
Or(xo175d == 0 , xo175d == 1),
Or(xo176l == 0 , xo176l == 1),
Or(xo176r == 0 , xo176r == 1),
Or(xo176u == 0 , xo176u == 1),
Or(xo176d == 0 , xo176d == 1),
Or(xo177l == 0 , xo177l == 1),
Or(xo177r == 0 , xo177r == 1),
Or(xo177u == 0 , xo177u == 1),
Or(xo177d == 0 , xo177d == 1),
Or(xo178l == 0 , xo178l == 1),
Or(xo178r == 0 , xo178r == 1),
Or(xo178u == 0 , xo178u == 1),
Or(xo178d == 0 , xo178d == 1),
Or(xo179l == 0 , xo179l == 1),
Or(xo179r == 0 , xo179r == 1),
Or(xo179u == 0 , xo179u == 1),
Or(xo179d == 0 , xo179d == 1),
Or(xo180l == 0 , xo180l == 1),
Or(xo180r == 0 , xo180r == 1),
Or(xo180u == 0 , xo180u == 1),
Or(xo180d == 0 , xo180d == 1),
Or(xo181l == 0 , xo181l == 1),
Or(xo181r == 0 , xo181r == 1),
Or(xo181u == 0 , xo181u == 1),
Or(xo181d == 0 , xo181d == 1),
Or(xo182l == 0 , xo182l == 1),
Or(xo182r == 0 , xo182r == 1),
Or(xo182u == 0 , xo182u == 1),
Or(xo182d == 0 , xo182d == 1),
Or(xo183l == 0 , xo183l == 1),
Or(xo183r == 0 , xo183r == 1),
Or(xo183u == 0 , xo183u == 1),
Or(xo183d == 0 , xo183d == 1),
Or(xo184l == 0 , xo184l == 1),
Or(xo184r == 0 , xo184r == 1),
Or(xo184u == 0 , xo184u == 1),
Or(xo184d == 0 , xo184d == 1),
Or(xo185l == 0 , xo185l == 1),
Or(xo185r == 0 , xo185r == 1),
Or(xo185u == 0 , xo185u == 1),
Or(xo185d == 0 , xo185d == 1),
Or(xo186l == 0 , xo186l == 1),
Or(xo186r == 0 , xo186r == 1),
Or(xo186u == 0 , xo186u == 1),
Or(xo186d == 0 , xo186d == 1),
Or(xo187l == 0 , xo187l == 1),
Or(xo187r == 0 , xo187r == 1),
Or(xo187u == 0 , xo187u == 1),
Or(xo187d == 0 , xo187d == 1),
Or(xo188l == 0 , xo188l == 1),
Or(xo188r == 0 , xo188r == 1),
Or(xo188u == 0 , xo188u == 1),
Or(xo188d == 0 , xo188d == 1),
Or(xo189l == 0 , xo189l == 1),
Or(xo189r == 0 , xo189r == 1),
Or(xo189u == 0 , xo189u == 1),
Or(xo189d == 0 , xo189d == 1),
Or(xo190l == 0 , xo190l == 1),
Or(xo190r == 0 , xo190r == 1),
Or(xo190u == 0 , xo190u == 1),
Or(xo190d == 0 , xo190d == 1),
Or(xo191l == 0 , xo191l == 1),
Or(xo191r == 0 , xo191r == 1),
Or(xo191u == 0 , xo191u == 1),
Or(xo191d == 0 , xo191d == 1),
Or(xo192l == 0 , xo192l == 1),
Or(xo192r == 0 , xo192r == 1),
Or(xo192u == 0 , xo192u == 1),
Or(xo192d == 0 , xo192d == 1),
Or(xo193l == 0 , xo193l == 1),
Or(xo193r == 0 , xo193r == 1),
Or(xo193u == 0 , xo193u == 1),
Or(xo193d == 0 , xo193d == 1),
Or(xo194l == 0 , xo194l == 1),
Or(xo194r == 0 , xo194r == 1),
Or(xo194u == 0 , xo194u == 1),
Or(xo194d == 0 , xo194d == 1),
Or(xo195l == 0 , xo195l == 1),
Or(xo195r == 0 , xo195r == 1),
Or(xo195u == 0 , xo195u == 1),
Or(xo195d == 0 , xo195d == 1),
Or(xo196l == 0 , xo196l == 1),
Or(xo196r == 0 , xo196r == 1),
Or(xo196u == 0 , xo196u == 1),
Or(xo196d == 0 , xo196d == 1),
Or(xo197l == 0 , xo197l == 1),
Or(xo197r == 0 , xo197r == 1),
Or(xo197u == 0 , xo197u == 1),
Or(xo197d == 0 , xo197d == 1),
Or(xo198l == 0 , xo198l == 1),
Or(xo198r == 0 , xo198r == 1),
Or(xo198u == 0 , xo198u == 1),
Or(xo198d == 0 , xo198d == 1),
Or(xo199l == 0 , xo199l == 1),
Or(xo199r == 0 , xo199r == 1),
Or(xo199u == 0 , xo199u == 1),
Or(xo199d == 0 , xo199d == 1),
Or(xo200l == 0 , xo200l == 1),
Or(xo200r == 0 , xo200r == 1),
Or(xo200u == 0 , xo200u == 1),
Or(xo200d == 0 , xo200d == 1),
Or(xo201l == 0 , xo201l == 1),
Or(xo201r == 0 , xo201r == 1),
Or(xo201u == 0 , xo201u == 1),
Or(xo201d == 0 , xo201d == 1),
Or(xo202l == 0 , xo202l == 1),
Or(xo202r == 0 , xo202r == 1),
Or(xo202u == 0 , xo202u == 1),
Or(xo202d == 0 , xo202d == 1),
Or(xo203l == 0 , xo203l == 1),
Or(xo203r == 0 , xo203r == 1),
Or(xo203u == 0 , xo203u == 1),
Or(xo203d == 0 , xo203d == 1),
Or(xo204l == 0 , xo204l == 1),
Or(xo204r == 0 , xo204r == 1),
Or(xo204u == 0 , xo204u == 1),
Or(xo204d == 0 , xo204d == 1),
Or(xo205l == 0 , xo205l == 1),
Or(xo205r == 0 , xo205r == 1),
Or(xo205u == 0 , xo205u == 1),
Or(xo205d == 0 , xo205d == 1),
Or(xo206l == 0 , xo206l == 1),
Or(xo206r == 0 , xo206r == 1),
Or(xo206u == 0 , xo206u == 1),
Or(xo206d == 0 , xo206d == 1),
Or(xo207l == 0 , xo207l == 1),
Or(xo207r == 0 , xo207r == 1),
Or(xo207u == 0 , xo207u == 1),
Or(xo207d == 0 , xo207d == 1),
Or(xo208l == 0 , xo208l == 1),
Or(xo208r == 0 , xo208r == 1),
Or(xo208u == 0 , xo208u == 1),
Or(xo208d == 0 , xo208d == 1),
Or(xo209l == 0 , xo209l == 1),
Or(xo209r == 0 , xo209r == 1),
Or(xo209u == 0 , xo209u == 1),
Or(xo209d == 0 , xo209d == 1),
Or(xo210l == 0 , xo210l == 1),
Or(xo210r == 0 , xo210r == 1),
Or(xo210u == 0 , xo210u == 1),
Or(xo210d == 0 , xo210d == 1),
Or(xo211l == 0 , xo211l == 1),
Or(xo211r == 0 , xo211r == 1),
Or(xo211u == 0 , xo211u == 1),
Or(xo211d == 0 , xo211d == 1),
Or(xo212l == 0 , xo212l == 1),
Or(xo212r == 0 , xo212r == 1),
Or(xo212u == 0 , xo212u == 1),
Or(xo212d == 0 , xo212d == 1),
Or(xo213l == 0 , xo213l == 1),
Or(xo213r == 0 , xo213r == 1),
Or(xo213u == 0 , xo213u == 1),
Or(xo213d == 0 , xo213d == 1),
Or(xo214l == 0 , xo214l == 1),
Or(xo214r == 0 , xo214r == 1),
Or(xo214u == 0 , xo214u == 1),
Or(xo214d == 0 , xo214d == 1),
Or(xo215l == 0 , xo215l == 1),
Or(xo215r == 0 , xo215r == 1),
Or(xo215u == 0 , xo215u == 1),
Or(xo215d == 0 , xo215d == 1),
Or(xo216l == 0 , xo216l == 1),
Or(xo216r == 0 , xo216r == 1),
Or(xo216u == 0 , xo216u == 1),
Or(xo216d == 0 , xo216d == 1),
Or(xo217l == 0 , xo217l == 1),
Or(xo217r == 0 , xo217r == 1),
Or(xo217u == 0 , xo217u == 1),
Or(xo217d == 0 , xo217d == 1),
Or(xo218l == 0 , xo218l == 1),
Or(xo218r == 0 , xo218r == 1),
Or(xo218u == 0 , xo218u == 1),
Or(xo218d == 0 , xo218d == 1),
Or(xo219l == 0 , xo219l == 1),
Or(xo219r == 0 , xo219r == 1),
Or(xo219u == 0 , xo219u == 1),
Or(xo219d == 0 , xo219d == 1),
Or(xo220l == 0 , xo220l == 1),
Or(xo220r == 0 , xo220r == 1),
Or(xo220u == 0 , xo220u == 1),
Or(xo220d == 0 , xo220d == 1),
Or(xo221l == 0 , xo221l == 1),
Or(xo221r == 0 , xo221r == 1),
Or(xo221u == 0 , xo221u == 1),
Or(xo221d == 0 , xo221d == 1),
Or(xo222l == 0 , xo222l == 1),
Or(xo222r == 0 , xo222r == 1),
Or(xo222u == 0 , xo222u == 1),
Or(xo222d == 0 , xo222d == 1),
Or(xo223l == 0 , xo223l == 1),
Or(xo223r == 0 , xo223r == 1),
Or(xo223u == 0 , xo223u == 1),
Or(xo223d == 0 , xo223d == 1),
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
Or (y195 == 0 , y195 == 1 ),
Or (y196 == 0 , y196 == 1 ),
Or (y197 == 0 , y197 == 1 ),
Or (y198 == 0 , y198 == 1 ),
Or (y199 == 0 , y199 == 1 ),
Or (y200 == 0 , y200 == 1 ),
Or (y201 == 0 , y201 == 1 ),
Or (y202 == 0 , y202 == 1 ),
Or (y203 == 0 , y203 == 1 ),
Or (y204 == 0 , y204 == 1 ),
Or (y205 == 0 , y205 == 1 ),
Or (y206 == 0 , y206 == 1 ),
Or (y207 == 0 , y207 == 1 ),
Or (y208 == 0 , y208 == 1 ),
Or (y209 == 0 , y209 == 1 ),
Or (y210 == 0 , y210 == 1 ),
Or (y211 == 0 , y211 == 1 ),
Or (y212 == 0 , y212 == 1 ),
Or (y213 == 0 , y213 == 1 ),
Or (y214 == 0 , y214 == 1 ),
Or (y215 == 0 , y215 == 1 ),
Or (y216 == 0 , y216 == 1 ),
Or (y217 == 0 , y217 == 1 ),
Or (y218 == 0 , y218 == 1 ),
Or (y219 == 0 , y219 == 1 ),
Or (y220 == 0 , y220 == 1 ),
Or (y221 == 0 , y221 == 1 ),
Or (y222 == 0 , y222 == 1 ),
Or (y223 == 0 , y223 == 1 ),
y0 + y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10 + y11 + y12 + y13 + y14 + y15 + y16 + y17 + y18 + y19 + y20 + y21 + y22 + y23 + y24 + y25 + y26 + y27 + y28 + y29 + y30 + y31 + y32 + y33 + y34 + y35 + y36 + y37 + y38 + y39 + y40 + y41 + y42 + y43 + y44 + y45 + y46 + y47 + y48 + y49 + y50 + y51 + y52 + y53 + y54 + y55 + y56 + y57 + y58 + y59 + y60 + y61 + y62 + y63 + y64 + y65 + y66 + y67 + y68 + y69 + y70 + y71 + y72 + y73 + y74 + y75 + y76 + y77 + y78 + y79 + y80 + y81 + y82 + y83 + y84 + y85 + y86 + y87 + y88 + y89 + y90 + y91 + y92 + y93 + y94 + y95 + y96 + y97 + y98 + y99 + y100 + y101 + y102 + y103 + y104 + y105 + y106 + y107 + y108 + y109 + y110 + y111 + y112 + y113 + y114 + y115 + y116 + y117 + y118 + y119 + y120 + y121 + y122 + y123 + y124 + y125 + y126 + y127 + y128 + y129 + y130 + y131 + y132 + y133 + y134 + y135 + y136 + y137 + y138 + y139 + y140 + y141 + y142 + y143 + y144 + y145 + y146 + y147 + y148 + y149 + y150 + y151 + y152 + y153 + y154 + y155 + y156 + y157 + y158 + y159 + y160 + y161 + y162 + y163 + y164 + y165 + y166 + y167 + y168 + y169 + y170 + y171 + y172 + y173 + y174 + y175 + y176 + y177 + y178 + y179 + y180 + y181 + y182 + y183 + y184 + y185 + y186 + y187 + y188 + y189 + y190 + y191 + y192 + y193 + y194 + y195 + y196 + y197 + y198 + y199 + y200 + y201 + y202 + y203 + y204 + y205 + y206 + y207 + y208 + y209 + y210 + y211 + y212 + y213 + y214 + y215 + y216 + y217 + y218 + y219 + y220 + y221 + y222 + y223 == 14
)
if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')