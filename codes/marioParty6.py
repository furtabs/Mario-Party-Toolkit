# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

def getBlueSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Blue Spaces Give {amountDec} Coins
C215F1E8 00000001
3880{amount} 00000000
'''

def getRedSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Red Spaces Take Away {amountDec} Coins
C215F278 00000001
3880{amount} 00000000
'''

def getMinigameCodeSix(amount, amountDec):
    return f'''
MP6 - Minigames Award {amountDec} Coins
C203A41C 00000013
3DC08026 61CE5BA8
89EE0000 2C0F0015
41820070 2C0F0016
41820068 2C0F0029
41820060 2C0F002D
41820058 2C0F002E
41820050 2C0F0030
41820048 2C0F003F
41820040 2C0F004F
41820038 2C0F0050
41820030 3DC08026
61CE5778 A1EE0000
2C0F0000 4182000C
39E0{amount} B1EE0000
39CE0108 3A100001
2C100003 4081FFE0
900D8B74 39C00000
39E00000 3A000000
60000000 00000000
'''

def getCharacterSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Character Spaces Give {amountDec} Coins
C215F230 00000001
3880{amount} 00000000
'''

def getStarSpaceCodeSix(amount, negAmount, amountDec, y4, y2, x2, x4):
    return f'''
MP6 - Stars Cost {amountDec} Coins
C218333C 00000001
2C03{amount} 00000000
C218342C 00000001
2C03{amount} 00000000
C21834C4 00000001
2C03{amount} 00000000
C215F668 00000001
2C03{amount} 00000000
C215FA18 00000001
3880{negAmount} 00000000
C216068C 00000001
2C00{amount} 00000000
C2160D0C 00000001
3880{negAmount} 00000000  
C2183590 00000002
3880{amount} 7C8400D0
60000000 00000000
28265B8A 00000014
00265B8B 0000{amount}
E2000001 80008000
204F0E28 2C030014
044F0E28 2C03{amount}
E2000001 80008000
204F0F38 3880FFEC
044F0F38 3880{negAmount}
E2000001 80008000
C2184538 00000001
2C14{amount} 00000000
C2184544 00000001
3880{negAmount} 00000000
28265B8A 00000014
00265B8B 000000{amount}
E2000001 80008000
04248064 000000{y4}
04248068 000000{y2}
04248070 000000{x2}
04248074 000000{x4}
04248D3C 000000{y4}
04248D40 000000{y2}
04248D48 000000{x2}
04248D4C 000000{x4}
204DDF60 465F6C00
044DDF74 000000{y4}
044DDF78 000000{y2}
044DDF80 000000{x2}
044DDF84 000000{x4}
E2000001 80008000
'''

def getPinkBooSpaceCodeSix(amount, negAmount, amountDec):
    return f'''
MP6 - Star Stealing Costs {amountDec} with Pink Boo.
C21B1FB4 00000001
2C04{amount} 00000000
C21B2634 00000001
3880{negAmount} 00000000
'''

def getPinkBooCoinsSpaceCodeSix(amount, negAmount, amountDec):
    return f'''
MP6 - Coin Stealing Costs {amountDec} with Pink Boo.
C21B1F28 00000001
2C03{amount} 00000000
C21B2626 00000001
3880{negAmount} 00000000
'''

def getMinigameReplacement6(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP6 - Minigame Replacement: {gameUno} ➜ {gameDos}
28265BA8 000000{hexUno}
02265BA8 000000{hexDos}
E2000001 80008000
'''

def getOrbModsSix(mushroomPrice1, mushroomPrice2, mushroomPrice34, mushroomSpaceOdds1, mushroomSpaceOdds2, mushroomSpaceOdds3, mushroomSpaceOdds4, mushroomShopOdds123, mushroomShopOdds4, goldenMushroomPrice1, goldenMushroomPrice2, goldenMushroomPrice34, goldenMushroomSpaceOdds1, goldenMushroomSpaceOdds2, goldenMushroomSpaceOdds3, goldenMushroomSpaceOdds4, goldenMushroomShopOdds123, goldenMushroomShopOdds4, slowMushroomPrice1, slowMushroomPrice2, slowMushroomPrice34, slowMushroomSpaceOdds1, slowMushroomSpaceOdds2, slowMushroomSpaceOdds3, slowMushroomSpaceOdds4, slowMushroomShopOdds123, slowMushroomShopOdds4, metalMushroomPrice1, metalMushroomPrice2, metalMushroomPrice34, metalMushroomSpaceOdds1, metalMushroomSpaceOdds2, metalMushroomSpaceOdds3, metalMushroomSpaceOdds4, metalMushroomShopOdds123, metalMushroomShopOdds4, bulletBillPrice1, bulletBillPrice2, bulletBillPrice34, bulletBillSpaceOdds1, bulletBillSpaceOdds2, bulletBillSpaceOdds3, bulletBillSpaceOdds4, bulletBillShopOdds123, bulletBillShopOdds4, flutterPrice1, flutterPrice2, flutterPrice34, flutterSpaceOdds1, flutterSpaceOdds2, flutterSpaceOdds3, flutterSpaceOdds4, flutterShopOdds123, flutterShopOdds4, cursedMushroomPrice1, cursedMushroomPrice2, cursedMushroomPrice34, cursedMushroomSpaceOdds1, cursedMushroomSpaceOdds2, cursedMushroomSpaceOdds3, cursedMushroomSpaceOdds4, cursedMushroomShopOdds123, cursedMushroomShopOdds4, spinyPrice1, spinyPrice2, spinyPrice34, spinySpaceOdds1, spinySpaceOdds2, spinySpaceOdds3, spinySpaceOdds4, spinyShopOdds123, spinyShopOdds4, goombaPrice1, goombaPrice2, goombaPrice34, goombaSpaceOdds1, goombaSpaceOdds2, goombaSpaceOdds3, goombaSpaceOdds4, goombaShopOdds123, goombaShopOdds4, plantPrice1, plantPrice2, plantPrice34, plantSpaceOdds1, plantSpaceOdds2, plantSpaceOdds3, plantSpaceOdds4, plantShopOdds123, plantShopOdds4, kleptoPrice1, kleptoPrice2, kleptoPrice34, kleptoSpaceOdds1, kleptoSpaceOdds2, kleptoSpaceOdds3, kleptoSpaceOdds4, kleptoShopOdds123, kleptoShopOdds4, toadyPrice1, toadyPrice2, toadyPrice34, toadySpaceOdds1, toadySpaceOdds2, toadySpaceOdds3, toadySpaceOdds4, toadyShopOdds123, toadyShopOdds4, kamekPrice1, kamekPrice2, kamekPrice34, kamekSpaceOdds1, kamekSpaceOdds2, kamekSpaceOdds3, kamekSpaceOdds4, kamekShopOdds123, kamekShopOdds4, blizzardPrice1, blizzardPrice2, blizzardPrice34, blizzardSpaceOdds1, blizzardSpaceOdds2, blizzardSpaceOdds3, blizzardSpaceOdds4, blizzardShopOdds123, blizzardShopOdds4, podobooPrice1, podobooPrice2, podobooPrice34, podobooSpaceOdds1, podobooSpaceOdds2, podobooSpaceOdds3, podobooSpaceOdds4, podobooShopOdds123, podobooShopOdds4, zapPrice1, zapPrice2, zapPrice34, zapSpaceOdds1, zapSpaceOdds2, zapSpaceOdds3, zapSpaceOdds4, zapShopOdds123, zapShopOdds4, tweesterPrice1, tweesterPrice2, tweesterPrice34, tweesterSpaceOdds1, tweesterSpaceOdds2, tweesterSpaceOdds3, tweesterSpaceOdds4, tweesterShopOdds123, tweesterShopOdds4, thwompPrice1, thwompPrice2, thwompPrice34, thwompSpaceOdds1, thwompSpaceOdds2, thwompSpaceOdds3, thwompSpaceOdds4, thwompShopOdds123, thwompShopOdds4, warpPipePrice1, warpPipePrice2, warpPipePrice34, warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds3, warpPipeSpaceOdds4, warpPipeShopOdds123, warpPipeShopOdds4, bombPrice1, bombPrice2, bombPrice34, bombSpaceOdds1, bombSpaceOdds2, bombSpaceOdds3, bombSpaceOdds4, bombShopOdds123, bombShopOdds4, paraTroopaPrice1, paraTroopaPrice2, paraTroopaPrice34, paraTroopaSpaceOdds1, paraTroopaSpaceOdds2, paraTroopaSpaceOdds3, paraTroopaSpaceOdds4, paraTroopaShopOdds123, paraTroopaShopOdds4, snackPrice1, snackPrice2, snackPrice34, snackSpaceOdds1, snackSpaceOdds2, snackSpaceOdds3, snackSpaceOdds4, snackShopOdds123, snackShopOdds4, gaddLightPrice1, gaddLightPrice2, gaddLightPrice34, gaddLightSpaceOdds1, gaddLightSpaceOdds2, gaddLightSpaceOdds3, gaddLightSpaceOdds4, gaddLightShopOdds123, gaddLightShopOdds4):
    return f'''
MP6 - Orb Modifier
042BD220 00{mushroomPrice2}{mushroomPrice1}{mushroomPrice34}
042BD224 {mushroomSpaceOdds1}{mushroomSpaceOdds2}{mushroomSpaceOdds3}{mushroomSpaceOdds4}
042BD228 {mushroomSpaceOdds1}{mushroomSpaceOdds2}{mushroomSpaceOdds3}{mushroomSpaceOdds4}
042BD22C {mushroomShopOdds123}{mushroomShopOdds4}{mushroomShopOdds123}{mushroomShopOdds4}
042BD230 01{goldenMushroomPrice1}{goldenMushroomPrice2}{goldenMushroomPrice34}
042BD234 {goldenMushroomSpaceOdds1}{goldenMushroomSpaceOdds2}{goldenMushroomSpaceOdds3}{goldenMushroomSpaceOdds4}
042BD238 {goldenMushroomSpaceOdds1}{goldenMushroomSpaceOdds2}{goldenMushroomSpaceOdds3}{goldenMushroomSpaceOdds4}
042BD23C {goldenMushroomShopOdds123}{goldenMushroomShopOdds4}{goldenMushroomShopOdds123}{goldenMushroomShopOdds4}
042BD240 02{slowMushroomPrice1}{slowMushroomPrice2}{slowMushroomPrice34}
042BD244 {slowMushroomSpaceOdds1}{slowMushroomSpaceOdds2}{slowMushroomSpaceOdds3}{slowMushroomSpaceOdds4}
042BD248 {slowMushroomSpaceOdds1}{slowMushroomSpaceOdds2}{slowMushroomSpaceOdds3}{slowMushroomSpaceOdds4}
042BD24C {slowMushroomShopOdds123}{slowMushroomShopOdds4}{slowMushroomShopOdds123}{slowMushroomShopOdds4}
042BD250 03{metalMushroomPrice1}{metalMushroomPrice2}{metalMushroomPrice34}
042BD254 {metalMushroomSpaceOdds1}{metalMushroomSpaceOdds2}{metalMushroomSpaceOdds3}{metalMushroomSpaceOdds4}
042BD258 {metalMushroomSpaceOdds1}{metalMushroomSpaceOdds2}{metalMushroomSpaceOdds3}{metalMushroomSpaceOdds4}
042BD25C {metalMushroomShopOdds123}{metalMushroomShopOdds4}{metalMushroomShopOdds123}{metalMushroomShopOdds4}
042BD260 04{bulletBillPrice1}{bulletBillPrice2}{bulletBillPrice34}
042BD264 {bulletBillSpaceOdds1}{bulletBillSpaceOdds2}{bulletBillSpaceOdds3}{bulletBillSpaceOdds4}
042BD268 {bulletBillSpaceOdds1}{bulletBillSpaceOdds2}{bulletBillSpaceOdds3}{bulletBillSpaceOdds4}
042BD26C {bulletBillShopOdds123}{bulletBillShopOdds4}{bulletBillShopOdds123}{bulletBillShopOdds4}
042BD270 05{flutterPrice1}{flutterPrice2}{flutterPrice34}
042BD274 {flutterSpaceOdds1}{flutterSpaceOdds2}{flutterSpaceOdds3}{flutterSpaceOdds4}
042BD278 {flutterSpaceOdds1}{flutterSpaceOdds2}{flutterSpaceOdds3}{flutterSpaceOdds4}
042BD27C {flutterShopOdds123}{flutterShopOdds4}{flutterShopOdds123}{flutterShopOdds4}
042BD280 06{cursedMushroomPrice1}{cursedMushroomPrice2}{cursedMushroomPrice34}
042BD284 {cursedMushroomSpaceOdds1}{cursedMushroomSpaceOdds2}{cursedMushroomSpaceOdds3}{cursedMushroomSpaceOdds4}
042BD288 {cursedMushroomSpaceOdds1}{cursedMushroomSpaceOdds2}{cursedMushroomSpaceOdds3}{cursedMushroomSpaceOdds4}
042BD28C {cursedMushroomShopOdds123}{cursedMushroomShopOdds4}{cursedMushroomShopOdds123}{cursedMushroomShopOdds4}
042BD290 07{spinyPrice1}{spinyPrice2}{spinyPrice34}
042BD294 {spinySpaceOdds1}{spinySpaceOdds2}{spinySpaceOdds3}{spinySpaceOdds4}
042BD298 {spinySpaceOdds1}{spinySpaceOdds2}{spinySpaceOdds3}{spinySpaceOdds4}
042BD29C {spinyShopOdds123}{spinyShopOdds4}{spinyShopOdds123}{spinyShopOdds4}
042BD2A0 0A{goombaPrice1}{goombaPrice2}{goombaPrice34}
042BD2A4 {goombaSpaceOdds1}{goombaSpaceOdds2}{goombaSpaceOdds3}{goombaSpaceOdds4}
042BD2A8 {goombaSpaceOdds1}{goombaSpaceOdds2}{goombaSpaceOdds3}{goombaSpaceOdds4}
042BD2AC {goombaShopOdds123}{goombaShopOdds4}{goombaShopOdds123}{goombaShopOdds4}
042BD2B0 0B{plantPrice1}{plantPrice2}{plantPrice34}
042BD2B4 {plantSpaceOdds1}{plantSpaceOdds2}{plantSpaceOdds3}{plantSpaceOdds4}
042BD2B8 {plantSpaceOdds1}{plantSpaceOdds2}{plantSpaceOdds3}{plantSpaceOdds4}
042BD2BC {plantShopOdds123}{plantShopOdds4}{plantShopOdds123}{plantShopOdds4}
042BD2C0 0C{kleptoPrice1}{kleptoPrice2}{kleptoPrice34}
042BD2C4 {kleptoSpaceOdds1}{kleptoSpaceOdds2}{kleptoSpaceOdds3}{kleptoSpaceOdds4}
042BD2C8 {kleptoSpaceOdds1}{kleptoSpaceOdds2}{kleptoSpaceOdds3}{kleptoSpaceOdds4}
042BD2CC {kleptoShopOdds123}{kleptoShopOdds4}{kleptoShopOdds123}{kleptoShopOdds4}
042BD2D0 0D{toadyPrice1}{toadyPrice2}{toadyPrice34}
042BD2D4 {toadySpaceOdds1}{toadySpaceOdds2}{toadySpaceOdds3}{toadySpaceOdds4}
042BD2D8 {toadySpaceOdds1}{toadySpaceOdds2}{toadySpaceOdds3}{toadySpaceOdds4}
042BD2DC {toadyShopOdds123}{toadyShopOdds4}{toadyShopOdds123}{toadyShopOdds4}
042BD2E0 0F{kamekPrice1}{kamekPrice2}{kamekPrice34}
042BD2E4 {kamekSpaceOdds1}{kamekSpaceOdds2}{kamekSpaceOdds3}{kamekSpaceOdds4}
042BD2E8 {kamekSpaceOdds1}{kamekSpaceOdds2}{kamekSpaceOdds3}{kamekSpaceOdds4}
042BD2EC {kamekShopOdds123}{kamekShopOdds4}{kamekShopOdds123}{kamekShopOdds4}
042BD2F0 10{blizzardPrice1}{blizzardPrice2}{blizzardPrice34}
042BD2F4 {blizzardSpaceOdds1}{blizzardSpaceOdds2}{blizzardSpaceOdds3}{blizzardSpaceOdds4}
042BD2F8 {blizzardSpaceOdds1}{blizzardSpaceOdds2}{blizzardSpaceOdds3}{blizzardSpaceOdds4}
042BD2FC {blizzardShopOdds123}{blizzardShopOdds4}{blizzardShopOdds123}{blizzardShopOdds4}
042BD300 11{podobooPrice1}{podobooPrice2}{podobooPrice34}
042BD304 {podobooSpaceOdds1}{podobooSpaceOdds2}{podobooSpaceOdds3}{podobooSpaceOdds4}
042BD308 {podobooSpaceOdds1}{podobooSpaceOdds2}{podobooSpaceOdds3}{podobooSpaceOdds4}
042BD30C {podobooShopOdds123}{podobooShopOdds4}{podobooShopOdds123}{podobooShopOdds4}
042BD310 14{zapPrice1}{zapPrice2}{zapPrice34}
042BD314 {zapSpaceOdds1}{zapSpaceOdds2}{zapSpaceOdds3}{zapSpaceOdds4}
042BD318 {zapSpaceOdds1}{zapSpaceOdds2}{zapSpaceOdds3}{zapSpaceOdds4}
042BD31C {zapShopOdds123}{zapShopOdds4}{zapShopOdds123}{zapShopOdds4}
042BD320 15{tweesterPrice1}{tweesterPrice2}{tweesterPrice34}
042BD324 {tweesterSpaceOdds1}{tweesterSpaceOdds2}{tweesterSpaceOdds3}{tweesterSpaceOdds4}
042BD328 {tweesterSpaceOdds1}{tweesterSpaceOdds2}{tweesterSpaceOdds3}{tweesterSpaceOdds4}
042BD32C {tweesterShopOdds123}{tweesterShopOdds4}{tweesterShopOdds123}{tweesterShopOdds4}
042BD330 16{thwompPrice1}{thwompPrice2}{thwompPrice34}
042BD334 {thwompSpaceOdds1}{thwompSpaceOdds2}{thwompSpaceOdds3}{thwompSpaceOdds4}
042BD338 {thwompSpaceOdds1}{thwompSpaceOdds2}{thwompSpaceOdds3}{thwompSpaceOdds4}
042BD33C {thwompShopOdds123}{thwompShopOdds4}{thwompShopOdds123}{thwompShopOdds4}
042BD340 17{warpPipePrice1}{warpPipePrice2}{warpPipePrice34}
042BD344 {warpPipeSpaceOdds1}{warpPipeSpaceOdds2}{warpPipeSpaceOdds3}{warpPipeSpaceOdds4}
042BD348 {warpPipeSpaceOdds1}{warpPipeSpaceOdds2}{warpPipeSpaceOdds3}{warpPipeSpaceOdds4}
042BD34C {warpPipeShopOdds123}{warpPipeShopOdds4}{warpPipeShopOdds123}{warpPipeShopOdds4}
042BD350 18{bombPrice1}{bombPrice2}{bombPrice34}
042BD354 {bombSpaceOdds1}{bombSpaceOdds2}{bombSpaceOdds3}{bombSpaceOdds4}
042BD358 {bombSpaceOdds1}{bombSpaceOdds2}{bombSpaceOdds3}{bombSpaceOdds4}
042BD35C {bombShopOdds123}{bombShopOdds4}{bombShopOdds123}{bombShopOdds4}
042BD360 19{paraTroopaPrice1}{paraTroopaPrice2}{paraTroopaPrice34}
042BD364 {paraTroopaSpaceOdds1}{paraTroopaSpaceOdds2}{paraTroopaSpaceOdds3}{paraTroopaSpaceOdds4}
042BD368 {paraTroopaSpaceOdds1}{paraTroopaSpaceOdds2}{paraTroopaSpaceOdds3}{paraTroopaSpaceOdds4}
042BD36C {paraTroopaShopOdds123}{paraTroopaShopOdds4}{paraTroopaShopOdds123}{paraTroopaShopOdds4}
042BD370 1E{snackPrice1}{snackPrice2}{snackPrice34}
042BD374 {snackSpaceOdds1}{snackSpaceOdds2}{snackSpaceOdds3}{snackSpaceOdds4}
042BD378 {snackSpaceOdds1}{snackSpaceOdds2}{snackSpaceOdds3}{snackSpaceOdds4}
042BD37C {snackShopOdds123}{snackShopOdds4}{snackShopOdds123}{snackShopOdds4}
042BD380 1F{gaddLightPrice1}{gaddLightPrice2}{gaddLightPrice34}
042BD384 {gaddLightSpaceOdds1}{gaddLightSpaceOdds2}{gaddLightSpaceOdds3}{gaddLightSpaceOdds4}
042BD388 {gaddLightSpaceOdds1}{gaddLightSpaceOdds2}{gaddLightSpaceOdds3}{gaddLightSpaceOdds4}
042BD38C {gaddLightShopOdds123}{gaddLightShopOdds4}{gaddLightShopOdds123}{gaddLightShopOdds4}
042BD390 FF000000
042BD394 00000000
042BD398 00000000
042BD39C 00000000
'''

def getInitialItemsSix(one, two, three, oneItem, twoItem, threeItem):
    return f'''
MP6 - Start with {oneItem}, {twoItem}, and {threeItem}
06003620 00000028
3D808000 618C363C
1C1F0003 7C00E214
7CAC00AE 98A30005
48150114 {one}{two}{three}{one}
{two}{three}{one}{two} {three}{one}{two}{three}
C2153748 00000001
4BEAFED8 00000000
'''

def getCoinStealBaseSix(value, amountDec):
    return f'''
MP6 - Steal Minimum Of {amountDec} Coins from Pink Boo
C21B3498 00000002
3884{value} 9081002C
60000000 00000000
'''

def getSpaceReplaceSix1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP6 - Replace {spaceName} with {spaceName2} (Slot A)
C217590C 00000005
A01F0030 280000{spaceHex1}
40820018 A09F0032
2804FFFF 4082000C
380000{spaceHex2} B01F0030
88030000 00000000
'''

def getSpaceReplaceSix2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP6 - Replace {spaceName} with {spaceName2} (Slot B)
C2175910 00000005
5418CFFE A01F0030
280000{spaceHex1} 40820018
A09F0032 2804FFFF
4082000C 380000{spaceHex2}
B01F0030 00000000
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP6 - Star Handicap
28265772 00000000
02265780 0000{p1}
02265888 0000{p2}
02265990 0000{p3}
02265A98 0000{p4}
E2000001 80008000
'''

def getStarReplaceSix1(amount, amountDec):
    return f'''
MP6 - Replace Minigame Star with {amountDec}
204ECF10 A883001E
C24ECF10 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSix2(amount, amountDec):
    return f'''
MP6 - Replace Orb Star with {amountDec}
204ECF4C A8C70034
C24ECF4C 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSix3(amount, amountDec):
    return f'''
MP6 - Replace Happening Star with {amountDec}
204ECF88 88040017
C24ECF88 00000002
{amount} 7C060378
60000000 00000000
E2000001 80008000
'''

def initialCoinsMod6(hex, hexDec):
    return f'''
MP6 - Gain {hexDec} Coins at the Start of the Game
C214B3AC 00000001
3880{hex} 00000000
'''

def getBattleGame6(p1, p2, p3, p4, p5, s1, s2, s3, s4, s5):
    return f'''
MP6 - Battle Minigames Bounties are {s1}, {s2}, {s3}, {s4}, and {s5}
0424BAB0 0000{p1}
0424BAB4 0000{p2}
0424BAB8 0000{p3}
0424BABC 0000{p4}
0424BAC0 0000{p5}
'''

def getZapOrb6(hex, amountDec):
    return f'''
MP6 - Zap Takes {amountDec} Coins
C21AE1B8 00000001
3B60{hex} 00000000
'''

def getFaireFlowerEventStars(value):
    return f'''
MP6 - Always Wager Stars at Faire Square Flower Event
282C0256 0000007D
C24D3C68 00000001
38E00001 00000000
C24D4E34 00000001
38000001 00000000
C24D3C68 00000001
38E00001 00000000
E2000001 80008000
'''

def getFaireFlowerEventCoins(value):
    return f'''
MP6 - Always Wager Coins at Faire Square Flower Event
282C0256 0000007D
C24D3C70 00000001
60000000 00000000
C24D4E3C 00000001
60000000 00000000
C24D3C70 00000001
60000000 00000000
E2000001 80008000
'''