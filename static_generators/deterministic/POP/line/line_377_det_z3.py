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
pi225 = Real('pi225')
pi226 = Real('pi226')
pi227 = Real('pi227')
pi228 = Real('pi228')
pi229 = Real('pi229')
pi230 = Real('pi230')
pi231 = Real('pi231')
pi232 = Real('pi232')
pi233 = Real('pi233')
pi234 = Real('pi234')
pi235 = Real('pi235')
pi236 = Real('pi236')
pi237 = Real('pi237')
pi238 = Real('pi238')
pi239 = Real('pi239')
pi240 = Real('pi240')
pi241 = Real('pi241')
pi242 = Real('pi242')
pi243 = Real('pi243')
pi244 = Real('pi244')
pi245 = Real('pi245')
pi246 = Real('pi246')
pi247 = Real('pi247')
pi248 = Real('pi248')
pi249 = Real('pi249')
pi250 = Real('pi250')
pi251 = Real('pi251')
pi252 = Real('pi252')
pi253 = Real('pi253')
pi254 = Real('pi254')
pi255 = Real('pi255')
pi256 = Real('pi256')
pi257 = Real('pi257')
pi258 = Real('pi258')
pi259 = Real('pi259')
pi260 = Real('pi260')
pi261 = Real('pi261')
pi262 = Real('pi262')
pi263 = Real('pi263')
pi264 = Real('pi264')
pi265 = Real('pi265')
pi266 = Real('pi266')
pi267 = Real('pi267')
pi268 = Real('pi268')
pi269 = Real('pi269')
pi270 = Real('pi270')
pi271 = Real('pi271')
pi272 = Real('pi272')
pi273 = Real('pi273')
pi274 = Real('pi274')
pi275 = Real('pi275')
pi276 = Real('pi276')
pi277 = Real('pi277')
pi278 = Real('pi278')
pi279 = Real('pi279')
pi280 = Real('pi280')
pi281 = Real('pi281')
pi282 = Real('pi282')
pi283 = Real('pi283')
pi284 = Real('pi284')
pi285 = Real('pi285')
pi286 = Real('pi286')
pi287 = Real('pi287')
pi288 = Real('pi288')
pi289 = Real('pi289')
pi290 = Real('pi290')
pi291 = Real('pi291')
pi292 = Real('pi292')
pi293 = Real('pi293')
pi294 = Real('pi294')
pi295 = Real('pi295')
pi296 = Real('pi296')
pi297 = Real('pi297')
pi298 = Real('pi298')
pi299 = Real('pi299')
pi300 = Real('pi300')
pi301 = Real('pi301')
pi302 = Real('pi302')
pi303 = Real('pi303')
pi304 = Real('pi304')
pi305 = Real('pi305')
pi306 = Real('pi306')
pi307 = Real('pi307')
pi308 = Real('pi308')
pi309 = Real('pi309')
pi310 = Real('pi310')
pi311 = Real('pi311')
pi312 = Real('pi312')
pi313 = Real('pi313')
pi314 = Real('pi314')
pi315 = Real('pi315')
pi316 = Real('pi316')
pi317 = Real('pi317')
pi318 = Real('pi318')
pi319 = Real('pi319')
pi320 = Real('pi320')
pi321 = Real('pi321')
pi322 = Real('pi322')
pi323 = Real('pi323')
pi324 = Real('pi324')
pi325 = Real('pi325')
pi326 = Real('pi326')
pi327 = Real('pi327')
pi328 = Real('pi328')
pi329 = Real('pi329')
pi330 = Real('pi330')
pi331 = Real('pi331')
pi332 = Real('pi332')
pi333 = Real('pi333')
pi334 = Real('pi334')
pi335 = Real('pi335')
pi336 = Real('pi336')
pi337 = Real('pi337')
pi338 = Real('pi338')
pi339 = Real('pi339')
pi340 = Real('pi340')
pi341 = Real('pi341')
pi342 = Real('pi342')
pi343 = Real('pi343')
pi344 = Real('pi344')
pi345 = Real('pi345')
pi346 = Real('pi346')
pi347 = Real('pi347')
pi348 = Real('pi348')
pi349 = Real('pi349')
pi350 = Real('pi350')
pi351 = Real('pi351')
pi352 = Real('pi352')
pi353 = Real('pi353')
pi354 = Real('pi354')
pi355 = Real('pi355')
pi356 = Real('pi356')
pi357 = Real('pi357')
pi358 = Real('pi358')
pi359 = Real('pi359')
pi360 = Real('pi360')
pi361 = Real('pi361')
pi362 = Real('pi362')
pi363 = Real('pi363')
pi364 = Real('pi364')
pi365 = Real('pi365')
pi366 = Real('pi366')
pi367 = Real('pi367')
pi368 = Real('pi368')
pi369 = Real('pi369')
pi370 = Real('pi370')
pi371 = Real('pi371')
pi372 = Real('pi372')
pi373 = Real('pi373')
pi374 = Real('pi374')
pi375 = Real('pi375')
pi376 = Real('pi376')

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
ys81 = Real('ys81')
ys82 = Real('ys82')
ys91 = Real('ys91')
ys92 = Real('ys92')
ys101 = Real('ys101')
ys102 = Real('ys102')
ys111 = Real('ys111')
ys112 = Real('ys112')
ys121 = Real('ys121')
ys122 = Real('ys122')
ys131 = Real('ys131')
ys132 = Real('ys132')
ys141 = Real('ys141')
ys142 = Real('ys142')
ys151 = Real('ys151')
ys152 = Real('ys152')
ys161 = Real('ys161')
ys162 = Real('ys162')
ys171 = Real('ys171')
ys172 = Real('ys172')
ys181 = Real('ys181')
ys182 = Real('ys182')
ys191 = Real('ys191')
ys192 = Real('ys192')
ys201 = Real('ys201')
ys202 = Real('ys202')
ys211 = Real('ys211')
ys212 = Real('ys212')
ys221 = Real('ys221')
ys222 = Real('ys222')
ys231 = Real('ys231')
ys232 = Real('ys232')
ys241 = Real('ys241')
ys242 = Real('ys242')
ys251 = Real('ys251')
ys252 = Real('ys252')
ys261 = Real('ys261')
ys262 = Real('ys262')
ys271 = Real('ys271')
ys272 = Real('ys272')
ys281 = Real('ys281')
ys282 = Real('ys282')
ys291 = Real('ys291')
ys292 = Real('ys292')
ys301 = Real('ys301')
ys302 = Real('ys302')
ys311 = Real('ys311')
ys312 = Real('ys312')
ys321 = Real('ys321')
ys322 = Real('ys322')
ys331 = Real('ys331')
ys332 = Real('ys332')
ys341 = Real('ys341')
ys342 = Real('ys342')
ys351 = Real('ys351')
ys352 = Real('ys352')
ys361 = Real('ys361')
ys362 = Real('ys362')
ys371 = Real('ys371')
ys372 = Real('ys372')
ys381 = Real('ys381')
ys382 = Real('ys382')
ys391 = Real('ys391')
ys392 = Real('ys392')
ys401 = Real('ys401')
ys402 = Real('ys402')
ys411 = Real('ys411')
ys412 = Real('ys412')
ys421 = Real('ys421')
ys422 = Real('ys422')
ys431 = Real('ys431')
ys432 = Real('ys432')
ys441 = Real('ys441')
ys442 = Real('ys442')
ys451 = Real('ys451')
ys452 = Real('ys452')
ys461 = Real('ys461')
ys462 = Real('ys462')
ys471 = Real('ys471')
ys472 = Real('ys472')
ys481 = Real('ys481')
ys482 = Real('ys482')
ys491 = Real('ys491')
ys492 = Real('ys492')
ys501 = Real('ys501')
ys502 = Real('ys502')
ys511 = Real('ys511')
ys512 = Real('ys512')
ys521 = Real('ys521')
ys522 = Real('ys522')
ys531 = Real('ys531')
ys532 = Real('ys532')
ys541 = Real('ys541')
ys542 = Real('ys542')
ys551 = Real('ys551')
ys552 = Real('ys552')
ys561 = Real('ys561')
ys562 = Real('ys562')
ys571 = Real('ys571')
ys572 = Real('ys572')
ys581 = Real('ys581')
ys582 = Real('ys582')
ys591 = Real('ys591')
ys592 = Real('ys592')
ys601 = Real('ys601')
ys602 = Real('ys602')
ys611 = Real('ys611')
ys612 = Real('ys612')
ys621 = Real('ys621')
ys622 = Real('ys622')
ys631 = Real('ys631')
ys632 = Real('ys632')
ys641 = Real('ys641')
ys642 = Real('ys642')
ys651 = Real('ys651')
ys652 = Real('ys652')
ys661 = Real('ys661')
ys662 = Real('ys662')
ys671 = Real('ys671')
ys672 = Real('ys672')
ys681 = Real('ys681')
ys682 = Real('ys682')
ys691 = Real('ys691')
ys692 = Real('ys692')
ys701 = Real('ys701')
ys702 = Real('ys702')
ys711 = Real('ys711')
ys712 = Real('ys712')
ys721 = Real('ys721')
ys722 = Real('ys722')
ys731 = Real('ys731')
ys732 = Real('ys732')
ys741 = Real('ys741')
ys742 = Real('ys742')
ys751 = Real('ys751')
ys752 = Real('ys752')
ys761 = Real('ys761')
ys762 = Real('ys762')
ys771 = Real('ys771')
ys772 = Real('ys772')
ys781 = Real('ys781')
ys782 = Real('ys782')
ys791 = Real('ys791')
ys792 = Real('ys792')
ys801 = Real('ys801')
ys802 = Real('ys802')
ys811 = Real('ys811')
ys812 = Real('ys812')
ys821 = Real('ys821')
ys822 = Real('ys822')
ys831 = Real('ys831')
ys832 = Real('ys832')
ys841 = Real('ys841')
ys842 = Real('ys842')
ys851 = Real('ys851')
ys852 = Real('ys852')
ys861 = Real('ys861')
ys862 = Real('ys862')
ys871 = Real('ys871')
ys872 = Real('ys872')
ys881 = Real('ys881')
ys882 = Real('ys882')
ys891 = Real('ys891')
ys892 = Real('ys892')
ys901 = Real('ys901')
ys902 = Real('ys902')
ys911 = Real('ys911')
ys912 = Real('ys912')
ys921 = Real('ys921')
ys922 = Real('ys922')
ys931 = Real('ys931')
ys932 = Real('ys932')
ys941 = Real('ys941')
ys942 = Real('ys942')
ys951 = Real('ys951')
ys952 = Real('ys952')
ys961 = Real('ys961')
ys962 = Real('ys962')
ys971 = Real('ys971')
ys972 = Real('ys972')
ys981 = Real('ys981')
ys982 = Real('ys982')
ys991 = Real('ys991')
ys992 = Real('ys992')
ys1001 = Real('ys1001')
ys1002 = Real('ys1002')
ys1011 = Real('ys1011')
ys1012 = Real('ys1012')
ys1021 = Real('ys1021')
ys1022 = Real('ys1022')
ys1031 = Real('ys1031')
ys1032 = Real('ys1032')
ys1041 = Real('ys1041')
ys1042 = Real('ys1042')
ys1051 = Real('ys1051')
ys1052 = Real('ys1052')
ys1061 = Real('ys1061')
ys1062 = Real('ys1062')
ys1071 = Real('ys1071')
ys1072 = Real('ys1072')
ys1081 = Real('ys1081')
ys1082 = Real('ys1082')
ys1091 = Real('ys1091')
ys1092 = Real('ys1092')
ys1101 = Real('ys1101')
ys1102 = Real('ys1102')
ys1111 = Real('ys1111')
ys1112 = Real('ys1112')
ys1121 = Real('ys1121')
ys1122 = Real('ys1122')
ys1131 = Real('ys1131')
ys1132 = Real('ys1132')
ys1141 = Real('ys1141')
ys1142 = Real('ys1142')
ys1151 = Real('ys1151')
ys1152 = Real('ys1152')
ys1161 = Real('ys1161')
ys1162 = Real('ys1162')
ys1171 = Real('ys1171')
ys1172 = Real('ys1172')
ys1181 = Real('ys1181')
ys1182 = Real('ys1182')
ys1191 = Real('ys1191')
ys1192 = Real('ys1192')
ys1201 = Real('ys1201')
ys1202 = Real('ys1202')
ys1211 = Real('ys1211')
ys1212 = Real('ys1212')
ys1221 = Real('ys1221')
ys1222 = Real('ys1222')
ys1231 = Real('ys1231')
ys1232 = Real('ys1232')
ys1241 = Real('ys1241')
ys1242 = Real('ys1242')
ys1251 = Real('ys1251')
ys1252 = Real('ys1252')
ys1261 = Real('ys1261')
ys1262 = Real('ys1262')
ys1271 = Real('ys1271')
ys1272 = Real('ys1272')
ys1281 = Real('ys1281')
ys1282 = Real('ys1282')
ys1291 = Real('ys1291')
ys1292 = Real('ys1292')
ys1301 = Real('ys1301')
ys1302 = Real('ys1302')
ys1311 = Real('ys1311')
ys1312 = Real('ys1312')
ys1321 = Real('ys1321')
ys1322 = Real('ys1322')
ys1331 = Real('ys1331')
ys1332 = Real('ys1332')
ys1341 = Real('ys1341')
ys1342 = Real('ys1342')
ys1351 = Real('ys1351')
ys1352 = Real('ys1352')
ys1361 = Real('ys1361')
ys1362 = Real('ys1362')
ys1371 = Real('ys1371')
ys1372 = Real('ys1372')
ys1381 = Real('ys1381')
ys1382 = Real('ys1382')
ys1391 = Real('ys1391')
ys1392 = Real('ys1392')
ys1401 = Real('ys1401')
ys1402 = Real('ys1402')
ys1411 = Real('ys1411')
ys1412 = Real('ys1412')
ys1421 = Real('ys1421')
ys1422 = Real('ys1422')
ys1431 = Real('ys1431')
ys1432 = Real('ys1432')
ys1441 = Real('ys1441')
ys1442 = Real('ys1442')
ys1451 = Real('ys1451')
ys1452 = Real('ys1452')
ys1461 = Real('ys1461')
ys1462 = Real('ys1462')
ys1471 = Real('ys1471')
ys1472 = Real('ys1472')
ys1481 = Real('ys1481')
ys1482 = Real('ys1482')
ys1491 = Real('ys1491')
ys1492 = Real('ys1492')
ys1501 = Real('ys1501')
ys1502 = Real('ys1502')
ys1511 = Real('ys1511')
ys1512 = Real('ys1512')
ys1521 = Real('ys1521')
ys1522 = Real('ys1522')
ys1531 = Real('ys1531')
ys1532 = Real('ys1532')
ys1541 = Real('ys1541')
ys1542 = Real('ys1542')
ys1551 = Real('ys1551')
ys1552 = Real('ys1552')
ys1561 = Real('ys1561')
ys1562 = Real('ys1562')
ys1571 = Real('ys1571')
ys1572 = Real('ys1572')
ys1581 = Real('ys1581')
ys1582 = Real('ys1582')
ys1591 = Real('ys1591')
ys1592 = Real('ys1592')
ys1601 = Real('ys1601')
ys1602 = Real('ys1602')
ys1611 = Real('ys1611')
ys1612 = Real('ys1612')
ys1621 = Real('ys1621')
ys1622 = Real('ys1622')
ys1631 = Real('ys1631')
ys1632 = Real('ys1632')
ys1641 = Real('ys1641')
ys1642 = Real('ys1642')
ys1651 = Real('ys1651')
ys1652 = Real('ys1652')
ys1661 = Real('ys1661')
ys1662 = Real('ys1662')
ys1671 = Real('ys1671')
ys1672 = Real('ys1672')
ys1681 = Real('ys1681')
ys1682 = Real('ys1682')
ys1691 = Real('ys1691')
ys1692 = Real('ys1692')
ys1701 = Real('ys1701')
ys1702 = Real('ys1702')
ys1711 = Real('ys1711')
ys1712 = Real('ys1712')
ys1721 = Real('ys1721')
ys1722 = Real('ys1722')
ys1731 = Real('ys1731')
ys1732 = Real('ys1732')
ys1741 = Real('ys1741')
ys1742 = Real('ys1742')
ys1751 = Real('ys1751')
ys1752 = Real('ys1752')
ys1761 = Real('ys1761')
ys1762 = Real('ys1762')
ys1771 = Real('ys1771')
ys1772 = Real('ys1772')
ys1781 = Real('ys1781')
ys1782 = Real('ys1782')
ys1791 = Real('ys1791')
ys1792 = Real('ys1792')
ys1801 = Real('ys1801')
ys1802 = Real('ys1802')
ys1811 = Real('ys1811')
ys1812 = Real('ys1812')
ys1821 = Real('ys1821')
ys1822 = Real('ys1822')
ys1831 = Real('ys1831')
ys1832 = Real('ys1832')
ys1841 = Real('ys1841')
ys1842 = Real('ys1842')
ys1851 = Real('ys1851')
ys1852 = Real('ys1852')
ys1861 = Real('ys1861')
ys1862 = Real('ys1862')
ys1871 = Real('ys1871')
ys1872 = Real('ys1872')
ys1891 = Real('ys1891')
ys1892 = Real('ys1892')
ys1901 = Real('ys1901')
ys1902 = Real('ys1902')
ys1911 = Real('ys1911')
ys1912 = Real('ys1912')
ys1921 = Real('ys1921')
ys1922 = Real('ys1922')
ys1931 = Real('ys1931')
ys1932 = Real('ys1932')
ys1941 = Real('ys1941')
ys1942 = Real('ys1942')
ys1951 = Real('ys1951')
ys1952 = Real('ys1952')
ys1961 = Real('ys1961')
ys1962 = Real('ys1962')
ys1971 = Real('ys1971')
ys1972 = Real('ys1972')
ys1981 = Real('ys1981')
ys1982 = Real('ys1982')
ys1991 = Real('ys1991')
ys1992 = Real('ys1992')
ys2001 = Real('ys2001')
ys2002 = Real('ys2002')
ys2011 = Real('ys2011')
ys2012 = Real('ys2012')
ys2021 = Real('ys2021')
ys2022 = Real('ys2022')
ys2031 = Real('ys2031')
ys2032 = Real('ys2032')
ys2041 = Real('ys2041')
ys2042 = Real('ys2042')
ys2051 = Real('ys2051')
ys2052 = Real('ys2052')
ys2061 = Real('ys2061')
ys2062 = Real('ys2062')
ys2071 = Real('ys2071')
ys2072 = Real('ys2072')
ys2081 = Real('ys2081')
ys2082 = Real('ys2082')
ys2091 = Real('ys2091')
ys2092 = Real('ys2092')
ys2101 = Real('ys2101')
ys2102 = Real('ys2102')
ys2111 = Real('ys2111')
ys2112 = Real('ys2112')
ys2121 = Real('ys2121')
ys2122 = Real('ys2122')
ys2131 = Real('ys2131')
ys2132 = Real('ys2132')
ys2141 = Real('ys2141')
ys2142 = Real('ys2142')
ys2151 = Real('ys2151')
ys2152 = Real('ys2152')
ys2161 = Real('ys2161')
ys2162 = Real('ys2162')
ys2171 = Real('ys2171')
ys2172 = Real('ys2172')
ys2181 = Real('ys2181')
ys2182 = Real('ys2182')
ys2191 = Real('ys2191')
ys2192 = Real('ys2192')
ys2201 = Real('ys2201')
ys2202 = Real('ys2202')
ys2211 = Real('ys2211')
ys2212 = Real('ys2212')
ys2221 = Real('ys2221')
ys2222 = Real('ys2222')
ys2231 = Real('ys2231')
ys2232 = Real('ys2232')
ys2241 = Real('ys2241')
ys2242 = Real('ys2242')
ys2251 = Real('ys2251')
ys2252 = Real('ys2252')
ys2261 = Real('ys2261')
ys2262 = Real('ys2262')
ys2271 = Real('ys2271')
ys2272 = Real('ys2272')
ys2281 = Real('ys2281')
ys2282 = Real('ys2282')
ys2291 = Real('ys2291')
ys2292 = Real('ys2292')
ys2301 = Real('ys2301')
ys2302 = Real('ys2302')
ys2311 = Real('ys2311')
ys2312 = Real('ys2312')
ys2321 = Real('ys2321')
ys2322 = Real('ys2322')
ys2331 = Real('ys2331')
ys2332 = Real('ys2332')
ys2341 = Real('ys2341')
ys2342 = Real('ys2342')
ys2351 = Real('ys2351')
ys2352 = Real('ys2352')
ys2361 = Real('ys2361')
ys2362 = Real('ys2362')
ys2371 = Real('ys2371')
ys2372 = Real('ys2372')
ys2381 = Real('ys2381')
ys2382 = Real('ys2382')
ys2391 = Real('ys2391')
ys2392 = Real('ys2392')
ys2401 = Real('ys2401')
ys2402 = Real('ys2402')
ys2411 = Real('ys2411')
ys2412 = Real('ys2412')
ys2421 = Real('ys2421')
ys2422 = Real('ys2422')
ys2431 = Real('ys2431')
ys2432 = Real('ys2432')
ys2441 = Real('ys2441')
ys2442 = Real('ys2442')
ys2451 = Real('ys2451')
ys2452 = Real('ys2452')
ys2461 = Real('ys2461')
ys2462 = Real('ys2462')
ys2471 = Real('ys2471')
ys2472 = Real('ys2472')
ys2481 = Real('ys2481')
ys2482 = Real('ys2482')
ys2491 = Real('ys2491')
ys2492 = Real('ys2492')
ys2501 = Real('ys2501')
ys2502 = Real('ys2502')
ys2511 = Real('ys2511')
ys2512 = Real('ys2512')
ys2521 = Real('ys2521')
ys2522 = Real('ys2522')
ys2531 = Real('ys2531')
ys2532 = Real('ys2532')
ys2541 = Real('ys2541')
ys2542 = Real('ys2542')
ys2551 = Real('ys2551')
ys2552 = Real('ys2552')
ys2561 = Real('ys2561')
ys2562 = Real('ys2562')
ys2571 = Real('ys2571')
ys2572 = Real('ys2572')
ys2581 = Real('ys2581')
ys2582 = Real('ys2582')
ys2591 = Real('ys2591')
ys2592 = Real('ys2592')
ys2601 = Real('ys2601')
ys2602 = Real('ys2602')
ys2611 = Real('ys2611')
ys2612 = Real('ys2612')
ys2621 = Real('ys2621')
ys2622 = Real('ys2622')
ys2631 = Real('ys2631')
ys2632 = Real('ys2632')
ys2641 = Real('ys2641')
ys2642 = Real('ys2642')
ys2651 = Real('ys2651')
ys2652 = Real('ys2652')
ys2661 = Real('ys2661')
ys2662 = Real('ys2662')
ys2671 = Real('ys2671')
ys2672 = Real('ys2672')
ys2681 = Real('ys2681')
ys2682 = Real('ys2682')
ys2691 = Real('ys2691')
ys2692 = Real('ys2692')
ys2701 = Real('ys2701')
ys2702 = Real('ys2702')
ys2711 = Real('ys2711')
ys2712 = Real('ys2712')
ys2721 = Real('ys2721')
ys2722 = Real('ys2722')
ys2731 = Real('ys2731')
ys2732 = Real('ys2732')
ys2741 = Real('ys2741')
ys2742 = Real('ys2742')
ys2751 = Real('ys2751')
ys2752 = Real('ys2752')
ys2761 = Real('ys2761')
ys2762 = Real('ys2762')
ys2771 = Real('ys2771')
ys2772 = Real('ys2772')
ys2781 = Real('ys2781')
ys2782 = Real('ys2782')
ys2791 = Real('ys2791')
ys2792 = Real('ys2792')
ys2801 = Real('ys2801')
ys2802 = Real('ys2802')
ys2811 = Real('ys2811')
ys2812 = Real('ys2812')
ys2821 = Real('ys2821')
ys2822 = Real('ys2822')
ys2831 = Real('ys2831')
ys2832 = Real('ys2832')
ys2841 = Real('ys2841')
ys2842 = Real('ys2842')
ys2851 = Real('ys2851')
ys2852 = Real('ys2852')
ys2861 = Real('ys2861')
ys2862 = Real('ys2862')
ys2871 = Real('ys2871')
ys2872 = Real('ys2872')
ys2881 = Real('ys2881')
ys2882 = Real('ys2882')
ys2891 = Real('ys2891')
ys2892 = Real('ys2892')
ys2901 = Real('ys2901')
ys2902 = Real('ys2902')
ys2911 = Real('ys2911')
ys2912 = Real('ys2912')
ys2921 = Real('ys2921')
ys2922 = Real('ys2922')
ys2931 = Real('ys2931')
ys2932 = Real('ys2932')
ys2941 = Real('ys2941')
ys2942 = Real('ys2942')
ys2951 = Real('ys2951')
ys2952 = Real('ys2952')
ys2961 = Real('ys2961')
ys2962 = Real('ys2962')
ys2971 = Real('ys2971')
ys2972 = Real('ys2972')
ys2981 = Real('ys2981')
ys2982 = Real('ys2982')
ys2991 = Real('ys2991')
ys2992 = Real('ys2992')
ys3001 = Real('ys3001')
ys3002 = Real('ys3002')
ys3011 = Real('ys3011')
ys3012 = Real('ys3012')
ys3021 = Real('ys3021')
ys3022 = Real('ys3022')
ys3031 = Real('ys3031')
ys3032 = Real('ys3032')
ys3041 = Real('ys3041')
ys3042 = Real('ys3042')
ys3051 = Real('ys3051')
ys3052 = Real('ys3052')
ys3061 = Real('ys3061')
ys3062 = Real('ys3062')
ys3071 = Real('ys3071')
ys3072 = Real('ys3072')
ys3081 = Real('ys3081')
ys3082 = Real('ys3082')
ys3091 = Real('ys3091')
ys3092 = Real('ys3092')
ys3101 = Real('ys3101')
ys3102 = Real('ys3102')
ys3111 = Real('ys3111')
ys3112 = Real('ys3112')
ys3121 = Real('ys3121')
ys3122 = Real('ys3122')
ys3131 = Real('ys3131')
ys3132 = Real('ys3132')
ys3141 = Real('ys3141')
ys3142 = Real('ys3142')
ys3151 = Real('ys3151')
ys3152 = Real('ys3152')
ys3161 = Real('ys3161')
ys3162 = Real('ys3162')
ys3171 = Real('ys3171')
ys3172 = Real('ys3172')
ys3181 = Real('ys3181')
ys3182 = Real('ys3182')
ys3191 = Real('ys3191')
ys3192 = Real('ys3192')
ys3201 = Real('ys3201')
ys3202 = Real('ys3202')
ys3211 = Real('ys3211')
ys3212 = Real('ys3212')
ys3221 = Real('ys3221')
ys3222 = Real('ys3222')
ys3231 = Real('ys3231')
ys3232 = Real('ys3232')
ys3241 = Real('ys3241')
ys3242 = Real('ys3242')
ys3251 = Real('ys3251')
ys3252 = Real('ys3252')
ys3261 = Real('ys3261')
ys3262 = Real('ys3262')
ys3271 = Real('ys3271')
ys3272 = Real('ys3272')
ys3281 = Real('ys3281')
ys3282 = Real('ys3282')
ys3291 = Real('ys3291')
ys3292 = Real('ys3292')
ys3301 = Real('ys3301')
ys3302 = Real('ys3302')
ys3311 = Real('ys3311')
ys3312 = Real('ys3312')
ys3321 = Real('ys3321')
ys3322 = Real('ys3322')
ys3331 = Real('ys3331')
ys3332 = Real('ys3332')
ys3341 = Real('ys3341')
ys3342 = Real('ys3342')
ys3351 = Real('ys3351')
ys3352 = Real('ys3352')
ys3361 = Real('ys3361')
ys3362 = Real('ys3362')
ys3371 = Real('ys3371')
ys3372 = Real('ys3372')
ys3381 = Real('ys3381')
ys3382 = Real('ys3382')
ys3391 = Real('ys3391')
ys3392 = Real('ys3392')
ys3401 = Real('ys3401')
ys3402 = Real('ys3402')
ys3411 = Real('ys3411')
ys3412 = Real('ys3412')
ys3421 = Real('ys3421')
ys3422 = Real('ys3422')
ys3431 = Real('ys3431')
ys3432 = Real('ys3432')
ys3441 = Real('ys3441')
ys3442 = Real('ys3442')
ys3451 = Real('ys3451')
ys3452 = Real('ys3452')
ys3461 = Real('ys3461')
ys3462 = Real('ys3462')
ys3471 = Real('ys3471')
ys3472 = Real('ys3472')
ys3481 = Real('ys3481')
ys3482 = Real('ys3482')
ys3491 = Real('ys3491')
ys3492 = Real('ys3492')
ys3501 = Real('ys3501')
ys3502 = Real('ys3502')
ys3511 = Real('ys3511')
ys3512 = Real('ys3512')
ys3521 = Real('ys3521')
ys3522 = Real('ys3522')
ys3531 = Real('ys3531')
ys3532 = Real('ys3532')
ys3541 = Real('ys3541')
ys3542 = Real('ys3542')
ys3551 = Real('ys3551')
ys3552 = Real('ys3552')
ys3561 = Real('ys3561')
ys3562 = Real('ys3562')
ys3571 = Real('ys3571')
ys3572 = Real('ys3572')
ys3581 = Real('ys3581')
ys3582 = Real('ys3582')
ys3591 = Real('ys3591')
ys3592 = Real('ys3592')
ys3601 = Real('ys3601')
ys3602 = Real('ys3602')
ys3611 = Real('ys3611')
ys3612 = Real('ys3612')
ys3621 = Real('ys3621')
ys3622 = Real('ys3622')
ys3631 = Real('ys3631')
ys3632 = Real('ys3632')
ys3641 = Real('ys3641')
ys3642 = Real('ys3642')
ys3651 = Real('ys3651')
ys3652 = Real('ys3652')
ys3661 = Real('ys3661')
ys3662 = Real('ys3662')
ys3671 = Real('ys3671')
ys3672 = Real('ys3672')
ys3681 = Real('ys3681')
ys3682 = Real('ys3682')
ys3691 = Real('ys3691')
ys3692 = Real('ys3692')
ys3701 = Real('ys3701')
ys3702 = Real('ys3702')
ys3711 = Real('ys3711')
ys3712 = Real('ys3712')
ys3721 = Real('ys3721')
ys3722 = Real('ys3722')
ys3731 = Real('ys3731')
ys3732 = Real('ys3732')
ys3741 = Real('ys3741')
ys3742 = Real('ys3742')
ys3751 = Real('ys3751')
ys3752 = Real('ys3752')
ys3761 = Real('ys3761')
ys3762 = Real('ys3762')

# Rates of randomized strategies
xo1l = Real('xo1l')
xo1r = Real('xo1r')
xo2l = Real('xo2l')
xo2r = Real('xo2r')
solver = Solver()


solver.add(
#We cannot do better than the fully observable case
pi0>=188, pi1>=187, pi2>=186, pi3>=185, pi4>=184, pi5>=183, pi6>=182, pi7>=181, pi8>=180, pi9>=179, pi10>=178, pi11>=177, pi12>=176, pi13>=175, pi14>=174, pi15>=173, pi16>=172, pi17>=171, pi18>=170, pi19>=169, pi20>=168, pi21>=167, pi22>=166, pi23>=165, pi24>=164, pi25>=163, pi26>=162, pi27>=161, pi28>=160, pi29>=159, pi30>=158, pi31>=157, pi32>=156, pi33>=155, pi34>=154, pi35>=153, pi36>=152, pi37>=151, pi38>=150, pi39>=149, pi40>=148, pi41>=147, pi42>=146, pi43>=145, pi44>=144, pi45>=143, pi46>=142, pi47>=141, pi48>=140, pi49>=139, pi50>=138, pi51>=137, pi52>=136, pi53>=135, pi54>=134, pi55>=133, pi56>=132, pi57>=131, pi58>=130, pi59>=129, pi60>=128, pi61>=127, pi62>=126, pi63>=125, pi64>=124, pi65>=123, pi66>=122, pi67>=121, pi68>=120, pi69>=119, pi70>=118, pi71>=117, pi72>=116, pi73>=115, pi74>=114, pi75>=113, pi76>=112, pi77>=111, pi78>=110, pi79>=109, pi80>=108, pi81>=107, pi82>=106, pi83>=105, pi84>=104, pi85>=103, pi86>=102, pi87>=101, pi88>=100, pi89>=99, pi90>=98, pi91>=97, pi92>=96, pi93>=95, pi94>=94, pi95>=93, pi96>=92, pi97>=91, pi98>=90, pi99>=89, pi100>=88, pi101>=87, pi102>=86, pi103>=85, pi104>=84, pi105>=83, pi106>=82, pi107>=81, pi108>=80, pi109>=79, pi110>=78, pi111>=77, pi112>=76, pi113>=75, pi114>=74, pi115>=73, pi116>=72, pi117>=71, pi118>=70, pi119>=69, pi120>=68, pi121>=67, pi122>=66, pi123>=65, pi124>=64, pi125>=63, pi126>=62, pi127>=61, pi128>=60, pi129>=59, pi130>=58, pi131>=57, pi132>=56, pi133>=55, pi134>=54, pi135>=53, pi136>=52, pi137>=51, pi138>=50, pi139>=49, pi140>=48, pi141>=47, pi142>=46, pi143>=45, pi144>=44, pi145>=43, pi146>=42, pi147>=41, pi148>=40, pi149>=39, pi150>=38, pi151>=37, pi152>=36, pi153>=35, pi154>=34, pi155>=33, pi156>=32, pi157>=31, pi158>=30, pi159>=29, pi160>=28, pi161>=27, pi162>=26, pi163>=25, pi164>=24, pi165>=23, pi166>=22, pi167>=21, pi168>=20, pi169>=19, pi170>=18, pi171>=17, pi172>=16, pi173>=15, pi174>=14, pi175>=13, pi176>=12, pi177>=11, pi178>=10, pi179>=9, pi180>=8, pi181>=7, pi182>=6, pi183>=5, pi184>=4, pi185>=3, pi186>=2, pi187>=1, pi188>=0, pi189>=1, pi190>=2, pi191>=3, pi192>=4, pi193>=5, pi194>=6, pi195>=7, pi196>=8, pi197>=9, pi198>=10, pi199>=11, pi200>=12, pi201>=13, pi202>=14, pi203>=15, pi204>=16, pi205>=17, pi206>=18, pi207>=19, pi208>=20, pi209>=21, pi210>=22, pi211>=23, pi212>=24, pi213>=25, pi214>=26, pi215>=27, pi216>=28, pi217>=29, pi218>=30, pi219>=31, pi220>=32, pi221>=33, pi222>=34, pi223>=35, pi224>=36, pi225>=37, pi226>=38, pi227>=39, pi228>=40, pi229>=41, pi230>=42, pi231>=43, pi232>=44, pi233>=45, pi234>=46, pi235>=47, pi236>=48, pi237>=49, pi238>=50, pi239>=51, pi240>=52, pi241>=53, pi242>=54, pi243>=55, pi244>=56, pi245>=57, pi246>=58, pi247>=59, pi248>=60, pi249>=61, pi250>=62, pi251>=63, pi252>=64, pi253>=65, pi254>=66, pi255>=67, pi256>=68, pi257>=69, pi258>=70, pi259>=71, pi260>=72, pi261>=73, pi262>=74, pi263>=75, pi264>=76, pi265>=77, pi266>=78, pi267>=79, pi268>=80, pi269>=81, pi270>=82, pi271>=83, pi272>=84, pi273>=85, pi274>=86, pi275>=87, pi276>=88, pi277>=89, pi278>=90, pi279>=91, pi280>=92, pi281>=93, pi282>=94, pi283>=95, pi284>=96, pi285>=97, pi286>=98, pi287>=99, pi288>=100, pi289>=101, pi290>=102, pi291>=103, pi292>=104, pi293>=105, pi294>=106, pi295>=107, pi296>=108, pi297>=109, pi298>=110, pi299>=111, pi300>=112, pi301>=113, pi302>=114, pi303>=115, pi304>=116, pi305>=117, pi306>=118, pi307>=119, pi308>=120, pi309>=121, pi310>=122, pi311>=123, pi312>=124, pi313>=125, pi314>=126, pi315>=127, pi316>=128, pi317>=129, pi318>=130, pi319>=131, pi320>=132, pi321>=133, pi322>=134, pi323>=135, pi324>=136, pi325>=137, pi326>=138, pi327>=139, pi328>=140, pi329>=141, pi330>=142, pi331>=143, pi332>=144, pi333>=145, pi334>=146, pi335>=147, pi336>=148, pi337>=149, pi338>=150, pi339>=151, pi340>=152, pi341>=153, pi342>=154, pi343>=155, pi344>=156, pi345>=157, pi346>=158, pi347>=159, pi348>=160, pi349>=161, pi350>=162, pi351>=163, pi352>=164, pi353>=165, pi354>=166, pi355>=167, pi356>=168, pi357>=169, pi358>=170, pi359>=171, pi360>=172, pi361>=173, pi362>=174, pi363>=175, pi364>=176, pi365>=177, pi366>=178, pi367>=179, pi368>=180, pi369>=181, pi370>=182, pi371>=183, pi372>=184, pi373>=185, pi374>=186, pi375>=187, pi376>=188, 
# Expected cost/reward equations
pi0 == (ys01*xo1l+ ys02*xo2l)*(1 + pi0) + (ys01*xo1r+ ys02*xo2r)*(1 + pi1),
pi1 == (ys11*xo1l+ ys12*xo2l)*(1 + pi0) + (ys11*xo1r+ ys12*xo2r)*(1 + pi2),
pi2 == (ys21*xo1l+ ys22*xo2l)*(1 + pi1) + (ys21*xo1r+ ys22*xo2r)*(1 + pi3),
pi3 == (ys31*xo1l+ ys32*xo2l)*(1 + pi2) + (ys31*xo1r+ ys32*xo2r)*(1 + pi4),
pi4 == (ys41*xo1l+ ys42*xo2l)*(1 + pi3) + (ys41*xo1r+ ys42*xo2r)*(1 + pi5),
pi5 == (ys51*xo1l+ ys52*xo2l)*(1 + pi4) + (ys51*xo1r+ ys52*xo2r)*(1 + pi6),
pi6 == (ys61*xo1l+ ys62*xo2l)*(1 + pi5) + (ys61*xo1r+ ys62*xo2r)*(1 + pi7),
pi7 == (ys71*xo1l+ ys72*xo2l)*(1 + pi6) + (ys71*xo1r+ ys72*xo2r)*(1 + pi8),
pi8 == (ys81*xo1l+ ys82*xo2l)*(1 + pi7) + (ys81*xo1r+ ys82*xo2r)*(1 + pi9),
pi9 == (ys91*xo1l+ ys92*xo2l)*(1 + pi8) + (ys91*xo1r+ ys92*xo2r)*(1 + pi10),
pi10 == (ys101*xo1l+ ys102*xo2l)*(1 + pi9) + (ys101*xo1r+ ys102*xo2r)*(1 + pi11),
pi11 == (ys111*xo1l+ ys112*xo2l)*(1 + pi10) + (ys111*xo1r+ ys112*xo2r)*(1 + pi12),
pi12 == (ys121*xo1l+ ys122*xo2l)*(1 + pi11) + (ys121*xo1r+ ys122*xo2r)*(1 + pi13),
pi13 == (ys131*xo1l+ ys132*xo2l)*(1 + pi12) + (ys131*xo1r+ ys132*xo2r)*(1 + pi14),
pi14 == (ys141*xo1l+ ys142*xo2l)*(1 + pi13) + (ys141*xo1r+ ys142*xo2r)*(1 + pi15),
pi15 == (ys151*xo1l+ ys152*xo2l)*(1 + pi14) + (ys151*xo1r+ ys152*xo2r)*(1 + pi16),
pi16 == (ys161*xo1l+ ys162*xo2l)*(1 + pi15) + (ys161*xo1r+ ys162*xo2r)*(1 + pi17),
pi17 == (ys171*xo1l+ ys172*xo2l)*(1 + pi16) + (ys171*xo1r+ ys172*xo2r)*(1 + pi18),
pi18 == (ys181*xo1l+ ys182*xo2l)*(1 + pi17) + (ys181*xo1r+ ys182*xo2r)*(1 + pi19),
pi19 == (ys191*xo1l+ ys192*xo2l)*(1 + pi18) + (ys191*xo1r+ ys192*xo2r)*(1 + pi20),
pi20 == (ys201*xo1l+ ys202*xo2l)*(1 + pi19) + (ys201*xo1r+ ys202*xo2r)*(1 + pi21),
pi21 == (ys211*xo1l+ ys212*xo2l)*(1 + pi20) + (ys211*xo1r+ ys212*xo2r)*(1 + pi22),
pi22 == (ys221*xo1l+ ys222*xo2l)*(1 + pi21) + (ys221*xo1r+ ys222*xo2r)*(1 + pi23),
pi23 == (ys231*xo1l+ ys232*xo2l)*(1 + pi22) + (ys231*xo1r+ ys232*xo2r)*(1 + pi24),
pi24 == (ys241*xo1l+ ys242*xo2l)*(1 + pi23) + (ys241*xo1r+ ys242*xo2r)*(1 + pi25),
pi25 == (ys251*xo1l+ ys252*xo2l)*(1 + pi24) + (ys251*xo1r+ ys252*xo2r)*(1 + pi26),
pi26 == (ys261*xo1l+ ys262*xo2l)*(1 + pi25) + (ys261*xo1r+ ys262*xo2r)*(1 + pi27),
pi27 == (ys271*xo1l+ ys272*xo2l)*(1 + pi26) + (ys271*xo1r+ ys272*xo2r)*(1 + pi28),
pi28 == (ys281*xo1l+ ys282*xo2l)*(1 + pi27) + (ys281*xo1r+ ys282*xo2r)*(1 + pi29),
pi29 == (ys291*xo1l+ ys292*xo2l)*(1 + pi28) + (ys291*xo1r+ ys292*xo2r)*(1 + pi30),
pi30 == (ys301*xo1l+ ys302*xo2l)*(1 + pi29) + (ys301*xo1r+ ys302*xo2r)*(1 + pi31),
pi31 == (ys311*xo1l+ ys312*xo2l)*(1 + pi30) + (ys311*xo1r+ ys312*xo2r)*(1 + pi32),
pi32 == (ys321*xo1l+ ys322*xo2l)*(1 + pi31) + (ys321*xo1r+ ys322*xo2r)*(1 + pi33),
pi33 == (ys331*xo1l+ ys332*xo2l)*(1 + pi32) + (ys331*xo1r+ ys332*xo2r)*(1 + pi34),
pi34 == (ys341*xo1l+ ys342*xo2l)*(1 + pi33) + (ys341*xo1r+ ys342*xo2r)*(1 + pi35),
pi35 == (ys351*xo1l+ ys352*xo2l)*(1 + pi34) + (ys351*xo1r+ ys352*xo2r)*(1 + pi36),
pi36 == (ys361*xo1l+ ys362*xo2l)*(1 + pi35) + (ys361*xo1r+ ys362*xo2r)*(1 + pi37),
pi37 == (ys371*xo1l+ ys372*xo2l)*(1 + pi36) + (ys371*xo1r+ ys372*xo2r)*(1 + pi38),
pi38 == (ys381*xo1l+ ys382*xo2l)*(1 + pi37) + (ys381*xo1r+ ys382*xo2r)*(1 + pi39),
pi39 == (ys391*xo1l+ ys392*xo2l)*(1 + pi38) + (ys391*xo1r+ ys392*xo2r)*(1 + pi40),
pi40 == (ys401*xo1l+ ys402*xo2l)*(1 + pi39) + (ys401*xo1r+ ys402*xo2r)*(1 + pi41),
pi41 == (ys411*xo1l+ ys412*xo2l)*(1 + pi40) + (ys411*xo1r+ ys412*xo2r)*(1 + pi42),
pi42 == (ys421*xo1l+ ys422*xo2l)*(1 + pi41) + (ys421*xo1r+ ys422*xo2r)*(1 + pi43),
pi43 == (ys431*xo1l+ ys432*xo2l)*(1 + pi42) + (ys431*xo1r+ ys432*xo2r)*(1 + pi44),
pi44 == (ys441*xo1l+ ys442*xo2l)*(1 + pi43) + (ys441*xo1r+ ys442*xo2r)*(1 + pi45),
pi45 == (ys451*xo1l+ ys452*xo2l)*(1 + pi44) + (ys451*xo1r+ ys452*xo2r)*(1 + pi46),
pi46 == (ys461*xo1l+ ys462*xo2l)*(1 + pi45) + (ys461*xo1r+ ys462*xo2r)*(1 + pi47),
pi47 == (ys471*xo1l+ ys472*xo2l)*(1 + pi46) + (ys471*xo1r+ ys472*xo2r)*(1 + pi48),
pi48 == (ys481*xo1l+ ys482*xo2l)*(1 + pi47) + (ys481*xo1r+ ys482*xo2r)*(1 + pi49),
pi49 == (ys491*xo1l+ ys492*xo2l)*(1 + pi48) + (ys491*xo1r+ ys492*xo2r)*(1 + pi50),
pi50 == (ys501*xo1l+ ys502*xo2l)*(1 + pi49) + (ys501*xo1r+ ys502*xo2r)*(1 + pi51),
pi51 == (ys511*xo1l+ ys512*xo2l)*(1 + pi50) + (ys511*xo1r+ ys512*xo2r)*(1 + pi52),
pi52 == (ys521*xo1l+ ys522*xo2l)*(1 + pi51) + (ys521*xo1r+ ys522*xo2r)*(1 + pi53),
pi53 == (ys531*xo1l+ ys532*xo2l)*(1 + pi52) + (ys531*xo1r+ ys532*xo2r)*(1 + pi54),
pi54 == (ys541*xo1l+ ys542*xo2l)*(1 + pi53) + (ys541*xo1r+ ys542*xo2r)*(1 + pi55),
pi55 == (ys551*xo1l+ ys552*xo2l)*(1 + pi54) + (ys551*xo1r+ ys552*xo2r)*(1 + pi56),
pi56 == (ys561*xo1l+ ys562*xo2l)*(1 + pi55) + (ys561*xo1r+ ys562*xo2r)*(1 + pi57),
pi57 == (ys571*xo1l+ ys572*xo2l)*(1 + pi56) + (ys571*xo1r+ ys572*xo2r)*(1 + pi58),
pi58 == (ys581*xo1l+ ys582*xo2l)*(1 + pi57) + (ys581*xo1r+ ys582*xo2r)*(1 + pi59),
pi59 == (ys591*xo1l+ ys592*xo2l)*(1 + pi58) + (ys591*xo1r+ ys592*xo2r)*(1 + pi60),
pi60 == (ys601*xo1l+ ys602*xo2l)*(1 + pi59) + (ys601*xo1r+ ys602*xo2r)*(1 + pi61),
pi61 == (ys611*xo1l+ ys612*xo2l)*(1 + pi60) + (ys611*xo1r+ ys612*xo2r)*(1 + pi62),
pi62 == (ys621*xo1l+ ys622*xo2l)*(1 + pi61) + (ys621*xo1r+ ys622*xo2r)*(1 + pi63),
pi63 == (ys631*xo1l+ ys632*xo2l)*(1 + pi62) + (ys631*xo1r+ ys632*xo2r)*(1 + pi64),
pi64 == (ys641*xo1l+ ys642*xo2l)*(1 + pi63) + (ys641*xo1r+ ys642*xo2r)*(1 + pi65),
pi65 == (ys651*xo1l+ ys652*xo2l)*(1 + pi64) + (ys651*xo1r+ ys652*xo2r)*(1 + pi66),
pi66 == (ys661*xo1l+ ys662*xo2l)*(1 + pi65) + (ys661*xo1r+ ys662*xo2r)*(1 + pi67),
pi67 == (ys671*xo1l+ ys672*xo2l)*(1 + pi66) + (ys671*xo1r+ ys672*xo2r)*(1 + pi68),
pi68 == (ys681*xo1l+ ys682*xo2l)*(1 + pi67) + (ys681*xo1r+ ys682*xo2r)*(1 + pi69),
pi69 == (ys691*xo1l+ ys692*xo2l)*(1 + pi68) + (ys691*xo1r+ ys692*xo2r)*(1 + pi70),
pi70 == (ys701*xo1l+ ys702*xo2l)*(1 + pi69) + (ys701*xo1r+ ys702*xo2r)*(1 + pi71),
pi71 == (ys711*xo1l+ ys712*xo2l)*(1 + pi70) + (ys711*xo1r+ ys712*xo2r)*(1 + pi72),
pi72 == (ys721*xo1l+ ys722*xo2l)*(1 + pi71) + (ys721*xo1r+ ys722*xo2r)*(1 + pi73),
pi73 == (ys731*xo1l+ ys732*xo2l)*(1 + pi72) + (ys731*xo1r+ ys732*xo2r)*(1 + pi74),
pi74 == (ys741*xo1l+ ys742*xo2l)*(1 + pi73) + (ys741*xo1r+ ys742*xo2r)*(1 + pi75),
pi75 == (ys751*xo1l+ ys752*xo2l)*(1 + pi74) + (ys751*xo1r+ ys752*xo2r)*(1 + pi76),
pi76 == (ys761*xo1l+ ys762*xo2l)*(1 + pi75) + (ys761*xo1r+ ys762*xo2r)*(1 + pi77),
pi77 == (ys771*xo1l+ ys772*xo2l)*(1 + pi76) + (ys771*xo1r+ ys772*xo2r)*(1 + pi78),
pi78 == (ys781*xo1l+ ys782*xo2l)*(1 + pi77) + (ys781*xo1r+ ys782*xo2r)*(1 + pi79),
pi79 == (ys791*xo1l+ ys792*xo2l)*(1 + pi78) + (ys791*xo1r+ ys792*xo2r)*(1 + pi80),
pi80 == (ys801*xo1l+ ys802*xo2l)*(1 + pi79) + (ys801*xo1r+ ys802*xo2r)*(1 + pi81),
pi81 == (ys811*xo1l+ ys812*xo2l)*(1 + pi80) + (ys811*xo1r+ ys812*xo2r)*(1 + pi82),
pi82 == (ys821*xo1l+ ys822*xo2l)*(1 + pi81) + (ys821*xo1r+ ys822*xo2r)*(1 + pi83),
pi83 == (ys831*xo1l+ ys832*xo2l)*(1 + pi82) + (ys831*xo1r+ ys832*xo2r)*(1 + pi84),
pi84 == (ys841*xo1l+ ys842*xo2l)*(1 + pi83) + (ys841*xo1r+ ys842*xo2r)*(1 + pi85),
pi85 == (ys851*xo1l+ ys852*xo2l)*(1 + pi84) + (ys851*xo1r+ ys852*xo2r)*(1 + pi86),
pi86 == (ys861*xo1l+ ys862*xo2l)*(1 + pi85) + (ys861*xo1r+ ys862*xo2r)*(1 + pi87),
pi87 == (ys871*xo1l+ ys872*xo2l)*(1 + pi86) + (ys871*xo1r+ ys872*xo2r)*(1 + pi88),
pi88 == (ys881*xo1l+ ys882*xo2l)*(1 + pi87) + (ys881*xo1r+ ys882*xo2r)*(1 + pi89),
pi89 == (ys891*xo1l+ ys892*xo2l)*(1 + pi88) + (ys891*xo1r+ ys892*xo2r)*(1 + pi90),
pi90 == (ys901*xo1l+ ys902*xo2l)*(1 + pi89) + (ys901*xo1r+ ys902*xo2r)*(1 + pi91),
pi91 == (ys911*xo1l+ ys912*xo2l)*(1 + pi90) + (ys911*xo1r+ ys912*xo2r)*(1 + pi92),
pi92 == (ys921*xo1l+ ys922*xo2l)*(1 + pi91) + (ys921*xo1r+ ys922*xo2r)*(1 + pi93),
pi93 == (ys931*xo1l+ ys932*xo2l)*(1 + pi92) + (ys931*xo1r+ ys932*xo2r)*(1 + pi94),
pi94 == (ys941*xo1l+ ys942*xo2l)*(1 + pi93) + (ys941*xo1r+ ys942*xo2r)*(1 + pi95),
pi95 == (ys951*xo1l+ ys952*xo2l)*(1 + pi94) + (ys951*xo1r+ ys952*xo2r)*(1 + pi96),
pi96 == (ys961*xo1l+ ys962*xo2l)*(1 + pi95) + (ys961*xo1r+ ys962*xo2r)*(1 + pi97),
pi97 == (ys971*xo1l+ ys972*xo2l)*(1 + pi96) + (ys971*xo1r+ ys972*xo2r)*(1 + pi98),
pi98 == (ys981*xo1l+ ys982*xo2l)*(1 + pi97) + (ys981*xo1r+ ys982*xo2r)*(1 + pi99),
pi99 == (ys991*xo1l+ ys992*xo2l)*(1 + pi98) + (ys991*xo1r+ ys992*xo2r)*(1 + pi100),
pi100 == (ys1001*xo1l+ ys1002*xo2l)*(1 + pi99) + (ys1001*xo1r+ ys1002*xo2r)*(1 + pi101),
pi101 == (ys1011*xo1l+ ys1012*xo2l)*(1 + pi100) + (ys1011*xo1r+ ys1012*xo2r)*(1 + pi102),
pi102 == (ys1021*xo1l+ ys1022*xo2l)*(1 + pi101) + (ys1021*xo1r+ ys1022*xo2r)*(1 + pi103),
pi103 == (ys1031*xo1l+ ys1032*xo2l)*(1 + pi102) + (ys1031*xo1r+ ys1032*xo2r)*(1 + pi104),
pi104 == (ys1041*xo1l+ ys1042*xo2l)*(1 + pi103) + (ys1041*xo1r+ ys1042*xo2r)*(1 + pi105),
pi105 == (ys1051*xo1l+ ys1052*xo2l)*(1 + pi104) + (ys1051*xo1r+ ys1052*xo2r)*(1 + pi106),
pi106 == (ys1061*xo1l+ ys1062*xo2l)*(1 + pi105) + (ys1061*xo1r+ ys1062*xo2r)*(1 + pi107),
pi107 == (ys1071*xo1l+ ys1072*xo2l)*(1 + pi106) + (ys1071*xo1r+ ys1072*xo2r)*(1 + pi108),
pi108 == (ys1081*xo1l+ ys1082*xo2l)*(1 + pi107) + (ys1081*xo1r+ ys1082*xo2r)*(1 + pi109),
pi109 == (ys1091*xo1l+ ys1092*xo2l)*(1 + pi108) + (ys1091*xo1r+ ys1092*xo2r)*(1 + pi110),
pi110 == (ys1101*xo1l+ ys1102*xo2l)*(1 + pi109) + (ys1101*xo1r+ ys1102*xo2r)*(1 + pi111),
pi111 == (ys1111*xo1l+ ys1112*xo2l)*(1 + pi110) + (ys1111*xo1r+ ys1112*xo2r)*(1 + pi112),
pi112 == (ys1121*xo1l+ ys1122*xo2l)*(1 + pi111) + (ys1121*xo1r+ ys1122*xo2r)*(1 + pi113),
pi113 == (ys1131*xo1l+ ys1132*xo2l)*(1 + pi112) + (ys1131*xo1r+ ys1132*xo2r)*(1 + pi114),
pi114 == (ys1141*xo1l+ ys1142*xo2l)*(1 + pi113) + (ys1141*xo1r+ ys1142*xo2r)*(1 + pi115),
pi115 == (ys1151*xo1l+ ys1152*xo2l)*(1 + pi114) + (ys1151*xo1r+ ys1152*xo2r)*(1 + pi116),
pi116 == (ys1161*xo1l+ ys1162*xo2l)*(1 + pi115) + (ys1161*xo1r+ ys1162*xo2r)*(1 + pi117),
pi117 == (ys1171*xo1l+ ys1172*xo2l)*(1 + pi116) + (ys1171*xo1r+ ys1172*xo2r)*(1 + pi118),
pi118 == (ys1181*xo1l+ ys1182*xo2l)*(1 + pi117) + (ys1181*xo1r+ ys1182*xo2r)*(1 + pi119),
pi119 == (ys1191*xo1l+ ys1192*xo2l)*(1 + pi118) + (ys1191*xo1r+ ys1192*xo2r)*(1 + pi120),
pi120 == (ys1201*xo1l+ ys1202*xo2l)*(1 + pi119) + (ys1201*xo1r+ ys1202*xo2r)*(1 + pi121),
pi121 == (ys1211*xo1l+ ys1212*xo2l)*(1 + pi120) + (ys1211*xo1r+ ys1212*xo2r)*(1 + pi122),
pi122 == (ys1221*xo1l+ ys1222*xo2l)*(1 + pi121) + (ys1221*xo1r+ ys1222*xo2r)*(1 + pi123),
pi123 == (ys1231*xo1l+ ys1232*xo2l)*(1 + pi122) + (ys1231*xo1r+ ys1232*xo2r)*(1 + pi124),
pi124 == (ys1241*xo1l+ ys1242*xo2l)*(1 + pi123) + (ys1241*xo1r+ ys1242*xo2r)*(1 + pi125),
pi125 == (ys1251*xo1l+ ys1252*xo2l)*(1 + pi124) + (ys1251*xo1r+ ys1252*xo2r)*(1 + pi126),
pi126 == (ys1261*xo1l+ ys1262*xo2l)*(1 + pi125) + (ys1261*xo1r+ ys1262*xo2r)*(1 + pi127),
pi127 == (ys1271*xo1l+ ys1272*xo2l)*(1 + pi126) + (ys1271*xo1r+ ys1272*xo2r)*(1 + pi128),
pi128 == (ys1281*xo1l+ ys1282*xo2l)*(1 + pi127) + (ys1281*xo1r+ ys1282*xo2r)*(1 + pi129),
pi129 == (ys1291*xo1l+ ys1292*xo2l)*(1 + pi128) + (ys1291*xo1r+ ys1292*xo2r)*(1 + pi130),
pi130 == (ys1301*xo1l+ ys1302*xo2l)*(1 + pi129) + (ys1301*xo1r+ ys1302*xo2r)*(1 + pi131),
pi131 == (ys1311*xo1l+ ys1312*xo2l)*(1 + pi130) + (ys1311*xo1r+ ys1312*xo2r)*(1 + pi132),
pi132 == (ys1321*xo1l+ ys1322*xo2l)*(1 + pi131) + (ys1321*xo1r+ ys1322*xo2r)*(1 + pi133),
pi133 == (ys1331*xo1l+ ys1332*xo2l)*(1 + pi132) + (ys1331*xo1r+ ys1332*xo2r)*(1 + pi134),
pi134 == (ys1341*xo1l+ ys1342*xo2l)*(1 + pi133) + (ys1341*xo1r+ ys1342*xo2r)*(1 + pi135),
pi135 == (ys1351*xo1l+ ys1352*xo2l)*(1 + pi134) + (ys1351*xo1r+ ys1352*xo2r)*(1 + pi136),
pi136 == (ys1361*xo1l+ ys1362*xo2l)*(1 + pi135) + (ys1361*xo1r+ ys1362*xo2r)*(1 + pi137),
pi137 == (ys1371*xo1l+ ys1372*xo2l)*(1 + pi136) + (ys1371*xo1r+ ys1372*xo2r)*(1 + pi138),
pi138 == (ys1381*xo1l+ ys1382*xo2l)*(1 + pi137) + (ys1381*xo1r+ ys1382*xo2r)*(1 + pi139),
pi139 == (ys1391*xo1l+ ys1392*xo2l)*(1 + pi138) + (ys1391*xo1r+ ys1392*xo2r)*(1 + pi140),
pi140 == (ys1401*xo1l+ ys1402*xo2l)*(1 + pi139) + (ys1401*xo1r+ ys1402*xo2r)*(1 + pi141),
pi141 == (ys1411*xo1l+ ys1412*xo2l)*(1 + pi140) + (ys1411*xo1r+ ys1412*xo2r)*(1 + pi142),
pi142 == (ys1421*xo1l+ ys1422*xo2l)*(1 + pi141) + (ys1421*xo1r+ ys1422*xo2r)*(1 + pi143),
pi143 == (ys1431*xo1l+ ys1432*xo2l)*(1 + pi142) + (ys1431*xo1r+ ys1432*xo2r)*(1 + pi144),
pi144 == (ys1441*xo1l+ ys1442*xo2l)*(1 + pi143) + (ys1441*xo1r+ ys1442*xo2r)*(1 + pi145),
pi145 == (ys1451*xo1l+ ys1452*xo2l)*(1 + pi144) + (ys1451*xo1r+ ys1452*xo2r)*(1 + pi146),
pi146 == (ys1461*xo1l+ ys1462*xo2l)*(1 + pi145) + (ys1461*xo1r+ ys1462*xo2r)*(1 + pi147),
pi147 == (ys1471*xo1l+ ys1472*xo2l)*(1 + pi146) + (ys1471*xo1r+ ys1472*xo2r)*(1 + pi148),
pi148 == (ys1481*xo1l+ ys1482*xo2l)*(1 + pi147) + (ys1481*xo1r+ ys1482*xo2r)*(1 + pi149),
pi149 == (ys1491*xo1l+ ys1492*xo2l)*(1 + pi148) + (ys1491*xo1r+ ys1492*xo2r)*(1 + pi150),
pi150 == (ys1501*xo1l+ ys1502*xo2l)*(1 + pi149) + (ys1501*xo1r+ ys1502*xo2r)*(1 + pi151),
pi151 == (ys1511*xo1l+ ys1512*xo2l)*(1 + pi150) + (ys1511*xo1r+ ys1512*xo2r)*(1 + pi152),
pi152 == (ys1521*xo1l+ ys1522*xo2l)*(1 + pi151) + (ys1521*xo1r+ ys1522*xo2r)*(1 + pi153),
pi153 == (ys1531*xo1l+ ys1532*xo2l)*(1 + pi152) + (ys1531*xo1r+ ys1532*xo2r)*(1 + pi154),
pi154 == (ys1541*xo1l+ ys1542*xo2l)*(1 + pi153) + (ys1541*xo1r+ ys1542*xo2r)*(1 + pi155),
pi155 == (ys1551*xo1l+ ys1552*xo2l)*(1 + pi154) + (ys1551*xo1r+ ys1552*xo2r)*(1 + pi156),
pi156 == (ys1561*xo1l+ ys1562*xo2l)*(1 + pi155) + (ys1561*xo1r+ ys1562*xo2r)*(1 + pi157),
pi157 == (ys1571*xo1l+ ys1572*xo2l)*(1 + pi156) + (ys1571*xo1r+ ys1572*xo2r)*(1 + pi158),
pi158 == (ys1581*xo1l+ ys1582*xo2l)*(1 + pi157) + (ys1581*xo1r+ ys1582*xo2r)*(1 + pi159),
pi159 == (ys1591*xo1l+ ys1592*xo2l)*(1 + pi158) + (ys1591*xo1r+ ys1592*xo2r)*(1 + pi160),
pi160 == (ys1601*xo1l+ ys1602*xo2l)*(1 + pi159) + (ys1601*xo1r+ ys1602*xo2r)*(1 + pi161),
pi161 == (ys1611*xo1l+ ys1612*xo2l)*(1 + pi160) + (ys1611*xo1r+ ys1612*xo2r)*(1 + pi162),
pi162 == (ys1621*xo1l+ ys1622*xo2l)*(1 + pi161) + (ys1621*xo1r+ ys1622*xo2r)*(1 + pi163),
pi163 == (ys1631*xo1l+ ys1632*xo2l)*(1 + pi162) + (ys1631*xo1r+ ys1632*xo2r)*(1 + pi164),
pi164 == (ys1641*xo1l+ ys1642*xo2l)*(1 + pi163) + (ys1641*xo1r+ ys1642*xo2r)*(1 + pi165),
pi165 == (ys1651*xo1l+ ys1652*xo2l)*(1 + pi164) + (ys1651*xo1r+ ys1652*xo2r)*(1 + pi166),
pi166 == (ys1661*xo1l+ ys1662*xo2l)*(1 + pi165) + (ys1661*xo1r+ ys1662*xo2r)*(1 + pi167),
pi167 == (ys1671*xo1l+ ys1672*xo2l)*(1 + pi166) + (ys1671*xo1r+ ys1672*xo2r)*(1 + pi168),
pi168 == (ys1681*xo1l+ ys1682*xo2l)*(1 + pi167) + (ys1681*xo1r+ ys1682*xo2r)*(1 + pi169),
pi169 == (ys1691*xo1l+ ys1692*xo2l)*(1 + pi168) + (ys1691*xo1r+ ys1692*xo2r)*(1 + pi170),
pi170 == (ys1701*xo1l+ ys1702*xo2l)*(1 + pi169) + (ys1701*xo1r+ ys1702*xo2r)*(1 + pi171),
pi171 == (ys1711*xo1l+ ys1712*xo2l)*(1 + pi170) + (ys1711*xo1r+ ys1712*xo2r)*(1 + pi172),
pi172 == (ys1721*xo1l+ ys1722*xo2l)*(1 + pi171) + (ys1721*xo1r+ ys1722*xo2r)*(1 + pi173),
pi173 == (ys1731*xo1l+ ys1732*xo2l)*(1 + pi172) + (ys1731*xo1r+ ys1732*xo2r)*(1 + pi174),
pi174 == (ys1741*xo1l+ ys1742*xo2l)*(1 + pi173) + (ys1741*xo1r+ ys1742*xo2r)*(1 + pi175),
pi175 == (ys1751*xo1l+ ys1752*xo2l)*(1 + pi174) + (ys1751*xo1r+ ys1752*xo2r)*(1 + pi176),
pi176 == (ys1761*xo1l+ ys1762*xo2l)*(1 + pi175) + (ys1761*xo1r+ ys1762*xo2r)*(1 + pi177),
pi177 == (ys1771*xo1l+ ys1772*xo2l)*(1 + pi176) + (ys1771*xo1r+ ys1772*xo2r)*(1 + pi178),
pi178 == (ys1781*xo1l+ ys1782*xo2l)*(1 + pi177) + (ys1781*xo1r+ ys1782*xo2r)*(1 + pi179),
pi179 == (ys1791*xo1l+ ys1792*xo2l)*(1 + pi178) + (ys1791*xo1r+ ys1792*xo2r)*(1 + pi180),
pi180 == (ys1801*xo1l+ ys1802*xo2l)*(1 + pi179) + (ys1801*xo1r+ ys1802*xo2r)*(1 + pi181),
pi181 == (ys1811*xo1l+ ys1812*xo2l)*(1 + pi180) + (ys1811*xo1r+ ys1812*xo2r)*(1 + pi182),
pi182 == (ys1821*xo1l+ ys1822*xo2l)*(1 + pi181) + (ys1821*xo1r+ ys1822*xo2r)*(1 + pi183),
pi183 == (ys1831*xo1l+ ys1832*xo2l)*(1 + pi182) + (ys1831*xo1r+ ys1832*xo2r)*(1 + pi184),
pi184 == (ys1841*xo1l+ ys1842*xo2l)*(1 + pi183) + (ys1841*xo1r+ ys1842*xo2r)*(1 + pi185),
pi185 == (ys1851*xo1l+ ys1852*xo2l)*(1 + pi184) + (ys1851*xo1r+ ys1852*xo2r)*(1 + pi186),
pi186 == (ys1861*xo1l+ ys1862*xo2l)*(1 + pi185) + (ys1861*xo1r+ ys1862*xo2r)*(1 + pi187),
pi187 == (ys1871*xo1l+ ys1872*xo2l)*(1 + pi186) + (ys1871*xo1r+ ys1872*xo2r)*(1 + pi188),
pi188 == 0, 
pi189 == (ys1891*xo1l+ ys1892*xo2l)*(1 + pi188) + (ys1891*xo1r+ ys1892*xo2r)*(1 + pi190),
pi190 == (ys1901*xo1l+ ys1902*xo2l)*(1 + pi189) + (ys1901*xo1r+ ys1902*xo2r)*(1 + pi191),
pi191 == (ys1911*xo1l+ ys1912*xo2l)*(1 + pi190) + (ys1911*xo1r+ ys1912*xo2r)*(1 + pi192),
pi192 == (ys1921*xo1l+ ys1922*xo2l)*(1 + pi191) + (ys1921*xo1r+ ys1922*xo2r)*(1 + pi193),
pi193 == (ys1931*xo1l+ ys1932*xo2l)*(1 + pi192) + (ys1931*xo1r+ ys1932*xo2r)*(1 + pi194),
pi194 == (ys1941*xo1l+ ys1942*xo2l)*(1 + pi193) + (ys1941*xo1r+ ys1942*xo2r)*(1 + pi195),
pi195 == (ys1951*xo1l+ ys1952*xo2l)*(1 + pi194) + (ys1951*xo1r+ ys1952*xo2r)*(1 + pi196),
pi196 == (ys1961*xo1l+ ys1962*xo2l)*(1 + pi195) + (ys1961*xo1r+ ys1962*xo2r)*(1 + pi197),
pi197 == (ys1971*xo1l+ ys1972*xo2l)*(1 + pi196) + (ys1971*xo1r+ ys1972*xo2r)*(1 + pi198),
pi198 == (ys1981*xo1l+ ys1982*xo2l)*(1 + pi197) + (ys1981*xo1r+ ys1982*xo2r)*(1 + pi199),
pi199 == (ys1991*xo1l+ ys1992*xo2l)*(1 + pi198) + (ys1991*xo1r+ ys1992*xo2r)*(1 + pi200),
pi200 == (ys2001*xo1l+ ys2002*xo2l)*(1 + pi199) + (ys2001*xo1r+ ys2002*xo2r)*(1 + pi201),
pi201 == (ys2011*xo1l+ ys2012*xo2l)*(1 + pi200) + (ys2011*xo1r+ ys2012*xo2r)*(1 + pi202),
pi202 == (ys2021*xo1l+ ys2022*xo2l)*(1 + pi201) + (ys2021*xo1r+ ys2022*xo2r)*(1 + pi203),
pi203 == (ys2031*xo1l+ ys2032*xo2l)*(1 + pi202) + (ys2031*xo1r+ ys2032*xo2r)*(1 + pi204),
pi204 == (ys2041*xo1l+ ys2042*xo2l)*(1 + pi203) + (ys2041*xo1r+ ys2042*xo2r)*(1 + pi205),
pi205 == (ys2051*xo1l+ ys2052*xo2l)*(1 + pi204) + (ys2051*xo1r+ ys2052*xo2r)*(1 + pi206),
pi206 == (ys2061*xo1l+ ys2062*xo2l)*(1 + pi205) + (ys2061*xo1r+ ys2062*xo2r)*(1 + pi207),
pi207 == (ys2071*xo1l+ ys2072*xo2l)*(1 + pi206) + (ys2071*xo1r+ ys2072*xo2r)*(1 + pi208),
pi208 == (ys2081*xo1l+ ys2082*xo2l)*(1 + pi207) + (ys2081*xo1r+ ys2082*xo2r)*(1 + pi209),
pi209 == (ys2091*xo1l+ ys2092*xo2l)*(1 + pi208) + (ys2091*xo1r+ ys2092*xo2r)*(1 + pi210),
pi210 == (ys2101*xo1l+ ys2102*xo2l)*(1 + pi209) + (ys2101*xo1r+ ys2102*xo2r)*(1 + pi211),
pi211 == (ys2111*xo1l+ ys2112*xo2l)*(1 + pi210) + (ys2111*xo1r+ ys2112*xo2r)*(1 + pi212),
pi212 == (ys2121*xo1l+ ys2122*xo2l)*(1 + pi211) + (ys2121*xo1r+ ys2122*xo2r)*(1 + pi213),
pi213 == (ys2131*xo1l+ ys2132*xo2l)*(1 + pi212) + (ys2131*xo1r+ ys2132*xo2r)*(1 + pi214),
pi214 == (ys2141*xo1l+ ys2142*xo2l)*(1 + pi213) + (ys2141*xo1r+ ys2142*xo2r)*(1 + pi215),
pi215 == (ys2151*xo1l+ ys2152*xo2l)*(1 + pi214) + (ys2151*xo1r+ ys2152*xo2r)*(1 + pi216),
pi216 == (ys2161*xo1l+ ys2162*xo2l)*(1 + pi215) + (ys2161*xo1r+ ys2162*xo2r)*(1 + pi217),
pi217 == (ys2171*xo1l+ ys2172*xo2l)*(1 + pi216) + (ys2171*xo1r+ ys2172*xo2r)*(1 + pi218),
pi218 == (ys2181*xo1l+ ys2182*xo2l)*(1 + pi217) + (ys2181*xo1r+ ys2182*xo2r)*(1 + pi219),
pi219 == (ys2191*xo1l+ ys2192*xo2l)*(1 + pi218) + (ys2191*xo1r+ ys2192*xo2r)*(1 + pi220),
pi220 == (ys2201*xo1l+ ys2202*xo2l)*(1 + pi219) + (ys2201*xo1r+ ys2202*xo2r)*(1 + pi221),
pi221 == (ys2211*xo1l+ ys2212*xo2l)*(1 + pi220) + (ys2211*xo1r+ ys2212*xo2r)*(1 + pi222),
pi222 == (ys2221*xo1l+ ys2222*xo2l)*(1 + pi221) + (ys2221*xo1r+ ys2222*xo2r)*(1 + pi223),
pi223 == (ys2231*xo1l+ ys2232*xo2l)*(1 + pi222) + (ys2231*xo1r+ ys2232*xo2r)*(1 + pi224),
pi224 == (ys2241*xo1l+ ys2242*xo2l)*(1 + pi223) + (ys2241*xo1r+ ys2242*xo2r)*(1 + pi225),
pi225 == (ys2251*xo1l+ ys2252*xo2l)*(1 + pi224) + (ys2251*xo1r+ ys2252*xo2r)*(1 + pi226),
pi226 == (ys2261*xo1l+ ys2262*xo2l)*(1 + pi225) + (ys2261*xo1r+ ys2262*xo2r)*(1 + pi227),
pi227 == (ys2271*xo1l+ ys2272*xo2l)*(1 + pi226) + (ys2271*xo1r+ ys2272*xo2r)*(1 + pi228),
pi228 == (ys2281*xo1l+ ys2282*xo2l)*(1 + pi227) + (ys2281*xo1r+ ys2282*xo2r)*(1 + pi229),
pi229 == (ys2291*xo1l+ ys2292*xo2l)*(1 + pi228) + (ys2291*xo1r+ ys2292*xo2r)*(1 + pi230),
pi230 == (ys2301*xo1l+ ys2302*xo2l)*(1 + pi229) + (ys2301*xo1r+ ys2302*xo2r)*(1 + pi231),
pi231 == (ys2311*xo1l+ ys2312*xo2l)*(1 + pi230) + (ys2311*xo1r+ ys2312*xo2r)*(1 + pi232),
pi232 == (ys2321*xo1l+ ys2322*xo2l)*(1 + pi231) + (ys2321*xo1r+ ys2322*xo2r)*(1 + pi233),
pi233 == (ys2331*xo1l+ ys2332*xo2l)*(1 + pi232) + (ys2331*xo1r+ ys2332*xo2r)*(1 + pi234),
pi234 == (ys2341*xo1l+ ys2342*xo2l)*(1 + pi233) + (ys2341*xo1r+ ys2342*xo2r)*(1 + pi235),
pi235 == (ys2351*xo1l+ ys2352*xo2l)*(1 + pi234) + (ys2351*xo1r+ ys2352*xo2r)*(1 + pi236),
pi236 == (ys2361*xo1l+ ys2362*xo2l)*(1 + pi235) + (ys2361*xo1r+ ys2362*xo2r)*(1 + pi237),
pi237 == (ys2371*xo1l+ ys2372*xo2l)*(1 + pi236) + (ys2371*xo1r+ ys2372*xo2r)*(1 + pi238),
pi238 == (ys2381*xo1l+ ys2382*xo2l)*(1 + pi237) + (ys2381*xo1r+ ys2382*xo2r)*(1 + pi239),
pi239 == (ys2391*xo1l+ ys2392*xo2l)*(1 + pi238) + (ys2391*xo1r+ ys2392*xo2r)*(1 + pi240),
pi240 == (ys2401*xo1l+ ys2402*xo2l)*(1 + pi239) + (ys2401*xo1r+ ys2402*xo2r)*(1 + pi241),
pi241 == (ys2411*xo1l+ ys2412*xo2l)*(1 + pi240) + (ys2411*xo1r+ ys2412*xo2r)*(1 + pi242),
pi242 == (ys2421*xo1l+ ys2422*xo2l)*(1 + pi241) + (ys2421*xo1r+ ys2422*xo2r)*(1 + pi243),
pi243 == (ys2431*xo1l+ ys2432*xo2l)*(1 + pi242) + (ys2431*xo1r+ ys2432*xo2r)*(1 + pi244),
pi244 == (ys2441*xo1l+ ys2442*xo2l)*(1 + pi243) + (ys2441*xo1r+ ys2442*xo2r)*(1 + pi245),
pi245 == (ys2451*xo1l+ ys2452*xo2l)*(1 + pi244) + (ys2451*xo1r+ ys2452*xo2r)*(1 + pi246),
pi246 == (ys2461*xo1l+ ys2462*xo2l)*(1 + pi245) + (ys2461*xo1r+ ys2462*xo2r)*(1 + pi247),
pi247 == (ys2471*xo1l+ ys2472*xo2l)*(1 + pi246) + (ys2471*xo1r+ ys2472*xo2r)*(1 + pi248),
pi248 == (ys2481*xo1l+ ys2482*xo2l)*(1 + pi247) + (ys2481*xo1r+ ys2482*xo2r)*(1 + pi249),
pi249 == (ys2491*xo1l+ ys2492*xo2l)*(1 + pi248) + (ys2491*xo1r+ ys2492*xo2r)*(1 + pi250),
pi250 == (ys2501*xo1l+ ys2502*xo2l)*(1 + pi249) + (ys2501*xo1r+ ys2502*xo2r)*(1 + pi251),
pi251 == (ys2511*xo1l+ ys2512*xo2l)*(1 + pi250) + (ys2511*xo1r+ ys2512*xo2r)*(1 + pi252),
pi252 == (ys2521*xo1l+ ys2522*xo2l)*(1 + pi251) + (ys2521*xo1r+ ys2522*xo2r)*(1 + pi253),
pi253 == (ys2531*xo1l+ ys2532*xo2l)*(1 + pi252) + (ys2531*xo1r+ ys2532*xo2r)*(1 + pi254),
pi254 == (ys2541*xo1l+ ys2542*xo2l)*(1 + pi253) + (ys2541*xo1r+ ys2542*xo2r)*(1 + pi255),
pi255 == (ys2551*xo1l+ ys2552*xo2l)*(1 + pi254) + (ys2551*xo1r+ ys2552*xo2r)*(1 + pi256),
pi256 == (ys2561*xo1l+ ys2562*xo2l)*(1 + pi255) + (ys2561*xo1r+ ys2562*xo2r)*(1 + pi257),
pi257 == (ys2571*xo1l+ ys2572*xo2l)*(1 + pi256) + (ys2571*xo1r+ ys2572*xo2r)*(1 + pi258),
pi258 == (ys2581*xo1l+ ys2582*xo2l)*(1 + pi257) + (ys2581*xo1r+ ys2582*xo2r)*(1 + pi259),
pi259 == (ys2591*xo1l+ ys2592*xo2l)*(1 + pi258) + (ys2591*xo1r+ ys2592*xo2r)*(1 + pi260),
pi260 == (ys2601*xo1l+ ys2602*xo2l)*(1 + pi259) + (ys2601*xo1r+ ys2602*xo2r)*(1 + pi261),
pi261 == (ys2611*xo1l+ ys2612*xo2l)*(1 + pi260) + (ys2611*xo1r+ ys2612*xo2r)*(1 + pi262),
pi262 == (ys2621*xo1l+ ys2622*xo2l)*(1 + pi261) + (ys2621*xo1r+ ys2622*xo2r)*(1 + pi263),
pi263 == (ys2631*xo1l+ ys2632*xo2l)*(1 + pi262) + (ys2631*xo1r+ ys2632*xo2r)*(1 + pi264),
pi264 == (ys2641*xo1l+ ys2642*xo2l)*(1 + pi263) + (ys2641*xo1r+ ys2642*xo2r)*(1 + pi265),
pi265 == (ys2651*xo1l+ ys2652*xo2l)*(1 + pi264) + (ys2651*xo1r+ ys2652*xo2r)*(1 + pi266),
pi266 == (ys2661*xo1l+ ys2662*xo2l)*(1 + pi265) + (ys2661*xo1r+ ys2662*xo2r)*(1 + pi267),
pi267 == (ys2671*xo1l+ ys2672*xo2l)*(1 + pi266) + (ys2671*xo1r+ ys2672*xo2r)*(1 + pi268),
pi268 == (ys2681*xo1l+ ys2682*xo2l)*(1 + pi267) + (ys2681*xo1r+ ys2682*xo2r)*(1 + pi269),
pi269 == (ys2691*xo1l+ ys2692*xo2l)*(1 + pi268) + (ys2691*xo1r+ ys2692*xo2r)*(1 + pi270),
pi270 == (ys2701*xo1l+ ys2702*xo2l)*(1 + pi269) + (ys2701*xo1r+ ys2702*xo2r)*(1 + pi271),
pi271 == (ys2711*xo1l+ ys2712*xo2l)*(1 + pi270) + (ys2711*xo1r+ ys2712*xo2r)*(1 + pi272),
pi272 == (ys2721*xo1l+ ys2722*xo2l)*(1 + pi271) + (ys2721*xo1r+ ys2722*xo2r)*(1 + pi273),
pi273 == (ys2731*xo1l+ ys2732*xo2l)*(1 + pi272) + (ys2731*xo1r+ ys2732*xo2r)*(1 + pi274),
pi274 == (ys2741*xo1l+ ys2742*xo2l)*(1 + pi273) + (ys2741*xo1r+ ys2742*xo2r)*(1 + pi275),
pi275 == (ys2751*xo1l+ ys2752*xo2l)*(1 + pi274) + (ys2751*xo1r+ ys2752*xo2r)*(1 + pi276),
pi276 == (ys2761*xo1l+ ys2762*xo2l)*(1 + pi275) + (ys2761*xo1r+ ys2762*xo2r)*(1 + pi277),
pi277 == (ys2771*xo1l+ ys2772*xo2l)*(1 + pi276) + (ys2771*xo1r+ ys2772*xo2r)*(1 + pi278),
pi278 == (ys2781*xo1l+ ys2782*xo2l)*(1 + pi277) + (ys2781*xo1r+ ys2782*xo2r)*(1 + pi279),
pi279 == (ys2791*xo1l+ ys2792*xo2l)*(1 + pi278) + (ys2791*xo1r+ ys2792*xo2r)*(1 + pi280),
pi280 == (ys2801*xo1l+ ys2802*xo2l)*(1 + pi279) + (ys2801*xo1r+ ys2802*xo2r)*(1 + pi281),
pi281 == (ys2811*xo1l+ ys2812*xo2l)*(1 + pi280) + (ys2811*xo1r+ ys2812*xo2r)*(1 + pi282),
pi282 == (ys2821*xo1l+ ys2822*xo2l)*(1 + pi281) + (ys2821*xo1r+ ys2822*xo2r)*(1 + pi283),
pi283 == (ys2831*xo1l+ ys2832*xo2l)*(1 + pi282) + (ys2831*xo1r+ ys2832*xo2r)*(1 + pi284),
pi284 == (ys2841*xo1l+ ys2842*xo2l)*(1 + pi283) + (ys2841*xo1r+ ys2842*xo2r)*(1 + pi285),
pi285 == (ys2851*xo1l+ ys2852*xo2l)*(1 + pi284) + (ys2851*xo1r+ ys2852*xo2r)*(1 + pi286),
pi286 == (ys2861*xo1l+ ys2862*xo2l)*(1 + pi285) + (ys2861*xo1r+ ys2862*xo2r)*(1 + pi287),
pi287 == (ys2871*xo1l+ ys2872*xo2l)*(1 + pi286) + (ys2871*xo1r+ ys2872*xo2r)*(1 + pi288),
pi288 == (ys2881*xo1l+ ys2882*xo2l)*(1 + pi287) + (ys2881*xo1r+ ys2882*xo2r)*(1 + pi289),
pi289 == (ys2891*xo1l+ ys2892*xo2l)*(1 + pi288) + (ys2891*xo1r+ ys2892*xo2r)*(1 + pi290),
pi290 == (ys2901*xo1l+ ys2902*xo2l)*(1 + pi289) + (ys2901*xo1r+ ys2902*xo2r)*(1 + pi291),
pi291 == (ys2911*xo1l+ ys2912*xo2l)*(1 + pi290) + (ys2911*xo1r+ ys2912*xo2r)*(1 + pi292),
pi292 == (ys2921*xo1l+ ys2922*xo2l)*(1 + pi291) + (ys2921*xo1r+ ys2922*xo2r)*(1 + pi293),
pi293 == (ys2931*xo1l+ ys2932*xo2l)*(1 + pi292) + (ys2931*xo1r+ ys2932*xo2r)*(1 + pi294),
pi294 == (ys2941*xo1l+ ys2942*xo2l)*(1 + pi293) + (ys2941*xo1r+ ys2942*xo2r)*(1 + pi295),
pi295 == (ys2951*xo1l+ ys2952*xo2l)*(1 + pi294) + (ys2951*xo1r+ ys2952*xo2r)*(1 + pi296),
pi296 == (ys2961*xo1l+ ys2962*xo2l)*(1 + pi295) + (ys2961*xo1r+ ys2962*xo2r)*(1 + pi297),
pi297 == (ys2971*xo1l+ ys2972*xo2l)*(1 + pi296) + (ys2971*xo1r+ ys2972*xo2r)*(1 + pi298),
pi298 == (ys2981*xo1l+ ys2982*xo2l)*(1 + pi297) + (ys2981*xo1r+ ys2982*xo2r)*(1 + pi299),
pi299 == (ys2991*xo1l+ ys2992*xo2l)*(1 + pi298) + (ys2991*xo1r+ ys2992*xo2r)*(1 + pi300),
pi300 == (ys3001*xo1l+ ys3002*xo2l)*(1 + pi299) + (ys3001*xo1r+ ys3002*xo2r)*(1 + pi301),
pi301 == (ys3011*xo1l+ ys3012*xo2l)*(1 + pi300) + (ys3011*xo1r+ ys3012*xo2r)*(1 + pi302),
pi302 == (ys3021*xo1l+ ys3022*xo2l)*(1 + pi301) + (ys3021*xo1r+ ys3022*xo2r)*(1 + pi303),
pi303 == (ys3031*xo1l+ ys3032*xo2l)*(1 + pi302) + (ys3031*xo1r+ ys3032*xo2r)*(1 + pi304),
pi304 == (ys3041*xo1l+ ys3042*xo2l)*(1 + pi303) + (ys3041*xo1r+ ys3042*xo2r)*(1 + pi305),
pi305 == (ys3051*xo1l+ ys3052*xo2l)*(1 + pi304) + (ys3051*xo1r+ ys3052*xo2r)*(1 + pi306),
pi306 == (ys3061*xo1l+ ys3062*xo2l)*(1 + pi305) + (ys3061*xo1r+ ys3062*xo2r)*(1 + pi307),
pi307 == (ys3071*xo1l+ ys3072*xo2l)*(1 + pi306) + (ys3071*xo1r+ ys3072*xo2r)*(1 + pi308),
pi308 == (ys3081*xo1l+ ys3082*xo2l)*(1 + pi307) + (ys3081*xo1r+ ys3082*xo2r)*(1 + pi309),
pi309 == (ys3091*xo1l+ ys3092*xo2l)*(1 + pi308) + (ys3091*xo1r+ ys3092*xo2r)*(1 + pi310),
pi310 == (ys3101*xo1l+ ys3102*xo2l)*(1 + pi309) + (ys3101*xo1r+ ys3102*xo2r)*(1 + pi311),
pi311 == (ys3111*xo1l+ ys3112*xo2l)*(1 + pi310) + (ys3111*xo1r+ ys3112*xo2r)*(1 + pi312),
pi312 == (ys3121*xo1l+ ys3122*xo2l)*(1 + pi311) + (ys3121*xo1r+ ys3122*xo2r)*(1 + pi313),
pi313 == (ys3131*xo1l+ ys3132*xo2l)*(1 + pi312) + (ys3131*xo1r+ ys3132*xo2r)*(1 + pi314),
pi314 == (ys3141*xo1l+ ys3142*xo2l)*(1 + pi313) + (ys3141*xo1r+ ys3142*xo2r)*(1 + pi315),
pi315 == (ys3151*xo1l+ ys3152*xo2l)*(1 + pi314) + (ys3151*xo1r+ ys3152*xo2r)*(1 + pi316),
pi316 == (ys3161*xo1l+ ys3162*xo2l)*(1 + pi315) + (ys3161*xo1r+ ys3162*xo2r)*(1 + pi317),
pi317 == (ys3171*xo1l+ ys3172*xo2l)*(1 + pi316) + (ys3171*xo1r+ ys3172*xo2r)*(1 + pi318),
pi318 == (ys3181*xo1l+ ys3182*xo2l)*(1 + pi317) + (ys3181*xo1r+ ys3182*xo2r)*(1 + pi319),
pi319 == (ys3191*xo1l+ ys3192*xo2l)*(1 + pi318) + (ys3191*xo1r+ ys3192*xo2r)*(1 + pi320),
pi320 == (ys3201*xo1l+ ys3202*xo2l)*(1 + pi319) + (ys3201*xo1r+ ys3202*xo2r)*(1 + pi321),
pi321 == (ys3211*xo1l+ ys3212*xo2l)*(1 + pi320) + (ys3211*xo1r+ ys3212*xo2r)*(1 + pi322),
pi322 == (ys3221*xo1l+ ys3222*xo2l)*(1 + pi321) + (ys3221*xo1r+ ys3222*xo2r)*(1 + pi323),
pi323 == (ys3231*xo1l+ ys3232*xo2l)*(1 + pi322) + (ys3231*xo1r+ ys3232*xo2r)*(1 + pi324),
pi324 == (ys3241*xo1l+ ys3242*xo2l)*(1 + pi323) + (ys3241*xo1r+ ys3242*xo2r)*(1 + pi325),
pi325 == (ys3251*xo1l+ ys3252*xo2l)*(1 + pi324) + (ys3251*xo1r+ ys3252*xo2r)*(1 + pi326),
pi326 == (ys3261*xo1l+ ys3262*xo2l)*(1 + pi325) + (ys3261*xo1r+ ys3262*xo2r)*(1 + pi327),
pi327 == (ys3271*xo1l+ ys3272*xo2l)*(1 + pi326) + (ys3271*xo1r+ ys3272*xo2r)*(1 + pi328),
pi328 == (ys3281*xo1l+ ys3282*xo2l)*(1 + pi327) + (ys3281*xo1r+ ys3282*xo2r)*(1 + pi329),
pi329 == (ys3291*xo1l+ ys3292*xo2l)*(1 + pi328) + (ys3291*xo1r+ ys3292*xo2r)*(1 + pi330),
pi330 == (ys3301*xo1l+ ys3302*xo2l)*(1 + pi329) + (ys3301*xo1r+ ys3302*xo2r)*(1 + pi331),
pi331 == (ys3311*xo1l+ ys3312*xo2l)*(1 + pi330) + (ys3311*xo1r+ ys3312*xo2r)*(1 + pi332),
pi332 == (ys3321*xo1l+ ys3322*xo2l)*(1 + pi331) + (ys3321*xo1r+ ys3322*xo2r)*(1 + pi333),
pi333 == (ys3331*xo1l+ ys3332*xo2l)*(1 + pi332) + (ys3331*xo1r+ ys3332*xo2r)*(1 + pi334),
pi334 == (ys3341*xo1l+ ys3342*xo2l)*(1 + pi333) + (ys3341*xo1r+ ys3342*xo2r)*(1 + pi335),
pi335 == (ys3351*xo1l+ ys3352*xo2l)*(1 + pi334) + (ys3351*xo1r+ ys3352*xo2r)*(1 + pi336),
pi336 == (ys3361*xo1l+ ys3362*xo2l)*(1 + pi335) + (ys3361*xo1r+ ys3362*xo2r)*(1 + pi337),
pi337 == (ys3371*xo1l+ ys3372*xo2l)*(1 + pi336) + (ys3371*xo1r+ ys3372*xo2r)*(1 + pi338),
pi338 == (ys3381*xo1l+ ys3382*xo2l)*(1 + pi337) + (ys3381*xo1r+ ys3382*xo2r)*(1 + pi339),
pi339 == (ys3391*xo1l+ ys3392*xo2l)*(1 + pi338) + (ys3391*xo1r+ ys3392*xo2r)*(1 + pi340),
pi340 == (ys3401*xo1l+ ys3402*xo2l)*(1 + pi339) + (ys3401*xo1r+ ys3402*xo2r)*(1 + pi341),
pi341 == (ys3411*xo1l+ ys3412*xo2l)*(1 + pi340) + (ys3411*xo1r+ ys3412*xo2r)*(1 + pi342),
pi342 == (ys3421*xo1l+ ys3422*xo2l)*(1 + pi341) + (ys3421*xo1r+ ys3422*xo2r)*(1 + pi343),
pi343 == (ys3431*xo1l+ ys3432*xo2l)*(1 + pi342) + (ys3431*xo1r+ ys3432*xo2r)*(1 + pi344),
pi344 == (ys3441*xo1l+ ys3442*xo2l)*(1 + pi343) + (ys3441*xo1r+ ys3442*xo2r)*(1 + pi345),
pi345 == (ys3451*xo1l+ ys3452*xo2l)*(1 + pi344) + (ys3451*xo1r+ ys3452*xo2r)*(1 + pi346),
pi346 == (ys3461*xo1l+ ys3462*xo2l)*(1 + pi345) + (ys3461*xo1r+ ys3462*xo2r)*(1 + pi347),
pi347 == (ys3471*xo1l+ ys3472*xo2l)*(1 + pi346) + (ys3471*xo1r+ ys3472*xo2r)*(1 + pi348),
pi348 == (ys3481*xo1l+ ys3482*xo2l)*(1 + pi347) + (ys3481*xo1r+ ys3482*xo2r)*(1 + pi349),
pi349 == (ys3491*xo1l+ ys3492*xo2l)*(1 + pi348) + (ys3491*xo1r+ ys3492*xo2r)*(1 + pi350),
pi350 == (ys3501*xo1l+ ys3502*xo2l)*(1 + pi349) + (ys3501*xo1r+ ys3502*xo2r)*(1 + pi351),
pi351 == (ys3511*xo1l+ ys3512*xo2l)*(1 + pi350) + (ys3511*xo1r+ ys3512*xo2r)*(1 + pi352),
pi352 == (ys3521*xo1l+ ys3522*xo2l)*(1 + pi351) + (ys3521*xo1r+ ys3522*xo2r)*(1 + pi353),
pi353 == (ys3531*xo1l+ ys3532*xo2l)*(1 + pi352) + (ys3531*xo1r+ ys3532*xo2r)*(1 + pi354),
pi354 == (ys3541*xo1l+ ys3542*xo2l)*(1 + pi353) + (ys3541*xo1r+ ys3542*xo2r)*(1 + pi355),
pi355 == (ys3551*xo1l+ ys3552*xo2l)*(1 + pi354) + (ys3551*xo1r+ ys3552*xo2r)*(1 + pi356),
pi356 == (ys3561*xo1l+ ys3562*xo2l)*(1 + pi355) + (ys3561*xo1r+ ys3562*xo2r)*(1 + pi357),
pi357 == (ys3571*xo1l+ ys3572*xo2l)*(1 + pi356) + (ys3571*xo1r+ ys3572*xo2r)*(1 + pi358),
pi358 == (ys3581*xo1l+ ys3582*xo2l)*(1 + pi357) + (ys3581*xo1r+ ys3582*xo2r)*(1 + pi359),
pi359 == (ys3591*xo1l+ ys3592*xo2l)*(1 + pi358) + (ys3591*xo1r+ ys3592*xo2r)*(1 + pi360),
pi360 == (ys3601*xo1l+ ys3602*xo2l)*(1 + pi359) + (ys3601*xo1r+ ys3602*xo2r)*(1 + pi361),
pi361 == (ys3611*xo1l+ ys3612*xo2l)*(1 + pi360) + (ys3611*xo1r+ ys3612*xo2r)*(1 + pi362),
pi362 == (ys3621*xo1l+ ys3622*xo2l)*(1 + pi361) + (ys3621*xo1r+ ys3622*xo2r)*(1 + pi363),
pi363 == (ys3631*xo1l+ ys3632*xo2l)*(1 + pi362) + (ys3631*xo1r+ ys3632*xo2r)*(1 + pi364),
pi364 == (ys3641*xo1l+ ys3642*xo2l)*(1 + pi363) + (ys3641*xo1r+ ys3642*xo2r)*(1 + pi365),
pi365 == (ys3651*xo1l+ ys3652*xo2l)*(1 + pi364) + (ys3651*xo1r+ ys3652*xo2r)*(1 + pi366),
pi366 == (ys3661*xo1l+ ys3662*xo2l)*(1 + pi365) + (ys3661*xo1r+ ys3662*xo2r)*(1 + pi367),
pi367 == (ys3671*xo1l+ ys3672*xo2l)*(1 + pi366) + (ys3671*xo1r+ ys3672*xo2r)*(1 + pi368),
pi368 == (ys3681*xo1l+ ys3682*xo2l)*(1 + pi367) + (ys3681*xo1r+ ys3682*xo2r)*(1 + pi369),
pi369 == (ys3691*xo1l+ ys3692*xo2l)*(1 + pi368) + (ys3691*xo1r+ ys3692*xo2r)*(1 + pi370),
pi370 == (ys3701*xo1l+ ys3702*xo2l)*(1 + pi369) + (ys3701*xo1r+ ys3702*xo2r)*(1 + pi371),
pi371 == (ys3711*xo1l+ ys3712*xo2l)*(1 + pi370) + (ys3711*xo1r+ ys3712*xo2r)*(1 + pi372),
pi372 == (ys3721*xo1l+ ys3722*xo2l)*(1 + pi371) + (ys3721*xo1r+ ys3722*xo2r)*(1 + pi373),
pi373 == (ys3731*xo1l+ ys3732*xo2l)*(1 + pi372) + (ys3731*xo1r+ ys3732*xo2r)*(1 + pi374),
pi374 == (ys3741*xo1l+ ys3742*xo2l)*(1 + pi373) + (ys3741*xo1r+ ys3742*xo2r)*(1 + pi375),
pi375 == (ys3751*xo1l+ ys3752*xo2l)*(1 + pi374) + (ys3751*xo1r+ ys3752*xo2r)*(1 + pi376),
pi376 == (ys3761*xo1l+ ys3762*xo2l)*(1 + pi375) + (ys3761*xo1r+ ys3762*xo2r)*(1 + pi376),
# We are dropped uniformly in the line
# We want to check if the minimal expected cost is below some threshold <= Q(189,2)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi99+pi100+pi101+pi102+pi103+pi104+pi105+pi106+pi107+pi108+pi109+pi110+pi111+pi112+pi113+pi114+pi115+pi116+pi117+pi118+pi119+pi120+pi121+pi122+pi123+pi124+pi125+pi126+pi127+pi128+pi129+pi130+pi131+pi132+pi133+pi134+pi135+pi136+pi137+pi138+pi139+pi140+pi141+pi142+pi143+pi144+pi145+pi146+pi147+pi148+pi149+pi150+pi151+pi152+pi153+pi154+pi155+pi156+pi157+pi158+pi159+pi160+pi161+pi162+pi163+pi164+pi165+pi166+pi167+pi168+pi169+pi170+pi171+pi172+pi173+pi174+pi175+pi176+pi177+pi178+pi179+pi180+pi181+pi182+pi183+pi184+pi185+pi186+pi187+pi189+pi190+pi191+pi192+pi193+pi194+pi195+pi196+pi197+pi198+pi199+pi200+pi201+pi202+pi203+pi204+pi205+pi206+pi207+pi208+pi209+pi210+pi211+pi212+pi213+pi214+pi215+pi216+pi217+pi218+pi219+pi220+pi221+pi222+pi223+pi224+pi225+pi226+pi227+pi228+pi229+pi230+pi231+pi232+pi233+pi234+pi235+pi236+pi237+pi238+pi239+pi240+pi241+pi242+pi243+pi244+pi245+pi246+pi247+pi248+pi249+pi250+pi251+pi252+pi253+pi254+pi255+pi256+pi257+pi258+pi259+pi260+pi261+pi262+pi263+pi264+pi265+pi266+pi267+pi268+pi269+pi270+pi271+pi272+pi273+pi274+pi275+pi276+pi277+pi278+pi279+pi280+pi281+pi282+pi283+pi284+pi285+pi286+pi287+pi288+pi289+pi290+pi291+pi292+pi293+pi294+pi295+pi296+pi297+pi298+pi299+pi300+pi301+pi302+pi303+pi304+pi305+pi306+pi307+pi308+pi309+pi310+pi311+pi312+pi313+pi314+pi315+pi316+pi317+pi318+pi319+pi320+pi321+pi322+pi323+pi324+pi325+pi326+pi327+pi328+pi329+pi330+pi331+pi332+pi333+pi334+pi335+pi336+pi337+pi338+pi339+pi340+pi341+pi342+pi343+pi344+pi345+pi346+pi347+pi348+pi349+pi350+pi351+pi352+pi353+pi354+pi355+pi356+pi357+pi358+pi359+pi360+pi361+pi362+pi363+pi364+pi365+pi366+pi367+pi368+pi369+pi370+pi371+pi372+pi373+pi374+pi375+pi376) * Q(1,376) <= Q(189,2),
# Randomised strategies (proper probability distributions)
xo1l>= 0,
xo1l<= 1,
xo1r>= 0,
xo1r<= 1,
xo2l>= 0,
xo2l<= 1,
xo2r>= 0,
xo2r<= 1,
xo1l + xo1r == 1,
xo2l + xo2r == 1,
# Deterministic Strategies activated
Or(xo1l == 0, xo1l == 1),
Or(xo1r == 0, xo1r == 1),
Or(xo2l == 0, xo2l == 1),
Or(xo2r == 0, xo2r == 1),
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
Or(ys81== 0 , ys81== 1),
Or(ys82== 0 , ys82== 1),
Or(ys91== 0 , ys91== 1),
Or(ys92== 0 , ys92== 1),
Or(ys101== 0 , ys101== 1),
Or(ys102== 0 , ys102== 1),
Or(ys111== 0 , ys111== 1),
Or(ys112== 0 , ys112== 1),
Or(ys121== 0 , ys121== 1),
Or(ys122== 0 , ys122== 1),
Or(ys131== 0 , ys131== 1),
Or(ys132== 0 , ys132== 1),
Or(ys141== 0 , ys141== 1),
Or(ys142== 0 , ys142== 1),
Or(ys151== 0 , ys151== 1),
Or(ys152== 0 , ys152== 1),
Or(ys161== 0 , ys161== 1),
Or(ys162== 0 , ys162== 1),
Or(ys171== 0 , ys171== 1),
Or(ys172== 0 , ys172== 1),
Or(ys181== 0 , ys181== 1),
Or(ys182== 0 , ys182== 1),
Or(ys191== 0 , ys191== 1),
Or(ys192== 0 , ys192== 1),
Or(ys201== 0 , ys201== 1),
Or(ys202== 0 , ys202== 1),
Or(ys211== 0 , ys211== 1),
Or(ys212== 0 , ys212== 1),
Or(ys221== 0 , ys221== 1),
Or(ys222== 0 , ys222== 1),
Or(ys231== 0 , ys231== 1),
Or(ys232== 0 , ys232== 1),
Or(ys241== 0 , ys241== 1),
Or(ys242== 0 , ys242== 1),
Or(ys251== 0 , ys251== 1),
Or(ys252== 0 , ys252== 1),
Or(ys261== 0 , ys261== 1),
Or(ys262== 0 , ys262== 1),
Or(ys271== 0 , ys271== 1),
Or(ys272== 0 , ys272== 1),
Or(ys281== 0 , ys281== 1),
Or(ys282== 0 , ys282== 1),
Or(ys291== 0 , ys291== 1),
Or(ys292== 0 , ys292== 1),
Or(ys301== 0 , ys301== 1),
Or(ys302== 0 , ys302== 1),
Or(ys311== 0 , ys311== 1),
Or(ys312== 0 , ys312== 1),
Or(ys321== 0 , ys321== 1),
Or(ys322== 0 , ys322== 1),
Or(ys331== 0 , ys331== 1),
Or(ys332== 0 , ys332== 1),
Or(ys341== 0 , ys341== 1),
Or(ys342== 0 , ys342== 1),
Or(ys351== 0 , ys351== 1),
Or(ys352== 0 , ys352== 1),
Or(ys361== 0 , ys361== 1),
Or(ys362== 0 , ys362== 1),
Or(ys371== 0 , ys371== 1),
Or(ys372== 0 , ys372== 1),
Or(ys381== 0 , ys381== 1),
Or(ys382== 0 , ys382== 1),
Or(ys391== 0 , ys391== 1),
Or(ys392== 0 , ys392== 1),
Or(ys401== 0 , ys401== 1),
Or(ys402== 0 , ys402== 1),
Or(ys411== 0 , ys411== 1),
Or(ys412== 0 , ys412== 1),
Or(ys421== 0 , ys421== 1),
Or(ys422== 0 , ys422== 1),
Or(ys431== 0 , ys431== 1),
Or(ys432== 0 , ys432== 1),
Or(ys441== 0 , ys441== 1),
Or(ys442== 0 , ys442== 1),
Or(ys451== 0 , ys451== 1),
Or(ys452== 0 , ys452== 1),
Or(ys461== 0 , ys461== 1),
Or(ys462== 0 , ys462== 1),
Or(ys471== 0 , ys471== 1),
Or(ys472== 0 , ys472== 1),
Or(ys481== 0 , ys481== 1),
Or(ys482== 0 , ys482== 1),
Or(ys491== 0 , ys491== 1),
Or(ys492== 0 , ys492== 1),
Or(ys501== 0 , ys501== 1),
Or(ys502== 0 , ys502== 1),
Or(ys511== 0 , ys511== 1),
Or(ys512== 0 , ys512== 1),
Or(ys521== 0 , ys521== 1),
Or(ys522== 0 , ys522== 1),
Or(ys531== 0 , ys531== 1),
Or(ys532== 0 , ys532== 1),
Or(ys541== 0 , ys541== 1),
Or(ys542== 0 , ys542== 1),
Or(ys551== 0 , ys551== 1),
Or(ys552== 0 , ys552== 1),
Or(ys561== 0 , ys561== 1),
Or(ys562== 0 , ys562== 1),
Or(ys571== 0 , ys571== 1),
Or(ys572== 0 , ys572== 1),
Or(ys581== 0 , ys581== 1),
Or(ys582== 0 , ys582== 1),
Or(ys591== 0 , ys591== 1),
Or(ys592== 0 , ys592== 1),
Or(ys601== 0 , ys601== 1),
Or(ys602== 0 , ys602== 1),
Or(ys611== 0 , ys611== 1),
Or(ys612== 0 , ys612== 1),
Or(ys621== 0 , ys621== 1),
Or(ys622== 0 , ys622== 1),
Or(ys631== 0 , ys631== 1),
Or(ys632== 0 , ys632== 1),
Or(ys641== 0 , ys641== 1),
Or(ys642== 0 , ys642== 1),
Or(ys651== 0 , ys651== 1),
Or(ys652== 0 , ys652== 1),
Or(ys661== 0 , ys661== 1),
Or(ys662== 0 , ys662== 1),
Or(ys671== 0 , ys671== 1),
Or(ys672== 0 , ys672== 1),
Or(ys681== 0 , ys681== 1),
Or(ys682== 0 , ys682== 1),
Or(ys691== 0 , ys691== 1),
Or(ys692== 0 , ys692== 1),
Or(ys701== 0 , ys701== 1),
Or(ys702== 0 , ys702== 1),
Or(ys711== 0 , ys711== 1),
Or(ys712== 0 , ys712== 1),
Or(ys721== 0 , ys721== 1),
Or(ys722== 0 , ys722== 1),
Or(ys731== 0 , ys731== 1),
Or(ys732== 0 , ys732== 1),
Or(ys741== 0 , ys741== 1),
Or(ys742== 0 , ys742== 1),
Or(ys751== 0 , ys751== 1),
Or(ys752== 0 , ys752== 1),
Or(ys761== 0 , ys761== 1),
Or(ys762== 0 , ys762== 1),
Or(ys771== 0 , ys771== 1),
Or(ys772== 0 , ys772== 1),
Or(ys781== 0 , ys781== 1),
Or(ys782== 0 , ys782== 1),
Or(ys791== 0 , ys791== 1),
Or(ys792== 0 , ys792== 1),
Or(ys801== 0 , ys801== 1),
Or(ys802== 0 , ys802== 1),
Or(ys811== 0 , ys811== 1),
Or(ys812== 0 , ys812== 1),
Or(ys821== 0 , ys821== 1),
Or(ys822== 0 , ys822== 1),
Or(ys831== 0 , ys831== 1),
Or(ys832== 0 , ys832== 1),
Or(ys841== 0 , ys841== 1),
Or(ys842== 0 , ys842== 1),
Or(ys851== 0 , ys851== 1),
Or(ys852== 0 , ys852== 1),
Or(ys861== 0 , ys861== 1),
Or(ys862== 0 , ys862== 1),
Or(ys871== 0 , ys871== 1),
Or(ys872== 0 , ys872== 1),
Or(ys881== 0 , ys881== 1),
Or(ys882== 0 , ys882== 1),
Or(ys891== 0 , ys891== 1),
Or(ys892== 0 , ys892== 1),
Or(ys901== 0 , ys901== 1),
Or(ys902== 0 , ys902== 1),
Or(ys911== 0 , ys911== 1),
Or(ys912== 0 , ys912== 1),
Or(ys921== 0 , ys921== 1),
Or(ys922== 0 , ys922== 1),
Or(ys931== 0 , ys931== 1),
Or(ys932== 0 , ys932== 1),
Or(ys941== 0 , ys941== 1),
Or(ys942== 0 , ys942== 1),
Or(ys951== 0 , ys951== 1),
Or(ys952== 0 , ys952== 1),
Or(ys961== 0 , ys961== 1),
Or(ys962== 0 , ys962== 1),
Or(ys971== 0 , ys971== 1),
Or(ys972== 0 , ys972== 1),
Or(ys981== 0 , ys981== 1),
Or(ys982== 0 , ys982== 1),
Or(ys991== 0 , ys991== 1),
Or(ys992== 0 , ys992== 1),
Or(ys1001== 0 , ys1001== 1),
Or(ys1002== 0 , ys1002== 1),
Or(ys1011== 0 , ys1011== 1),
Or(ys1012== 0 , ys1012== 1),
Or(ys1021== 0 , ys1021== 1),
Or(ys1022== 0 , ys1022== 1),
Or(ys1031== 0 , ys1031== 1),
Or(ys1032== 0 , ys1032== 1),
Or(ys1041== 0 , ys1041== 1),
Or(ys1042== 0 , ys1042== 1),
Or(ys1051== 0 , ys1051== 1),
Or(ys1052== 0 , ys1052== 1),
Or(ys1061== 0 , ys1061== 1),
Or(ys1062== 0 , ys1062== 1),
Or(ys1071== 0 , ys1071== 1),
Or(ys1072== 0 , ys1072== 1),
Or(ys1081== 0 , ys1081== 1),
Or(ys1082== 0 , ys1082== 1),
Or(ys1091== 0 , ys1091== 1),
Or(ys1092== 0 , ys1092== 1),
Or(ys1101== 0 , ys1101== 1),
Or(ys1102== 0 , ys1102== 1),
Or(ys1111== 0 , ys1111== 1),
Or(ys1112== 0 , ys1112== 1),
Or(ys1121== 0 , ys1121== 1),
Or(ys1122== 0 , ys1122== 1),
Or(ys1131== 0 , ys1131== 1),
Or(ys1132== 0 , ys1132== 1),
Or(ys1141== 0 , ys1141== 1),
Or(ys1142== 0 , ys1142== 1),
Or(ys1151== 0 , ys1151== 1),
Or(ys1152== 0 , ys1152== 1),
Or(ys1161== 0 , ys1161== 1),
Or(ys1162== 0 , ys1162== 1),
Or(ys1171== 0 , ys1171== 1),
Or(ys1172== 0 , ys1172== 1),
Or(ys1181== 0 , ys1181== 1),
Or(ys1182== 0 , ys1182== 1),
Or(ys1191== 0 , ys1191== 1),
Or(ys1192== 0 , ys1192== 1),
Or(ys1201== 0 , ys1201== 1),
Or(ys1202== 0 , ys1202== 1),
Or(ys1211== 0 , ys1211== 1),
Or(ys1212== 0 , ys1212== 1),
Or(ys1221== 0 , ys1221== 1),
Or(ys1222== 0 , ys1222== 1),
Or(ys1231== 0 , ys1231== 1),
Or(ys1232== 0 , ys1232== 1),
Or(ys1241== 0 , ys1241== 1),
Or(ys1242== 0 , ys1242== 1),
Or(ys1251== 0 , ys1251== 1),
Or(ys1252== 0 , ys1252== 1),
Or(ys1261== 0 , ys1261== 1),
Or(ys1262== 0 , ys1262== 1),
Or(ys1271== 0 , ys1271== 1),
Or(ys1272== 0 , ys1272== 1),
Or(ys1281== 0 , ys1281== 1),
Or(ys1282== 0 , ys1282== 1),
Or(ys1291== 0 , ys1291== 1),
Or(ys1292== 0 , ys1292== 1),
Or(ys1301== 0 , ys1301== 1),
Or(ys1302== 0 , ys1302== 1),
Or(ys1311== 0 , ys1311== 1),
Or(ys1312== 0 , ys1312== 1),
Or(ys1321== 0 , ys1321== 1),
Or(ys1322== 0 , ys1322== 1),
Or(ys1331== 0 , ys1331== 1),
Or(ys1332== 0 , ys1332== 1),
Or(ys1341== 0 , ys1341== 1),
Or(ys1342== 0 , ys1342== 1),
Or(ys1351== 0 , ys1351== 1),
Or(ys1352== 0 , ys1352== 1),
Or(ys1361== 0 , ys1361== 1),
Or(ys1362== 0 , ys1362== 1),
Or(ys1371== 0 , ys1371== 1),
Or(ys1372== 0 , ys1372== 1),
Or(ys1381== 0 , ys1381== 1),
Or(ys1382== 0 , ys1382== 1),
Or(ys1391== 0 , ys1391== 1),
Or(ys1392== 0 , ys1392== 1),
Or(ys1401== 0 , ys1401== 1),
Or(ys1402== 0 , ys1402== 1),
Or(ys1411== 0 , ys1411== 1),
Or(ys1412== 0 , ys1412== 1),
Or(ys1421== 0 , ys1421== 1),
Or(ys1422== 0 , ys1422== 1),
Or(ys1431== 0 , ys1431== 1),
Or(ys1432== 0 , ys1432== 1),
Or(ys1441== 0 , ys1441== 1),
Or(ys1442== 0 , ys1442== 1),
Or(ys1451== 0 , ys1451== 1),
Or(ys1452== 0 , ys1452== 1),
Or(ys1461== 0 , ys1461== 1),
Or(ys1462== 0 , ys1462== 1),
Or(ys1471== 0 , ys1471== 1),
Or(ys1472== 0 , ys1472== 1),
Or(ys1481== 0 , ys1481== 1),
Or(ys1482== 0 , ys1482== 1),
Or(ys1491== 0 , ys1491== 1),
Or(ys1492== 0 , ys1492== 1),
Or(ys1501== 0 , ys1501== 1),
Or(ys1502== 0 , ys1502== 1),
Or(ys1511== 0 , ys1511== 1),
Or(ys1512== 0 , ys1512== 1),
Or(ys1521== 0 , ys1521== 1),
Or(ys1522== 0 , ys1522== 1),
Or(ys1531== 0 , ys1531== 1),
Or(ys1532== 0 , ys1532== 1),
Or(ys1541== 0 , ys1541== 1),
Or(ys1542== 0 , ys1542== 1),
Or(ys1551== 0 , ys1551== 1),
Or(ys1552== 0 , ys1552== 1),
Or(ys1561== 0 , ys1561== 1),
Or(ys1562== 0 , ys1562== 1),
Or(ys1571== 0 , ys1571== 1),
Or(ys1572== 0 , ys1572== 1),
Or(ys1581== 0 , ys1581== 1),
Or(ys1582== 0 , ys1582== 1),
Or(ys1591== 0 , ys1591== 1),
Or(ys1592== 0 , ys1592== 1),
Or(ys1601== 0 , ys1601== 1),
Or(ys1602== 0 , ys1602== 1),
Or(ys1611== 0 , ys1611== 1),
Or(ys1612== 0 , ys1612== 1),
Or(ys1621== 0 , ys1621== 1),
Or(ys1622== 0 , ys1622== 1),
Or(ys1631== 0 , ys1631== 1),
Or(ys1632== 0 , ys1632== 1),
Or(ys1641== 0 , ys1641== 1),
Or(ys1642== 0 , ys1642== 1),
Or(ys1651== 0 , ys1651== 1),
Or(ys1652== 0 , ys1652== 1),
Or(ys1661== 0 , ys1661== 1),
Or(ys1662== 0 , ys1662== 1),
Or(ys1671== 0 , ys1671== 1),
Or(ys1672== 0 , ys1672== 1),
Or(ys1681== 0 , ys1681== 1),
Or(ys1682== 0 , ys1682== 1),
Or(ys1691== 0 , ys1691== 1),
Or(ys1692== 0 , ys1692== 1),
Or(ys1701== 0 , ys1701== 1),
Or(ys1702== 0 , ys1702== 1),
Or(ys1711== 0 , ys1711== 1),
Or(ys1712== 0 , ys1712== 1),
Or(ys1721== 0 , ys1721== 1),
Or(ys1722== 0 , ys1722== 1),
Or(ys1731== 0 , ys1731== 1),
Or(ys1732== 0 , ys1732== 1),
Or(ys1741== 0 , ys1741== 1),
Or(ys1742== 0 , ys1742== 1),
Or(ys1751== 0 , ys1751== 1),
Or(ys1752== 0 , ys1752== 1),
Or(ys1761== 0 , ys1761== 1),
Or(ys1762== 0 , ys1762== 1),
Or(ys1771== 0 , ys1771== 1),
Or(ys1772== 0 , ys1772== 1),
Or(ys1781== 0 , ys1781== 1),
Or(ys1782== 0 , ys1782== 1),
Or(ys1791== 0 , ys1791== 1),
Or(ys1792== 0 , ys1792== 1),
Or(ys1801== 0 , ys1801== 1),
Or(ys1802== 0 , ys1802== 1),
Or(ys1811== 0 , ys1811== 1),
Or(ys1812== 0 , ys1812== 1),
Or(ys1821== 0 , ys1821== 1),
Or(ys1822== 0 , ys1822== 1),
Or(ys1831== 0 , ys1831== 1),
Or(ys1832== 0 , ys1832== 1),
Or(ys1841== 0 , ys1841== 1),
Or(ys1842== 0 , ys1842== 1),
Or(ys1851== 0 , ys1851== 1),
Or(ys1852== 0 , ys1852== 1),
Or(ys1861== 0 , ys1861== 1),
Or(ys1862== 0 , ys1862== 1),
Or(ys1871== 0 , ys1871== 1),
Or(ys1872== 0 , ys1872== 1),
Or(ys1891== 0 , ys1891== 1),
Or(ys1892== 0 , ys1892== 1),
Or(ys1901== 0 , ys1901== 1),
Or(ys1902== 0 , ys1902== 1),
Or(ys1911== 0 , ys1911== 1),
Or(ys1912== 0 , ys1912== 1),
Or(ys1921== 0 , ys1921== 1),
Or(ys1922== 0 , ys1922== 1),
Or(ys1931== 0 , ys1931== 1),
Or(ys1932== 0 , ys1932== 1),
Or(ys1941== 0 , ys1941== 1),
Or(ys1942== 0 , ys1942== 1),
Or(ys1951== 0 , ys1951== 1),
Or(ys1952== 0 , ys1952== 1),
Or(ys1961== 0 , ys1961== 1),
Or(ys1962== 0 , ys1962== 1),
Or(ys1971== 0 , ys1971== 1),
Or(ys1972== 0 , ys1972== 1),
Or(ys1981== 0 , ys1981== 1),
Or(ys1982== 0 , ys1982== 1),
Or(ys1991== 0 , ys1991== 1),
Or(ys1992== 0 , ys1992== 1),
Or(ys2001== 0 , ys2001== 1),
Or(ys2002== 0 , ys2002== 1),
Or(ys2011== 0 , ys2011== 1),
Or(ys2012== 0 , ys2012== 1),
Or(ys2021== 0 , ys2021== 1),
Or(ys2022== 0 , ys2022== 1),
Or(ys2031== 0 , ys2031== 1),
Or(ys2032== 0 , ys2032== 1),
Or(ys2041== 0 , ys2041== 1),
Or(ys2042== 0 , ys2042== 1),
Or(ys2051== 0 , ys2051== 1),
Or(ys2052== 0 , ys2052== 1),
Or(ys2061== 0 , ys2061== 1),
Or(ys2062== 0 , ys2062== 1),
Or(ys2071== 0 , ys2071== 1),
Or(ys2072== 0 , ys2072== 1),
Or(ys2081== 0 , ys2081== 1),
Or(ys2082== 0 , ys2082== 1),
Or(ys2091== 0 , ys2091== 1),
Or(ys2092== 0 , ys2092== 1),
Or(ys2101== 0 , ys2101== 1),
Or(ys2102== 0 , ys2102== 1),
Or(ys2111== 0 , ys2111== 1),
Or(ys2112== 0 , ys2112== 1),
Or(ys2121== 0 , ys2121== 1),
Or(ys2122== 0 , ys2122== 1),
Or(ys2131== 0 , ys2131== 1),
Or(ys2132== 0 , ys2132== 1),
Or(ys2141== 0 , ys2141== 1),
Or(ys2142== 0 , ys2142== 1),
Or(ys2151== 0 , ys2151== 1),
Or(ys2152== 0 , ys2152== 1),
Or(ys2161== 0 , ys2161== 1),
Or(ys2162== 0 , ys2162== 1),
Or(ys2171== 0 , ys2171== 1),
Or(ys2172== 0 , ys2172== 1),
Or(ys2181== 0 , ys2181== 1),
Or(ys2182== 0 , ys2182== 1),
Or(ys2191== 0 , ys2191== 1),
Or(ys2192== 0 , ys2192== 1),
Or(ys2201== 0 , ys2201== 1),
Or(ys2202== 0 , ys2202== 1),
Or(ys2211== 0 , ys2211== 1),
Or(ys2212== 0 , ys2212== 1),
Or(ys2221== 0 , ys2221== 1),
Or(ys2222== 0 , ys2222== 1),
Or(ys2231== 0 , ys2231== 1),
Or(ys2232== 0 , ys2232== 1),
Or(ys2241== 0 , ys2241== 1),
Or(ys2242== 0 , ys2242== 1),
Or(ys2251== 0 , ys2251== 1),
Or(ys2252== 0 , ys2252== 1),
Or(ys2261== 0 , ys2261== 1),
Or(ys2262== 0 , ys2262== 1),
Or(ys2271== 0 , ys2271== 1),
Or(ys2272== 0 , ys2272== 1),
Or(ys2281== 0 , ys2281== 1),
Or(ys2282== 0 , ys2282== 1),
Or(ys2291== 0 , ys2291== 1),
Or(ys2292== 0 , ys2292== 1),
Or(ys2301== 0 , ys2301== 1),
Or(ys2302== 0 , ys2302== 1),
Or(ys2311== 0 , ys2311== 1),
Or(ys2312== 0 , ys2312== 1),
Or(ys2321== 0 , ys2321== 1),
Or(ys2322== 0 , ys2322== 1),
Or(ys2331== 0 , ys2331== 1),
Or(ys2332== 0 , ys2332== 1),
Or(ys2341== 0 , ys2341== 1),
Or(ys2342== 0 , ys2342== 1),
Or(ys2351== 0 , ys2351== 1),
Or(ys2352== 0 , ys2352== 1),
Or(ys2361== 0 , ys2361== 1),
Or(ys2362== 0 , ys2362== 1),
Or(ys2371== 0 , ys2371== 1),
Or(ys2372== 0 , ys2372== 1),
Or(ys2381== 0 , ys2381== 1),
Or(ys2382== 0 , ys2382== 1),
Or(ys2391== 0 , ys2391== 1),
Or(ys2392== 0 , ys2392== 1),
Or(ys2401== 0 , ys2401== 1),
Or(ys2402== 0 , ys2402== 1),
Or(ys2411== 0 , ys2411== 1),
Or(ys2412== 0 , ys2412== 1),
Or(ys2421== 0 , ys2421== 1),
Or(ys2422== 0 , ys2422== 1),
Or(ys2431== 0 , ys2431== 1),
Or(ys2432== 0 , ys2432== 1),
Or(ys2441== 0 , ys2441== 1),
Or(ys2442== 0 , ys2442== 1),
Or(ys2451== 0 , ys2451== 1),
Or(ys2452== 0 , ys2452== 1),
Or(ys2461== 0 , ys2461== 1),
Or(ys2462== 0 , ys2462== 1),
Or(ys2471== 0 , ys2471== 1),
Or(ys2472== 0 , ys2472== 1),
Or(ys2481== 0 , ys2481== 1),
Or(ys2482== 0 , ys2482== 1),
Or(ys2491== 0 , ys2491== 1),
Or(ys2492== 0 , ys2492== 1),
Or(ys2501== 0 , ys2501== 1),
Or(ys2502== 0 , ys2502== 1),
Or(ys2511== 0 , ys2511== 1),
Or(ys2512== 0 , ys2512== 1),
Or(ys2521== 0 , ys2521== 1),
Or(ys2522== 0 , ys2522== 1),
Or(ys2531== 0 , ys2531== 1),
Or(ys2532== 0 , ys2532== 1),
Or(ys2541== 0 , ys2541== 1),
Or(ys2542== 0 , ys2542== 1),
Or(ys2551== 0 , ys2551== 1),
Or(ys2552== 0 , ys2552== 1),
Or(ys2561== 0 , ys2561== 1),
Or(ys2562== 0 , ys2562== 1),
Or(ys2571== 0 , ys2571== 1),
Or(ys2572== 0 , ys2572== 1),
Or(ys2581== 0 , ys2581== 1),
Or(ys2582== 0 , ys2582== 1),
Or(ys2591== 0 , ys2591== 1),
Or(ys2592== 0 , ys2592== 1),
Or(ys2601== 0 , ys2601== 1),
Or(ys2602== 0 , ys2602== 1),
Or(ys2611== 0 , ys2611== 1),
Or(ys2612== 0 , ys2612== 1),
Or(ys2621== 0 , ys2621== 1),
Or(ys2622== 0 , ys2622== 1),
Or(ys2631== 0 , ys2631== 1),
Or(ys2632== 0 , ys2632== 1),
Or(ys2641== 0 , ys2641== 1),
Or(ys2642== 0 , ys2642== 1),
Or(ys2651== 0 , ys2651== 1),
Or(ys2652== 0 , ys2652== 1),
Or(ys2661== 0 , ys2661== 1),
Or(ys2662== 0 , ys2662== 1),
Or(ys2671== 0 , ys2671== 1),
Or(ys2672== 0 , ys2672== 1),
Or(ys2681== 0 , ys2681== 1),
Or(ys2682== 0 , ys2682== 1),
Or(ys2691== 0 , ys2691== 1),
Or(ys2692== 0 , ys2692== 1),
Or(ys2701== 0 , ys2701== 1),
Or(ys2702== 0 , ys2702== 1),
Or(ys2711== 0 , ys2711== 1),
Or(ys2712== 0 , ys2712== 1),
Or(ys2721== 0 , ys2721== 1),
Or(ys2722== 0 , ys2722== 1),
Or(ys2731== 0 , ys2731== 1),
Or(ys2732== 0 , ys2732== 1),
Or(ys2741== 0 , ys2741== 1),
Or(ys2742== 0 , ys2742== 1),
Or(ys2751== 0 , ys2751== 1),
Or(ys2752== 0 , ys2752== 1),
Or(ys2761== 0 , ys2761== 1),
Or(ys2762== 0 , ys2762== 1),
Or(ys2771== 0 , ys2771== 1),
Or(ys2772== 0 , ys2772== 1),
Or(ys2781== 0 , ys2781== 1),
Or(ys2782== 0 , ys2782== 1),
Or(ys2791== 0 , ys2791== 1),
Or(ys2792== 0 , ys2792== 1),
Or(ys2801== 0 , ys2801== 1),
Or(ys2802== 0 , ys2802== 1),
Or(ys2811== 0 , ys2811== 1),
Or(ys2812== 0 , ys2812== 1),
Or(ys2821== 0 , ys2821== 1),
Or(ys2822== 0 , ys2822== 1),
Or(ys2831== 0 , ys2831== 1),
Or(ys2832== 0 , ys2832== 1),
Or(ys2841== 0 , ys2841== 1),
Or(ys2842== 0 , ys2842== 1),
Or(ys2851== 0 , ys2851== 1),
Or(ys2852== 0 , ys2852== 1),
Or(ys2861== 0 , ys2861== 1),
Or(ys2862== 0 , ys2862== 1),
Or(ys2871== 0 , ys2871== 1),
Or(ys2872== 0 , ys2872== 1),
Or(ys2881== 0 , ys2881== 1),
Or(ys2882== 0 , ys2882== 1),
Or(ys2891== 0 , ys2891== 1),
Or(ys2892== 0 , ys2892== 1),
Or(ys2901== 0 , ys2901== 1),
Or(ys2902== 0 , ys2902== 1),
Or(ys2911== 0 , ys2911== 1),
Or(ys2912== 0 , ys2912== 1),
Or(ys2921== 0 , ys2921== 1),
Or(ys2922== 0 , ys2922== 1),
Or(ys2931== 0 , ys2931== 1),
Or(ys2932== 0 , ys2932== 1),
Or(ys2941== 0 , ys2941== 1),
Or(ys2942== 0 , ys2942== 1),
Or(ys2951== 0 , ys2951== 1),
Or(ys2952== 0 , ys2952== 1),
Or(ys2961== 0 , ys2961== 1),
Or(ys2962== 0 , ys2962== 1),
Or(ys2971== 0 , ys2971== 1),
Or(ys2972== 0 , ys2972== 1),
Or(ys2981== 0 , ys2981== 1),
Or(ys2982== 0 , ys2982== 1),
Or(ys2991== 0 , ys2991== 1),
Or(ys2992== 0 , ys2992== 1),
Or(ys3001== 0 , ys3001== 1),
Or(ys3002== 0 , ys3002== 1),
Or(ys3011== 0 , ys3011== 1),
Or(ys3012== 0 , ys3012== 1),
Or(ys3021== 0 , ys3021== 1),
Or(ys3022== 0 , ys3022== 1),
Or(ys3031== 0 , ys3031== 1),
Or(ys3032== 0 , ys3032== 1),
Or(ys3041== 0 , ys3041== 1),
Or(ys3042== 0 , ys3042== 1),
Or(ys3051== 0 , ys3051== 1),
Or(ys3052== 0 , ys3052== 1),
Or(ys3061== 0 , ys3061== 1),
Or(ys3062== 0 , ys3062== 1),
Or(ys3071== 0 , ys3071== 1),
Or(ys3072== 0 , ys3072== 1),
Or(ys3081== 0 , ys3081== 1),
Or(ys3082== 0 , ys3082== 1),
Or(ys3091== 0 , ys3091== 1),
Or(ys3092== 0 , ys3092== 1),
Or(ys3101== 0 , ys3101== 1),
Or(ys3102== 0 , ys3102== 1),
Or(ys3111== 0 , ys3111== 1),
Or(ys3112== 0 , ys3112== 1),
Or(ys3121== 0 , ys3121== 1),
Or(ys3122== 0 , ys3122== 1),
Or(ys3131== 0 , ys3131== 1),
Or(ys3132== 0 , ys3132== 1),
Or(ys3141== 0 , ys3141== 1),
Or(ys3142== 0 , ys3142== 1),
Or(ys3151== 0 , ys3151== 1),
Or(ys3152== 0 , ys3152== 1),
Or(ys3161== 0 , ys3161== 1),
Or(ys3162== 0 , ys3162== 1),
Or(ys3171== 0 , ys3171== 1),
Or(ys3172== 0 , ys3172== 1),
Or(ys3181== 0 , ys3181== 1),
Or(ys3182== 0 , ys3182== 1),
Or(ys3191== 0 , ys3191== 1),
Or(ys3192== 0 , ys3192== 1),
Or(ys3201== 0 , ys3201== 1),
Or(ys3202== 0 , ys3202== 1),
Or(ys3211== 0 , ys3211== 1),
Or(ys3212== 0 , ys3212== 1),
Or(ys3221== 0 , ys3221== 1),
Or(ys3222== 0 , ys3222== 1),
Or(ys3231== 0 , ys3231== 1),
Or(ys3232== 0 , ys3232== 1),
Or(ys3241== 0 , ys3241== 1),
Or(ys3242== 0 , ys3242== 1),
Or(ys3251== 0 , ys3251== 1),
Or(ys3252== 0 , ys3252== 1),
Or(ys3261== 0 , ys3261== 1),
Or(ys3262== 0 , ys3262== 1),
Or(ys3271== 0 , ys3271== 1),
Or(ys3272== 0 , ys3272== 1),
Or(ys3281== 0 , ys3281== 1),
Or(ys3282== 0 , ys3282== 1),
Or(ys3291== 0 , ys3291== 1),
Or(ys3292== 0 , ys3292== 1),
Or(ys3301== 0 , ys3301== 1),
Or(ys3302== 0 , ys3302== 1),
Or(ys3311== 0 , ys3311== 1),
Or(ys3312== 0 , ys3312== 1),
Or(ys3321== 0 , ys3321== 1),
Or(ys3322== 0 , ys3322== 1),
Or(ys3331== 0 , ys3331== 1),
Or(ys3332== 0 , ys3332== 1),
Or(ys3341== 0 , ys3341== 1),
Or(ys3342== 0 , ys3342== 1),
Or(ys3351== 0 , ys3351== 1),
Or(ys3352== 0 , ys3352== 1),
Or(ys3361== 0 , ys3361== 1),
Or(ys3362== 0 , ys3362== 1),
Or(ys3371== 0 , ys3371== 1),
Or(ys3372== 0 , ys3372== 1),
Or(ys3381== 0 , ys3381== 1),
Or(ys3382== 0 , ys3382== 1),
Or(ys3391== 0 , ys3391== 1),
Or(ys3392== 0 , ys3392== 1),
Or(ys3401== 0 , ys3401== 1),
Or(ys3402== 0 , ys3402== 1),
Or(ys3411== 0 , ys3411== 1),
Or(ys3412== 0 , ys3412== 1),
Or(ys3421== 0 , ys3421== 1),
Or(ys3422== 0 , ys3422== 1),
Or(ys3431== 0 , ys3431== 1),
Or(ys3432== 0 , ys3432== 1),
Or(ys3441== 0 , ys3441== 1),
Or(ys3442== 0 , ys3442== 1),
Or(ys3451== 0 , ys3451== 1),
Or(ys3452== 0 , ys3452== 1),
Or(ys3461== 0 , ys3461== 1),
Or(ys3462== 0 , ys3462== 1),
Or(ys3471== 0 , ys3471== 1),
Or(ys3472== 0 , ys3472== 1),
Or(ys3481== 0 , ys3481== 1),
Or(ys3482== 0 , ys3482== 1),
Or(ys3491== 0 , ys3491== 1),
Or(ys3492== 0 , ys3492== 1),
Or(ys3501== 0 , ys3501== 1),
Or(ys3502== 0 , ys3502== 1),
Or(ys3511== 0 , ys3511== 1),
Or(ys3512== 0 , ys3512== 1),
Or(ys3521== 0 , ys3521== 1),
Or(ys3522== 0 , ys3522== 1),
Or(ys3531== 0 , ys3531== 1),
Or(ys3532== 0 , ys3532== 1),
Or(ys3541== 0 , ys3541== 1),
Or(ys3542== 0 , ys3542== 1),
Or(ys3551== 0 , ys3551== 1),
Or(ys3552== 0 , ys3552== 1),
Or(ys3561== 0 , ys3561== 1),
Or(ys3562== 0 , ys3562== 1),
Or(ys3571== 0 , ys3571== 1),
Or(ys3572== 0 , ys3572== 1),
Or(ys3581== 0 , ys3581== 1),
Or(ys3582== 0 , ys3582== 1),
Or(ys3591== 0 , ys3591== 1),
Or(ys3592== 0 , ys3592== 1),
Or(ys3601== 0 , ys3601== 1),
Or(ys3602== 0 , ys3602== 1),
Or(ys3611== 0 , ys3611== 1),
Or(ys3612== 0 , ys3612== 1),
Or(ys3621== 0 , ys3621== 1),
Or(ys3622== 0 , ys3622== 1),
Or(ys3631== 0 , ys3631== 1),
Or(ys3632== 0 , ys3632== 1),
Or(ys3641== 0 , ys3641== 1),
Or(ys3642== 0 , ys3642== 1),
Or(ys3651== 0 , ys3651== 1),
Or(ys3652== 0 , ys3652== 1),
Or(ys3661== 0 , ys3661== 1),
Or(ys3662== 0 , ys3662== 1),
Or(ys3671== 0 , ys3671== 1),
Or(ys3672== 0 , ys3672== 1),
Or(ys3681== 0 , ys3681== 1),
Or(ys3682== 0 , ys3682== 1),
Or(ys3691== 0 , ys3691== 1),
Or(ys3692== 0 , ys3692== 1),
Or(ys3701== 0 , ys3701== 1),
Or(ys3702== 0 , ys3702== 1),
Or(ys3711== 0 , ys3711== 1),
Or(ys3712== 0 , ys3712== 1),
Or(ys3721== 0 , ys3721== 1),
Or(ys3722== 0 , ys3722== 1),
Or(ys3731== 0 , ys3731== 1),
Or(ys3732== 0 , ys3732== 1),
Or(ys3741== 0 , ys3741== 1),
Or(ys3742== 0 , ys3742== 1),
Or(ys3751== 0 , ys3751== 1),
Or(ys3752== 0 , ys3752== 1),
Or(ys3761== 0 , ys3761== 1),
Or(ys3762== 0 , ys3762== 1),
# Every state should be mapped to exactly one equivalence class
ys01 + ys02 == 1,
ys11 + ys12 == 1,
ys21 + ys22 == 1,
ys31 + ys32 == 1,
ys41 + ys42 == 1,
ys51 + ys52 == 1,
ys61 + ys62 == 1,
ys71 + ys72 == 1,
ys81 + ys82 == 1,
ys91 + ys92 == 1,
ys101 + ys102 == 1,
ys111 + ys112 == 1,
ys121 + ys122 == 1,
ys131 + ys132 == 1,
ys141 + ys142 == 1,
ys151 + ys152 == 1,
ys161 + ys162 == 1,
ys171 + ys172 == 1,
ys181 + ys182 == 1,
ys191 + ys192 == 1,
ys201 + ys202 == 1,
ys211 + ys212 == 1,
ys221 + ys222 == 1,
ys231 + ys232 == 1,
ys241 + ys242 == 1,
ys251 + ys252 == 1,
ys261 + ys262 == 1,
ys271 + ys272 == 1,
ys281 + ys282 == 1,
ys291 + ys292 == 1,
ys301 + ys302 == 1,
ys311 + ys312 == 1,
ys321 + ys322 == 1,
ys331 + ys332 == 1,
ys341 + ys342 == 1,
ys351 + ys352 == 1,
ys361 + ys362 == 1,
ys371 + ys372 == 1,
ys381 + ys382 == 1,
ys391 + ys392 == 1,
ys401 + ys402 == 1,
ys411 + ys412 == 1,
ys421 + ys422 == 1,
ys431 + ys432 == 1,
ys441 + ys442 == 1,
ys451 + ys452 == 1,
ys461 + ys462 == 1,
ys471 + ys472 == 1,
ys481 + ys482 == 1,
ys491 + ys492 == 1,
ys501 + ys502 == 1,
ys511 + ys512 == 1,
ys521 + ys522 == 1,
ys531 + ys532 == 1,
ys541 + ys542 == 1,
ys551 + ys552 == 1,
ys561 + ys562 == 1,
ys571 + ys572 == 1,
ys581 + ys582 == 1,
ys591 + ys592 == 1,
ys601 + ys602 == 1,
ys611 + ys612 == 1,
ys621 + ys622 == 1,
ys631 + ys632 == 1,
ys641 + ys642 == 1,
ys651 + ys652 == 1,
ys661 + ys662 == 1,
ys671 + ys672 == 1,
ys681 + ys682 == 1,
ys691 + ys692 == 1,
ys701 + ys702 == 1,
ys711 + ys712 == 1,
ys721 + ys722 == 1,
ys731 + ys732 == 1,
ys741 + ys742 == 1,
ys751 + ys752 == 1,
ys761 + ys762 == 1,
ys771 + ys772 == 1,
ys781 + ys782 == 1,
ys791 + ys792 == 1,
ys801 + ys802 == 1,
ys811 + ys812 == 1,
ys821 + ys822 == 1,
ys831 + ys832 == 1,
ys841 + ys842 == 1,
ys851 + ys852 == 1,
ys861 + ys862 == 1,
ys871 + ys872 == 1,
ys881 + ys882 == 1,
ys891 + ys892 == 1,
ys901 + ys902 == 1,
ys911 + ys912 == 1,
ys921 + ys922 == 1,
ys931 + ys932 == 1,
ys941 + ys942 == 1,
ys951 + ys952 == 1,
ys961 + ys962 == 1,
ys971 + ys972 == 1,
ys981 + ys982 == 1,
ys991 + ys992 == 1,
ys1001 + ys1002 == 1,
ys1011 + ys1012 == 1,
ys1021 + ys1022 == 1,
ys1031 + ys1032 == 1,
ys1041 + ys1042 == 1,
ys1051 + ys1052 == 1,
ys1061 + ys1062 == 1,
ys1071 + ys1072 == 1,
ys1081 + ys1082 == 1,
ys1091 + ys1092 == 1,
ys1101 + ys1102 == 1,
ys1111 + ys1112 == 1,
ys1121 + ys1122 == 1,
ys1131 + ys1132 == 1,
ys1141 + ys1142 == 1,
ys1151 + ys1152 == 1,
ys1161 + ys1162 == 1,
ys1171 + ys1172 == 1,
ys1181 + ys1182 == 1,
ys1191 + ys1192 == 1,
ys1201 + ys1202 == 1,
ys1211 + ys1212 == 1,
ys1221 + ys1222 == 1,
ys1231 + ys1232 == 1,
ys1241 + ys1242 == 1,
ys1251 + ys1252 == 1,
ys1261 + ys1262 == 1,
ys1271 + ys1272 == 1,
ys1281 + ys1282 == 1,
ys1291 + ys1292 == 1,
ys1301 + ys1302 == 1,
ys1311 + ys1312 == 1,
ys1321 + ys1322 == 1,
ys1331 + ys1332 == 1,
ys1341 + ys1342 == 1,
ys1351 + ys1352 == 1,
ys1361 + ys1362 == 1,
ys1371 + ys1372 == 1,
ys1381 + ys1382 == 1,
ys1391 + ys1392 == 1,
ys1401 + ys1402 == 1,
ys1411 + ys1412 == 1,
ys1421 + ys1422 == 1,
ys1431 + ys1432 == 1,
ys1441 + ys1442 == 1,
ys1451 + ys1452 == 1,
ys1461 + ys1462 == 1,
ys1471 + ys1472 == 1,
ys1481 + ys1482 == 1,
ys1491 + ys1492 == 1,
ys1501 + ys1502 == 1,
ys1511 + ys1512 == 1,
ys1521 + ys1522 == 1,
ys1531 + ys1532 == 1,
ys1541 + ys1542 == 1,
ys1551 + ys1552 == 1,
ys1561 + ys1562 == 1,
ys1571 + ys1572 == 1,
ys1581 + ys1582 == 1,
ys1591 + ys1592 == 1,
ys1601 + ys1602 == 1,
ys1611 + ys1612 == 1,
ys1621 + ys1622 == 1,
ys1631 + ys1632 == 1,
ys1641 + ys1642 == 1,
ys1651 + ys1652 == 1,
ys1661 + ys1662 == 1,
ys1671 + ys1672 == 1,
ys1681 + ys1682 == 1,
ys1691 + ys1692 == 1,
ys1701 + ys1702 == 1,
ys1711 + ys1712 == 1,
ys1721 + ys1722 == 1,
ys1731 + ys1732 == 1,
ys1741 + ys1742 == 1,
ys1751 + ys1752 == 1,
ys1761 + ys1762 == 1,
ys1771 + ys1772 == 1,
ys1781 + ys1782 == 1,
ys1791 + ys1792 == 1,
ys1801 + ys1802 == 1,
ys1811 + ys1812 == 1,
ys1821 + ys1822 == 1,
ys1831 + ys1832 == 1,
ys1841 + ys1842 == 1,
ys1851 + ys1852 == 1,
ys1861 + ys1862 == 1,
ys1871 + ys1872 == 1,
ys1891 + ys1892 == 1,
ys1901 + ys1902 == 1,
ys1911 + ys1912 == 1,
ys1921 + ys1922 == 1,
ys1931 + ys1932 == 1,
ys1941 + ys1942 == 1,
ys1951 + ys1952 == 1,
ys1961 + ys1962 == 1,
ys1971 + ys1972 == 1,
ys1981 + ys1982 == 1,
ys1991 + ys1992 == 1,
ys2001 + ys2002 == 1,
ys2011 + ys2012 == 1,
ys2021 + ys2022 == 1,
ys2031 + ys2032 == 1,
ys2041 + ys2042 == 1,
ys2051 + ys2052 == 1,
ys2061 + ys2062 == 1,
ys2071 + ys2072 == 1,
ys2081 + ys2082 == 1,
ys2091 + ys2092 == 1,
ys2101 + ys2102 == 1,
ys2111 + ys2112 == 1,
ys2121 + ys2122 == 1,
ys2131 + ys2132 == 1,
ys2141 + ys2142 == 1,
ys2151 + ys2152 == 1,
ys2161 + ys2162 == 1,
ys2171 + ys2172 == 1,
ys2181 + ys2182 == 1,
ys2191 + ys2192 == 1,
ys2201 + ys2202 == 1,
ys2211 + ys2212 == 1,
ys2221 + ys2222 == 1,
ys2231 + ys2232 == 1,
ys2241 + ys2242 == 1,
ys2251 + ys2252 == 1,
ys2261 + ys2262 == 1,
ys2271 + ys2272 == 1,
ys2281 + ys2282 == 1,
ys2291 + ys2292 == 1,
ys2301 + ys2302 == 1,
ys2311 + ys2312 == 1,
ys2321 + ys2322 == 1,
ys2331 + ys2332 == 1,
ys2341 + ys2342 == 1,
ys2351 + ys2352 == 1,
ys2361 + ys2362 == 1,
ys2371 + ys2372 == 1,
ys2381 + ys2382 == 1,
ys2391 + ys2392 == 1,
ys2401 + ys2402 == 1,
ys2411 + ys2412 == 1,
ys2421 + ys2422 == 1,
ys2431 + ys2432 == 1,
ys2441 + ys2442 == 1,
ys2451 + ys2452 == 1,
ys2461 + ys2462 == 1,
ys2471 + ys2472 == 1,
ys2481 + ys2482 == 1,
ys2491 + ys2492 == 1,
ys2501 + ys2502 == 1,
ys2511 + ys2512 == 1,
ys2521 + ys2522 == 1,
ys2531 + ys2532 == 1,
ys2541 + ys2542 == 1,
ys2551 + ys2552 == 1,
ys2561 + ys2562 == 1,
ys2571 + ys2572 == 1,
ys2581 + ys2582 == 1,
ys2591 + ys2592 == 1,
ys2601 + ys2602 == 1,
ys2611 + ys2612 == 1,
ys2621 + ys2622 == 1,
ys2631 + ys2632 == 1,
ys2641 + ys2642 == 1,
ys2651 + ys2652 == 1,
ys2661 + ys2662 == 1,
ys2671 + ys2672 == 1,
ys2681 + ys2682 == 1,
ys2691 + ys2692 == 1,
ys2701 + ys2702 == 1,
ys2711 + ys2712 == 1,
ys2721 + ys2722 == 1,
ys2731 + ys2732 == 1,
ys2741 + ys2742 == 1,
ys2751 + ys2752 == 1,
ys2761 + ys2762 == 1,
ys2771 + ys2772 == 1,
ys2781 + ys2782 == 1,
ys2791 + ys2792 == 1,
ys2801 + ys2802 == 1,
ys2811 + ys2812 == 1,
ys2821 + ys2822 == 1,
ys2831 + ys2832 == 1,
ys2841 + ys2842 == 1,
ys2851 + ys2852 == 1,
ys2861 + ys2862 == 1,
ys2871 + ys2872 == 1,
ys2881 + ys2882 == 1,
ys2891 + ys2892 == 1,
ys2901 + ys2902 == 1,
ys2911 + ys2912 == 1,
ys2921 + ys2922 == 1,
ys2931 + ys2932 == 1,
ys2941 + ys2942 == 1,
ys2951 + ys2952 == 1,
ys2961 + ys2962 == 1,
ys2971 + ys2972 == 1,
ys2981 + ys2982 == 1,
ys2991 + ys2992 == 1,
ys3001 + ys3002 == 1,
ys3011 + ys3012 == 1,
ys3021 + ys3022 == 1,
ys3031 + ys3032 == 1,
ys3041 + ys3042 == 1,
ys3051 + ys3052 == 1,
ys3061 + ys3062 == 1,
ys3071 + ys3072 == 1,
ys3081 + ys3082 == 1,
ys3091 + ys3092 == 1,
ys3101 + ys3102 == 1,
ys3111 + ys3112 == 1,
ys3121 + ys3122 == 1,
ys3131 + ys3132 == 1,
ys3141 + ys3142 == 1,
ys3151 + ys3152 == 1,
ys3161 + ys3162 == 1,
ys3171 + ys3172 == 1,
ys3181 + ys3182 == 1,
ys3191 + ys3192 == 1,
ys3201 + ys3202 == 1,
ys3211 + ys3212 == 1,
ys3221 + ys3222 == 1,
ys3231 + ys3232 == 1,
ys3241 + ys3242 == 1,
ys3251 + ys3252 == 1,
ys3261 + ys3262 == 1,
ys3271 + ys3272 == 1,
ys3281 + ys3282 == 1,
ys3291 + ys3292 == 1,
ys3301 + ys3302 == 1,
ys3311 + ys3312 == 1,
ys3321 + ys3322 == 1,
ys3331 + ys3332 == 1,
ys3341 + ys3342 == 1,
ys3351 + ys3352 == 1,
ys3361 + ys3362 == 1,
ys3371 + ys3372 == 1,
ys3381 + ys3382 == 1,
ys3391 + ys3392 == 1,
ys3401 + ys3402 == 1,
ys3411 + ys3412 == 1,
ys3421 + ys3422 == 1,
ys3431 + ys3432 == 1,
ys3441 + ys3442 == 1,
ys3451 + ys3452 == 1,
ys3461 + ys3462 == 1,
ys3471 + ys3472 == 1,
ys3481 + ys3482 == 1,
ys3491 + ys3492 == 1,
ys3501 + ys3502 == 1,
ys3511 + ys3512 == 1,
ys3521 + ys3522 == 1,
ys3531 + ys3532 == 1,
ys3541 + ys3542 == 1,
ys3551 + ys3552 == 1,
ys3561 + ys3562 == 1,
ys3571 + ys3572 == 1,
ys3581 + ys3582 == 1,
ys3591 + ys3592 == 1,
ys3601 + ys3602 == 1,
ys3611 + ys3612 == 1,
ys3621 + ys3622 == 1,
ys3631 + ys3632 == 1,
ys3641 + ys3642 == 1,
ys3651 + ys3652 == 1,
ys3661 + ys3662 == 1,
ys3671 + ys3672 == 1,
ys3681 + ys3682 == 1,
ys3691 + ys3692 == 1,
ys3701 + ys3702 == 1,
ys3711 + ys3712 == 1,
ys3721 + ys3722 == 1,
ys3731 + ys3732 == 1,
ys3741 + ys3742 == 1,
ys3751 + ys3752 == 1,
ys3761 + ys3762 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')