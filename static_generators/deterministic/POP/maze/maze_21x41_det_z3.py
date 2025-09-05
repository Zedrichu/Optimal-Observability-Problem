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
ys191 = Real('ys191')
ys192 = Real('ys192')
ys193 = Real('ys193')
ys194 = Real('ys194')
ys201 = Real('ys201')
ys202 = Real('ys202')
ys203 = Real('ys203')
ys204 = Real('ys204')
ys211 = Real('ys211')
ys212 = Real('ys212')
ys213 = Real('ys213')
ys214 = Real('ys214')
ys221 = Real('ys221')
ys222 = Real('ys222')
ys223 = Real('ys223')
ys224 = Real('ys224')
ys231 = Real('ys231')
ys232 = Real('ys232')
ys233 = Real('ys233')
ys234 = Real('ys234')
ys241 = Real('ys241')
ys242 = Real('ys242')
ys243 = Real('ys243')
ys244 = Real('ys244')
ys251 = Real('ys251')
ys252 = Real('ys252')
ys253 = Real('ys253')
ys254 = Real('ys254')
ys261 = Real('ys261')
ys262 = Real('ys262')
ys263 = Real('ys263')
ys264 = Real('ys264')
ys271 = Real('ys271')
ys272 = Real('ys272')
ys273 = Real('ys273')
ys274 = Real('ys274')
ys281 = Real('ys281')
ys282 = Real('ys282')
ys283 = Real('ys283')
ys284 = Real('ys284')
ys291 = Real('ys291')
ys292 = Real('ys292')
ys293 = Real('ys293')
ys294 = Real('ys294')
ys301 = Real('ys301')
ys302 = Real('ys302')
ys303 = Real('ys303')
ys304 = Real('ys304')
ys311 = Real('ys311')
ys312 = Real('ys312')
ys313 = Real('ys313')
ys314 = Real('ys314')
ys321 = Real('ys321')
ys322 = Real('ys322')
ys323 = Real('ys323')
ys324 = Real('ys324')
ys331 = Real('ys331')
ys332 = Real('ys332')
ys333 = Real('ys333')
ys334 = Real('ys334')
ys341 = Real('ys341')
ys342 = Real('ys342')
ys343 = Real('ys343')
ys344 = Real('ys344')
ys351 = Real('ys351')
ys352 = Real('ys352')
ys353 = Real('ys353')
ys354 = Real('ys354')
ys361 = Real('ys361')
ys362 = Real('ys362')
ys363 = Real('ys363')
ys364 = Real('ys364')
ys371 = Real('ys371')
ys372 = Real('ys372')
ys373 = Real('ys373')
ys374 = Real('ys374')
ys381 = Real('ys381')
ys382 = Real('ys382')
ys383 = Real('ys383')
ys384 = Real('ys384')
ys391 = Real('ys391')
ys392 = Real('ys392')
ys393 = Real('ys393')
ys394 = Real('ys394')
ys401 = Real('ys401')
ys402 = Real('ys402')
ys403 = Real('ys403')
ys404 = Real('ys404')
ys411 = Real('ys411')
ys412 = Real('ys412')
ys413 = Real('ys413')
ys414 = Real('ys414')
ys421 = Real('ys421')
ys422 = Real('ys422')
ys423 = Real('ys423')
ys424 = Real('ys424')
ys431 = Real('ys431')
ys432 = Real('ys432')
ys433 = Real('ys433')
ys434 = Real('ys434')
ys441 = Real('ys441')
ys442 = Real('ys442')
ys443 = Real('ys443')
ys444 = Real('ys444')
ys451 = Real('ys451')
ys452 = Real('ys452')
ys453 = Real('ys453')
ys454 = Real('ys454')
ys461 = Real('ys461')
ys462 = Real('ys462')
ys463 = Real('ys463')
ys464 = Real('ys464')
ys471 = Real('ys471')
ys472 = Real('ys472')
ys473 = Real('ys473')
ys474 = Real('ys474')
ys481 = Real('ys481')
ys482 = Real('ys482')
ys483 = Real('ys483')
ys484 = Real('ys484')
ys491 = Real('ys491')
ys492 = Real('ys492')
ys493 = Real('ys493')
ys494 = Real('ys494')
ys501 = Real('ys501')
ys502 = Real('ys502')
ys503 = Real('ys503')
ys504 = Real('ys504')
ys511 = Real('ys511')
ys512 = Real('ys512')
ys513 = Real('ys513')
ys514 = Real('ys514')
ys521 = Real('ys521')
ys522 = Real('ys522')
ys523 = Real('ys523')
ys524 = Real('ys524')
ys531 = Real('ys531')
ys532 = Real('ys532')
ys533 = Real('ys533')
ys534 = Real('ys534')
ys541 = Real('ys541')
ys542 = Real('ys542')
ys543 = Real('ys543')
ys544 = Real('ys544')
ys551 = Real('ys551')
ys552 = Real('ys552')
ys553 = Real('ys553')
ys554 = Real('ys554')
ys561 = Real('ys561')
ys562 = Real('ys562')
ys563 = Real('ys563')
ys564 = Real('ys564')
ys571 = Real('ys571')
ys572 = Real('ys572')
ys573 = Real('ys573')
ys574 = Real('ys574')
ys581 = Real('ys581')
ys582 = Real('ys582')
ys583 = Real('ys583')
ys584 = Real('ys584')
ys591 = Real('ys591')
ys592 = Real('ys592')
ys593 = Real('ys593')
ys594 = Real('ys594')
ys601 = Real('ys601')
ys602 = Real('ys602')
ys603 = Real('ys603')
ys604 = Real('ys604')
ys611 = Real('ys611')
ys612 = Real('ys612')
ys613 = Real('ys613')
ys614 = Real('ys614')
ys621 = Real('ys621')
ys622 = Real('ys622')
ys623 = Real('ys623')
ys624 = Real('ys624')
ys631 = Real('ys631')
ys632 = Real('ys632')
ys633 = Real('ys633')
ys634 = Real('ys634')
ys641 = Real('ys641')
ys642 = Real('ys642')
ys643 = Real('ys643')
ys644 = Real('ys644')
ys651 = Real('ys651')
ys652 = Real('ys652')
ys653 = Real('ys653')
ys654 = Real('ys654')
ys661 = Real('ys661')
ys662 = Real('ys662')
ys663 = Real('ys663')
ys664 = Real('ys664')
ys671 = Real('ys671')
ys672 = Real('ys672')
ys673 = Real('ys673')
ys674 = Real('ys674')
ys681 = Real('ys681')
ys682 = Real('ys682')
ys683 = Real('ys683')
ys684 = Real('ys684')
ys691 = Real('ys691')
ys692 = Real('ys692')
ys693 = Real('ys693')
ys694 = Real('ys694')
ys701 = Real('ys701')
ys702 = Real('ys702')
ys703 = Real('ys703')
ys704 = Real('ys704')
ys711 = Real('ys711')
ys712 = Real('ys712')
ys713 = Real('ys713')
ys714 = Real('ys714')
ys721 = Real('ys721')
ys722 = Real('ys722')
ys723 = Real('ys723')
ys724 = Real('ys724')
ys731 = Real('ys731')
ys732 = Real('ys732')
ys733 = Real('ys733')
ys734 = Real('ys734')
ys741 = Real('ys741')
ys742 = Real('ys742')
ys743 = Real('ys743')
ys744 = Real('ys744')
ys751 = Real('ys751')
ys752 = Real('ys752')
ys753 = Real('ys753')
ys754 = Real('ys754')
ys761 = Real('ys761')
ys762 = Real('ys762')
ys763 = Real('ys763')
ys764 = Real('ys764')
ys771 = Real('ys771')
ys772 = Real('ys772')
ys773 = Real('ys773')
ys774 = Real('ys774')
ys781 = Real('ys781')
ys782 = Real('ys782')
ys783 = Real('ys783')
ys784 = Real('ys784')
ys791 = Real('ys791')
ys792 = Real('ys792')
ys793 = Real('ys793')
ys794 = Real('ys794')
ys801 = Real('ys801')
ys802 = Real('ys802')
ys803 = Real('ys803')
ys804 = Real('ys804')
ys811 = Real('ys811')
ys812 = Real('ys812')
ys813 = Real('ys813')
ys814 = Real('ys814')
ys821 = Real('ys821')
ys822 = Real('ys822')
ys823 = Real('ys823')
ys824 = Real('ys824')
ys831 = Real('ys831')
ys832 = Real('ys832')
ys833 = Real('ys833')
ys834 = Real('ys834')
ys841 = Real('ys841')
ys842 = Real('ys842')
ys843 = Real('ys843')
ys844 = Real('ys844')
ys851 = Real('ys851')
ys852 = Real('ys852')
ys853 = Real('ys853')
ys854 = Real('ys854')
ys861 = Real('ys861')
ys862 = Real('ys862')
ys863 = Real('ys863')
ys864 = Real('ys864')
ys871 = Real('ys871')
ys872 = Real('ys872')
ys873 = Real('ys873')
ys874 = Real('ys874')
ys881 = Real('ys881')
ys882 = Real('ys882')
ys883 = Real('ys883')
ys884 = Real('ys884')
ys891 = Real('ys891')
ys892 = Real('ys892')
ys893 = Real('ys893')
ys894 = Real('ys894')
ys901 = Real('ys901')
ys902 = Real('ys902')
ys903 = Real('ys903')
ys904 = Real('ys904')
ys911 = Real('ys911')
ys912 = Real('ys912')
ys913 = Real('ys913')
ys914 = Real('ys914')
ys921 = Real('ys921')
ys922 = Real('ys922')
ys923 = Real('ys923')
ys924 = Real('ys924')
ys931 = Real('ys931')
ys932 = Real('ys932')
ys933 = Real('ys933')
ys934 = Real('ys934')
ys941 = Real('ys941')
ys942 = Real('ys942')
ys943 = Real('ys943')
ys944 = Real('ys944')
ys951 = Real('ys951')
ys952 = Real('ys952')
ys953 = Real('ys953')
ys954 = Real('ys954')
ys961 = Real('ys961')
ys962 = Real('ys962')
ys963 = Real('ys963')
ys964 = Real('ys964')
ys971 = Real('ys971')
ys972 = Real('ys972')
ys973 = Real('ys973')
ys974 = Real('ys974')
ys981 = Real('ys981')
ys982 = Real('ys982')
ys983 = Real('ys983')
ys984 = Real('ys984')
ys1001 = Real('ys1001')
ys1002 = Real('ys1002')
ys1003 = Real('ys1003')
ys1004 = Real('ys1004')

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
pi0>=40, pi1>=39, pi2>=38, pi3>=37, pi4>=36, pi5>=35, pi6>=34, pi7>=33, pi8>=32, pi9>=31, pi10>=30, pi11>=29, pi12>=28, pi13>=27, pi14>=26, pi15>=25, pi16>=24, pi17>=23, pi18>=22, pi19>=21, pi20>=20, pi21>=21, pi22>=22, pi23>=23, pi24>=24, pi25>=25, pi26>=26, pi27>=27, pi28>=28, pi29>=29, pi30>=30, pi31>=31, pi32>=32, pi33>=33, pi34>=34, pi35>=35, pi36>=36, pi37>=37, pi38>=38, pi39>=39, pi40>=40, pi41>=41, pi42>=19, pi43>=41, pi44>=42, pi45>=18, pi46>=42, pi47>=43, pi48>=17, pi49>=43, pi50>=44, pi51>=16, pi52>=44, pi53>=45, pi54>=15, pi55>=45, pi56>=46, pi57>=14, pi58>=46, pi59>=47, pi60>=13, pi61>=47, pi62>=48, pi63>=12, pi64>=48, pi65>=49, pi66>=11, pi67>=49, pi68>=50, pi69>=10, pi70>=50, pi71>=51, pi72>=9, pi73>=51, pi74>=52, pi75>=8, pi76>=52, pi77>=53, pi78>=7, pi79>=53, pi80>=54, pi81>=6, pi82>=54, pi83>=55, pi84>=5, pi85>=55, pi86>=56, pi87>=4, pi88>=56, pi89>=57, pi90>=3, pi91>=57, pi92>=58, pi93>=2, pi94>=58, pi95>=59, pi96>=1, pi97>=59, pi98>=60, pi99>=0, pi100>=60, 
# Expected cost/reward equations
pi0 == (ys01*xo1l + ys02*xo2l + ys03*xo3l + ys04*xo4l) * (1 + pi0) + (ys01*xo1r + ys02*xo2r + ys03*xo3r + ys04*xo4r) * (1 + pi1) + (ys01*xo1u + ys02*xo2u + ys03*xo3u + ys04*xo4u) * (1 + pi0) + (ys01*xo1d + ys02*xo2d + ys03*xo3d + ys04*xo4d) * (1 + pi41),
pi1 == (ys11*xo1l + ys12*xo2l + ys13*xo3l + ys14*xo4l) * (1 + pi0) + (ys11*xo1r + ys12*xo2r + ys13*xo3r + ys14*xo4r) * (1 + pi2) + (ys11*xo1u + ys12*xo2u + ys13*xo3u + ys14*xo4u) * (1 + pi1) + (ys11*xo1d + ys12*xo2d + ys13*xo3d + ys14*xo4d) * (1 + pi1),
pi2 == (ys21*xo1l + ys22*xo2l + ys23*xo3l + ys24*xo4l) * (1 + pi1) + (ys21*xo1r + ys22*xo2r + ys23*xo3r + ys24*xo4r) * (1 + pi3) + (ys21*xo1u + ys22*xo2u + ys23*xo3u + ys24*xo4u) * (1 + pi2) + (ys21*xo1d + ys22*xo2d + ys23*xo3d + ys24*xo4d) * (1 + pi2),
pi3 == (ys31*xo1l + ys32*xo2l + ys33*xo3l + ys34*xo4l) * (1 + pi2) + (ys31*xo1r + ys32*xo2r + ys33*xo3r + ys34*xo4r) * (1 + pi4) + (ys31*xo1u + ys32*xo2u + ys33*xo3u + ys34*xo4u) * (1 + pi3) + (ys31*xo1d + ys32*xo2d + ys33*xo3d + ys34*xo4d) * (1 + pi3),
pi4 == (ys41*xo1l + ys42*xo2l + ys43*xo3l + ys44*xo4l) * (1 + pi3) + (ys41*xo1r + ys42*xo2r + ys43*xo3r + ys44*xo4r) * (1 + pi5) + (ys41*xo1u + ys42*xo2u + ys43*xo3u + ys44*xo4u) * (1 + pi4) + (ys41*xo1d + ys42*xo2d + ys43*xo3d + ys44*xo4d) * (1 + pi4),
pi5 == (ys51*xo1l + ys52*xo2l + ys53*xo3l + ys54*xo4l) * (1 + pi4) + (ys51*xo1r + ys52*xo2r + ys53*xo3r + ys54*xo4r) * (1 + pi6) + (ys51*xo1u + ys52*xo2u + ys53*xo3u + ys54*xo4u) * (1 + pi5) + (ys51*xo1d + ys52*xo2d + ys53*xo3d + ys54*xo4d) * (1 + pi5),
pi6 == (ys61*xo1l + ys62*xo2l + ys63*xo3l + ys64*xo4l) * (1 + pi5) + (ys61*xo1r + ys62*xo2r + ys63*xo3r + ys64*xo4r) * (1 + pi7) + (ys61*xo1u + ys62*xo2u + ys63*xo3u + ys64*xo4u) * (1 + pi6) + (ys61*xo1d + ys62*xo2d + ys63*xo3d + ys64*xo4d) * (1 + pi6),
pi7 == (ys71*xo1l + ys72*xo2l + ys73*xo3l + ys74*xo4l) * (1 + pi6) + (ys71*xo1r + ys72*xo2r + ys73*xo3r + ys74*xo4r) * (1 + pi8) + (ys71*xo1u + ys72*xo2u + ys73*xo3u + ys74*xo4u) * (1 + pi7) + (ys71*xo1d + ys72*xo2d + ys73*xo3d + ys74*xo4d) * (1 + pi7),
pi8 == (ys81*xo1l + ys82*xo2l + ys83*xo3l + ys84*xo4l) * (1 + pi7) + (ys81*xo1r + ys82*xo2r + ys83*xo3r + ys84*xo4r) * (1 + pi9) + (ys81*xo1u + ys82*xo2u + ys83*xo3u + ys84*xo4u) * (1 + pi8) + (ys81*xo1d + ys82*xo2d + ys83*xo3d + ys84*xo4d) * (1 + pi8),
pi9 == (ys91*xo1l + ys92*xo2l + ys93*xo3l + ys94*xo4l) * (1 + pi8) + (ys91*xo1r + ys92*xo2r + ys93*xo3r + ys94*xo4r) * (1 + pi10) + (ys91*xo1u + ys92*xo2u + ys93*xo3u + ys94*xo4u) * (1 + pi9) + (ys91*xo1d + ys92*xo2d + ys93*xo3d + ys94*xo4d) * (1 + pi9),
pi10 == (ys101*xo1l + ys102*xo2l + ys103*xo3l + ys104*xo4l) * (1 + pi9) + (ys101*xo1r + ys102*xo2r + ys103*xo3r + ys104*xo4r) * (1 + pi11) + (ys101*xo1u + ys102*xo2u + ys103*xo3u + ys104*xo4u) * (1 + pi10) + (ys101*xo1d + ys102*xo2d + ys103*xo3d + ys104*xo4d) * (1 + pi10),
pi11 == (ys111*xo1l + ys112*xo2l + ys113*xo3l + ys114*xo4l) * (1 + pi10) + (ys111*xo1r + ys112*xo2r + ys113*xo3r + ys114*xo4r) * (1 + pi12) + (ys111*xo1u + ys112*xo2u + ys113*xo3u + ys114*xo4u) * (1 + pi11) + (ys111*xo1d + ys112*xo2d + ys113*xo3d + ys114*xo4d) * (1 + pi11),
pi12 == (ys121*xo1l + ys122*xo2l + ys123*xo3l + ys124*xo4l) * (1 + pi11) + (ys121*xo1r + ys122*xo2r + ys123*xo3r + ys124*xo4r) * (1 + pi13) + (ys121*xo1u + ys122*xo2u + ys123*xo3u + ys124*xo4u) * (1 + pi12) + (ys121*xo1d + ys122*xo2d + ys123*xo3d + ys124*xo4d) * (1 + pi12),
pi13 == (ys131*xo1l + ys132*xo2l + ys133*xo3l + ys134*xo4l) * (1 + pi12) + (ys131*xo1r + ys132*xo2r + ys133*xo3r + ys134*xo4r) * (1 + pi14) + (ys131*xo1u + ys132*xo2u + ys133*xo3u + ys134*xo4u) * (1 + pi13) + (ys131*xo1d + ys132*xo2d + ys133*xo3d + ys134*xo4d) * (1 + pi13),
pi14 == (ys141*xo1l + ys142*xo2l + ys143*xo3l + ys144*xo4l) * (1 + pi13) + (ys141*xo1r + ys142*xo2r + ys143*xo3r + ys144*xo4r) * (1 + pi15) + (ys141*xo1u + ys142*xo2u + ys143*xo3u + ys144*xo4u) * (1 + pi14) + (ys141*xo1d + ys142*xo2d + ys143*xo3d + ys144*xo4d) * (1 + pi14),
pi15 == (ys151*xo1l + ys152*xo2l + ys153*xo3l + ys154*xo4l) * (1 + pi14) + (ys151*xo1r + ys152*xo2r + ys153*xo3r + ys154*xo4r) * (1 + pi16) + (ys151*xo1u + ys152*xo2u + ys153*xo3u + ys154*xo4u) * (1 + pi15) + (ys151*xo1d + ys152*xo2d + ys153*xo3d + ys154*xo4d) * (1 + pi15),
pi16 == (ys161*xo1l + ys162*xo2l + ys163*xo3l + ys164*xo4l) * (1 + pi15) + (ys161*xo1r + ys162*xo2r + ys163*xo3r + ys164*xo4r) * (1 + pi17) + (ys161*xo1u + ys162*xo2u + ys163*xo3u + ys164*xo4u) * (1 + pi16) + (ys161*xo1d + ys162*xo2d + ys163*xo3d + ys164*xo4d) * (1 + pi16),
pi17 == (ys171*xo1l + ys172*xo2l + ys173*xo3l + ys174*xo4l) * (1 + pi16) + (ys171*xo1r + ys172*xo2r + ys173*xo3r + ys174*xo4r) * (1 + pi18) + (ys171*xo1u + ys172*xo2u + ys173*xo3u + ys174*xo4u) * (1 + pi17) + (ys171*xo1d + ys172*xo2d + ys173*xo3d + ys174*xo4d) * (1 + pi17),
pi18 == (ys181*xo1l + ys182*xo2l + ys183*xo3l + ys184*xo4l) * (1 + pi17) + (ys181*xo1r + ys182*xo2r + ys183*xo3r + ys184*xo4r) * (1 + pi19) + (ys181*xo1u + ys182*xo2u + ys183*xo3u + ys184*xo4u) * (1 + pi18) + (ys181*xo1d + ys182*xo2d + ys183*xo3d + ys184*xo4d) * (1 + pi18),
pi19 == (ys191*xo1l + ys192*xo2l + ys193*xo3l + ys194*xo4l) * (1 + pi18) + (ys191*xo1r + ys192*xo2r + ys193*xo3r + ys194*xo4r) * (1 + pi20) + (ys191*xo1u + ys192*xo2u + ys193*xo3u + ys194*xo4u) * (1 + pi19) + (ys191*xo1d + ys192*xo2d + ys193*xo3d + ys194*xo4d) * (1 + pi19),
pi20 == (ys201*xo1l + ys202*xo2l + ys203*xo3l + ys204*xo4l) * (1 + pi19) + (ys201*xo1r + ys202*xo2r + ys203*xo3r + ys204*xo4r) * (1 + pi21) + (ys201*xo1u + ys202*xo2u + ys203*xo3u + ys204*xo4u) * (1 + pi20) + (ys201*xo1d + ys202*xo2d + ys203*xo3d + ys204*xo4d) * (1 + pi42),
pi21 == (ys211*xo1l + ys212*xo2l + ys213*xo3l + ys214*xo4l) * (1 + pi20) + (ys211*xo1r + ys212*xo2r + ys213*xo3r + ys214*xo4r) * (1 + pi22) + (ys211*xo1u + ys212*xo2u + ys213*xo3u + ys214*xo4u) * (1 + pi21) + (ys211*xo1d + ys212*xo2d + ys213*xo3d + ys214*xo4d) * (1 + pi21),
pi22 == (ys221*xo1l + ys222*xo2l + ys223*xo3l + ys224*xo4l) * (1 + pi21) + (ys221*xo1r + ys222*xo2r + ys223*xo3r + ys224*xo4r) * (1 + pi23) + (ys221*xo1u + ys222*xo2u + ys223*xo3u + ys224*xo4u) * (1 + pi22) + (ys221*xo1d + ys222*xo2d + ys223*xo3d + ys224*xo4d) * (1 + pi22),
pi23 == (ys231*xo1l + ys232*xo2l + ys233*xo3l + ys234*xo4l) * (1 + pi22) + (ys231*xo1r + ys232*xo2r + ys233*xo3r + ys234*xo4r) * (1 + pi24) + (ys231*xo1u + ys232*xo2u + ys233*xo3u + ys234*xo4u) * (1 + pi23) + (ys231*xo1d + ys232*xo2d + ys233*xo3d + ys234*xo4d) * (1 + pi23),
pi24 == (ys241*xo1l + ys242*xo2l + ys243*xo3l + ys244*xo4l) * (1 + pi23) + (ys241*xo1r + ys242*xo2r + ys243*xo3r + ys244*xo4r) * (1 + pi25) + (ys241*xo1u + ys242*xo2u + ys243*xo3u + ys244*xo4u) * (1 + pi24) + (ys241*xo1d + ys242*xo2d + ys243*xo3d + ys244*xo4d) * (1 + pi24),
pi25 == (ys251*xo1l + ys252*xo2l + ys253*xo3l + ys254*xo4l) * (1 + pi24) + (ys251*xo1r + ys252*xo2r + ys253*xo3r + ys254*xo4r) * (1 + pi26) + (ys251*xo1u + ys252*xo2u + ys253*xo3u + ys254*xo4u) * (1 + pi25) + (ys251*xo1d + ys252*xo2d + ys253*xo3d + ys254*xo4d) * (1 + pi25),
pi26 == (ys261*xo1l + ys262*xo2l + ys263*xo3l + ys264*xo4l) * (1 + pi25) + (ys261*xo1r + ys262*xo2r + ys263*xo3r + ys264*xo4r) * (1 + pi27) + (ys261*xo1u + ys262*xo2u + ys263*xo3u + ys264*xo4u) * (1 + pi26) + (ys261*xo1d + ys262*xo2d + ys263*xo3d + ys264*xo4d) * (1 + pi26),
pi27 == (ys271*xo1l + ys272*xo2l + ys273*xo3l + ys274*xo4l) * (1 + pi26) + (ys271*xo1r + ys272*xo2r + ys273*xo3r + ys274*xo4r) * (1 + pi28) + (ys271*xo1u + ys272*xo2u + ys273*xo3u + ys274*xo4u) * (1 + pi27) + (ys271*xo1d + ys272*xo2d + ys273*xo3d + ys274*xo4d) * (1 + pi27),
pi28 == (ys281*xo1l + ys282*xo2l + ys283*xo3l + ys284*xo4l) * (1 + pi27) + (ys281*xo1r + ys282*xo2r + ys283*xo3r + ys284*xo4r) * (1 + pi29) + (ys281*xo1u + ys282*xo2u + ys283*xo3u + ys284*xo4u) * (1 + pi28) + (ys281*xo1d + ys282*xo2d + ys283*xo3d + ys284*xo4d) * (1 + pi28),
pi29 == (ys291*xo1l + ys292*xo2l + ys293*xo3l + ys294*xo4l) * (1 + pi28) + (ys291*xo1r + ys292*xo2r + ys293*xo3r + ys294*xo4r) * (1 + pi30) + (ys291*xo1u + ys292*xo2u + ys293*xo3u + ys294*xo4u) * (1 + pi29) + (ys291*xo1d + ys292*xo2d + ys293*xo3d + ys294*xo4d) * (1 + pi29),
pi30 == (ys301*xo1l + ys302*xo2l + ys303*xo3l + ys304*xo4l) * (1 + pi29) + (ys301*xo1r + ys302*xo2r + ys303*xo3r + ys304*xo4r) * (1 + pi31) + (ys301*xo1u + ys302*xo2u + ys303*xo3u + ys304*xo4u) * (1 + pi30) + (ys301*xo1d + ys302*xo2d + ys303*xo3d + ys304*xo4d) * (1 + pi30),
pi31 == (ys311*xo1l + ys312*xo2l + ys313*xo3l + ys314*xo4l) * (1 + pi30) + (ys311*xo1r + ys312*xo2r + ys313*xo3r + ys314*xo4r) * (1 + pi32) + (ys311*xo1u + ys312*xo2u + ys313*xo3u + ys314*xo4u) * (1 + pi31) + (ys311*xo1d + ys312*xo2d + ys313*xo3d + ys314*xo4d) * (1 + pi31),
pi32 == (ys321*xo1l + ys322*xo2l + ys323*xo3l + ys324*xo4l) * (1 + pi31) + (ys321*xo1r + ys322*xo2r + ys323*xo3r + ys324*xo4r) * (1 + pi33) + (ys321*xo1u + ys322*xo2u + ys323*xo3u + ys324*xo4u) * (1 + pi32) + (ys321*xo1d + ys322*xo2d + ys323*xo3d + ys324*xo4d) * (1 + pi32),
pi33 == (ys331*xo1l + ys332*xo2l + ys333*xo3l + ys334*xo4l) * (1 + pi32) + (ys331*xo1r + ys332*xo2r + ys333*xo3r + ys334*xo4r) * (1 + pi34) + (ys331*xo1u + ys332*xo2u + ys333*xo3u + ys334*xo4u) * (1 + pi33) + (ys331*xo1d + ys332*xo2d + ys333*xo3d + ys334*xo4d) * (1 + pi33),
pi34 == (ys341*xo1l + ys342*xo2l + ys343*xo3l + ys344*xo4l) * (1 + pi33) + (ys341*xo1r + ys342*xo2r + ys343*xo3r + ys344*xo4r) * (1 + pi35) + (ys341*xo1u + ys342*xo2u + ys343*xo3u + ys344*xo4u) * (1 + pi34) + (ys341*xo1d + ys342*xo2d + ys343*xo3d + ys344*xo4d) * (1 + pi34),
pi35 == (ys351*xo1l + ys352*xo2l + ys353*xo3l + ys354*xo4l) * (1 + pi34) + (ys351*xo1r + ys352*xo2r + ys353*xo3r + ys354*xo4r) * (1 + pi36) + (ys351*xo1u + ys352*xo2u + ys353*xo3u + ys354*xo4u) * (1 + pi35) + (ys351*xo1d + ys352*xo2d + ys353*xo3d + ys354*xo4d) * (1 + pi35),
pi36 == (ys361*xo1l + ys362*xo2l + ys363*xo3l + ys364*xo4l) * (1 + pi35) + (ys361*xo1r + ys362*xo2r + ys363*xo3r + ys364*xo4r) * (1 + pi37) + (ys361*xo1u + ys362*xo2u + ys363*xo3u + ys364*xo4u) * (1 + pi36) + (ys361*xo1d + ys362*xo2d + ys363*xo3d + ys364*xo4d) * (1 + pi36),
pi37 == (ys371*xo1l + ys372*xo2l + ys373*xo3l + ys374*xo4l) * (1 + pi36) + (ys371*xo1r + ys372*xo2r + ys373*xo3r + ys374*xo4r) * (1 + pi38) + (ys371*xo1u + ys372*xo2u + ys373*xo3u + ys374*xo4u) * (1 + pi37) + (ys371*xo1d + ys372*xo2d + ys373*xo3d + ys374*xo4d) * (1 + pi37),
pi38 == (ys381*xo1l + ys382*xo2l + ys383*xo3l + ys384*xo4l) * (1 + pi37) + (ys381*xo1r + ys382*xo2r + ys383*xo3r + ys384*xo4r) * (1 + pi39) + (ys381*xo1u + ys382*xo2u + ys383*xo3u + ys384*xo4u) * (1 + pi38) + (ys381*xo1d + ys382*xo2d + ys383*xo3d + ys384*xo4d) * (1 + pi38),
pi39 == (ys391*xo1l + ys392*xo2l + ys393*xo3l + ys394*xo4l) * (1 + pi38) + (ys391*xo1r + ys392*xo2r + ys393*xo3r + ys394*xo4r) * (1 + pi40) + (ys391*xo1u + ys392*xo2u + ys393*xo3u + ys394*xo4u) * (1 + pi39) + (ys391*xo1d + ys392*xo2d + ys393*xo3d + ys394*xo4d) * (1 + pi39),
pi40 == (ys401*xo1l + ys402*xo2l + ys403*xo3l + ys404*xo4l) * (1 + pi39) + (ys401*xo1r + ys402*xo2r + ys403*xo3r + ys404*xo4r) * (1 + pi40) + (ys401*xo1u + ys402*xo2u + ys403*xo3u + ys404*xo4u) * (1 + pi40) + (ys401*xo1d + ys402*xo2d + ys403*xo3d + ys404*xo4d) * (1 + pi43),
pi41 == (ys411*xo1l + ys412*xo2l + ys413*xo3l + ys414*xo4l) * (1 + pi41) + (ys411*xo1r + ys412*xo2r + ys413*xo3r + ys414*xo4r) * (1 + pi41) + (ys411*xo1u + ys412*xo2u + ys413*xo3u + ys414*xo4u) * (1 + pi0) + (ys411*xo1d + ys412*xo2d + ys413*xo3d + ys414*xo4d) * (1 + pi44),
pi42 == (ys421*xo1l + ys422*xo2l + ys423*xo3l + ys424*xo4l) * (1 + pi42) + (ys421*xo1r + ys422*xo2r + ys423*xo3r + ys424*xo4r) * (1 + pi42) + (ys421*xo1u + ys422*xo2u + ys423*xo3u + ys424*xo4u) * (1 + pi20) + (ys421*xo1d + ys422*xo2d + ys423*xo3d + ys424*xo4d) * (1 + pi45),
pi43 == (ys431*xo1l + ys432*xo2l + ys433*xo3l + ys434*xo4l) * (1 + pi43) + (ys431*xo1r + ys432*xo2r + ys433*xo3r + ys434*xo4r) * (1 + pi43) + (ys431*xo1u + ys432*xo2u + ys433*xo3u + ys434*xo4u) * (1 + pi40) + (ys431*xo1d + ys432*xo2d + ys433*xo3d + ys434*xo4d) * (1 + pi46),
pi44 == (ys441*xo1l + ys442*xo2l + ys443*xo3l + ys444*xo4l) * (1 + pi44) + (ys441*xo1r + ys442*xo2r + ys443*xo3r + ys444*xo4r) * (1 + pi44) + (ys441*xo1u + ys442*xo2u + ys443*xo3u + ys444*xo4u) * (1 + pi41) + (ys441*xo1d + ys442*xo2d + ys443*xo3d + ys444*xo4d) * (1 + pi47),
pi45 == (ys451*xo1l + ys452*xo2l + ys453*xo3l + ys454*xo4l) * (1 + pi45) + (ys451*xo1r + ys452*xo2r + ys453*xo3r + ys454*xo4r) * (1 + pi45) + (ys451*xo1u + ys452*xo2u + ys453*xo3u + ys454*xo4u) * (1 + pi42) + (ys451*xo1d + ys452*xo2d + ys453*xo3d + ys454*xo4d) * (1 + pi48),
pi46 == (ys461*xo1l + ys462*xo2l + ys463*xo3l + ys464*xo4l) * (1 + pi46) + (ys461*xo1r + ys462*xo2r + ys463*xo3r + ys464*xo4r) * (1 + pi46) + (ys461*xo1u + ys462*xo2u + ys463*xo3u + ys464*xo4u) * (1 + pi43) + (ys461*xo1d + ys462*xo2d + ys463*xo3d + ys464*xo4d) * (1 + pi49),
pi47 == (ys471*xo1l + ys472*xo2l + ys473*xo3l + ys474*xo4l) * (1 + pi47) + (ys471*xo1r + ys472*xo2r + ys473*xo3r + ys474*xo4r) * (1 + pi47) + (ys471*xo1u + ys472*xo2u + ys473*xo3u + ys474*xo4u) * (1 + pi44) + (ys471*xo1d + ys472*xo2d + ys473*xo3d + ys474*xo4d) * (1 + pi50),
pi48 == (ys481*xo1l + ys482*xo2l + ys483*xo3l + ys484*xo4l) * (1 + pi48) + (ys481*xo1r + ys482*xo2r + ys483*xo3r + ys484*xo4r) * (1 + pi48) + (ys481*xo1u + ys482*xo2u + ys483*xo3u + ys484*xo4u) * (1 + pi45) + (ys481*xo1d + ys482*xo2d + ys483*xo3d + ys484*xo4d) * (1 + pi51),
pi49 == (ys491*xo1l + ys492*xo2l + ys493*xo3l + ys494*xo4l) * (1 + pi49) + (ys491*xo1r + ys492*xo2r + ys493*xo3r + ys494*xo4r) * (1 + pi49) + (ys491*xo1u + ys492*xo2u + ys493*xo3u + ys494*xo4u) * (1 + pi46) + (ys491*xo1d + ys492*xo2d + ys493*xo3d + ys494*xo4d) * (1 + pi52),
pi50 == (ys501*xo1l + ys502*xo2l + ys503*xo3l + ys504*xo4l) * (1 + pi50) + (ys501*xo1r + ys502*xo2r + ys503*xo3r + ys504*xo4r) * (1 + pi50) + (ys501*xo1u + ys502*xo2u + ys503*xo3u + ys504*xo4u) * (1 + pi47) + (ys501*xo1d + ys502*xo2d + ys503*xo3d + ys504*xo4d) * (1 + pi53),
pi51 == (ys511*xo1l + ys512*xo2l + ys513*xo3l + ys514*xo4l) * (1 + pi51) + (ys511*xo1r + ys512*xo2r + ys513*xo3r + ys514*xo4r) * (1 + pi51) + (ys511*xo1u + ys512*xo2u + ys513*xo3u + ys514*xo4u) * (1 + pi48) + (ys511*xo1d + ys512*xo2d + ys513*xo3d + ys514*xo4d) * (1 + pi54),
pi52 == (ys521*xo1l + ys522*xo2l + ys523*xo3l + ys524*xo4l) * (1 + pi52) + (ys521*xo1r + ys522*xo2r + ys523*xo3r + ys524*xo4r) * (1 + pi52) + (ys521*xo1u + ys522*xo2u + ys523*xo3u + ys524*xo4u) * (1 + pi49) + (ys521*xo1d + ys522*xo2d + ys523*xo3d + ys524*xo4d) * (1 + pi55),
pi53 == (ys531*xo1l + ys532*xo2l + ys533*xo3l + ys534*xo4l) * (1 + pi53) + (ys531*xo1r + ys532*xo2r + ys533*xo3r + ys534*xo4r) * (1 + pi53) + (ys531*xo1u + ys532*xo2u + ys533*xo3u + ys534*xo4u) * (1 + pi50) + (ys531*xo1d + ys532*xo2d + ys533*xo3d + ys534*xo4d) * (1 + pi56),
pi54 == (ys541*xo1l + ys542*xo2l + ys543*xo3l + ys544*xo4l) * (1 + pi54) + (ys541*xo1r + ys542*xo2r + ys543*xo3r + ys544*xo4r) * (1 + pi54) + (ys541*xo1u + ys542*xo2u + ys543*xo3u + ys544*xo4u) * (1 + pi51) + (ys541*xo1d + ys542*xo2d + ys543*xo3d + ys544*xo4d) * (1 + pi57),
pi55 == (ys551*xo1l + ys552*xo2l + ys553*xo3l + ys554*xo4l) * (1 + pi55) + (ys551*xo1r + ys552*xo2r + ys553*xo3r + ys554*xo4r) * (1 + pi55) + (ys551*xo1u + ys552*xo2u + ys553*xo3u + ys554*xo4u) * (1 + pi52) + (ys551*xo1d + ys552*xo2d + ys553*xo3d + ys554*xo4d) * (1 + pi58),
pi56 == (ys561*xo1l + ys562*xo2l + ys563*xo3l + ys564*xo4l) * (1 + pi56) + (ys561*xo1r + ys562*xo2r + ys563*xo3r + ys564*xo4r) * (1 + pi56) + (ys561*xo1u + ys562*xo2u + ys563*xo3u + ys564*xo4u) * (1 + pi53) + (ys561*xo1d + ys562*xo2d + ys563*xo3d + ys564*xo4d) * (1 + pi59),
pi57 == (ys571*xo1l + ys572*xo2l + ys573*xo3l + ys574*xo4l) * (1 + pi57) + (ys571*xo1r + ys572*xo2r + ys573*xo3r + ys574*xo4r) * (1 + pi57) + (ys571*xo1u + ys572*xo2u + ys573*xo3u + ys574*xo4u) * (1 + pi54) + (ys571*xo1d + ys572*xo2d + ys573*xo3d + ys574*xo4d) * (1 + pi60),
pi58 == (ys581*xo1l + ys582*xo2l + ys583*xo3l + ys584*xo4l) * (1 + pi58) + (ys581*xo1r + ys582*xo2r + ys583*xo3r + ys584*xo4r) * (1 + pi58) + (ys581*xo1u + ys582*xo2u + ys583*xo3u + ys584*xo4u) * (1 + pi55) + (ys581*xo1d + ys582*xo2d + ys583*xo3d + ys584*xo4d) * (1 + pi61),
pi59 == (ys591*xo1l + ys592*xo2l + ys593*xo3l + ys594*xo4l) * (1 + pi59) + (ys591*xo1r + ys592*xo2r + ys593*xo3r + ys594*xo4r) * (1 + pi59) + (ys591*xo1u + ys592*xo2u + ys593*xo3u + ys594*xo4u) * (1 + pi56) + (ys591*xo1d + ys592*xo2d + ys593*xo3d + ys594*xo4d) * (1 + pi62),
pi60 == (ys601*xo1l + ys602*xo2l + ys603*xo3l + ys604*xo4l) * (1 + pi60) + (ys601*xo1r + ys602*xo2r + ys603*xo3r + ys604*xo4r) * (1 + pi60) + (ys601*xo1u + ys602*xo2u + ys603*xo3u + ys604*xo4u) * (1 + pi57) + (ys601*xo1d + ys602*xo2d + ys603*xo3d + ys604*xo4d) * (1 + pi63),
pi61 == (ys611*xo1l + ys612*xo2l + ys613*xo3l + ys614*xo4l) * (1 + pi61) + (ys611*xo1r + ys612*xo2r + ys613*xo3r + ys614*xo4r) * (1 + pi61) + (ys611*xo1u + ys612*xo2u + ys613*xo3u + ys614*xo4u) * (1 + pi58) + (ys611*xo1d + ys612*xo2d + ys613*xo3d + ys614*xo4d) * (1 + pi64),
pi62 == (ys621*xo1l + ys622*xo2l + ys623*xo3l + ys624*xo4l) * (1 + pi62) + (ys621*xo1r + ys622*xo2r + ys623*xo3r + ys624*xo4r) * (1 + pi62) + (ys621*xo1u + ys622*xo2u + ys623*xo3u + ys624*xo4u) * (1 + pi59) + (ys621*xo1d + ys622*xo2d + ys623*xo3d + ys624*xo4d) * (1 + pi65),
pi63 == (ys631*xo1l + ys632*xo2l + ys633*xo3l + ys634*xo4l) * (1 + pi63) + (ys631*xo1r + ys632*xo2r + ys633*xo3r + ys634*xo4r) * (1 + pi63) + (ys631*xo1u + ys632*xo2u + ys633*xo3u + ys634*xo4u) * (1 + pi60) + (ys631*xo1d + ys632*xo2d + ys633*xo3d + ys634*xo4d) * (1 + pi66),
pi64 == (ys641*xo1l + ys642*xo2l + ys643*xo3l + ys644*xo4l) * (1 + pi64) + (ys641*xo1r + ys642*xo2r + ys643*xo3r + ys644*xo4r) * (1 + pi64) + (ys641*xo1u + ys642*xo2u + ys643*xo3u + ys644*xo4u) * (1 + pi61) + (ys641*xo1d + ys642*xo2d + ys643*xo3d + ys644*xo4d) * (1 + pi67),
pi65 == (ys651*xo1l + ys652*xo2l + ys653*xo3l + ys654*xo4l) * (1 + pi65) + (ys651*xo1r + ys652*xo2r + ys653*xo3r + ys654*xo4r) * (1 + pi65) + (ys651*xo1u + ys652*xo2u + ys653*xo3u + ys654*xo4u) * (1 + pi62) + (ys651*xo1d + ys652*xo2d + ys653*xo3d + ys654*xo4d) * (1 + pi68),
pi66 == (ys661*xo1l + ys662*xo2l + ys663*xo3l + ys664*xo4l) * (1 + pi66) + (ys661*xo1r + ys662*xo2r + ys663*xo3r + ys664*xo4r) * (1 + pi66) + (ys661*xo1u + ys662*xo2u + ys663*xo3u + ys664*xo4u) * (1 + pi63) + (ys661*xo1d + ys662*xo2d + ys663*xo3d + ys664*xo4d) * (1 + pi69),
pi67 == (ys671*xo1l + ys672*xo2l + ys673*xo3l + ys674*xo4l) * (1 + pi67) + (ys671*xo1r + ys672*xo2r + ys673*xo3r + ys674*xo4r) * (1 + pi67) + (ys671*xo1u + ys672*xo2u + ys673*xo3u + ys674*xo4u) * (1 + pi64) + (ys671*xo1d + ys672*xo2d + ys673*xo3d + ys674*xo4d) * (1 + pi70),
pi68 == (ys681*xo1l + ys682*xo2l + ys683*xo3l + ys684*xo4l) * (1 + pi68) + (ys681*xo1r + ys682*xo2r + ys683*xo3r + ys684*xo4r) * (1 + pi68) + (ys681*xo1u + ys682*xo2u + ys683*xo3u + ys684*xo4u) * (1 + pi65) + (ys681*xo1d + ys682*xo2d + ys683*xo3d + ys684*xo4d) * (1 + pi71),
pi69 == (ys691*xo1l + ys692*xo2l + ys693*xo3l + ys694*xo4l) * (1 + pi69) + (ys691*xo1r + ys692*xo2r + ys693*xo3r + ys694*xo4r) * (1 + pi69) + (ys691*xo1u + ys692*xo2u + ys693*xo3u + ys694*xo4u) * (1 + pi66) + (ys691*xo1d + ys692*xo2d + ys693*xo3d + ys694*xo4d) * (1 + pi72),
pi70 == (ys701*xo1l + ys702*xo2l + ys703*xo3l + ys704*xo4l) * (1 + pi70) + (ys701*xo1r + ys702*xo2r + ys703*xo3r + ys704*xo4r) * (1 + pi70) + (ys701*xo1u + ys702*xo2u + ys703*xo3u + ys704*xo4u) * (1 + pi67) + (ys701*xo1d + ys702*xo2d + ys703*xo3d + ys704*xo4d) * (1 + pi73),
pi71 == (ys711*xo1l + ys712*xo2l + ys713*xo3l + ys714*xo4l) * (1 + pi71) + (ys711*xo1r + ys712*xo2r + ys713*xo3r + ys714*xo4r) * (1 + pi71) + (ys711*xo1u + ys712*xo2u + ys713*xo3u + ys714*xo4u) * (1 + pi68) + (ys711*xo1d + ys712*xo2d + ys713*xo3d + ys714*xo4d) * (1 + pi74),
pi72 == (ys721*xo1l + ys722*xo2l + ys723*xo3l + ys724*xo4l) * (1 + pi72) + (ys721*xo1r + ys722*xo2r + ys723*xo3r + ys724*xo4r) * (1 + pi72) + (ys721*xo1u + ys722*xo2u + ys723*xo3u + ys724*xo4u) * (1 + pi69) + (ys721*xo1d + ys722*xo2d + ys723*xo3d + ys724*xo4d) * (1 + pi75),
pi73 == (ys731*xo1l + ys732*xo2l + ys733*xo3l + ys734*xo4l) * (1 + pi73) + (ys731*xo1r + ys732*xo2r + ys733*xo3r + ys734*xo4r) * (1 + pi73) + (ys731*xo1u + ys732*xo2u + ys733*xo3u + ys734*xo4u) * (1 + pi70) + (ys731*xo1d + ys732*xo2d + ys733*xo3d + ys734*xo4d) * (1 + pi76),
pi74 == (ys741*xo1l + ys742*xo2l + ys743*xo3l + ys744*xo4l) * (1 + pi74) + (ys741*xo1r + ys742*xo2r + ys743*xo3r + ys744*xo4r) * (1 + pi74) + (ys741*xo1u + ys742*xo2u + ys743*xo3u + ys744*xo4u) * (1 + pi71) + (ys741*xo1d + ys742*xo2d + ys743*xo3d + ys744*xo4d) * (1 + pi77),
pi75 == (ys751*xo1l + ys752*xo2l + ys753*xo3l + ys754*xo4l) * (1 + pi75) + (ys751*xo1r + ys752*xo2r + ys753*xo3r + ys754*xo4r) * (1 + pi75) + (ys751*xo1u + ys752*xo2u + ys753*xo3u + ys754*xo4u) * (1 + pi72) + (ys751*xo1d + ys752*xo2d + ys753*xo3d + ys754*xo4d) * (1 + pi78),
pi76 == (ys761*xo1l + ys762*xo2l + ys763*xo3l + ys764*xo4l) * (1 + pi76) + (ys761*xo1r + ys762*xo2r + ys763*xo3r + ys764*xo4r) * (1 + pi76) + (ys761*xo1u + ys762*xo2u + ys763*xo3u + ys764*xo4u) * (1 + pi73) + (ys761*xo1d + ys762*xo2d + ys763*xo3d + ys764*xo4d) * (1 + pi79),
pi77 == (ys771*xo1l + ys772*xo2l + ys773*xo3l + ys774*xo4l) * (1 + pi77) + (ys771*xo1r + ys772*xo2r + ys773*xo3r + ys774*xo4r) * (1 + pi77) + (ys771*xo1u + ys772*xo2u + ys773*xo3u + ys774*xo4u) * (1 + pi74) + (ys771*xo1d + ys772*xo2d + ys773*xo3d + ys774*xo4d) * (1 + pi80),
pi78 == (ys781*xo1l + ys782*xo2l + ys783*xo3l + ys784*xo4l) * (1 + pi78) + (ys781*xo1r + ys782*xo2r + ys783*xo3r + ys784*xo4r) * (1 + pi78) + (ys781*xo1u + ys782*xo2u + ys783*xo3u + ys784*xo4u) * (1 + pi75) + (ys781*xo1d + ys782*xo2d + ys783*xo3d + ys784*xo4d) * (1 + pi81),
pi79 == (ys791*xo1l + ys792*xo2l + ys793*xo3l + ys794*xo4l) * (1 + pi79) + (ys791*xo1r + ys792*xo2r + ys793*xo3r + ys794*xo4r) * (1 + pi79) + (ys791*xo1u + ys792*xo2u + ys793*xo3u + ys794*xo4u) * (1 + pi76) + (ys791*xo1d + ys792*xo2d + ys793*xo3d + ys794*xo4d) * (1 + pi82),
pi80 == (ys801*xo1l + ys802*xo2l + ys803*xo3l + ys804*xo4l) * (1 + pi80) + (ys801*xo1r + ys802*xo2r + ys803*xo3r + ys804*xo4r) * (1 + pi80) + (ys801*xo1u + ys802*xo2u + ys803*xo3u + ys804*xo4u) * (1 + pi77) + (ys801*xo1d + ys802*xo2d + ys803*xo3d + ys804*xo4d) * (1 + pi83),
pi81 == (ys811*xo1l + ys812*xo2l + ys813*xo3l + ys814*xo4l) * (1 + pi81) + (ys811*xo1r + ys812*xo2r + ys813*xo3r + ys814*xo4r) * (1 + pi81) + (ys811*xo1u + ys812*xo2u + ys813*xo3u + ys814*xo4u) * (1 + pi78) + (ys811*xo1d + ys812*xo2d + ys813*xo3d + ys814*xo4d) * (1 + pi84),
pi82 == (ys821*xo1l + ys822*xo2l + ys823*xo3l + ys824*xo4l) * (1 + pi82) + (ys821*xo1r + ys822*xo2r + ys823*xo3r + ys824*xo4r) * (1 + pi82) + (ys821*xo1u + ys822*xo2u + ys823*xo3u + ys824*xo4u) * (1 + pi79) + (ys821*xo1d + ys822*xo2d + ys823*xo3d + ys824*xo4d) * (1 + pi85),
pi83 == (ys831*xo1l + ys832*xo2l + ys833*xo3l + ys834*xo4l) * (1 + pi83) + (ys831*xo1r + ys832*xo2r + ys833*xo3r + ys834*xo4r) * (1 + pi83) + (ys831*xo1u + ys832*xo2u + ys833*xo3u + ys834*xo4u) * (1 + pi80) + (ys831*xo1d + ys832*xo2d + ys833*xo3d + ys834*xo4d) * (1 + pi86),
pi84 == (ys841*xo1l + ys842*xo2l + ys843*xo3l + ys844*xo4l) * (1 + pi84) + (ys841*xo1r + ys842*xo2r + ys843*xo3r + ys844*xo4r) * (1 + pi84) + (ys841*xo1u + ys842*xo2u + ys843*xo3u + ys844*xo4u) * (1 + pi81) + (ys841*xo1d + ys842*xo2d + ys843*xo3d + ys844*xo4d) * (1 + pi87),
pi85 == (ys851*xo1l + ys852*xo2l + ys853*xo3l + ys854*xo4l) * (1 + pi85) + (ys851*xo1r + ys852*xo2r + ys853*xo3r + ys854*xo4r) * (1 + pi85) + (ys851*xo1u + ys852*xo2u + ys853*xo3u + ys854*xo4u) * (1 + pi82) + (ys851*xo1d + ys852*xo2d + ys853*xo3d + ys854*xo4d) * (1 + pi88),
pi86 == (ys861*xo1l + ys862*xo2l + ys863*xo3l + ys864*xo4l) * (1 + pi86) + (ys861*xo1r + ys862*xo2r + ys863*xo3r + ys864*xo4r) * (1 + pi86) + (ys861*xo1u + ys862*xo2u + ys863*xo3u + ys864*xo4u) * (1 + pi83) + (ys861*xo1d + ys862*xo2d + ys863*xo3d + ys864*xo4d) * (1 + pi89),
pi87 == (ys871*xo1l + ys872*xo2l + ys873*xo3l + ys874*xo4l) * (1 + pi87) + (ys871*xo1r + ys872*xo2r + ys873*xo3r + ys874*xo4r) * (1 + pi87) + (ys871*xo1u + ys872*xo2u + ys873*xo3u + ys874*xo4u) * (1 + pi84) + (ys871*xo1d + ys872*xo2d + ys873*xo3d + ys874*xo4d) * (1 + pi90),
pi88 == (ys881*xo1l + ys882*xo2l + ys883*xo3l + ys884*xo4l) * (1 + pi88) + (ys881*xo1r + ys882*xo2r + ys883*xo3r + ys884*xo4r) * (1 + pi88) + (ys881*xo1u + ys882*xo2u + ys883*xo3u + ys884*xo4u) * (1 + pi85) + (ys881*xo1d + ys882*xo2d + ys883*xo3d + ys884*xo4d) * (1 + pi91),
pi89 == (ys891*xo1l + ys892*xo2l + ys893*xo3l + ys894*xo4l) * (1 + pi89) + (ys891*xo1r + ys892*xo2r + ys893*xo3r + ys894*xo4r) * (1 + pi89) + (ys891*xo1u + ys892*xo2u + ys893*xo3u + ys894*xo4u) * (1 + pi86) + (ys891*xo1d + ys892*xo2d + ys893*xo3d + ys894*xo4d) * (1 + pi92),
pi90 == (ys901*xo1l + ys902*xo2l + ys903*xo3l + ys904*xo4l) * (1 + pi90) + (ys901*xo1r + ys902*xo2r + ys903*xo3r + ys904*xo4r) * (1 + pi90) + (ys901*xo1u + ys902*xo2u + ys903*xo3u + ys904*xo4u) * (1 + pi87) + (ys901*xo1d + ys902*xo2d + ys903*xo3d + ys904*xo4d) * (1 + pi93),
pi91 == (ys911*xo1l + ys912*xo2l + ys913*xo3l + ys914*xo4l) * (1 + pi91) + (ys911*xo1r + ys912*xo2r + ys913*xo3r + ys914*xo4r) * (1 + pi91) + (ys911*xo1u + ys912*xo2u + ys913*xo3u + ys914*xo4u) * (1 + pi88) + (ys911*xo1d + ys912*xo2d + ys913*xo3d + ys914*xo4d) * (1 + pi94),
pi92 == (ys921*xo1l + ys922*xo2l + ys923*xo3l + ys924*xo4l) * (1 + pi92) + (ys921*xo1r + ys922*xo2r + ys923*xo3r + ys924*xo4r) * (1 + pi92) + (ys921*xo1u + ys922*xo2u + ys923*xo3u + ys924*xo4u) * (1 + pi89) + (ys921*xo1d + ys922*xo2d + ys923*xo3d + ys924*xo4d) * (1 + pi95),
pi93 == (ys931*xo1l + ys932*xo2l + ys933*xo3l + ys934*xo4l) * (1 + pi93) + (ys931*xo1r + ys932*xo2r + ys933*xo3r + ys934*xo4r) * (1 + pi93) + (ys931*xo1u + ys932*xo2u + ys933*xo3u + ys934*xo4u) * (1 + pi90) + (ys931*xo1d + ys932*xo2d + ys933*xo3d + ys934*xo4d) * (1 + pi96),
pi94 == (ys941*xo1l + ys942*xo2l + ys943*xo3l + ys944*xo4l) * (1 + pi94) + (ys941*xo1r + ys942*xo2r + ys943*xo3r + ys944*xo4r) * (1 + pi94) + (ys941*xo1u + ys942*xo2u + ys943*xo3u + ys944*xo4u) * (1 + pi91) + (ys941*xo1d + ys942*xo2d + ys943*xo3d + ys944*xo4d) * (1 + pi97),
pi95 == (ys951*xo1l + ys952*xo2l + ys953*xo3l + ys954*xo4l) * (1 + pi95) + (ys951*xo1r + ys952*xo2r + ys953*xo3r + ys954*xo4r) * (1 + pi95) + (ys951*xo1u + ys952*xo2u + ys953*xo3u + ys954*xo4u) * (1 + pi92) + (ys951*xo1d + ys952*xo2d + ys953*xo3d + ys954*xo4d) * (1 + pi98),
pi96 == (ys961*xo1l + ys962*xo2l + ys963*xo3l + ys964*xo4l) * (1 + pi96) + (ys961*xo1r + ys962*xo2r + ys963*xo3r + ys964*xo4r) * (1 + pi96) + (ys961*xo1u + ys962*xo2u + ys963*xo3u + ys964*xo4u) * (1 + pi93) + (ys961*xo1d + ys962*xo2d + ys963*xo3d + ys964*xo4d) * (1 + pi99),
pi97 == (ys971*xo1l + ys972*xo2l + ys973*xo3l + ys974*xo4l) * (1 + pi97) + (ys971*xo1r + ys972*xo2r + ys973*xo3r + ys974*xo4r) * (1 + pi97) + (ys971*xo1u + ys972*xo2u + ys973*xo3u + ys974*xo4u) * (1 + pi94) + (ys971*xo1d + ys972*xo2d + ys973*xo3d + ys974*xo4d) * (1 + pi100),
pi98 == (ys981*xo1l + ys982*xo2l + ys983*xo3l + ys984*xo4l) * (1 + pi98) + (ys981*xo1r + ys982*xo2r + ys983*xo3r + ys984*xo4r) * (1 + pi98) + (ys981*xo1u + ys982*xo2u + ys983*xo3u + ys984*xo4u) * (1 + pi95) + (ys981*xo1d + ys982*xo2d + ys983*xo3d + ys984*xo4d) * (1 + pi98),
pi99 == 0, 
pi100 == (ys1001*xo1l + ys1002*xo2l + ys1003*xo3l + ys1004*xo4l) * (1 + pi100) + (ys1001*xo1r + ys1002*xo2r + ys1003*xo3r + ys1004*xo4r) * (1 + pi100) + (ys1001*xo1u + ys1002*xo2u + ys1003*xo3u + ys1004*xo4u) * (1 + pi97) + (ys1001*xo1d + ys1002*xo2d + ys1003*xo3d + ys1004*xo4d) * (1 + pi100),
# We are dropped uniformly in the grid
# We want to check if the minimal expected cost is below some threshold <=Q(3450,100)
(pi0+pi1+pi2+pi3+pi4+pi5+pi6+pi7+pi8+pi9+pi10+pi11+pi12+pi13+pi14+pi15+pi16+pi17+pi18+pi19+pi20+pi21+pi22+pi23+pi24+pi25+pi26+pi27+pi28+pi29+pi30+pi31+pi32+pi33+pi34+pi35+pi36+pi37+pi38+pi39+pi40+pi41+pi42+pi43+pi44+pi45+pi46+pi47+pi48+pi49+pi50+pi51+pi52+pi53+pi54+pi55+pi56+pi57+pi58+pi59+pi60+pi61+pi62+pi63+pi64+pi65+pi66+pi67+pi68+pi69+pi70+pi71+pi72+pi73+pi74+pi75+pi76+pi77+pi78+pi79+pi80+pi81+pi82+pi83+pi84+pi85+pi86+pi87+pi88+pi89+pi90+pi91+pi92+pi93+pi94+pi95+pi96+pi97+pi98+pi100) * Q(1,100) <=Q(3450,100),
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
Or(ys191== 0 , ys191== 1),
Or(ys192== 0 , ys192== 1),
Or(ys193== 0 , ys193== 1),
Or(ys194== 0 , ys194== 1),
Or(ys201== 0 , ys201== 1),
Or(ys202== 0 , ys202== 1),
Or(ys203== 0 , ys203== 1),
Or(ys204== 0 , ys204== 1),
Or(ys211== 0 , ys211== 1),
Or(ys212== 0 , ys212== 1),
Or(ys213== 0 , ys213== 1),
Or(ys214== 0 , ys214== 1),
Or(ys221== 0 , ys221== 1),
Or(ys222== 0 , ys222== 1),
Or(ys223== 0 , ys223== 1),
Or(ys224== 0 , ys224== 1),
Or(ys231== 0 , ys231== 1),
Or(ys232== 0 , ys232== 1),
Or(ys233== 0 , ys233== 1),
Or(ys234== 0 , ys234== 1),
Or(ys241== 0 , ys241== 1),
Or(ys242== 0 , ys242== 1),
Or(ys243== 0 , ys243== 1),
Or(ys244== 0 , ys244== 1),
Or(ys251== 0 , ys251== 1),
Or(ys252== 0 , ys252== 1),
Or(ys253== 0 , ys253== 1),
Or(ys254== 0 , ys254== 1),
Or(ys261== 0 , ys261== 1),
Or(ys262== 0 , ys262== 1),
Or(ys263== 0 , ys263== 1),
Or(ys264== 0 , ys264== 1),
Or(ys271== 0 , ys271== 1),
Or(ys272== 0 , ys272== 1),
Or(ys273== 0 , ys273== 1),
Or(ys274== 0 , ys274== 1),
Or(ys281== 0 , ys281== 1),
Or(ys282== 0 , ys282== 1),
Or(ys283== 0 , ys283== 1),
Or(ys284== 0 , ys284== 1),
Or(ys291== 0 , ys291== 1),
Or(ys292== 0 , ys292== 1),
Or(ys293== 0 , ys293== 1),
Or(ys294== 0 , ys294== 1),
Or(ys301== 0 , ys301== 1),
Or(ys302== 0 , ys302== 1),
Or(ys303== 0 , ys303== 1),
Or(ys304== 0 , ys304== 1),
Or(ys311== 0 , ys311== 1),
Or(ys312== 0 , ys312== 1),
Or(ys313== 0 , ys313== 1),
Or(ys314== 0 , ys314== 1),
Or(ys321== 0 , ys321== 1),
Or(ys322== 0 , ys322== 1),
Or(ys323== 0 , ys323== 1),
Or(ys324== 0 , ys324== 1),
Or(ys331== 0 , ys331== 1),
Or(ys332== 0 , ys332== 1),
Or(ys333== 0 , ys333== 1),
Or(ys334== 0 , ys334== 1),
Or(ys341== 0 , ys341== 1),
Or(ys342== 0 , ys342== 1),
Or(ys343== 0 , ys343== 1),
Or(ys344== 0 , ys344== 1),
Or(ys351== 0 , ys351== 1),
Or(ys352== 0 , ys352== 1),
Or(ys353== 0 , ys353== 1),
Or(ys354== 0 , ys354== 1),
Or(ys361== 0 , ys361== 1),
Or(ys362== 0 , ys362== 1),
Or(ys363== 0 , ys363== 1),
Or(ys364== 0 , ys364== 1),
Or(ys371== 0 , ys371== 1),
Or(ys372== 0 , ys372== 1),
Or(ys373== 0 , ys373== 1),
Or(ys374== 0 , ys374== 1),
Or(ys381== 0 , ys381== 1),
Or(ys382== 0 , ys382== 1),
Or(ys383== 0 , ys383== 1),
Or(ys384== 0 , ys384== 1),
Or(ys391== 0 , ys391== 1),
Or(ys392== 0 , ys392== 1),
Or(ys393== 0 , ys393== 1),
Or(ys394== 0 , ys394== 1),
Or(ys401== 0 , ys401== 1),
Or(ys402== 0 , ys402== 1),
Or(ys403== 0 , ys403== 1),
Or(ys404== 0 , ys404== 1),
Or(ys411== 0 , ys411== 1),
Or(ys412== 0 , ys412== 1),
Or(ys413== 0 , ys413== 1),
Or(ys414== 0 , ys414== 1),
Or(ys421== 0 , ys421== 1),
Or(ys422== 0 , ys422== 1),
Or(ys423== 0 , ys423== 1),
Or(ys424== 0 , ys424== 1),
Or(ys431== 0 , ys431== 1),
Or(ys432== 0 , ys432== 1),
Or(ys433== 0 , ys433== 1),
Or(ys434== 0 , ys434== 1),
Or(ys441== 0 , ys441== 1),
Or(ys442== 0 , ys442== 1),
Or(ys443== 0 , ys443== 1),
Or(ys444== 0 , ys444== 1),
Or(ys451== 0 , ys451== 1),
Or(ys452== 0 , ys452== 1),
Or(ys453== 0 , ys453== 1),
Or(ys454== 0 , ys454== 1),
Or(ys461== 0 , ys461== 1),
Or(ys462== 0 , ys462== 1),
Or(ys463== 0 , ys463== 1),
Or(ys464== 0 , ys464== 1),
Or(ys471== 0 , ys471== 1),
Or(ys472== 0 , ys472== 1),
Or(ys473== 0 , ys473== 1),
Or(ys474== 0 , ys474== 1),
Or(ys481== 0 , ys481== 1),
Or(ys482== 0 , ys482== 1),
Or(ys483== 0 , ys483== 1),
Or(ys484== 0 , ys484== 1),
Or(ys491== 0 , ys491== 1),
Or(ys492== 0 , ys492== 1),
Or(ys493== 0 , ys493== 1),
Or(ys494== 0 , ys494== 1),
Or(ys501== 0 , ys501== 1),
Or(ys502== 0 , ys502== 1),
Or(ys503== 0 , ys503== 1),
Or(ys504== 0 , ys504== 1),
Or(ys511== 0 , ys511== 1),
Or(ys512== 0 , ys512== 1),
Or(ys513== 0 , ys513== 1),
Or(ys514== 0 , ys514== 1),
Or(ys521== 0 , ys521== 1),
Or(ys522== 0 , ys522== 1),
Or(ys523== 0 , ys523== 1),
Or(ys524== 0 , ys524== 1),
Or(ys531== 0 , ys531== 1),
Or(ys532== 0 , ys532== 1),
Or(ys533== 0 , ys533== 1),
Or(ys534== 0 , ys534== 1),
Or(ys541== 0 , ys541== 1),
Or(ys542== 0 , ys542== 1),
Or(ys543== 0 , ys543== 1),
Or(ys544== 0 , ys544== 1),
Or(ys551== 0 , ys551== 1),
Or(ys552== 0 , ys552== 1),
Or(ys553== 0 , ys553== 1),
Or(ys554== 0 , ys554== 1),
Or(ys561== 0 , ys561== 1),
Or(ys562== 0 , ys562== 1),
Or(ys563== 0 , ys563== 1),
Or(ys564== 0 , ys564== 1),
Or(ys571== 0 , ys571== 1),
Or(ys572== 0 , ys572== 1),
Or(ys573== 0 , ys573== 1),
Or(ys574== 0 , ys574== 1),
Or(ys581== 0 , ys581== 1),
Or(ys582== 0 , ys582== 1),
Or(ys583== 0 , ys583== 1),
Or(ys584== 0 , ys584== 1),
Or(ys591== 0 , ys591== 1),
Or(ys592== 0 , ys592== 1),
Or(ys593== 0 , ys593== 1),
Or(ys594== 0 , ys594== 1),
Or(ys601== 0 , ys601== 1),
Or(ys602== 0 , ys602== 1),
Or(ys603== 0 , ys603== 1),
Or(ys604== 0 , ys604== 1),
Or(ys611== 0 , ys611== 1),
Or(ys612== 0 , ys612== 1),
Or(ys613== 0 , ys613== 1),
Or(ys614== 0 , ys614== 1),
Or(ys621== 0 , ys621== 1),
Or(ys622== 0 , ys622== 1),
Or(ys623== 0 , ys623== 1),
Or(ys624== 0 , ys624== 1),
Or(ys631== 0 , ys631== 1),
Or(ys632== 0 , ys632== 1),
Or(ys633== 0 , ys633== 1),
Or(ys634== 0 , ys634== 1),
Or(ys641== 0 , ys641== 1),
Or(ys642== 0 , ys642== 1),
Or(ys643== 0 , ys643== 1),
Or(ys644== 0 , ys644== 1),
Or(ys651== 0 , ys651== 1),
Or(ys652== 0 , ys652== 1),
Or(ys653== 0 , ys653== 1),
Or(ys654== 0 , ys654== 1),
Or(ys661== 0 , ys661== 1),
Or(ys662== 0 , ys662== 1),
Or(ys663== 0 , ys663== 1),
Or(ys664== 0 , ys664== 1),
Or(ys671== 0 , ys671== 1),
Or(ys672== 0 , ys672== 1),
Or(ys673== 0 , ys673== 1),
Or(ys674== 0 , ys674== 1),
Or(ys681== 0 , ys681== 1),
Or(ys682== 0 , ys682== 1),
Or(ys683== 0 , ys683== 1),
Or(ys684== 0 , ys684== 1),
Or(ys691== 0 , ys691== 1),
Or(ys692== 0 , ys692== 1),
Or(ys693== 0 , ys693== 1),
Or(ys694== 0 , ys694== 1),
Or(ys701== 0 , ys701== 1),
Or(ys702== 0 , ys702== 1),
Or(ys703== 0 , ys703== 1),
Or(ys704== 0 , ys704== 1),
Or(ys711== 0 , ys711== 1),
Or(ys712== 0 , ys712== 1),
Or(ys713== 0 , ys713== 1),
Or(ys714== 0 , ys714== 1),
Or(ys721== 0 , ys721== 1),
Or(ys722== 0 , ys722== 1),
Or(ys723== 0 , ys723== 1),
Or(ys724== 0 , ys724== 1),
Or(ys731== 0 , ys731== 1),
Or(ys732== 0 , ys732== 1),
Or(ys733== 0 , ys733== 1),
Or(ys734== 0 , ys734== 1),
Or(ys741== 0 , ys741== 1),
Or(ys742== 0 , ys742== 1),
Or(ys743== 0 , ys743== 1),
Or(ys744== 0 , ys744== 1),
Or(ys751== 0 , ys751== 1),
Or(ys752== 0 , ys752== 1),
Or(ys753== 0 , ys753== 1),
Or(ys754== 0 , ys754== 1),
Or(ys761== 0 , ys761== 1),
Or(ys762== 0 , ys762== 1),
Or(ys763== 0 , ys763== 1),
Or(ys764== 0 , ys764== 1),
Or(ys771== 0 , ys771== 1),
Or(ys772== 0 , ys772== 1),
Or(ys773== 0 , ys773== 1),
Or(ys774== 0 , ys774== 1),
Or(ys781== 0 , ys781== 1),
Or(ys782== 0 , ys782== 1),
Or(ys783== 0 , ys783== 1),
Or(ys784== 0 , ys784== 1),
Or(ys791== 0 , ys791== 1),
Or(ys792== 0 , ys792== 1),
Or(ys793== 0 , ys793== 1),
Or(ys794== 0 , ys794== 1),
Or(ys801== 0 , ys801== 1),
Or(ys802== 0 , ys802== 1),
Or(ys803== 0 , ys803== 1),
Or(ys804== 0 , ys804== 1),
Or(ys811== 0 , ys811== 1),
Or(ys812== 0 , ys812== 1),
Or(ys813== 0 , ys813== 1),
Or(ys814== 0 , ys814== 1),
Or(ys821== 0 , ys821== 1),
Or(ys822== 0 , ys822== 1),
Or(ys823== 0 , ys823== 1),
Or(ys824== 0 , ys824== 1),
Or(ys831== 0 , ys831== 1),
Or(ys832== 0 , ys832== 1),
Or(ys833== 0 , ys833== 1),
Or(ys834== 0 , ys834== 1),
Or(ys841== 0 , ys841== 1),
Or(ys842== 0 , ys842== 1),
Or(ys843== 0 , ys843== 1),
Or(ys844== 0 , ys844== 1),
Or(ys851== 0 , ys851== 1),
Or(ys852== 0 , ys852== 1),
Or(ys853== 0 , ys853== 1),
Or(ys854== 0 , ys854== 1),
Or(ys861== 0 , ys861== 1),
Or(ys862== 0 , ys862== 1),
Or(ys863== 0 , ys863== 1),
Or(ys864== 0 , ys864== 1),
Or(ys871== 0 , ys871== 1),
Or(ys872== 0 , ys872== 1),
Or(ys873== 0 , ys873== 1),
Or(ys874== 0 , ys874== 1),
Or(ys881== 0 , ys881== 1),
Or(ys882== 0 , ys882== 1),
Or(ys883== 0 , ys883== 1),
Or(ys884== 0 , ys884== 1),
Or(ys891== 0 , ys891== 1),
Or(ys892== 0 , ys892== 1),
Or(ys893== 0 , ys893== 1),
Or(ys894== 0 , ys894== 1),
Or(ys901== 0 , ys901== 1),
Or(ys902== 0 , ys902== 1),
Or(ys903== 0 , ys903== 1),
Or(ys904== 0 , ys904== 1),
Or(ys911== 0 , ys911== 1),
Or(ys912== 0 , ys912== 1),
Or(ys913== 0 , ys913== 1),
Or(ys914== 0 , ys914== 1),
Or(ys921== 0 , ys921== 1),
Or(ys922== 0 , ys922== 1),
Or(ys923== 0 , ys923== 1),
Or(ys924== 0 , ys924== 1),
Or(ys931== 0 , ys931== 1),
Or(ys932== 0 , ys932== 1),
Or(ys933== 0 , ys933== 1),
Or(ys934== 0 , ys934== 1),
Or(ys941== 0 , ys941== 1),
Or(ys942== 0 , ys942== 1),
Or(ys943== 0 , ys943== 1),
Or(ys944== 0 , ys944== 1),
Or(ys951== 0 , ys951== 1),
Or(ys952== 0 , ys952== 1),
Or(ys953== 0 , ys953== 1),
Or(ys954== 0 , ys954== 1),
Or(ys961== 0 , ys961== 1),
Or(ys962== 0 , ys962== 1),
Or(ys963== 0 , ys963== 1),
Or(ys964== 0 , ys964== 1),
Or(ys971== 0 , ys971== 1),
Or(ys972== 0 , ys972== 1),
Or(ys973== 0 , ys973== 1),
Or(ys974== 0 , ys974== 1),
Or(ys981== 0 , ys981== 1),
Or(ys982== 0 , ys982== 1),
Or(ys983== 0 , ys983== 1),
Or(ys984== 0 , ys984== 1),
Or(ys1001== 0 , ys1001== 1),
Or(ys1002== 0 , ys1002== 1),
Or(ys1003== 0 , ys1003== 1),
Or(ys1004== 0 , ys1004== 1),
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
ys191 + ys192 + ys193 + ys194 == 1,
ys201 + ys202 + ys203 + ys204 == 1,
ys211 + ys212 + ys213 + ys214 == 1,
ys221 + ys222 + ys223 + ys224 == 1,
ys231 + ys232 + ys233 + ys234 == 1,
ys241 + ys242 + ys243 + ys244 == 1,
ys251 + ys252 + ys253 + ys254 == 1,
ys261 + ys262 + ys263 + ys264 == 1,
ys271 + ys272 + ys273 + ys274 == 1,
ys281 + ys282 + ys283 + ys284 == 1,
ys291 + ys292 + ys293 + ys294 == 1,
ys301 + ys302 + ys303 + ys304 == 1,
ys311 + ys312 + ys313 + ys314 == 1,
ys321 + ys322 + ys323 + ys324 == 1,
ys331 + ys332 + ys333 + ys334 == 1,
ys341 + ys342 + ys343 + ys344 == 1,
ys351 + ys352 + ys353 + ys354 == 1,
ys361 + ys362 + ys363 + ys364 == 1,
ys371 + ys372 + ys373 + ys374 == 1,
ys381 + ys382 + ys383 + ys384 == 1,
ys391 + ys392 + ys393 + ys394 == 1,
ys401 + ys402 + ys403 + ys404 == 1,
ys411 + ys412 + ys413 + ys414 == 1,
ys421 + ys422 + ys423 + ys424 == 1,
ys431 + ys432 + ys433 + ys434 == 1,
ys441 + ys442 + ys443 + ys444 == 1,
ys451 + ys452 + ys453 + ys454 == 1,
ys461 + ys462 + ys463 + ys464 == 1,
ys471 + ys472 + ys473 + ys474 == 1,
ys481 + ys482 + ys483 + ys484 == 1,
ys491 + ys492 + ys493 + ys494 == 1,
ys501 + ys502 + ys503 + ys504 == 1,
ys511 + ys512 + ys513 + ys514 == 1,
ys521 + ys522 + ys523 + ys524 == 1,
ys531 + ys532 + ys533 + ys534 == 1,
ys541 + ys542 + ys543 + ys544 == 1,
ys551 + ys552 + ys553 + ys554 == 1,
ys561 + ys562 + ys563 + ys564 == 1,
ys571 + ys572 + ys573 + ys574 == 1,
ys581 + ys582 + ys583 + ys584 == 1,
ys591 + ys592 + ys593 + ys594 == 1,
ys601 + ys602 + ys603 + ys604 == 1,
ys611 + ys612 + ys613 + ys614 == 1,
ys621 + ys622 + ys623 + ys624 == 1,
ys631 + ys632 + ys633 + ys634 == 1,
ys641 + ys642 + ys643 + ys644 == 1,
ys651 + ys652 + ys653 + ys654 == 1,
ys661 + ys662 + ys663 + ys664 == 1,
ys671 + ys672 + ys673 + ys674 == 1,
ys681 + ys682 + ys683 + ys684 == 1,
ys691 + ys692 + ys693 + ys694 == 1,
ys701 + ys702 + ys703 + ys704 == 1,
ys711 + ys712 + ys713 + ys714 == 1,
ys721 + ys722 + ys723 + ys724 == 1,
ys731 + ys732 + ys733 + ys734 == 1,
ys741 + ys742 + ys743 + ys744 == 1,
ys751 + ys752 + ys753 + ys754 == 1,
ys761 + ys762 + ys763 + ys764 == 1,
ys771 + ys772 + ys773 + ys774 == 1,
ys781 + ys782 + ys783 + ys784 == 1,
ys791 + ys792 + ys793 + ys794 == 1,
ys801 + ys802 + ys803 + ys804 == 1,
ys811 + ys812 + ys813 + ys814 == 1,
ys821 + ys822 + ys823 + ys824 == 1,
ys831 + ys832 + ys833 + ys834 == 1,
ys841 + ys842 + ys843 + ys844 == 1,
ys851 + ys852 + ys853 + ys854 == 1,
ys861 + ys862 + ys863 + ys864 == 1,
ys871 + ys872 + ys873 + ys874 == 1,
ys881 + ys882 + ys883 + ys884 == 1,
ys891 + ys892 + ys893 + ys894 == 1,
ys901 + ys902 + ys903 + ys904 == 1,
ys911 + ys912 + ys913 + ys914 == 1,
ys921 + ys922 + ys923 + ys924 == 1,
ys931 + ys932 + ys933 + ys934 == 1,
ys941 + ys942 + ys943 + ys944 == 1,
ys951 + ys952 + ys953 + ys954 == 1,
ys961 + ys962 + ys963 + ys964 == 1,
ys971 + ys972 + ys973 + ys974 == 1,
ys981 + ys982 + ys983 + ys984 == 1,
ys1001 + ys1002 + ys1003 + ys1004 == 1
)

if solver.check() == sat:
	m = solver.model()
	print('This is a solution:')
	print(m)
elif solver.check() == unsat:
	print('No solution!!!')
else:
	print('Unknown')
