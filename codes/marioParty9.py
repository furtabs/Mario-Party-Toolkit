# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

def getMinigameReplacement9(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP9 - Minigame Replacement: {gameUno} -> {gameDos}
4A000000 81000000
30758730 {hexUno}00
14758730 {hexDos}00
E0000000 80008000
'''