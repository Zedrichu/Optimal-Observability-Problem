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
pi377 = Real('pi377')
pi378 = Real('pi378')
pi379 = Real('pi379')
pi380 = Real('pi380')
pi381 = Real('pi381')
pi382 = Real('pi382')
pi383 = Real('pi383')
pi384 = Real('pi384')
pi385 = Real('pi385')
pi386 = Real('pi386')
pi387 = Real('pi387')
pi388 = Real('pi388')
pi389 = Real('pi389')
pi390 = Real('pi390')
pi391 = Real('pi391')
pi392 = Real('pi392')
pi393 = Real('pi393')
pi394 = Real('pi394')
pi395 = Real('pi395')
pi396 = Real('pi396')
pi397 = Real('pi397')
pi398 = Real('pi398')
pi399 = Real('pi399')
pi400 = Real('pi400')
pi401 = Real('pi401')
pi402 = Real('pi402')
pi403 = Real('pi403')
pi404 = Real('pi404')
pi405 = Real('pi405')
pi406 = Real('pi406')
pi407 = Real('pi407')
pi408 = Real('pi408')
pi409 = Real('pi409')
pi410 = Real('pi410')
pi411 = Real('pi411')
pi412 = Real('pi412')
pi413 = Real('pi413')
pi414 = Real('pi414')
pi415 = Real('pi415')
pi416 = Real('pi416')
pi417 = Real('pi417')
pi418 = Real('pi418')
pi419 = Real('pi419')
pi420 = Real('pi420')
pi421 = Real('pi421')
pi422 = Real('pi422')
pi423 = Real('pi423')
pi424 = Real('pi424')
pi425 = Real('pi425')
pi426 = Real('pi426')
pi427 = Real('pi427')
pi428 = Real('pi428')
pi429 = Real('pi429')
pi430 = Real('pi430')
pi431 = Real('pi431')
pi432 = Real('pi432')
pi433 = Real('pi433')
pi434 = Real('pi434')
pi435 = Real('pi435')
pi436 = Real('pi436')
pi437 = Real('pi437')
pi438 = Real('pi438')
pi439 = Real('pi439')
pi440 = Real('pi440')
pi441 = Real('pi441')
pi442 = Real('pi442')
pi443 = Real('pi443')
pi444 = Real('pi444')
pi445 = Real('pi445')
pi446 = Real('pi446')
pi447 = Real('pi447')
pi448 = Real('pi448')
pi449 = Real('pi449')
pi450 = Real('pi450')
pi451 = Real('pi451')
pi452 = Real('pi452')
pi453 = Real('pi453')
pi454 = Real('pi454')
pi455 = Real('pi455')
pi456 = Real('pi456')
pi457 = Real('pi457')
pi458 = Real('pi458')
pi459 = Real('pi459')
pi460 = Real('pi460')
pi461 = Real('pi461')
pi462 = Real('pi462')
pi463 = Real('pi463')
pi464 = Real('pi464')
pi465 = Real('pi465')
pi466 = Real('pi466')
pi467 = Real('pi467')
pi468 = Real('pi468')
pi469 = Real('pi469')
pi470 = Real('pi470')
pi471 = Real('pi471')
pi472 = Real('pi472')
pi473 = Real('pi473')
pi474 = Real('pi474')
pi475 = Real('pi475')
pi476 = Real('pi476')
pi477 = Real('pi477')
pi478 = Real('pi478')
pi479 = Real('pi479')
pi480 = Real('pi480')
pi481 = Real('pi481')
pi482 = Real('pi482')
pi483 = Real('pi483')
pi484 = Real('pi484')
pi485 = Real('pi485')
pi486 = Real('pi486')
pi487 = Real('pi487')
pi488 = Real('pi488')
pi489 = Real('pi489')
pi490 = Real('pi490')
pi491 = Real('pi491')
pi492 = Real('pi492')
pi493 = Real('pi493')
pi494 = Real('pi494')
pi495 = Real('pi495')
pi496 = Real('pi496')
pi497 = Real('pi497')
pi498 = Real('pi498')
pi499 = Real('pi499')
pi500 = Real('pi500')
pi501 = Real('pi501')
pi502 = Real('pi502')
pi503 = Real('pi503')
pi504 = Real('pi504')
pi505 = Real('pi505')
pi506 = Real('pi506')
pi507 = Real('pi507')
pi508 = Real('pi508')
pi509 = Real('pi509')
pi510 = Real('pi510')
pi511 = Real('pi511')
pi512 = Real('pi512')
pi513 = Real('pi513')
pi514 = Real('pi514')
pi515 = Real('pi515')
pi516 = Real('pi516')
pi517 = Real('pi517')
pi518 = Real('pi518')
pi519 = Real('pi519')
pi520 = Real('pi520')
pi521 = Real('pi521')
pi522 = Real('pi522')
pi523 = Real('pi523')
pi524 = Real('pi524')
pi525 = Real('pi525')
pi526 = Real('pi526')
pi527 = Real('pi527')
pi528 = Real('pi528')
pi529 = Real('pi529')
pi530 = Real('pi530')
pi531 = Real('pi531')
pi532 = Real('pi532')
pi533 = Real('pi533')
pi534 = Real('pi534')
pi535 = Real('pi535')
pi536 = Real('pi536')
pi537 = Real('pi537')
pi538 = Real('pi538')
pi539 = Real('pi539')
pi540 = Real('pi540')
pi541 = Real('pi541')
pi542 = Real('pi542')
pi543 = Real('pi543')
pi544 = Real('pi544')
pi545 = Real('pi545')
pi546 = Real('pi546')
pi547 = Real('pi547')
pi548 = Real('pi548')
pi549 = Real('pi549')
pi550 = Real('pi550')
pi551 = Real('pi551')
pi552 = Real('pi552')
pi553 = Real('pi553')
pi554 = Real('pi554')
pi555 = Real('pi555')
pi556 = Real('pi556')
pi557 = Real('pi557')
pi558 = Real('pi558')
pi559 = Real('pi559')
pi560 = Real('pi560')
pi561 = Real('pi561')
pi562 = Real('pi562')
pi563 = Real('pi563')
pi564 = Real('pi564')
pi565 = Real('pi565')
pi566 = Real('pi566')
pi567 = Real('pi567')
pi568 = Real('pi568')
pi569 = Real('pi569')
pi570 = Real('pi570')
pi571 = Real('pi571')
pi572 = Real('pi572')
pi573 = Real('pi573')
pi574 = Real('pi574')
pi575 = Real('pi575')
pi576 = Real('pi576')
pi577 = Real('pi577')
pi578 = Real('pi578')
pi579 = Real('pi579')
pi580 = Real('pi580')
pi581 = Real('pi581')
pi582 = Real('pi582')
pi583 = Real('pi583')
pi584 = Real('pi584')
pi585 = Real('pi585')
pi586 = Real('pi586')
pi587 = Real('pi587')
pi588 = Real('pi588')
pi589 = Real('pi589')
pi590 = Real('pi590')
pi591 = Real('pi591')
pi592 = Real('pi592')
pi593 = Real('pi593')
pi594 = Real('pi594')
pi595 = Real('pi595')
pi596 = Real('pi596')
pi597 = Real('pi597')
pi598 = Real('pi598')
pi599 = Real('pi599')
pi600 = Real('pi600')
pi601 = Real('pi601')
pi602 = Real('pi602')
pi603 = Real('pi603')
pi604 = Real('pi604')
pi605 = Real('pi605')
pi606 = Real('pi606')
pi607 = Real('pi607')
pi608 = Real('pi608')
pi609 = Real('pi609')
pi610 = Real('pi610')
pi611 = Real('pi611')
pi612 = Real('pi612')
pi613 = Real('pi613')
pi614 = Real('pi614')
pi615 = Real('pi615')
pi616 = Real('pi616')
pi617 = Real('pi617')
pi618 = Real('pi618')
pi619 = Real('pi619')
pi620 = Real('pi620')
pi621 = Real('pi621')
pi622 = Real('pi622')
pi623 = Real('pi623')
pi624 = Real('pi624')

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
ys1881 = Real('ys1881')
ys1882 = Real('ys1882')
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
ys3771 = Real('ys3771')
ys3772 = Real('ys3772')
ys3781 = Real('ys3781')
ys3782 = Real('ys3782')
ys3791 = Real('ys3791')
ys3792 = Real('ys3792')
ys3801 = Real('ys3801')
ys3802 = Real('ys3802')
ys3811 = Real('ys3811')
ys3812 = Real('ys3812')
ys3821 = Real('ys3821')
ys3822 = Real('ys3822')
ys3831 = Real('ys3831')
ys3832 = Real('ys3832')
ys3841 = Real('ys3841')
ys3842 = Real('ys3842')
ys3851 = Real('ys3851')
ys3852 = Real('ys3852')
ys3861 = Real('ys3861')
ys3862 = Real('ys3862')
ys3871 = Real('ys3871')
ys3872 = Real('ys3872')
ys3881 = Real('ys3881')
ys3882 = Real('ys3882')
ys3891 = Real('ys3891')
ys3892 = Real('ys3892')
ys3901 = Real('ys3901')
ys3902 = Real('ys3902')
ys3911 = Real('ys3911')
ys3912 = Real('ys3912')
ys3921 = Real('ys3921')
ys3922 = Real('ys3922')
ys3931 = Real('ys3931')
ys3932 = Real('ys3932')
ys3941 = Real('ys3941')
ys3942 = Real('ys3942')
ys3951 = Real('ys3951')
ys3952 = Real('ys3952')
ys3961 = Real('ys3961')
ys3962 = Real('ys3962')
ys3971 = Real('ys3971')
ys3972 = Real('ys3972')
ys3981 = Real('ys3981')
ys3982 = Real('ys3982')
ys3991 = Real('ys3991')
ys3992 = Real('ys3992')
ys4001 = Real('ys4001')
ys4002 = Real('ys4002')
ys4011 = Real('ys4011')
ys4012 = Real('ys4012')
ys4021 = Real('ys4021')
ys4022 = Real('ys4022')
ys4031 = Real('ys4031')
ys4032 = Real('ys4032')
ys4041 = Real('ys4041')
ys4042 = Real('ys4042')
ys4051 = Real('ys4051')
ys4052 = Real('ys4052')
ys4061 = Real('ys4061')
ys4062 = Real('ys4062')
ys4071 = Real('ys4071')
ys4072 = Real('ys4072')
ys4081 = Real('ys4081')
ys4082 = Real('ys4082')
ys4091 = Real('ys4091')
ys4092 = Real('ys4092')
ys4101 = Real('ys4101')
ys4102 = Real('ys4102')
ys4111 = Real('ys4111')
ys4112 = Real('ys4112')
ys4121 = Real('ys4121')
ys4122 = Real('ys4122')
ys4131 = Real('ys4131')
ys4132 = Real('ys4132')
ys4141 = Real('ys4141')
ys4142 = Real('ys4142')
ys4151 = Real('ys4151')
ys4152 = Real('ys4152')
ys4161 = Real('ys4161')
ys4162 = Real('ys4162')
ys4171 = Real('ys4171')
ys4172 = Real('ys4172')
ys4181 = Real('ys4181')
ys4182 = Real('ys4182')
ys4191 = Real('ys4191')
ys4192 = Real('ys4192')
ys4201 = Real('ys4201')
ys4202 = Real('ys4202')
ys4211 = Real('ys4211')
ys4212 = Real('ys4212')
ys4221 = Real('ys4221')
ys4222 = Real('ys4222')
ys4231 = Real('ys4231')
ys4232 = Real('ys4232')
ys4241 = Real('ys4241')
ys4242 = Real('ys4242')
ys4251 = Real('ys4251')
ys4252 = Real('ys4252')
ys4261 = Real('ys4261')
ys4262 = Real('ys4262')
ys4271 = Real('ys4271')
ys4272 = Real('ys4272')
ys4281 = Real('ys4281')
ys4282 = Real('ys4282')
ys4291 = Real('ys4291')
ys4292 = Real('ys4292')
ys4301 = Real('ys4301')
ys4302 = Real('ys4302')
ys4311 = Real('ys4311')
ys4312 = Real('ys4312')
ys4321 = Real('ys4321')
ys4322 = Real('ys4322')
ys4331 = Real('ys4331')
ys4332 = Real('ys4332')
ys4341 = Real('ys4341')
ys4342 = Real('ys4342')
ys4351 = Real('ys4351')
ys4352 = Real('ys4352')
ys4361 = Real('ys4361')
ys4362 = Real('ys4362')
ys4371 = Real('ys4371')
ys4372 = Real('ys4372')
ys4381 = Real('ys4381')
ys4382 = Real('ys4382')
ys4391 = Real('ys4391')
ys4392 = Real('ys4392')
ys4401 = Real('ys4401')
ys4402 = Real('ys4402')
ys4411 = Real('ys4411')
ys4412 = Real('ys4412')
ys4421 = Real('ys4421')
ys4422 = Real('ys4422')
ys4431 = Real('ys4431')
ys4432 = Real('ys4432')
ys4441 = Real('ys4441')
ys4442 = Real('ys4442')
ys4451 = Real('ys4451')
ys4452 = Real('ys4452')
ys4461 = Real('ys4461')
ys4462 = Real('ys4462')
ys4471 = Real('ys4471')
ys4472 = Real('ys4472')
ys4481 = Real('ys4481')
ys4482 = Real('ys4482')
ys4491 = Real('ys4491')
ys4492 = Real('ys4492')
ys4501 = Real('ys4501')
ys4502 = Real('ys4502')
ys4511 = Real('ys4511')
ys4512 = Real('ys4512')
ys4521 = Real('ys4521')
ys4522 = Real('ys4522')
ys4531 = Real('ys4531')
ys4532 = Real('ys4532')
ys4541 = Real('ys4541')
ys4542 = Real('ys4542')
ys4551 = Real('ys4551')
ys4552 = Real('ys4552')
ys4561 = Real('ys4561')
ys4562 = Real('ys4562')
ys4571 = Real('ys4571')
ys4572 = Real('ys4572')
ys4581 = Real('ys4581')
ys4582 = Real('ys4582')
ys4591 = Real('ys4591')
ys4592 = Real('ys4592')
ys4601 = Real('ys4601')
ys4602 = Real('ys4602')
ys4611 = Real('ys4611')
ys4612 = Real('ys4612')
ys4621 = Real('ys4621')
ys4622 = Real('ys4622')
ys4631 = Real('ys4631')
ys4632 = Real('ys4632')
ys4641 = Real('ys4641')
ys4642 = Real('ys4642')
ys4651 = Real('ys4651')
ys4652 = Real('ys4652')
ys4661 = Real('ys4661')
ys4662 = Real('ys4662')
ys4671 = Real('ys4671')
ys4672 = Real('ys4672')
ys4681 = Real('ys4681')
ys4682 = Real('ys4682')
ys4691 = Real('ys4691')
ys4692 = Real('ys4692')
ys4701 = Real('ys4701')
ys4702 = Real('ys4702')
ys4711 = Real('ys4711')
ys4712 = Real('ys4712')
ys4721 = Real('ys4721')
ys4722 = Real('ys4722')
ys4731 = Real('ys4731')
ys4732 = Real('ys4732')
ys4741 = Real('ys4741')
ys4742 = Real('ys4742')
ys4751 = Real('ys4751')
ys4752 = Real('ys4752')
ys4761 = Real('ys4761')
ys4762 = Real('ys4762')
ys4771 = Real('ys4771')
ys4772 = Real('ys4772')
ys4781 = Real('ys4781')
ys4782 = Real('ys4782')
ys4791 = Real('ys4791')
ys4792 = Real('ys4792')
ys4801 = Real('ys4801')
ys4802 = Real('ys4802')
ys4811 = Real('ys4811')
ys4812 = Real('ys4812')
ys4821 = Real('ys4821')
ys4822 = Real('ys4822')
ys4831 = Real('ys4831')
ys4832 = Real('ys4832')
ys4841 = Real('ys4841')
ys4842 = Real('ys4842')
ys4851 = Real('ys4851')
ys4852 = Real('ys4852')
ys4861 = Real('ys4861')
ys4862 = Real('ys4862')
ys4871 = Real('ys4871')
ys4872 = Real('ys4872')
ys4881 = Real('ys4881')
ys4882 = Real('ys4882')
ys4891 = Real('ys4891')
ys4892 = Real('ys4892')
ys4901 = Real('ys4901')
ys4902 = Real('ys4902')
ys4911 = Real('ys4911')
ys4912 = Real('ys4912')
ys4921 = Real('ys4921')
ys4922 = Real('ys4922')
ys4931 = Real('ys4931')
ys4932 = Real('ys4932')
ys4941 = Real('ys4941')
ys4942 = Real('ys4942')
ys4951 = Real('ys4951')
ys4952 = Real('ys4952')
ys4961 = Real('ys4961')
ys4962 = Real('ys4962')
ys4971 = Real('ys4971')
ys4972 = Real('ys4972')
ys4981 = Real('ys4981')
ys4982 = Real('ys4982')
ys4991 = Real('ys4991')
ys4992 = Real('ys4992')
ys5001 = Real('ys5001')
ys5002 = Real('ys5002')
ys5011 = Real('ys5011')
ys5012 = Real('ys5012')
ys5021 = Real('ys5021')
ys5022 = Real('ys5022')
ys5031 = Real('ys5031')
ys5032 = Real('ys5032')
ys5041 = Real('ys5041')
ys5042 = Real('ys5042')
ys5051 = Real('ys5051')
ys5052 = Real('ys5052')
ys5061 = Real('ys5061')
ys5062 = Real('ys5062')
ys5071 = Real('ys5071')
ys5072 = Real('ys5072')
ys5081 = Real('ys5081')
ys5082 = Real('ys5082')
ys5091 = Real('ys5091')
ys5092 = Real('ys5092')
ys5101 = Real('ys5101')
ys5102 = Real('ys5102')
ys5111 = Real('ys5111')
ys5112 = Real('ys5112')
ys5121 = Real('ys5121')
ys5122 = Real('ys5122')
ys5131 = Real('ys5131')
ys5132 = Real('ys5132')
ys5141 = Real('ys5141')
ys5142 = Real('ys5142')
ys5151 = Real('ys5151')
ys5152 = Real('ys5152')
ys5161 = Real('ys5161')
ys5162 = Real('ys5162')
ys5171 = Real('ys5171')
ys5172 = Real('ys5172')
ys5181 = Real('ys5181')
ys5182 = Real('ys5182')
ys5191 = Real('ys5191')
ys5192 = Real('ys5192')
ys5201 = Real('ys5201')
ys5202 = Real('ys5202')
ys5211 = Real('ys5211')
ys5212 = Real('ys5212')
ys5221 = Real('ys5221')
ys5222 = Real('ys5222')
ys5231 = Real('ys5231')
ys5232 = Real('ys5232')
ys5241 = Real('ys5241')
ys5242 = Real('ys5242')
ys5251 = Real('ys5251')
ys5252 = Real('ys5252')
ys5261 = Real('ys5261')
ys5262 = Real('ys5262')
ys5271 = Real('ys5271')
ys5272 = Real('ys5272')
ys5281 = Real('ys5281')
ys5282 = Real('ys5282')
ys5291 = Real('ys5291')
ys5292 = Real('ys5292')
ys5301 = Real('ys5301')
ys5302 = Real('ys5302')
ys5311 = Real('ys5311')
ys5312 = Real('ys5312')
ys5321 = Real('ys5321')
ys5322 = Real('ys5322')
ys5331 = Real('ys5331')
ys5332 = Real('ys5332')
ys5341 = Real('ys5341')
ys5342 = Real('ys5342')
ys5351 = Real('ys5351')
ys5352 = Real('ys5352')
ys5361 = Real('ys5361')
ys5362 = Real('ys5362')
ys5371 = Real('ys5371')
ys5372 = Real('ys5372')
ys5381 = Real('ys5381')
ys5382 = Real('ys5382')
ys5391 = Real('ys5391')
ys5392 = Real('ys5392')
ys5401 = Real('ys5401')
ys5402 = Real('ys5402')
ys5411 = Real('ys5411')
ys5412 = Real('ys5412')
ys5421 = Real('ys5421')
ys5422 = Real('ys5422')
ys5431 = Real('ys5431')
ys5432 = Real('ys5432')
ys5441 = Real('ys5441')
ys5442 = Real('ys5442')
ys5451 = Real('ys5451')
ys5452 = Real('ys5452')
ys5461 = Real('ys5461')
ys5462 = Real('ys5462')
ys5471 = Real('ys5471')
ys5472 = Real('ys5472')
ys5481 = Real('ys5481')
ys5482 = Real('ys5482')
ys5491 = Real('ys5491')
ys5492 = Real('ys5492')
ys5501 = Real('ys5501')
ys5502 = Real('ys5502')
ys5511 = Real('ys5511')
ys5512 = Real('ys5512')
ys5521 = Real('ys5521')
ys5522 = Real('ys5522')
ys5531 = Real('ys5531')
ys5532 = Real('ys5532')
ys5541 = Real('ys5541')
ys5542 = Real('ys5542')
ys5551 = Real('ys5551')
ys5552 = Real('ys5552')
ys5561 = Real('ys5561')
ys5562 = Real('ys5562')
ys5571 = Real('ys5571')
ys5572 = Real('ys5572')
ys5581 = Real('ys5581')
ys5582 = Real('ys5582')
ys5591 = Real('ys5591')
ys5592 = Real('ys5592')
ys5601 = Real('ys5601')
ys5602 = Real('ys5602')
ys5611 = Real('ys5611')
ys5612 = Real('ys5612')
ys5621 = Real('ys5621')
ys5622 = Real('ys5622')
ys5631 = Real('ys5631')
ys5632 = Real('ys5632')
ys5641 = Real('ys5641')
ys5642 = Real('ys5642')
ys5651 = Real('ys5651')
ys5652 = Real('ys5652')
ys5661 = Real('ys5661')
ys5662 = Real('ys5662')
ys5671 = Real('ys5671')
ys5672 = Real('ys5672')
ys5681 = Real('ys5681')
ys5682 = Real('ys5682')
ys5691 = Real('ys5691')
ys5692 = Real('ys5692')
ys5701 = Real('ys5701')
ys5702 = Real('ys5702')
ys5711 = Real('ys5711')
ys5712 = Real('ys5712')
ys5721 = Real('ys5721')
ys5722 = Real('ys5722')
ys5731 = Real('ys5731')
ys5732 = Real('ys5732')
ys5741 = Real('ys5741')
ys5742 = Real('ys5742')
ys5751 = Real('ys5751')
ys5752 = Real('ys5752')
ys5761 = Real('ys5761')
ys5762 = Real('ys5762')
ys5771 = Real('ys5771')
ys5772 = Real('ys5772')
ys5781 = Real('ys5781')
ys5782 = Real('ys5782')
ys5791 = Real('ys5791')
ys5792 = Real('ys5792')
ys5801 = Real('ys5801')
ys5802 = Real('ys5802')
ys5811 = Real('ys5811')
ys5812 = Real('ys5812')
ys5821 = Real('ys5821')
ys5822 = Real('ys5822')
ys5831 = Real('ys5831')
ys5832 = Real('ys5832')
ys5841 = Real('ys5841')
ys5842 = Real('ys5842')
ys5851 = Real('ys5851')
ys5852 = Real('ys5852')
ys5861 = Real('ys5861')
ys5862 = Real('ys5862')
ys5871 = Real('ys5871')
ys5872 = Real('ys5872')
ys5881 = Real('ys5881')
ys5882 = Real('ys5882')
ys5891 = Real('ys5891')
ys5892 = Real('ys5892')
ys5901 = Real('ys5901')
ys5902 = Real('ys5902')
ys5911 = Real('ys5911')
ys5912 = Real('ys5912')
ys5921 = Real('ys5921')
ys5922 = Real('ys5922')
ys5931 = Real('ys5931')
ys5932 = Real('ys5932')
ys5941 = Real('ys5941')
ys5942 = Real('ys5942')
ys5951 = Real('ys5951')
ys5952 = Real('ys5952')
ys5961 = Real('ys5961')
ys5962 = Real('ys5962')
ys5971 = Real('ys5971')
ys5972 = Real('ys5972')
ys5981 = Real('ys5981')
ys5982 = Real('ys5982')
ys5991 = Real('ys5991')
ys5992 = Real('ys5992')
ys6001 = Real('ys6001')
ys6002 = Real('ys6002')
ys6011 = Real('ys6011')
ys6012 = Real('ys6012')
ys6021 = Real('ys6021')
ys6022 = Real('ys6022')
ys6031 = Real('ys6031')
ys6032 = Real('ys6032')
ys6041 = Real('ys6041')
ys6042 = Real('ys6042')
ys6051 = Real('ys6051')
ys6052 = Real('ys6052')
ys6061 = Real('ys6061')
ys6062 = Real('ys6062')
ys6071 = Real('ys6071')
ys6072 = Real('ys6072')
ys6081 = Real('ys6081')
ys6082 = Real('ys6082')
ys6091 = Real('ys6091')
ys6092 = Real('ys6092')
ys6101 = Real('ys6101')
ys6102 = Real('ys6102')
ys6111 = Real('ys6111')
ys6112 = Real('ys6112')
ys6121 = Real('ys6121')
ys6122 = Real('ys6122')
ys6131 = Real('ys6131')
ys6132 = Real('ys6132')
ys6141 = Real('ys6141')
ys6142 = Real('ys6142')
ys6151 = Real('ys6151')
ys6152 = Real('ys6152')
ys6161 = Real('ys6161')
ys6162 = Real('ys6162')
ys6171 = Real('ys6171')
ys6172 = Real('ys6172')
ys6181 = Real('ys6181')
ys6182 = Real('ys6182')
ys6191 = Real('ys6191')
ys6192 = Real('ys6192')
ys6201 = Real('ys6201')
ys6202 = Real('ys6202')
ys6211 = Real('ys6211')
ys6212 = Real('ys6212')
ys6221 = Real('ys6221')
ys6222 = Real('ys6222')
ys6231 = Real('ys6231')
ys6232 = Real('ys6232')

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
pi0>=48, pi1>=47, pi2>=46, pi3>=45, pi4>=44, pi5>=43, pi6>=42, pi7>=41, pi8>=40, pi9>=39, pi10>=38, pi11>=37, pi12>=36, pi13>=35, pi14>=34, pi15>=33, pi16>=32, pi17>=31, pi18>=30, pi19>=29, pi20>=28, pi21>=27, pi22>=26, pi23>=25, pi24>=24, pi25>=47, pi26>=46, pi27>=45, pi28>=44, pi29>=43, pi30>=42, pi31>=41, pi32>=40, pi33>=39, pi34>=38, pi35>=37, pi36>=36, pi37>=35, pi38>=34, pi39>=33, pi40>=32, pi41>=31, pi42>=30, pi43>=29, pi44>=28, pi45>=27, pi46>=26, pi47>=25, pi48>=24, pi49>=23, pi50>=46, pi51>=45, pi52>=44, pi53>=43, pi54>=42, pi55>=41, pi56>=40, pi57>=39, pi58>=38, pi59>=37, pi60>=36, pi61>=35, pi62>=34, pi63>=33, pi64>=32, pi65>=31, pi66>=30, pi67>=29, pi68>=28, pi69>=27, pi70>=26, pi71>=25, pi72>=24, pi73>=23, pi74>=22, pi75>=45, pi76>=44, pi77>=43, pi78>=42, pi79>=41, pi80>=40, pi81>=39, pi82>=38, pi83>=37, pi84>=36, pi85>=35, pi86>=34, pi87>=33, pi88>=32, pi89>=31, pi90>=30, pi91>=29, pi92>=28, pi93>=27, pi94>=26, pi95>=25, pi96>=24, pi97>=23, pi98>=22, pi99>=21, pi100>=44, pi101>=43, pi102>=42, pi103>=41, pi104>=40, pi105>=39, pi106>=38, pi107>=37, pi108>=36, pi109>=35, pi110>=34, pi111>=33, pi112>=32, pi113>=31, pi114>=30, pi115>=29, pi116>=28, pi117>=27, pi118>=26, pi119>=25, pi120>=24, pi121>=23, pi122>=22, pi123>=21, pi124>=20, pi125>=43, pi126>=42, pi127>=41, pi128>=40, pi129>=39, pi130>=38, pi131>=37, pi132>=36, pi133>=35, pi134>=34, pi135>=33, pi136>=32, pi137>=31, pi138>=30, pi139>=29, pi140>=28, pi141>=27, pi142>=26, pi143>=25, pi144>=24, pi145>=23, pi146>=22, pi147>=21, pi148>=20, pi149>=19, pi150>=42, pi151>=41, pi152>=40, pi153>=39, pi154>=38, pi155>=37, pi156>=36, pi157>=35, pi158>=34, pi159>=33, pi160>=32, pi161>=31, pi162>=30, pi163>=29, pi164>=28, pi165>=27, pi166>=26, pi167>=25, pi168>=24, pi169>=23, pi170>=22, pi171>=21, pi172>=20, pi173>=19, pi174>=18, pi175>=41, pi176>=40, pi177>=39, pi178>=38, pi179>=37, pi180>=36, pi181>=35, pi182>=34, pi183>=33, pi184>=32, pi185>=31, pi186>=30, pi187>=29, pi188>=28, pi189>=27, pi190>=26, pi191>=25, pi192>=24, pi193>=23, pi194>=22, pi195>=21, pi196>=20, pi197>=19, pi198>=18, pi199>=17, pi200>=40, pi201>=39, pi202>=38, pi203>=37, pi204>=36, pi205>=35, pi206>=34, pi207>=33, pi208>=32, pi209>=31, pi210>=30, pi211>=29, pi212>=28, pi213>=27, pi214>=26, pi215>=25, pi216>=24, pi217>=23, pi218>=22, pi219>=21, pi220>=20, pi221>=19, pi222>=18, pi223>=17, pi224>=16, pi225>=39, pi226>=38, pi227>=37, pi228>=36, pi229>=35, pi230>=34, pi231>=33, pi232>=32, pi233>=31, pi234>=30, pi235>=29, pi236>=28, pi237>=27, pi238>=26, pi239>=25, pi240>=24, pi241>=23, pi242>=22, pi243>=21, pi244>=20, pi245>=19, pi246>=18, pi247>=17, pi248>=16, pi249>=15, pi250>=38, pi251>=37, pi252>=36, pi253>=35, pi254>=34, pi255>=33, pi256>=32, pi257>=31, pi258>=30, pi259>=29, pi260>=28, pi261>=27, pi262>=26, pi263>=25, pi264>=24, pi265>=23, pi266>=22, pi267>=21, pi268>=20, pi269>=19, pi270>=18, pi271>=17, pi272>=16, pi273>=15, pi274>=14, pi275>=37, pi276>=36, pi277>=35, pi278>=34, pi279>=33, pi280>=32, pi281>=31, pi282>=30, pi283>=29, pi284>=28, pi285>=27, pi286>=26, pi287>=25, pi288>=24, pi289>=23, pi290>=22, pi291>=21, pi292>=20, pi293>=19, pi294>=18, pi295>=17, pi296>=16, pi297>=15, pi298>=14, pi299>=13, pi300>=36, pi301>=35, pi302>=34, pi303>=33, pi304>=32, pi305>=31, pi306>=30, pi307>=29, pi308>=28, pi309>=27, pi310>=26, pi311>=25, pi312>=24, pi313>=23, pi314>=22, pi315>=21, pi316>=20, pi317>=19, pi318>=18, pi319>=17, pi320>=16, pi321>=15, pi322>=14, pi323>=13, pi324>=12, pi325>=35, pi326>=34, pi327>=33, pi328>=32, pi329>=31, pi330>=30, pi331>=29, pi332>=28, pi333>=27, pi334>=26, pi335>=25, pi336>=24, pi337>=23, pi338>=22, pi339>=21, pi340>=20, pi341>=19, pi342>=18, pi343>=17, pi344>=16, pi345>=15, pi346>=14, pi347>=13, pi348>=12, pi349>=11, pi350>=34, pi351>=33, pi352>=32, pi353>=31, pi354>=30, pi355>=29, pi356>=28, pi357>=27, pi358>=26, pi359>=25, pi360>=24, pi361>=23, pi362>=22, pi363>=21, pi364>=20, pi365>=19, pi366>=18, pi367>=17, pi368>=16, pi369>=15, pi370>=14, pi371>=13, pi372>=12, pi373>=11, pi374>=10, pi375>=33, pi376>=32, pi377>=31, pi378>=30, pi379>=29, pi380>=28, pi381>=27, pi382>=26, pi383>=25, pi384>=24, pi385>=23, pi386>=22, pi387>=21, pi388>=20, pi389>=19, pi390>=18, pi391>=17, pi392>=16, pi393>=15, pi394>=14, pi395>=13, pi396>=12, pi397>=11, pi398>=10, pi399>=9, pi400>=32, pi401>=31, pi402>=30, pi403>=29, pi404>=28, pi405>=27, pi406>=26, pi407>=25, pi408>=24, pi409>=23, pi410>=22, pi411>=21, pi412>=20, pi413>=19, pi414>=18, pi415>=17, pi416>=16, pi417>=15, pi418>=14, pi419>=13, pi420>=12, pi421>=11, pi422>=10, pi423>=9, pi424>=8, pi425>=31, pi426>=30, pi427>=29, pi428>=28, pi429>=27, pi430>=26, pi431>=25, pi432>=24, pi433>=23, pi434>=22, pi435>=21, pi436>=20, pi437>=19, pi438>=18, pi439>=17, pi440>=16, pi441>=15, pi442>=14, pi443>=13, pi444>=12, pi445>=11, pi446>=10, pi447>=9, pi448>=8, pi449>=7, pi450>=30, pi451>=29, pi452>=28, pi453>=27, pi454>=26, pi455>=25, pi456>=24, pi457>=23, pi458>=22, pi459>=21, pi460>=20, pi461>=19, pi462>=18, pi463>=17, pi464>=16, pi465>=15, pi466>=14, pi467>=13, pi468>=12, pi469>=11, pi470>=10, pi471>=9, pi472>=8, pi473>=7, pi474>=6, pi475>=29, pi476>=28, pi477>=27, pi478>=26, pi479>=25, pi480>=24, pi481>=23, pi482>=22, pi483>=21, pi484>=20, pi485>=19, pi486>=18, pi487>=17, pi488>=16, pi489>=15, pi490>=14, pi491>=13, pi492>=12, pi493>=11, pi494>=10, pi495>=9, pi496>=8, pi497>=7, pi498>=6, pi499>=5, pi500>=28, pi501>=27, pi502>=26, pi503>=25, pi504>=24, pi505>=23, pi506>=22, pi507>=21, pi508>=20, pi509>=19, pi510>=18, pi511>=17, pi512>=16, pi513>=15, pi514>=14, pi515>=13, pi516>=12, pi517>=11, pi518>=10, pi519>=9, pi520>=8, pi521>=7, pi522>=6, pi523>=5, pi524>=4, pi525>=27, pi526>=26, pi527>=25, pi528>=24, pi529>=23, pi530>=22, pi531>=21, pi532>=20, pi533>=19, pi534>=18, pi535>=17, pi536>=16, pi537>=15, pi538>=14, pi539>=13, pi540>=12, pi541>=11, pi542>=10, pi543>=9, pi544>=8, pi545>=7, pi546>=6, pi547>=5, pi548>=4, pi549>=3, pi550>=26, pi551>=25, pi552>=24, pi553>=23, pi554>=22, pi555>=21, pi556>=20, pi557>=19, pi558>=18, pi559>=17, pi560>=16, pi561>=15, pi562>=14, pi563>=13, pi564>=12, pi565>=11, pi566>=10, pi567>=9, pi568>=8, pi569>=7, pi570>=6, pi571>=5, pi572>=4, pi573>=3, pi574>=2, pi575>=25, pi576>=24, pi577>=23, pi578>=22, pi579>=21, pi580>=20, pi581>=19, pi582>=18, pi583>=17, pi584>=16, pi585>=15, pi586>=14, pi587>=13, pi588>=12, pi589>=11, pi590>=10, pi591>=9, pi592>=8, pi593>=7, pi594>=6, pi595>=5, pi596>=4, pi597>=3, pi598>=2, pi599>=1, pi600>=24, pi601>=23, pi602>=22, pi603>=21, pi604>=20, pi605>=19, pi606>=18, pi607>=17, pi608>=16, pi609>=15, pi610>=14, pi611>=13, pi612>=12, pi613>=11, pi614>=10, pi615>=9, pi616>=8, pi617>=7, pi618>=6, pi619>=5, pi620>=4, pi621>=3, pi622>=2, pi623>=1, pi624>=0, 
# Expected cost/reward equations
pi0 == (ys01*xo1l + ys02*xo2l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d) * (1 + pi25),
pi1 == (ys11*xo1l + ys12*xo2l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r) * (1 + pi2) + (ys11*xo1u + ys12*xo2u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d) * (1 + pi26),
pi2 == (ys21*xo1l + ys22*xo2l) * (1 + pi1) + (ys21*xo1r + ys22*xo2r) * (1 + pi3) + (ys21*xo1u + ys22*xo2u) * (1 + pi2) + (ys21*xo1d + ys22*xo2d) * (1 + pi27),
pi3 == (ys31*xo1l + ys32*xo2l) * (1 + pi2) + (ys31*xo1r + ys32*xo2r) * (1 + pi4) + (ys31*xo1u + ys32*xo2u) * (1 + pi3) + (ys31*xo1d + ys32*xo2d) * (1 + pi28),
pi4 == (ys41*xo1l + ys42*xo2l) * (1 + pi3) + (ys41*xo1r + ys42*xo2r) * (1 + pi5) + (ys41*xo1u + ys42*xo2u) * (1 + pi4) + (ys41*xo1d + ys42*xo2d) * (1 + pi29),
pi5 == (ys51*xo1l + ys52*xo2l) * (1 + pi4) + (ys51*xo1r + ys52*xo2r) * (1 + pi6) + (ys51*xo1u + ys52*xo2u) * (1 + pi5) + (ys51*xo1d + ys52*xo2d) * (1 + pi30),
pi6 == (ys61*xo1l + ys62*xo2l) * (1 + pi5) + (ys61*xo1r + ys62*xo2r) * (1 + pi7) + (ys61*xo1u + ys62*xo2u) * (1 + pi6) + (ys61*xo1d + ys62*xo2d) * (1 + pi31),
pi7 == (ys71*xo1l + ys72*xo2l) * (1 + pi6) + (ys71*xo1r + ys72*xo2r) * (1 + pi8) + (ys71*xo1u + ys72*xo2u) * (1 + pi7) + (ys71*xo1d + ys72*xo2d) * (1 + pi32),
pi8 == (ys81*xo1l + ys82*xo2l) * (1 + pi7) + (ys81*xo1r + ys82*xo2r) * (1 + pi9) + (ys81*xo1u + ys82*xo2u) * (1 + pi8) + (ys81*xo1d + ys82*xo2d) * (1 + pi33),
pi9 == (ys91*xo1l + ys92*xo2l) * (1 + pi8) + (ys91*xo1r + ys92*xo2r) * (1 + pi10) + (ys91*xo1u + ys92*xo2u) * (1 + pi9) + (ys91*xo1d + ys92*xo2d) * (1 + pi34),
pi10 == (ys101*xo1l + ys102*xo2l) * (1 + pi9) + (ys101*xo1r + ys102*xo2r) * (1 + pi11) + (ys101*xo1u + ys102*xo2u) * (1 + pi10) + (ys101*xo1d + ys102*xo2d) * (1 + pi35),
pi11 == (ys111*xo1l + ys112*xo2l) * (1 + pi10) + (ys111*xo1r + ys112*xo2r) * (1 + pi12) + (ys111*xo1u + ys112*xo2u) * (1 + pi11) + (ys111*xo1d + ys112*xo2d) * (1 + pi36),
pi12 == (ys121*xo1l + ys122*xo2l) * (1 + pi11) + (ys121*xo1r + ys122*xo2r) * (1 + pi13) + (ys121*xo1u + ys122*xo2u) * (1 + pi12) + (ys121*xo1d + ys122*xo2d) * (1 + pi37),
pi13 == (ys131*xo1l + ys132*xo2l) * (1 + pi12) + (ys131*xo1r + ys132*xo2r) * (1 + pi14) + (ys131*xo1u + ys132*xo2u) * (1 + pi13) + (ys131*xo1d + ys132*xo2d) * (1 + pi38),
pi14 == (ys141*xo1l + ys142*xo2l) * (1 + pi13) + (ys141*xo1r + ys142*xo2r) * (1 + pi15) + (ys141*xo1u + ys142*xo2u) * (1 + pi14) + (ys141*xo1d + ys142*xo2d) * (1 + pi39),
pi15 == (ys151*xo1l + ys152*xo2l) * (1 + pi14) + (ys151*xo1r + ys152*xo2r) * (1 + pi16) + (ys151*xo1u + ys152*xo2u) * (1 + pi15) + (ys151*xo1d + ys152*xo2d) * (1 + pi40),
pi16 == (ys161*xo1l + ys162*xo2l) * (1 + pi15) + (ys161*xo1r + ys162*xo2r) * (1 + pi17) + (ys161*xo1u + ys162*xo2u) * (1 + pi16) + (ys161*xo1d + ys162*xo2d) * (1 + pi41),
pi17 == (ys171*xo1l + ys172*xo2l) * (1 + pi16) + (ys171*xo1r + ys172*xo2r) * (1 + pi18) + (ys171*xo1u + ys172*xo2u) * (1 + pi17) + (ys171*xo1d + ys172*xo2d) * (1 + pi42),
pi18 == (ys181*xo1l + ys182*xo2l) * (1 + pi17) + (ys181*xo1r + ys182*xo2r) * (1 + pi19) + (ys181*xo1u + ys182*xo2u) * (1 + pi18) + (ys181*xo1d + ys182*xo2d) * (1 + pi43),
pi19 == (ys191*xo1l + ys192*xo2l) * (1 + pi18) + (ys191*xo1r + ys192*xo2r) * (1 + pi20) + (ys191*xo1u + ys192*xo2u) * (1 + pi19) + (ys191*xo1d + ys192*xo2d) * (1 + pi44),
pi20 == (ys201*xo1l + ys202*xo2l) * (1 + pi19) + (ys201*xo1r + ys202*xo2r) * (1 + pi21) + (ys201*xo1u + ys202*xo2u) * (1 + pi20) + (ys201*xo1d + ys202*xo2d) * (1 + pi45),
pi21 == (ys211*xo1l + ys212*xo2l) * (1 + pi20) + (ys211*xo1r + ys212*xo2r) * (1 + pi22) + (ys211*xo1u + ys212*xo2u) * (1 + pi21) + (ys211*xo1d + ys212*xo2d) * (1 + pi46),
pi22 == (ys221*xo1l + ys222*xo2l) * (1 + pi21) + (ys221*xo1r + ys222*xo2r) * (1 + pi23) + (ys221*xo1u + ys222*xo2u) * (1 + pi22) + (ys221*xo1d + ys222*xo2d) * (1 + pi47),
pi23 == (ys231*xo1l + ys232*xo2l) * (1 + pi22) + (ys231*xo1r + ys232*xo2r) * (1 + pi24) + (ys231*xo1u + ys232*xo2u) * (1 + pi23) + (ys231*xo1d + ys232*xo2d) * (1 + pi48),
pi24 == (ys241*xo1l + ys242*xo2l) * (1 + pi23) + (ys241*xo1r + ys242*xo2r) * (1 + pi24) + (ys241*xo1u + ys242*xo2u) * (1 + pi24) + (ys241*xo1d + ys242*xo2d) * (1 + pi49),
pi25 == (ys251*xo1l + ys252*xo2l) * (1 + pi25) + (ys251*xo1r + ys252*xo2r) * (1 + pi26) + (ys251*xo1u + ys252*xo2u) * (1 + pi0) + (ys251*xo1d + ys252*xo2d) * (1 + pi50),
pi26 == (ys261*xo1l + ys262*xo2l) * (1 + pi25) + (ys261*xo1r + ys262*xo2r) * (1 + pi27) + (ys261*xo1u + ys262*xo2u) * (1 + pi1) + (ys261*xo1d + ys262*xo2d) * (1 + pi51),
pi27 == (ys271*xo1l + ys272*xo2l) * (1 + pi26) + (ys271*xo1r + ys272*xo2r) * (1 + pi28) + (ys271*xo1u + ys272*xo2u) * (1 + pi2) + (ys271*xo1d + ys272*xo2d) * (1 + pi52),
pi28 == (ys281*xo1l + ys282*xo2l) * (1 + pi27) + (ys281*xo1r + ys282*xo2r) * (1 + pi29) + (ys281*xo1u + ys282*xo2u) * (1 + pi3) + (ys281*xo1d + ys282*xo2d) * (1 + pi53),
pi29 == (ys291*xo1l + ys292*xo2l) * (1 + pi28) + (ys291*xo1r + ys292*xo2r) * (1 + pi30) + (ys291*xo1u + ys292*xo2u) * (1 + pi4) + (ys291*xo1d + ys292*xo2d) * (1 + pi54),
pi30 == (ys301*xo1l + ys302*xo2l) * (1 + pi29) + (ys301*xo1r + ys302*xo2r) * (1 + pi31) + (ys301*xo1u + ys302*xo2u) * (1 + pi5) + (ys301*xo1d + ys302*xo2d) * (1 + pi55),
pi31 == (ys311*xo1l + ys312*xo2l) * (1 + pi30) + (ys311*xo1r + ys312*xo2r) * (1 + pi32) + (ys311*xo1u + ys312*xo2u) * (1 + pi6) + (ys311*xo1d + ys312*xo2d) * (1 + pi56),
pi32 == (ys321*xo1l + ys322*xo2l) * (1 + pi31) + (ys321*xo1r + ys322*xo2r) * (1 + pi33) + (ys321*xo1u + ys322*xo2u) * (1 + pi7) + (ys321*xo1d + ys322*xo2d) * (1 + pi57),
pi33 == (ys331*xo1l + ys332*xo2l) * (1 + pi32) + (ys331*xo1r + ys332*xo2r) * (1 + pi34) + (ys331*xo1u + ys332*xo2u) * (1 + pi8) + (ys331*xo1d + ys332*xo2d) * (1 + pi58),
pi34 == (ys341*xo1l + ys342*xo2l) * (1 + pi33) + (ys341*xo1r + ys342*xo2r) * (1 + pi35) + (ys341*xo1u + ys342*xo2u) * (1 + pi9) + (ys341*xo1d + ys342*xo2d) * (1 + pi59),
pi35 == (ys351*xo1l + ys352*xo2l) * (1 + pi34) + (ys351*xo1r + ys352*xo2r) * (1 + pi36) + (ys351*xo1u + ys352*xo2u) * (1 + pi10) + (ys351*xo1d + ys352*xo2d) * (1 + pi60),
pi36 == (ys361*xo1l + ys362*xo2l) * (1 + pi35) + (ys361*xo1r + ys362*xo2r) * (1 + pi37) + (ys361*xo1u + ys362*xo2u) * (1 + pi11) + (ys361*xo1d + ys362*xo2d) * (1 + pi61),
pi37 == (ys371*xo1l + ys372*xo2l) * (1 + pi36) + (ys371*xo1r + ys372*xo2r) * (1 + pi38) + (ys371*xo1u + ys372*xo2u) * (1 + pi12) + (ys371*xo1d + ys372*xo2d) * (1 + pi62),
pi38 == (ys381*xo1l + ys382*xo2l) * (1 + pi37) + (ys381*xo1r + ys382*xo2r) * (1 + pi39) + (ys381*xo1u + ys382*xo2u) * (1 + pi13) + (ys381*xo1d + ys382*xo2d) * (1 + pi63),
pi39 == (ys391*xo1l + ys392*xo2l) * (1 + pi38) + (ys391*xo1r + ys392*xo2r) * (1 + pi40) + (ys391*xo1u + ys392*xo2u) * (1 + pi14) + (ys391*xo1d + ys392*xo2d) * (1 + pi64),
pi40 == (ys401*xo1l + ys402*xo2l) * (1 + pi39) + (ys401*xo1r + ys402*xo2r) * (1 + pi41) + (ys401*xo1u + ys402*xo2u) * (1 + pi15) + (ys401*xo1d + ys402*xo2d) * (1 + pi65),
pi41 == (ys411*xo1l + ys412*xo2l) * (1 + pi40) + (ys411*xo1r + ys412*xo2r) * (1 + pi42) + (ys411*xo1u + ys412*xo2u) * (1 + pi16) + (ys411*xo1d + ys412*xo2d) * (1 + pi66),
pi42 == (ys421*xo1l + ys422*xo2l) * (1 + pi41) + (ys421*xo1r + ys422*xo2r) * (1 + pi43) + (ys421*xo1u + ys422*xo2u) * (1 + pi17) + (ys421*xo1d + ys422*xo2d) * (1 + pi67),
pi43 == (ys431*xo1l + ys432*xo2l) * (1 + pi42) + (ys431*xo1r + ys432*xo2r) * (1 + pi44) + (ys431*xo1u + ys432*xo2u) * (1 + pi18) + (ys431*xo1d + ys432*xo2d) * (1 + pi68),
pi44 == (ys441*xo1l + ys442*xo2l) * (1 + pi43) + (ys441*xo1r + ys442*xo2r) * (1 + pi45) + (ys441*xo1u + ys442*xo2u) * (1 + pi19) + (ys441*xo1d + ys442*xo2d) * (1 + pi69),
pi45 == (ys451*xo1l + ys452*xo2l) * (1 + pi44) + (ys451*xo1r + ys452*xo2r) * (1 + pi46) + (ys451*xo1u + ys452*xo2u) * (1 + pi20) + (ys451*xo1d + ys452*xo2d) * (1 + pi70),
pi46 == (ys461*xo1l + ys462*xo2l) * (1 + pi45) + (ys461*xo1r + ys462*xo2r) * (1 + pi47) + (ys461*xo1u + ys462*xo2u) * (1 + pi21) + (ys461*xo1d + ys462*xo2d) * (1 + pi71),
pi47 == (ys471*xo1l + ys472*xo2l) * (1 + pi46) + (ys471*xo1r + ys472*xo2r) * (1 + pi48) + (ys471*xo1u + ys472*xo2u) * (1 + pi22) + (ys471*xo1d + ys472*xo2d) * (1 + pi72),
pi48 == (ys481*xo1l + ys482*xo2l) * (1 + pi47) + (ys481*xo1r + ys482*xo2r) * (1 + pi49) + (ys481*xo1u + ys482*xo2u) * (1 + pi23) + (ys481*xo1d + ys482*xo2d) * (1 + pi73),
pi49 == (ys491*xo1l + ys492*xo2l) * (1 + pi48) + (ys491*xo1r + ys492*xo2r) * (1 + pi49) + (ys491*xo1u + ys492*xo2u) * (1 + pi24) + (ys491*xo1d + ys492*xo2d) * (1 + pi74),
pi50 == (ys501*xo1l + ys502*xo2l) * (1 + pi50) + (ys501*xo1r + ys502*xo2r) * (1 + pi51) + (ys501*xo1u + ys502*xo2u) * (1 + pi25) + (ys501*xo1d + ys502*xo2d) * (1 + pi75),
pi51 == (ys511*xo1l + ys512*xo2l) * (1 + pi50) + (ys511*xo1r + ys512*xo2r) * (1 + pi52) + (ys511*xo1u + ys512*xo2u) * (1 + pi26) + (ys511*xo1d + ys512*xo2d) * (1 + pi76),
pi52 == (ys521*xo1l + ys522*xo2l) * (1 + pi51) + (ys521*xo1r + ys522*xo2r) * (1 + pi53) + (ys521*xo1u + ys522*xo2u) * (1 + pi27) + (ys521*xo1d + ys522*xo2d) * (1 + pi77),
pi53 == (ys531*xo1l + ys532*xo2l) * (1 + pi52) + (ys531*xo1r + ys532*xo2r) * (1 + pi54) + (ys531*xo1u + ys532*xo2u) * (1 + pi28) + (ys531*xo1d + ys532*xo2d) * (1 + pi78),
pi54 == (ys541*xo1l + ys542*xo2l) * (1 + pi53) + (ys541*xo1r + ys542*xo2r) * (1 + pi55) + (ys541*xo1u + ys542*xo2u) * (1 + pi29) + (ys541*xo1d + ys542*xo2d) * (1 + pi79),
pi55 == (ys551*xo1l + ys552*xo2l) * (1 + pi54) + (ys551*xo1r + ys552*xo2r) * (1 + pi56) + (ys551*xo1u + ys552*xo2u) * (1 + pi30) + (ys551*xo1d + ys552*xo2d) * (1 + pi80),
pi56 == (ys561*xo1l + ys562*xo2l) * (1 + pi55) + (ys561*xo1r + ys562*xo2r) * (1 + pi57) + (ys561*xo1u + ys562*xo2u) * (1 + pi31) + (ys561*xo1d + ys562*xo2d) * (1 + pi81),
pi57 == (ys571*xo1l + ys572*xo2l) * (1 + pi56) + (ys571*xo1r + ys572*xo2r) * (1 + pi58) + (ys571*xo1u + ys572*xo2u) * (1 + pi32) + (ys571*xo1d + ys572*xo2d) * (1 + pi82),
pi58 == (ys581*xo1l + ys582*xo2l) * (1 + pi57) + (ys581*xo1r + ys582*xo2r) * (1 + pi59) + (ys581*xo1u + ys582*xo2u) * (1 + pi33) + (ys581*xo1d + ys582*xo2d) * (1 + pi83),
pi59 == (ys591*xo1l + ys592*xo2l) * (1 + pi58) + (ys591*xo1r + ys592*xo2r) * (1 + pi60) + (ys591*xo1u + ys592*xo2u) * (1 + pi34) + (ys591*xo1d + ys592*xo2d) * (1 + pi84),
pi60 == (ys601*xo1l + ys602*xo2l) * (1 + pi59) + (ys601*xo1r + ys602*xo2r) * (1 + pi61) + (ys601*xo1u + ys602*xo2u) * (1 + pi35) + (ys601*xo1d + ys602*xo2d) * (1 + pi85),
pi61 == (ys611*xo1l + ys612*xo2l) * (1 + pi60) + (ys611*xo1r + ys612*xo2r) * (1 + pi62) + (ys611*xo1u + ys612*xo2u) * (1 + pi36) + (ys611*xo1d + ys612*xo2d) * (1 + pi86),
pi62 == (ys621*xo1l + ys622*xo2l) * (1 + pi61) + (ys621*xo1r + ys622*xo2r) * (1 + pi63) + (ys621*xo1u + ys622*xo2u) * (1 + pi37) + (ys621*xo1d + ys622*xo2d) * (1 + pi87),
pi63 == (ys631*xo1l + ys632*xo2l) * (1 + pi62) + (ys631*xo1r + ys632*xo2r) * (1 + pi64) + (ys631*xo1u + ys632*xo2u) * (1 + pi38) + (ys631*xo1d + ys632*xo2d) * (1 + pi88),
pi64 == (ys641*xo1l + ys642*xo2l) * (1 + pi63) + (ys641*xo1r + ys642*xo2r) * (1 + pi65) + (ys641*xo1u + ys642*xo2u) * (1 + pi39) + (ys641*xo1d + ys642*xo2d) * (1 + pi89),
pi65 == (ys651*xo1l + ys652*xo2l) * (1 + pi64) + (ys651*xo1r + ys652*xo2r) * (1 + pi66) + (ys651*xo1u + ys652*xo2u) * (1 + pi40) + (ys651*xo1d + ys652*xo2d) * (1 + pi90),
pi66 == (ys661*xo1l + ys662*xo2l) * (1 + pi65) + (ys661*xo1r + ys662*xo2r) * (1 + pi67) + (ys661*xo1u + ys662*xo2u) * (1 + pi41) + (ys661*xo1d + ys662*xo2d) * (1 + pi91),
pi67 == (ys671*xo1l + ys672*xo2l) * (1 + pi66) + (ys671*xo1r + ys672*xo2r) * (1 + pi68) + (ys671*xo1u + ys672*xo2u) * (1 + pi42) + (ys671*xo1d + ys672*xo2d) * (1 + pi92),
pi68 == (ys681*xo1l + ys682*xo2l) * (1 + pi67) + (ys681*xo1r + ys682*xo2r) * (1 + pi69) + (ys681*xo1u + ys682*xo2u) * (1 + pi43) + (ys681*xo1d + ys682*xo2d) * (1 + pi93),
pi69 == (ys691*xo1l + ys692*xo2l) * (1 + pi68) + (ys691*xo1r + ys692*xo2r) * (1 + pi70) + (ys691*xo1u + ys692*xo2u) * (1 + pi44) + (ys691*xo1d + ys692*xo2d) * (1 + pi94),
pi70 == (ys701*xo1l + ys702*xo2l) * (1 + pi69) + (ys701*xo1r + ys702*xo2r) * (1 + pi71) + (ys701*xo1u + ys702*xo2u) * (1 + pi45) + (ys701*xo1d + ys702*xo2d) * (1 + pi95),
pi71 == (ys711*xo1l + ys712*xo2l) * (1 + pi70) + (ys711*xo1r + ys712*xo2r) * (1 + pi72) + (ys711*xo1u + ys712*xo2u) * (1 + pi46) + (ys711*xo1d + ys712*xo2d) * (1 + pi96),
pi72 == (ys721*xo1l + ys722*xo2l) * (1 + pi71) + (ys721*xo1r + ys722*xo2r) * (1 + pi73) + (ys721*xo1u + ys722*xo2u) * (1 + pi47) + (ys721*xo1d + ys722*xo2d) * (1 + pi97),
pi73 == (ys731*xo1l + ys732*xo2l) * (1 + pi72) + (ys731*xo1r + ys732*xo2r) * (1 + pi74) + (ys731*xo1u + ys732*xo2u) * (1 + pi48) + (ys731*xo1d + ys732*xo2d) * (1 + pi98),
pi74 == (ys741*xo1l + ys742*xo2l) * (1 + pi73) + (ys741*xo1r + ys742*xo2r) * (1 + pi74) + (ys741*xo1u + ys742*xo2u) * (1 + pi49) + (ys741*xo1d + ys742*xo2d) * (1 + pi99),
pi75 == (ys751*xo1l + ys752*xo2l) * (1 + pi75) + (ys751*xo1r + ys752*xo2r) * (1 + pi76) + (ys751*xo1u + ys752*xo2u) * (1 + pi50) + (ys751*xo1d + ys752*xo2d) * (1 + pi100),
pi76 == (ys761*xo1l + ys762*xo2l) * (1 + pi75) + (ys761*xo1r + ys762*xo2r) * (1 + pi77) + (ys761*xo1u + ys762*xo2u) * (1 + pi51) + (ys761*xo1d + ys762*xo2d) * (1 + pi101),
pi77 == (ys771*xo1l + ys772*xo2l) * (1 + pi76) + (ys771*xo1r + ys772*xo2r) * (1 + pi78) + (ys771*xo1u + ys772*xo2u) * (1 + pi52) + (ys771*xo1d + ys772*xo2d) * (1 + pi102),
pi78 == (ys781*xo1l + ys782*xo2l) * (1 + pi77) + (ys781*xo1r + ys782*xo2r) * (1 + pi79) + (ys781*xo1u + ys782*xo2u) * (1 + pi53) + (ys781*xo1d + ys782*xo2d) * (1 + pi103),
pi79 == (ys791*xo1l + ys792*xo2l) * (1 + pi78) + (ys791*xo1r + ys792*xo2r) * (1 + pi80) + (ys791*xo1u + ys792*xo2u) * (1 + pi54) + (ys791*xo1d + ys792*xo2d) * (1 + pi104),
pi80 == (ys801*xo1l + ys802*xo2l) * (1 + pi79) + (ys801*xo1r + ys802*xo2r) * (1 + pi81) + (ys801*xo1u + ys802*xo2u) * (1 + pi55) + (ys801*xo1d + ys802*xo2d) * (1 + pi105),
pi81 == (ys811*xo1l + ys812*xo2l) * (1 + pi80) + (ys811*xo1r + ys812*xo2r) * (1 + pi82) + (ys811*xo1u + ys812*xo2u) * (1 + pi56) + (ys811*xo1d + ys812*xo2d) * (1 + pi106),
pi82 == (ys821*xo1l + ys822*xo2l) * (1 + pi81) + (ys821*xo1r + ys822*xo2r) * (1 + pi83) + (ys821*xo1u + ys822*xo2u) * (1 + pi57) + (ys821*xo1d + ys822*xo2d) * (1 + pi107),
pi83 == (ys831*xo1l + ys832*xo2l) * (1 + pi82) + (ys831*xo1r + ys832*xo2r) * (1 + pi84) + (ys831*xo1u + ys832*xo2u) * (1 + pi58) + (ys831*xo1d + ys832*xo2d) * (1 + pi108),
pi84 == (ys841*xo1l + ys842*xo2l) * (1 + pi83) + (ys841*xo1r + ys842*xo2r) * (1 + pi85) + (ys841*xo1u + ys842*xo2u) * (1 + pi59) + (ys841*xo1d + ys842*xo2d) * (1 + pi109),
pi85 == (ys851*xo1l + ys852*xo2l) * (1 + pi84) + (ys851*xo1r + ys852*xo2r) * (1 + pi86) + (ys851*xo1u + ys852*xo2u) * (1 + pi60) + (ys851*xo1d + ys852*xo2d) * (1 + pi110),
pi86 == (ys861*xo1l + ys862*xo2l) * (1 + pi85) + (ys861*xo1r + ys862*xo2r) * (1 + pi87) + (ys861*xo1u + ys862*xo2u) * (1 + pi61) + (ys861*xo1d + ys862*xo2d) * (1 + pi111),
pi87 == (ys871*xo1l + ys872*xo2l) * (1 + pi86) + (ys871*xo1r + ys872*xo2r) * (1 + pi88) + (ys871*xo1u + ys872*xo2u) * (1 + pi62) + (ys871*xo1d + ys872*xo2d) * (1 + pi112),
pi88 == (ys881*xo1l + ys882*xo2l) * (1 + pi87) + (ys881*xo1r + ys882*xo2r) * (1 + pi89) + (ys881*xo1u + ys882*xo2u) * (1 + pi63) + (ys881*xo1d + ys882*xo2d) * (1 + pi113),
pi89 == (ys891*xo1l + ys892*xo2l) * (1 + pi88) + (ys891*xo1r + ys892*xo2r) * (1 + pi90) + (ys891*xo1u + ys892*xo2u) * (1 + pi64) + (ys891*xo1d + ys892*xo2d) * (1 + pi114),
pi90 == (ys901*xo1l + ys902*xo2l) * (1 + pi89) + (ys901*xo1r + ys902*xo2r) * (1 + pi91) + (ys901*xo1u + ys902*xo2u) * (1 + pi65) + (ys901*xo1d + ys902*xo2d) * (1 + pi115),
pi91 == (ys911*xo1l + ys912*xo2l) * (1 + pi90) + (ys911*xo1r + ys912*xo2r) * (1 + pi92) + (ys911*xo1u + ys912*xo2u) * (1 + pi66) + (ys911*xo1d + ys912*xo2d) * (1 + pi116),
pi92 == (ys921*xo1l + ys922*xo2l) * (1 + pi91) + (ys921*xo1r + ys922*xo2r) * (1 + pi93) + (ys921*xo1u + ys922*xo2u) * (1 + pi67) + (ys921*xo1d + ys922*xo2d) * (1 + pi117),
pi93 == (ys931*xo1l + ys932*xo2l) * (1 + pi92) + (ys931*xo1r + ys932*xo2r) * (1 + pi94) + (ys931*xo1u + ys932*xo2u) * (1 + pi68) + (ys931*xo1d + ys932*xo2d) * (1 + pi118),
pi94 == (ys941*xo1l + ys942*xo2l) * (1 + pi93) + (ys941*xo1r + ys942*xo2r) * (1 + pi95) + (ys941*xo1u + ys942*xo2u) * (1 + pi69) + (ys941*xo1d + ys942*xo2d) * (1 + pi119),
pi95 == (ys951*xo1l + ys952*xo2l) * (1 + pi94) + (ys951*xo1r + ys952*xo2r) * (1 + pi96) + (ys951*xo1u + ys952*xo2u) * (1 + pi70) + (ys951*xo1d + ys952*xo2d) * (1 + pi120),
pi96 == (ys961*xo1l + ys962*xo2l) * (1 + pi95) + (ys961*xo1r + ys962*xo2r) * (1 + pi97) + (ys961*xo1u + ys962*xo2u) * (1 + pi71) + (ys961*xo1d + ys962*xo2d) * (1 + pi121),
pi97 == (ys971*xo1l + ys972*xo2l) * (1 + pi96) + (ys971*xo1r + ys972*xo2r) * (1 + pi98) + (ys971*xo1u + ys972*xo2u) * (1 + pi72) + (ys971*xo1d + ys972*xo2d) * (1 + pi122),
pi98 == (ys981*xo1l + ys982*xo2l) * (1 + pi97) + (ys981*xo1r + ys982*xo2r) * (1 + pi99) + (ys981*xo1u + ys982*xo2u) * (1 + pi73) + (ys981*xo1d + ys982*xo2d) * (1 + pi123),
pi99 == (ys991*xo1l + ys992*xo2l) * (1 + pi98) + (ys991*xo1r + ys992*xo2r) * (1 + pi99) + (ys991*xo1u + ys992*xo2u) * (1 + pi74) + (ys991*xo1d + ys992*xo2d) * (1 + pi124),
pi100 == (ys1001*xo1l + ys1002*xo2l) * (1 + pi100) + (ys1001*xo1r + ys1002*xo2r) * (1 + pi101) + (ys1001*xo1u + ys1002*xo2u) * (1 + pi75) + (ys1001*xo1d + ys1002*xo2d) * (1 + pi125),
pi101 == (ys1011*xo1l + ys1012*xo2l) * (1 + pi100) + (ys1011*xo1r + ys1012*xo2r) * (1 + pi102) + (ys1011*xo1u + ys1012*xo2u) * (1 + pi76) + (ys1011*xo1d + ys1012*xo2d) * (1 + pi126),
pi102 == (ys1021*xo1l + ys1022*xo2l) * (1 + pi101) + (ys1021*xo1r + ys1022*xo2r) * (1 + pi103) + (ys1021*xo1u + ys1022*xo2u) * (1 + pi77) + (ys1021*xo1d + ys1022*xo2d) * (1 + pi127),
pi103 == (ys1031*xo1l + ys1032*xo2l) * (1 + pi102) + (ys1031*xo1r + ys1032*xo2r) * (1 + pi104) + (ys1031*xo1u + ys1032*xo2u) * (1 + pi78) + (ys1031*xo1d + ys1032*xo2d) * (1 + pi128),
pi104 == (ys1041*xo1l + ys1042*xo2l) * (1 + pi103) + (ys1041*xo1r + ys1042*xo2r) * (1 + pi105) + (ys1041*xo1u + ys1042*xo2u) * (1 + pi79) + (ys1041*xo1d + ys1042*xo2d) * (1 + pi129),
pi105 == (ys1051*xo1l + ys1052*xo2l) * (1 + pi104) + (ys1051*xo1r + ys1052*xo2r) * (1 + pi106) + (ys1051*xo1u + ys1052*xo2u) * (1 + pi80) + (ys1051*xo1d + ys1052*xo2d) * (1 + pi130),
pi106 == (ys1061*xo1l + ys1062*xo2l) * (1 + pi105) + (ys1061*xo1r + ys1062*xo2r) * (1 + pi107) + (ys1061*xo1u + ys1062*xo2u) * (1 + pi81) + (ys1061*xo1d + ys1062*xo2d) * (1 + pi131),
pi107 == (ys1071*xo1l + ys1072*xo2l) * (1 + pi106) + (ys1071*xo1r + ys1072*xo2r) * (1 + pi108) + (ys1071*xo1u + ys1072*xo2u) * (1 + pi82) + (ys1071*xo1d + ys1072*xo2d) * (1 + pi132),
pi108 == (ys1081*xo1l + ys1082*xo2l) * (1 + pi107) + (ys1081*xo1r + ys1082*xo2r) * (1 + pi109) + (ys1081*xo1u + ys1082*xo2u) * (1 + pi83) + (ys1081*xo1d + ys1082*xo2d) * (1 + pi133),
pi109 == (ys1091*xo1l + ys1092*xo2l) * (1 + pi108) + (ys1091*xo1r + ys1092*xo2r) * (1 + pi110) + (ys1091*xo1u + ys1092*xo2u) * (1 + pi84) + (ys1091*xo1d + ys1092*xo2d) * (1 + pi134),
pi110 == (ys1101*xo1l + ys1102*xo2l) * (1 + pi109) + (ys1101*xo1r + ys1102*xo2r) * (1 + pi111) + (ys1101*xo1u + ys1102*xo2u) * (1 + pi85) + (ys1101*xo1d + ys1102*xo2d) * (1 + pi135),
pi111 == (ys1111*xo1l + ys1112*xo2l) * (1 + pi110) + (ys1111*xo1r + ys1112*xo2r) * (1 + pi112) + (ys1111*xo1u + ys1112*xo2u) * (1 + pi86) + (ys1111*xo1d + ys1112*xo2d) * (1 + pi136),
pi112 == (ys1121*xo1l + ys1122*xo2l) * (1 + pi111) + (ys1121*xo1r + ys1122*xo2r) * (1 + pi113) + (ys1121*xo1u + ys1122*xo2u) * (1 + pi87) + (ys1121*xo1d + ys1122*xo2d) * (1 + pi137),
pi113 == (ys1131*xo1l + ys1132*xo2l) * (1 + pi112) + (ys1131*xo1r + ys1132*xo2r) * (1 + pi114) + (ys1131*xo1u + ys1132*xo2u) * (1 + pi88) + (ys1131*xo1d + ys1132*xo2d) * (1 + pi138),
pi114 == (ys1141*xo1l + ys1142*xo2l) * (1 + pi113) + (ys1141*xo1r + ys1142*xo2r) * (1 + pi115) + (ys1141*xo1u + ys1142*xo2u) * (1 + pi89) + (ys1141*xo1d + ys1142*xo2d) * (1 + pi139),
pi115 == (ys1151*xo1l + ys1152*xo2l) * (1 + pi114) + (ys1151*xo1r + ys1152*xo2r) * (1 + pi116) + (ys1151*xo1u + ys1152*xo2u) * (1 + pi90) + (ys1151*xo1d + ys1152*xo2d) * (1 + pi140),
pi116 == (ys1161*xo1l + ys1162*xo2l) * (1 + pi115) + (ys1161*xo1r + ys1162*xo2r) * (1 + pi117) + (ys1161*xo1u + ys1162*xo2u) * (1 + pi91) + (ys1161*xo1d + ys1162*xo2d) * (1 + pi141),
pi117 == (ys1171*xo1l + ys1172*xo2l) * (1 + pi116) + (ys1171*xo1r + ys1172*xo2r) * (1 + pi118) + (ys1171*xo1u + ys1172*xo2u) * (1 + pi92) + (ys1171*xo1d + ys1172*xo2d) * (1 + pi142),
pi118 == (ys1181*xo1l + ys1182*xo2l) * (1 + pi117) + (ys1181*xo1r + ys1182*xo2r) * (1 + pi119) + (ys1181*xo1u + ys1182*xo2u) * (1 + pi93) + (ys1181*xo1d + ys1182*xo2d) * (1 + pi143),
pi119 == (ys1191*xo1l + ys1192*xo2l) * (1 + pi118) + (ys1191*xo1r + ys1192*xo2r) * (1 + pi120) + (ys1191*xo1u + ys1192*xo2u) * (1 + pi94) + (ys1191*xo1d + ys1192*xo2d) * (1 + pi144),
pi120 == (ys1201*xo1l + ys1202*xo2l) * (1 + pi119) + (ys1201*xo1r + ys1202*xo2r) * (1 + pi121) + (ys1201*xo1u + ys1202*xo2u) * (1 + pi95) + (ys1201*xo1d + ys1202*xo2d) * (1 + pi145),
pi121 == (ys1211*xo1l + ys1212*xo2l) * (1 + pi120) + (ys1211*xo1r + ys1212*xo2r) * (1 + pi122) + (ys1211*xo1u + ys1212*xo2u) * (1 + pi96) + (ys1211*xo1d + ys1212*xo2d) * (1 + pi146),
pi122 == (ys1221*xo1l + ys1222*xo2l) * (1 + pi121) + (ys1221*xo1r + ys1222*xo2r) * (1 + pi123) + (ys1221*xo1u + ys1222*xo2u) * (1 + pi97) + (ys1221*xo1d + ys1222*xo2d) * (1 + pi147),
pi123 == (ys1231*xo1l + ys1232*xo2l) * (1 + pi122) + (ys1231*xo1r + ys1232*xo2r) * (1 + pi124) + (ys1231*xo1u + ys1232*xo2u) * (1 + pi98) + (ys1231*xo1d + ys1232*xo2d) * (1 + pi148),
pi124 == (ys1241*xo1l + ys1242*xo2l) * (1 + pi123) + (ys1241*xo1r + ys1242*xo2r) * (1 + pi124) + (ys1241*xo1u + ys1242*xo2u) * (1 + pi99) + (ys1241*xo1d + ys1242*xo2d) * (1 + pi149),
pi125 == (ys1251*xo1l + ys1252*xo2l) * (1 + pi125) + (ys1251*xo1r + ys1252*xo2r) * (1 + pi126) + (ys1251*xo1u + ys1252*xo2u) * (1 + pi100) + (ys1251*xo1d + ys1252*xo2d) * (1 + pi150),
pi126 == (ys1261*xo1l + ys1262*xo2l) * (1 + pi125) + (ys1261*xo1r + ys1262*xo2r) * (1 + pi127) + (ys1261*xo1u + ys1262*xo2u) * (1 + pi101) + (ys1261*xo1d + ys1262*xo2d) * (1 + pi151),
pi127 == (ys1271*xo1l + ys1272*xo2l) * (1 + pi126) + (ys1271*xo1r + ys1272*xo2r) * (1 + pi128) + (ys1271*xo1u + ys1272*xo2u) * (1 + pi102) + (ys1271*xo1d + ys1272*xo2d) * (1 + pi152),
pi128 == (ys1281*xo1l + ys1282*xo2l) * (1 + pi127) + (ys1281*xo1r + ys1282*xo2r) * (1 + pi129) + (ys1281*xo1u + ys1282*xo2u) * (1 + pi103) + (ys1281*xo1d + ys1282*xo2d) * (1 + pi153),
pi129 == (ys1291*xo1l + ys1292*xo2l) * (1 + pi128) + (ys1291*xo1r + ys1292*xo2r) * (1 + pi130) + (ys1291*xo1u + ys1292*xo2u) * (1 + pi104) + (ys1291*xo1d + ys1292*xo2d) * (1 + pi154),
pi130 == (ys1301*xo1l + ys1302*xo2l) * (1 + pi129) + (ys1301*xo1r + ys1302*xo2r) * (1 + pi131) + (ys1301*xo1u + ys1302*xo2u) * (1 + pi105) + (ys1301*xo1d + ys1302*xo2d) * (1 + pi155),
pi131 == (ys1311*xo1l + ys1312*xo2l) * (1 + pi130) + (ys1311*xo1r + ys1312*xo2r) * (1 + pi132) + (ys1311*xo1u + ys1312*xo2u) * (1 + pi106) + (ys1311*xo1d + ys1312*xo2d) * (1 + pi156),
pi132 == (ys1321*xo1l + ys1322*xo2l) * (1 + pi131) + (ys1321*xo1r + ys1322*xo2r) * (1 + pi133) + (ys1321*xo1u + ys1322*xo2u) * (1 + pi107) + (ys1321*xo1d + ys1322*xo2d) * (1 + pi157),
pi133 == (ys1331*xo1l + ys1332*xo2l) * (1 + pi132) + (ys1331*xo1r + ys1332*xo2r) * (1 + pi134) + (ys1331*xo1u + ys1332*xo2u) * (1 + pi108) + (ys1331*xo1d + ys1332*xo2d) * (1 + pi158),
pi134 == (ys1341*xo1l + ys1342*xo2l) * (1 + pi133) + (ys1341*xo1r + ys1342*xo2r) * (1 + pi135) + (ys1341*xo1u + ys1342*xo2u) * (1 + pi109) + (ys1341*xo1d + ys1342*xo2d) * (1 + pi159),
pi135 == (ys1351*xo1l + ys1352*xo2l) * (1 + pi134) + (ys1351*xo1r + ys1352*xo2r) * (1 + pi136) + (ys1351*xo1u + ys1352*xo2u) * (1 + pi110) + (ys1351*xo1d + ys1352*xo2d) * (1 + pi160),
pi136 == (ys1361*xo1l + ys1362*xo2l) * (1 + pi135) + (ys1361*xo1r + ys1362*xo2r) * (1 + pi137) + (ys1361*xo1u + ys1362*xo2u) * (1 + pi111) + (ys1361*xo1d + ys1362*xo2d) * (1 + pi161),
pi137 == (ys1371*xo1l + ys1372*xo2l) * (1 + pi136) + (ys1371*xo1r + ys1372*xo2r) * (1 + pi138) + (ys1371*xo1u + ys1372*xo2u) * (1 + pi112) + (ys1371*xo1d + ys1372*xo2d) * (1 + pi162),
pi138 == (ys1381*xo1l + ys1382*xo2l) * (1 + pi137) + (ys1381*xo1r + ys1382*xo2r) * (1 + pi139) + (ys1381*xo1u + ys1382*xo2u) * (1 + pi113) + (ys1381*xo1d + ys1382*xo2d) * (1 + pi163),
pi139 == (ys1391*xo1l + ys1392*xo2l) * (1 + pi138) + (ys1391*xo1r + ys1392*xo2r) * (1 + pi140) + (ys1391*xo1u + ys1392*xo2u) * (1 + pi114) + (ys1391*xo1d + ys1392*xo2d) * (1 + pi164),
pi140 == (ys1401*xo1l + ys1402*xo2l) * (1 + pi139) + (ys1401*xo1r + ys1402*xo2r) * (1 + pi141) + (ys1401*xo1u + ys1402*xo2u) * (1 + pi115) + (ys1401*xo1d + ys1402*xo2d) * (1 + pi165),
pi141 == (ys1411*xo1l + ys1412*xo2l) * (1 + pi140) + (ys1411*xo1r + ys1412*xo2r) * (1 + pi142) + (ys1411*xo1u + ys1412*xo2u) * (1 + pi116) + (ys1411*xo1d + ys1412*xo2d) * (1 + pi166),
pi142 == (ys1421*xo1l + ys1422*xo2l) * (1 + pi141) + (ys1421*xo1r + ys1422*xo2r) * (1 + pi143) + (ys1421*xo1u + ys1422*xo2u) * (1 + pi117) + (ys1421*xo1d + ys1422*xo2d) * (1 + pi167),
pi143 == (ys1431*xo1l + ys1432*xo2l) * (1 + pi142) + (ys1431*xo1r + ys1432*xo2r) * (1 + pi144) + (ys1431*xo1u + ys1432*xo2u) * (1 + pi118) + (ys1431*xo1d + ys1432*xo2d) * (1 + pi168),
pi144 == (ys1441*xo1l + ys1442*xo2l) * (1 + pi143) + (ys1441*xo1r + ys1442*xo2r) * (1 + pi145) + (ys1441*xo1u + ys1442*xo2u) * (1 + pi119) + (ys1441*xo1d + ys1442*xo2d) * (1 + pi169),
pi145 == (ys1451*xo1l + ys1452*xo2l) * (1 + pi144) + (ys1451*xo1r + ys1452*xo2r) * (1 + pi146) + (ys1451*xo1u + ys1452*xo2u) * (1 + pi120) + (ys1451*xo1d + ys1452*xo2d) * (1 + pi170),
pi146 == (ys1461*xo1l + ys1462*xo2l) * (1 + pi145) + (ys1461*xo1r + ys1462*xo2r) * (1 + pi147) + (ys1461*xo1u + ys1462*xo2u) * (1 + pi121) + (ys1461*xo1d + ys1462*xo2d) * (1 + pi171),
pi147 == (ys1471*xo1l + ys1472*xo2l) * (1 + pi146) + (ys1471*xo1r + ys1472*xo2r) * (1 + pi148) + (ys1471*xo1u + ys1472*xo2u) * (1 + pi122) + (ys1471*xo1d + ys1472*xo2d) * (1 + pi172),
pi148 == (ys1481*xo1l + ys1482*xo2l) * (1 + pi147) + (ys1481*xo1r + ys1482*xo2r) * (1 + pi149) + (ys1481*xo1u + ys1482*xo2u) * (1 + pi123) + (ys1481*xo1d + ys1482*xo2d) * (1 + pi173),
pi149 == (ys1491*xo1l + ys1492*xo2l) * (1 + pi148) + (ys1491*xo1r + ys1492*xo2r) * (1 + pi149) + (ys1491*xo1u + ys1492*xo2u) * (1 + pi124) + (ys1491*xo1d + ys1492*xo2d) * (1 + pi174),
pi150 == (ys1501*xo1l + ys1502*xo2l) * (1 + pi150) + (ys1501*xo1r + ys1502*xo2r) * (1 + pi151) + (ys1501*xo1u + ys1502*xo2u) * (1 + pi125) + (ys1501*xo1d + ys1502*xo2d) * (1 + pi175),
pi151 == (ys1511*xo1l + ys1512*xo2l) * (1 + pi150) + (ys1511*xo1r + ys1512*xo2r) * (1 + pi152) + (ys1511*xo1u + ys1512*xo2u) * (1 + pi126) + (ys1511*xo1d + ys1512*xo2d) * (1 + pi176),
pi152 == (ys1521*xo1l + ys1522*xo2l) * (1 + pi151) + (ys1521*xo1r + ys1522*xo2r) * (1 + pi153) + (ys1521*xo1u + ys1522*xo2u) * (1 + pi127) + (ys1521*xo1d + ys1522*xo2d) * (1 + pi177),
pi153 == (ys1531*xo1l + ys1532*xo2l) * (1 + pi152) + (ys1531*xo1r + ys1532*xo2r) * (1 + pi154) + (ys1531*xo1u + ys1532*xo2u) * (1 + pi128) + (ys1531*xo1d + ys1532*xo2d) * (1 + pi178),
pi154 == (ys1541*xo1l + ys1542*xo2l) * (1 + pi153) + (ys1541*xo1r + ys1542*xo2r) * (1 + pi155) + (ys1541*xo1u + ys1542*xo2u) * (1 + pi129) + (ys1541*xo1d + ys1542*xo2d) * (1 + pi179),
pi155 == (ys1551*xo1l + ys1552*xo2l) * (1 + pi154) + (ys1551*xo1r + ys1552*xo2r) * (1 + pi156) + (ys1551*xo1u + ys1552*xo2u) * (1 + pi130) + (ys1551*xo1d + ys1552*xo2d) * (1 + pi180),
pi156 == (ys1561*xo1l + ys1562*xo2l) * (1 + pi155) + (ys1561*xo1r + ys1562*xo2r) * (1 + pi157) + (ys1561*xo1u + ys1562*xo2u) * (1 + pi131) + (ys1561*xo1d + ys1562*xo2d) * (1 + pi181),
pi157 == (ys1571*xo1l + ys1572*xo2l) * (1 + pi156) + (ys1571*xo1r + ys1572*xo2r) * (1 + pi158) + (ys1571*xo1u + ys1572*xo2u) * (1 + pi132) + (ys1571*xo1d + ys1572*xo2d) * (1 + pi182),
pi158 == (ys1581*xo1l + ys1582*xo2l) * (1 + pi157) + (ys1581*xo1r + ys1582*xo2r) * (1 + pi159) + (ys1581*xo1u + ys1582*xo2u) * (1 + pi133) + (ys1581*xo1d + ys1582*xo2d) * (1 + pi183),
pi159 == (ys1591*xo1l + ys1592*xo2l) * (1 + pi158) + (ys1591*xo1r + ys1592*xo2r) * (1 + pi160) + (ys1591*xo1u + ys1592*xo2u) * (1 + pi134) + (ys1591*xo1d + ys1592*xo2d) * (1 + pi184),
pi160 == (ys1601*xo1l + ys1602*xo2l) * (1 + pi159) + (ys1601*xo1r + ys1602*xo2r) * (1 + pi161) + (ys1601*xo1u + ys1602*xo2u) * (1 + pi135) + (ys1601*xo1d + ys1602*xo2d) * (1 + pi185),
pi161 == (ys1611*xo1l + ys1612*xo2l) * (1 + pi160) + (ys1611*xo1r + ys1612*xo2r) * (1 + pi162) + (ys1611*xo1u + ys1612*xo2u) * (1 + pi136) + (ys1611*xo1d + ys1612*xo2d) * (1 + pi186),
pi162 == (ys1621*xo1l + ys1622*xo2l) * (1 + pi161) + (ys1621*xo1r + ys1622*xo2r) * (1 + pi163) + (ys1621*xo1u + ys1622*xo2u) * (1 + pi137) + (ys1621*xo1d + ys1622*xo2d) * (1 + pi187),
pi163 == (ys1631*xo1l + ys1632*xo2l) * (1 + pi162) + (ys1631*xo1r + ys1632*xo2r) * (1 + pi164) + (ys1631*xo1u + ys1632*xo2u) * (1 + pi138) + (ys1631*xo1d + ys1632*xo2d) * (1 + pi188),
pi164 == (ys1641*xo1l + ys1642*xo2l) * (1 + pi163) + (ys1641*xo1r + ys1642*xo2r) * (1 + pi165) + (ys1641*xo1u + ys1642*xo2u) * (1 + pi139) + (ys1641*xo1d + ys1642*xo2d) * (1 + pi189),
pi165 == (ys1651*xo1l + ys1652*xo2l) * (1 + pi164) + (ys1651*xo1r + ys1652*xo2r) * (1 + pi166) + (ys1651*xo1u + ys1652*xo2u) * (1 + pi140) + (ys1651*xo1d + ys1652*xo2d) * (1 + pi190),
pi166 == (ys1661*xo1l + ys1662*xo2l) * (1 + pi165) + (ys1661*xo1r + ys1662*xo2r) * (1 + pi167) + (ys1661*xo1u + ys1662*xo2u) * (1 + pi141) + (ys1661*xo1d + ys1662*xo2d) * (1 + pi191),
pi167 == (ys1671*xo1l + ys1672*xo2l) * (1 + pi166) + (ys1671*xo1r + ys1672*xo2r) * (1 + pi168) + (ys1671*xo1u + ys1672*xo2u) * (1 + pi142) + (ys1671*xo1d + ys1672*xo2d) * (1 + pi192),
pi168 == (ys1681*xo1l + ys1682*xo2l) * (1 + pi167) + (ys1681*xo1r + ys1682*xo2r) * (1 + pi169) + (ys1681*xo1u + ys1682*xo2u) * (1 + pi143) + (ys1681*xo1d + ys1682*xo2d) * (1 + pi193),
pi169 == (ys1691*xo1l + ys1692*xo2l) * (1 + pi168) + (ys1691*xo1r + ys1692*xo2r) * (1 + pi170) + (ys1691*xo1u + ys1692*xo2u) * (1 + pi144) + (ys1691*xo1d + ys1692*xo2d) * (1 + pi194),
pi170 == (ys1701*xo1l + ys1702*xo2l) * (1 + pi169) + (ys1701*xo1r + ys1702*xo2r) * (1 + pi171) + (ys1701*xo1u + ys1702*xo2u) * (1 + pi145) + (ys1701*xo1d + ys1702*xo2d) * (1 + pi195),
pi171 == (ys1711*xo1l + ys1712*xo2l) * (1 + pi170) + (ys1711*xo1r + ys1712*xo2r) * (1 + pi172) + (ys1711*xo1u + ys1712*xo2u) * (1 + pi146) + (ys1711*xo1d + ys1712*xo2d) * (1 + pi196),
pi172 == (ys1721*xo1l + ys1722*xo2l) * (1 + pi171) + (ys1721*xo1r + ys1722*xo2r) * (1 + pi173) + (ys1721*xo1u + ys1722*xo2u) * (1 + pi147) + (ys1721*xo1d + ys1722*xo2d) * (1 + pi197),
pi173 == (ys1731*xo1l + ys1732*xo2l) * (1 + pi172) + (ys1731*xo1r + ys1732*xo2r) * (1 + pi174) + (ys1731*xo1u + ys1732*xo2u) * (1 + pi148) + (ys1731*xo1d + ys1732*xo2d) * (1 + pi198),
pi174 == (ys1741*xo1l + ys1742*xo2l) * (1 + pi173) + (ys1741*xo1r + ys1742*xo2r) * (1 + pi174) + (ys1741*xo1u + ys1742*xo2u) * (1 + pi149) + (ys1741*xo1d + ys1742*xo2d) * (1 + pi199),
pi175 == (ys1751*xo1l + ys1752*xo2l) * (1 + pi175) + (ys1751*xo1r + ys1752*xo2r) * (1 + pi176) + (ys1751*xo1u + ys1752*xo2u) * (1 + pi150) + (ys1751*xo1d + ys1752*xo2d) * (1 + pi200),
pi176 == (ys1761*xo1l + ys1762*xo2l) * (1 + pi175) + (ys1761*xo1r + ys1762*xo2r) * (1 + pi177) + (ys1761*xo1u + ys1762*xo2u) * (1 + pi151) + (ys1761*xo1d + ys1762*xo2d) * (1 + pi201),
pi177 == (ys1771*xo1l + ys1772*xo2l) * (1 + pi176) + (ys1771*xo1r + ys1772*xo2r) * (1 + pi178) + (ys1771*xo1u + ys1772*xo2u) * (1 + pi152) + (ys1771*xo1d + ys1772*xo2d) * (1 + pi202),
pi178 == (ys1781*xo1l + ys1782*xo2l) * (1 + pi177) + (ys1781*xo1r + ys1782*xo2r) * (1 + pi179) + (ys1781*xo1u + ys1782*xo2u) * (1 + pi153) + (ys1781*xo1d + ys1782*xo2d) * (1 + pi203),
pi179 == (ys1791*xo1l + ys1792*xo2l) * (1 + pi178) + (ys1791*xo1r + ys1792*xo2r) * (1 + pi180) + (ys1791*xo1u + ys1792*xo2u) * (1 + pi154) + (ys1791*xo1d + ys1792*xo2d) * (1 + pi204),
pi180 == (ys1801*xo1l + ys1802*xo2l) * (1 + pi179) + (ys1801*xo1r + ys1802*xo2r) * (1 + pi181) + (ys1801*xo1u + ys1802*xo2u) * (1 + pi155) + (ys1801*xo1d + ys1802*xo2d) * (1 + pi205),
pi181 == (ys1811*xo1l + ys1812*xo2l) * (1 + pi180) + (ys1811*xo1r + ys1812*xo2r) * (1 + pi182) + (ys1811*xo1u + ys1812*xo2u) * (1 + pi156) + (ys1811*xo1d + ys1812*xo2d) * (1 + pi206),
pi182 == (ys1821*xo1l + ys1822*xo2l) * (1 + pi181) + (ys1821*xo1r + ys1822*xo2r) * (1 + pi183) + (ys1821*xo1u + ys1822*xo2u) * (1 + pi157) + (ys1821*xo1d + ys1822*xo2d) * (1 + pi207),
pi183 == (ys1831*xo1l + ys1832*xo2l) * (1 + pi182) + (ys1831*xo1r + ys1832*xo2r) * (1 + pi184) + (ys1831*xo1u + ys1832*xo2u) * (1 + pi158) + (ys1831*xo1d + ys1832*xo2d) * (1 + pi208),
pi184 == (ys1841*xo1l + ys1842*xo2l) * (1 + pi183) + (ys1841*xo1r + ys1842*xo2r) * (1 + pi185) + (ys1841*xo1u + ys1842*xo2u) * (1 + pi159) + (ys1841*xo1d + ys1842*xo2d) * (1 + pi209),
pi185 == (ys1851*xo1l + ys1852*xo2l) * (1 + pi184) + (ys1851*xo1r + ys1852*xo2r) * (1 + pi186) + (ys1851*xo1u + ys1852*xo2u) * (1 + pi160) + (ys1851*xo1d + ys1852*xo2d) * (1 + pi210),
pi186 == (ys1861*xo1l + ys1862*xo2l) * (1 + pi185) + (ys1861*xo1r + ys1862*xo2r) * (1 + pi187) + (ys1861*xo1u + ys1862*xo2u) * (1 + pi161) + (ys1861*xo1d + ys1862*xo2d) * (1 + pi211),
pi187 == (ys1871*xo1l + ys1872*xo2l) * (1 + pi186) + (ys1871*xo1r + ys1872*xo2r) * (1 + pi188) + (ys1871*xo1u + ys1872*xo2u) * (1 + pi162) + (ys1871*xo1d + ys1872*xo2d) * (1 + pi212),
pi188 == (ys1881*xo1l + ys1882*xo2l) * (1 + pi187) + (ys1881*xo1r + ys1882*xo2r) * (1 + pi189) + (ys1881*xo1u + ys1882*xo2u) * (1 + pi163) + (ys1881*xo1d + ys1882*xo2d) * (1 + pi213),
pi189 == (ys1891*xo1l + ys1892*xo2l) * (1 + pi188) + (ys1891*xo1r + ys1892*xo2r) * (1 + pi190) + (ys1891*xo1u + ys1892*xo2u) * (1 + pi164) + (ys1891*xo1d + ys1892*xo2d) * (1 + pi214),
pi190 == (ys1901*xo1l + ys1902*xo2l) * (1 + pi189) + (ys1901*xo1r + ys1902*xo2r) * (1 + pi191) + (ys1901*xo1u + ys1902*xo2u) * (1 + pi165) + (ys1901*xo1d + ys1902*xo2d) * (1 + pi215),
pi191 == (ys1911*xo1l + ys1912*xo2l) * (1 + pi190) + (ys1911*xo1r + ys1912*xo2r) * (1 + pi192) + (ys1911*xo1u + ys1912*xo2u) * (1 + pi166) + (ys1911*xo1d + ys1912*xo2d) * (1 + pi216),
pi192 == (ys1921*xo1l + ys1922*xo2l) * (1 + pi191) + (ys1921*xo1r + ys1922*xo2r) * (1 + pi193) + (ys1921*xo1u + ys1922*xo2u) * (1 + pi167) + (ys1921*xo1d + ys1922*xo2d) * (1 + pi217),
pi193 == (ys1931*xo1l + ys1932*xo2l) * (1 + pi192) + (ys1931*xo1r + ys1932*xo2r) * (1 + pi194) + (ys1931*xo1u + ys1932*xo2u) * (1 + pi168) + (ys1931*xo1d + ys1932*xo2d) * (1 + pi218),
pi194 == (ys1941*xo1l + ys1942*xo2l) * (1 + pi193) + (ys1941*xo1r + ys1942*xo2r) * (1 + pi195) + (ys1941*xo1u + ys1942*xo2u) * (1 + pi169) + (ys1941*xo1d + ys1942*xo2d) * (1 + pi219),
pi195 == (ys1951*xo1l + ys1952*xo2l) * (1 + pi194) + (ys1951*xo1r + ys1952*xo2r) * (1 + pi196) + (ys1951*xo1u + ys1952*xo2u) * (1 + pi170) + (ys1951*xo1d + ys1952*xo2d) * (1 + pi220),
pi196 == (ys1961*xo1l + ys1962*xo2l) * (1 + pi195) + (ys1961*xo1r + ys1962*xo2r) * (1 + pi197) + (ys1961*xo1u + ys1962*xo2u) * (1 + pi171) + (ys1961*xo1d + ys1962*xo2d) * (1 + pi221),
pi197 == (ys1971*xo1l + ys1972*xo2l) * (1 + pi196) + (ys1971*xo1r + ys1972*xo2r) * (1 + pi198) + (ys1971*xo1u + ys1972*xo2u) * (1 + pi172) + (ys1971*xo1d + ys1972*xo2d) * (1 + pi222),
pi198 == (ys1981*xo1l + ys1982*xo2l) * (1 + pi197) + (ys1981*xo1r + ys1982*xo2r) * (1 + pi199) + (ys1981*xo1u + ys1982*xo2u) * (1 + pi173) + (ys1981*xo1d + ys1982*xo2d) * (1 + pi223),
pi199 == (ys1991*xo1l + ys1992*xo2l) * (1 + pi198) + (ys1991*xo1r + ys1992*xo2r) * (1 + pi199) + (ys1991*xo1u + ys1992*xo2u) * (1 + pi174) + (ys1991*xo1d + ys1992*xo2d) * (1 + pi224),
pi200 == (ys2001*xo1l + ys2002*xo2l) * (1 + pi200) + (ys2001*xo1r + ys2002*xo2r) * (1 + pi201) + (ys2001*xo1u + ys2002*xo2u) * (1 + pi175) + (ys2001*xo1d + ys2002*xo2d) * (1 + pi225),
pi201 == (ys2011*xo1l + ys2012*xo2l) * (1 + pi200) + (ys2011*xo1r + ys2012*xo2r) * (1 + pi202) + (ys2011*xo1u + ys2012*xo2u) * (1 + pi176) + (ys2011*xo1d + ys2012*xo2d) * (1 + pi226),
pi202 == (ys2021*xo1l + ys2022*xo2l) * (1 + pi201) + (ys2021*xo1r + ys2022*xo2r) * (1 + pi203) + (ys2021*xo1u + ys2022*xo2u) * (1 + pi177) + (ys2021*xo1d + ys2022*xo2d) * (1 + pi227),
pi203 == (ys2031*xo1l + ys2032*xo2l) * (1 + pi202) + (ys2031*xo1r + ys2032*xo2r) * (1 + pi204) + (ys2031*xo1u + ys2032*xo2u) * (1 + pi178) + (ys2031*xo1d + ys2032*xo2d) * (1 + pi228),
pi204 == (ys2041*xo1l + ys2042*xo2l) * (1 + pi203) + (ys2041*xo1r + ys2042*xo2r) * (1 + pi205) + (ys2041*xo1u + ys2042*xo2u) * (1 + pi179) + (ys2041*xo1d + ys2042*xo2d) * (1 + pi229),
pi205 == (ys2051*xo1l + ys2052*xo2l) * (1 + pi204) + (ys2051*xo1r + ys2052*xo2r) * (1 + pi206) + (ys2051*xo1u + ys2052*xo2u) * (1 + pi180) + (ys2051*xo1d + ys2052*xo2d) * (1 + pi230),
pi206 == (ys2061*xo1l + ys2062*xo2l) * (1 + pi205) + (ys2061*xo1r + ys2062*xo2r) * (1 + pi207) + (ys2061*xo1u + ys2062*xo2u) * (1 + pi181) + (ys2061*xo1d + ys2062*xo2d) * (1 + pi231),
pi207 == (ys2071*xo1l + ys2072*xo2l) * (1 + pi206) + (ys2071*xo1r + ys2072*xo2r) * (1 + pi208) + (ys2071*xo1u + ys2072*xo2u) * (1 + pi182) + (ys2071*xo1d + ys2072*xo2d) * (1 + pi232),
pi208 == (ys2081*xo1l + ys2082*xo2l) * (1 + pi207) + (ys2081*xo1r + ys2082*xo2r) * (1 + pi209) + (ys2081*xo1u + ys2082*xo2u) * (1 + pi183) + (ys2081*xo1d + ys2082*xo2d) * (1 + pi233),
pi209 == (ys2091*xo1l + ys2092*xo2l) * (1 + pi208) + (ys2091*xo1r + ys2092*xo2r) * (1 + pi210) + (ys2091*xo1u + ys2092*xo2u) * (1 + pi184) + (ys2091*xo1d + ys2092*xo2d) * (1 + pi234),
pi210 == (ys2101*xo1l + ys2102*xo2l) * (1 + pi209) + (ys2101*xo1r + ys2102*xo2r) * (1 + pi211) + (ys2101*xo1u + ys2102*xo2u) * (1 + pi185) + (ys2101*xo1d + ys2102*xo2d) * (1 + pi235),
pi211 == (ys2111*xo1l + ys2112*xo2l) * (1 + pi210) + (ys2111*xo1r + ys2112*xo2r) * (1 + pi212) + (ys2111*xo1u + ys2112*xo2u) * (1 + pi186) + (ys2111*xo1d + ys2112*xo2d) * (1 + pi236),
pi212 == (ys2121*xo1l + ys2122*xo2l) * (1 + pi211) + (ys2121*xo1r + ys2122*xo2r) * (1 + pi213) + (ys2121*xo1u + ys2122*xo2u) * (1 + pi187) + (ys2121*xo1d + ys2122*xo2d) * (1 + pi237),
pi213 == (ys2131*xo1l + ys2132*xo2l) * (1 + pi212) + (ys2131*xo1r + ys2132*xo2r) * (1 + pi214) + (ys2131*xo1u + ys2132*xo2u) * (1 + pi188) + (ys2131*xo1d + ys2132*xo2d) * (1 + pi238),
pi214 == (ys2141*xo1l + ys2142*xo2l) * (1 + pi213) + (ys2141*xo1r + ys2142*xo2r) * (1 + pi215) + (ys2141*xo1u + ys2142*xo2u) * (1 + pi189) + (ys2141*xo1d + ys2142*xo2d) * (1 + pi239),
pi215 == (ys2151*xo1l + ys2152*xo2l) * (1 + pi214) + (ys2151*xo1r + ys2152*xo2r) * (1 + pi216) + (ys2151*xo1u + ys2152*xo2u) * (1 + pi190) + (ys2151*xo1d + ys2152*xo2d) * (1 + pi240),
pi216 == (ys2161*xo1l + ys2162*xo2l) * (1 + pi215) + (ys2161*xo1r + ys2162*xo2r) * (1 + pi217) + (ys2161*xo1u + ys2162*xo2u) * (1 + pi191) + (ys2161*xo1d + ys2162*xo2d) * (1 + pi241),
pi217 == (ys2171*xo1l + ys2172*xo2l) * (1 + pi216) + (ys2171*xo1r + ys2172*xo2r) * (1 + pi218) + (ys2171*xo1u + ys2172*xo2u) * (1 + pi192) + (ys2171*xo1d + ys2172*xo2d) * (1 + pi242),
pi218 == (ys2181*xo1l + ys2182*xo2l) * (1 + pi217) + (ys2181*xo1r + ys2182*xo2r) * (1 + pi219) + (ys2181*xo1u + ys2182*xo2u) * (1 + pi193) + (ys2181*xo1d + ys2182*xo2d) * (1 + pi243),
pi219 == (ys2191*xo1l + ys2192*xo2l) * (1 + pi218) + (ys2191*xo1r + ys2192*xo2r) * (1 + pi220) + (ys2191*xo1u + ys2192*xo2u) * (1 + pi194) + (ys2191*xo1d + ys2192*xo2d) * (1 + pi244),
pi220 == (ys2201*xo1l + ys2202*xo2l) * (1 + pi219) + (ys2201*xo1r + ys2202*xo2r) * (1 + pi221) + (ys2201*xo1u + ys2202*xo2u) * (1 + pi195) + (ys2201*xo1d + ys2202*xo2d) * (1 + pi245),
pi221 == (ys2211*xo1l + ys2212*xo2l) * (1 + pi220) + (ys2211*xo1r + ys2212*xo2r) * (1 + pi222) + (ys2211*xo1u + ys2212*xo2u) * (1 + pi196) + (ys2211*xo1d + ys2212*xo2d) * (1 + pi246),
pi222 == (ys2221*xo1l + ys2222*xo2l) * (1 + pi221) + (ys2221*xo1r + ys2222*xo2r) * (1 + pi223) + (ys2221*xo1u + ys2222*xo2u) * (1 + pi197) + (ys2221*xo1d + ys2222*xo2d) * (1 + pi247),
pi223 == (ys2231*xo1l + ys2232*xo2l) * (1 + pi222) + (ys2231*xo1r + ys2232*xo2r) * (1 + pi224) + (ys2231*xo1u + ys2232*xo2u) * (1 + pi198) + (ys2231*xo1d + ys2232*xo2d) * (1 + pi248),
pi224 == (ys2241*xo1l + ys2242*xo2l) * (1 + pi223) + (ys2241*xo1r + ys2242*xo2r) * (1 + pi224) + (ys2241*xo1u + ys2242*xo2u) * (1 + pi199) + (ys2241*xo1d + ys2242*xo2d) * (1 + pi249),
pi225 == (ys2251*xo1l + ys2252*xo2l) * (1 + pi225) + (ys2251*xo1r + ys2252*xo2r) * (1 + pi226) + (ys2251*xo1u + ys2252*xo2u) * (1 + pi200) + (ys2251*xo1d + ys2252*xo2d) * (1 + pi250),
pi226 == (ys2261*xo1l + ys2262*xo2l) * (1 + pi225) + (ys2261*xo1r + ys2262*xo2r) * (1 + pi227) + (ys2261*xo1u + ys2262*xo2u) * (1 + pi201) + (ys2261*xo1d + ys2262*xo2d) * (1 + pi251),
pi227 == (ys2271*xo1l + ys2272*xo2l) * (1 + pi226) + (ys2271*xo1r + ys2272*xo2r) * (1 + pi228) + (ys2271*xo1u + ys2272*xo2u) * (1 + pi202) + (ys2271*xo1d + ys2272*xo2d) * (1 + pi252),
pi228 == (ys2281*xo1l + ys2282*xo2l) * (1 + pi227) + (ys2281*xo1r + ys2282*xo2r) * (1 + pi229) + (ys2281*xo1u + ys2282*xo2u) * (1 + pi203) + (ys2281*xo1d + ys2282*xo2d) * (1 + pi253),
pi229 == (ys2291*xo1l + ys2292*xo2l) * (1 + pi228) + (ys2291*xo1r + ys2292*xo2r) * (1 + pi230) + (ys2291*xo1u + ys2292*xo2u) * (1 + pi204) + (ys2291*xo1d + ys2292*xo2d) * (1 + pi254),
pi230 == (ys2301*xo1l + ys2302*xo2l) * (1 + pi229) + (ys2301*xo1r + ys2302*xo2r) * (1 + pi231) + (ys2301*xo1u + ys2302*xo2u) * (1 + pi205) + (ys2301*xo1d + ys2302*xo2d) * (1 + pi255),
pi231 == (ys2311*xo1l + ys2312*xo2l) * (1 + pi230) + (ys2311*xo1r + ys2312*xo2r) * (1 + pi232) + (ys2311*xo1u + ys2312*xo2u) * (1 + pi206) + (ys2311*xo1d + ys2312*xo2d) * (1 + pi256),
pi232 == (ys2321*xo1l + ys2322*xo2l) * (1 + pi231) + (ys2321*xo1r + ys2322*xo2r) * (1 + pi233) + (ys2321*xo1u + ys2322*xo2u) * (1 + pi207) + (ys2321*xo1d + ys2322*xo2d) * (1 + pi257),
pi233 == (ys2331*xo1l + ys2332*xo2l) * (1 + pi232) + (ys2331*xo1r + ys2332*xo2r) * (1 + pi234) + (ys2331*xo1u + ys2332*xo2u) * (1 + pi208) + (ys2331*xo1d + ys2332*xo2d) * (1 + pi258),
pi234 == (ys2341*xo1l + ys2342*xo2l) * (1 + pi233) + (ys2341*xo1r + ys2342*xo2r) * (1 + pi235) + (ys2341*xo1u + ys2342*xo2u) * (1 + pi209) + (ys2341*xo1d + ys2342*xo2d) * (1 + pi259),
pi235 == (ys2351*xo1l + ys2352*xo2l) * (1 + pi234) + (ys2351*xo1r + ys2352*xo2r) * (1 + pi236) + (ys2351*xo1u + ys2352*xo2u) * (1 + pi210) + (ys2351*xo1d + ys2352*xo2d) * (1 + pi260),
pi236 == (ys2361*xo1l + ys2362*xo2l) * (1 + pi235) + (ys2361*xo1r + ys2362*xo2r) * (1 + pi237) + (ys2361*xo1u + ys2362*xo2u) * (1 + pi211) + (ys2361*xo1d + ys2362*xo2d) * (1 + pi261),
pi237 == (ys2371*xo1l + ys2372*xo2l) * (1 + pi236) + (ys2371*xo1r + ys2372*xo2r) * (1 + pi238) + (ys2371*xo1u + ys2372*xo2u) * (1 + pi212) + (ys2371*xo1d + ys2372*xo2d) * (1 + pi262),
pi238 == (ys2381*xo1l + ys2382*xo2l) * (1 + pi237) + (ys2381*xo1r + ys2382*xo2r) * (1 + pi239) + (ys2381*xo1u + ys2382*xo2u) * (1 + pi213) + (ys2381*xo1d + ys2382*xo2d) * (1 + pi263),
pi239 == (ys2391*xo1l + ys2392*xo2l) * (1 + pi238) + (ys2391*xo1r + ys2392*xo2r) * (1 + pi240) + (ys2391*xo1u + ys2392*xo2u) * (1 + pi214) + (ys2391*xo1d + ys2392*xo2d) * (1 + pi264),
pi240 == (ys2401*xo1l + ys2402*xo2l) * (1 + pi239) + (ys2401*xo1r + ys2402*xo2r) * (1 + pi241) + (ys2401*xo1u + ys2402*xo2u) * (1 + pi215) + (ys2401*xo1d + ys2402*xo2d) * (1 + pi265),
pi241 == (ys2411*xo1l + ys2412*xo2l) * (1 + pi240) + (ys2411*xo1r + ys2412*xo2r) * (1 + pi242) + (ys2411*xo1u + ys2412*xo2u) * (1 + pi216) + (ys2411*xo1d + ys2412*xo2d) * (1 + pi266),
pi242 == (ys2421*xo1l + ys2422*xo2l) * (1 + pi241) + (ys2421*xo1r + ys2422*xo2r) * (1 + pi243) + (ys2421*xo1u + ys2422*xo2u) * (1 + pi217) + (ys2421*xo1d + ys2422*xo2d) * (1 + pi267),
pi243 == (ys2431*xo1l + ys2432*xo2l) * (1 + pi242) + (ys2431*xo1r + ys2432*xo2r) * (1 + pi244) + (ys2431*xo1u + ys2432*xo2u) * (1 + pi218) + (ys2431*xo1d + ys2432*xo2d) * (1 + pi268),
pi244 == (ys2441*xo1l + ys2442*xo2l) * (1 + pi243) + (ys2441*xo1r + ys2442*xo2r) * (1 + pi245) + (ys2441*xo1u + ys2442*xo2u) * (1 + pi219) + (ys2441*xo1d + ys2442*xo2d) * (1 + pi269),
pi245 == (ys2451*xo1l + ys2452*xo2l) * (1 + pi244) + (ys2451*xo1r + ys2452*xo2r) * (1 + pi246) + (ys2451*xo1u + ys2452*xo2u) * (1 + pi220) + (ys2451*xo1d + ys2452*xo2d) * (1 + pi270),
pi246 == (ys2461*xo1l + ys2462*xo2l) * (1 + pi245) + (ys2461*xo1r + ys2462*xo2r) * (1 + pi247) + (ys2461*xo1u + ys2462*xo2u) * (1 + pi221) + (ys2461*xo1d + ys2462*xo2d) * (1 + pi271),
pi247 == (ys2471*xo1l + ys2472*xo2l) * (1 + pi246) + (ys2471*xo1r + ys2472*xo2r) * (1 + pi248) + (ys2471*xo1u + ys2472*xo2u) * (1 + pi222) + (ys2471*xo1d + ys2472*xo2d) * (1 + pi272),
pi248 == (ys2481*xo1l + ys2482*xo2l) * (1 + pi247) + (ys2481*xo1r + ys2482*xo2r) * (1 + pi249) + (ys2481*xo1u + ys2482*xo2u) * (1 + pi223) + (ys2481*xo1d + ys2482*xo2d) * (1 + pi273),
pi249 == (ys2491*xo1l + ys2492*xo2l) * (1 + pi248) + (ys2491*xo1r + ys2492*xo2r) * (1 + pi249) + (ys2491*xo1u + ys2492*xo2u) * (1 + pi224) + (ys2491*xo1d + ys2492*xo2d) * (1 + pi274),
pi250 == (ys2501*xo1l + ys2502*xo2l) * (1 + pi250) + (ys2501*xo1r + ys2502*xo2r) * (1 + pi251) + (ys2501*xo1u + ys2502*xo2u) * (1 + pi225) + (ys2501*xo1d + ys2502*xo2d) * (1 + pi275),
pi251 == (ys2511*xo1l + ys2512*xo2l) * (1 + pi250) + (ys2511*xo1r + ys2512*xo2r) * (1 + pi252) + (ys2511*xo1u + ys2512*xo2u) * (1 + pi226) + (ys2511*xo1d + ys2512*xo2d) * (1 + pi276),
pi252 == (ys2521*xo1l + ys2522*xo2l) * (1 + pi251) + (ys2521*xo1r + ys2522*xo2r) * (1 + pi253) + (ys2521*xo1u + ys2522*xo2u) * (1 + pi227) + (ys2521*xo1d + ys2522*xo2d) * (1 + pi277),
pi253 == (ys2531*xo1l + ys2532*xo2l) * (1 + pi252) + (ys2531*xo1r + ys2532*xo2r) * (1 + pi254) + (ys2531*xo1u + ys2532*xo2u) * (1 + pi228) + (ys2531*xo1d + ys2532*xo2d) * (1 + pi278),
pi254 == (ys2541*xo1l + ys2542*xo2l) * (1 + pi253) + (ys2541*xo1r + ys2542*xo2r) * (1 + pi255) + (ys2541*xo1u + ys2542*xo2u) * (1 + pi229) + (ys2541*xo1d + ys2542*xo2d) * (1 + pi279),
pi255 == (ys2551*xo1l + ys2552*xo2l) * (1 + pi254) + (ys2551*xo1r + ys2552*xo2r) * (1 + pi256) + (ys2551*xo1u + ys2552*xo2u) * (1 + pi230) + (ys2551*xo1d + ys2552*xo2d) * (1 + pi280),
pi256 == (ys2561*xo1l + ys2562*xo2l) * (1 + pi255) + (ys2561*xo1r + ys2562*xo2r) * (1 + pi257) + (ys2561*xo1u + ys2562*xo2u) * (1 + pi231) + (ys2561*xo1d + ys2562*xo2d) * (1 + pi281),
pi257 == (ys2571*xo1l + ys2572*xo2l) * (1 + pi256) + (ys2571*xo1r + ys2572*xo2r) * (1 + pi258) + (ys2571*xo1u + ys2572*xo2u) * (1 + pi232) + (ys2571*xo1d + ys2572*xo2d) * (1 + pi282),
pi258 == (ys2581*xo1l + ys2582*xo2l) * (1 + pi257) + (ys2581*xo1r + ys2582*xo2r) * (1 + pi259) + (ys2581*xo1u + ys2582*xo2u) * (1 + pi233) + (ys2581*xo1d + ys2582*xo2d) * (1 + pi283),
pi259 == (ys2591*xo1l + ys2592*xo2l) * (1 + pi258) + (ys2591*xo1r + ys2592*xo2r) * (1 + pi260) + (ys2591*xo1u + ys2592*xo2u) * (1 + pi234) + (ys2591*xo1d + ys2592*xo2d) * (1 + pi284),
pi260 == (ys2601*xo1l + ys2602*xo2l) * (1 + pi259) + (ys2601*xo1r + ys2602*xo2r) * (1 + pi261) + (ys2601*xo1u + ys2602*xo2u) * (1 + pi235) + (ys2601*xo1d + ys2602*xo2d) * (1 + pi285),
pi261 == (ys2611*xo1l + ys2612*xo2l) * (1 + pi260) + (ys2611*xo1r + ys2612*xo2r) * (1 + pi262) + (ys2611*xo1u + ys2612*xo2u) * (1 + pi236) + (ys2611*xo1d + ys2612*xo2d) * (1 + pi286),
pi262 == (ys2621*xo1l + ys2622*xo2l) * (1 + pi261) + (ys2621*xo1r + ys2622*xo2r) * (1 + pi263) + (ys2621*xo1u + ys2622*xo2u) * (1 + pi237) + (ys2621*xo1d + ys2622*xo2d) * (1 + pi287),
pi263 == (ys2631*xo1l + ys2632*xo2l) * (1 + pi262) + (ys2631*xo1r + ys2632*xo2r) * (1 + pi264) + (ys2631*xo1u + ys2632*xo2u) * (1 + pi238) + (ys2631*xo1d + ys2632*xo2d) * (1 + pi288),
pi264 == (ys2641*xo1l + ys2642*xo2l) * (1 + pi263) + (ys2641*xo1r + ys2642*xo2r) * (1 + pi265) + (ys2641*xo1u + ys2642*xo2u) * (1 + pi239) + (ys2641*xo1d + ys2642*xo2d) * (1 + pi289),
pi265 == (ys2651*xo1l + ys2652*xo2l) * (1 + pi264) + (ys2651*xo1r + ys2652*xo2r) * (1 + pi266) + (ys2651*xo1u + ys2652*xo2u) * (1 + pi240) + (ys2651*xo1d + ys2652*xo2d) * (1 + pi290),
pi266 == (ys2661*xo1l + ys2662*xo2l) * (1 + pi265) + (ys2661*xo1r + ys2662*xo2r) * (1 + pi267) + (ys2661*xo1u + ys2662*xo2u) * (1 + pi241) + (ys2661*xo1d + ys2662*xo2d) * (1 + pi291),
pi267 == (ys2671*xo1l + ys2672*xo2l) * (1 + pi266) + (ys2671*xo1r + ys2672*xo2r) * (1 + pi268) + (ys2671*xo1u + ys2672*xo2u) * (1 + pi242) + (ys2671*xo1d + ys2672*xo2d) * (1 + pi292),
pi268 == (ys2681*xo1l + ys2682*xo2l) * (1 + pi267) + (ys2681*xo1r + ys2682*xo2r) * (1 + pi269) + (ys2681*xo1u + ys2682*xo2u) * (1 + pi243) + (ys2681*xo1d + ys2682*xo2d) * (1 + pi293),
pi269 == (ys2691*xo1l + ys2692*xo2l) * (1 + pi268) + (ys2691*xo1r + ys2692*xo2r) * (1 + pi270) + (ys2691*xo1u + ys2692*xo2u) * (1 + pi244) + (ys2691*xo1d + ys2692*xo2d) * (1 + pi294),
pi270 == (ys2701*xo1l + ys2702*xo2l) * (1 + pi269) + (ys2701*xo1r + ys2702*xo2r) * (1 + pi271) + (ys2701*xo1u + ys2702*xo2u) * (1 + pi245) + (ys2701*xo1d + ys2702*xo2d) * (1 + pi295),
pi271 == (ys2711*xo1l + ys2712*xo2l) * (1 + pi270) + (ys2711*xo1r + ys2712*xo2r) * (1 + pi272) + (ys2711*xo1u + ys2712*xo2u) * (1 + pi246) + (ys2711*xo1d + ys2712*xo2d) * (1 + pi296),
pi272 == (ys2721*xo1l + ys2722*xo2l) * (1 + pi271) + (ys2721*xo1r + ys2722*xo2r) * (1 + pi273) + (ys2721*xo1u + ys2722*xo2u) * (1 + pi247) + (ys2721*xo1d + ys2722*xo2d) * (1 + pi297),
pi273 == (ys2731*xo1l + ys2732*xo2l) * (1 + pi272) + (ys2731*xo1r + ys2732*xo2r) * (1 + pi274) + (ys2731*xo1u + ys2732*xo2u) * (1 + pi248) + (ys2731*xo1d + ys2732*xo2d) * (1 + pi298),
pi274 == (ys2741*xo1l + ys2742*xo2l) * (1 + pi273) + (ys2741*xo1r + ys2742*xo2r) * (1 + pi274) + (ys2741*xo1u + ys2742*xo2u) * (1 + pi249) + (ys2741*xo1d + ys2742*xo2d) * (1 + pi299),
pi275 == (ys2751*xo1l + ys2752*xo2l) * (1 + pi275) + (ys2751*xo1r + ys2752*xo2r) * (1 + pi276) + (ys2751*xo1u + ys2752*xo2u) * (1 + pi250) + (ys2751*xo1d + ys2752*xo2d) * (1 + pi300),
pi276 == (ys2761*xo1l + ys2762*xo2l) * (1 + pi275) + (ys2761*xo1r + ys2762*xo2r) * (1 + pi277) + (ys2761*xo1u + ys2762*xo2u) * (1 + pi251) + (ys2761*xo1d + ys2762*xo2d) * (1 + pi301),
pi277 == (ys2771*xo1l + ys2772*xo2l) * (1 + pi276) + (ys2771*xo1r + ys2772*xo2r) * (1 + pi278) + (ys2771*xo1u + ys2772*xo2u) * (1 + pi252) + (ys2771*xo1d + ys2772*xo2d) * (1 + pi302),
pi278 == (ys2781*xo1l + ys2782*xo2l) * (1 + pi277) + (ys2781*xo1r + ys2782*xo2r) * (1 + pi279) + (ys2781*xo1u + ys2782*xo2u) * (1 + pi253) + (ys2781*xo1d + ys2782*xo2d) * (1 + pi303),
pi279 == (ys2791*xo1l + ys2792*xo2l) * (1 + pi278) + (ys2791*xo1r + ys2792*xo2r) * (1 + pi280) + (ys2791*xo1u + ys2792*xo2u) * (1 + pi254) + (ys2791*xo1d + ys2792*xo2d) * (1 + pi304),
pi280 == (ys2801*xo1l + ys2802*xo2l) * (1 + pi279) + (ys2801*xo1r + ys2802*xo2r) * (1 + pi281) + (ys2801*xo1u + ys2802*xo2u) * (1 + pi255) + (ys2801*xo1d + ys2802*xo2d) * (1 + pi305),
pi281 == (ys2811*xo1l + ys2812*xo2l) * (1 + pi280) + (ys2811*xo1r + ys2812*xo2r) * (1 + pi282) + (ys2811*xo1u + ys2812*xo2u) * (1 + pi256) + (ys2811*xo1d + ys2812*xo2d) * (1 + pi306),
pi282 == (ys2821*xo1l + ys2822*xo2l) * (1 + pi281) + (ys2821*xo1r + ys2822*xo2r) * (1 + pi283) + (ys2821*xo1u + ys2822*xo2u) * (1 + pi257) + (ys2821*xo1d + ys2822*xo2d) * (1 + pi307),
pi283 == (ys2831*xo1l + ys2832*xo2l) * (1 + pi282) + (ys2831*xo1r + ys2832*xo2r) * (1 + pi284) + (ys2831*xo1u + ys2832*xo2u) * (1 + pi258) + (ys2831*xo1d + ys2832*xo2d) * (1 + pi308),
pi284 == (ys2841*xo1l + ys2842*xo2l) * (1 + pi283) + (ys2841*xo1r + ys2842*xo2r) * (1 + pi285) + (ys2841*xo1u + ys2842*xo2u) * (1 + pi259) + (ys2841*xo1d + ys2842*xo2d) * (1 + pi309),
pi285 == (ys2851*xo1l + ys2852*xo2l) * (1 + pi284) + (ys2851*xo1r + ys2852*xo2r) * (1 + pi286) + (ys2851*xo1u + ys2852*xo2u) * (1 + pi260) + (ys2851*xo1d + ys2852*xo2d) * (1 + pi310),
pi286 == (ys2861*xo1l + ys2862*xo2l) * (1 + pi285) + (ys2861*xo1r + ys2862*xo2r) * (1 + pi287) + (ys2861*xo1u + ys2862*xo2u) * (1 + pi261) + (ys2861*xo1d + ys2862*xo2d) * (1 + pi311),
pi287 == (ys2871*xo1l + ys2872*xo2l) * (1 + pi286) + (ys2871*xo1r + ys2872*xo2r) * (1 + pi288) + (ys2871*xo1u + ys2872*xo2u) * (1 + pi262) + (ys2871*xo1d + ys2872*xo2d) * (1 + pi312),
pi288 == (ys2881*xo1l + ys2882*xo2l) * (1 + pi287) + (ys2881*xo1r + ys2882*xo2r) * (1 + pi289) + (ys2881*xo1u + ys2882*xo2u) * (1 + pi263) + (ys2881*xo1d + ys2882*xo2d) * (1 + pi313),
pi289 == (ys2891*xo1l + ys2892*xo2l) * (1 + pi288) + (ys2891*xo1r + ys2892*xo2r) * (1 + pi290) + (ys2891*xo1u + ys2892*xo2u) * (1 + pi264) + (ys2891*xo1d + ys2892*xo2d) * (1 + pi314),
pi290 == (ys2901*xo1l + ys2902*xo2l) * (1 + pi289) + (ys2901*xo1r + ys2902*xo2r) * (1 + pi291) + (ys2901*xo1u + ys2902*xo2u) * (1 + pi265) + (ys2901*xo1d + ys2902*xo2d) * (1 + pi315),
pi291 == (ys2911*xo1l + ys2912*xo2l) * (1 + pi290) + (ys2911*xo1r + ys2912*xo2r) * (1 + pi292) + (ys2911*xo1u + ys2912*xo2u) * (1 + pi266) + (ys2911*xo1d + ys2912*xo2d) * (1 + pi316),
pi292 == (ys2921*xo1l + ys2922*xo2l) * (1 + pi291) + (ys2921*xo1r + ys2922*xo2r) * (1 + pi293) + (ys2921*xo1u + ys2922*xo2u) * (1 + pi267) + (ys2921*xo1d + ys2922*xo2d) * (1 + pi317),
pi293 == (ys2931*xo1l + ys2932*xo2l) * (1 + pi292) + (ys2931*xo1r + ys2932*xo2r) * (1 + pi294) + (ys2931*xo1u + ys2932*xo2u) * (1 + pi268) + (ys2931*xo1d + ys2932*xo2d) * (1 + pi318),
pi294 == (ys2941*xo1l + ys2942*xo2l) * (1 + pi293) + (ys2941*xo1r + ys2942*xo2r) * (1 + pi295) + (ys2941*xo1u + ys2942*xo2u) * (1 + pi269) + (ys2941*xo1d + ys2942*xo2d) * (1 + pi319),
pi295 == (ys2951*xo1l + ys2952*xo2l) * (1 + pi294) + (ys2951*xo1r + ys2952*xo2r) * (1 + pi296) + (ys2951*xo1u + ys2952*xo2u) * (1 + pi270) + (ys2951*xo1d + ys2952*xo2d) * (1 + pi320),
pi296 == (ys2961*xo1l + ys2962*xo2l) * (1 + pi295) + (ys2961*xo1r + ys2962*xo2r) * (1 + pi297) + (ys2961*xo1u + ys2962*xo2u) * (1 + pi271) + (ys2961*xo1d + ys2962*xo2d) * (1 + pi321),
pi297 == (ys2971*xo1l + ys2972*xo2l) * (1 + pi296) + (ys2971*xo1r + ys2972*xo2r) * (1 + pi298) + (ys2971*xo1u + ys2972*xo2u) * (1 + pi272) + (ys2971*xo1d + ys2972*xo2d) * (1 + pi322),
pi298 == (ys2981*xo1l + ys2982*xo2l) * (1 + pi297) + (ys2981*xo1r + ys2982*xo2r) * (1 + pi299) + (ys2981*xo1u + ys2982*xo2u) * (1 + pi273) + (ys2981*xo1d + ys2982*xo2d) * (1 + pi323),
pi299 == (ys2991*xo1l + ys2992*xo2l) * (1 + pi298) + (ys2991*xo1r + ys2992*xo2r) * (1 + pi299) + (ys2991*xo1u + ys2992*xo2u) * (1 + pi274) + (ys2991*xo1d + ys2992*xo2d) * (1 + pi324),
pi300 == (ys3001*xo1l + ys3002*xo2l) * (1 + pi300) + (ys3001*xo1r + ys3002*xo2r) * (1 + pi301) + (ys3001*xo1u + ys3002*xo2u) * (1 + pi275) + (ys3001*xo1d + ys3002*xo2d) * (1 + pi325),
pi301 == (ys3011*xo1l + ys3012*xo2l) * (1 + pi300) + (ys3011*xo1r + ys3012*xo2r) * (1 + pi302) + (ys3011*xo1u + ys3012*xo2u) * (1 + pi276) + (ys3011*xo1d + ys3012*xo2d) * (1 + pi326),
pi302 == (ys3021*xo1l + ys3022*xo2l) * (1 + pi301) + (ys3021*xo1r + ys3022*xo2r) * (1 + pi303) + (ys3021*xo1u + ys3022*xo2u) * (1 + pi277) + (ys3021*xo1d + ys3022*xo2d) * (1 + pi327),
pi303 == (ys3031*xo1l + ys3032*xo2l) * (1 + pi302) + (ys3031*xo1r + ys3032*xo2r) * (1 + pi304) + (ys3031*xo1u + ys3032*xo2u) * (1 + pi278) + (ys3031*xo1d + ys3032*xo2d) * (1 + pi328),
pi304 == (ys3041*xo1l + ys3042*xo2l) * (1 + pi303) + (ys3041*xo1r + ys3042*xo2r) * (1 + pi305) + (ys3041*xo1u + ys3042*xo2u) * (1 + pi279) + (ys3041*xo1d + ys3042*xo2d) * (1 + pi329),
pi305 == (ys3051*xo1l + ys3052*xo2l) * (1 + pi304) + (ys3051*xo1r + ys3052*xo2r) * (1 + pi306) + (ys3051*xo1u + ys3052*xo2u) * (1 + pi280) + (ys3051*xo1d + ys3052*xo2d) * (1 + pi330),
pi306 == (ys3061*xo1l + ys3062*xo2l) * (1 + pi305) + (ys3061*xo1r + ys3062*xo2r) * (1 + pi307) + (ys3061*xo1u + ys3062*xo2u) * (1 + pi281) + (ys3061*xo1d + ys3062*xo2d) * (1 + pi331),
pi307 == (ys3071*xo1l + ys3072*xo2l) * (1 + pi306) + (ys3071*xo1r + ys3072*xo2r) * (1 + pi308) + (ys3071*xo1u + ys3072*xo2u) * (1 + pi282) + (ys3071*xo1d + ys3072*xo2d) * (1 + pi332),
pi308 == (ys3081*xo1l + ys3082*xo2l) * (1 + pi307) + (ys3081*xo1r + ys3082*xo2r) * (1 + pi309) + (ys3081*xo1u + ys3082*xo2u) * (1 + pi283) + (ys3081*xo1d + ys3082*xo2d) * (1 + pi333),
pi309 == (ys3091*xo1l + ys3092*xo2l) * (1 + pi308) + (ys3091*xo1r + ys3092*xo2r) * (1 + pi310) + (ys3091*xo1u + ys3092*xo2u) * (1 + pi284) + (ys3091*xo1d + ys3092*xo2d) * (1 + pi334),
pi310 == (ys3101*xo1l + ys3102*xo2l) * (1 + pi309) + (ys3101*xo1r + ys3102*xo2r) * (1 + pi311) + (ys3101*xo1u + ys3102*xo2u) * (1 + pi285) + (ys3101*xo1d + ys3102*xo2d) * (1 + pi335),
pi311 == (ys3111*xo1l + ys3112*xo2l) * (1 + pi310) + (ys3111*xo1r + ys3112*xo2r) * (1 + pi312) + (ys3111*xo1u + ys3112*xo2u) * (1 + pi286) + (ys3111*xo1d + ys3112*xo2d) * (1 + pi336),
pi312 == (ys3121*xo1l + ys3122*xo2l) * (1 + pi311) + (ys3121*xo1r + ys3122*xo2r) * (1 + pi313) + (ys3121*xo1u + ys3122*xo2u) * (1 + pi287) + (ys3121*xo1d + ys3122*xo2d) * (1 + pi337),
pi313 == (ys3131*xo1l + ys3132*xo2l) * (1 + pi312) + (ys3131*xo1r + ys3132*xo2r) * (1 + pi314) + (ys3131*xo1u + ys3132*xo2u) * (1 + pi288) + (ys3131*xo1d + ys3132*xo2d) * (1 + pi338),
pi314 == (ys3141*xo1l + ys3142*xo2l) * (1 + pi313) + (ys3141*xo1r + ys3142*xo2r) * (1 + pi315) + (ys3141*xo1u + ys3142*xo2u) * (1 + pi289) + (ys3141*xo1d + ys3142*xo2d) * (1 + pi339),
pi315 == (ys3151*xo1l + ys3152*xo2l) * (1 + pi314) + (ys3151*xo1r + ys3152*xo2r) * (1 + pi316) + (ys3151*xo1u + ys3152*xo2u) * (1 + pi290) + (ys3151*xo1d + ys3152*xo2d) * (1 + pi340),
pi316 == (ys3161*xo1l + ys3162*xo2l) * (1 + pi315) + (ys3161*xo1r + ys3162*xo2r) * (1 + pi317) + (ys3161*xo1u + ys3162*xo2u) * (1 + pi291) + (ys3161*xo1d + ys3162*xo2d) * (1 + pi341),
pi317 == (ys3171*xo1l + ys3172*xo2l) * (1 + pi316) + (ys3171*xo1r + ys3172*xo2r) * (1 + pi318) + (ys3171*xo1u + ys3172*xo2u) * (1 + pi292) + (ys3171*xo1d + ys3172*xo2d) * (1 + pi342),
pi318 == (ys3181*xo1l + ys3182*xo2l) * (1 + pi317) + (ys3181*xo1r + ys3182*xo2r) * (1 + pi319) + (ys3181*xo1u + ys3182*xo2u) * (1 + pi293) + (ys3181*xo1d + ys3182*xo2d) * (1 + pi343),
pi319 == (ys3191*xo1l + ys3192*xo2l) * (1 + pi318) + (ys3191*xo1r + ys3192*xo2r) * (1 + pi320) + (ys3191*xo1u + ys3192*xo2u) * (1 + pi294) + (ys3191*xo1d + ys3192*xo2d) * (1 + pi344),
pi320 == (ys3201*xo1l + ys3202*xo2l) * (1 + pi319) + (ys3201*xo1r + ys3202*xo2r) * (1 + pi321) + (ys3201*xo1u + ys3202*xo2u) * (1 + pi295) + (ys3201*xo1d + ys3202*xo2d) * (1 + pi345),
pi321 == (ys3211*xo1l + ys3212*xo2l) * (1 + pi320) + (ys3211*xo1r + ys3212*xo2r) * (1 + pi322) + (ys3211*xo1u + ys3212*xo2u) * (1 + pi296) + (ys3211*xo1d + ys3212*xo2d) * (1 + pi346),
pi322 == (ys3221*xo1l + ys3222*xo2l) * (1 + pi321) + (ys3221*xo1r + ys3222*xo2r) * (1 + pi323) + (ys3221*xo1u + ys3222*xo2u) * (1 + pi297) + (ys3221*xo1d + ys3222*xo2d) * (1 + pi347),
pi323 == (ys3231*xo1l + ys3232*xo2l) * (1 + pi322) + (ys3231*xo1r + ys3232*xo2r) * (1 + pi324) + (ys3231*xo1u + ys3232*xo2u) * (1 + pi298) + (ys3231*xo1d + ys3232*xo2d) * (1 + pi348),
pi324 == (ys3241*xo1l + ys3242*xo2l) * (1 + pi323) + (ys3241*xo1r + ys3242*xo2r) * (1 + pi324) + (ys3241*xo1u + ys3242*xo2u) * (1 + pi299) + (ys3241*xo1d + ys3242*xo2d) * (1 + pi349),
pi325 == (ys3251*xo1l + ys3252*xo2l) * (1 + pi325) + (ys3251*xo1r + ys3252*xo2r) * (1 + pi326) + (ys3251*xo1u + ys3252*xo2u) * (1 + pi300) + (ys3251*xo1d + ys3252*xo2d) * (1 + pi350),
pi326 == (ys3261*xo1l + ys3262*xo2l) * (1 + pi325) + (ys3261*xo1r + ys3262*xo2r) * (1 + pi327) + (ys3261*xo1u + ys3262*xo2u) * (1 + pi301) + (ys3261*xo1d + ys3262*xo2d) * (1 + pi351),
pi327 == (ys3271*xo1l + ys3272*xo2l) * (1 + pi326) + (ys3271*xo1r + ys3272*xo2r) * (1 + pi328) + (ys3271*xo1u + ys3272*xo2u) * (1 + pi302) + (ys3271*xo1d + ys3272*xo2d) * (1 + pi352),
pi328 == (ys3281*xo1l + ys3282*xo2l) * (1 + pi327) + (ys3281*xo1r + ys3282*xo2r) * (1 + pi329) + (ys3281*xo1u + ys3282*xo2u) * (1 + pi303) + (ys3281*xo1d + ys3282*xo2d) * (1 + pi353),
pi329 == (ys3291*xo1l + ys3292*xo2l) * (1 + pi328) + (ys3291*xo1r + ys3292*xo2r) * (1 + pi330) + (ys3291*xo1u + ys3292*xo2u) * (1 + pi304) + (ys3291*xo1d + ys3292*xo2d) * (1 + pi354),
pi330 == (ys3301*xo1l + ys3302*xo2l) * (1 + pi329) + (ys3301*xo1r + ys3302*xo2r) * (1 + pi331) + (ys3301*xo1u + ys3302*xo2u) * (1 + pi305) + (ys3301*xo1d + ys3302*xo2d) * (1 + pi355),
pi331 == (ys3311*xo1l + ys3312*xo2l) * (1 + pi330) + (ys3311*xo1r + ys3312*xo2r) * (1 + pi332) + (ys3311*xo1u + ys3312*xo2u) * (1 + pi306) + (ys3311*xo1d + ys3312*xo2d) * (1 + pi356),
pi332 == (ys3321*xo1l + ys3322*xo2l) * (1 + pi331) + (ys3321*xo1r + ys3322*xo2r) * (1 + pi333) + (ys3321*xo1u + ys3322*xo2u) * (1 + pi307) + (ys3321*xo1d + ys3322*xo2d) * (1 + pi357),
pi333 == (ys3331*xo1l + ys3332*xo2l) * (1 + pi332) + (ys3331*xo1r + ys3332*xo2r) * (1 + pi334) + (ys3331*xo1u + ys3332*xo2u) * (1 + pi308) + (ys3331*xo1d + ys3332*xo2d) * (1 + pi358),
pi334 == (ys3341*xo1l + ys3342*xo2l) * (1 + pi333) + (ys3341*xo1r + ys3342*xo2r) * (1 + pi335) + (ys3341*xo1u + ys3342*xo2u) * (1 + pi309) + (ys3341*xo1d + ys3342*xo2d) * (1 + pi359),
pi335 == (ys3351*xo1l + ys3352*xo2l) * (1 + pi334) + (ys3351*xo1r + ys3352*xo2r) * (1 + pi336) + (ys3351*xo1u + ys3352*xo2u) * (1 + pi310) + (ys3351*xo1d + ys3352*xo2d) * (1 + pi360),
pi336 == (ys3361*xo1l + ys3362*xo2l) * (1 + pi335) + (ys3361*xo1r + ys3362*xo2r) * (1 + pi337) + (ys3361*xo1u + ys3362*xo2u) * (1 + pi311) + (ys3361*xo1d + ys3362*xo2d) * (1 + pi361),
pi337 == (ys3371*xo1l + ys3372*xo2l) * (1 + pi336) + (ys3371*xo1r + ys3372*xo2r) * (1 + pi338) + (ys3371*xo1u + ys3372*xo2u) * (1 + pi312) + (ys3371*xo1d + ys3372*xo2d) * (1 + pi362),
pi338 == (ys3381*xo1l + ys3382*xo2l) * (1 + pi337) + (ys3381*xo1r + ys3382*xo2r) * (1 + pi339) + (ys3381*xo1u + ys3382*xo2u) * (1 + pi313) + (ys3381*xo1d + ys3382*xo2d) * (1 + pi363),
pi339 == (ys3391*xo1l + ys3392*xo2l) * (1 + pi338) + (ys3391*xo1r + ys3392*xo2r) * (1 + pi340) + (ys3391*xo1u + ys3392*xo2u) * (1 + pi314) + (ys3391*xo1d + ys3392*xo2d) * (1 + pi364),
pi340 == (ys3401*xo1l + ys3402*xo2l) * (1 + pi339) + (ys3401*xo1r + ys3402*xo2r) * (1 + pi341) + (ys3401*xo1u + ys3402*xo2u) * (1 + pi315) + (ys3401*xo1d + ys3402*xo2d) * (1 + pi365),
pi341 == (ys3411*xo1l + ys3412*xo2l) * (1 + pi340) + (ys3411*xo1r + ys3412*xo2r) * (1 + pi342) + (ys3411*xo1u + ys3412*xo2u) * (1 + pi316) + (ys3411*xo1d + ys3412*xo2d) * (1 + pi366),
pi342 == (ys3421*xo1l + ys3422*xo2l) * (1 + pi341) + (ys3421*xo1r + ys3422*xo2r) * (1 + pi343) + (ys3421*xo1u + ys3422*xo2u) * (1 + pi317) + (ys3421*xo1d + ys3422*xo2d) * (1 + pi367),
pi343 == (ys3431*xo1l + ys3432*xo2l) * (1 + pi342) + (ys3431*xo1r + ys3432*xo2r) * (1 + pi344) + (ys3431*xo1u + ys3432*xo2u) * (1 + pi318) + (ys3431*xo1d + ys3432*xo2d) * (1 + pi368),
pi344 == (ys3441*xo1l + ys3442*xo2l) * (1 + pi343) + (ys3441*xo1r + ys3442*xo2r) * (1 + pi345) + (ys3441*xo1u + ys3442*xo2u) * (1 + pi319) + (ys3441*xo1d + ys3442*xo2d) * (1 + pi369),
pi345 == (ys3451*xo1l + ys3452*xo2l) * (1 + pi344) + (ys3451*xo1r + ys3452*xo2r) * (1 + pi346) + (ys3451*xo1u + ys3452*xo2u) * (1 + pi320) + (ys3451*xo1d + ys3452*xo2d) * (1 + pi370),
pi346 == (ys3461*xo1l + ys3462*xo2l) * (1 + pi345) + (ys3461*xo1r + ys3462*xo2r) * (1 + pi347) + (ys3461*xo1u + ys3462*xo2u) * (1 + pi321) + (ys3461*xo1d + ys3462*xo2d) * (1 + pi371),
pi347 == (ys3471*xo1l + ys3472*xo2l) * (1 + pi346) + (ys3471*xo1r + ys3472*xo2r) * (1 + pi348) + (ys3471*xo1u + ys3472*xo2u) * (1 + pi322) + (ys3471*xo1d + ys3472*xo2d) * (1 + pi372),
pi348 == (ys3481*xo1l + ys3482*xo2l) * (1 + pi347) + (ys3481*xo1r + ys3482*xo2r) * (1 + pi349) + (ys3481*xo1u + ys3482*xo2u) * (1 + pi323) + (ys3481*xo1d + ys3482*xo2d) * (1 + pi373),
pi349 == (ys3491*xo1l + ys3492*xo2l) * (1 + pi348) + (ys3491*xo1r + ys3492*xo2r) * (1 + pi349) + (ys3491*xo1u + ys3492*xo2u) * (1 + pi324) + (ys3491*xo1d + ys3492*xo2d) * (1 + pi374),
pi350 == (ys3501*xo1l + ys3502*xo2l) * (1 + pi350) + (ys3501*xo1r + ys3502*xo2r) * (1 + pi351) + (ys3501*xo1u + ys3502*xo2u) * (1 + pi325) + (ys3501*xo1d + ys3502*xo2d) * (1 + pi375),
pi351 == (ys3511*xo1l + ys3512*xo2l) * (1 + pi350) + (ys3511*xo1r + ys3512*xo2r) * (1 + pi352) + (ys3511*xo1u + ys3512*xo2u) * (1 + pi326) + (ys3511*xo1d + ys3512*xo2d) * (1 + pi376),
pi352 == (ys3521*xo1l + ys3522*xo2l) * (1 + pi351) + (ys3521*xo1r + ys3522*xo2r) * (1 + pi353) + (ys3521*xo1u + ys3522*xo2u) * (1 + pi327) + (ys3521*xo1d + ys3522*xo2d) * (1 + pi377),
pi353 == (ys3531*xo1l + ys3532*xo2l) * (1 + pi352) + (ys3531*xo1r + ys3532*xo2r) * (1 + pi354) + (ys3531*xo1u + ys3532*xo2u) * (1 + pi328) + (ys3531*xo1d + ys3532*xo2d) * (1 + pi378),
pi354 == (ys3541*xo1l + ys3542*xo2l) * (1 + pi353) + (ys3541*xo1r + ys3542*xo2r) * (1 + pi355) + (ys3541*xo1u + ys3542*xo2u) * (1 + pi329) + (ys3541*xo1d + ys3542*xo2d) * (1 + pi379),
pi355 == (ys3551*xo1l + ys3552*xo2l) * (1 + pi354) + (ys3551*xo1r + ys3552*xo2r) * (1 + pi356) + (ys3551*xo1u + ys3552*xo2u) * (1 + pi330) + (ys3551*xo1d + ys3552*xo2d) * (1 + pi380),
pi356 == (ys3561*xo1l + ys3562*xo2l) * (1 + pi355) + (ys3561*xo1r + ys3562*xo2r) * (1 + pi357) + (ys3561*xo1u + ys3562*xo2u) * (1 + pi331) + (ys3561*xo1d + ys3562*xo2d) * (1 + pi381),
pi357 == (ys3571*xo1l + ys3572*xo2l) * (1 + pi356) + (ys3571*xo1r + ys3572*xo2r) * (1 + pi358) + (ys3571*xo1u + ys3572*xo2u) * (1 + pi332) + (ys3571*xo1d + ys3572*xo2d) * (1 + pi382),
pi358 == (ys3581*xo1l + ys3582*xo2l) * (1 + pi357) + (ys3581*xo1r + ys3582*xo2r) * (1 + pi359) + (ys3581*xo1u + ys3582*xo2u) * (1 + pi333) + (ys3581*xo1d + ys3582*xo2d) * (1 + pi383),
pi359 == (ys3591*xo1l + ys3592*xo2l) * (1 + pi358) + (ys3591*xo1r + ys3592*xo2r) * (1 + pi360) + (ys3591*xo1u + ys3592*xo2u) * (1 + pi334) + (ys3591*xo1d + ys3592*xo2d) * (1 + pi384),
pi360 == (ys3601*xo1l + ys3602*xo2l) * (1 + pi359) + (ys3601*xo1r + ys3602*xo2r) * (1 + pi361) + (ys3601*xo1u + ys3602*xo2u) * (1 + pi335) + (ys3601*xo1d + ys3602*xo2d) * (1 + pi385),
pi361 == (ys3611*xo1l + ys3612*xo2l) * (1 + pi360) + (ys3611*xo1r + ys3612*xo2r) * (1 + pi362) + (ys3611*xo1u + ys3612*xo2u) * (1 + pi336) + (ys3611*xo1d + ys3612*xo2d) * (1 + pi386),
pi362 == (ys3621*xo1l + ys3622*xo2l) * (1 + pi361) + (ys3621*xo1r + ys3622*xo2r) * (1 + pi363) + (ys3621*xo1u + ys3622*xo2u) * (1 + pi337) + (ys3621*xo1d + ys3622*xo2d) * (1 + pi387),
pi363 == (ys3631*xo1l + ys3632*xo2l) * (1 + pi362) + (ys3631*xo1r + ys3632*xo2r) * (1 + pi364) + (ys3631*xo1u + ys3632*xo2u) * (1 + pi338) + (ys3631*xo1d + ys3632*xo2d) * (1 + pi388),
pi364 == (ys3641*xo1l + ys3642*xo2l) * (1 + pi363) + (ys3641*xo1r + ys3642*xo2r) * (1 + pi365) + (ys3641*xo1u + ys3642*xo2u) * (1 + pi339) + (ys3641*xo1d + ys3642*xo2d) * (1 + pi389),
pi365 == (ys3651*xo1l + ys3652*xo2l) * (1 + pi364) + (ys3651*xo1r + ys3652*xo2r) * (1 + pi366) + (ys3651*xo1u + ys3652*xo2u) * (1 + pi340) + (ys3651*xo1d + ys3652*xo2d) * (1 + pi390),
pi366 == (ys3661*xo1l + ys3662*xo2l) * (1 + pi365) + (ys3661*xo1r + ys3662*xo2r) * (1 + pi367) + (ys3661*xo1u + ys3662*xo2u) * (1 + pi341) + (ys3661*xo1d + ys3662*xo2d) * (1 + pi391),
pi367 == (ys3671*xo1l + ys3672*xo2l) * (1 + pi366) + (ys3671*xo1r + ys3672*xo2r) * (1 + pi368) + (ys3671*xo1u + ys3672*xo2u) * (1 + pi342) + (ys3671*xo1d + ys3672*xo2d) * (1 + pi392),
pi368 == (ys3681*xo1l + ys3682*xo2l) * (1 + pi367) + (ys3681*xo1r + ys3682*xo2r) * (1 + pi369) + (ys3681*xo1u + ys3682*xo2u) * (1 + pi343) + (ys3681*xo1d + ys3682*xo2d) * (1 + pi393),
pi369 == (ys3691*xo1l + ys3692*xo2l) * (1 + pi368) + (ys3691*xo1r + ys3692*xo2r) * (1 + pi370) + (ys3691*xo1u + ys3692*xo2u) * (1 + pi344) + (ys3691*xo1d + ys3692*xo2d) * (1 + pi394),
pi370 == (ys3701*xo1l + ys3702*xo2l) * (1 + pi369) + (ys3701*xo1r + ys3702*xo2r) * (1 + pi371) + (ys3701*xo1u + ys3702*xo2u) * (1 + pi345) + (ys3701*xo1d + ys3702*xo2d) * (1 + pi395),
pi371 == (ys3711*xo1l + ys3712*xo2l) * (1 + pi370) + (ys3711*xo1r + ys3712*xo2r) * (1 + pi372) + (ys3711*xo1u + ys3712*xo2u) * (1 + pi346) + (ys3711*xo1d + ys3712*xo2d) * (1 + pi396),
pi372 == (ys3721*xo1l + ys3722*xo2l) * (1 + pi371) + (ys3721*xo1r + ys3722*xo2r) * (1 + pi373) + (ys3721*xo1u + ys3722*xo2u) * (1 + pi347) + (ys3721*xo1d + ys3722*xo2d) * (1 + pi397),
pi373 == (ys3731*xo1l + ys3732*xo2l) * (1 + pi372) + (ys3731*xo1r + ys3732*xo2r) * (1 + pi374) + (ys3731*xo1u + ys3732*xo2u) * (1 + pi348) + (ys3731*xo1d + ys3732*xo2d) * (1 + pi398),
pi374 == (ys3741*xo1l + ys3742*xo2l) * (1 + pi373) + (ys3741*xo1r + ys3742*xo2r) * (1 + pi374) + (ys3741*xo1u + ys3742*xo2u) * (1 + pi349) + (ys3741*xo1d + ys3742*xo2d) * (1 + pi399),
pi375 == (ys3751*xo1l + ys3752*xo2l) * (1 + pi375) + (ys3751*xo1r + ys3752*xo2r) * (1 + pi376) + (ys3751*xo1u + ys3752*xo2u) * (1 + pi350) + (ys3751*xo1d + ys3752*xo2d) * (1 + pi400),
pi376 == (ys3761*xo1l + ys3762*xo2l) * (1 + pi375) + (ys3761*xo1r + ys3762*xo2r) * (1 + pi377) + (ys3761*xo1u + ys3762*xo2u) * (1 + pi351) + (ys3761*xo1d + ys3762*xo2d) * (1 + pi401),
pi377 == (ys3771*xo1l + ys3772*xo2l) * (1 + pi376) + (ys3771*xo1r + ys3772*xo2r) * (1 + pi378) + (ys3771*xo1u + ys3772*xo2u) * (1 + pi352) + (ys3771*xo1d + ys3772*xo2d) * (1 + pi402),
pi378 == (ys3781*xo1l + ys3782*xo2l) * (1 + pi377) + (ys3781*xo1r + ys3782*xo2r) * (1 + pi379) + (ys3781*xo1u + ys3782*xo2u) * (1 + pi353) + (ys3781*xo1d + ys3782*xo2d) * (1 + pi403),
pi379 == (ys3791*xo1l + ys3792*xo2l) * (1 + pi378) + (ys3791*xo1r + ys3792*xo2r) * (1 + pi380) + (ys3791*xo1u + ys3792*xo2u) * (1 + pi354) + (ys3791*xo1d + ys3792*xo2d) * (1 + pi404),
pi380 == (ys3801*xo1l + ys3802*xo2l) * (1 + pi379) + (ys3801*xo1r + ys3802*xo2r) * (1 + pi381) + (ys3801*xo1u + ys3802*xo2u) * (1 + pi355) + (ys3801*xo1d + ys3802*xo2d) * (1 + pi405),
pi381 == (ys3811*xo1l + ys3812*xo2l) * (1 + pi380) + (ys3811*xo1r + ys3812*xo2r) * (1 + pi382) + (ys3811*xo1u + ys3812*xo2u) * (1 + pi356) + (ys3811*xo1d + ys3812*xo2d) * (1 + pi406),
pi382 == (ys3821*xo1l + ys3822*xo2l) * (1 + pi381) + (ys3821*xo1r + ys3822*xo2r) * (1 + pi383) + (ys3821*xo1u + ys3822*xo2u) * (1 + pi357) + (ys3821*xo1d + ys3822*xo2d) * (1 + pi407),
pi383 == (ys3831*xo1l + ys3832*xo2l) * (1 + pi382) + (ys3831*xo1r + ys3832*xo2r) * (1 + pi384) + (ys3831*xo1u + ys3832*xo2u) * (1 + pi358) + (ys3831*xo1d + ys3832*xo2d) * (1 + pi408),
pi384 == (ys3841*xo1l + ys3842*xo2l) * (1 + pi383) + (ys3841*xo1r + ys3842*xo2r) * (1 + pi385) + (ys3841*xo1u + ys3842*xo2u) * (1 + pi359) + (ys3841*xo1d + ys3842*xo2d) * (1 + pi409),
pi385 == (ys3851*xo1l + ys3852*xo2l) * (1 + pi384) + (ys3851*xo1r + ys3852*xo2r) * (1 + pi386) + (ys3851*xo1u + ys3852*xo2u) * (1 + pi360) + (ys3851*xo1d + ys3852*xo2d) * (1 + pi410),
pi386 == (ys3861*xo1l + ys3862*xo2l) * (1 + pi385) + (ys3861*xo1r + ys3862*xo2r) * (1 + pi387) + (ys3861*xo1u + ys3862*xo2u) * (1 + pi361) + (ys3861*xo1d + ys3862*xo2d) * (1 + pi411),
pi387 == (ys3871*xo1l + ys3872*xo2l) * (1 + pi386) + (ys3871*xo1r + ys3872*xo2r) * (1 + pi388) + (ys3871*xo1u + ys3872*xo2u) * (1 + pi362) + (ys3871*xo1d + ys3872*xo2d) * (1 + pi412),
pi388 == (ys3881*xo1l + ys3882*xo2l) * (1 + pi387) + (ys3881*xo1r + ys3882*xo2r) * (1 + pi389) + (ys3881*xo1u + ys3882*xo2u) * (1 + pi363) + (ys3881*xo1d + ys3882*xo2d) * (1 + pi413),
pi389 == (ys3891*xo1l + ys3892*xo2l) * (1 + pi388) + (ys3891*xo1r + ys3892*xo2r) * (1 + pi390) + (ys3891*xo1u + ys3892*xo2u) * (1 + pi364) + (ys3891*xo1d + ys3892*xo2d) * (1 + pi414),
pi390 == (ys3901*xo1l + ys3902*xo2l) * (1 + pi389) + (ys3901*xo1r + ys3902*xo2r) * (1 + pi391) + (ys3901*xo1u + ys3902*xo2u) * (1 + pi365) + (ys3901*xo1d + ys3902*xo2d) * (1 + pi415),
pi391 == (ys3911*xo1l + ys3912*xo2l) * (1 + pi390) + (ys3911*xo1r + ys3912*xo2r) * (1 + pi392) + (ys3911*xo1u + ys3912*xo2u) * (1 + pi366) + (ys3911*xo1d + ys3912*xo2d) * (1 + pi416),
pi392 == (ys3921*xo1l + ys3922*xo2l) * (1 + pi391) + (ys3921*xo1r + ys3922*xo2r) * (1 + pi393) + (ys3921*xo1u + ys3922*xo2u) * (1 + pi367) + (ys3921*xo1d + ys3922*xo2d) * (1 + pi417),
pi393 == (ys3931*xo1l + ys3932*xo2l) * (1 + pi392) + (ys3931*xo1r + ys3932*xo2r) * (1 + pi394) + (ys3931*xo1u + ys3932*xo2u) * (1 + pi368) + (ys3931*xo1d + ys3932*xo2d) * (1 + pi418),
pi394 == (ys3941*xo1l + ys3942*xo2l) * (1 + pi393) + (ys3941*xo1r + ys3942*xo2r) * (1 + pi395) + (ys3941*xo1u + ys3942*xo2u) * (1 + pi369) + (ys3941*xo1d + ys3942*xo2d) * (1 + pi419),
pi395 == (ys3951*xo1l + ys3952*xo2l) * (1 + pi394) + (ys3951*xo1r + ys3952*xo2r) * (1 + pi396) + (ys3951*xo1u + ys3952*xo2u) * (1 + pi370) + (ys3951*xo1d + ys3952*xo2d) * (1 + pi420),
pi396 == (ys3961*xo1l + ys3962*xo2l) * (1 + pi395) + (ys3961*xo1r + ys3962*xo2r) * (1 + pi397) + (ys3961*xo1u + ys3962*xo2u) * (1 + pi371) + (ys3961*xo1d + ys3962*xo2d) * (1 + pi421),
pi397 == (ys3971*xo1l + ys3972*xo2l) * (1 + pi396) + (ys3971*xo1r + ys3972*xo2r) * (1 + pi398) + (ys3971*xo1u + ys3972*xo2u) * (1 + pi372) + (ys3971*xo1d + ys3972*xo2d) * (1 + pi422),
pi398 == (ys3981*xo1l + ys3982*xo2l) * (1 + pi397) + (ys3981*xo1r + ys3982*xo2r) * (1 + pi399) + (ys3981*xo1u + ys3982*xo2u) * (1 + pi373) + (ys3981*xo1d + ys3982*xo2d) * (1 + pi423),
pi399 == (ys3991*xo1l + ys3992*xo2l) * (1 + pi398) + (ys3991*xo1r + ys3992*xo2r) * (1 + pi399) + (ys3991*xo1u + ys3992*xo2u) * (1 + pi374) + (ys3991*xo1d + ys3992*xo2d) * (1 + pi424),
pi400 == (ys4001*xo1l + ys4002*xo2l) * (1 + pi400) + (ys4001*xo1r + ys4002*xo2r) * (1 + pi401) + (ys4001*xo1u + ys4002*xo2u) * (1 + pi375) + (ys4001*xo1d + ys4002*xo2d) * (1 + pi425),
pi401 == (ys4011*xo1l + ys4012*xo2l) * (1 + pi400) + (ys4011*xo1r + ys4012*xo2r) * (1 + pi402) + (ys4011*xo1u + ys4012*xo2u) * (1 + pi376) + (ys4011*xo1d + ys4012*xo2d) * (1 + pi426),
pi402 == (ys4021*xo1l + ys4022*xo2l) * (1 + pi401) + (ys4021*xo1r + ys4022*xo2r) * (1 + pi403) + (ys4021*xo1u + ys4022*xo2u) * (1 + pi377) + (ys4021*xo1d + ys4022*xo2d) * (1 + pi427),
pi403 == (ys4031*xo1l + ys4032*xo2l) * (1 + pi402) + (ys4031*xo1r + ys4032*xo2r) * (1 + pi404) + (ys4031*xo1u + ys4032*xo2u) * (1 + pi378) + (ys4031*xo1d + ys4032*xo2d) * (1 + pi428),
pi404 == (ys4041*xo1l + ys4042*xo2l) * (1 + pi403) + (ys4041*xo1r + ys4042*xo2r) * (1 + pi405) + (ys4041*xo1u + ys4042*xo2u) * (1 + pi379) + (ys4041*xo1d + ys4042*xo2d) * (1 + pi429),
pi405 == (ys4051*xo1l + ys4052*xo2l) * (1 + pi404) + (ys4051*xo1r + ys4052*xo2r) * (1 + pi406) + (ys4051*xo1u + ys4052*xo2u) * (1 + pi380) + (ys4051*xo1d + ys4052*xo2d) * (1 + pi430),
pi406 == (ys4061*xo1l + ys4062*xo2l) * (1 + pi405) + (ys4061*xo1r + ys4062*xo2r) * (1 + pi407) + (ys4061*xo1u + ys4062*xo2u) * (1 + pi381) + (ys4061*xo1d + ys4062*xo2d) * (1 + pi431),
pi407 == (ys4071*xo1l + ys4072*xo2l) * (1 + pi406) + (ys4071*xo1r + ys4072*xo2r) * (1 + pi408) + (ys4071*xo1u + ys4072*xo2u) * (1 + pi382) + (ys4071*xo1d + ys4072*xo2d) * (1 + pi432),
pi408 == (ys4081*xo1l + ys4082*xo2l) * (1 + pi407) + (ys4081*xo1r + ys4082*xo2r) * (1 + pi409) + (ys4081*xo1u + ys4082*xo2u) * (1 + pi383) + (ys4081*xo1d + ys4082*xo2d) * (1 + pi433),
pi409 == (ys4091*xo1l + ys4092*xo2l) * (1 + pi408) + (ys4091*xo1r + ys4092*xo2r) * (1 + pi410) + (ys4091*xo1u + ys4092*xo2u) * (1 + pi384) + (ys4091*xo1d + ys4092*xo2d) * (1 + pi434),
pi410 == (ys4101*xo1l + ys4102*xo2l) * (1 + pi409) + (ys4101*xo1r + ys4102*xo2r) * (1 + pi411) + (ys4101*xo1u + ys4102*xo2u) * (1 + pi385) + (ys4101*xo1d + ys4102*xo2d) * (1 + pi435),
pi411 == (ys4111*xo1l + ys4112*xo2l) * (1 + pi410) + (ys4111*xo1r + ys4112*xo2r) * (1 + pi412) + (ys4111*xo1u + ys4112*xo2u) * (1 + pi386) + (ys4111*xo1d + ys4112*xo2d) * (1 + pi436),
pi412 == (ys4121*xo1l + ys4122*xo2l) * (1 + pi411) + (ys4121*xo1r + ys4122*xo2r) * (1 + pi413) + (ys4121*xo1u + ys4122*xo2u) * (1 + pi387) + (ys4121*xo1d + ys4122*xo2d) * (1 + pi437),
pi413 == (ys4131*xo1l + ys4132*xo2l) * (1 + pi412) + (ys4131*xo1r + ys4132*xo2r) * (1 + pi414) + (ys4131*xo1u + ys4132*xo2u) * (1 + pi388) + (ys4131*xo1d + ys4132*xo2d) * (1 + pi438),
pi414 == (ys4141*xo1l + ys4142*xo2l) * (1 + pi413) + (ys4141*xo1r + ys4142*xo2r) * (1 + pi415) + (ys4141*xo1u + ys4142*xo2u) * (1 + pi389) + (ys4141*xo1d + ys4142*xo2d) * (1 + pi439),
pi415 == (ys4151*xo1l + ys4152*xo2l) * (1 + pi414) + (ys4151*xo1r + ys4152*xo2r) * (1 + pi416) + (ys4151*xo1u + ys4152*xo2u) * (1 + pi390) + (ys4151*xo1d + ys4152*xo2d) * (1 + pi440),
pi416 == (ys4161*xo1l + ys4162*xo2l) * (1 + pi415) + (ys4161*xo1r + ys4162*xo2r) * (1 + pi417) + (ys4161*xo1u + ys4162*xo2u) * (1 + pi391) + (ys4161*xo1d + ys4162*xo2d) * (1 + pi441),
pi417 == (ys4171*xo1l + ys4172*xo2l) * (1 + pi416) + (ys4171*xo1r + ys4172*xo2r) * (1 + pi418) + (ys4171*xo1u + ys4172*xo2u) * (1 + pi392) + (ys4171*xo1d + ys4172*xo2d) * (1 + pi442),
pi418 == (ys4181*xo1l + ys4182*xo2l) * (1 + pi417) + (ys4181*xo1r + ys4182*xo2r) * (1 + pi419) + (ys4181*xo1u + ys4182*xo2u) * (1 + pi393) + (ys4181*xo1d + ys4182*xo2d) * (1 + pi443),
pi419 == (ys4191*xo1l + ys4192*xo2l) * (1 + pi418) + (ys4191*xo1r + ys4192*xo2r) * (1 + pi420) + (ys4191*xo1u + ys4192*xo2u) * (1 + pi394) + (ys4191*xo1d + ys4192*xo2d) * (1 + pi444),
pi420 == (ys4201*xo1l + ys4202*xo2l) * (1 + pi419) + (ys4201*xo1r + ys4202*xo2r) * (1 + pi421) + (ys4201*xo1u + ys4202*xo2u) * (1 + pi395) + (ys4201*xo1d + ys4202*xo2d) * (1 + pi445),
pi421 == (ys4211*xo1l + ys4212*xo2l) * (1 + pi420) + (ys4211*xo1r + ys4212*xo2r) * (1 + pi422) + (ys4211*xo1u + ys4212*xo2u) * (1 + pi396) + (ys4211*xo1d + ys4212*xo2d) * (1 + pi446),
pi422 == (ys4221*xo1l + ys4222*xo2l) * (1 + pi421) + (ys4221*xo1r + ys4222*xo2r) * (1 + pi423) + (ys4221*xo1u + ys4222*xo2u) * (1 + pi397) + (ys4221*xo1d + ys4222*xo2d) * (1 + pi447),
pi423 == (ys4231*xo1l + ys4232*xo2l) * (1 + pi422) + (ys4231*xo1r + ys4232*xo2r) * (1 + pi424) + (ys4231*xo1u + ys4232*xo2u) * (1 + pi398) + (ys4231*xo1d + ys4232*xo2d) * (1 + pi448),
pi424 == (ys4241*xo1l + ys4242*xo2l) * (1 + pi423) + (ys4241*xo1r + ys4242*xo2r) * (1 + pi424) + (ys4241*xo1u + ys4242*xo2u) * (1 + pi399) + (ys4241*xo1d + ys4242*xo2d) * (1 + pi449),
pi425 == (ys4251*xo1l + ys4252*xo2l) * (1 + pi425) + (ys4251*xo1r + ys4252*xo2r) * (1 + pi426) + (ys4251*xo1u + ys4252*xo2u) * (1 + pi400) + (ys4251*xo1d + ys4252*xo2d) * (1 + pi450),
pi426 == (ys4261*xo1l + ys4262*xo2l) * (1 + pi425) + (ys4261*xo1r + ys4262*xo2r) * (1 + pi427) + (ys4261*xo1u + ys4262*xo2u) * (1 + pi401) + (ys4261*xo1d + ys4262*xo2d) * (1 + pi451),
pi427 == (ys4271*xo1l + ys4272*xo2l) * (1 + pi426) + (ys4271*xo1r + ys4272*xo2r) * (1 + pi428) + (ys4271*xo1u + ys4272*xo2u) * (1 + pi402) + (ys4271*xo1d + ys4272*xo2d) * (1 + pi452),
pi428 == (ys4281*xo1l + ys4282*xo2l) * (1 + pi427) + (ys4281*xo1r + ys4282*xo2r) * (1 + pi429) + (ys4281*xo1u + ys4282*xo2u) * (1 + pi403) + (ys4281*xo1d + ys4282*xo2d) * (1 + pi453),
pi429 == (ys4291*xo1l + ys4292*xo2l) * (1 + pi428) + (ys4291*xo1r + ys4292*xo2r) * (1 + pi430) + (ys4291*xo1u + ys4292*xo2u) * (1 + pi404) + (ys4291*xo1d + ys4292*xo2d) * (1 + pi454),
pi430 == (ys4301*xo1l + ys4302*xo2l) * (1 + pi429) + (ys4301*xo1r + ys4302*xo2r) * (1 + pi431) + (ys4301*xo1u + ys4302*xo2u) * (1 + pi405) + (ys4301*xo1d + ys4302*xo2d) * (1 + pi455),
pi431 == (ys4311*xo1l + ys4312*xo2l) * (1 + pi430) + (ys4311*xo1r + ys4312*xo2r) * (1 + pi432) + (ys4311*xo1u + ys4312*xo2u) * (1 + pi406) + (ys4311*xo1d + ys4312*xo2d) * (1 + pi456),
pi432 == (ys4321*xo1l + ys4322*xo2l) * (1 + pi431) + (ys4321*xo1r + ys4322*xo2r) * (1 + pi433) + (ys4321*xo1u + ys4322*xo2u) * (1 + pi407) + (ys4321*xo1d + ys4322*xo2d) * (1 + pi457),
pi433 == (ys4331*xo1l + ys4332*xo2l) * (1 + pi432) + (ys4331*xo1r + ys4332*xo2r) * (1 + pi434) + (ys4331*xo1u + ys4332*xo2u) * (1 + pi408) + (ys4331*xo1d + ys4332*xo2d) * (1 + pi458),
pi434 == (ys4341*xo1l + ys4342*xo2l) * (1 + pi433) + (ys4341*xo1r + ys4342*xo2r) * (1 + pi435) + (ys4341*xo1u + ys4342*xo2u) * (1 + pi409) + (ys4341*xo1d + ys4342*xo2d) * (1 + pi459),
pi435 == (ys4351*xo1l + ys4352*xo2l) * (1 + pi434) + (ys4351*xo1r + ys4352*xo2r) * (1 + pi436) + (ys4351*xo1u + ys4352*xo2u) * (1 + pi410) + (ys4351*xo1d + ys4352*xo2d) * (1 + pi460),
pi436 == (ys4361*xo1l + ys4362*xo2l) * (1 + pi435) + (ys4361*xo1r + ys4362*xo2r) * (1 + pi437) + (ys4361*xo1u + ys4362*xo2u) * (1 + pi411) + (ys4361*xo1d + ys4362*xo2d) * (1 + pi461),
pi437 == (ys4371*xo1l + ys4372*xo2l) * (1 + pi436) + (ys4371*xo1r + ys4372*xo2r) * (1 + pi438) + (ys4371*xo1u + ys4372*xo2u) * (1 + pi412) + (ys4371*xo1d + ys4372*xo2d) * (1 + pi462),
pi438 == (ys4381*xo1l + ys4382*xo2l) * (1 + pi437) + (ys4381*xo1r + ys4382*xo2r) * (1 + pi439) + (ys4381*xo1u + ys4382*xo2u) * (1 + pi413) + (ys4381*xo1d + ys4382*xo2d) * (1 + pi463),
pi439 == (ys4391*xo1l + ys4392*xo2l) * (1 + pi438) + (ys4391*xo1r + ys4392*xo2r) * (1 + pi440) + (ys4391*xo1u + ys4392*xo2u) * (1 + pi414) + (ys4391*xo1d + ys4392*xo2d) * (1 + pi464),
pi440 == (ys4401*xo1l + ys4402*xo2l) * (1 + pi439) + (ys4401*xo1r + ys4402*xo2r) * (1 + pi441) + (ys4401*xo1u + ys4402*xo2u) * (1 + pi415) + (ys4401*xo1d + ys4402*xo2d) * (1 + pi465),
pi441 == (ys4411*xo1l + ys4412*xo2l) * (1 + pi440) + (ys4411*xo1r + ys4412*xo2r) * (1 + pi442) + (ys4411*xo1u + ys4412*xo2u) * (1 + pi416) + (ys4411*xo1d + ys4412*xo2d) * (1 + pi466),
pi442 == (ys4421*xo1l + ys4422*xo2l) * (1 + pi441) + (ys4421*xo1r + ys4422*xo2r) * (1 + pi443) + (ys4421*xo1u + ys4422*xo2u) * (1 + pi417) + (ys4421*xo1d + ys4422*xo2d) * (1 + pi467),
pi443 == (ys4431*xo1l + ys4432*xo2l) * (1 + pi442) + (ys4431*xo1r + ys4432*xo2r) * (1 + pi444) + (ys4431*xo1u + ys4432*xo2u) * (1 + pi418) + (ys4431*xo1d + ys4432*xo2d) * (1 + pi468),
pi444 == (ys4441*xo1l + ys4442*xo2l) * (1 + pi443) + (ys4441*xo1r + ys4442*xo2r) * (1 + pi445) + (ys4441*xo1u + ys4442*xo2u) * (1 + pi419) + (ys4441*xo1d + ys4442*xo2d) * (1 + pi469),
pi445 == (ys4451*xo1l + ys4452*xo2l) * (1 + pi444) + (ys4451*xo1r + ys4452*xo2r) * (1 + pi446) + (ys4451*xo1u + ys4452*xo2u) * (1 + pi420) + (ys4451*xo1d + ys4452*xo2d) * (1 + pi470),
pi446 == (ys4461*xo1l + ys4462*xo2l) * (1 + pi445) + (ys4461*xo1r + ys4462*xo2r) * (1 + pi447) + (ys4461*xo1u + ys4462*xo2u) * (1 + pi421) + (ys4461*xo1d + ys4462*xo2d) * (1 + pi471),
pi447 == (ys4471*xo1l + ys4472*xo2l) * (1 + pi446) + (ys4471*xo1r + ys4472*xo2r) * (1 + pi448) + (ys4471*xo1u + ys4472*xo2u) * (1 + pi422) + (ys4471*xo1d + ys4472*xo2d) * (1 + pi472),
pi448 == (ys4481*xo1l + ys4482*xo2l) * (1 + pi447) + (ys4481*xo1r + ys4482*xo2r) * (1 + pi449) + (ys4481*xo1u + ys4482*xo2u) * (1 + pi423) + (ys4481*xo1d + ys4482*xo2d) * (1 + pi473),
pi449 == (ys4491*xo1l + ys4492*xo2l) * (1 + pi448) + (ys4491*xo1r + ys4492*xo2r) * (1 + pi449) + (ys4491*xo1u + ys4492*xo2u) * (1 + pi424) + (ys4491*xo1d + ys4492*xo2d) * (1 + pi474),
pi450 == (ys4501*xo1l + ys4502*xo2l) * (1 + pi450) + (ys4501*xo1r + ys4502*xo2r) * (1 + pi451) + (ys4501*xo1u + ys4502*xo2u) * (1 + pi425) + (ys4501*xo1d + ys4502*xo2d) * (1 + pi475),
pi451 == (ys4511*xo1l + ys4512*xo2l) * (1 + pi450) + (ys4511*xo1r + ys4512*xo2r) * (1 + pi452) + (ys4511*xo1u + ys4512*xo2u) * (1 + pi426) + (ys4511*xo1d + ys4512*xo2d) * (1 + pi476),
pi452 == (ys4521*xo1l + ys4522*xo2l) * (1 + pi451) + (ys4521*xo1r + ys4522*xo2r) * (1 + pi453) + (ys4521*xo1u + ys4522*xo2u) * (1 + pi427) + (ys4521*xo1d + ys4522*xo2d) * (1 + pi477),
pi453 == (ys4531*xo1l + ys4532*xo2l) * (1 + pi452) + (ys4531*xo1r + ys4532*xo2r) * (1 + pi454) + (ys4531*xo1u + ys4532*xo2u) * (1 + pi428) + (ys4531*xo1d + ys4532*xo2d) * (1 + pi478),
pi454 == (ys4541*xo1l + ys4542*xo2l) * (1 + pi453) + (ys4541*xo1r + ys4542*xo2r) * (1 + pi455) + (ys4541*xo1u + ys4542*xo2u) * (1 + pi429) + (ys4541*xo1d + ys4542*xo2d) * (1 + pi479),
pi455 == (ys4551*xo1l + ys4552*xo2l) * (1 + pi454) + (ys4551*xo1r + ys4552*xo2r) * (1 + pi456) + (ys4551*xo1u + ys4552*xo2u) * (1 + pi430) + (ys4551*xo1d + ys4552*xo2d) * (1 + pi480),
pi456 == (ys4561*xo1l + ys4562*xo2l) * (1 + pi455) + (ys4561*xo1r + ys4562*xo2r) * (1 + pi457) + (ys4561*xo1u + ys4562*xo2u) * (1 + pi431) + (ys4561*xo1d + ys4562*xo2d) * (1 + pi481),
pi457 == (ys4571*xo1l + ys4572*xo2l) * (1 + pi456) + (ys4571*xo1r + ys4572*xo2r) * (1 + pi458) + (ys4571*xo1u + ys4572*xo2u) * (1 + pi432) + (ys4571*xo1d + ys4572*xo2d) * (1 + pi482),
pi458 == (ys4581*xo1l + ys4582*xo2l) * (1 + pi457) + (ys4581*xo1r + ys4582*xo2r) * (1 + pi459) + (ys4581*xo1u + ys4582*xo2u) * (1 + pi433) + (ys4581*xo1d + ys4582*xo2d) * (1 + pi483),
pi459 == (ys4591*xo1l + ys4592*xo2l) * (1 + pi458) + (ys4591*xo1r + ys4592*xo2r) * (1 + pi460) + (ys4591*xo1u + ys4592*xo2u) * (1 + pi434) + (ys4591*xo1d + ys4592*xo2d) * (1 + pi484),
pi460 == (ys4601*xo1l + ys4602*xo2l) * (1 + pi459) + (ys4601*xo1r + ys4602*xo2r) * (1 + pi461) + (ys4601*xo1u + ys4602*xo2u) * (1 + pi435) + (ys4601*xo1d + ys4602*xo2d) * (1 + pi485),
pi461 == (ys4611*xo1l + ys4612*xo2l) * (1 + pi460) + (ys4611*xo1r + ys4612*xo2r) * (1 + pi462) + (ys4611*xo1u + ys4612*xo2u) * (1 + pi436) + (ys4611*xo1d + ys4612*xo2d) * (1 + pi486),
pi462 == (ys4621*xo1l + ys4622*xo2l) * (1 + pi461) + (ys4621*xo1r + ys4622*xo2r) * (1 + pi463) + (ys4621*xo1u + ys4622*xo2u) * (1 + pi437) + (ys4621*xo1d + ys4622*xo2d) * (1 + pi487),
pi463 == (ys4631*xo1l + ys4632*xo2l) * (1 + pi462) + (ys4631*xo1r + ys4632*xo2r) * (1 + pi464) + (ys4631*xo1u + ys4632*xo2u) * (1 + pi438) + (ys4631*xo1d + ys4632*xo2d) * (1 + pi488),
pi464 == (ys4641*xo1l + ys4642*xo2l) * (1 + pi463) + (ys4641*xo1r + ys4642*xo2r) * (1 + pi465) + (ys4641*xo1u + ys4642*xo2u) * (1 + pi439) + (ys4641*xo1d + ys4642*xo2d) * (1 + pi489),
pi465 == (ys4651*xo1l + ys4652*xo2l) * (1 + pi464) + (ys4651*xo1r + ys4652*xo2r) * (1 + pi466) + (ys4651*xo1u + ys4652*xo2u) * (1 + pi440) + (ys4651*xo1d + ys4652*xo2d) * (1 + pi490),
pi466 == (ys4661*xo1l + ys4662*xo2l) * (1 + pi465) + (ys4661*xo1r + ys4662*xo2r) * (1 + pi467) + (ys4661*xo1u + ys4662*xo2u) * (1 + pi441) + (ys4661*xo1d + ys4662*xo2d) * (1 + pi491),
pi467 == (ys4671*xo1l + ys4672*xo2l) * (1 + pi466) + (ys4671*xo1r + ys4672*xo2r) * (1 + pi468) + (ys4671*xo1u + ys4672*xo2u) * (1 + pi442) + (ys4671*xo1d + ys4672*xo2d) * (1 + pi492),
pi468 == (ys4681*xo1l + ys4682*xo2l) * (1 + pi467) + (ys4681*xo1r + ys4682*xo2r) * (1 + pi469) + (ys4681*xo1u + ys4682*xo2u) * (1 + pi443) + (ys4681*xo1d + ys4682*xo2d) * (1 + pi493),
pi469 == (ys4691*xo1l + ys4692*xo2l) * (1 + pi468) + (ys4691*xo1r + ys4692*xo2r) * (1 + pi470) + (ys4691*xo1u + ys4692*xo2u) * (1 + pi444) + (ys4691*xo1d + ys4692*xo2d) * (1 + pi494),
pi470 == (ys4701*xo1l + ys4702*xo2l) * (1 + pi469) + (ys4701*xo1r + ys4702*xo2r) * (1 + pi471) + (ys4701*xo1u + ys4702*xo2u) * (1 + pi445) + (ys4701*xo1d + ys4702*xo2d) * (1 + pi495),
pi471 == (ys4711*xo1l + ys4712*xo2l) * (1 + pi470) + (ys4711*xo1r + ys4712*xo2r) * (1 + pi472) + (ys4711*xo1u + ys4712*xo2u) * (1 + pi446) + (ys4711*xo1d + ys4712*xo2d) * (1 + pi496),
pi472 == (ys4721*xo1l + ys4722*xo2l) * (1 + pi471) + (ys4721*xo1r + ys4722*xo2r) * (1 + pi473) + (ys4721*xo1u + ys4722*xo2u) * (1 + pi447) + (ys4721*xo1d + ys4722*xo2d) * (1 + pi497),
pi473 == (ys4731*xo1l + ys4732*xo2l) * (1 + pi472) + (ys4731*xo1r + ys4732*xo2r) * (1 + pi474) + (ys4731*xo1u + ys4732*xo2u) * (1 + pi448) + (ys4731*xo1d + ys4732*xo2d) * (1 + pi498),
pi474 == (ys4741*xo1l + ys4742*xo2l) * (1 + pi473) + (ys4741*xo1r + ys4742*xo2r) * (1 + pi474) + (ys4741*xo1u + ys4742*xo2u) * (1 + pi449) + (ys4741*xo1d + ys4742*xo2d) * (1 + pi499),
pi475 == (ys4751*xo1l + ys4752*xo2l) * (1 + pi475) + (ys4751*xo1r + ys4752*xo2r) * (1 + pi476) + (ys4751*xo1u + ys4752*xo2u) * (1 + pi450) + (ys4751*xo1d + ys4752*xo2d) * (1 + pi500),
pi476 == (ys4761*xo1l + ys4762*xo2l) * (1 + pi475) + (ys4761*xo1r + ys4762*xo2r) * (1 + pi477) + (ys4761*xo1u + ys4762*xo2u) * (1 + pi451) + (ys4761*xo1d + ys4762*xo2d) * (1 + pi501),
pi477 == (ys4771*xo1l + ys4772*xo2l) * (1 + pi476) + (ys4771*xo1r + ys4772*xo2r) * (1 + pi478) + (ys4771*xo1u + ys4772*xo2u) * (1 + pi452) + (ys4771*xo1d + ys4772*xo2d) * (1 + pi502),
pi478 == (ys4781*xo1l + ys4782*xo2l) * (1 + pi477) + (ys4781*xo1r + ys4782*xo2r) * (1 + pi479) + (ys4781*xo1u + ys4782*xo2u) * (1 + pi453) + (ys4781*xo1d + ys4782*xo2d) * (1 + pi503),
pi479 == (ys4791*xo1l + ys4792*xo2l) * (1 + pi478) + (ys4791*xo1r + ys4792*xo2r) * (1 + pi480) + (ys4791*xo1u + ys4792*xo2u) * (1 + pi454) + (ys4791*xo1d + ys4792*xo2d) * (1 + pi504),
pi480 == (ys4801*xo1l + ys4802*xo2l) * (1 + pi479) + (ys4801*xo1r + ys4802*xo2r) * (1 + pi481) + (ys4801*xo1u + ys4802*xo2u) * (1 + pi455) + (ys4801*xo1d + ys4802*xo2d) * (1 + pi505),
pi481 == (ys4811*xo1l + ys4812*xo2l) * (1 + pi480) + (ys4811*xo1r + ys4812*xo2r) * (1 + pi482) + (ys4811*xo1u + ys4812*xo2u) * (1 + pi456) + (ys4811*xo1d + ys4812*xo2d) * (1 + pi506),
pi482 == (ys4821*xo1l + ys4822*xo2l) * (1 + pi481) + (ys4821*xo1r + ys4822*xo2r) * (1 + pi483) + (ys4821*xo1u + ys4822*xo2u) * (1 + pi457) + (ys4821*xo1d + ys4822*xo2d) * (1 + pi507),
pi483 == (ys4831*xo1l + ys4832*xo2l) * (1 + pi482) + (ys4831*xo1r + ys4832*xo2r) * (1 + pi484) + (ys4831*xo1u + ys4832*xo2u) * (1 + pi458) + (ys4831*xo1d + ys4832*xo2d) * (1 + pi508),
pi484 == (ys4841*xo1l + ys4842*xo2l) * (1 + pi483) + (ys4841*xo1r + ys4842*xo2r) * (1 + pi485) + (ys4841*xo1u + ys4842*xo2u) * (1 + pi459) + (ys4841*xo1d + ys4842*xo2d) * (1 + pi509),
pi485 == (ys4851*xo1l + ys4852*xo2l) * (1 + pi484) + (ys4851*xo1r + ys4852*xo2r) * (1 + pi486) + (ys4851*xo1u + ys4852*xo2u) * (1 + pi460) + (ys4851*xo1d + ys4852*xo2d) * (1 + pi510),
pi486 == (ys4861*xo1l + ys4862*xo2l) * (1 + pi485) + (ys4861*xo1r + ys4862*xo2r) * (1 + pi487) + (ys4861*xo1u + ys4862*xo2u) * (1 + pi461) + (ys4861*xo1d + ys4862*xo2d) * (1 + pi511),
pi487 == (ys4871*xo1l + ys4872*xo2l) * (1 + pi486) + (ys4871*xo1r + ys4872*xo2r) * (1 + pi488) + (ys4871*xo1u + ys4872*xo2u) * (1 + pi462) + (ys4871*xo1d + ys4872*xo2d) * (1 + pi512),
pi488 == (ys4881*xo1l + ys4882*xo2l) * (1 + pi487) + (ys4881*xo1r + ys4882*xo2r) * (1 + pi489) + (ys4881*xo1u + ys4882*xo2u) * (1 + pi463) + (ys4881*xo1d + ys4882*xo2d) * (1 + pi513),
pi489 == (ys4891*xo1l + ys4892*xo2l) * (1 + pi488) + (ys4891*xo1r + ys4892*xo2r) * (1 + pi490) + (ys4891*xo1u + ys4892*xo2u) * (1 + pi464) + (ys4891*xo1d + ys4892*xo2d) * (1 + pi514),
pi490 == (ys4901*xo1l + ys4902*xo2l) * (1 + pi489) + (ys4901*xo1r + ys4902*xo2r) * (1 + pi491) + (ys4901*xo1u + ys4902*xo2u) * (1 + pi465) + (ys4901*xo1d + ys4902*xo2d) * (1 + pi515),
pi491 == (ys4911*xo1l + ys4912*xo2l) * (1 + pi490) + (ys4911*xo1r + ys4912*xo2r) * (1 + pi492) + (ys4911*xo1u + ys4912*xo2u) * (1 + pi466) + (ys4911*xo1d + ys4912*xo2d) * (1 + pi516),
pi492 == (ys4921*xo1l + ys4922*xo2l) * (1 + pi491) + (ys4921*xo1r + ys4922*xo2r) * (1 + pi493) + (ys4921*xo1u + ys4922*xo2u) * (1 + pi467) + (ys4921*xo1d + ys4922*xo2d) * (1 + pi517),
pi493 == (ys4931*xo1l + ys4932*xo2l) * (1 + pi492) + (ys4931*xo1r + ys4932*xo2r) * (1 + pi494) + (ys4931*xo1u + ys4932*xo2u) * (1 + pi468) + (ys4931*xo1d + ys4932*xo2d) * (1 + pi518),
pi494 == (ys4941*xo1l + ys4942*xo2l) * (1 + pi493) + (ys4941*xo1r + ys4942*xo2r) * (1 + pi495) + (ys4941*xo1u + ys4942*xo2u) * (1 + pi469) + (ys4941*xo1d + ys4942*xo2d) * (1 + pi519),
pi495 == (ys4951*xo1l + ys4952*xo2l) * (1 + pi494) + (ys4951*xo1r + ys4952*xo2r) * (1 + pi496) + (ys4951*xo1u + ys4952*xo2u) * (1 + pi470) + (ys4951*xo1d + ys4952*xo2d) * (1 + pi520),
pi496 == (ys4961*xo1l + ys4962*xo2l) * (1 + pi495) + (ys4961*xo1r + ys4962*xo2r) * (1 + pi497) + (ys4961*xo1u + ys4962*xo2u) * (1 + pi471) + (ys4961*xo1d + ys4962*xo2d) * (1 + pi521),
pi497 == (ys4971*xo1l + ys4972*xo2l) * (1 + pi496) + (ys4971*xo1r + ys4972*xo2r) * (1 + pi498) + (ys4971*xo1u + ys4972*xo2u) * (1 + pi472) + (ys4971*xo1d + ys4972*xo2d) * (1 + pi522),
pi498 == (ys4981*xo1l + ys4982*xo2l) * (1 + pi497) + (ys4981*xo1r + ys4982*xo2r) * (1 + pi499) + (ys4981*xo1u + ys4982*xo2u) * (1 + pi473) + (ys4981*xo1d + ys4982*xo2d) * (1 + pi523),
pi499 == (ys4991*xo1l + ys4992*xo2l) * (1 + pi498) + (ys4991*xo1r + ys4992*xo2r) * (1 + pi499) + (ys4991*xo1u + ys4992*xo2u) * (1 + pi474) + (ys4991*xo1d + ys4992*xo2d) * (1 + pi524),
pi500 == (ys5001*xo1l + ys5002*xo2l) * (1 + pi500) + (ys5001*xo1r + ys5002*xo2r) * (1 + pi501) + (ys5001*xo1u + ys5002*xo2u) * (1 + pi475) + (ys5001*xo1d + ys5002*xo2d) * (1 + pi525),
pi501 == (ys5011*xo1l + ys5012*xo2l) * (1 + pi500) + (ys5011*xo1r + ys5012*xo2r) * (1 + pi502) + (ys5011*xo1u + ys5012*xo2u) * (1 + pi476) + (ys5011*xo1d + ys5012*xo2d) * (1 + pi526),
pi502 == (ys5021*xo1l + ys5022*xo2l) * (1 + pi501) + (ys5021*xo1r + ys5022*xo2r) * (1 + pi503) + (ys5021*xo1u + ys5022*xo2u) * (1 + pi477) + (ys5021*xo1d + ys5022*xo2d) * (1 + pi527),
pi503 == (ys5031*xo1l + ys5032*xo2l) * (1 + pi502) + (ys5031*xo1r + ys5032*xo2r) * (1 + pi504) + (ys5031*xo1u + ys5032*xo2u) * (1 + pi478) + (ys5031*xo1d + ys5032*xo2d) * (1 + pi528),
pi504 == (ys5041*xo1l + ys5042*xo2l) * (1 + pi503) + (ys5041*xo1r + ys5042*xo2r) * (1 + pi505) + (ys5041*xo1u + ys5042*xo2u) * (1 + pi479) + (ys5041*xo1d + ys5042*xo2d) * (1 + pi529),
pi505 == (ys5051*xo1l + ys5052*xo2l) * (1 + pi504) + (ys5051*xo1r + ys5052*xo2r) * (1 + pi506) + (ys5051*xo1u + ys5052*xo2u) * (1 + pi480) + (ys5051*xo1d + ys5052*xo2d) * (1 + pi530),
pi506 == (ys5061*xo1l + ys5062*xo2l) * (1 + pi505) + (ys5061*xo1r + ys5062*xo2r) * (1 + pi507) + (ys5061*xo1u + ys5062*xo2u) * (1 + pi481) + (ys5061*xo1d + ys5062*xo2d) * (1 + pi531),
pi507 == (ys5071*xo1l + ys5072*xo2l) * (1 + pi506) + (ys5071*xo1r + ys5072*xo2r) * (1 + pi508) + (ys5071*xo1u + ys5072*xo2u) * (1 + pi482) + (ys5071*xo1d + ys5072*xo2d) * (1 + pi532),
pi508 == (ys5081*xo1l + ys5082*xo2l) * (1 + pi507) + (ys5081*xo1r + ys5082*xo2r) * (1 + pi509) + (ys5081*xo1u + ys5082*xo2u) * (1 + pi483) + (ys5081*xo1d + ys5082*xo2d) * (1 + pi533),
pi509 == (ys5091*xo1l + ys5092*xo2l) * (1 + pi508) + (ys5091*xo1r + ys5092*xo2r) * (1 + pi510) + (ys5091*xo1u + ys5092*xo2u) * (1 + pi484) + (ys5091*xo1d + ys5092*xo2d) * (1 + pi534),
pi510 == (ys5101*xo1l + ys5102*xo2l) * (1 + pi509) + (ys5101*xo1r + ys5102*xo2r) * (1 + pi511) + (ys5101*xo1u + ys5102*xo2u) * (1 + pi485) + (ys5101*xo1d + ys5102*xo2d) * (1 + pi535),
pi511 == (ys5111*xo1l + ys5112*xo2l) * (1 + pi510) + (ys5111*xo1r + ys5112*xo2r) * (1 + pi512) + (ys5111*xo1u + ys5112*xo2u) * (1 + pi486) + (ys5111*xo1d + ys5112*xo2d) * (1 + pi536),
pi512 == (ys5121*xo1l + ys5122*xo2l) * (1 + pi511) + (ys5121*xo1r + ys5122*xo2r) * (1 + pi513) + (ys5121*xo1u + ys5122*xo2u) * (1 + pi487) + (ys5121*xo1d + ys5122*xo2d) * (1 + pi537),
pi513 == (ys5131*xo1l + ys5132*xo2l) * (1 + pi512) + (ys5131*xo1r + ys5132*xo2r) * (1 + pi514) + (ys5131*xo1u + ys5132*xo2u) * (1 + pi488) + (ys5131*xo1d + ys5132*xo2d) * (1 + pi538),
pi514 == (ys5141*xo1l + ys5142*xo2l) * (1 + pi513) + (ys5141*xo1r + ys5142*xo2r) * (1 + pi515) + (ys5141*xo1u + ys5142*xo2u) * (1 + pi489) + (ys5141*xo1d + ys5142*xo2d) * (1 + pi539),
pi515 == (ys5151*xo1l + ys5152*xo2l) * (1 + pi514) + (ys5151*xo1r + ys5152*xo2r) * (1 + pi516) + (ys5151*xo1u + ys5152*xo2u) * (1 + pi490) + (ys5151*xo1d + ys5152*xo2d) * (1 + pi540),
pi516 == (ys5161*xo1l + ys5162*xo2l) * (1 + pi515) + (ys5161*xo1r + ys5162*xo2r) * (1 + pi517) + (ys5161*xo1u + ys5162*xo2u) * (1 + pi491) + (ys5161*xo1d + ys5162*xo2d) * (1 + pi541),
pi517 == (ys5171*xo1l + ys5172*xo2l) * (1 + pi516) + (ys5171*xo1r + ys5172*xo2r) * (1 + pi518) + (ys5171*xo1u + ys5172*xo2u) * (1 + pi492) + (ys5171*xo1d + ys5172*xo2d) * (1 + pi542),
pi518 == (ys5181*xo1l + ys5182*xo2l) * (1 + pi517) + (ys5181*xo1r + ys5182*xo2r) * (1 + pi519) + (ys5181*xo1u + ys5182*xo2u) * (1 + pi493) + (ys5181*xo1d + ys5182*xo2d) * (1 + pi543),
pi519 == (ys5191*xo1l + ys5192*xo2l) * (1 + pi518) + (ys5191*xo1r + ys5192*xo2r) * (1 + pi520) + (ys5191*xo1u + ys5192*xo2u) * (1 + pi494) + (ys5191*xo1d + ys5192*xo2d) * (1 + pi544),
pi520 == (ys5201*xo1l + ys5202*xo2l) * (1 + pi519) + (ys5201*xo1r + ys5202*xo2r) * (1 + pi521) + (ys5201*xo1u + ys5202*xo2u) * (1 + pi495) + (ys5201*xo1d + ys5202*xo2d) * (1 + pi545),
pi521 == (ys5211*xo1l + ys5212*xo2l) * (1 + pi520) + (ys5211*xo1r + ys5212*xo2r) * (1 + pi522) + (ys5211*xo1u + ys5212*xo2u) * (1 + pi496) + (ys5211*xo1d + ys5212*xo2d) * (1 + pi546),
pi522 == (ys5221*xo1l + ys5222*xo2l) * (1 + pi521) + (ys5221*xo1r + ys5222*xo2r) * (1 + pi523) + (ys5221*xo1u + ys5222*xo2u) * (1 + pi497) + (ys5221*xo1d + ys5222*xo2d) * (1 + pi547),
pi523 == (ys5231*xo1l + ys5232*xo2l) * (1 + pi522) + (ys5231*xo1r + ys5232*xo2r) * (1 + pi524) + (ys5231*xo1u + ys5232*xo2u) * (1 + pi498) + (ys5231*xo1d + ys5232*xo2d) * (1 + pi548),
pi524 == (ys5241*xo1l + ys5242*xo2l) * (1 + pi523) + (ys5241*xo1r + ys5242*xo2r) * (1 + pi524) + (ys5241*xo1u + ys5242*xo2u) * (1 + pi499) + (ys5241*xo1d + ys5242*xo2d) * (1 + pi549),
pi525 == (ys5251*xo1l + ys5252*xo2l) * (1 + pi525) + (ys5251*xo1r + ys5252*xo2r) * (1 + pi526) + (ys5251*xo1u + ys5252*xo2u) * (1 + pi500) + (ys5251*xo1d + ys5252*xo2d) * (1 + pi550),
pi526 == (ys5261*xo1l + ys5262*xo2l) * (1 + pi525) + (ys5261*xo1r + ys5262*xo2r) * (1 + pi527) + (ys5261*xo1u + ys5262*xo2u) * (1 + pi501) + (ys5261*xo1d + ys5262*xo2d) * (1 + pi551),
pi527 == (ys5271*xo1l + ys5272*xo2l) * (1 + pi526) + (ys5271*xo1r + ys5272*xo2r) * (1 + pi528) + (ys5271*xo1u + ys5272*xo2u) * (1 + pi502) + (ys5271*xo1d + ys5272*xo2d) * (1 + pi552),
pi528 == (ys5281*xo1l + ys5282*xo2l) * (1 + pi527) + (ys5281*xo1r + ys5282*xo2r) * (1 + pi529) + (ys5281*xo1u + ys5282*xo2u) * (1 + pi503) + (ys5281*xo1d + ys5282*xo2d) * (1 + pi553),
pi529 == (ys5291*xo1l + ys5292*xo2l) * (1 + pi528) + (ys5291*xo1r + ys5292*xo2r) * (1 + pi530) + (ys5291*xo1u + ys5292*xo2u) * (1 + pi504) + (ys5291*xo1d + ys5292*xo2d) * (1 + pi554),
pi530 == (ys5301*xo1l + ys5302*xo2l) * (1 + pi529) + (ys5301*xo1r + ys5302*xo2r) * (1 + pi531) + (ys5301*xo1u + ys5302*xo2u) * (1 + pi505) + (ys5301*xo1d + ys5302*xo2d) * (1 + pi555),
pi531 == (ys5311*xo1l + ys5312*xo2l) * (1 + pi530) + (ys5311*xo1r + ys5312*xo2r) * (1 + pi532) + (ys5311*xo1u + ys5312*xo2u) * (1 + pi506) + (ys5311*xo1d + ys5312*xo2d) * (1 + pi556),
pi532 == (ys5321*xo1l + ys5322*xo2l) * (1 + pi531) + (ys5321*xo1r + ys5322*xo2r) * (1 + pi533) + (ys5321*xo1u + ys5322*xo2u) * (1 + pi507) + (ys5321*xo1d + ys5322*xo2d) * (1 + pi557),
pi533 == (ys5331*xo1l + ys5332*xo2l) * (1 + pi532) + (ys5331*xo1r + ys5332*xo2r) * (1 + pi534) + (ys5331*xo1u + ys5332*xo2u) * (1 + pi508) + (ys5331*xo1d + ys5332*xo2d) * (1 + pi558),
pi534 == (ys5341*xo1l + ys5342*xo2l) * (1 + pi533) + (ys5341*xo1r + ys5342*xo2r) * (1 + pi535) + (ys5341*xo1u + ys5342*xo2u) * (1 + pi509) + (ys5341*xo1d + ys5342*xo2d) * (1 + pi559),
pi535 == (ys5351*xo1l + ys5352*xo2l) * (1 + pi534) + (ys5351*xo1r + ys5352*xo2r) * (1 + pi536) + (ys5351*xo1u + ys5352*xo2u) * (1 + pi510) + (ys5351*xo1d + ys5352*xo2d) * (1 + pi560),
pi536 == (ys5361*xo1l + ys5362*xo2l) * (1 + pi535) + (ys5361*xo1r + ys5362*xo2r) * (1 + pi537) + (ys5361*xo1u + ys5362*xo2u) * (1 + pi511) + (ys5361*xo1d + ys5362*xo2d) * (1 + pi561),
pi537 == (ys5371*xo1l + ys5372*xo2l) * (1 + pi536) + (ys5371*xo1r + ys5372*xo2r) * (1 + pi538) + (ys5371*xo1u + ys5372*xo2u) * (1 + pi512) + (ys5371*xo1d + ys5372*xo2d) * (1 + pi562),
pi538 == (ys5381*xo1l + ys5382*xo2l) * (1 + pi537) + (ys5381*xo1r + ys5382*xo2r) * (1 + pi539) + (ys5381*xo1u + ys5382*xo2u) * (1 + pi513) + (ys5381*xo1d + ys5382*xo2d) * (1 + pi563),
pi539 == (ys5391*xo1l + ys5392*xo2l) * (1 + pi538) + (ys5391*xo1r + ys5392*xo2r) * (1 + pi540) + (ys5391*xo1u + ys5392*xo2u) * (1 + pi514) + (ys5391*xo1d + ys5392*xo2d) * (1 + pi564),
pi540 == (ys5401*xo1l + ys5402*xo2l) * (1 + pi539) + (ys5401*xo1r + ys5402*xo2r) * (1 + pi541) + (ys5401*xo1u + ys5402*xo2u) * (1 + pi515) + (ys5401*xo1d + ys5402*xo2d) * (1 + pi565),
pi541 == (ys5411*xo1l + ys5412*xo2l) * (1 + pi540) + (ys5411*xo1r + ys5412*xo2r) * (1 + pi542) + (ys5411*xo1u + ys5412*xo2u) * (1 + pi516) + (ys5411*xo1d + ys5412*xo2d) * (1 + pi566),
pi542 == (ys5421*xo1l + ys5422*xo2l) * (1 + pi541) + (ys5421*xo1r + ys5422*xo2r) * (1 + pi543) + (ys5421*xo1u + ys5422*xo2u) * (1 + pi517) + (ys5421*xo1d + ys5422*xo2d) * (1 + pi567),
pi543 == (ys5431*xo1l + ys5432*xo2l) * (1 + pi542) + (ys5431*xo1r + ys5432*xo2r) * (1 + pi544) + (ys5431*xo1u + ys5432*xo2u) * (1 + pi518) + (ys5431*xo1d + ys5432*xo2d) * (1 + pi568),
pi544 == (ys5441*xo1l + ys5442*xo2l) * (1 + pi543) + (ys5441*xo1r + ys5442*xo2r) * (1 + pi545) + (ys5441*xo1u + ys5442*xo2u) * (1 + pi519) + (ys5441*xo1d + ys5442*xo2d) * (1 + pi569),
pi545 == (ys5451*xo1l + ys5452*xo2l) * (1 + pi544) + (ys5451*xo1r + ys5452*xo2r) * (1 + pi546) + (ys5451*xo1u + ys5452*xo2u) * (1 + pi520) + (ys5451*xo1d + ys5452*xo2d) * (1 + pi570),
pi546 == (ys5461*xo1l + ys5462*xo2l) * (1 + pi545) + (ys5461*xo1r + ys5462*xo2r) * (1 + pi547) + (ys5461*xo1u + ys5462*xo2u) * (1 + pi521) + (ys5461*xo1d + ys5462*xo2d) * (1 + pi571),
pi547 == (ys5471*xo1l + ys5472*xo2l) * (1 + pi546) + (ys5471*xo1r + ys5472*xo2r) * (1 + pi548) + (ys5471*xo1u + ys5472*xo2u) * (1 + pi522) + (ys5471*xo1d + ys5472*xo2d) * (1 + pi572),
pi548 == (ys5481*xo1l + ys5482*xo2l) * (1 + pi547) + (ys5481*xo1r + ys5482*xo2r) * (1 + pi549) + (ys5481*xo1u + ys5482*xo2u) * (1 + pi523) + (ys5481*xo1d + ys5482*xo2d) * (1 + pi573),
pi549 == (ys5491*xo1l + ys5492*xo2l) * (1 + pi548) + (ys5491*xo1r + ys5492*xo2r) * (1 + pi549) + (ys5491*xo1u + ys5492*xo2u) * (1 + pi524) + (ys5491*xo1d + ys5492*xo2d) * (1 + pi574),
pi550 == (ys5501*xo1l + ys5502*xo2l) * (1 + pi550) + (ys5501*xo1r + ys5502*xo2r) * (1 + pi551) + (ys5501*xo1u + ys5502*xo2u) * (1 + pi525) + (ys5501*xo1d + ys5502*xo2d) * (1 + pi575),
pi551 == (ys5511*xo1l + ys5512*xo2l) * (1 + pi550) + (ys5511*xo1r + ys5512*xo2r) * (1 + pi552) + (ys5511*xo1u + ys5512*xo2u) * (1 + pi526) + (ys5511*xo1d + ys5512*xo2d) * (1 + pi576),
pi552 == (ys5521*xo1l + ys5522*xo2l) * (1 + pi551) + (ys5521*xo1r + ys5522*xo2r) * (1 + pi553) + (ys5521*xo1u + ys5522*xo2u) * (1 + pi527) + (ys5521*xo1d + ys5522*xo2d) * (1 + pi577),
pi553 == (ys5531*xo1l + ys5532*xo2l) * (1 + pi552) + (ys5531*xo1r + ys5532*xo2r) * (1 + pi554) + (ys5531*xo1u + ys5532*xo2u) * (1 + pi528) + (ys5531*xo1d + ys5532*xo2d) * (1 + pi578),
pi554 == (ys5541*xo1l + ys5542*xo2l) * (1 + pi553) + (ys5541*xo1r + ys5542*xo2r) * (1 + pi555) + (ys5541*xo1u + ys5542*xo2u) * (1 + pi529) + (ys5541*xo1d + ys5542*xo2d) * (1 + pi579),
pi555 == (ys5551*xo1l + ys5552*xo2l) * (1 + pi554) + (ys5551*xo1r + ys5552*xo2r) * (1 + pi556) + (ys5551*xo1u + ys5552*xo2u) * (1 + pi530) + (ys5551*xo1d + ys5552*xo2d) * (1 + pi580),
pi556 == (ys5561*xo1l + ys5562*xo2l) * (1 + pi555) + (ys5561*xo1r + ys5562*xo2r) * (1 + pi557) + (ys5561*xo1u + ys5562*xo2u) * (1 + pi531) + (ys5561*xo1d + ys5562*xo2d) * (1 + pi581),
pi557 == (ys5571*xo1l + ys5572*xo2l) * (1 + pi556) + (ys5571*xo1r + ys5572*xo2r) * (1 + pi558) + (ys5571*xo1u + ys5572*xo2u) * (1 + pi532) + (ys5571*xo1d + ys5572*xo2d) * (1 + pi582),
pi558 == (ys5581*xo1l + ys5582*xo2l) * (1 + pi557) + (ys5581*xo1r + ys5582*xo2r) * (1 + pi559) + (ys5581*xo1u + ys5582*xo2u) * (1 + pi533) + (ys5581*xo1d + ys5582*xo2d) * (1 + pi583),
pi559 == (ys5591*xo1l + ys5592*xo2l) * (1 + pi558) + (ys5591*xo1r + ys5592*xo2r) * (1 + pi560) + (ys5591*xo1u + ys5592*xo2u) * (1 + pi534) + (ys5591*xo1d + ys5592*xo2d) * (1 + pi584),
pi560 == (ys5601*xo1l + ys5602*xo2l) * (1 + pi559) + (ys5601*xo1r + ys5602*xo2r) * (1 + pi561) + (ys5601*xo1u + ys5602*xo2u) * (1 + pi535) + (ys5601*xo1d + ys5602*xo2d) * (1 + pi585),
pi561 == (ys5611*xo1l + ys5612*xo2l) * (1 + pi560) + (ys5611*xo1r + ys5612*xo2r) * (1 + pi562) + (ys5611*xo1u + ys5612*xo2u) * (1 + pi536) + (ys5611*xo1d + ys5612*xo2d) * (1 + pi586),
pi562 == (ys5621*xo1l + ys5622*xo2l) * (1 + pi561) + (ys5621*xo1r + ys5622*xo2r) * (1 + pi563) + (ys5621*xo1u + ys5622*xo2u) * (1 + pi537) + (ys5621*xo1d + ys5622*xo2d) * (1 + pi587),
pi563 == (ys5631*xo1l + ys5632*xo2l) * (1 + pi562) + (ys5631*xo1r + ys5632*xo2r) * (1 + pi564) + (ys5631*xo1u + ys5632*xo2u) * (1 + pi538) + (ys5631*xo1d + ys5632*xo2d) * (1 + pi588),
pi564 == (ys5641*xo1l + ys5642*xo2l) * (1 + pi563) + (ys5641*xo1r + ys5642*xo2r) * (1 + pi565) + (ys5641*xo1u + ys5642*xo2u) * (1 + pi539) + (ys5641*xo1d + ys5642*xo2d) * (1 + pi589),
pi565 == (ys5651*xo1l + ys5652*xo2l) * (1 + pi564) + (ys5651*xo1r + ys5652*xo2r) * (1 + pi566) + (ys5651*xo1u + ys5652*xo2u) * (1 + pi540) + (ys5651*xo1d + ys5652*xo2d) * (1 + pi590),
pi566 == (ys5661*xo1l + ys5662*xo2l) * (1 + pi565) + (ys5661*xo1r + ys5662*xo2r) * (1 + pi567) + (ys5661*xo1u + ys5662*xo2u) * (1 + pi541) + (ys5661*xo1d + ys5662*xo2d) * (1 + pi591),
pi567 == (ys5671*xo1l + ys5672*xo2l) * (1 + pi566) + (ys5671*xo1r + ys5672*xo2r) * (1 + pi568) + (ys5671*xo1u + ys5672*xo2u) * (1 + pi542) + (ys5671*xo1d + ys5672*xo2d) * (1 + pi592),
pi568 == (ys5681*xo1l + ys5682*xo2l) * (1 + pi567) + (ys5681*xo1r + ys5682*xo2r) * (1 + pi569) + (ys5681*xo1u + ys5682*xo2u) * (1 + pi543) + (ys5681*xo1d + ys5682*xo2d) * (1 + pi593),
pi569 == (ys5691*xo1l + ys5692*xo2l) * (1 + pi568) + (ys5691*xo1r + ys5692*xo2r) * (1 + pi570) + (ys5691*xo1u + ys5692*xo2u) * (1 + pi544) + (ys5691*xo1d + ys5692*xo2d) * (1 + pi594),
pi570 == (ys5701*xo1l + ys5702*xo2l) * (1 + pi569) + (ys5701*xo1r + ys5702*xo2r) * (1 + pi571) + (ys5701*xo1u + ys5702*xo2u) * (1 + pi545) + (ys5701*xo1d + ys5702*xo2d) * (1 + pi595),
pi571 == (ys5711*xo1l + ys5712*xo2l) * (1 + pi570) + (ys5711*xo1r + ys5712*xo2r) * (1 + pi572) + (ys5711*xo1u + ys5712*xo2u) * (1 + pi546) + (ys5711*xo1d + ys5712*xo2d) * (1 + pi596),
pi572 == (ys5721*xo1l + ys5722*xo2l) * (1 + pi571) + (ys5721*xo1r + ys5722*xo2r) * (1 + pi573) + (ys5721*xo1u + ys5722*xo2u) * (1 + pi547) + (ys5721*xo1d + ys5722*xo2d) * (1 + pi597),
pi573 == (ys5731*xo1l + ys5732*xo2l) * (1 + pi572) + (ys5731*xo1r + ys5732*xo2r) * (1 + pi574) + (ys5731*xo1u + ys5732*xo2u) * (1 + pi548) + (ys5731*xo1d + ys5732*xo2d) * (1 + pi598),
pi574 == (ys5741*xo1l + ys5742*xo2l) * (1 + pi573) + (ys5741*xo1r + ys5742*xo2r) * (1 + pi574) + (ys5741*xo1u + ys5742*xo2u) * (1 + pi549) + (ys5741*xo1d + ys5742*xo2d) * (1 + pi599),
pi575 == (ys5751*xo1l + ys5752*xo2l) * (1 + pi575) + (ys5751*xo1r + ys5752*xo2r) * (1 + pi576) + (ys5751*xo1u + ys5752*xo2u) * (1 + pi550) + (ys5751*xo1d + ys5752*xo2d) * (1 + pi600),
pi576 == (ys5761*xo1l + ys5762*xo2l) * (1 + pi575) + (ys5761*xo1r + ys5762*xo2r) * (1 + pi577) + (ys5761*xo1u + ys5762*xo2u) * (1 + pi551) + (ys5761*xo1d + ys5762*xo2d) * (1 + pi601),
pi577 == (ys5771*xo1l + ys5772*xo2l) * (1 + pi576) + (ys5771*xo1r + ys5772*xo2r) * (1 + pi578) + (ys5771*xo1u + ys5772*xo2u) * (1 + pi552) + (ys5771*xo1d + ys5772*xo2d) * (1 + pi602),
pi578 == (ys5781*xo1l + ys5782*xo2l) * (1 + pi577) + (ys5781*xo1r + ys5782*xo2r) * (1 + pi579) + (ys5781*xo1u + ys5782*xo2u) * (1 + pi553) + (ys5781*xo1d + ys5782*xo2d) * (1 + pi603),
pi579 == (ys5791*xo1l + ys5792*xo2l) * (1 + pi578) + (ys5791*xo1r + ys5792*xo2r) * (1 + pi580) + (ys5791*xo1u + ys5792*xo2u) * (1 + pi554) + (ys5791*xo1d + ys5792*xo2d) * (1 + pi604),
pi580 == (ys5801*xo1l + ys5802*xo2l) * (1 + pi579) + (ys5801*xo1r + ys5802*xo2r) * (1 + pi581) + (ys5801*xo1u + ys5802*xo2u) * (1 + pi555) + (ys5801*xo1d + ys5802*xo2d) * (1 + pi605),
pi581 == (ys5811*xo1l + ys5812*xo2l) * (1 + pi580) + (ys5811*xo1r + ys5812*xo2r) * (1 + pi582) + (ys5811*xo1u + ys5812*xo2u) * (1 + pi556) + (ys5811*xo1d + ys5812*xo2d) * (1 + pi606),
pi582 == (ys5821*xo1l + ys5822*xo2l) * (1 + pi581) + (ys5821*xo1r + ys5822*xo2r) * (1 + pi583) + (ys5821*xo1u + ys5822*xo2u) * (1 + pi557) + (ys5821*xo1d + ys5822*xo2d) * (1 + pi607),
pi583 == (ys5831*xo1l + ys5832*xo2l) * (1 + pi582) + (ys5831*xo1r + ys5832*xo2r) * (1 + pi584) + (ys5831*xo1u + ys5832*xo2u) * (1 + pi558) + (ys5831*xo1d + ys5832*xo2d) * (1 + pi608),
pi584 == (ys5841*xo1l + ys5842*xo2l) * (1 + pi583) + (ys5841*xo1r + ys5842*xo2r) * (1 + pi585) + (ys5841*xo1u + ys5842*xo2u) * (1 + pi559) + (ys5841*xo1d + ys5842*xo2d) * (1 + pi609),
pi585 == (ys5851*xo1l + ys5852*xo2l) * (1 + pi584) + (ys5851*xo1r + ys5852*xo2r) * (1 + pi586) + (ys5851*xo1u + ys5852*xo2u) * (1 + pi560) + (ys5851*xo1d + ys5852*xo2d) * (1 + pi610),
pi586 == (ys5861*xo1l + ys5862*xo2l) * (1 + pi585) + (ys5861*xo1r + ys5862*xo2r) * (1 + pi587) + (ys5861*xo1u + ys5862*xo2u) * (1 + pi561) + (ys5861*xo1d + ys5862*xo2d) * (1 + pi611),
pi587 == (ys5871*xo1l + ys5872*xo2l) * (1 + pi586) + (ys5871*xo1r + ys5872*xo2r) * (1 + pi588) + (ys5871*xo1u + ys5872*xo2u) * (1 + pi562) + (ys5871*xo1d + ys5872*xo2d) * (1 + pi612),
pi588 == (ys5881*xo1l + ys5882*xo2l) * (1 + pi587) + (ys5881*xo1r + ys5882*xo2r) * (1 + pi589) + (ys5881*xo1u + ys5882*xo2u) * (1 + pi563) + (ys5881*xo1d + ys5882*xo2d) * (1 + pi613),
pi589 == (ys5891*xo1l + ys5892*xo2l) * (1 + pi588) + (ys5891*xo1r + ys5892*xo2r) * (1 + pi590) + (ys5891*xo1u + ys5892*xo2u) * (1 + pi564) + (ys5891*xo1d + ys5892*xo2d) * (1 + pi614),
pi590 == (ys5901*xo1l + ys5902*xo2l) * (1 + pi589) + (ys5901*xo1r + ys5902*xo2r) * (1 + pi591) + (ys5901*xo1u + ys5902*xo2u) * (1 + pi565) + (ys5901*xo1d + ys5902*xo2d) * (1 + pi615),
pi591 == (ys5911*xo1l + ys5912*xo2l) * (1 + pi590) + (ys5911*xo1r + ys5912*xo2r) * (1 + pi592) + (ys5911*xo1u + ys5912*xo2u) * (1 + pi566) + (ys5911*xo1d + ys5912*xo2d) * (1 + pi616),
pi592 == (ys5921*xo1l + ys5922*xo2l) * (1 + pi591) + (ys5921*xo1r + ys5922*xo2r) * (1 + pi593) + (ys5921*xo1u + ys5922*xo2u) * (1 + pi567) + (ys5921*xo1d + ys5922*xo2d) * (1 + pi617),
pi593 == (ys5931*xo1l + ys5932*xo2l) * (1 + pi592) + (ys5931*xo1r + ys5932*xo2r) * (1 + pi594) + (ys5931*xo1u + ys5932*xo2u) * (1 + pi568) + (ys5931*xo1d + ys5932*xo2d) * (1 + pi618),
pi594 == (ys5941*xo1l + ys5942*xo2l) * (1 + pi593) + (ys5941*xo1r + ys5942*xo2r) * (1 + pi595) + (ys5941*xo1u + ys5942*xo2u) * (1 + pi569) + (ys5941*xo1d + ys5942*xo2d) * (1 + pi619),
pi595 == (ys5951*xo1l + ys5952*xo2l) * (1 + pi594) + (ys5951*xo1r + ys5952*xo2r) * (1 + pi596) + (ys5951*xo1u + ys5952*xo2u) * (1 + pi570) + (ys5951*xo1d + ys5952*xo2d) * (1 + pi620),
pi596 == (ys5961*xo1l + ys5962*xo2l) * (1 + pi595) + (ys5961*xo1r + ys5962*xo2r) * (1 + pi597) + (ys5961*xo1u + ys5962*xo2u) * (1 + pi571) + (ys5961*xo1d + ys5962*xo2d) * (1 + pi621),
pi597 == (ys5971*xo1l + ys5972*xo2l) * (1 + pi596) + (ys5971*xo1r + ys5972*xo2r) * (1 + pi598) + (ys5971*xo1u + ys5972*xo2u) * (1 + pi572) + (ys5971*xo1d + ys5972*xo2d) * (1 + pi622),
pi598 == (ys5981*xo1l + ys5982*xo2l) * (1 + pi597) + (ys5981*xo1r + ys5982*xo2r) * (1 + pi599) + (ys5981*xo1u + ys5982*xo2u) * (1 + pi573) + (ys5981*xo1d + ys5982*xo2d) * (1 + pi623),
pi599 == (ys5991*xo1l + ys5992*xo2l) * (1 + pi598) + (ys5991*xo1r + ys5992*xo2r) * (1 + pi599) + (ys5991*xo1u + ys5992*xo2u) * (1 + pi574) + (ys5991*xo1d + ys5992*xo2d) * (1 + pi624),
pi600 == (ys6001*xo1l + ys6002*xo2l) * (1 + pi600) + (ys6001*xo1r + ys6002*xo2r) * (1 + pi601) + (ys6001*xo1u + ys6002*xo2u) * (1 + pi575) + (ys6001*xo1d + ys6002*xo2d) * (1 + pi600),
pi601 == (ys6011*xo1l + ys6012*xo2l) * (1 + pi600) + (ys6011*xo1r + ys6012*xo2r) * (1 + pi602) + (ys6011*xo1u + ys6012*xo2u) * (1 + pi576) + (ys6011*xo1d + ys6012*xo2d) * (1 + pi601),
pi602 == (ys6021*xo1l + ys6022*xo2l) * (1 + pi601) + (ys6021*xo1r + ys6022*xo2r) * (1 + pi603) + (ys6021*xo1u + ys6022*xo2u) * (1 + pi577) + (ys6021*xo1d + ys6022*xo2d) * (1 + pi602),
pi603 == (ys6031*xo1l + ys6032*xo2l) * (1 + pi602) + (ys6031*xo1r + ys6032*xo2r) * (1 + pi604) + (ys6031*xo1u + ys6032*xo2u) * (1 + pi578) + (ys6031*xo1d + ys6032*xo2d) * (1 + pi603),
pi604 == (ys6041*xo1l + ys6042*xo2l) * (1 + pi603) + (ys6041*xo1r + ys6042*xo2r) * (1 + pi605) + (ys6041*xo1u + ys6042*xo2u) * (1 + pi579) + (ys6041*xo1d + ys6042*xo2d) * (1 + pi604),
pi605 == (ys6051*xo1l + ys6052*xo2l) * (1 + pi604) + (ys6051*xo1r + ys6052*xo2r) * (1 + pi606) + (ys6051*xo1u + ys6052*xo2u) * (1 + pi580) + (ys6051*xo1d + ys6052*xo2d) * (1 + pi605),
pi606 == (ys6061*xo1l + ys6062*xo2l) * (1 + pi605) + (ys6061*xo1r + ys6062*xo2r) * (1 + pi607) + (ys6061*xo1u + ys6062*xo2u) * (1 + pi581) + (ys6061*xo1d + ys6062*xo2d) * (1 + pi606),
pi607 == (ys6071*xo1l + ys6072*xo2l) * (1 + pi606) + (ys6071*xo1r + ys6072*xo2r) * (1 + pi608) + (ys6071*xo1u + ys6072*xo2u) * (1 + pi582) + (ys6071*xo1d + ys6072*xo2d) * (1 + pi607),
pi608 == (ys6081*xo1l + ys6082*xo2l) * (1 + pi607) + (ys6081*xo1r + ys6082*xo2r) * (1 + pi609) + (ys6081*xo1u + ys6082*xo2u) * (1 + pi583) + (ys6081*xo1d + ys6082*xo2d) * (1 + pi608),
pi609 == (ys6091*xo1l + ys6092*xo2l) * (1 + pi608) + (ys6091*xo1r + ys6092*xo2r) * (1 + pi610) + (ys6091*xo1u + ys6092*xo2u) * (1 + pi584) + (ys6091*xo1d + ys6092*xo2d) * (1 + pi609),
pi610 == (ys6101*xo1l + ys6102*xo2l) * (1 + pi609) + (ys6101*xo1r + ys6102*xo2r) * (1 + pi611) + (ys6101*xo1u + ys6102*xo2u) * (1 + pi585) + (ys6101*xo1d + ys6102*xo2d) * (1 + pi610),
pi611 == (ys6111*xo1l + ys6112*xo2l) * (1 + pi610) + (ys6111*xo1r + ys6112*xo2r) * (1 + pi612) + (ys6111*xo1u + ys6112*xo2u) * (1 + pi586) + (ys6111*xo1d + ys6112*xo2d) * (1 + pi611),
pi612 == (ys6121*xo1l + ys6122*xo2l) * (1 + pi611) + (ys6121*xo1r + ys6122*xo2r) * (1 + pi613) + (ys6121*xo1u + ys6122*xo2u) * (1 + pi587) + (ys6121*xo1d + ys6122*xo2d) * (1 + pi612),
pi613 == (ys6131*xo1l + ys6132*xo2l) * (1 + pi612) + (ys6131*xo1r + ys6132*xo2r) * (1 + pi614) + (ys6131*xo1u + ys6132*xo2u) * (1 + pi588) + (ys6131*xo1d + ys6132*xo2d) * (1 + pi613),
pi614 == (ys6141*xo1l + ys6142*xo2l) * (1 + pi613) + (ys6141*xo1r + ys6142*xo2r) * (1 + pi615) + (ys6141*xo1u + ys6142*xo2u) * (1 + pi589) + (ys6141*xo1d + ys6142*xo2d) * (1 + pi614),
pi615 == (ys6151*xo1l + ys6152*xo2l) * (1 + pi614) + (ys6151*xo1r + ys6152*xo2r) * (1 + pi616) + (ys6151*xo1u + ys6152*xo2u) * (1 + pi590) + (ys6151*xo1d + ys6152*xo2d) * (1 + pi615),
pi616 == (ys6161*xo1l + ys6162*xo2l) * (1 + pi615) + (ys6161*xo1r + ys6162*xo2r) * (1 + pi617) + (ys6161*xo1u + ys6162*xo2u) * (1 + pi591) + (ys6161*xo1d + ys6162*xo2d) * (1 + pi616),
pi617 == (ys6171*xo1l + ys6172*xo2l) * (1 + pi616) + (ys6171*xo1r + ys6172*xo2r) * (1 + pi618) + (ys6171*xo1u + ys6172*xo2u) * (1 + pi592) + (ys6171*xo1d + ys6172*xo2d) * (1 + pi617),
pi618 == (ys6181*xo1l + ys6182*xo2l) * (1 + pi617) + (ys6181*xo1r + ys6182*xo2r) * (1 + pi619) + (ys6181*xo1u + ys6182*xo2u) * (1 + pi593) + (ys6181*xo1d + ys6182*xo2d) * (1 + pi618),
pi619 == (ys6191*xo1l + ys6192*xo2l) * (1 + pi618) + (ys6191*xo1r + ys6192*xo2r) * (1 + pi620) + (ys6191*xo1u + ys6192*xo2u) * (1 + pi594) + (ys6191*xo1d + ys6192*xo2d) * (1 + pi619),
pi620 == (ys6201*xo1l + ys6202*xo2l) * (1 + pi619) + (ys6201*xo1r + ys6202*xo2r) * (1 + pi621) + (ys6201*xo1u + ys6202*xo2u) * (1 + pi595) + (ys6201*xo1d + ys6202*xo2d) * (1 + pi620),
pi621 == (ys6211*xo1l + ys6212*xo2l) * (1 + pi620) + (ys6211*xo1r + ys6212*xo2r) * (1 + pi622) + (ys6211*xo1u + ys6212*xo2u) * (1 + pi596) + (ys6211*xo1d + ys6212*xo2d) * (1 + pi621),
pi622 == (ys6221*xo1l + ys6222*xo2l) * (1 + pi621) + (ys6221*xo1r + ys6222*xo2r) * (1 + pi623) + (ys6221*xo1u + ys6222*xo2u) * (1 + pi597) + (ys6221*xo1d + ys6222*xo2d) * (1 + pi622),
pi623 == (ys6231*xo1l + ys6232*xo2l) * (1 + pi622) + (ys6231*xo1r + ys6232*xo2r) * (1 + pi624) + (ys6231*xo1u + ys6232*xo2u) * (1 + pi598) + (ys6231*xo1d + ys6232*xo2d) * (1 + pi623),
pi624 == 0, 
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <= Q(15000,624)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi99+pi100+pi101+pi102+pi103+pi104+pi105+pi106+pi107+pi108+pi109+pi110+pi111+pi112+pi113+pi114+pi115+pi116+pi117+pi118+pi119+pi120+pi121+pi122+pi123+pi124+pi125+pi126+pi127+pi128+pi129+pi130+pi131+pi132+pi133+pi134+pi135+pi136+pi137+pi138+pi139+pi140+pi141+pi142+pi143+pi144+pi145+pi146+pi147+pi148+pi149+pi150+pi151+pi152+pi153+pi154+pi155+pi156+pi157+pi158+pi159+pi160+pi161+pi162+pi163+pi164+pi165+pi166+pi167+pi168+pi169+pi170+pi171+pi172+pi173+pi174+pi175+pi176+pi177+pi178+pi179+pi180+pi181+pi182+pi183+pi184+pi185+pi186+pi187+pi188+pi189+pi190+pi191+pi192+pi193+pi194+pi195+pi196+pi197+pi198+pi199+pi200+pi201+pi202+pi203+pi204+pi205+pi206+pi207+pi208+pi209+pi210+pi211+pi212+pi213+pi214+pi215+pi216+pi217+pi218+pi219+pi220+pi221+pi222+pi223+pi224+pi225+pi226+pi227+pi228+pi229+pi230+pi231+pi232+pi233+pi234+pi235+pi236+pi237+pi238+pi239+pi240+pi241+pi242+pi243+pi244+pi245+pi246+pi247+pi248+pi249+pi250+pi251+pi252+pi253+pi254+pi255+pi256+pi257+pi258+pi259+pi260+pi261+pi262+pi263+pi264+pi265+pi266+pi267+pi268+pi269+pi270+pi271+pi272+pi273+pi274+pi275+pi276+pi277+pi278+pi279+pi280+pi281+pi282+pi283+pi284+pi285+pi286+pi287+pi288+pi289+pi290+pi291+pi292+pi293+pi294+pi295+pi296+pi297+pi298+pi299+pi300+pi301+pi302+pi303+pi304+pi305+pi306+pi307+pi308+pi309+pi310+pi311+pi312+pi313+pi314+pi315+pi316+pi317+pi318+pi319+pi320+pi321+pi322+pi323+pi324+pi325+pi326+pi327+pi328+pi329+pi330+pi331+pi332+pi333+pi334+pi335+pi336+pi337+pi338+pi339+pi340+pi341+pi342+pi343+pi344+pi345+pi346+pi347+pi348+pi349+pi350+pi351+pi352+pi353+pi354+pi355+pi356+pi357+pi358+pi359+pi360+pi361+pi362+pi363+pi364+pi365+pi366+pi367+pi368+pi369+pi370+pi371+pi372+pi373+pi374+pi375+pi376+pi377+pi378+pi379+pi380+pi381+pi382+pi383+pi384+pi385+pi386+pi387+pi388+pi389+pi390+pi391+pi392+pi393+pi394+pi395+pi396+pi397+pi398+pi399+pi400+pi401+pi402+pi403+pi404+pi405+pi406+pi407+pi408+pi409+pi410+pi411+pi412+pi413+pi414+pi415+pi416+pi417+pi418+pi419+pi420+pi421+pi422+pi423+pi424+pi425+pi426+pi427+pi428+pi429+pi430+pi431+pi432+pi433+pi434+pi435+pi436+pi437+pi438+pi439+pi440+pi441+pi442+pi443+pi444+pi445+pi446+pi447+pi448+pi449+pi450+pi451+pi452+pi453+pi454+pi455+pi456+pi457+pi458+pi459+pi460+pi461+pi462+pi463+pi464+pi465+pi466+pi467+pi468+pi469+pi470+pi471+pi472+pi473+pi474+pi475+pi476+pi477+pi478+pi479+pi480+pi481+pi482+pi483+pi484+pi485+pi486+pi487+pi488+pi489+pi490+pi491+pi492+pi493+pi494+pi495+pi496+pi497+pi498+pi499+pi500+pi501+pi502+pi503+pi504+pi505+pi506+pi507+pi508+pi509+pi510+pi511+pi512+pi513+pi514+pi515+pi516+pi517+pi518+pi519+pi520+pi521+pi522+pi523+pi524+pi525+pi526+pi527+pi528+pi529+pi530+pi531+pi532+pi533+pi534+pi535+pi536+pi537+pi538+pi539+pi540+pi541+pi542+pi543+pi544+pi545+pi546+pi547+pi548+pi549+pi550+pi551+pi552+pi553+pi554+pi555+pi556+pi557+pi558+pi559+pi560+pi561+pi562+pi563+pi564+pi565+pi566+pi567+pi568+pi569+pi570+pi571+pi572+pi573+pi574+pi575+pi576+pi577+pi578+pi579+pi580+pi581+pi582+pi583+pi584+pi585+pi586+pi587+pi588+pi589+pi590+pi591+pi592+pi593+pi594+pi595+pi596+pi597+pi598+pi599+pi600+pi601+pi602+pi603+pi604+pi605+pi606+pi607+pi608+pi609+pi610+pi611+pi612+pi613+pi614+pi615+pi616+pi617+pi618+pi619+pi620+pi621+pi622+pi623) * Q(1,624) <= Q(15000,624),
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
Or(ys1881== 0 , ys1881== 1),
Or(ys1882== 0 , ys1882== 1),
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
Or(ys3771== 0 , ys3771== 1),
Or(ys3772== 0 , ys3772== 1),
Or(ys3781== 0 , ys3781== 1),
Or(ys3782== 0 , ys3782== 1),
Or(ys3791== 0 , ys3791== 1),
Or(ys3792== 0 , ys3792== 1),
Or(ys3801== 0 , ys3801== 1),
Or(ys3802== 0 , ys3802== 1),
Or(ys3811== 0 , ys3811== 1),
Or(ys3812== 0 , ys3812== 1),
Or(ys3821== 0 , ys3821== 1),
Or(ys3822== 0 , ys3822== 1),
Or(ys3831== 0 , ys3831== 1),
Or(ys3832== 0 , ys3832== 1),
Or(ys3841== 0 , ys3841== 1),
Or(ys3842== 0 , ys3842== 1),
Or(ys3851== 0 , ys3851== 1),
Or(ys3852== 0 , ys3852== 1),
Or(ys3861== 0 , ys3861== 1),
Or(ys3862== 0 , ys3862== 1),
Or(ys3871== 0 , ys3871== 1),
Or(ys3872== 0 , ys3872== 1),
Or(ys3881== 0 , ys3881== 1),
Or(ys3882== 0 , ys3882== 1),
Or(ys3891== 0 , ys3891== 1),
Or(ys3892== 0 , ys3892== 1),
Or(ys3901== 0 , ys3901== 1),
Or(ys3902== 0 , ys3902== 1),
Or(ys3911== 0 , ys3911== 1),
Or(ys3912== 0 , ys3912== 1),
Or(ys3921== 0 , ys3921== 1),
Or(ys3922== 0 , ys3922== 1),
Or(ys3931== 0 , ys3931== 1),
Or(ys3932== 0 , ys3932== 1),
Or(ys3941== 0 , ys3941== 1),
Or(ys3942== 0 , ys3942== 1),
Or(ys3951== 0 , ys3951== 1),
Or(ys3952== 0 , ys3952== 1),
Or(ys3961== 0 , ys3961== 1),
Or(ys3962== 0 , ys3962== 1),
Or(ys3971== 0 , ys3971== 1),
Or(ys3972== 0 , ys3972== 1),
Or(ys3981== 0 , ys3981== 1),
Or(ys3982== 0 , ys3982== 1),
Or(ys3991== 0 , ys3991== 1),
Or(ys3992== 0 , ys3992== 1),
Or(ys4001== 0 , ys4001== 1),
Or(ys4002== 0 , ys4002== 1),
Or(ys4011== 0 , ys4011== 1),
Or(ys4012== 0 , ys4012== 1),
Or(ys4021== 0 , ys4021== 1),
Or(ys4022== 0 , ys4022== 1),
Or(ys4031== 0 , ys4031== 1),
Or(ys4032== 0 , ys4032== 1),
Or(ys4041== 0 , ys4041== 1),
Or(ys4042== 0 , ys4042== 1),
Or(ys4051== 0 , ys4051== 1),
Or(ys4052== 0 , ys4052== 1),
Or(ys4061== 0 , ys4061== 1),
Or(ys4062== 0 , ys4062== 1),
Or(ys4071== 0 , ys4071== 1),
Or(ys4072== 0 , ys4072== 1),
Or(ys4081== 0 , ys4081== 1),
Or(ys4082== 0 , ys4082== 1),
Or(ys4091== 0 , ys4091== 1),
Or(ys4092== 0 , ys4092== 1),
Or(ys4101== 0 , ys4101== 1),
Or(ys4102== 0 , ys4102== 1),
Or(ys4111== 0 , ys4111== 1),
Or(ys4112== 0 , ys4112== 1),
Or(ys4121== 0 , ys4121== 1),
Or(ys4122== 0 , ys4122== 1),
Or(ys4131== 0 , ys4131== 1),
Or(ys4132== 0 , ys4132== 1),
Or(ys4141== 0 , ys4141== 1),
Or(ys4142== 0 , ys4142== 1),
Or(ys4151== 0 , ys4151== 1),
Or(ys4152== 0 , ys4152== 1),
Or(ys4161== 0 , ys4161== 1),
Or(ys4162== 0 , ys4162== 1),
Or(ys4171== 0 , ys4171== 1),
Or(ys4172== 0 , ys4172== 1),
Or(ys4181== 0 , ys4181== 1),
Or(ys4182== 0 , ys4182== 1),
Or(ys4191== 0 , ys4191== 1),
Or(ys4192== 0 , ys4192== 1),
Or(ys4201== 0 , ys4201== 1),
Or(ys4202== 0 , ys4202== 1),
Or(ys4211== 0 , ys4211== 1),
Or(ys4212== 0 , ys4212== 1),
Or(ys4221== 0 , ys4221== 1),
Or(ys4222== 0 , ys4222== 1),
Or(ys4231== 0 , ys4231== 1),
Or(ys4232== 0 , ys4232== 1),
Or(ys4241== 0 , ys4241== 1),
Or(ys4242== 0 , ys4242== 1),
Or(ys4251== 0 , ys4251== 1),
Or(ys4252== 0 , ys4252== 1),
Or(ys4261== 0 , ys4261== 1),
Or(ys4262== 0 , ys4262== 1),
Or(ys4271== 0 , ys4271== 1),
Or(ys4272== 0 , ys4272== 1),
Or(ys4281== 0 , ys4281== 1),
Or(ys4282== 0 , ys4282== 1),
Or(ys4291== 0 , ys4291== 1),
Or(ys4292== 0 , ys4292== 1),
Or(ys4301== 0 , ys4301== 1),
Or(ys4302== 0 , ys4302== 1),
Or(ys4311== 0 , ys4311== 1),
Or(ys4312== 0 , ys4312== 1),
Or(ys4321== 0 , ys4321== 1),
Or(ys4322== 0 , ys4322== 1),
Or(ys4331== 0 , ys4331== 1),
Or(ys4332== 0 , ys4332== 1),
Or(ys4341== 0 , ys4341== 1),
Or(ys4342== 0 , ys4342== 1),
Or(ys4351== 0 , ys4351== 1),
Or(ys4352== 0 , ys4352== 1),
Or(ys4361== 0 , ys4361== 1),
Or(ys4362== 0 , ys4362== 1),
Or(ys4371== 0 , ys4371== 1),
Or(ys4372== 0 , ys4372== 1),
Or(ys4381== 0 , ys4381== 1),
Or(ys4382== 0 , ys4382== 1),
Or(ys4391== 0 , ys4391== 1),
Or(ys4392== 0 , ys4392== 1),
Or(ys4401== 0 , ys4401== 1),
Or(ys4402== 0 , ys4402== 1),
Or(ys4411== 0 , ys4411== 1),
Or(ys4412== 0 , ys4412== 1),
Or(ys4421== 0 , ys4421== 1),
Or(ys4422== 0 , ys4422== 1),
Or(ys4431== 0 , ys4431== 1),
Or(ys4432== 0 , ys4432== 1),
Or(ys4441== 0 , ys4441== 1),
Or(ys4442== 0 , ys4442== 1),
Or(ys4451== 0 , ys4451== 1),
Or(ys4452== 0 , ys4452== 1),
Or(ys4461== 0 , ys4461== 1),
Or(ys4462== 0 , ys4462== 1),
Or(ys4471== 0 , ys4471== 1),
Or(ys4472== 0 , ys4472== 1),
Or(ys4481== 0 , ys4481== 1),
Or(ys4482== 0 , ys4482== 1),
Or(ys4491== 0 , ys4491== 1),
Or(ys4492== 0 , ys4492== 1),
Or(ys4501== 0 , ys4501== 1),
Or(ys4502== 0 , ys4502== 1),
Or(ys4511== 0 , ys4511== 1),
Or(ys4512== 0 , ys4512== 1),
Or(ys4521== 0 , ys4521== 1),
Or(ys4522== 0 , ys4522== 1),
Or(ys4531== 0 , ys4531== 1),
Or(ys4532== 0 , ys4532== 1),
Or(ys4541== 0 , ys4541== 1),
Or(ys4542== 0 , ys4542== 1),
Or(ys4551== 0 , ys4551== 1),
Or(ys4552== 0 , ys4552== 1),
Or(ys4561== 0 , ys4561== 1),
Or(ys4562== 0 , ys4562== 1),
Or(ys4571== 0 , ys4571== 1),
Or(ys4572== 0 , ys4572== 1),
Or(ys4581== 0 , ys4581== 1),
Or(ys4582== 0 , ys4582== 1),
Or(ys4591== 0 , ys4591== 1),
Or(ys4592== 0 , ys4592== 1),
Or(ys4601== 0 , ys4601== 1),
Or(ys4602== 0 , ys4602== 1),
Or(ys4611== 0 , ys4611== 1),
Or(ys4612== 0 , ys4612== 1),
Or(ys4621== 0 , ys4621== 1),
Or(ys4622== 0 , ys4622== 1),
Or(ys4631== 0 , ys4631== 1),
Or(ys4632== 0 , ys4632== 1),
Or(ys4641== 0 , ys4641== 1),
Or(ys4642== 0 , ys4642== 1),
Or(ys4651== 0 , ys4651== 1),
Or(ys4652== 0 , ys4652== 1),
Or(ys4661== 0 , ys4661== 1),
Or(ys4662== 0 , ys4662== 1),
Or(ys4671== 0 , ys4671== 1),
Or(ys4672== 0 , ys4672== 1),
Or(ys4681== 0 , ys4681== 1),
Or(ys4682== 0 , ys4682== 1),
Or(ys4691== 0 , ys4691== 1),
Or(ys4692== 0 , ys4692== 1),
Or(ys4701== 0 , ys4701== 1),
Or(ys4702== 0 , ys4702== 1),
Or(ys4711== 0 , ys4711== 1),
Or(ys4712== 0 , ys4712== 1),
Or(ys4721== 0 , ys4721== 1),
Or(ys4722== 0 , ys4722== 1),
Or(ys4731== 0 , ys4731== 1),
Or(ys4732== 0 , ys4732== 1),
Or(ys4741== 0 , ys4741== 1),
Or(ys4742== 0 , ys4742== 1),
Or(ys4751== 0 , ys4751== 1),
Or(ys4752== 0 , ys4752== 1),
Or(ys4761== 0 , ys4761== 1),
Or(ys4762== 0 , ys4762== 1),
Or(ys4771== 0 , ys4771== 1),
Or(ys4772== 0 , ys4772== 1),
Or(ys4781== 0 , ys4781== 1),
Or(ys4782== 0 , ys4782== 1),
Or(ys4791== 0 , ys4791== 1),
Or(ys4792== 0 , ys4792== 1),
Or(ys4801== 0 , ys4801== 1),
Or(ys4802== 0 , ys4802== 1),
Or(ys4811== 0 , ys4811== 1),
Or(ys4812== 0 , ys4812== 1),
Or(ys4821== 0 , ys4821== 1),
Or(ys4822== 0 , ys4822== 1),
Or(ys4831== 0 , ys4831== 1),
Or(ys4832== 0 , ys4832== 1),
Or(ys4841== 0 , ys4841== 1),
Or(ys4842== 0 , ys4842== 1),
Or(ys4851== 0 , ys4851== 1),
Or(ys4852== 0 , ys4852== 1),
Or(ys4861== 0 , ys4861== 1),
Or(ys4862== 0 , ys4862== 1),
Or(ys4871== 0 , ys4871== 1),
Or(ys4872== 0 , ys4872== 1),
Or(ys4881== 0 , ys4881== 1),
Or(ys4882== 0 , ys4882== 1),
Or(ys4891== 0 , ys4891== 1),
Or(ys4892== 0 , ys4892== 1),
Or(ys4901== 0 , ys4901== 1),
Or(ys4902== 0 , ys4902== 1),
Or(ys4911== 0 , ys4911== 1),
Or(ys4912== 0 , ys4912== 1),
Or(ys4921== 0 , ys4921== 1),
Or(ys4922== 0 , ys4922== 1),
Or(ys4931== 0 , ys4931== 1),
Or(ys4932== 0 , ys4932== 1),
Or(ys4941== 0 , ys4941== 1),
Or(ys4942== 0 , ys4942== 1),
Or(ys4951== 0 , ys4951== 1),
Or(ys4952== 0 , ys4952== 1),
Or(ys4961== 0 , ys4961== 1),
Or(ys4962== 0 , ys4962== 1),
Or(ys4971== 0 , ys4971== 1),
Or(ys4972== 0 , ys4972== 1),
Or(ys4981== 0 , ys4981== 1),
Or(ys4982== 0 , ys4982== 1),
Or(ys4991== 0 , ys4991== 1),
Or(ys4992== 0 , ys4992== 1),
Or(ys5001== 0 , ys5001== 1),
Or(ys5002== 0 , ys5002== 1),
Or(ys5011== 0 , ys5011== 1),
Or(ys5012== 0 , ys5012== 1),
Or(ys5021== 0 , ys5021== 1),
Or(ys5022== 0 , ys5022== 1),
Or(ys5031== 0 , ys5031== 1),
Or(ys5032== 0 , ys5032== 1),
Or(ys5041== 0 , ys5041== 1),
Or(ys5042== 0 , ys5042== 1),
Or(ys5051== 0 , ys5051== 1),
Or(ys5052== 0 , ys5052== 1),
Or(ys5061== 0 , ys5061== 1),
Or(ys5062== 0 , ys5062== 1),
Or(ys5071== 0 , ys5071== 1),
Or(ys5072== 0 , ys5072== 1),
Or(ys5081== 0 , ys5081== 1),
Or(ys5082== 0 , ys5082== 1),
Or(ys5091== 0 , ys5091== 1),
Or(ys5092== 0 , ys5092== 1),
Or(ys5101== 0 , ys5101== 1),
Or(ys5102== 0 , ys5102== 1),
Or(ys5111== 0 , ys5111== 1),
Or(ys5112== 0 , ys5112== 1),
Or(ys5121== 0 , ys5121== 1),
Or(ys5122== 0 , ys5122== 1),
Or(ys5131== 0 , ys5131== 1),
Or(ys5132== 0 , ys5132== 1),
Or(ys5141== 0 , ys5141== 1),
Or(ys5142== 0 , ys5142== 1),
Or(ys5151== 0 , ys5151== 1),
Or(ys5152== 0 , ys5152== 1),
Or(ys5161== 0 , ys5161== 1),
Or(ys5162== 0 , ys5162== 1),
Or(ys5171== 0 , ys5171== 1),
Or(ys5172== 0 , ys5172== 1),
Or(ys5181== 0 , ys5181== 1),
Or(ys5182== 0 , ys5182== 1),
Or(ys5191== 0 , ys5191== 1),
Or(ys5192== 0 , ys5192== 1),
Or(ys5201== 0 , ys5201== 1),
Or(ys5202== 0 , ys5202== 1),
Or(ys5211== 0 , ys5211== 1),
Or(ys5212== 0 , ys5212== 1),
Or(ys5221== 0 , ys5221== 1),
Or(ys5222== 0 , ys5222== 1),
Or(ys5231== 0 , ys5231== 1),
Or(ys5232== 0 , ys5232== 1),
Or(ys5241== 0 , ys5241== 1),
Or(ys5242== 0 , ys5242== 1),
Or(ys5251== 0 , ys5251== 1),
Or(ys5252== 0 , ys5252== 1),
Or(ys5261== 0 , ys5261== 1),
Or(ys5262== 0 , ys5262== 1),
Or(ys5271== 0 , ys5271== 1),
Or(ys5272== 0 , ys5272== 1),
Or(ys5281== 0 , ys5281== 1),
Or(ys5282== 0 , ys5282== 1),
Or(ys5291== 0 , ys5291== 1),
Or(ys5292== 0 , ys5292== 1),
Or(ys5301== 0 , ys5301== 1),
Or(ys5302== 0 , ys5302== 1),
Or(ys5311== 0 , ys5311== 1),
Or(ys5312== 0 , ys5312== 1),
Or(ys5321== 0 , ys5321== 1),
Or(ys5322== 0 , ys5322== 1),
Or(ys5331== 0 , ys5331== 1),
Or(ys5332== 0 , ys5332== 1),
Or(ys5341== 0 , ys5341== 1),
Or(ys5342== 0 , ys5342== 1),
Or(ys5351== 0 , ys5351== 1),
Or(ys5352== 0 , ys5352== 1),
Or(ys5361== 0 , ys5361== 1),
Or(ys5362== 0 , ys5362== 1),
Or(ys5371== 0 , ys5371== 1),
Or(ys5372== 0 , ys5372== 1),
Or(ys5381== 0 , ys5381== 1),
Or(ys5382== 0 , ys5382== 1),
Or(ys5391== 0 , ys5391== 1),
Or(ys5392== 0 , ys5392== 1),
Or(ys5401== 0 , ys5401== 1),
Or(ys5402== 0 , ys5402== 1),
Or(ys5411== 0 , ys5411== 1),
Or(ys5412== 0 , ys5412== 1),
Or(ys5421== 0 , ys5421== 1),
Or(ys5422== 0 , ys5422== 1),
Or(ys5431== 0 , ys5431== 1),
Or(ys5432== 0 , ys5432== 1),
Or(ys5441== 0 , ys5441== 1),
Or(ys5442== 0 , ys5442== 1),
Or(ys5451== 0 , ys5451== 1),
Or(ys5452== 0 , ys5452== 1),
Or(ys5461== 0 , ys5461== 1),
Or(ys5462== 0 , ys5462== 1),
Or(ys5471== 0 , ys5471== 1),
Or(ys5472== 0 , ys5472== 1),
Or(ys5481== 0 , ys5481== 1),
Or(ys5482== 0 , ys5482== 1),
Or(ys5491== 0 , ys5491== 1),
Or(ys5492== 0 , ys5492== 1),
Or(ys5501== 0 , ys5501== 1),
Or(ys5502== 0 , ys5502== 1),
Or(ys5511== 0 , ys5511== 1),
Or(ys5512== 0 , ys5512== 1),
Or(ys5521== 0 , ys5521== 1),
Or(ys5522== 0 , ys5522== 1),
Or(ys5531== 0 , ys5531== 1),
Or(ys5532== 0 , ys5532== 1),
Or(ys5541== 0 , ys5541== 1),
Or(ys5542== 0 , ys5542== 1),
Or(ys5551== 0 , ys5551== 1),
Or(ys5552== 0 , ys5552== 1),
Or(ys5561== 0 , ys5561== 1),
Or(ys5562== 0 , ys5562== 1),
Or(ys5571== 0 , ys5571== 1),
Or(ys5572== 0 , ys5572== 1),
Or(ys5581== 0 , ys5581== 1),
Or(ys5582== 0 , ys5582== 1),
Or(ys5591== 0 , ys5591== 1),
Or(ys5592== 0 , ys5592== 1),
Or(ys5601== 0 , ys5601== 1),
Or(ys5602== 0 , ys5602== 1),
Or(ys5611== 0 , ys5611== 1),
Or(ys5612== 0 , ys5612== 1),
Or(ys5621== 0 , ys5621== 1),
Or(ys5622== 0 , ys5622== 1),
Or(ys5631== 0 , ys5631== 1),
Or(ys5632== 0 , ys5632== 1),
Or(ys5641== 0 , ys5641== 1),
Or(ys5642== 0 , ys5642== 1),
Or(ys5651== 0 , ys5651== 1),
Or(ys5652== 0 , ys5652== 1),
Or(ys5661== 0 , ys5661== 1),
Or(ys5662== 0 , ys5662== 1),
Or(ys5671== 0 , ys5671== 1),
Or(ys5672== 0 , ys5672== 1),
Or(ys5681== 0 , ys5681== 1),
Or(ys5682== 0 , ys5682== 1),
Or(ys5691== 0 , ys5691== 1),
Or(ys5692== 0 , ys5692== 1),
Or(ys5701== 0 , ys5701== 1),
Or(ys5702== 0 , ys5702== 1),
Or(ys5711== 0 , ys5711== 1),
Or(ys5712== 0 , ys5712== 1),
Or(ys5721== 0 , ys5721== 1),
Or(ys5722== 0 , ys5722== 1),
Or(ys5731== 0 , ys5731== 1),
Or(ys5732== 0 , ys5732== 1),
Or(ys5741== 0 , ys5741== 1),
Or(ys5742== 0 , ys5742== 1),
Or(ys5751== 0 , ys5751== 1),
Or(ys5752== 0 , ys5752== 1),
Or(ys5761== 0 , ys5761== 1),
Or(ys5762== 0 , ys5762== 1),
Or(ys5771== 0 , ys5771== 1),
Or(ys5772== 0 , ys5772== 1),
Or(ys5781== 0 , ys5781== 1),
Or(ys5782== 0 , ys5782== 1),
Or(ys5791== 0 , ys5791== 1),
Or(ys5792== 0 , ys5792== 1),
Or(ys5801== 0 , ys5801== 1),
Or(ys5802== 0 , ys5802== 1),
Or(ys5811== 0 , ys5811== 1),
Or(ys5812== 0 , ys5812== 1),
Or(ys5821== 0 , ys5821== 1),
Or(ys5822== 0 , ys5822== 1),
Or(ys5831== 0 , ys5831== 1),
Or(ys5832== 0 , ys5832== 1),
Or(ys5841== 0 , ys5841== 1),
Or(ys5842== 0 , ys5842== 1),
Or(ys5851== 0 , ys5851== 1),
Or(ys5852== 0 , ys5852== 1),
Or(ys5861== 0 , ys5861== 1),
Or(ys5862== 0 , ys5862== 1),
Or(ys5871== 0 , ys5871== 1),
Or(ys5872== 0 , ys5872== 1),
Or(ys5881== 0 , ys5881== 1),
Or(ys5882== 0 , ys5882== 1),
Or(ys5891== 0 , ys5891== 1),
Or(ys5892== 0 , ys5892== 1),
Or(ys5901== 0 , ys5901== 1),
Or(ys5902== 0 , ys5902== 1),
Or(ys5911== 0 , ys5911== 1),
Or(ys5912== 0 , ys5912== 1),
Or(ys5921== 0 , ys5921== 1),
Or(ys5922== 0 , ys5922== 1),
Or(ys5931== 0 , ys5931== 1),
Or(ys5932== 0 , ys5932== 1),
Or(ys5941== 0 , ys5941== 1),
Or(ys5942== 0 , ys5942== 1),
Or(ys5951== 0 , ys5951== 1),
Or(ys5952== 0 , ys5952== 1),
Or(ys5961== 0 , ys5961== 1),
Or(ys5962== 0 , ys5962== 1),
Or(ys5971== 0 , ys5971== 1),
Or(ys5972== 0 , ys5972== 1),
Or(ys5981== 0 , ys5981== 1),
Or(ys5982== 0 , ys5982== 1),
Or(ys5991== 0 , ys5991== 1),
Or(ys5992== 0 , ys5992== 1),
Or(ys6001== 0 , ys6001== 1),
Or(ys6002== 0 , ys6002== 1),
Or(ys6011== 0 , ys6011== 1),
Or(ys6012== 0 , ys6012== 1),
Or(ys6021== 0 , ys6021== 1),
Or(ys6022== 0 , ys6022== 1),
Or(ys6031== 0 , ys6031== 1),
Or(ys6032== 0 , ys6032== 1),
Or(ys6041== 0 , ys6041== 1),
Or(ys6042== 0 , ys6042== 1),
Or(ys6051== 0 , ys6051== 1),
Or(ys6052== 0 , ys6052== 1),
Or(ys6061== 0 , ys6061== 1),
Or(ys6062== 0 , ys6062== 1),
Or(ys6071== 0 , ys6071== 1),
Or(ys6072== 0 , ys6072== 1),
Or(ys6081== 0 , ys6081== 1),
Or(ys6082== 0 , ys6082== 1),
Or(ys6091== 0 , ys6091== 1),
Or(ys6092== 0 , ys6092== 1),
Or(ys6101== 0 , ys6101== 1),
Or(ys6102== 0 , ys6102== 1),
Or(ys6111== 0 , ys6111== 1),
Or(ys6112== 0 , ys6112== 1),
Or(ys6121== 0 , ys6121== 1),
Or(ys6122== 0 , ys6122== 1),
Or(ys6131== 0 , ys6131== 1),
Or(ys6132== 0 , ys6132== 1),
Or(ys6141== 0 , ys6141== 1),
Or(ys6142== 0 , ys6142== 1),
Or(ys6151== 0 , ys6151== 1),
Or(ys6152== 0 , ys6152== 1),
Or(ys6161== 0 , ys6161== 1),
Or(ys6162== 0 , ys6162== 1),
Or(ys6171== 0 , ys6171== 1),
Or(ys6172== 0 , ys6172== 1),
Or(ys6181== 0 , ys6181== 1),
Or(ys6182== 0 , ys6182== 1),
Or(ys6191== 0 , ys6191== 1),
Or(ys6192== 0 , ys6192== 1),
Or(ys6201== 0 , ys6201== 1),
Or(ys6202== 0 , ys6202== 1),
Or(ys6211== 0 , ys6211== 1),
Or(ys6212== 0 , ys6212== 1),
Or(ys6221== 0 , ys6221== 1),
Or(ys6222== 0 , ys6222== 1),
Or(ys6231== 0 , ys6231== 1),
Or(ys6232== 0 , ys6232== 1),
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
ys1881 + ys1882 == 1,
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
ys3761 + ys3762 == 1,
ys3771 + ys3772 == 1,
ys3781 + ys3782 == 1,
ys3791 + ys3792 == 1,
ys3801 + ys3802 == 1,
ys3811 + ys3812 == 1,
ys3821 + ys3822 == 1,
ys3831 + ys3832 == 1,
ys3841 + ys3842 == 1,
ys3851 + ys3852 == 1,
ys3861 + ys3862 == 1,
ys3871 + ys3872 == 1,
ys3881 + ys3882 == 1,
ys3891 + ys3892 == 1,
ys3901 + ys3902 == 1,
ys3911 + ys3912 == 1,
ys3921 + ys3922 == 1,
ys3931 + ys3932 == 1,
ys3941 + ys3942 == 1,
ys3951 + ys3952 == 1,
ys3961 + ys3962 == 1,
ys3971 + ys3972 == 1,
ys3981 + ys3982 == 1,
ys3991 + ys3992 == 1,
ys4001 + ys4002 == 1,
ys4011 + ys4012 == 1,
ys4021 + ys4022 == 1,
ys4031 + ys4032 == 1,
ys4041 + ys4042 == 1,
ys4051 + ys4052 == 1,
ys4061 + ys4062 == 1,
ys4071 + ys4072 == 1,
ys4081 + ys4082 == 1,
ys4091 + ys4092 == 1,
ys4101 + ys4102 == 1,
ys4111 + ys4112 == 1,
ys4121 + ys4122 == 1,
ys4131 + ys4132 == 1,
ys4141 + ys4142 == 1,
ys4151 + ys4152 == 1,
ys4161 + ys4162 == 1,
ys4171 + ys4172 == 1,
ys4181 + ys4182 == 1,
ys4191 + ys4192 == 1,
ys4201 + ys4202 == 1,
ys4211 + ys4212 == 1,
ys4221 + ys4222 == 1,
ys4231 + ys4232 == 1,
ys4241 + ys4242 == 1,
ys4251 + ys4252 == 1,
ys4261 + ys4262 == 1,
ys4271 + ys4272 == 1,
ys4281 + ys4282 == 1,
ys4291 + ys4292 == 1,
ys4301 + ys4302 == 1,
ys4311 + ys4312 == 1,
ys4321 + ys4322 == 1,
ys4331 + ys4332 == 1,
ys4341 + ys4342 == 1,
ys4351 + ys4352 == 1,
ys4361 + ys4362 == 1,
ys4371 + ys4372 == 1,
ys4381 + ys4382 == 1,
ys4391 + ys4392 == 1,
ys4401 + ys4402 == 1,
ys4411 + ys4412 == 1,
ys4421 + ys4422 == 1,
ys4431 + ys4432 == 1,
ys4441 + ys4442 == 1,
ys4451 + ys4452 == 1,
ys4461 + ys4462 == 1,
ys4471 + ys4472 == 1,
ys4481 + ys4482 == 1,
ys4491 + ys4492 == 1,
ys4501 + ys4502 == 1,
ys4511 + ys4512 == 1,
ys4521 + ys4522 == 1,
ys4531 + ys4532 == 1,
ys4541 + ys4542 == 1,
ys4551 + ys4552 == 1,
ys4561 + ys4562 == 1,
ys4571 + ys4572 == 1,
ys4581 + ys4582 == 1,
ys4591 + ys4592 == 1,
ys4601 + ys4602 == 1,
ys4611 + ys4612 == 1,
ys4621 + ys4622 == 1,
ys4631 + ys4632 == 1,
ys4641 + ys4642 == 1,
ys4651 + ys4652 == 1,
ys4661 + ys4662 == 1,
ys4671 + ys4672 == 1,
ys4681 + ys4682 == 1,
ys4691 + ys4692 == 1,
ys4701 + ys4702 == 1,
ys4711 + ys4712 == 1,
ys4721 + ys4722 == 1,
ys4731 + ys4732 == 1,
ys4741 + ys4742 == 1,
ys4751 + ys4752 == 1,
ys4761 + ys4762 == 1,
ys4771 + ys4772 == 1,
ys4781 + ys4782 == 1,
ys4791 + ys4792 == 1,
ys4801 + ys4802 == 1,
ys4811 + ys4812 == 1,
ys4821 + ys4822 == 1,
ys4831 + ys4832 == 1,
ys4841 + ys4842 == 1,
ys4851 + ys4852 == 1,
ys4861 + ys4862 == 1,
ys4871 + ys4872 == 1,
ys4881 + ys4882 == 1,
ys4891 + ys4892 == 1,
ys4901 + ys4902 == 1,
ys4911 + ys4912 == 1,
ys4921 + ys4922 == 1,
ys4931 + ys4932 == 1,
ys4941 + ys4942 == 1,
ys4951 + ys4952 == 1,
ys4961 + ys4962 == 1,
ys4971 + ys4972 == 1,
ys4981 + ys4982 == 1,
ys4991 + ys4992 == 1,
ys5001 + ys5002 == 1,
ys5011 + ys5012 == 1,
ys5021 + ys5022 == 1,
ys5031 + ys5032 == 1,
ys5041 + ys5042 == 1,
ys5051 + ys5052 == 1,
ys5061 + ys5062 == 1,
ys5071 + ys5072 == 1,
ys5081 + ys5082 == 1,
ys5091 + ys5092 == 1,
ys5101 + ys5102 == 1,
ys5111 + ys5112 == 1,
ys5121 + ys5122 == 1,
ys5131 + ys5132 == 1,
ys5141 + ys5142 == 1,
ys5151 + ys5152 == 1,
ys5161 + ys5162 == 1,
ys5171 + ys5172 == 1,
ys5181 + ys5182 == 1,
ys5191 + ys5192 == 1,
ys5201 + ys5202 == 1,
ys5211 + ys5212 == 1,
ys5221 + ys5222 == 1,
ys5231 + ys5232 == 1,
ys5241 + ys5242 == 1,
ys5251 + ys5252 == 1,
ys5261 + ys5262 == 1,
ys5271 + ys5272 == 1,
ys5281 + ys5282 == 1,
ys5291 + ys5292 == 1,
ys5301 + ys5302 == 1,
ys5311 + ys5312 == 1,
ys5321 + ys5322 == 1,
ys5331 + ys5332 == 1,
ys5341 + ys5342 == 1,
ys5351 + ys5352 == 1,
ys5361 + ys5362 == 1,
ys5371 + ys5372 == 1,
ys5381 + ys5382 == 1,
ys5391 + ys5392 == 1,
ys5401 + ys5402 == 1,
ys5411 + ys5412 == 1,
ys5421 + ys5422 == 1,
ys5431 + ys5432 == 1,
ys5441 + ys5442 == 1,
ys5451 + ys5452 == 1,
ys5461 + ys5462 == 1,
ys5471 + ys5472 == 1,
ys5481 + ys5482 == 1,
ys5491 + ys5492 == 1,
ys5501 + ys5502 == 1,
ys5511 + ys5512 == 1,
ys5521 + ys5522 == 1,
ys5531 + ys5532 == 1,
ys5541 + ys5542 == 1,
ys5551 + ys5552 == 1,
ys5561 + ys5562 == 1,
ys5571 + ys5572 == 1,
ys5581 + ys5582 == 1,
ys5591 + ys5592 == 1,
ys5601 + ys5602 == 1,
ys5611 + ys5612 == 1,
ys5621 + ys5622 == 1,
ys5631 + ys5632 == 1,
ys5641 + ys5642 == 1,
ys5651 + ys5652 == 1,
ys5661 + ys5662 == 1,
ys5671 + ys5672 == 1,
ys5681 + ys5682 == 1,
ys5691 + ys5692 == 1,
ys5701 + ys5702 == 1,
ys5711 + ys5712 == 1,
ys5721 + ys5722 == 1,
ys5731 + ys5732 == 1,
ys5741 + ys5742 == 1,
ys5751 + ys5752 == 1,
ys5761 + ys5762 == 1,
ys5771 + ys5772 == 1,
ys5781 + ys5782 == 1,
ys5791 + ys5792 == 1,
ys5801 + ys5802 == 1,
ys5811 + ys5812 == 1,
ys5821 + ys5822 == 1,
ys5831 + ys5832 == 1,
ys5841 + ys5842 == 1,
ys5851 + ys5852 == 1,
ys5861 + ys5862 == 1,
ys5871 + ys5872 == 1,
ys5881 + ys5882 == 1,
ys5891 + ys5892 == 1,
ys5901 + ys5902 == 1,
ys5911 + ys5912 == 1,
ys5921 + ys5922 == 1,
ys5931 + ys5932 == 1,
ys5941 + ys5942 == 1,
ys5951 + ys5952 == 1,
ys5961 + ys5962 == 1,
ys5971 + ys5972 == 1,
ys5981 + ys5982 == 1,
ys5991 + ys5992 == 1,
ys6001 + ys6002 == 1,
ys6011 + ys6012 == 1,
ys6021 + ys6022 == 1,
ys6031 + ys6032 == 1,
ys6041 + ys6042 == 1,
ys6051 + ys6052 == 1,
ys6061 + ys6062 == 1,
ys6071 + ys6072 == 1,
ys6081 + ys6082 == 1,
ys6091 + ys6092 == 1,
ys6101 + ys6102 == 1,
ys6111 + ys6112 == 1,
ys6121 + ys6122 == 1,
ys6131 + ys6132 == 1,
ys6141 + ys6142 == 1,
ys6151 + ys6152 == 1,
ys6161 + ys6162 == 1,
ys6171 + ys6172 == 1,
ys6181 + ys6182 == 1,
ys6191 + ys6192 == 1,
ys6201 + ys6202 == 1,
ys6211 + ys6212 == 1,
ys6221 + ys6222 == 1,
ys6231 + ys6232 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')