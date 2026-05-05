# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty6 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp6DX(mushroomCapsuleShopOdds12 = "0", mushroomCapsuleShopOdds34 = "0", mushroomCapsuleSpaceOdds1 = "0", mushroomCapsuleSpaceOdds2 = "0", mushroomCapsuleSpaceOdds34 = "0", goldenMushroomCapsulePrice1 = "0", goldenMushroomCapsulePrice2 = "0", goldenMushroomCapsulePrice34 = "0", goldenMushroomCapsuleShopOdds12 = "0", goldenMushroomCapsuleShopOdds34 = "0", goldenMushroomCapsuleSpaceOdds1 = "0", goldenMushroomCapsuleSpaceOdds2 = "0", goldenMushroomCapsuleSpaceOdds34 = "0", slowMushroomCapsulePrice1 = "0", slowMushroomCapsulePrice2 = "0", slowMushroomCapsulePrice34 = "0", slowMushroomCapsuleShopOdds12 = "0", slowMushroomCapsuleShopOdds34 = "0", slowMushroomCapsuleSpaceOdds1 = "0", slowMushroomCapsuleSpaceOdds2 = "0", slowMushroomCapsuleSpaceOdds34 = "0", metalMushroomCapsulePrice1 = "0", metalMushroomCapsulePrice2 = "0", metalMushroomCapsulePrice34 = "0", metalMushroomCapsuleShopOdds12 = "0", metalMushroomCapsuleShopOdds34 = "0", metalMushroomCapsuleSpaceOdds1 = "0", metalMushroomCapsuleSpaceOdds2 = "0", metalMushroomCapsuleSpaceOdds34 = "0", flutterCapsulePrice1 = "0", flutterCapsulePrice2 = "0", flutterCapsulePrice34 = "0", flutterCapsuleShopOdds12 = "0", flutterCapsuleShopOdds34 = "0", flutterCapsuleSpaceOdds1 = "0", flutterCapsuleSpaceOdds2 = "0", flutterCapsuleSpaceOdds34 = "0", cannonCapsulePrice1 = "0", cannonCapsulePrice2 = "0", cannonCapsulePrice34 = "0", cannonCapsuleShopOdds12 = "0", cannonCapsuleShopOdds34 = "0", cannonCapsuleSpaceOdds1 = "0", cannonCapsuleSpaceOdds2 = "0", cannonCapsuleSpaceOdds34 = "0", snackCapsulePrice1 = "0", snackCapsulePrice2 = "0", snackCapsulePrice34 = "0", snackCapsuleShopOdds12 = "0", snackCapsuleShopOdds34 = "0", snackCapsuleSpaceOdds1 = "0", snackCapsuleSpaceOdds2 = "0", snackCapsuleSpaceOdds34 = "0", goombaCapsulePrice1 = "0", goombaCapsulePrice2 = "0", goombaCapsulePrice34 = "0", goombaCapsuleShopOdds12 = "0", goombaCapsuleShopOdds34 = "0", goombaCapsuleSpaceOdds1 = "0", goombaCapsuleSpaceOdds2 = "0", goombaCapsuleSpaceOdds34 = "0", hammerBroCapsulePrice1 = "0", hammerBroCapsulePrice2 = "0", hammerBroCapsulePrice34 = "0", hammerBroCapsuleShopOdds12 = "0", hammerBroCapsuleShopOdds34 = "0", hammerBroCapsuleSpaceOdds1 = "0", hammerBroCapsuleSpaceOdds2 = "0", hammerBroCapsuleSpaceOdds34 = "0", piranhaPlantCapsulePrice1 = "0", piranhaPlantCapsulePrice2 = "0", piranhaPlantCapsulePrice34 = "0", piranhaPlantCapsuleShopOdds12 = "0", piranhaPlantCapsuleShopOdds34 = "0", piranhaPlantCapsuleSpaceOdds1 = "0", piranhaPlantCapsuleSpaceOdds2 = "0", piranhaPlantCapsuleSpaceOdds34 = "0", kleptoCapsulePrice1 = "0", kleptoCapsulePrice2 = "0", kleptoCapsulePrice34 = "0", kleptoCapsuleShopOdds12 = "0", kleptoCapsuleShopOdds34 = "0", kleptoCapsuleSpaceOdds1 = "0", kleptoCapsuleSpaceOdds2 = "0", kleptoCapsuleSpaceOdds34 = "0", kamekCapsulePrice1 = "0", kamekCapsulePrice2 = "0", kamekCapsulePrice34 = "0", kamekCapsuleShopOdds12 = "0", kamekCapsuleShopOdds34 = "0", kamekCapsuleSpaceOdds1 = "0", kamekCapsuleSpaceOdds2 = "0", kamekCapsuleSpaceOdds34 = "0", toadyCapsulePrice1 = "0", toadyCapsulePrice2 = "0", toadyCapsulePrice34 = "0", toadyCapsuleShopOdds12 = "0", toadyCapsuleShopOdds34 = "0", toadyCapsuleSpaceOdds1 = "0", toadyCapsuleSpaceOdds2 = "0", toadyCapsuleSpaceOdds34 = "0", mrBlizzardCapsulePrice1 = "0", mrBlizzardCapsulePrice2 = "0", mrBlizzardCapsulePrice34 = "0", mrBlizzardCapsuleShopOdds12 = "0", mrBlizzardCapsuleShopOdds34 = "0", mrBlizzardCapsuleSpaceOdds1 = "0", mrBlizzardCapsuleSpaceOdds2 = "0", mrBlizzardCapsuleSpaceOdds34 = "0", banditCapsulePrice1 = "0", banditCapsulePrice2 = "0", banditCapsulePrice34 = "0", banditCapsuleShopOdds12 = "0", banditCapsuleShopOdds34 = "0", banditCapsuleSpaceOdds1 = "0", banditCapsuleSpaceOdds2 = "0", banditCapsuleSpaceOdds34 = "0", pinkBooCapsulePrice1 = "0", pinkBooCapsulePrice2 = "0", pinkBooCapsulePrice34 = "0", pinkBooCapsuleShopOdds12 = "0", pinkBooCapsuleShopOdds34 = "0", pinkBooCapsuleSpaceOdds1 = "0", pinkBooCapsuleSpaceOdds2 = "0", pinkBooCapsuleSpaceOdds34 = "0", spinyCapsulePrice1 = "0", spinyCapsulePrice2 = "0", spinyCapsulePrice34 = "0", spinyCapsuleShopOdds12 = "0", spinyCapsuleShopOdds34 = "0", spinyCapsuleSpaceOdds1 = "0", spinyCapsuleSpaceOdds2 = "0", spinyCapsuleSpaceOdds34 = "0", podobooCapsulePrice1 = "0", podobooCapsulePrice2 = "0", podobooCapsulePrice34 = "0", podobooCapsuleShopOdds12 = "0", podobooCapsuleShopOdds34 = "0", podobooCapsuleSpaceOdds1 = "0", podobooCapsuleSpaceOdds2 = "0", podobooCapsuleSpaceOdds34 = "0", tweesterCapsulePrice1 = "0", tweesterCapsulePrice2 = "0", tweesterCapsulePrice34 = "0", tweesterCapsuleShopOdds12 = "0", tweesterCapsuleShopOdds34 = "0", tweesterCapsuleSpaceOdds1 = "0", tweesterCapsuleSpaceOdds2 = "0", tweesterCapsuleSpaceOdds34 = "0", thwompCapsulePrice1 = "0", thwompCapsulePrice2 = "0", thwompCapsulePrice34 = "0", thwompCapsuleShopOdds12 = "0", thwompCapsuleShopOdds34 = "0", thwompCapsuleSpaceOdds1 = "0", thwompCapsuleSpaceOdds2 = "0", thwompCapsuleSpaceOdds34 = "0", warpCapsulePrice1 = "0", warpCapsulePrice2 = "0", warpCapsulePrice34 = "0", warpCapsuleShopOdds12 = "0", warpCapsuleShopOdds34 = "0", warpCapsuleSpaceOdds1 = "0", warpCapsuleSpaceOdds2 = "0", warpCapsuleSpaceOdds34 = "0", bombCapsulePrice1 = "0", bombCapsulePrice2 = "0", bombCapsulePrice34 = "0", bombCapsuleShopOdds12 = "0", bombCapsuleShopOdds34 = "0", bombCapsuleSpaceOdds1 = "0", bombCapsuleSpaceOdds2 = "0", bombCapsuleSpaceOdds34 = "0", fireballCapsulePrice1 = "0", fireballCapsulePrice2 = "0", fireballCapsulePrice34 = "0", fireballCapsuleShopOdds12 = "0", fireballCapsuleShopOdds34 = "0", fireballCapsuleSpaceOdds1 = "0", fireballCapsuleSpaceOdds2 = "0", fireballCapsuleSpaceOdds34 = "0", paraTroopaCapsulePrice1 = "0", paraTroopaCapsulePrice2 = "0", paraTroopaCapsulePrice34 = "0", paraTroopaCapsuleShopOdds12 = "0", paraTroopaCapsuleShopOdds34 = "0", paraTroopaCapsuleSpaceOdds1 = "0", paraTroopaCapsuleSpaceOdds2 = "0", paraTroopaCapsuleSpaceOdds34 = "0", eggCapsulePrice1 = "0", eggCapsulePrice2 = "0", eggCapsulePrice34 = "0", eggCapsuleShopOdds12 = "0", eggCapsuleShopOdds34 = "0", eggCapsuleSpaceOdds1 = "0", eggCapsuleSpaceOdds2 = "0", eggCapsuleSpaceOdds34 = "0", vacuumCapsulePrice1 = "0", vacuumCapsulePrice2 = "0", vacuumCapsulePrice34 = "0", vacuumCapsuleShopOdds12 = "0", vacuumCapsuleShopOdds34 = "0", vacuumCapsuleSpaceOdds1 = "0", vacuumCapsuleSpaceOdds2 = "0", vacuumCapsuleSpaceOdds34 = "0", magicCapsulePrice1 = "0", magicCapsulePrice2 = "0", magicCapsulePrice34 = "0", magicCapsuleShopOdds12 = "0", magicCapsuleShopOdds34 = "0", magicCapsuleSpaceOdds1 = "0", magicCapsuleSpaceOdds2 = "0", magicCapsuleSpaceOdds34 = "0", tripleCapsulePrice1 = "0", tripleCapsulePrice2 = "0", tripleCapsulePrice34 = "0", tripleCapsuleShopOdds12 = "0", tripleCapsuleShopOdds34 = "0", tripleCapsuleSpaceOdds1 = "0", tripleCapsuleSpaceOdds2 = "0", tripleCapsuleSpaceOdds34 = "0", koopaCapsulePrice1 = "0", koopaCapsulePrice2 = "0", koopaCapsulePrice34 = "0", koopaCapsuleShopOdds12 = "0", koopaCapsuleShopOdds34 = "0", koopaCapsuleSpaceOdds1 = "0", koopaCapsuleSpaceOdds2 = "0", koopaCapsuleSpaceOdds34 = "0", cursedMushroomPrice1 = "0", cursedMushroomPrice2 = "0", cursedMushroomPrice34 = "0", cursedMushroomShopOdds12 = "0", cursedMushroomShopOdds34 = "0", cursedMushroomSpaceOdds1 = "0", cursedMushroomSpaceOdds2 = "0", cursedMushroomSpaceOdds34 = "0", orbBagCapsulePrice1 = "0", orbBagCapsulePrice2 = "0", orbBagCapsulePrice34 = "0", orbBagCapsuleShopOdds12 = "0", orbBagCapsuleShopOdds34 = "0", orbBagCapsuleSpaceOdds1 = "0", orbBagCapsuleSpaceOdds2 = "0", orbBagCapsuleSpaceOdds34 = "0", mysteryCapsulePrice1 = "0", mysteryCapsulePrice2 = "0", mysteryCapsulePrice34 = "0", mysteryCapsuleShopOdds12 = "0", mysteryCapsuleShopOdds34 = "0", mysteryCapsuleSpaceOdds1 = "0", mysteryCapsuleSpaceOdds2 = "0", mysteryCapsuleSpaceOdds34 = "0", dkCapsulePrice1 = "0", dkCapsulePrice2 = "0", dkCapsulePrice34 = "0", dkCapsuleShopOdds12 = "0", dkCapsuleShopOdds34 = "0", dkCapsuleSpaceOdds1 = "0", dkCapsuleSpaceOdds2 = "0", dkCapsuleSpaceOdds34 = "0", duelCapsulePrice1 = "0", duelCapsulePrice2 = "0", duelCapsulePrice34 = "0", duelCapsuleShopOdds12 = "0", duelCapsuleShopOdds34 = "0", duelCapsuleSpaceOdds1 = "0", duelCapsuleSpaceOdds2 = "0", duelCapsuleSpaceOdds34 = "0", DxCapsuleDuelPrice1 = "0", DxCapsuleDuelPrice2 = "0", DxCapsuleDuelPrice34 = "0", DxCapsuleDuelShopOdds12 = "0", DxCapsuleDuelShopOdds34 = "0", DxCapsuleDuelSpaceOdds1 = "0", DxCapsuleDuelSpaceOdds2 = "0", DxCapsuleDuelSpaceOdds34 = "0", DxCapsuleChancePrice1 = "0", DxCapsuleChancePrice2 = "0", DxCapsuleChancePrice34 = "0", DxCapsuleChanceShopOdds12 = "0", DxCapsuleChanceShopOdds34 = "0", DxCapsuleChanceSpaceOdds1 = "0", DxCapsuleChanceSpaceOdds2 = "0", DxCapsuleChanceSpaceOdds34 = "0", DxCapsuleBowserPrice1 = "0", DxCapsuleBowserPrice2 = "0", DxCapsuleBowserPrice34 = "0", DxCapsuleBowserShopOdds12 = "0", DxCapsuleBowserShopOdds34 = "0", DxCapsuleBowserSpaceOdds1 = "0", DxCapsuleBowserSpaceOdds2 = "0", DxCapsuleBowserSpaceOdds34 = "0",DxCapsuleDonkeyKongPrice1 = "0", DxCapsuleDonkeyKongPrice2 = "0", DxCapsuleDonkeyKongPrice34 = "0", DxCapsuleDonkeyKongShopOdds12 = "0", DxCapsuleDonkeyKongShopOdds34 = "0", DxCapsuleDonkeyKongSpaceOdds1 = "0", DxCapsuleDonkeyKongSpaceOdds2 = "0", DxCapsuleDonkeyKongSpaceOdds34 = "0", DxCapsulePinkBooPrice1 = "0", DxCapsulePinkBooPrice2 = "0", DxCapsulePinkBooPrice34 = "0", DxCapsulePinkBooShopOdds12 = "0", DxCapsulePinkBooShopOdds34 = "0", DxCapsulePinkBooSpaceOdds1 = "0", DxCapsulePinkBooSpaceOdds2 = "0", DxCapsulePinkBooSpaceOdds34 = "0", DxCapsuleSolunaPrice1 = "0", DxCapsuleSolunaPrice2 = "0", DxCapsuleSolunaPrice34 = "0", DxCapsuleSolunaShopOdds12 = "0", DxCapsuleSolunaShopOdds34 = "0", DxCapsuleSolunaSpaceOdds1 = "0", DxCapsuleSolunaSpaceOdds2 = "0", DxCapsuleSolunaSpaceOdds34 = "0", DxCapsuleChainChompPrice1 = "0", DxCapsuleChainChompPrice2 = "0", DxCapsuleChainChompPrice34 = "0", DxCapsuleChainChompShopOdds12 = "0", DxCapsuleChainChompShopOdds34 = "0", DxCapsuleChainChompSpaceOdds1 = "0", DxCapsuleChainChompSpaceOdds2 = "0", DxCapsuleChainChompSpaceOdds34 = "0", DxCapsuleWackyWatchPrice1 = "0", DxCapsuleWackyWatchPrice2 = "0", DxCapsuleWackyWatchPrice34 = "0", DxCapsuleWackyWatchShopOdds12 = "0", DxCapsuleWackyWatchShopOdds34 = "0", DxCapsuleWackyWatchSpaceOdds1 = "0", DxCapsuleWackyWatchSpaceOdds2 = "0", DxCapsuleWackyWatchSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            # Handle string values from UI
            if isinstance(capsule, str):
                return int(capsule) if capsule else 0
            # Handle Tkinter widget values
            return capsule.get()
        except:
            return 0

    mushroomCapsuleShopOdds12 = get_capsule_value(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = get_capsule_value(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = get_capsule_value(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = get_capsule_value(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = get_capsule_value(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsulePrice1 = get_capsule_value(goldenMushroomCapsulePrice1)
    goldenMushroomCapsulePrice2 = get_capsule_value(goldenMushroomCapsulePrice2)
    goldenMushroomCapsulePrice34 = get_capsule_value(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = get_capsule_value(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = get_capsule_value(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = get_capsule_value(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = get_capsule_value(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = get_capsule_value(goldenMushroomCapsuleSpaceOdds34)


    slowMushroomCapsulePrice1 = get_capsule_value(slowMushroomCapsulePrice1)
    slowMushroomCapsulePrice2 = get_capsule_value(slowMushroomCapsulePrice2)
    slowMushroomCapsulePrice34 = get_capsule_value(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = get_capsule_value(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = get_capsule_value(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = get_capsule_value(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = get_capsule_value(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = get_capsule_value(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsulePrice1 = get_capsule_value(metalMushroomCapsulePrice1)
    metalMushroomCapsulePrice2 = get_capsule_value(metalMushroomCapsulePrice2)
    metalMushroomCapsulePrice34 = get_capsule_value(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = get_capsule_value(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = get_capsule_value(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = get_capsule_value(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = get_capsule_value(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = get_capsule_value(metalMushroomCapsuleSpaceOdds34)

    flutterCapsulePrice1 = get_capsule_value(flutterCapsulePrice1)
    flutterCapsulePrice2 = get_capsule_value(flutterCapsulePrice2)
    flutterCapsulePrice34 = get_capsule_value(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = get_capsule_value(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = get_capsule_value(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = get_capsule_value(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = get_capsule_value(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = get_capsule_value(flutterCapsuleSpaceOdds34)

    cannonCapsulePrice1 = get_capsule_value(cannonCapsulePrice1)
    cannonCapsulePrice2 = get_capsule_value(cannonCapsulePrice2)
    cannonCapsulePrice34 = get_capsule_value(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = get_capsule_value(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = get_capsule_value(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = get_capsule_value(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = get_capsule_value(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = get_capsule_value(cannonCapsuleSpaceOdds34)

    snackCapsulePrice1 = get_capsule_value(snackCapsulePrice1)
    snackCapsulePrice2 = get_capsule_value(snackCapsulePrice2)
    snackCapsulePrice34 = get_capsule_value(snackCapsulePrice34)
    snackCapsuleShopOdds12 = get_capsule_value(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = get_capsule_value(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = get_capsule_value(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = get_capsule_value(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = get_capsule_value(snackCapsuleSpaceOdds34)

    goombaCapsulePrice1 = get_capsule_value(goombaCapsulePrice1)
    goombaCapsulePrice2 = get_capsule_value(goombaCapsulePrice2)
    goombaCapsulePrice34 = get_capsule_value(goombaCapsulePrice34)
    goombaCapsuleShopOdds12 = get_capsule_value(goombaCapsuleShopOdds12)
    goombaCapsuleShopOdds34 = get_capsule_value(goombaCapsuleShopOdds34)
    goombaCapsuleSpaceOdds1 = get_capsule_value(goombaCapsuleSpaceOdds1)
    goombaCapsuleSpaceOdds2 = get_capsule_value(goombaCapsuleSpaceOdds2)
    goombaCapsuleSpaceOdds34 = get_capsule_value(goombaCapsuleSpaceOdds34)

    hammerBroCapsulePrice1 = get_capsule_value(hammerBroCapsulePrice1)
    hammerBroCapsulePrice2 = get_capsule_value(hammerBroCapsulePrice2)
    hammerBroCapsulePrice34 = get_capsule_value(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = get_capsule_value(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = get_capsule_value(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = get_capsule_value(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = get_capsule_value(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = get_capsule_value(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsulePrice1 = get_capsule_value(piranhaPlantCapsulePrice1)
    piranhaPlantCapsulePrice2 = get_capsule_value(piranhaPlantCapsulePrice2)
    piranhaPlantCapsulePrice34 = get_capsule_value(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = get_capsule_value(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = get_capsule_value(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = get_capsule_value(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = get_capsule_value(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = get_capsule_value(piranhaPlantCapsuleSpaceOdds34)

    kleptoCapsulePrice1 = get_capsule_value(kleptoCapsulePrice1)
    kleptoCapsulePrice2 = get_capsule_value(kleptoCapsulePrice2)
    kleptoCapsulePrice34 = get_capsule_value(kleptoCapsulePrice34)
    kleptoCapsuleShopOdds12 = get_capsule_value(kleptoCapsuleShopOdds12)
    kleptoCapsuleShopOdds34 = get_capsule_value(kleptoCapsuleShopOdds34)
    kleptoCapsuleSpaceOdds1 = get_capsule_value(kleptoCapsuleSpaceOdds1)
    kleptoCapsuleSpaceOdds2 = get_capsule_value(kleptoCapsuleSpaceOdds2)
    kleptoCapsuleSpaceOdds34 = get_capsule_value(kleptoCapsuleSpaceOdds34)

    kamekCapsulePrice1 = get_capsule_value(kamekCapsulePrice1)
    kamekCapsulePrice2 = get_capsule_value(kamekCapsulePrice2)
    kamekCapsulePrice34 = get_capsule_value(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = get_capsule_value(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = get_capsule_value(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = get_capsule_value(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = get_capsule_value(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = get_capsule_value(kamekCapsuleSpaceOdds34)

    toadyCapsulePrice1 = get_capsule_value(toadyCapsulePrice1)
    toadyCapsulePrice2 = get_capsule_value(toadyCapsulePrice2)
    toadyCapsulePrice34 = get_capsule_value(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = get_capsule_value(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = get_capsule_value(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = get_capsule_value(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = get_capsule_value(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = get_capsule_value(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsulePrice1 = get_capsule_value(mrBlizzardCapsulePrice1)
    mrBlizzardCapsulePrice2 = get_capsule_value(mrBlizzardCapsulePrice2)
    mrBlizzardCapsulePrice34 = get_capsule_value(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = get_capsule_value(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = get_capsule_value(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = get_capsule_value(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = get_capsule_value(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = get_capsule_value(mrBlizzardCapsuleSpaceOdds34)

    banditCapsulePrice1 = get_capsule_value(banditCapsulePrice1)
    banditCapsulePrice2 = get_capsule_value(banditCapsulePrice2)
    banditCapsulePrice34 = get_capsule_value(banditCapsulePrice34)
    banditCapsuleShopOdds12 = get_capsule_value(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = get_capsule_value(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = get_capsule_value(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = get_capsule_value(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = get_capsule_value(banditCapsuleSpaceOdds34)

    pinkBooCapsulePrice1 = get_capsule_value(pinkBooCapsulePrice1)
    pinkBooCapsulePrice2 = get_capsule_value(pinkBooCapsulePrice2)
    pinkBooCapsulePrice34 = get_capsule_value(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = get_capsule_value(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = get_capsule_value(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = get_capsule_value(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = get_capsule_value(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = get_capsule_value(pinkBooCapsuleSpaceOdds34)

    spinyCapsulePrice1 = get_capsule_value(spinyCapsulePrice1)
    spinyCapsulePrice2 = get_capsule_value(spinyCapsulePrice2)
    spinyCapsulePrice34 = get_capsule_value(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = get_capsule_value(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = get_capsule_value(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = get_capsule_value(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = get_capsule_value(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = get_capsule_value(spinyCapsuleSpaceOdds34)

    podobooCapsulePrice1 = get_capsule_value(podobooCapsulePrice1)
    podobooCapsulePrice2 = get_capsule_value(podobooCapsulePrice2)
    podobooCapsulePrice34 = get_capsule_value(podobooCapsulePrice34)
    podobooCapsuleShopOdds12 = get_capsule_value(podobooCapsuleShopOdds12)
    podobooCapsuleShopOdds34 = get_capsule_value(podobooCapsuleShopOdds34)
    podobooCapsuleSpaceOdds1 = get_capsule_value(podobooCapsuleSpaceOdds1)
    podobooCapsuleSpaceOdds2 = get_capsule_value(podobooCapsuleSpaceOdds2)
    podobooCapsuleSpaceOdds34 = get_capsule_value(podobooCapsuleSpaceOdds34)

    tweesterCapsulePrice1 = get_capsule_value(tweesterCapsulePrice1)
    tweesterCapsulePrice2 = get_capsule_value(tweesterCapsulePrice2)
    tweesterCapsulePrice34 = get_capsule_value(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = get_capsule_value(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = get_capsule_value(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = get_capsule_value(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = get_capsule_value(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = get_capsule_value(tweesterCapsuleSpaceOdds34)

    thwompCapsulePrice1 = get_capsule_value(thwompCapsulePrice1)
    thwompCapsulePrice2 = get_capsule_value(thwompCapsulePrice2)
    thwompCapsulePrice34 = get_capsule_value(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = get_capsule_value(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = get_capsule_value(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = get_capsule_value(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = get_capsule_value(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = get_capsule_value(thwompCapsuleSpaceOdds34)

    warpCapsulePrice1 = get_capsule_value(warpCapsulePrice1)
    warpCapsulePrice2 = get_capsule_value(warpCapsulePrice2)
    warpCapsulePrice34 = get_capsule_value(warpCapsulePrice34)
    warpCapsuleShopOdds12 = get_capsule_value(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = get_capsule_value(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = get_capsule_value(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = get_capsule_value(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = get_capsule_value(warpCapsuleSpaceOdds34)

    bombCapsulePrice1 = get_capsule_value(bombCapsulePrice1)
    bombCapsulePrice2 = get_capsule_value(bombCapsulePrice2)
    bombCapsulePrice34 = get_capsule_value(bombCapsulePrice34)
    bombCapsuleShopOdds12 = get_capsule_value(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = get_capsule_value(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = get_capsule_value(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = get_capsule_value(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = get_capsule_value(bombCapsuleSpaceOdds34)

    fireballCapsulePrice1 = get_capsule_value(fireballCapsulePrice1)
    fireballCapsulePrice2 = get_capsule_value(fireballCapsulePrice2)
    fireballCapsulePrice34 = get_capsule_value(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = get_capsule_value(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = get_capsule_value(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = get_capsule_value(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = get_capsule_value(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = get_capsule_value(fireballCapsuleSpaceOdds34)

    paraTroopaCapsulePrice1 = get_capsule_value(paraTroopaCapsulePrice1)
    paraTroopaCapsulePrice2 = get_capsule_value(paraTroopaCapsulePrice2)
    paraTroopaCapsulePrice34 = get_capsule_value(paraTroopaCapsulePrice34)
    paraTroopaCapsuleShopOdds12 = get_capsule_value(paraTroopaCapsuleShopOdds12)
    paraTroopaCapsuleShopOdds34 = get_capsule_value(paraTroopaCapsuleShopOdds34)
    paraTroopaCapsuleSpaceOdds1 = get_capsule_value(paraTroopaCapsuleSpaceOdds1)
    paraTroopaCapsuleSpaceOdds2 = get_capsule_value(paraTroopaCapsuleSpaceOdds2)
    paraTroopaCapsuleSpaceOdds34 = get_capsule_value(paraTroopaCapsuleSpaceOdds34)

    eggCapsulePrice1 = get_capsule_value(eggCapsulePrice1)
    eggCapsulePrice2 = get_capsule_value(eggCapsulePrice2)
    eggCapsulePrice34 = get_capsule_value(eggCapsulePrice34)
    eggCapsuleShopOdds12 = get_capsule_value(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = get_capsule_value(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = get_capsule_value(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = get_capsule_value(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = get_capsule_value(eggCapsuleSpaceOdds34)

    vacuumCapsulePrice1 = get_capsule_value(vacuumCapsulePrice1)
    vacuumCapsulePrice2 = get_capsule_value(vacuumCapsulePrice2)
    vacuumCapsulePrice34 = get_capsule_value(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = get_capsule_value(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = get_capsule_value(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = get_capsule_value(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = get_capsule_value(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = get_capsule_value(vacuumCapsuleSpaceOdds34)

    magicCapsulePrice1 = get_capsule_value(magicCapsulePrice1)
    magicCapsulePrice2 = get_capsule_value(magicCapsulePrice2)
    magicCapsulePrice34 = get_capsule_value(magicCapsulePrice34)
    magicCapsuleShopOdds12 = get_capsule_value(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = get_capsule_value(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = get_capsule_value(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = get_capsule_value(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = get_capsule_value(magicCapsuleSpaceOdds34)

    tripleCapsulePrice1 = get_capsule_value(tripleCapsulePrice1)
    tripleCapsulePrice2 = get_capsule_value(tripleCapsulePrice2)
    tripleCapsulePrice34 = get_capsule_value(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = get_capsule_value(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = get_capsule_value(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = get_capsule_value(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = get_capsule_value(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = get_capsule_value(tripleCapsuleSpaceOdds34)

    koopaCapsulePrice1 = get_capsule_value(koopaCapsulePrice1)
    koopaCapsulePrice2 = get_capsule_value(koopaCapsulePrice2)
    koopaCapsulePrice34 = get_capsule_value(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = get_capsule_value(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = get_capsule_value(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = get_capsule_value(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = get_capsule_value(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = get_capsule_value(koopaCapsuleSpaceOdds34)

    cursedMushroomPrice1 = get_capsule_value(cursedMushroomPrice1)
    cursedMushroomPrice2 = get_capsule_value(cursedMushroomPrice2)
    cursedMushroomPrice34 = get_capsule_value(cursedMushroomPrice34)
    cursedMushroomShopOdds12 = get_capsule_value(cursedMushroomShopOdds12)
    cursedMushroomShopOdds34 = get_capsule_value(cursedMushroomShopOdds34)
    cursedMushroomSpaceOdds1 = get_capsule_value(cursedMushroomSpaceOdds1)
    cursedMushroomSpaceOdds2 = get_capsule_value(cursedMushroomSpaceOdds2)
    cursedMushroomSpaceOdds34 = get_capsule_value(cursedMushroomSpaceOdds34)

    orbBagCapsulePrice1 = get_capsule_value(orbBagCapsulePrice1)
    orbBagCapsulePrice2 = get_capsule_value(orbBagCapsulePrice2)
    orbBagCapsulePrice34 = get_capsule_value(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = get_capsule_value(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = get_capsule_value(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = get_capsule_value(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = get_capsule_value(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = get_capsule_value(orbBagCapsuleSpaceOdds34)

    mysteryCapsulePrice1 = get_capsule_value(mysteryCapsulePrice1)
    mysteryCapsulePrice2 = get_capsule_value(mysteryCapsulePrice2)
    mysteryCapsulePrice34 = get_capsule_value(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = get_capsule_value(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = get_capsule_value(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = get_capsule_value(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = get_capsule_value(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = get_capsule_value(mysteryCapsuleSpaceOdds34)

    dkCapsulePrice1 = get_capsule_value(dkCapsulePrice1)
    dkCapsulePrice2 = get_capsule_value(dkCapsulePrice2)
    dkCapsulePrice34 = get_capsule_value(dkCapsulePrice34)
    dkCapsuleShopOdds12 = get_capsule_value(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = get_capsule_value(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = get_capsule_value(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = get_capsule_value(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = get_capsule_value(dkCapsuleSpaceOdds34)

    duelCapsulePrice1 = get_capsule_value(duelCapsulePrice1)
    duelCapsulePrice2 = get_capsule_value(duelCapsulePrice2)
    duelCapsulePrice34 = get_capsule_value(duelCapsulePrice34)
    duelCapsuleShopOdds12 = get_capsule_value(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = get_capsule_value(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = get_capsule_value(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = get_capsule_value(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = get_capsule_value(duelCapsuleSpaceOdds34)

    DxCapsuleDuelPrice1 = get_capsule_value(DxCapsuleDuelPrice1)
    DxCapsuleDuelPrice2 = get_capsule_value(DxCapsuleDuelPrice2)
    DxCapsuleDuelPrice34 = get_capsule_value(DxCapsuleDuelPrice34)
    DxCapsuleDuelShopOdds12 = get_capsule_value(DxCapsuleDuelShopOdds12)
    DxCapsuleDuelShopOdds34 = get_capsule_value(DxCapsuleDuelShopOdds34)
    DxCapsuleDuelSpaceOdds1 = get_capsule_value(DxCapsuleDuelSpaceOdds1)
    DxCapsuleDuelSpaceOdds2 = get_capsule_value(DxCapsuleDuelSpaceOdds2)
    DxCapsuleDuelSpaceOdds34 = get_capsule_value(DxCapsuleDuelSpaceOdds34)

    DxCapsuleChancePrice1 = get_capsule_value(DxCapsuleChancePrice1)
    DxCapsuleChancePrice2 = get_capsule_value(DxCapsuleChancePrice2)
    DxCapsuleChancePrice34 = get_capsule_value(DxCapsuleChancePrice34)
    DxCapsuleChanceShopOdds12 = get_capsule_value(DxCapsuleChanceShopOdds12)
    DxCapsuleChanceShopOdds34 = get_capsule_value(DxCapsuleChanceShopOdds34)
    DxCapsuleChanceSpaceOdds1 = get_capsule_value(DxCapsuleChanceSpaceOdds1)
    DxCapsuleChanceSpaceOdds2 = get_capsule_value(DxCapsuleChanceSpaceOdds2)
    DxCapsuleChanceSpaceOdds34 = get_capsule_value(DxCapsuleChanceSpaceOdds34)

    DxCapsuleBowserPrice1 = get_capsule_value(DxCapsuleBowserPrice1)
    DxCapsuleBowserPrice2 = get_capsule_value(DxCapsuleBowserPrice2)
    DxCapsuleBowserPrice34 = get_capsule_value(DxCapsuleBowserPrice34)
    DxCapsuleBowserShopOdds12 = get_capsule_value(DxCapsuleBowserShopOdds12)
    DxCapsuleBowserShopOdds34 = get_capsule_value(DxCapsuleBowserShopOdds34)
    DxCapsuleBowserSpaceOdds1 = get_capsule_value(DxCapsuleBowserSpaceOdds1)
    DxCapsuleBowserSpaceOdds2 = get_capsule_value(DxCapsuleBowserSpaceOdds2)
    DxCapsuleBowserSpaceOdds34 = get_capsule_value(DxCapsuleBowserSpaceOdds34)

    DxCapsuleDonkeyKongPrice1 = get_capsule_value(DxCapsuleDonkeyKongPrice1)
    DxCapsuleDonkeyKongPrice2 = get_capsule_value(DxCapsuleDonkeyKongPrice2)
    DxCapsuleDonkeyKongPrice34 = get_capsule_value(DxCapsuleDonkeyKongPrice34)
    DxCapsuleDonkeyKongShopOdds12 = get_capsule_value(DxCapsuleDonkeyKongShopOdds12)
    DxCapsuleDonkeyKongShopOdds34 = get_capsule_value(DxCapsuleDonkeyKongShopOdds34)
    DxCapsuleDonkeyKongSpaceOdds1 = get_capsule_value(DxCapsuleDonkeyKongSpaceOdds1)
    DxCapsuleDonkeyKongSpaceOdds2 = get_capsule_value(DxCapsuleDonkeyKongSpaceOdds2)
    DxCapsuleDonkeyKongSpaceOdds34 = get_capsule_value(DxCapsuleDonkeyKongSpaceOdds34)

    DxCapsulePinkBooPrice1 = get_capsule_value(DxCapsulePinkBooPrice1)
    DxCapsulePinkBooPrice2 = get_capsule_value(DxCapsulePinkBooPrice2)
    DxCapsulePinkBooPrice34 = get_capsule_value(DxCapsulePinkBooPrice34)
    DxCapsulePinkBooShopOdds12 = get_capsule_value(DxCapsulePinkBooShopOdds12)
    DxCapsulePinkBooShopOdds34 = get_capsule_value(DxCapsulePinkBooShopOdds34)
    DxCapsulePinkBooSpaceOdds1 = get_capsule_value(DxCapsulePinkBooSpaceOdds1)
    DxCapsulePinkBooSpaceOdds2 = get_capsule_value(DxCapsulePinkBooSpaceOdds2)
    DxCapsulePinkBooSpaceOdds34 = get_capsule_value(DxCapsulePinkBooSpaceOdds34)

    DxCapsuleSolunaPrice1 = get_capsule_value(DxCapsuleSolunaPrice1)
    DxCapsuleSolunaPrice2 = get_capsule_value(DxCapsuleSolunaPrice2)
    DxCapsuleSolunaPrice34 = get_capsule_value(DxCapsuleSolunaPrice34)
    DxCapsuleSolunaShopOdds12 = get_capsule_value(DxCapsuleSolunaShopOdds12)
    DxCapsuleSolunaShopOdds34 = get_capsule_value(DxCapsuleSolunaShopOdds34)
    DxCapsuleSolunaSpaceOdds1 = get_capsule_value(DxCapsuleSolunaSpaceOdds1)
    DxCapsuleSolunaSpaceOdds2 = get_capsule_value(DxCapsuleSolunaSpaceOdds2)
    DxCapsuleSolunaSpaceOdds34 = get_capsule_value(DxCapsuleSolunaSpaceOdds34)

    DxCapsuleChainChompPrice1 = get_capsule_value(DxCapsuleChainChompPrice1)
    DxCapsuleChainChompPrice2 = get_capsule_value(DxCapsuleChainChompPrice2)
    DxCapsuleChainChompPrice34 = get_capsule_value(DxCapsuleChainChompPrice34)
    DxCapsuleChainChompShopOdds12 = get_capsule_value(DxCapsuleChainChompShopOdds12)
    DxCapsuleChainChompShopOdds34 = get_capsule_value(DxCapsuleChainChompShopOdds34)
    DxCapsuleChainChompSpaceOdds1 = get_capsule_value(DxCapsuleChainChompSpaceOdds1)
    DxCapsuleChainChompSpaceOdds2 = get_capsule_value(DxCapsuleChainChompSpaceOdds2)
    DxCapsuleChainChompSpaceOdds34 = get_capsule_value(DxCapsuleChainChompSpaceOdds34)

    DxCapsuleWackyWatchPrice1 = get_capsule_value(DxCapsuleWackyWatchPrice1)
    DxCapsuleWackyWatchPrice2 = get_capsule_value(DxCapsuleWackyWatchPrice2)
    DxCapsuleWackyWatchPrice34 = get_capsule_value(DxCapsuleWackyWatchPrice34)
    DxCapsuleWackyWatchShopOdds12 = get_capsule_value(DxCapsuleWackyWatchShopOdds12)
    DxCapsuleWackyWatchShopOdds34 = get_capsule_value(DxCapsuleWackyWatchShopOdds34)
    DxCapsuleWackyWatchSpaceOdds1 = get_capsule_value(DxCapsuleWackyWatchSpaceOdds1)
    DxCapsuleWackyWatchSpaceOdds2 = get_capsule_value(DxCapsuleWackyWatchSpaceOdds2)
    DxCapsuleWackyWatchSpaceOdds34 = get_capsule_value(DxCapsuleWackyWatchSpaceOdds34)
    
    # Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, goombaCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, kleptoCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, podobooCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, paraTroopaCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12,
        DxCapsuleDuelShopOdds12, DxCapsuleChanceShopOdds12, DxCapsuleBowserShopOdds12,
        DxCapsuleDonkeyKongShopOdds12, DxCapsulePinkBooShopOdds12, DxCapsuleSolunaShopOdds12, DxCapsuleChainChompShopOdds12,
        DxCapsuleWackyWatchShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, goombaCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, kleptoCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, podobooCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, paraTroopaCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34,
        DxCapsuleDuelShopOdds34, DxCapsuleChanceShopOdds34, DxCapsuleBowserShopOdds34,
        DxCapsuleDonkeyKongShopOdds34, DxCapsulePinkBooShopOdds34, DxCapsuleSolunaShopOdds34, DxCapsuleChainChompShopOdds34,
        DxCapsuleWackyWatchShopOdds34
    ]

    spaceOdds1 = [
        mushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds1,
        slowMushroomCapsuleSpaceOdds1, flutterCapsuleSpaceOdds1, cannonCapsuleSpaceOdds1,
        snackCapsuleSpaceOdds1, goombaCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds1,
        piranhaPlantCapsuleSpaceOdds1, kleptoCapsuleSpaceOdds1, kamekCapsuleSpaceOdds1,
        toadyCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds1, banditCapsuleSpaceOdds1,
        pinkBooCapsuleSpaceOdds1, spinyCapsuleSpaceOdds1, podobooCapsuleSpaceOdds1,
        tweesterCapsuleSpaceOdds1, thwompCapsuleSpaceOdds1, warpCapsuleSpaceOdds1,
        bombCapsuleSpaceOdds1, fireballCapsuleSpaceOdds1, paraTroopaCapsuleSpaceOdds1,
        eggCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds1, magicCapsuleSpaceOdds1,
        tripleCapsuleSpaceOdds1, koopaCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds1,
        duelCapsuleSpaceOdds1, dkCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds1,
        DxCapsuleDuelSpaceOdds1, DxCapsuleChanceSpaceOdds1, DxCapsuleBowserSpaceOdds1,
        DxCapsuleDonkeyKongSpaceOdds1, DxCapsulePinkBooSpaceOdds1, DxCapsuleSolunaSpaceOdds1, DxCapsuleChainChompSpaceOdds1,
        DxCapsuleWackyWatchSpaceOdds1
    ]

    spaceOdds2 = [
        mushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds2,
        slowMushroomCapsuleSpaceOdds2, flutterCapsuleSpaceOdds2, cannonCapsuleSpaceOdds2,
        snackCapsuleSpaceOdds2, goombaCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds2,
        piranhaPlantCapsuleSpaceOdds2, kleptoCapsuleSpaceOdds2, kamekCapsuleSpaceOdds2,
        toadyCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds2, banditCapsuleSpaceOdds2,
        pinkBooCapsuleSpaceOdds2, spinyCapsuleSpaceOdds2, podobooCapsuleSpaceOdds2,
        tweesterCapsuleSpaceOdds2, thwompCapsuleSpaceOdds2, warpCapsuleSpaceOdds2,
        bombCapsuleSpaceOdds2, fireballCapsuleSpaceOdds2, paraTroopaCapsuleSpaceOdds2,
        eggCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds2, magicCapsuleSpaceOdds2,
        tripleCapsuleSpaceOdds2, koopaCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds2,
        duelCapsuleSpaceOdds2, dkCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds2,
        DxCapsuleDuelSpaceOdds2, DxCapsuleChanceSpaceOdds2, DxCapsuleBowserSpaceOdds2,
        DxCapsuleDonkeyKongSpaceOdds2, DxCapsulePinkBooSpaceOdds2, DxCapsuleSolunaSpaceOdds2, DxCapsuleChainChompSpaceOdds2,
        DxCapsuleWackyWatchSpaceOdds2
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, goombaCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, kleptoCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, podobooCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, paraTroopaCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34,
        DxCapsuleDuelSpaceOdds34, DxCapsuleChanceSpaceOdds34, DxCapsuleBowserSpaceOdds34,
        DxCapsuleDonkeyKongSpaceOdds34, DxCapsulePinkBooSpaceOdds34, DxCapsuleSolunaSpaceOdds34, DxCapsuleChainChompSpaceOdds34,
        DxCapsuleWackyWatchSpaceOdds34
    ]

    def safe_int(val):
        try:
            return int(val) if val else 0
        except (ValueError, TypeError):
            return 0
    
    shopOdds12Weights = sum(safe_int(weight) for weight in shopOdds12)
    shopOdds34Weights = sum(safe_int(weight) for weight in shopOdds34)
    spaceOdds1Weights = sum(safe_int(weight) for weight in spaceOdds1)
    spaceOdds2Weights = sum(safe_int(weight) for weight in spaceOdds2)
    spaceOdds34Weights = sum(safe_int(weight) for weight in spaceOdds34)

    def calculateWeight(weight, total):
        try:
            weight = int(weight) if weight else 0
            if total < 100 and total > 0: # Added total > 0 to be safe
                return weight
            
            percentage = (weight / total) * 100
            return math.ceil(percentage) if 0 < percentage < 1 else round(percentage)
        except ZeroDivisionError:
            # This catches the division by zero and returns a safe default
            return 0

    # Calculate weights for shop odds 12
    mushroomCapsuleShopOdds12 = calculateWeight(mushroomCapsuleShopOdds12, shopOdds12Weights)
    goldenMushroomCapsuleShopOdds12 = calculateWeight(goldenMushroomCapsuleShopOdds12, shopOdds12Weights)
    metalMushroomCapsuleShopOdds12 = calculateWeight(metalMushroomCapsuleShopOdds12, shopOdds12Weights)
    slowMushroomCapsuleShopOdds12 = calculateWeight(slowMushroomCapsuleShopOdds12, shopOdds12Weights)
    flutterCapsuleShopOdds12 = calculateWeight(flutterCapsuleShopOdds12, shopOdds12Weights)
    cannonCapsuleShopOdds12 = calculateWeight(cannonCapsuleShopOdds12, shopOdds12Weights)
    snackCapsuleShopOdds12 = calculateWeight(snackCapsuleShopOdds12, shopOdds12Weights)
    goombaCapsuleShopOdds12 = calculateWeight(goombaCapsuleShopOdds12, shopOdds12Weights)
    hammerBroCapsuleShopOdds12 = calculateWeight(hammerBroCapsuleShopOdds12, shopOdds12Weights)
    piranhaPlantCapsuleShopOdds12 = calculateWeight(piranhaPlantCapsuleShopOdds12, shopOdds12Weights)
    kleptoCapsuleShopOdds12 = calculateWeight(kleptoCapsuleShopOdds12, shopOdds12Weights)
    kamekCapsuleShopOdds12 = calculateWeight(kamekCapsuleShopOdds12, shopOdds12Weights)
    toadyCapsuleShopOdds12 = calculateWeight(toadyCapsuleShopOdds12, shopOdds12Weights)
    mrBlizzardCapsuleShopOdds12 = calculateWeight(mrBlizzardCapsuleShopOdds12, shopOdds12Weights)
    banditCapsuleShopOdds12 = calculateWeight(banditCapsuleShopOdds12, shopOdds12Weights)
    pinkBooCapsuleShopOdds12 = calculateWeight(pinkBooCapsuleShopOdds12, shopOdds12Weights)
    spinyCapsuleShopOdds12 = calculateWeight(spinyCapsuleShopOdds12, shopOdds12Weights)
    podobooCapsuleShopOdds12 = calculateWeight(podobooCapsuleShopOdds12, shopOdds12Weights)
    tweesterCapsuleShopOdds12 = calculateWeight(tweesterCapsuleShopOdds12, shopOdds12Weights)
    thwompCapsuleShopOdds12 = calculateWeight(thwompCapsuleShopOdds12, shopOdds12Weights)
    warpCapsuleShopOdds12 = calculateWeight(warpCapsuleShopOdds12, shopOdds12Weights)
    bombCapsuleShopOdds12 = calculateWeight(bombCapsuleShopOdds12, shopOdds12Weights)
    fireballCapsuleShopOdds12 = calculateWeight(fireballCapsuleShopOdds12, shopOdds12Weights)
    paraTroopaCapsuleShopOdds12 = calculateWeight(paraTroopaCapsuleShopOdds12, shopOdds12Weights)
    eggCapsuleShopOdds12 = calculateWeight(eggCapsuleShopOdds12, shopOdds12Weights)
    vacuumCapsuleShopOdds12 = calculateWeight(vacuumCapsuleShopOdds12, shopOdds12Weights)
    magicCapsuleShopOdds12 = calculateWeight(magicCapsuleShopOdds12, shopOdds12Weights)
    tripleCapsuleShopOdds12 = calculateWeight(tripleCapsuleShopOdds12, shopOdds12Weights)
    koopaCapsuleShopOdds12 = calculateWeight(koopaCapsuleShopOdds12, shopOdds12Weights)
    mysteryCapsuleShopOdds12 = calculateWeight(mysteryCapsuleShopOdds12, shopOdds12Weights)
    duelCapsuleShopOdds12 = calculateWeight(duelCapsuleShopOdds12, shopOdds12Weights)
    dkCapsuleShopOdds12 = calculateWeight(dkCapsuleShopOdds12, shopOdds12Weights)
    orbBagCapsuleShopOdds12 = calculateWeight(orbBagCapsuleShopOdds12, shopOdds12Weights)
    DxCapsuleDuelShopOdds12 = calculateWeight(DxCapsuleDuelShopOdds12, shopOdds12Weights)
    DxCapsuleChanceShopOdds12 = calculateWeight(DxCapsuleChanceShopOdds12, shopOdds12Weights)
    DxCapsuleBowserShopOdds12 = calculateWeight(DxCapsuleBowserShopOdds12, shopOdds12Weights)
    DxCapsuleDonkeyKongShopOdds12 = calculateWeight(DxCapsuleDonkeyKongShopOdds12, shopOdds12Weights)
    DxCapsulePinkBooShopOdds12 = calculateWeight(DxCapsulePinkBooShopOdds12, shopOdds12Weights)
    DxCapsuleSolunaShopOdds12 = calculateWeight(DxCapsuleSolunaShopOdds12, shopOdds12Weights)
    DxCapsuleChainChompShopOdds12 = calculateWeight(DxCapsuleChainChompShopOdds12, shopOdds12Weights)
    DxCapsuleWackyWatchShopOdds12 = calculateWeight(DxCapsuleWackyWatchShopOdds12, shopOdds12Weights)

    # Calculate weights for shop odds 34
    mushroomCapsuleShopOdds34 = calculateWeight(mushroomCapsuleShopOdds34, shopOdds34Weights)
    goldenMushroomCapsuleShopOdds34 = calculateWeight(goldenMushroomCapsuleShopOdds34, shopOdds34Weights)
    metalMushroomCapsuleShopOdds34 = calculateWeight(metalMushroomCapsuleShopOdds34, shopOdds34Weights)
    slowMushroomCapsuleShopOdds34 = calculateWeight(slowMushroomCapsuleShopOdds34, shopOdds34Weights)
    flutterCapsuleShopOdds34 = calculateWeight(flutterCapsuleShopOdds34, shopOdds34Weights)
    cannonCapsuleShopOdds34 = calculateWeight(cannonCapsuleShopOdds34, shopOdds34Weights)
    snackCapsuleShopOdds34 = calculateWeight(snackCapsuleShopOdds34, shopOdds34Weights)
    goombaCapsuleShopOdds34 = calculateWeight(goombaCapsuleShopOdds34, shopOdds34Weights)
    hammerBroCapsuleShopOdds34 = calculateWeight(hammerBroCapsuleShopOdds34, shopOdds34Weights)
    piranhaPlantCapsuleShopOdds34 = calculateWeight(piranhaPlantCapsuleShopOdds34, shopOdds34Weights)
    kleptoCapsuleShopOdds34 = calculateWeight(kleptoCapsuleShopOdds34, shopOdds34Weights)
    kamekCapsuleShopOdds34 = calculateWeight(kamekCapsuleShopOdds34, shopOdds34Weights)
    toadyCapsuleShopOdds34 = calculateWeight(toadyCapsuleShopOdds34, shopOdds34Weights)
    mrBlizzardCapsuleShopOdds34 = calculateWeight(mrBlizzardCapsuleShopOdds34, shopOdds34Weights)
    banditCapsuleShopOdds34 = calculateWeight(banditCapsuleShopOdds34, shopOdds34Weights)
    pinkBooCapsuleShopOdds34 = calculateWeight(pinkBooCapsuleShopOdds34, shopOdds34Weights)
    spinyCapsuleShopOdds34 = calculateWeight(spinyCapsuleShopOdds34, shopOdds34Weights)
    podobooCapsuleShopOdds34 = calculateWeight(podobooCapsuleShopOdds34, shopOdds34Weights)
    tweesterCapsuleShopOdds34 = calculateWeight(tweesterCapsuleShopOdds34, shopOdds34Weights)
    thwompCapsuleShopOdds34 = calculateWeight(thwompCapsuleShopOdds34, shopOdds34Weights)
    warpCapsuleShopOdds34 = calculateWeight(warpCapsuleShopOdds34, shopOdds34Weights)
    bombCapsuleShopOdds34 = calculateWeight(bombCapsuleShopOdds34, shopOdds34Weights)
    fireballCapsuleShopOdds34 = calculateWeight(fireballCapsuleShopOdds34, shopOdds34Weights)
    paraTroopaCapsuleShopOdds34 = calculateWeight(paraTroopaCapsuleShopOdds34, shopOdds34Weights)
    eggCapsuleShopOdds34 = calculateWeight(eggCapsuleShopOdds34, shopOdds34Weights)
    vacuumCapsuleShopOdds34 = calculateWeight(vacuumCapsuleShopOdds34, shopOdds34Weights)
    magicCapsuleShopOdds34 = calculateWeight(magicCapsuleShopOdds34, shopOdds34Weights)
    tripleCapsuleShopOdds34 = calculateWeight(tripleCapsuleShopOdds34, shopOdds34Weights)
    koopaCapsuleShopOdds34 = calculateWeight(koopaCapsuleShopOdds34, shopOdds34Weights)
    mysteryCapsuleShopOdds34 = calculateWeight(mysteryCapsuleShopOdds34, shopOdds34Weights)
    duelCapsuleShopOdds34 = calculateWeight(duelCapsuleShopOdds34, shopOdds34Weights)
    dkCapsuleShopOdds34 = calculateWeight(dkCapsuleShopOdds34, shopOdds34Weights)
    orbBagCapsuleShopOdds34 = calculateWeight(orbBagCapsuleShopOdds34, shopOdds34Weights)
    DxCapsuleDuelShopOdds34 = calculateWeight(DxCapsuleDuelShopOdds34, shopOdds34Weights)
    DxCapsuleChanceShopOdds34 = calculateWeight(DxCapsuleChanceShopOdds34, shopOdds34Weights)
    DxCapsuleBowserShopOdds34 = calculateWeight(DxCapsuleBowserShopOdds34, shopOdds34Weights)
    DxCapsuleDonkeyKongShopOdds34 = calculateWeight(DxCapsuleDonkeyKongShopOdds34, shopOdds34Weights)
    DxCapsulePinkBooShopOdds34 = calculateWeight(DxCapsulePinkBooShopOdds34, shopOdds34Weights)
    DxCapsuleSolunaShopOdds34 = calculateWeight(DxCapsuleSolunaShopOdds34, shopOdds34Weights)
    DxCapsuleChainChompShopOdds34 = calculateWeight(DxCapsuleChainChompShopOdds34, shopOdds34Weights)
    DxCapsuleWackyWatchShopOdds34 = calculateWeight(DxCapsuleWackyWatchShopOdds34, shopOdds34Weights)

    # Calculate weights for space odds 1
    mushroomCapsuleSpaceOdds1 = calculateWeight(mushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    goldenMushroomCapsuleSpaceOdds1 = calculateWeight(goldenMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    metalMushroomCapsuleSpaceOdds1 = calculateWeight(metalMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    slowMushroomCapsuleSpaceOdds1 = calculateWeight(slowMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    flutterCapsuleSpaceOdds1 = calculateWeight(flutterCapsuleSpaceOdds1, spaceOdds1Weights)
    cannonCapsuleSpaceOdds1 = calculateWeight(cannonCapsuleSpaceOdds1, spaceOdds1Weights)
    snackCapsuleSpaceOdds1 = calculateWeight(snackCapsuleSpaceOdds1, spaceOdds1Weights)
    goombaCapsuleSpaceOdds1 = calculateWeight(goombaCapsuleSpaceOdds1, spaceOdds1Weights)
    hammerBroCapsuleSpaceOdds1 = calculateWeight(hammerBroCapsuleSpaceOdds1, spaceOdds1Weights)
    piranhaPlantCapsuleSpaceOdds1 = calculateWeight(piranhaPlantCapsuleSpaceOdds1, spaceOdds1Weights)
    kleptoCapsuleSpaceOdds1 = calculateWeight(kleptoCapsuleSpaceOdds1, spaceOdds1Weights)
    kamekCapsuleSpaceOdds1 = calculateWeight(kamekCapsuleSpaceOdds1, spaceOdds1Weights)
    toadyCapsuleSpaceOdds1 = calculateWeight(toadyCapsuleSpaceOdds1, spaceOdds1Weights)
    mrBlizzardCapsuleSpaceOdds1 = calculateWeight(mrBlizzardCapsuleSpaceOdds1, spaceOdds1Weights)
    banditCapsuleSpaceOdds1 = calculateWeight(banditCapsuleSpaceOdds1, spaceOdds1Weights)
    pinkBooCapsuleSpaceOdds1 = calculateWeight(pinkBooCapsuleSpaceOdds1, spaceOdds1Weights)
    spinyCapsuleSpaceOdds1 = calculateWeight(spinyCapsuleSpaceOdds1, spaceOdds1Weights)
    podobooCapsuleSpaceOdds1 = calculateWeight(podobooCapsuleSpaceOdds1, spaceOdds1Weights)
    tweesterCapsuleSpaceOdds1 = calculateWeight(tweesterCapsuleSpaceOdds1, spaceOdds1Weights)
    thwompCapsuleSpaceOdds1 = calculateWeight(thwompCapsuleSpaceOdds1, spaceOdds1Weights)
    warpCapsuleSpaceOdds1 = calculateWeight(warpCapsuleSpaceOdds1, spaceOdds1Weights)
    bombCapsuleSpaceOdds1 = calculateWeight(bombCapsuleSpaceOdds1, spaceOdds1Weights)
    fireballCapsuleSpaceOdds1 = calculateWeight(fireballCapsuleSpaceOdds1, spaceOdds1Weights)
    paraTroopaCapsuleSpaceOdds1 = calculateWeight(paraTroopaCapsuleSpaceOdds1, spaceOdds1Weights)
    eggCapsuleSpaceOdds1 = calculateWeight(eggCapsuleSpaceOdds1, spaceOdds1Weights)
    vacuumCapsuleSpaceOdds1 = calculateWeight(vacuumCapsuleSpaceOdds1, spaceOdds1Weights)
    magicCapsuleSpaceOdds1 = calculateWeight(magicCapsuleSpaceOdds1, spaceOdds1Weights)
    tripleCapsuleSpaceOdds1 = calculateWeight(tripleCapsuleSpaceOdds1, spaceOdds1Weights)
    koopaCapsuleSpaceOdds1 = calculateWeight(koopaCapsuleSpaceOdds1, spaceOdds1Weights)
    mysteryCapsuleSpaceOdds1 = calculateWeight(mysteryCapsuleSpaceOdds1, spaceOdds1Weights)
    duelCapsuleSpaceOdds1 = calculateWeight(duelCapsuleSpaceOdds1, spaceOdds1Weights)
    dkCapsuleSpaceOdds1 = calculateWeight(dkCapsuleSpaceOdds1, spaceOdds1Weights)
    orbBagCapsuleSpaceOdds1 = calculateWeight(orbBagCapsuleSpaceOdds1, spaceOdds1Weights)
    DxCapsuleDuelSpaceOdds1 = calculateWeight(DxCapsuleDuelSpaceOdds1, spaceOdds1Weights)
    DxCapsuleChanceSpaceOdds1 = calculateWeight(DxCapsuleChanceSpaceOdds1, spaceOdds1Weights)
    DxCapsuleBowserSpaceOdds1 = calculateWeight(DxCapsuleBowserSpaceOdds1, spaceOdds1Weights)
    DxCapsuleDonkeyKongSpaceOdds1 = calculateWeight(DxCapsuleDonkeyKongSpaceOdds1, spaceOdds1Weights)
    DxCapsulePinkBooSpaceOdds1 = calculateWeight(DxCapsulePinkBooSpaceOdds1, spaceOdds1Weights)
    DxCapsuleSolunaSpaceOdds1 = calculateWeight(DxCapsuleSolunaSpaceOdds1, spaceOdds1Weights)
    DxCapsuleChainChompSpaceOdds1 = calculateWeight(DxCapsuleChainChompSpaceOdds1, spaceOdds1Weights)
    DxCapsuleWackyWatchSpaceOdds1 = calculateWeight(DxCapsuleWackyWatchSpaceOdds1, spaceOdds1Weights)

    # Calculate weights for space odds 2
    mushroomCapsuleSpaceOdds2 = calculateWeight(mushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    goldenMushroomCapsuleSpaceOdds2 = calculateWeight(goldenMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    metalMushroomCapsuleSpaceOdds2 = calculateWeight(metalMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    slowMushroomCapsuleSpaceOdds2 = calculateWeight(slowMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    flutterCapsuleSpaceOdds2 = calculateWeight(flutterCapsuleSpaceOdds2, spaceOdds2Weights)
    cannonCapsuleSpaceOdds2 = calculateWeight(cannonCapsuleSpaceOdds2, spaceOdds2Weights)
    snackCapsuleSpaceOdds2 = calculateWeight(snackCapsuleSpaceOdds2, spaceOdds2Weights)
    goombaCapsuleSpaceOdds2 = calculateWeight(goombaCapsuleSpaceOdds2, spaceOdds2Weights)
    hammerBroCapsuleSpaceOdds2 = calculateWeight(hammerBroCapsuleSpaceOdds2, spaceOdds2Weights)
    piranhaPlantCapsuleSpaceOdds2 = calculateWeight(piranhaPlantCapsuleSpaceOdds2, spaceOdds2Weights)
    kleptoCapsuleSpaceOdds2 = calculateWeight(kleptoCapsuleSpaceOdds2, spaceOdds2Weights)
    kamekCapsuleSpaceOdds2 = calculateWeight(kamekCapsuleSpaceOdds2, spaceOdds2Weights)
    toadyCapsuleSpaceOdds2 = calculateWeight(toadyCapsuleSpaceOdds2, spaceOdds2Weights)
    mrBlizzardCapsuleSpaceOdds2 = calculateWeight(mrBlizzardCapsuleSpaceOdds2, spaceOdds2Weights)
    banditCapsuleSpaceOdds2 = calculateWeight(banditCapsuleSpaceOdds2, spaceOdds2Weights)
    pinkBooCapsuleSpaceOdds2 = calculateWeight(pinkBooCapsuleSpaceOdds2, spaceOdds2Weights)
    spinyCapsuleSpaceOdds2 = calculateWeight(spinyCapsuleSpaceOdds2, spaceOdds2Weights)
    podobooCapsuleSpaceOdds2 = calculateWeight(podobooCapsuleSpaceOdds2, spaceOdds2Weights)
    tweesterCapsuleSpaceOdds2 = calculateWeight(tweesterCapsuleSpaceOdds2, spaceOdds2Weights)
    thwompCapsuleSpaceOdds2 = calculateWeight(thwompCapsuleSpaceOdds2, spaceOdds2Weights)
    warpCapsuleSpaceOdds2 = calculateWeight(warpCapsuleSpaceOdds2, spaceOdds2Weights)
    bombCapsuleSpaceOdds2 = calculateWeight(bombCapsuleSpaceOdds2, spaceOdds2Weights)
    fireballCapsuleSpaceOdds2 = calculateWeight(fireballCapsuleSpaceOdds2, spaceOdds2Weights)
    paraTroopaCapsuleSpaceOdds2 = calculateWeight(paraTroopaCapsuleSpaceOdds2, spaceOdds2Weights)
    eggCapsuleSpaceOdds2 = calculateWeight(eggCapsuleSpaceOdds2, spaceOdds2Weights)
    vacuumCapsuleSpaceOdds2 = calculateWeight(vacuumCapsuleSpaceOdds2, spaceOdds2Weights)
    magicCapsuleSpaceOdds2 = calculateWeight(magicCapsuleSpaceOdds2, spaceOdds2Weights)
    tripleCapsuleSpaceOdds2 = calculateWeight(tripleCapsuleSpaceOdds2, spaceOdds2Weights)
    koopaCapsuleSpaceOdds2 = calculateWeight(koopaCapsuleSpaceOdds2, spaceOdds2Weights)
    mysteryCapsuleSpaceOdds2 = calculateWeight(mysteryCapsuleSpaceOdds2, spaceOdds2Weights)
    duelCapsuleSpaceOdds2 = calculateWeight(duelCapsuleSpaceOdds2, spaceOdds2Weights)
    dkCapsuleSpaceOdds2 = calculateWeight(dkCapsuleSpaceOdds2, spaceOdds2Weights)
    orbBagCapsuleSpaceOdds2 = calculateWeight(orbBagCapsuleSpaceOdds2, spaceOdds2Weights)
    DxCapsuleDuelSpaceOdds2 = calculateWeight(DxCapsuleDuelSpaceOdds2, spaceOdds2Weights)
    DxCapsuleChanceSpaceOdds2 = calculateWeight(DxCapsuleChanceSpaceOdds2, spaceOdds2Weights)
    DxCapsuleBowserSpaceOdds2 = calculateWeight(DxCapsuleBowserSpaceOdds2, spaceOdds2Weights)
    DxCapsuleDonkeyKongSpaceOdds2 = calculateWeight(DxCapsuleDonkeyKongSpaceOdds2, spaceOdds2Weights)
    DxCapsulePinkBooSpaceOdds2 = calculateWeight(DxCapsulePinkBooSpaceOdds2, spaceOdds2Weights)
    DxCapsuleSolunaSpaceOdds2 = calculateWeight(DxCapsuleSolunaSpaceOdds2, spaceOdds2Weights)
    DxCapsuleChainChompSpaceOdds2 = calculateWeight(DxCapsuleChainChompSpaceOdds2, spaceOdds2Weights)
    DxCapsuleWackyWatchSpaceOdds2 = calculateWeight(DxCapsuleWackyWatchSpaceOdds2, spaceOdds2Weights)

    # Calculate weights for space odds 34
    mushroomCapsuleSpaceOdds34 = calculateWeight(mushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    goldenMushroomCapsuleSpaceOdds34 = calculateWeight(goldenMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    metalMushroomCapsuleSpaceOdds34 = calculateWeight(metalMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    slowMushroomCapsuleSpaceOdds34 = calculateWeight(slowMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    flutterCapsuleSpaceOdds34 = calculateWeight(flutterCapsuleSpaceOdds34, spaceOdds34Weights)
    cannonCapsuleSpaceOdds34 = calculateWeight(cannonCapsuleSpaceOdds34, spaceOdds34Weights)
    snackCapsuleSpaceOdds34 = calculateWeight(snackCapsuleSpaceOdds34, spaceOdds34Weights)
    goombaCapsuleSpaceOdds34 = calculateWeight(goombaCapsuleSpaceOdds34, spaceOdds34Weights)
    hammerBroCapsuleSpaceOdds34 = calculateWeight(hammerBroCapsuleSpaceOdds34, spaceOdds34Weights)
    piranhaPlantCapsuleSpaceOdds34 = calculateWeight(piranhaPlantCapsuleSpaceOdds34, spaceOdds34Weights)
    kleptoCapsuleSpaceOdds34 = calculateWeight(kleptoCapsuleSpaceOdds34, spaceOdds34Weights)
    kamekCapsuleSpaceOdds34 = calculateWeight(kamekCapsuleSpaceOdds34, spaceOdds34Weights)
    toadyCapsuleSpaceOdds34 = calculateWeight(toadyCapsuleSpaceOdds34, spaceOdds34Weights)
    mrBlizzardCapsuleSpaceOdds34 = calculateWeight(mrBlizzardCapsuleSpaceOdds34, spaceOdds34Weights)
    banditCapsuleSpaceOdds34 = calculateWeight(banditCapsuleSpaceOdds34, spaceOdds34Weights)
    pinkBooCapsuleSpaceOdds34 = calculateWeight(pinkBooCapsuleSpaceOdds34, spaceOdds34Weights)
    spinyCapsuleSpaceOdds34 = calculateWeight(spinyCapsuleSpaceOdds34, spaceOdds34Weights)
    podobooCapsuleSpaceOdds34 = calculateWeight(podobooCapsuleSpaceOdds34, spaceOdds34Weights)
    tweesterCapsuleSpaceOdds34 = calculateWeight(tweesterCapsuleSpaceOdds34, spaceOdds34Weights)
    thwompCapsuleSpaceOdds34 = calculateWeight(thwompCapsuleSpaceOdds34, spaceOdds34Weights)
    warpCapsuleSpaceOdds34 = calculateWeight(warpCapsuleSpaceOdds34, spaceOdds34Weights)
    bombCapsuleSpaceOdds34 = calculateWeight(bombCapsuleSpaceOdds34, spaceOdds34Weights)
    fireballCapsuleSpaceOdds34 = calculateWeight(fireballCapsuleSpaceOdds34, spaceOdds34Weights)
    paraTroopaCapsuleSpaceOdds34 = calculateWeight(paraTroopaCapsuleSpaceOdds34, spaceOdds34Weights)
    eggCapsuleSpaceOdds34 = calculateWeight(eggCapsuleSpaceOdds34, spaceOdds34Weights)
    vacuumCapsuleSpaceOdds34 = calculateWeight(vacuumCapsuleSpaceOdds34, spaceOdds34Weights)
    magicCapsuleSpaceOdds34 = calculateWeight(magicCapsuleSpaceOdds34, spaceOdds34Weights)
    tripleCapsuleSpaceOdds34 = calculateWeight(tripleCapsuleSpaceOdds34, spaceOdds34Weights)
    koopaCapsuleSpaceOdds34 = calculateWeight(koopaCapsuleSpaceOdds34, spaceOdds34Weights)
    mysteryCapsuleSpaceOdds34 = calculateWeight(mysteryCapsuleSpaceOdds34, spaceOdds34Weights)
    duelCapsuleSpaceOdds34 = calculateWeight(duelCapsuleSpaceOdds34, spaceOdds34Weights)
    dkCapsuleSpaceOdds34 = calculateWeight(dkCapsuleSpaceOdds34, spaceOdds34Weights)
    orbBagCapsuleSpaceOdds34 = calculateWeight(orbBagCapsuleSpaceOdds34, spaceOdds34Weights)
    DxCapsuleDuelSpaceOdds34 = calculateWeight(DxCapsuleDuelSpaceOdds34, spaceOdds34Weights)
    DxCapsuleChanceSpaceOdds34 = calculateWeight(DxCapsuleChanceSpaceOdds34, spaceOdds34Weights)
    DxCapsuleBowserSpaceOdds34 = calculateWeight(DxCapsuleBowserSpaceOdds34, spaceOdds34Weights)
    DxCapsuleDonkeyKongSpaceOdds34 = calculateWeight(DxCapsuleDonkeyKongSpaceOdds34, spaceOdds34Weights)
    DxCapsulePinkBooSpaceOdds34 = calculateWeight(DxCapsulePinkBooSpaceOdds34, spaceOdds34Weights)
    DxCapsuleSolunaSpaceOdds34 = calculateWeight(DxCapsuleSolunaSpaceOdds34, spaceOdds34Weights)
    DxCapsuleChainChompSpaceOdds34 = calculateWeight(DxCapsuleChainChompSpaceOdds34, spaceOdds34Weights)
    DxCapsuleWackyWatchSpaceOdds34 = calculateWeight(DxCapsuleWackyWatchSpaceOdds34, spaceOdds34Weights)

    # Redefine Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, goombaCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, kleptoCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, podobooCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, paraTroopaCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12,
        DxCapsuleDuelShopOdds12, DxCapsuleChanceShopOdds12, DxCapsuleBowserShopOdds12,
        DxCapsuleDonkeyKongShopOdds12, DxCapsulePinkBooShopOdds12, DxCapsuleSolunaShopOdds12, DxCapsuleChainChompShopOdds12,
        DxCapsuleWackyWatchShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, goombaCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, kleptoCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, podobooCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, paraTroopaCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34,
        DxCapsuleDuelShopOdds34, DxCapsuleChanceShopOdds34, DxCapsuleBowserShopOdds34,
        DxCapsuleDonkeyKongShopOdds34, DxCapsulePinkBooShopOdds34, DxCapsuleSolunaShopOdds34, DxCapsuleChainChompShopOdds34,
        DxCapsuleWackyWatchShopOdds34
    ]

    spaceOdds1 = [
        mushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds1,
        slowMushroomCapsuleSpaceOdds1, flutterCapsuleSpaceOdds1, cannonCapsuleSpaceOdds1,
        snackCapsuleSpaceOdds1, goombaCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds1,
        piranhaPlantCapsuleSpaceOdds1, kleptoCapsuleSpaceOdds1, kamekCapsuleSpaceOdds1,
        toadyCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds1, banditCapsuleSpaceOdds1,
        pinkBooCapsuleSpaceOdds1, spinyCapsuleSpaceOdds1, podobooCapsuleSpaceOdds1,
        tweesterCapsuleSpaceOdds1, thwompCapsuleSpaceOdds1, warpCapsuleSpaceOdds1,
        bombCapsuleSpaceOdds1, fireballCapsuleSpaceOdds1, paraTroopaCapsuleSpaceOdds1,
        eggCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds1, magicCapsuleSpaceOdds1,
        tripleCapsuleSpaceOdds1, koopaCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds1,
        duelCapsuleSpaceOdds1, dkCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds1,
        DxCapsuleDuelSpaceOdds1, DxCapsuleChanceSpaceOdds1, DxCapsuleBowserSpaceOdds1,
        DxCapsuleDonkeyKongSpaceOdds1, DxCapsulePinkBooSpaceOdds1, DxCapsuleSolunaSpaceOdds1, DxCapsuleChainChompSpaceOdds1,
        DxCapsuleWackyWatchSpaceOdds1
    ]

    spaceOdds2 = [
        mushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds2,
        slowMushroomCapsuleSpaceOdds2, flutterCapsuleSpaceOdds2, cannonCapsuleSpaceOdds2,
        snackCapsuleSpaceOdds2, goombaCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds2,
        piranhaPlantCapsuleSpaceOdds2, kleptoCapsuleSpaceOdds2, kamekCapsuleSpaceOdds2,
        toadyCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds2, banditCapsuleSpaceOdds2,
        pinkBooCapsuleSpaceOdds2, spinyCapsuleSpaceOdds2, podobooCapsuleSpaceOdds2,
        tweesterCapsuleSpaceOdds2, thwompCapsuleSpaceOdds2, warpCapsuleSpaceOdds2,
        bombCapsuleSpaceOdds2, fireballCapsuleSpaceOdds2, paraTroopaCapsuleSpaceOdds2,
        eggCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds2, magicCapsuleSpaceOdds2,
        tripleCapsuleSpaceOdds2, koopaCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds2,
        duelCapsuleSpaceOdds2, dkCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds2,
        DxCapsuleDuelSpaceOdds2, DxCapsuleChanceSpaceOdds2, DxCapsuleBowserSpaceOdds2,
        DxCapsuleDonkeyKongSpaceOdds2, DxCapsulePinkBooSpaceOdds2, DxCapsuleSolunaSpaceOdds2, DxCapsuleChainChompSpaceOdds2,
        DxCapsuleWackyWatchSpaceOdds2
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, goombaCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, kleptoCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, podobooCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, paraTroopaCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34,
        DxCapsuleDuelSpaceOdds34, DxCapsuleChanceSpaceOdds34, DxCapsuleBowserSpaceOdds34,
        DxCapsuleDonkeyKongSpaceOdds34, DxCapsulePinkBooSpaceOdds34, DxCapsuleSolunaSpaceOdds34, DxCapsuleChainChompSpaceOdds34,
        DxCapsuleWackyWatchSpaceOdds34
    ]

    shopOdds12Weights = sum(weight for weight in shopOdds12)
    shopOdds34Weights = sum(weight for weight in shopOdds34)
    spaceOdds1Weights = sum(weight for weight in spaceOdds1)
    spaceOdds2Weights = sum(weight for weight in spaceOdds2)
    spaceOdds34Weights = sum(weight for weight in shopOdds34)

    if spaceOdds1Weights < 101:
        spaceOdds1Max = max(zip(spaceOdds1, spaceOdds1), key=lambda tuple: tuple[1])[0]

    if spaceOdds34Weights < 101:
        spaceOdds34Max = max(zip(spaceOdds34, spaceOdds34), key=lambda tuple: tuple[1])[0]

    if shopOdds12Weights < 101:
        shopOdds12Max = max(zip(shopOdds12, shopOdds12), key=lambda tuple: tuple[1])[0]

    if spaceOdds2Weights < 101:
        spaceOdds2Max = max(zip(spaceOdds2, spaceOdds2), key=lambda tuple: tuple[1])[0]

    if shopOdds34Weights < 101:
        shopOdds34Max = max(zip(shopOdds34, shopOdds34), key=lambda tuple: tuple[1])[0]

    if shopOdds12Max == 'mushroomCapsuleShopOdds12':
        mushroomCapsuleShopOdds12 += (100 - mushroomCapsuleShopOdds12)

    if shopOdds12Max == 'goldenMushroomCapsuleShopOdds12':
        goldenMushroomCapsuleShopOdds12 += (100 - goldenMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'metalMushroomCapsuleShopOdds12':
        metalMushroomCapsuleShopOdds12 += (100 - metalMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'slowMushroomCapsuleShopOdds12':
        slowMushroomCapsuleShopOdds12 += (100 - slowMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'flutterCapsuleShopOdds12':
        flutterCapsuleShopOdds12 += (100 - flutterCapsuleShopOdds12)

    if shopOdds12Max == 'cannonCapsuleShopOdds12':
        cannonCapsuleShopOdds12 += (100 - cannonCapsuleShopOdds12)

    if shopOdds12Max == 'snackCapsuleShopOdds12':
        snackCapsuleShopOdds12 += (100 - snackCapsuleShopOdds12)

    if shopOdds12Max == 'goombaCapsuleShopOdds12':
        goombaCapsuleShopOdds12 += (100 - goombaCapsuleShopOdds12)

    if shopOdds12Max == 'hammerBroCapsuleShopOdds12':
        hammerBroCapsuleShopOdds12 += (100 - hammerBroCapsuleShopOdds12)

    if shopOdds12Max == 'piranhaPlantCapsuleShopOdds12':
        piranhaPlantCapsuleShopOdds12 += (100 - piranhaPlantCapsuleShopOdds12)

    if shopOdds12Max == 'kleptoCapsuleShopOdds12':
        kleptoCapsuleShopOdds12 += (100 - kleptoCapsuleShopOdds12)

    if shopOdds12Max == 'kamekCapsuleShopOdds12':
        kamekCapsuleShopOdds12 += (100 - kamekCapsuleShopOdds12)

    if shopOdds12Max == 'toadyCapsuleShopOdds12':
        toadyCapsuleShopOdds12 += (100 - toadyCapsuleShopOdds12)

    if shopOdds12Max == 'mrBlizzardCapsuleShopOdds12':
        mrBlizzardCapsuleShopOdds12 += (100 - mrBlizzardCapsuleShopOdds12)

    if shopOdds12Max == 'banditCapsuleShopOdds12':
        banditCapsuleShopOdds12 += (100 - banditCapsuleShopOdds12)

    if shopOdds12Max == 'pinkBooCapsuleShopOdds12':
        pinkBooCapsuleShopOdds12 += (100 - pinkBooCapsuleShopOdds12)

    if shopOdds12Max == 'spinyCapsuleShopOdds12':
        spinyCapsuleShopOdds12 += (100 - spinyCapsuleShopOdds12)

    if shopOdds12Max == 'podobooCapsuleShopOdds12':
        podobooCapsuleShopOdds12 += (100 - podobooCapsuleShopOdds12)

    if shopOdds12Max == 'tweesterCapsuleShopOdds12':
        tweesterCapsuleShopOdds12 += (100 - tweesterCapsuleShopOdds12)

    if shopOdds12Max == 'thwompCapsuleShopOdds12':
        thwompCapsuleShopOdds12 += (100 - thwompCapsuleShopOdds12)

    if shopOdds12Max == 'warpCapsuleShopOdds12':
        warpCapsuleShopOdds12 += (100 - warpCapsuleShopOdds12)

    if shopOdds12Max == 'bombCapsuleShopOdds12':
        bombCapsuleShopOdds12 += (100 - bombCapsuleShopOdds12)

    if shopOdds12Max == 'fireballCapsuleShopOdds12':
        fireballCapsuleShopOdds12 += (100 - fireballCapsuleShopOdds12)

    if shopOdds12Max == 'paraTroopaCapsuleShopOdds12':
        paraTroopaCapsuleShopOdds12 += (100 - paraTroopaCapsuleShopOdds12)

    if shopOdds12Max == 'eggCapsuleShopOdds12':
        eggCapsuleShopOdds12 += (100 - eggCapsuleShopOdds12)

    if shopOdds12Max == 'vacuumCapsuleShopOdds12':
        vacuumCapsuleShopOdds12 += (100 - vacuumCapsuleShopOdds12)

    if shopOdds12Max == 'magicCapsuleShopOdds12':
        magicCapsuleShopOdds12 += (100 - magicCapsuleShopOdds12)

    if shopOdds12Max == 'tripleCapsuleShopOdds12':
        tripleCapsuleShopOdds12 += (100 - tripleCapsuleShopOdds12)

    if shopOdds12Max == 'koopaCapsuleShopOdds12':
        koopaCapsuleShopOdds12 += (100 - koopaCapsuleShopOdds12)

    if shopOdds12Max == 'mysteryCapsuleShopOdds12':
        mysteryCapsuleShopOdds12 += (100 - mysteryCapsuleShopOdds12)

    if shopOdds12Max == 'duelCapsuleShopOdds12':
        duelCapsuleShopOdds12 += (100 - duelCapsuleShopOdds12)

    if shopOdds12Max == 'dkCapsuleShopOdds12':
        dkCapsuleShopOdds12 += (100 - dkCapsuleShopOdds12)

    if shopOdds12Max == 'orbBagCapsuleShopOdds12':
        orbBagCapsuleShopOdds12 += (100 - orbBagCapsuleShopOdds12)

    if shopOdds12Max == 'DxCapsuleDuelShopOdds12':
        DxCapsuleDuelShopOdds12 += (100 - DxCapsuleDuelShopOdds12)
    
    if shopOdds12Max == 'DxCapsuleChanceShopOdds12':
        DxCapsuleChanceShopOdds12 += (100 - DxCapsuleChanceShopOdds12)
    
    if shopOdds12Max == 'DxCapsuleBowserShopOdds12':
        DxCapsuleBowserShopOdds12 += (100 - DxCapsuleBowserShopOdds12)
    
    if shopOdds12Max == 'DxCapsuleDonkeyKongShopOdds12':
        DxCapsuleDonkeyKongShopOdds12 += (100 - DxCapsuleDonkeyKongShopOdds12)

    if shopOdds12Max == 'DxCapsulePinkBooShopOdds12':
        DxCapsulePinkBooShopOdds12 += (100 - DxCapsulePinkBooShopOdds12)
    
    if shopOdds12Max == 'DxCapsuleSolunaShopOdds12':
        DxCapsuleSolunaShopOdds12 += (100 - DxCapsuleSolunaShopOdds12)

    if shopOdds12Max == 'DxCapsuleChainChompShopOdds12':
        DxCapsuleChainChompShopOdds12 += (100 - DxCapsuleChainChompShopOdds12)

    if shopOdds12Max == 'DxCapsuleWackyWatchShopOdds12':
        DxCapsuleWackyWatchShopOdds12 += (100 - DxCapsuleWackyWatchShopOdds12)

    if shopOdds34Max == 'mushroomCapsuleShopOdds34':
        mushroomCapsuleShopOdds34 += (100 - mushroomCapsuleShopOdds34)

    if shopOdds34Max == 'goldenMushroomCapsuleShopOdds34':
        goldenMushroomCapsuleShopOdds34 += (100 - goldenMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'metalMushroomCapsuleShopOdds34':
        metalMushroomCapsuleShopOdds34 += (100 - metalMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'slowMushroomCapsuleShopOdds34':
        slowMushroomCapsuleShopOdds34 += (100 - slowMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'flutterCapsuleShopOdds34':
        flutterCapsuleShopOdds34 += (100 - flutterCapsuleShopOdds34)

    if shopOdds34Max == 'cannonCapsuleShopOdds34':
        cannonCapsuleShopOdds34 += (100 - cannonCapsuleShopOdds34)

    if shopOdds34Max == 'snackCapsuleShopOdds34':
        snackCapsuleShopOdds34 += (100 - snackCapsuleShopOdds34)

    if shopOdds34Max == 'goombaCapsuleShopOdds34':
        goombaCapsuleShopOdds34 += (100 - goombaCapsuleShopOdds34)

    if shopOdds34Max == 'hammerBroCapsuleShopOdds34':
        hammerBroCapsuleShopOdds34 += (100 - hammerBroCapsuleShopOdds34)

    if shopOdds34Max == 'piranhaPlantCapsuleShopOdds34':
        piranhaPlantCapsuleShopOdds34 += (100 - piranhaPlantCapsuleShopOdds34)

    if shopOdds34Max == 'kleptoCapsuleShopOdds34':
        kleptoCapsuleShopOdds34 += (100 - kleptoCapsuleShopOdds34)

    if shopOdds34Max == 'kamekCapsuleShopOdds34':
        kamekCapsuleShopOdds34 += (100 - kamekCapsuleShopOdds34)

    if shopOdds34Max == 'toadyCapsuleShopOdds34':
        toadyCapsuleShopOdds34 += (100 - toadyCapsuleShopOdds34)

    if shopOdds34Max == 'mrBlizzardCapsuleShopOdds34':
        mrBlizzardCapsuleShopOdds34 += (100 - mrBlizzardCapsuleShopOdds34)

    if shopOdds34Max == 'banditCapsuleShopOdds34':
        banditCapsuleShopOdds34 += (100 - banditCapsuleShopOdds34)

    if shopOdds34Max == 'pinkBooCapsuleShopOdds34':
        pinkBooCapsuleShopOdds34 += (100 - pinkBooCapsuleShopOdds34)

    if shopOdds34Max == 'spinyCapsuleShopOdds34':
        spinyCapsuleShopOdds34 += (100 - spinyCapsuleShopOdds34)

    if shopOdds34Max == 'podobooCapsuleShopOdds34':
        podobooCapsuleShopOdds34 += (100 - podobooCapsuleShopOdds34)

    if shopOdds34Max == 'tweesterCapsuleShopOdds34':
        tweesterCapsuleShopOdds34 += (100 - tweesterCapsuleShopOdds34)

    if shopOdds34Max == 'thwompCapsuleShopOdds34':
        thwompCapsuleShopOdds34 += (100 - thwompCapsuleShopOdds34)

    if shopOdds34Max == 'warpCapsuleShopOdds34':
        warpCapsuleShopOdds34 += (100 - warpCapsuleShopOdds34)

    if shopOdds34Max == 'bombCapsuleShopOdds34':
        bombCapsuleShopOdds34 += (100 - bombCapsuleShopOdds34)

    if shopOdds34Max == 'fireballCapsuleShopOdds34':
        fireballCapsuleShopOdds34 += (100 - fireballCapsuleShopOdds34)

    if shopOdds34Max == 'paraTroopaCapsuleShopOdds34':
        paraTroopaCapsuleShopOdds34 += (100 - paraTroopaCapsuleShopOdds34)

    if shopOdds34Max == 'eggCapsuleShopOdds34':
        eggCapsuleShopOdds34 += (100 - eggCapsuleShopOdds34)

    if shopOdds34Max == 'vacuumCapsuleShopOdds34':
        vacuumCapsuleShopOdds34 += (100 - vacuumCapsuleShopOdds34)

    if shopOdds34Max == 'magicCapsuleShopOdds34':
        magicCapsuleShopOdds34 += (100 - magicCapsuleShopOdds34)

    if shopOdds34Max == 'tripleCapsuleShopOdds34':
        tripleCapsuleShopOdds34 += (100 - tripleCapsuleShopOdds34)

    if shopOdds34Max == 'koopaCapsuleShopOdds34':
        koopaCapsuleShopOdds34 += (100 - koopaCapsuleShopOdds34)

    if shopOdds34Max == 'mysteryCapsuleShopOdds34':
        mysteryCapsuleShopOdds34 += (100 - mysteryCapsuleShopOdds34)

    if shopOdds34Max == 'duelCapsuleShopOdds34':
        duelCapsuleShopOdds34 += (100 - duelCapsuleShopOdds34)

    if shopOdds34Max == 'dkCapsuleShopOdds34':
        dkCapsuleShopOdds34 += (100 - dkCapsuleShopOdds34)

    if shopOdds34Max == 'orbBagCapsuleShopOdds34':
        orbBagCapsuleShopOdds34 += (100 - orbBagCapsuleShopOdds34)

    if shopOdds34Max == 'DxCapsuleDuelShopOdds34':
        DxCapsuleDuelShopOdds34 += (100 - DxCapsuleDuelShopOdds34)

    if shopOdds34Max == 'DxCapsuleChanceShopOdds34':
        DxCapsuleChanceShopOdds34 += (100 - DxCapsuleChanceShopOdds34)

    if shopOdds34Max == 'DxCapsuleBowserShopOdds34':
        DxCapsuleBowserShopOdds34 += (100 - DxCapsuleBowserShopOdds34)

    if shopOdds34Max == 'DxCapsuleDonkeyKongShopOdds34':
        DxCapsuleDonkeyKongShopOdds34 += (100 - DxCapsuleDonkeyKongShopOdds34)

    if shopOdds34Max == 'DxCapsulePinkBooShopOdds34':
        DxCapsulePinkBooShopOdds34 += (100 - DxCapsulePinkBooShopOdds34)

    if shopOdds34Max == 'DxCapsuleSolunaShopOdds34':
        DxCapsuleSolunaShopOdds34 += (100 - DxCapsuleSolunaShopOdds34)

    if shopOdds34Max == 'DxCapsuleChainChompShopOdds34':
        DxCapsuleChainChompShopOdds34 += (100 - DxCapsuleChainChompShopOdds34)

    if shopOdds34Max == 'DxCapsuleWackyWatchShopOdds34':
        DxCapsuleWackyWatchShopOdds34 += (100 - DxCapsuleWackyWatchShopOdds34)    

    if spaceOdds1Max == 'mushroomCapsuleSpaceOdds1':
        mushroomCapsuleSpaceOdds1 += (100 - mushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'goldenMushroomCapsuleSpaceOdds1':
        goldenMushroomCapsuleSpaceOdds1 += (100 - goldenMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'metalMushroomCapsuleSpaceOdds1':
        metalMushroomCapsuleSpaceOdds1 += (100 - metalMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'slowMushroomCapsuleSpaceOdds1':
        slowMushroomCapsuleSpaceOdds1 += (100 - slowMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'flutterCapsuleSpaceOdds1':
        flutterCapsuleSpaceOdds1 += (100 - flutterCapsuleSpaceOdds1)

    if spaceOdds1Max == 'cannonCapsuleSpaceOdds1':
        cannonCapsuleSpaceOdds1 += (100 - cannonCapsuleSpaceOdds1)

    if spaceOdds1Max == 'snackCapsuleSpaceOdds1':
        snackCapsuleSpaceOdds1 += (100 - snackCapsuleSpaceOdds1)

    if spaceOdds1Max == 'goombaCapsuleSpaceOdds1':
        goombaCapsuleSpaceOdds1 += (100 - goombaCapsuleSpaceOdds1)

    if spaceOdds1Max == 'hammerBroCapsuleSpaceOdds1':
        hammerBroCapsuleSpaceOdds1 += (100 - hammerBroCapsuleSpaceOdds1)

    if spaceOdds1Max == 'piranhaPlantCapsuleSpaceOdds1':
        piranhaPlantCapsuleSpaceOdds1 += (100 - piranhaPlantCapsuleSpaceOdds1)

    if spaceOdds1Max == 'kleptoCapsuleSpaceOdds1':
        kleptoCapsuleSpaceOdds1 += (100 - kleptoCapsuleSpaceOdds1)

    if spaceOdds1Max == 'kamekCapsuleSpaceOdds1':
        kamekCapsuleSpaceOdds1 += (100 - kamekCapsuleSpaceOdds1)

    if spaceOdds1Max == 'toadyCapsuleSpaceOdds1':
        toadyCapsuleSpaceOdds1 += (100 - toadyCapsuleSpaceOdds1)

    if spaceOdds1Max == 'mrBlizzardCapsuleSpaceOdds1':
        mrBlizzardCapsuleSpaceOdds1 += (100 - mrBlizzardCapsuleSpaceOdds1)

    if spaceOdds1Max == 'banditCapsuleSpaceOdds1':
        banditCapsuleSpaceOdds1 += (100 - banditCapsuleSpaceOdds1)

    if spaceOdds1Max == 'pinkBooCapsuleSpaceOdds1':
        pinkBooCapsuleSpaceOdds1 += (100 - pinkBooCapsuleSpaceOdds1)

    if spaceOdds1Max == 'spinyCapsuleSpaceOdds1':
        spinyCapsuleSpaceOdds1 += (100 - spinyCapsuleSpaceOdds1)

    if spaceOdds1Max == 'podobooCapsuleSpaceOdds1':
        podobooCapsuleSpaceOdds1 += (100 - podobooCapsuleSpaceOdds1)

    if spaceOdds1Max == 'tweesterCapsuleSpaceOdds1':
        tweesterCapsuleSpaceOdds1 += (100 - tweesterCapsuleSpaceOdds1)

    if spaceOdds1Max == 'thwompCapsuleSpaceOdds1':
        thwompCapsuleSpaceOdds1 += (100 - thwompCapsuleSpaceOdds1)

    if spaceOdds1Max == 'warpCapsuleSpaceOdds1':
        warpCapsuleSpaceOdds1 += (100 - warpCapsuleSpaceOdds1)

    if spaceOdds1Max == 'bombCapsuleSpaceOdds1':
        bombCapsuleSpaceOdds1 += (100 - bombCapsuleSpaceOdds1)

    if spaceOdds1Max == 'fireballCapsuleSpaceOdds1':
        fireballCapsuleSpaceOdds1 += (100 - fireballCapsuleSpaceOdds1)

    if spaceOdds1Max == 'paraTroopaCapsuleSpaceOdds1':
        paraTroopaCapsuleSpaceOdds1 += (100 - paraTroopaCapsuleSpaceOdds1)

    if spaceOdds1Max == 'eggCapsuleSpaceOdds1':
        eggCapsuleSpaceOdds1 += (100 - eggCapsuleSpaceOdds1)

    if spaceOdds1Max == 'vacuumCapsuleSpaceOdds1':
        vacuumCapsuleSpaceOdds1 += (100 - vacuumCapsuleSpaceOdds1)

    if spaceOdds1Max == 'magicCapsuleSpaceOdds1':
        magicCapsuleSpaceOdds1 += (100 - magicCapsuleSpaceOdds1)

    if spaceOdds1Max == 'tripleCapsuleSpaceOdds1':
        tripleCapsuleSpaceOdds1 += (100 - tripleCapsuleSpaceOdds1)

    if spaceOdds1Max == 'koopaCapsuleSpaceOdds1':
        koopaCapsuleSpaceOdds1 += (100 - koopaCapsuleSpaceOdds1)

    if spaceOdds1Max == 'mysteryCapsuleSpaceOdds1':
        mysteryCapsuleSpaceOdds1 += (100 - mysteryCapsuleSpaceOdds1)

    if spaceOdds1Max == 'duelCapsuleSpaceOdds1':
        duelCapsuleSpaceOdds1 += (100 - duelCapsuleSpaceOdds1)

    if spaceOdds1Max == 'dkCapsuleSpaceOdds1':
        dkCapsuleSpaceOdds1 += (100 - dkCapsuleSpaceOdds1)

    if spaceOdds1Max == 'DxCapsuleDuelSpaceOdds1':
        DxCapsuleDuelSpaceOdds1 += (100 - DxCapsuleDuelSpaceOdds1)

    if spaceOdds1Max == 'DxCapsuleChanceSpaceOdds1':
        DxCapsuleChanceSpaceOdds1 += (100 - DxCapsuleChanceSpaceOdds1)

    if spaceOdds1Max == 'DxCapsuleBowserSpaceOdds1':
        DxCapsuleBowserSpaceOdds1 += (100 - DxCapsuleBowserSpaceOdds1)

    if spaceOdds1Max == 'DxCapsuleDonkeyKongSpaceOdds1':
        DxCapsuleDonkeyKongSpaceOdds1 += (100 - DxCapsuleDonkeyKongSpaceOdds1)

    if spaceOdds1Max == 'DxCapsulePinkBooSpaceOdds1':
        DxCapsulePinkBooSpaceOdds1 += (100 - DxCapsulePinkBooSpaceOdds1)

    if spaceOdds1Max == 'DxCapsuleSolunaSpaceOdds1':
        DxCapsuleSolunaSpaceOdds1 += (100 - DxCapsuleSolunaSpaceOdds1)
    
    if spaceOdds1Max == 'DxCapsuleChainChompSpaceOdds1':
        DxCapsuleChainChompSpaceOdds1 += (100 - DxCapsuleChainChompSpaceOdds1)

    if spaceOdds1Max == 'DxCapsuleWackyWatchSpaceOdds1':
        DxCapsuleWackyWatchSpaceOdds1 += (100 - DxCapsuleWackyWatchSpaceOdds1)

    if spaceOdds1Max == 'orbBagCapsuleSpaceOdds1':
        orbBagCapsuleSpaceOdds1 += (100 - orbBagCapsuleSpaceOdds1)

    if spaceOdds2Max == 'mushroomCapsuleSpaceOdds2':
        mushroomCapsuleSpaceOdds2 += (100 - mushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'goldenMushroomCapsuleSpaceOdds2':
        goldenMushroomCapsuleSpaceOdds2 += (100 - goldenMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'metalMushroomCapsuleSpaceOdds2':
        metalMushroomCapsuleSpaceOdds2 += (100 - metalMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'slowMushroomCapsuleSpaceOdds2':
        slowMushroomCapsuleSpaceOdds2 += (100 - slowMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'flutterCapsuleSpaceOdds2':
        flutterCapsuleSpaceOdds2 += (100 - flutterCapsuleSpaceOdds2)

    if spaceOdds2Max == 'cannonCapsuleSpaceOdds2':
        cannonCapsuleSpaceOdds2 += (100 - cannonCapsuleSpaceOdds2)

    if spaceOdds2Max == 'snackCapsuleSpaceOdds2':
        snackCapsuleSpaceOdds2 += (100 - snackCapsuleSpaceOdds2)

    if spaceOdds2Max == 'goombaCapsuleSpaceOdds2':
        goombaCapsuleSpaceOdds2 += (100 - goombaCapsuleSpaceOdds2)

    if spaceOdds2Max == 'hammerBroCapsuleSpaceOdds2':
        hammerBroCapsuleSpaceOdds2 += (100 - hammerBroCapsuleSpaceOdds2)

    if spaceOdds2Max == 'piranhaPlantCapsuleSpaceOdds2':
        piranhaPlantCapsuleSpaceOdds2 += (100 - piranhaPlantCapsuleSpaceOdds2)

    if spaceOdds2Max == 'kleptoCapsuleSpaceOdds2':
        kleptoCapsuleSpaceOdds2 += (100 - kleptoCapsuleSpaceOdds2)

    if spaceOdds2Max == 'kamekCapsuleSpaceOdds2':
        kamekCapsuleSpaceOdds2 += (100 - kamekCapsuleSpaceOdds2)

    if spaceOdds2Max == 'toadyCapsuleSpaceOdds2':
        toadyCapsuleSpaceOdds2 += (100 - toadyCapsuleSpaceOdds2)

    if spaceOdds2Max == 'mrBlizzardCapsuleSpaceOdds2':
        mrBlizzardCapsuleSpaceOdds2 += (100 - mrBlizzardCapsuleSpaceOdds2)

    if spaceOdds2Max == 'banditCapsuleSpaceOdds2':
        banditCapsuleSpaceOdds2 += (100 - banditCapsuleSpaceOdds2)

    if spaceOdds2Max == 'pinkBooCapsuleSpaceOdds2':
        pinkBooCapsuleSpaceOdds2 += (100 - pinkBooCapsuleSpaceOdds2)

    if spaceOdds2Max == 'spinyCapsuleSpaceOdds2':
        spinyCapsuleSpaceOdds2 += (100 - spinyCapsuleSpaceOdds2)

    if spaceOdds2Max == 'podobooCapsuleSpaceOdds2':
        podobooCapsuleSpaceOdds2 += (100 - podobooCapsuleSpaceOdds2)

    if spaceOdds2Max == 'tweesterCapsuleSpaceOdds2':
        tweesterCapsuleSpaceOdds2 += (100 - tweesterCapsuleSpaceOdds2)

    if spaceOdds2Max == 'thwompCapsuleSpaceOdds2':
        thwompCapsuleSpaceOdds2 += (100 - thwompCapsuleSpaceOdds2)

    if spaceOdds2Max == 'warpCapsuleSpaceOdds2':
        warpCapsuleSpaceOdds2 += (100 - warpCapsuleSpaceOdds2)

    if spaceOdds2Max == 'bombCapsuleSpaceOdds2':
        bombCapsuleSpaceOdds2 += (100 - bombCapsuleSpaceOdds2)

    if spaceOdds2Max == 'fireballCapsuleSpaceOdds2':
        fireballCapsuleSpaceOdds2 += (100 - fireballCapsuleSpaceOdds2)

    if spaceOdds2Max == 'paraTroopaCapsuleSpaceOdds2':
        paraTroopaCapsuleSpaceOdds2 += (100 - paraTroopaCapsuleSpaceOdds2)

    if spaceOdds2Max == 'eggCapsuleSpaceOdds2':
        eggCapsuleSpaceOdds2 += (100 - eggCapsuleSpaceOdds2)

    if spaceOdds2Max == 'vacuumCapsuleSpaceOdds2':
        vacuumCapsuleSpaceOdds2 += (100 - vacuumCapsuleSpaceOdds2)

    if spaceOdds2Max == 'magicCapsuleSpaceOdds2':
        magicCapsuleSpaceOdds2 += (100 - magicCapsuleSpaceOdds2)

    if spaceOdds2Max == 'tripleCapsuleSpaceOdds2':
        tripleCapsuleSpaceOdds2 += (100 - tripleCapsuleSpaceOdds2)

    if spaceOdds2Max == 'koopaCapsuleSpaceOdds2':
        koopaCapsuleSpaceOdds2 += (100 - koopaCapsuleSpaceOdds2)

    if spaceOdds2Max == 'mysteryCapsuleSpaceOdds2':
        mysteryCapsuleSpaceOdds2 += (100 - mysteryCapsuleSpaceOdds2)

    if spaceOdds2Max == 'duelCapsuleSpaceOdds2':
        duelCapsuleSpaceOdds2 += (100 - duelCapsuleSpaceOdds2)

    if spaceOdds2Max == 'dkCapsuleSpaceOdds2':
        dkCapsuleSpaceOdds2 += (100 - dkCapsuleSpaceOdds2)

    if spaceOdds2Max == 'orbBagCapsuleSpaceOdds2':
        orbBagCapsuleSpaceOdds2 += (100 - orbBagCapsuleSpaceOdds2)

    if spaceOdds2Max == 'DxCapsuleDuelSpaceOdds2':
        DxCapsuleDuelSpaceOdds2 += (100 - DxCapsuleDuelSpaceOdds2)
    
    if spaceOdds2Max == 'DxCapsuleChanceSpaceOdds2':
        DxCapsuleChanceSpaceOdds2 += (100 - DxCapsuleChanceSpaceOdds2)

    if spaceOdds2Max == 'DxCapsuleBowserSpaceOdds2':
        DxCapsuleBowserSpaceOdds2 += (100 - DxCapsuleBowserSpaceOdds2)

    if spaceOdds2Max == 'DxCapsuleDonkeyKongSpaceOdds2':
        DxCapsuleDonkeyKongSpaceOdds2 += (100 - DxCapsuleDonkeyKongSpaceOdds2)
    
    if spaceOdds2Max == 'DxCapsulePinkBooSpaceOdds2':
        DxCapsulePinkBooSpaceOdds2 += (100 - DxCapsulePinkBooSpaceOdds2)

    if spaceOdds2Max == 'DxCapsuleSolunaSpaceOdds2':
        DxCapsuleSolunaSpaceOdds2 += (100 - DxCapsuleSolunaSpaceOdds2)

    if spaceOdds2Max == 'DxCapsuleChainChompSpaceOdds2':
        DxCapsuleChainChompSpaceOdds2 += (100 - DxCapsuleChainChompSpaceOdds2)

    if spaceOdds2Max == 'DxCapsuleWackyWatchSpaceOdds2':
        DxCapsuleWackyWatchSpaceOdds2 += (100 - DxCapsuleWackyWatchSpaceOdds2)

    if spaceOdds34Max == 'mushroomCapsuleSpaceOdds34':
        mushroomCapsuleSpaceOdds34 += (100 - mushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'goldenMushroomCapsuleSpaceOdds34':
        goldenMushroomCapsuleSpaceOdds34 += (100 - goldenMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'metalMushroomCapsuleSpaceOdds34':
        metalMushroomCapsuleSpaceOdds34 += (100 - metalMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'slowMushroomCapsuleSpaceOdds34':
        slowMushroomCapsuleSpaceOdds34 += (100 - slowMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'flutterCapsuleSpaceOdds34':
        flutterCapsuleSpaceOdds34 += (100 - flutterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'cannonCapsuleSpaceOdds34':
        cannonCapsuleSpaceOdds34 += (100 - cannonCapsuleSpaceOdds34)

    if spaceOdds34Max == 'snackCapsuleSpaceOdds34':
        snackCapsuleSpaceOdds34 += (100 - snackCapsuleSpaceOdds34)

    if spaceOdds34Max == 'goombaCapsuleSpaceOdds34':
        goombaCapsuleSpaceOdds34 += (100 - goombaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'hammerBroCapsuleSpaceOdds34':
        hammerBroCapsuleSpaceOdds34 += (100 - hammerBroCapsuleSpaceOdds34)

    if spaceOdds34Max == 'piranhaPlantCapsuleSpaceOdds34':
        piranhaPlantCapsuleSpaceOdds34 += (100 - piranhaPlantCapsuleSpaceOdds34)

    if spaceOdds34Max == 'kleptoCapsuleSpaceOdds34':
        kleptoCapsuleSpaceOdds34 += (100 - kleptoCapsuleSpaceOdds34)

    if spaceOdds34Max == 'kamekCapsuleSpaceOdds34':
        kamekCapsuleSpaceOdds34 += (100 - kamekCapsuleSpaceOdds34)

    if spaceOdds34Max == 'toadyCapsuleSpaceOdds34':
        toadyCapsuleSpaceOdds34 += (100 - toadyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mrBlizzardCapsuleSpaceOdds34':
        mrBlizzardCapsuleSpaceOdds34 += (100 - mrBlizzardCapsuleSpaceOdds34)

    if spaceOdds34Max == 'banditCapsuleSpaceOdds34':
        banditCapsuleSpaceOdds34 += (100 - banditCapsuleSpaceOdds34)

    if spaceOdds34Max == 'pinkBooCapsuleSpaceOdds34':
        pinkBooCapsuleSpaceOdds34 += (100 - pinkBooCapsuleSpaceOdds34)

    if spaceOdds34Max == 'spinyCapsuleSpaceOdds34':
        spinyCapsuleSpaceOdds34 += (100 - spinyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'podobooCapsuleSpaceOdds34':
        podobooCapsuleSpaceOdds34 += (100 - podobooCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tweesterCapsuleSpaceOdds34':
        tweesterCapsuleSpaceOdds34 += (100 - tweesterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'thwompCapsuleSpaceOdds34':
        thwompCapsuleSpaceOdds34 += (100 - thwompCapsuleSpaceOdds34)

    if spaceOdds34Max == 'warpCapsuleSpaceOdds34':
        warpCapsuleSpaceOdds34 += (100 - warpCapsuleSpaceOdds34)

    if spaceOdds34Max == 'bombCapsuleSpaceOdds34':
        bombCapsuleSpaceOdds34 += (100 - bombCapsuleSpaceOdds34)

    if spaceOdds34Max == 'fireballCapsuleSpaceOdds34':
        fireballCapsuleSpaceOdds34 += (100 - fireballCapsuleSpaceOdds34)

    if spaceOdds34Max == 'paraTroopaCapsuleSpaceOdds34':
        paraTroopaCapsuleSpaceOdds34 += (100 - paraTroopaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'eggCapsuleSpaceOdds34':
        eggCapsuleSpaceOdds34 += (100 - eggCapsuleSpaceOdds34)

    if spaceOdds34Max == 'vacuumCapsuleSpaceOdds34':
        vacuumCapsuleSpaceOdds34 += (100 - vacuumCapsuleSpaceOdds34)

    if spaceOdds34Max == 'magicCapsuleSpaceOdds34':
        magicCapsuleSpaceOdds34 += (100 - magicCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tripleCapsuleSpaceOdds34':
        tripleCapsuleSpaceOdds34 += (100 - tripleCapsuleSpaceOdds34)

    if spaceOdds34Max == 'koopaCapsuleSpaceOdds34':
        koopaCapsuleSpaceOdds34 += (100 - koopaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mysteryCapsuleSpaceOdds34':
        mysteryCapsuleSpaceOdds34 += (100 - mysteryCapsuleSpaceOdds34)

    if spaceOdds34Max == 'duelCapsuleSpaceOdds34':
        duelCapsuleSpaceOdds34 += (100 - duelCapsuleSpaceOdds34)

    if spaceOdds34Max == 'dkCapsuleSpaceOdds34':
        dkCapsuleSpaceOdds34 += (100 - dkCapsuleSpaceOdds34)

    if spaceOdds34Max == 'orbBagCapsuleSpaceOdds34':
        orbBagCapsuleSpaceOdds34 += (100 - orbBagCapsuleSpaceOdds34)

    if spaceOdds34Max == 'DxCapsuleDuelSpaceOdds34':
        DxCapsuleDuelSpaceOdds34 += (100 - DxCapsuleDuelSpaceOdds34)

    if spaceOdds34Max == 'DxCapsuleChanceSpaceOdds34':
        DxCapsuleChanceSpaceOdds34 += (100 - DxCapsuleChanceSpaceOdds34)

    if spaceOdds34Max == 'DxCapsuleBowserSpaceOdds34':
        DxCapsuleBowserSpaceOdds34 += (100 - DxCapsuleBowserSpaceOdds34)

    if spaceOdds34Max == 'DxCapsuleDonkeyKongSpaceOdds34':
        DxCapsuleDonkeyKongSpaceOdds34 += (100 - DxCapsuleDonkeyKongSpaceOdds34)

    if spaceOdds34Max == 'DxCapsulePinkBooSpaceOdds34':
        DxCapsulePinkBooSpaceOdds34 += (100 - DxCapsulePinkBooSpaceOdds34)

    if spaceOdds34Max == 'DxCapsuleSolunaSpaceOdds34':
        DxCapsuleSolunaSpaceOdds34 += (100 - DxCapsuleSolunaSpaceOdds34)

    if spaceOdds34Max == 'DxCapsuleChainChompSpaceOdds34':
        DxCapsuleChainChompSpaceOdds34 += (100 - DxCapsuleChainChompSpaceOdds34)

    if spaceOdds34Max == 'DxCapsuleWackyWatchSpaceOdds34':
        DxCapsuleWackyWatchSpaceOdds34 += (100 - DxCapsuleWackyWatchSpaceOdds34)

    mushroomCapsuleShopOdds12 = str(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = str(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = str(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = str(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = str(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsuleShopOdds12 = str(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = str(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = str(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = str(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = str(goldenMushroomCapsuleSpaceOdds34)

    slowMushroomCapsuleShopOdds12 = str(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = str(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = str(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = str(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = str(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsuleShopOdds12 = str(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = str(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = str(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = str(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = str(metalMushroomCapsuleSpaceOdds34)

    flutterCapsuleShopOdds12 = str(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = str(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = str(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = str(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = str(flutterCapsuleSpaceOdds34)

    cannonCapsuleShopOdds12 = str(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = str(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = str(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = str(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = str(cannonCapsuleSpaceOdds34)

    snackCapsuleShopOdds12 = str(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = str(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = str(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = str(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = str(snackCapsuleSpaceOdds34)

    goombaCapsuleShopOdds12 = str(goombaCapsuleShopOdds12)
    goombaCapsuleShopOdds34 = str(goombaCapsuleShopOdds34)
    goombaCapsuleSpaceOdds1 = str(goombaCapsuleSpaceOdds1)
    goombaCapsuleSpaceOdds2 = str(goombaCapsuleSpaceOdds2)
    goombaCapsuleSpaceOdds34 = str(goombaCapsuleSpaceOdds34)

    hammerBroCapsuleShopOdds12 = str(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = str(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = str(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = str(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = str(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsuleShopOdds12 = str(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = str(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = str(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = str(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = str(piranhaPlantCapsuleSpaceOdds34)

    kleptoCapsuleShopOdds12 = str(kleptoCapsuleShopOdds12)
    kleptoCapsuleShopOdds34 = str(kleptoCapsuleShopOdds34)
    kleptoCapsuleSpaceOdds1 = str(kleptoCapsuleSpaceOdds1)
    kleptoCapsuleSpaceOdds2 = str(kleptoCapsuleSpaceOdds2)
    kleptoCapsuleSpaceOdds34 = str(kleptoCapsuleSpaceOdds34)

    kamekCapsuleShopOdds12 = str(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = str(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = str(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = str(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = str(kamekCapsuleSpaceOdds34)

    toadyCapsuleShopOdds12 = str(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = str(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = str(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = str(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = str(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsuleShopOdds12 = str(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = str(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = str(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = str(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = str(mrBlizzardCapsuleSpaceOdds34)

    banditCapsuleShopOdds12 = str(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = str(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = str(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = str(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = str(banditCapsuleSpaceOdds34)

    pinkBooCapsuleShopOdds12 = str(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = str(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = str(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = str(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = str(pinkBooCapsuleSpaceOdds34)

    spinyCapsuleShopOdds12 = str(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = str(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = str(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = str(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = str(spinyCapsuleSpaceOdds34)

    podobooCapsuleShopOdds12 = str(podobooCapsuleShopOdds12)
    podobooCapsuleShopOdds34 = str(podobooCapsuleShopOdds34)
    podobooCapsuleSpaceOdds1 = str(podobooCapsuleSpaceOdds1)
    podobooCapsuleSpaceOdds2 = str(podobooCapsuleSpaceOdds2)
    podobooCapsuleSpaceOdds34 = str(podobooCapsuleSpaceOdds34)

    tweesterCapsuleShopOdds12 = str(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = str(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = str(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = str(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = str(tweesterCapsuleSpaceOdds34)

    thwompCapsuleShopOdds12 = str(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = str(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = str(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = str(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = str(thwompCapsuleSpaceOdds34)

    warpCapsuleShopOdds12 = str(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = str(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = str(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = str(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = str(warpCapsuleSpaceOdds34)

    bombCapsuleShopOdds12 = str(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = str(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = str(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = str(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = str(bombCapsuleSpaceOdds34)

    fireballCapsuleShopOdds12 = str(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = str(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = str(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = str(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = str(fireballCapsuleSpaceOdds34)

    paraTroopaCapsuleShopOdds12 = str(paraTroopaCapsuleShopOdds12)
    paraTroopaCapsuleShopOdds34 = str(paraTroopaCapsuleShopOdds34)
    paraTroopaCapsuleSpaceOdds1 = str(paraTroopaCapsuleSpaceOdds1)
    paraTroopaCapsuleSpaceOdds2 = str(paraTroopaCapsuleSpaceOdds2)
    paraTroopaCapsuleSpaceOdds34 = str(paraTroopaCapsuleSpaceOdds34)

    eggCapsuleShopOdds12 = str(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = str(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = str(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = str(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = str(eggCapsuleSpaceOdds34)

    vacuumCapsuleShopOdds12 = str(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = str(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = str(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = str(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = str(vacuumCapsuleSpaceOdds34)

    magicCapsuleShopOdds12 = str(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = str(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = str(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = str(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = str(magicCapsuleSpaceOdds34)

    tripleCapsuleShopOdds12 = str(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = str(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = str(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = str(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = str(tripleCapsuleSpaceOdds34)

    koopaCapsuleShopOdds12 = str(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = str(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = str(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = str(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = str(koopaCapsuleSpaceOdds34)

    cursedMushroomShopOdds12 = str(cursedMushroomShopOdds12)
    cursedMushroomShopOdds34 = str(cursedMushroomShopOdds34)
    cursedMushroomSpaceOdds1 = str(cursedMushroomSpaceOdds1)
    cursedMushroomSpaceOdds2 = str(cursedMushroomSpaceOdds2)
    cursedMushroomSpaceOdds34 = str(cursedMushroomSpaceOdds34)

    orbBagCapsuleShopOdds12 = str(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = str(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = str(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = str(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = str(orbBagCapsuleSpaceOdds34)

    mysteryCapsuleShopOdds12 = str(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = str(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = str(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = str(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = str(mysteryCapsuleSpaceOdds34)

    dkCapsuleShopOdds12 = str(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = str(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = str(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = str(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = str(dkCapsuleSpaceOdds34)

    duelCapsuleShopOdds12 = str(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = str(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = str(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = str(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = str(duelCapsuleSpaceOdds34)

    DxCapsuleDuelShopOdds12 = str(DxCapsuleDuelShopOdds12)
    DxCapsuleDuelShopOdds34 = str(DxCapsuleDuelShopOdds34)
    DxCapsuleDuelSpaceOdds1 = str(DxCapsuleDuelSpaceOdds1)
    DxCapsuleDuelSpaceOdds2 = str(DxCapsuleDuelSpaceOdds2)
    DxCapsuleDuelSpaceOdds34 = str(DxCapsuleDuelSpaceOdds34)

    DxCapsuleChanceShopOdds12 = str(DxCapsuleChanceShopOdds12)
    DxCapsuleChanceShopOdds34 = str(DxCapsuleChanceShopOdds34)
    DxCapsuleChanceSpaceOdds1 = str(DxCapsuleChanceSpaceOdds1)
    DxCapsuleChanceSpaceOdds2 = str(DxCapsuleChanceSpaceOdds2)
    DxCapsuleChanceSpaceOdds34 = str(DxCapsuleChanceSpaceOdds34)

    DxCapsuleBowserShopOdds12 = str(DxCapsuleBowserShopOdds12)
    DxCapsuleBowserShopOdds34 = str(DxCapsuleBowserShopOdds34)
    DxCapsuleBowserSpaceOdds1 = str(DxCapsuleBowserSpaceOdds1)
    DxCapsuleBowserSpaceOdds2 = str(DxCapsuleBowserSpaceOdds2)
    DxCapsuleBowserSpaceOdds34 = str(DxCapsuleBowserSpaceOdds34)

    DxCapsuleDonkeyKongShopOdds12 = str(DxCapsuleDonkeyKongShopOdds12)
    DxCapsuleDonkeyKongShopOdds34 = str(DxCapsuleDonkeyKongShopOdds34)
    DxCapsuleDonkeyKongSpaceOdds1 = str(DxCapsuleDonkeyKongSpaceOdds1)
    DxCapsuleDonkeyKongSpaceOdds2 = str(DxCapsuleDonkeyKongSpaceOdds2)
    DxCapsuleDonkeyKongSpaceOdds34 = str(DxCapsuleDonkeyKongSpaceOdds34)

    DxCapsulePinkBooShopOdds12 = str(DxCapsulePinkBooShopOdds12)
    DxCapsulePinkBooShopOdds34 = str(DxCapsulePinkBooShopOdds34)
    DxCapsulePinkBooSpaceOdds1 = str(DxCapsulePinkBooSpaceOdds1)
    DxCapsulePinkBooSpaceOdds2 = str(DxCapsulePinkBooSpaceOdds2)
    DxCapsulePinkBooSpaceOdds34 = str(DxCapsulePinkBooSpaceOdds34)

    DxCapsuleSolunaShopOdds12 = str(DxCapsuleSolunaShopOdds12)
    DxCapsuleSolunaShopOdds34 = str(DxCapsuleSolunaShopOdds34)
    DxCapsuleSolunaSpaceOdds1 = str(DxCapsuleSolunaSpaceOdds1)
    DxCapsuleSolunaSpaceOdds2 = str(DxCapsuleSolunaSpaceOdds2)
    DxCapsuleSolunaSpaceOdds34 = str(DxCapsuleSolunaSpaceOdds34)

    DxCapsuleChainChompShopOdds12 = str(DxCapsuleChainChompShopOdds12)
    DxCapsuleChainChompShopOdds34 = str(DxCapsuleChainChompShopOdds34)
    DxCapsuleChainChompSpaceOdds1 = str(DxCapsuleChainChompSpaceOdds1)
    DxCapsuleChainChompSpaceOdds2 = str(DxCapsuleChainChompSpaceOdds2)
    DxCapsuleChainChompSpaceOdds34 = str(DxCapsuleChainChompSpaceOdds34)

    DxCapsuleWackyWatchShopOdds12 = str(DxCapsuleWackyWatchShopOdds12)
    DxCapsuleWackyWatchShopOdds34 = str(DxCapsuleWackyWatchShopOdds34)
    DxCapsuleWackyWatchSpaceOdds1 = str(DxCapsuleWackyWatchSpaceOdds1)
    DxCapsuleWackyWatchSpaceOdds2 = str(DxCapsuleWackyWatchSpaceOdds2)
    DxCapsuleWackyWatchSpaceOdds34 = str(DxCapsuleWackyWatchSpaceOdds34)

    def convert_to_hex_weight(weight):
        try:
            weight_hex = hex(int(weight))
            if len(weight_hex) == 4:
                return weight_hex[2:]  # Remove '0x' prefix
            elif len(weight_hex) == 3:
                return "0" + weight_hex[2:]  # Add leading zero
            return weight_hex[2:]  # Return as is for other lengths
        except:
            return "00"  # Return default value on error

    # Usage
    mushroomCapsuleShopOdds12 = convert_to_hex_weight(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = convert_to_hex_weight(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = convert_to_hex_weight(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = convert_to_hex_weight(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = convert_to_hex_weight(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsulePrice1 = convert_to_hex_weight(goldenMushroomCapsulePrice1)
    goldenMushroomCapsulePrice2 = convert_to_hex_weight(goldenMushroomCapsulePrice2)
    goldenMushroomCapsulePrice34 = convert_to_hex_weight(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds34)

    slowMushroomCapsulePrice1 = convert_to_hex_weight(slowMushroomCapsulePrice1)
    slowMushroomCapsulePrice2 = convert_to_hex_weight(slowMushroomCapsulePrice2)
    slowMushroomCapsulePrice34 = convert_to_hex_weight(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = convert_to_hex_weight(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = convert_to_hex_weight(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsulePrice1 = convert_to_hex_weight(metalMushroomCapsulePrice1)
    metalMushroomCapsulePrice2 = convert_to_hex_weight(metalMushroomCapsulePrice2)
    metalMushroomCapsulePrice34 = convert_to_hex_weight(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = convert_to_hex_weight(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = convert_to_hex_weight(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds34)

    flutterCapsulePrice1 = convert_to_hex_weight(flutterCapsulePrice1)
    flutterCapsulePrice2 = convert_to_hex_weight(flutterCapsulePrice2)
    flutterCapsulePrice34 = convert_to_hex_weight(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = convert_to_hex_weight(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = convert_to_hex_weight(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = convert_to_hex_weight(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = convert_to_hex_weight(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = convert_to_hex_weight(flutterCapsuleSpaceOdds34)

    cannonCapsulePrice1 = convert_to_hex_weight(cannonCapsulePrice1)
    cannonCapsulePrice2 = convert_to_hex_weight(cannonCapsulePrice2)
    cannonCapsulePrice34 = convert_to_hex_weight(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = convert_to_hex_weight(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = convert_to_hex_weight(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = convert_to_hex_weight(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = convert_to_hex_weight(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = convert_to_hex_weight(cannonCapsuleSpaceOdds34)

    snackCapsulePrice1 = convert_to_hex_weight(snackCapsulePrice1)
    snackCapsulePrice2 = convert_to_hex_weight(snackCapsulePrice2)
    snackCapsulePrice34 = convert_to_hex_weight(snackCapsulePrice34)
    snackCapsuleShopOdds12 = convert_to_hex_weight(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = convert_to_hex_weight(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = convert_to_hex_weight(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = convert_to_hex_weight(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = convert_to_hex_weight(snackCapsuleSpaceOdds34)

    goombaCapsulePrice1 = convert_to_hex_weight(goombaCapsulePrice1)
    goombaCapsulePrice2 = convert_to_hex_weight(goombaCapsulePrice2)
    goombaCapsulePrice34 = convert_to_hex_weight(goombaCapsulePrice34)
    goombaCapsuleShopOdds12 = convert_to_hex_weight(goombaCapsuleShopOdds12)
    goombaCapsuleShopOdds34 = convert_to_hex_weight(goombaCapsuleShopOdds34)
    goombaCapsuleSpaceOdds1 = convert_to_hex_weight(goombaCapsuleSpaceOdds1)
    goombaCapsuleSpaceOdds2 = convert_to_hex_weight(goombaCapsuleSpaceOdds2)
    goombaCapsuleSpaceOdds34 = convert_to_hex_weight(goombaCapsuleSpaceOdds34)

    hammerBroCapsulePrice1 = convert_to_hex_weight(hammerBroCapsulePrice1)
    hammerBroCapsulePrice2 = convert_to_hex_weight(hammerBroCapsulePrice2)
    hammerBroCapsulePrice34 = convert_to_hex_weight(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = convert_to_hex_weight(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = convert_to_hex_weight(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsulePrice1 = convert_to_hex_weight(piranhaPlantCapsulePrice1)
    piranhaPlantCapsulePrice2 = convert_to_hex_weight(piranhaPlantCapsulePrice2)
    piranhaPlantCapsulePrice34 = convert_to_hex_weight(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds34)

    kleptoCapsulePrice1 = convert_to_hex_weight(kleptoCapsulePrice1)
    kleptoCapsulePrice2 = convert_to_hex_weight(kleptoCapsulePrice2)
    kleptoCapsulePrice34 = convert_to_hex_weight(kleptoCapsulePrice34)
    kleptoCapsuleShopOdds12 = convert_to_hex_weight(kleptoCapsuleShopOdds12)
    kleptoCapsuleShopOdds34 = convert_to_hex_weight(kleptoCapsuleShopOdds34)
    kleptoCapsuleSpaceOdds1 = convert_to_hex_weight(kleptoCapsuleSpaceOdds1)
    kleptoCapsuleSpaceOdds2 = convert_to_hex_weight(kleptoCapsuleSpaceOdds2)
    kleptoCapsuleSpaceOdds34 = convert_to_hex_weight(kleptoCapsuleSpaceOdds34)

    kamekCapsulePrice1 = convert_to_hex_weight(kamekCapsulePrice1)
    kamekCapsulePrice2 = convert_to_hex_weight(kamekCapsulePrice2)
    kamekCapsulePrice34 = convert_to_hex_weight(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = convert_to_hex_weight(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = convert_to_hex_weight(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = convert_to_hex_weight(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = convert_to_hex_weight(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = convert_to_hex_weight(kamekCapsuleSpaceOdds34)

    toadyCapsulePrice1 = convert_to_hex_weight(toadyCapsulePrice1)
    toadyCapsulePrice2 = convert_to_hex_weight(toadyCapsulePrice2)
    toadyCapsulePrice34 = convert_to_hex_weight(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = convert_to_hex_weight(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = convert_to_hex_weight(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = convert_to_hex_weight(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = convert_to_hex_weight(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = convert_to_hex_weight(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsulePrice1 = convert_to_hex_weight(mrBlizzardCapsulePrice1)
    mrBlizzardCapsulePrice2 = convert_to_hex_weight(mrBlizzardCapsulePrice2)
    mrBlizzardCapsulePrice34 = convert_to_hex_weight(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds34)

    banditCapsulePrice1 = convert_to_hex_weight(banditCapsulePrice1)
    banditCapsulePrice2 = convert_to_hex_weight(banditCapsulePrice2)
    banditCapsulePrice34 = convert_to_hex_weight(banditCapsulePrice34)
    banditCapsuleShopOdds12 = convert_to_hex_weight(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = convert_to_hex_weight(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = convert_to_hex_weight(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = convert_to_hex_weight(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = convert_to_hex_weight(banditCapsuleSpaceOdds34)

    pinkBooCapsulePrice1 = convert_to_hex_weight(pinkBooCapsulePrice1)
    pinkBooCapsulePrice2 = convert_to_hex_weight(pinkBooCapsulePrice2)
    pinkBooCapsulePrice34 = convert_to_hex_weight(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = convert_to_hex_weight(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = convert_to_hex_weight(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds34)

    spinyCapsulePrice1 = convert_to_hex_weight(spinyCapsulePrice1)
    spinyCapsulePrice2 = convert_to_hex_weight(spinyCapsulePrice2)
    spinyCapsulePrice34 = convert_to_hex_weight(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = convert_to_hex_weight(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = convert_to_hex_weight(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = convert_to_hex_weight(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = convert_to_hex_weight(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = convert_to_hex_weight(spinyCapsuleSpaceOdds34)

    podobooCapsulePrice1 = convert_to_hex_weight(podobooCapsulePrice1)
    podobooCapsulePrice2 = convert_to_hex_weight(podobooCapsulePrice2)
    podobooCapsulePrice34 = convert_to_hex_weight(podobooCapsulePrice34)
    podobooCapsuleShopOdds12 = convert_to_hex_weight(podobooCapsuleShopOdds12)
    podobooCapsuleShopOdds34 = convert_to_hex_weight(podobooCapsuleShopOdds34)
    podobooCapsuleSpaceOdds1 = convert_to_hex_weight(podobooCapsuleSpaceOdds1)
    podobooCapsuleSpaceOdds2 = convert_to_hex_weight(podobooCapsuleSpaceOdds2)
    podobooCapsuleSpaceOdds34 = convert_to_hex_weight(podobooCapsuleSpaceOdds34)

    tweesterCapsulePrice1 = convert_to_hex_weight(tweesterCapsulePrice1)
    tweesterCapsulePrice2 = convert_to_hex_weight(tweesterCapsulePrice2)
    tweesterCapsulePrice34 = convert_to_hex_weight(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = convert_to_hex_weight(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = convert_to_hex_weight(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = convert_to_hex_weight(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = convert_to_hex_weight(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = convert_to_hex_weight(tweesterCapsuleSpaceOdds34)

    thwompCapsulePrice1 = convert_to_hex_weight(thwompCapsulePrice1)
    thwompCapsulePrice2 = convert_to_hex_weight(thwompCapsulePrice2)
    thwompCapsulePrice34 = convert_to_hex_weight(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = convert_to_hex_weight(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = convert_to_hex_weight(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = convert_to_hex_weight(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = convert_to_hex_weight(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = convert_to_hex_weight(thwompCapsuleSpaceOdds34)

    warpCapsulePrice1 = convert_to_hex_weight(warpCapsulePrice1)
    warpCapsulePrice2 = convert_to_hex_weight(warpCapsulePrice2)
    warpCapsulePrice34 = convert_to_hex_weight(warpCapsulePrice34)
    warpCapsuleShopOdds12 = convert_to_hex_weight(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = convert_to_hex_weight(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = convert_to_hex_weight(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = convert_to_hex_weight(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = convert_to_hex_weight(warpCapsuleSpaceOdds34)

    bombCapsulePrice1 = convert_to_hex_weight(bombCapsulePrice1)
    bombCapsulePrice2 = convert_to_hex_weight(bombCapsulePrice2)
    bombCapsulePrice34 = convert_to_hex_weight(bombCapsulePrice34)
    bombCapsuleShopOdds12 = convert_to_hex_weight(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = convert_to_hex_weight(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = convert_to_hex_weight(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = convert_to_hex_weight(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = convert_to_hex_weight(bombCapsuleSpaceOdds34)

    fireballCapsulePrice1 = convert_to_hex_weight(fireballCapsulePrice1)
    fireballCapsulePrice2 = convert_to_hex_weight(fireballCapsulePrice2)
    fireballCapsulePrice34 = convert_to_hex_weight(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = convert_to_hex_weight(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = convert_to_hex_weight(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = convert_to_hex_weight(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = convert_to_hex_weight(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = convert_to_hex_weight(fireballCapsuleSpaceOdds34)

    paraTroopaCapsulePrice1 = convert_to_hex_weight(paraTroopaCapsulePrice1)
    paraTroopaCapsulePrice2 = convert_to_hex_weight(paraTroopaCapsulePrice2)
    paraTroopaCapsulePrice34 = convert_to_hex_weight(paraTroopaCapsulePrice34)
    paraTroopaCapsuleShopOdds12 = convert_to_hex_weight(paraTroopaCapsuleShopOdds12)
    paraTroopaCapsuleShopOdds34 = convert_to_hex_weight(paraTroopaCapsuleShopOdds34)
    paraTroopaCapsuleSpaceOdds1 = convert_to_hex_weight(paraTroopaCapsuleSpaceOdds1)
    paraTroopaCapsuleSpaceOdds2 = convert_to_hex_weight(paraTroopaCapsuleSpaceOdds2)
    paraTroopaCapsuleSpaceOdds34 = convert_to_hex_weight(paraTroopaCapsuleSpaceOdds34)

    eggCapsulePrice1 = convert_to_hex_weight(eggCapsulePrice1)
    eggCapsulePrice2 = convert_to_hex_weight(eggCapsulePrice2)
    eggCapsulePrice34 = convert_to_hex_weight(eggCapsulePrice34)
    eggCapsuleShopOdds12 = convert_to_hex_weight(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = convert_to_hex_weight(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = convert_to_hex_weight(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = convert_to_hex_weight(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = convert_to_hex_weight(eggCapsuleSpaceOdds34)

    vacuumCapsulePrice1 = convert_to_hex_weight(vacuumCapsulePrice1)
    vacuumCapsulePrice2 = convert_to_hex_weight(vacuumCapsulePrice2)
    vacuumCapsulePrice34 = convert_to_hex_weight(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = convert_to_hex_weight(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = convert_to_hex_weight(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = convert_to_hex_weight(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = convert_to_hex_weight(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = convert_to_hex_weight(vacuumCapsuleSpaceOdds34)

    magicCapsulePrice1 = convert_to_hex_weight(magicCapsulePrice1)
    magicCapsulePrice2 = convert_to_hex_weight(magicCapsulePrice2)
    magicCapsulePrice34 = convert_to_hex_weight(magicCapsulePrice34)
    magicCapsuleShopOdds12 = convert_to_hex_weight(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = convert_to_hex_weight(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = convert_to_hex_weight(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = convert_to_hex_weight(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = convert_to_hex_weight(magicCapsuleSpaceOdds34)

    tripleCapsulePrice1 = convert_to_hex_weight(tripleCapsulePrice1)
    tripleCapsulePrice2 = convert_to_hex_weight(tripleCapsulePrice2)
    tripleCapsulePrice34 = convert_to_hex_weight(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = convert_to_hex_weight(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = convert_to_hex_weight(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = convert_to_hex_weight(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = convert_to_hex_weight(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = convert_to_hex_weight(tripleCapsuleSpaceOdds34)

    koopaCapsulePrice1 = convert_to_hex_weight(koopaCapsulePrice1)
    koopaCapsulePrice2 = convert_to_hex_weight(koopaCapsulePrice2)
    koopaCapsulePrice34 = convert_to_hex_weight(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = convert_to_hex_weight(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = convert_to_hex_weight(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = convert_to_hex_weight(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = convert_to_hex_weight(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = convert_to_hex_weight(koopaCapsuleSpaceOdds34)

    cursedMushroomPrice1 = convert_to_hex_weight(cursedMushroomPrice1)
    cursedMushroomPrice2 = convert_to_hex_weight(cursedMushroomPrice2)
    cursedMushroomPrice34 = convert_to_hex_weight(cursedMushroomPrice34)
    cursedMushroomShopOdds12 = convert_to_hex_weight(cursedMushroomShopOdds12)
    cursedMushroomShopOdds34 = convert_to_hex_weight(cursedMushroomShopOdds34)
    cursedMushroomSpaceOdds1 = convert_to_hex_weight(cursedMushroomSpaceOdds1)
    cursedMushroomSpaceOdds2 = convert_to_hex_weight(cursedMushroomSpaceOdds2)
    cursedMushroomSpaceOdds34 = convert_to_hex_weight(cursedMushroomSpaceOdds34)

    orbBagCapsulePrice1 = convert_to_hex_weight(orbBagCapsulePrice1)
    orbBagCapsulePrice2 = convert_to_hex_weight(orbBagCapsulePrice2)
    orbBagCapsulePrice34 = convert_to_hex_weight(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = convert_to_hex_weight(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = convert_to_hex_weight(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = convert_to_hex_weight(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = convert_to_hex_weight(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = convert_to_hex_weight(orbBagCapsuleSpaceOdds34)

    mysteryCapsulePrice1 = convert_to_hex_weight(mysteryCapsulePrice1)
    mysteryCapsulePrice2 = convert_to_hex_weight(mysteryCapsulePrice2)
    mysteryCapsulePrice34 = convert_to_hex_weight(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = convert_to_hex_weight(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = convert_to_hex_weight(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = convert_to_hex_weight(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = convert_to_hex_weight(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = convert_to_hex_weight(mysteryCapsuleSpaceOdds34)

    dkCapsulePrice1 = convert_to_hex_weight(dkCapsulePrice1)
    dkCapsulePrice2 = convert_to_hex_weight(dkCapsulePrice2)
    dkCapsulePrice34 = convert_to_hex_weight(dkCapsulePrice34)
    dkCapsuleShopOdds12 = convert_to_hex_weight(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = convert_to_hex_weight(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = convert_to_hex_weight(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = convert_to_hex_weight(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = convert_to_hex_weight(dkCapsuleSpaceOdds34)

    duelCapsulePrice1 = convert_to_hex_weight(duelCapsulePrice1)
    duelCapsulePrice2 = convert_to_hex_weight(duelCapsulePrice2)
    duelCapsulePrice34 = convert_to_hex_weight(duelCapsulePrice34)
    duelCapsuleShopOdds12 = convert_to_hex_weight(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = convert_to_hex_weight(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = convert_to_hex_weight(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = convert_to_hex_weight(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = convert_to_hex_weight(duelCapsuleSpaceOdds34)

    DxCapsuleSolunaPrice1 = convert_to_hex_weight(DxCapsuleSolunaPrice1)
    DxCapsuleSolunaPrice2 = convert_to_hex_weight(DxCapsuleSolunaPrice2)
    DxCapsuleSolunaPrice34 = convert_to_hex_weight(DxCapsuleSolunaPrice34)
    DxCapsuleSolunaShopOdds12 = convert_to_hex_weight(DxCapsuleSolunaShopOdds12)
    DxCapsuleSolunaShopOdds34 = convert_to_hex_weight(DxCapsuleSolunaShopOdds34)
    DxCapsuleSolunaSpaceOdds1 = convert_to_hex_weight(DxCapsuleSolunaSpaceOdds1)
    DxCapsuleSolunaSpaceOdds2 = convert_to_hex_weight(DxCapsuleSolunaSpaceOdds2)
    DxCapsuleSolunaSpaceOdds34 = convert_to_hex_weight(DxCapsuleSolunaSpaceOdds34)

    DxCapsuleChainChompPrice1 = convert_to_hex_weight(DxCapsuleChainChompPrice1)
    DxCapsuleChainChompPrice2 = convert_to_hex_weight(DxCapsuleChainChompPrice2)
    DxCapsuleChainChompPrice34 = convert_to_hex_weight(DxCapsuleChainChompPrice34)
    DxCapsuleChainChompShopOdds12 = convert_to_hex_weight(DxCapsuleChainChompShopOdds12)
    DxCapsuleChainChompShopOdds34 = convert_to_hex_weight(DxCapsuleChainChompShopOdds34)
    DxCapsuleChainChompSpaceOdds1 = convert_to_hex_weight(DxCapsuleChainChompSpaceOdds1)
    DxCapsuleChainChompSpaceOdds2 = convert_to_hex_weight(DxCapsuleChainChompSpaceOdds2)
    DxCapsuleChainChompSpaceOdds34 = convert_to_hex_weight(DxCapsuleChainChompSpaceOdds34)

    DxCapsuleWackyWatchPrice1 = convert_to_hex_weight(DxCapsuleWackyWatchPrice1)
    DxCapsuleWackyWatchPrice2 = convert_to_hex_weight(DxCapsuleWackyWatchPrice2)
    DxCapsuleWackyWatchPrice34 = convert_to_hex_weight(DxCapsuleWackyWatchPrice34)
    DxCapsuleWackyWatchShopOdds12 = convert_to_hex_weight(DxCapsuleWackyWatchShopOdds12)
    DxCapsuleWackyWatchShopOdds34 = convert_to_hex_weight(DxCapsuleWackyWatchShopOdds34)
    DxCapsuleWackyWatchSpaceOdds1 = convert_to_hex_weight(DxCapsuleWackyWatchSpaceOdds1)
    DxCapsuleWackyWatchSpaceOdds2 = convert_to_hex_weight(DxCapsuleWackyWatchSpaceOdds2)
    DxCapsuleWackyWatchSpaceOdds34 = convert_to_hex_weight(DxCapsuleWackyWatchSpaceOdds34)

    DxCapsuleBowserPrice1 = convert_to_hex_weight(DxCapsuleBowserPrice1)
    DxCapsuleBowserPrice2 = convert_to_hex_weight(DxCapsuleBowserPrice2)
    DxCapsuleBowserPrice34 = convert_to_hex_weight(DxCapsuleBowserPrice34)
    DxCapsuleBowserShopOdds12 = convert_to_hex_weight(DxCapsuleBowserShopOdds12)
    DxCapsuleBowserShopOdds34 = convert_to_hex_weight(DxCapsuleBowserShopOdds34)
    DxCapsuleBowserSpaceOdds1 = convert_to_hex_weight(DxCapsuleBowserSpaceOdds1)
    DxCapsuleBowserSpaceOdds2 = convert_to_hex_weight(DxCapsuleBowserSpaceOdds2)
    DxCapsuleBowserSpaceOdds34 = convert_to_hex_weight(DxCapsuleBowserSpaceOdds34)

    DxCapsuleDonkeyKongPrice1 = convert_to_hex_weight(DxCapsuleDonkeyKongPrice1)
    DxCapsuleDonkeyKongPrice2 = convert_to_hex_weight(DxCapsuleDonkeyKongPrice2)
    DxCapsuleDonkeyKongPrice34 = convert_to_hex_weight(DxCapsuleDonkeyKongPrice34)
    DxCapsuleDonkeyKongShopOdds12 = convert_to_hex_weight(DxCapsuleDonkeyKongShopOdds12)
    DxCapsuleDonkeyKongShopOdds34 = convert_to_hex_weight(DxCapsuleDonkeyKongShopOdds34)
    DxCapsuleDonkeyKongSpaceOdds1 = convert_to_hex_weight(DxCapsuleDonkeyKongSpaceOdds1)
    DxCapsuleDonkeyKongSpaceOdds2 = convert_to_hex_weight(DxCapsuleDonkeyKongSpaceOdds2)
    DxCapsuleDonkeyKongSpaceOdds34 = convert_to_hex_weight(DxCapsuleDonkeyKongSpaceOdds34)
    
    DxCapsulePinkBooPrice1 = convert_to_hex_weight(DxCapsulePinkBooPrice1)
    DxCapsulePinkBooPrice2 = convert_to_hex_weight(DxCapsulePinkBooPrice2)
    DxCapsulePinkBooPrice34 = convert_to_hex_weight(DxCapsulePinkBooPrice34)
    DxCapsulePinkBooShopOdds12 = convert_to_hex_weight(DxCapsulePinkBooShopOdds12)
    DxCapsulePinkBooShopOdds34 = convert_to_hex_weight(DxCapsulePinkBooShopOdds34)
    DxCapsulePinkBooSpaceOdds1 = convert_to_hex_weight(DxCapsulePinkBooSpaceOdds1)
    DxCapsulePinkBooSpaceOdds2 = convert_to_hex_weight(DxCapsulePinkBooSpaceOdds2)
    DxCapsulePinkBooSpaceOdds34 = convert_to_hex_weight(DxCapsulePinkBooSpaceOdds34)
    
    DxCapsuleDuelPrice1 = convert_to_hex_weight(DxCapsuleDuelPrice1)
    DxCapsuleDuelPrice2 = convert_to_hex_weight(DxCapsuleDuelPrice2)
    DxCapsuleDuelPrice34 = convert_to_hex_weight(DxCapsuleDuelPrice34)
    DxCapsuleDuelShopOdds12 = convert_to_hex_weight(DxCapsuleDuelShopOdds12)
    DxCapsuleDuelShopOdds34 = convert_to_hex_weight(DxCapsuleDuelShopOdds34)
    DxCapsuleDuelSpaceOdds1 = convert_to_hex_weight(DxCapsuleDuelSpaceOdds1)
    DxCapsuleDuelSpaceOdds2 = convert_to_hex_weight(DxCapsuleDuelSpaceOdds2)
    DxCapsuleDuelSpaceOdds34 = convert_to_hex_weight(DxCapsuleDuelSpaceOdds34)

    DxCapsuleChancePrice1 = convert_to_hex_weight(DxCapsuleChancePrice1)
    DxCapsuleChancePrice2 = convert_to_hex_weight(DxCapsuleChancePrice2)
    DxCapsuleChancePrice34 = convert_to_hex_weight(DxCapsuleChancePrice34)
    DxCapsuleChanceShopOdds12 = convert_to_hex_weight(DxCapsuleChanceShopOdds12)
    DxCapsuleChanceShopOdds34 = convert_to_hex_weight(DxCapsuleChanceShopOdds34)
    DxCapsuleChanceSpaceOdds1 = convert_to_hex_weight(DxCapsuleChanceSpaceOdds1)
    DxCapsuleChanceSpaceOdds2 = convert_to_hex_weight(DxCapsuleChanceSpaceOdds2)
    DxCapsuleChanceSpaceOdds34 = convert_to_hex_weight(DxCapsuleChanceSpaceOdds34)

    mushroomSpaceOdds1 = mushroomCapsuleSpaceOdds1
    mushroomSpaceOdds2 = mushroomCapsuleSpaceOdds2
    mushroomSpaceOdds3 = mushroomCapsuleSpaceOdds34
    mushroomSpaceOdds4 = mushroomCapsuleSpaceOdds34
    mushroomShopOdds123 = mushroomCapsuleShopOdds12
    mushroomShopOdds4 = mushroomCapsuleShopOdds34

    goldenMushroomPrice1 = goldenMushroomCapsulePrice1
    goldenMushroomPrice2 = goldenMushroomCapsulePrice2
    goldenMushroomPrice34 = goldenMushroomCapsulePrice34
    goldenMushroomSpaceOdds1 = goldenMushroomCapsuleSpaceOdds1
    goldenMushroomSpaceOdds2 = goldenMushroomCapsuleSpaceOdds2
    goldenMushroomSpaceOdds3 = goldenMushroomCapsuleSpaceOdds34
    goldenMushroomSpaceOdds4 = goldenMushroomCapsuleSpaceOdds34
    goldenMushroomShopOdds123 = goldenMushroomCapsuleShopOdds12
    goldenMushroomShopOdds4 = goldenMushroomCapsuleShopOdds34

    slowMushroomPrice1 = slowMushroomCapsulePrice1
    slowMushroomPrice2 = slowMushroomCapsulePrice2
    slowMushroomPrice34 = slowMushroomCapsulePrice34
    slowMushroomSpaceOdds1 = slowMushroomCapsuleSpaceOdds1
    slowMushroomSpaceOdds2 = slowMushroomCapsuleSpaceOdds2
    slowMushroomSpaceOdds3 = slowMushroomCapsuleSpaceOdds34
    slowMushroomSpaceOdds4 = slowMushroomCapsuleSpaceOdds34
    slowMushroomShopOdds123 = slowMushroomCapsuleShopOdds12
    slowMushroomShopOdds4 = slowMushroomCapsuleShopOdds34

    metalMushroomPrice1 = metalMushroomCapsulePrice1
    metalMushroomPrice2 = metalMushroomCapsulePrice2
    metalMushroomPrice34 = metalMushroomCapsulePrice34
    metalMushroomSpaceOdds1 = metalMushroomCapsuleSpaceOdds1
    metalMushroomSpaceOdds2 = metalMushroomCapsuleSpaceOdds2
    metalMushroomSpaceOdds3 = metalMushroomCapsuleSpaceOdds34
    metalMushroomSpaceOdds4 = metalMushroomCapsuleSpaceOdds34
    metalMushroomShopOdds123 = metalMushroomCapsuleShopOdds12
    metalMushroomShopOdds4 = metalMushroomCapsuleShopOdds34

    bulletBillPrice1 = cannonCapsulePrice1
    bulletBillPrice2 = cannonCapsulePrice2
    bulletBillPrice34 = cannonCapsulePrice34
    bulletBillSpaceOdds1 = cannonCapsuleSpaceOdds1
    bulletBillSpaceOdds2 = cannonCapsuleSpaceOdds2
    bulletBillSpaceOdds3 = cannonCapsuleSpaceOdds34
    bulletBillSpaceOdds4 = cannonCapsuleSpaceOdds34
    bulletBillShopOdds123 = cannonCapsuleShopOdds12
    bulletBillShopOdds4 = cannonCapsuleShopOdds34

    flutterPrice1 = flutterCapsulePrice1
    flutterPrice2 = flutterCapsulePrice2
    flutterPrice34 = flutterCapsulePrice34
    flutterSpaceOdds1 = flutterCapsuleSpaceOdds1
    flutterSpaceOdds2 = flutterCapsuleSpaceOdds2
    flutterSpaceOdds3 = flutterCapsuleSpaceOdds34
    flutterSpaceOdds4 = flutterCapsuleSpaceOdds34
    flutterShopOdds123 = flutterCapsuleShopOdds12
    flutterShopOdds4 = flutterCapsuleShopOdds34

    cursedMushroomPrice1 = cursedMushroomPrice1
    cursedMushroomPrice2 = cursedMushroomPrice2
    cursedMushroomPrice34 = cursedMushroomPrice34
    cursedMushroomSpaceOdds1 = cursedMushroomSpaceOdds1
    cursedMushroomSpaceOdds2 = cursedMushroomSpaceOdds2
    cursedMushroomSpaceOdds3 = cursedMushroomSpaceOdds34
    cursedMushroomSpaceOdds4 = cursedMushroomSpaceOdds34
    cursedMushroomShopOdds123 = cursedMushroomShopOdds12
    cursedMushroomShopOdds4 = cursedMushroomShopOdds34

    spinyPrice1 = spinyCapsulePrice1
    spinyPrice2 = spinyCapsulePrice2
    spinyPrice34 = spinyCapsulePrice34
    spinySpaceOdds1 = spinyCapsuleSpaceOdds1
    spinySpaceOdds2 = spinyCapsuleSpaceOdds2
    spinySpaceOdds3 = spinyCapsuleSpaceOdds34
    spinySpaceOdds4 = spinyCapsuleSpaceOdds34
    spinyShopOdds123 = spinyCapsuleShopOdds12
    spinyShopOdds4 = spinyCapsuleShopOdds34

    goombaCapsulePrice1 = goombaCapsulePrice1
    goombaCapsulePrice2 = goombaCapsulePrice2
    goombaCapsulePrice34 = goombaCapsulePrice34
    goombaCapsuleSpaceOdds1 = goombaCapsuleSpaceOdds1
    goombaCapsuleSpaceOdds2 = goombaCapsuleSpaceOdds2
    goombaCapsuleSpaceOdds3 = goombaCapsuleSpaceOdds34
    goombaCapsuleSpaceOdds4 = goombaCapsuleSpaceOdds34
    goombaCapsuleShopOdds123 = goombaCapsuleShopOdds12
    goombaCapsuleShopOdds4 = goombaCapsuleShopOdds34

    plantPrice1 = piranhaPlantCapsulePrice1
    plantPrice2 = piranhaPlantCapsulePrice2
    plantPrice34 = piranhaPlantCapsulePrice34
    plantSpaceOdds1 = piranhaPlantCapsuleSpaceOdds1
    plantSpaceOdds2 = piranhaPlantCapsuleSpaceOdds2
    plantSpaceOdds3 = piranhaPlantCapsuleSpaceOdds34
    plantSpaceOdds4 = piranhaPlantCapsuleSpaceOdds34
    plantShopOdds123 = piranhaPlantCapsuleShopOdds12
    plantShopOdds4 = piranhaPlantCapsuleShopOdds34

    kleptoCapsulePrice1 = kleptoCapsulePrice1
    kleptoCapsulePrice2 = kleptoCapsulePrice2
    kleptoCapsulePrice34 = kleptoCapsulePrice34
    kleptoCapsuleSpaceOdds1 = kleptoCapsuleSpaceOdds1
    kleptoCapsuleSpaceOdds2 = kleptoCapsuleSpaceOdds2
    kleptoCapsuleSpaceOdds3 = kleptoCapsuleSpaceOdds34
    kleptoCapsuleSpaceOdds4 = kleptoCapsuleSpaceOdds34
    kleptoCapsuleShopOdds123 = kleptoCapsuleShopOdds12
    kleptoCapsuleShopOdds4 = kleptoCapsuleShopOdds34

    toadyPrice1 = toadyCapsulePrice1
    toadyPrice2 = toadyCapsulePrice2
    toadyPrice34 = toadyCapsulePrice34
    toadySpaceOdds1 = toadyCapsuleSpaceOdds1
    toadySpaceOdds2 = toadyCapsuleSpaceOdds2
    toadySpaceOdds3 = toadyCapsuleSpaceOdds34
    toadySpaceOdds4 = toadyCapsuleSpaceOdds34
    toadyShopOdds123 = toadyCapsuleShopOdds12
    toadyShopOdds4 = toadyCapsuleShopOdds34

    kamekPrice1 = kamekCapsulePrice1
    kamekPrice2 = kamekCapsulePrice2
    kamekPrice34 = kamekCapsulePrice34
    kamekSpaceOdds1 = kamekCapsuleSpaceOdds1
    kamekSpaceOdds2 = kamekCapsuleSpaceOdds2
    kamekSpaceOdds3 = kamekCapsuleSpaceOdds34
    kamekSpaceOdds4 = kamekCapsuleSpaceOdds34
    kamekShopOdds123 = kamekCapsuleShopOdds12
    kamekShopOdds4 = kamekCapsuleShopOdds34

    blizzardPrice1 = mrBlizzardCapsulePrice1
    blizzardPrice2 = mrBlizzardCapsulePrice2
    blizzardPrice34 = mrBlizzardCapsulePrice34
    blizzardSpaceOdds1 = mrBlizzardCapsuleSpaceOdds1
    blizzardSpaceOdds2 = mrBlizzardCapsuleSpaceOdds2
    blizzardSpaceOdds3 = mrBlizzardCapsuleSpaceOdds34
    blizzardSpaceOdds4 = mrBlizzardCapsuleSpaceOdds34
    blizzardShopOdds123 = mrBlizzardCapsuleShopOdds12
    blizzardShopOdds4 = mrBlizzardCapsuleShopOdds34

    podobooCapsulePrice1 = podobooCapsulePrice1
    podobooCapsulePrice2 = podobooCapsulePrice2
    podobooCapsulePrice34 = podobooCapsulePrice34
    podobooCapsuleSpaceOdds1 = podobooCapsuleSpaceOdds1
    podobooCapsuleSpaceOdds2 = podobooCapsuleSpaceOdds2
    podobooCapsuleSpaceOdds3 = podobooCapsuleSpaceOdds34
    podobooCapsuleSpaceOdds4 = podobooCapsuleSpaceOdds34
    podobooCapsuleShopOdds123 = podobooCapsuleShopOdds12
    podobooCapsuleShopOdds4 = podobooCapsuleShopOdds34

    zapPrice1 = banditCapsulePrice1
    zapPrice2 = banditCapsulePrice2
    zapPrice34 = banditCapsulePrice34
    zapSpaceOdds1 = banditCapsuleSpaceOdds1
    zapSpaceOdds2 = banditCapsuleSpaceOdds2
    zapSpaceOdds3 = banditCapsuleSpaceOdds34
    zapSpaceOdds4 = banditCapsuleSpaceOdds34
    zapShopOdds123 = banditCapsuleShopOdds12
    zapShopOdds4 = banditCapsuleShopOdds34

    tweesterPrice1 = thwompCapsulePrice1
    tweesterPrice2 = thwompCapsulePrice2
    tweesterPrice34 = thwompCapsulePrice34
    tweesterSpaceOdds1 = thwompCapsuleSpaceOdds1
    tweesterSpaceOdds2 = thwompCapsuleSpaceOdds2
    tweesterSpaceOdds3 = thwompCapsuleSpaceOdds34
    tweesterSpaceOdds4 = thwompCapsuleSpaceOdds34
    tweesterShopOdds123 = thwompCapsuleShopOdds12
    tweesterShopOdds4 = thwompCapsuleShopOdds34

    thwompPrice1 = warpCapsulePrice1
    thwompPrice2 = warpCapsulePrice2
    thwompPrice34 = warpCapsulePrice34
    thwompSpaceOdds1 = warpCapsuleSpaceOdds1
    thwompSpaceOdds2 = warpCapsuleSpaceOdds2
    thwompSpaceOdds3 = warpCapsuleSpaceOdds34
    thwompSpaceOdds4 = warpCapsuleSpaceOdds34
    thwompShopOdds123 = warpCapsuleShopOdds12
    thwompShopOdds4 = warpCapsuleShopOdds34

    warpPipePrice1 = bombCapsulePrice1
    warpPipePrice2 = bombCapsulePrice2
    warpPipePrice34 = bombCapsulePrice34
    warpPipeSpaceOdds1 = bombCapsuleSpaceOdds1
    warpPipeSpaceOdds2 = bombCapsuleSpaceOdds2
    warpPipeSpaceOdds3 = bombCapsuleSpaceOdds34
    warpPipeSpaceOdds4 = bombCapsuleSpaceOdds34
    warpPipeShopOdds123 = bombCapsuleShopOdds12
    warpPipeShopOdds4 = bombCapsuleShopOdds34

    bombPrice1 = fireballCapsulePrice1
    bombPrice2 = fireballCapsulePrice2
    bombPrice34 = fireballCapsulePrice34
    bombSpaceOdds1 = fireballCapsuleSpaceOdds1
    bombSpaceOdds2 = fireballCapsuleSpaceOdds2
    bombSpaceOdds3 = fireballCapsuleSpaceOdds34
    bombSpaceOdds4 = fireballCapsuleSpaceOdds34
    bombShopOdds123 = fireballCapsuleShopOdds12
    bombShopOdds4 = fireballCapsuleShopOdds34

    paraTroopaCapsulePrice1 = paraTroopaCapsulePrice1
    paraTroopaCapsulePrice2 = paraTroopaCapsulePrice2
    paraTroopaCapsulePrice34 = paraTroopaCapsulePrice34
    paraTroopaCapsuleSpaceOdds1 = paraTroopaCapsuleSpaceOdds1
    paraTroopaCapsuleSpaceOdds2 = paraTroopaCapsuleSpaceOdds2
    paraTroopaCapsuleSpaceOdds3 = paraTroopaCapsuleSpaceOdds34
    paraTroopaCapsuleSpaceOdds4 = paraTroopaCapsuleSpaceOdds34
    paraTroopaCapsuleShopOdds123 = paraTroopaCapsuleShopOdds12
    paraTroopaCapsuleShopOdds4 = paraTroopaCapsuleShopOdds34

    snackPrice1 = eggCapsulePrice1
    snackPrice2 = eggCapsulePrice2
    snackPrice34 = eggCapsulePrice34
    snackSpaceOdds1 = eggCapsuleSpaceOdds1
    snackSpaceOdds2 = eggCapsuleSpaceOdds2
    snackSpaceOdds3 = eggCapsuleSpaceOdds34
    snackSpaceOdds4 = eggCapsuleSpaceOdds34
    snackShopOdds123 = eggCapsuleShopOdds12
    snackShopOdds4 = eggCapsuleShopOdds34

    gaddLightPrice1 = vacuumCapsulePrice1
    gaddLightPrice2 = vacuumCapsulePrice2
    gaddLightPrice34 = vacuumCapsulePrice34
    gaddLightSpaceOdds1 = vacuumCapsuleSpaceOdds1
    gaddLightSpaceOdds2 = vacuumCapsuleSpaceOdds2
    gaddLightSpaceOdds3 = vacuumCapsuleSpaceOdds34
    gaddLightSpaceOdds4 = vacuumCapsuleSpaceOdds34
    gaddLightShopOdds123 = vacuumCapsuleShopOdds12
    gaddLightShopOdds4 = vacuumCapsuleShopOdds34

    # Map DX-only capsule variable names to formatter argument names
    duelPrice1 = DxCapsuleDuelPrice1
    duelPrice2 = DxCapsuleDuelPrice2
    duelPrice34 = DxCapsuleDuelPrice34
    duelSpaceOdds1 = DxCapsuleDuelSpaceOdds1
    duelSpaceOdds2 = DxCapsuleDuelSpaceOdds2
    duelSpaceOdds3 = DxCapsuleDuelSpaceOdds34
    duelSpaceOdds4 = DxCapsuleDuelSpaceOdds34
    duelShopOdds123 = DxCapsuleDuelShopOdds12
    duelShopOdds124 = DxCapsuleDuelShopOdds12
    duelShopOdds4 = DxCapsuleDuelShopOdds34

    chanceTimePrice1 = DxCapsuleChancePrice1
    chanceTimePrice2 = DxCapsuleChancePrice2
    chanceTimePrice34 = DxCapsuleChancePrice34
    chanceTimeSpaceOdds1 = DxCapsuleChanceSpaceOdds1
    chanceTimeSpaceOdds2 = DxCapsuleChanceSpaceOdds2
    chanceTimeSpaceOdds3 = DxCapsuleChanceSpaceOdds34
    chanceTimeSpaceOdds4 = DxCapsuleChanceSpaceOdds34
    chanceTimeShopOdds123 = DxCapsuleChanceShopOdds12
    chanceTimeShopOdds124 = DxCapsuleChanceShopOdds12
    chanceTimeShopOdds4 = DxCapsuleChanceShopOdds34

    bowserPrice1 = DxCapsuleBowserPrice1
    bowserPrice2 = DxCapsuleBowserPrice2
    bowserPrice34 = DxCapsuleBowserPrice34
    bowserSpaceOdds1 = DxCapsuleBowserSpaceOdds1
    bowserSpaceOdds2 = DxCapsuleBowserSpaceOdds2
    bowserSpaceOdds3 = DxCapsuleBowserSpaceOdds34
    bowserSpaceOdds4 = DxCapsuleBowserSpaceOdds34
    bowserShopOdds123 = DxCapsuleBowserShopOdds12
    bowserShopOdds124 = DxCapsuleBowserShopOdds12
    bowserShopOdds4 = DxCapsuleBowserShopOdds34

    donkeyKongPrice1 = DxCapsuleDonkeyKongPrice1
    donkeyKongPrice2 = DxCapsuleDonkeyKongPrice2
    donkeyKongPrice34 = DxCapsuleDonkeyKongPrice34
    donkeyKongSpaceOdds1 = DxCapsuleDonkeyKongSpaceOdds1
    donkeyKongSpaceOdds2 = DxCapsuleDonkeyKongSpaceOdds2
    donkeyKongSpaceOdds3 = DxCapsuleDonkeyKongSpaceOdds34
    donkeyKongSpaceOdds4 = DxCapsuleDonkeyKongSpaceOdds34
    donkeyKongShopOdds123 = DxCapsuleDonkeyKongShopOdds12
    donkeyKongShopOdds124 = DxCapsuleDonkeyKongShopOdds12
    donkeyKongShopOdds4 = DxCapsuleDonkeyKongShopOdds34

    pinkBooPrice1 = DxCapsulePinkBooPrice1
    pinkBooPrice2 = DxCapsulePinkBooPrice2
    pinkBooPrice34 = DxCapsulePinkBooPrice34
    pinkBooSpaceOdds1 = DxCapsulePinkBooSpaceOdds1
    pinkBooSpaceOdds2 = DxCapsulePinkBooSpaceOdds2
    pinkBooSpaceOdds3 = DxCapsulePinkBooSpaceOdds34
    pinkBooSpaceOdds4 = DxCapsulePinkBooSpaceOdds34
    pinkBooShopOdds123 = DxCapsulePinkBooShopOdds12
    pinkBooShopOdds124 = DxCapsulePinkBooShopOdds12
    pinkBooShopOdds4 = DxCapsulePinkBooShopOdds34

    solunaPrice1 = DxCapsuleSolunaPrice1
    solunaPrice2 = DxCapsuleSolunaPrice2
    solunaPrice34 = DxCapsuleSolunaPrice34
    solunaSpaceOdds1 = DxCapsuleSolunaSpaceOdds1
    solunaSpaceOdds2 = DxCapsuleSolunaSpaceOdds2
    solunaSpaceOdds3 = DxCapsuleSolunaSpaceOdds34
    solunaSpaceOdds4 = DxCapsuleSolunaSpaceOdds34
    solunaShopOdds123 = DxCapsuleSolunaShopOdds12
    solunaShopOdds124 = DxCapsuleSolunaShopOdds12
    solunaShopOdds4 = DxCapsuleSolunaShopOdds34

    chainChompPrice1 = DxCapsuleChainChompPrice1
    chainChompPrice2 = DxCapsuleChainChompPrice2
    chainChompPrice34 = DxCapsuleChainChompPrice34
    chainChompSpaceOdds1 = DxCapsuleChainChompSpaceOdds1
    chainChompSpaceOdds2 = DxCapsuleChainChompSpaceOdds2
    chainChompSpaceOdds3 = DxCapsuleChainChompSpaceOdds34
    chainChompSpaceOdds4 = DxCapsuleChainChompSpaceOdds34
    chainChompShopOdds123 = DxCapsuleChainChompShopOdds12
    chainChompShopOdds124 = DxCapsuleChainChompShopOdds12
    chainChompShopOdds4 = DxCapsuleChainChompShopOdds34

    wackyWatchPrice1 = DxCapsuleWackyWatchPrice1
    wackyWatchPrice2 = DxCapsuleWackyWatchPrice2
    wackyWatchPrice34 = DxCapsuleWackyWatchPrice34
    wackyWatchSpaceOdds1 = DxCapsuleWackyWatchSpaceOdds1
    wackyWatchSpaceOdds2 = DxCapsuleWackyWatchSpaceOdds2
    wackyWatchSpaceOdds3 = DxCapsuleWackyWatchSpaceOdds34
    wackyWatchSpaceOdds4 = DxCapsuleWackyWatchSpaceOdds34
    wackyWatchShopOdds123 = DxCapsuleWackyWatchShopOdds12
    wackyWatchShopOdds124 = DxCapsuleWackyWatchShopOdds12
    wackyWatchShopOdds4 = DxCapsuleWackyWatchShopOdds34

    import inspect
    current_values = locals().copy()
    dx_kwargs = {
        name: current_values.get(name, "00")
        for name in inspect.signature(getOrbModsSixDX).parameters
    }
    generatedCode = getOrbModsSixDX(**dx_kwargs)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def itemsEvent_mp6(mushroomCapsuleShopOdds12 = "0", mushroomCapsuleShopOdds34 = "0", mushroomCapsuleSpaceOdds1 = "0", mushroomCapsuleSpaceOdds2 = "0", mushroomCapsuleSpaceOdds34 = "0", goldenMushroomCapsulePrice1 = "0", goldenMushroomCapsulePrice2 = "0", goldenMushroomCapsulePrice34 = "0", goldenMushroomCapsuleShopOdds12 = "0", goldenMushroomCapsuleShopOdds34 = "0", goldenMushroomCapsuleSpaceOdds1 = "0", goldenMushroomCapsuleSpaceOdds2 = "0", goldenMushroomCapsuleSpaceOdds34 = "0", slowMushroomCapsulePrice1 = "0", slowMushroomCapsulePrice2 = "0", slowMushroomCapsulePrice34 = "0", slowMushroomCapsuleShopOdds12 = "0", slowMushroomCapsuleShopOdds34 = "0", slowMushroomCapsuleSpaceOdds1 = "0", slowMushroomCapsuleSpaceOdds2 = "0", slowMushroomCapsuleSpaceOdds34 = "0", metalMushroomCapsulePrice1 = "0", metalMushroomCapsulePrice2 = "0", metalMushroomCapsulePrice34 = "0", metalMushroomCapsuleShopOdds12 = "0", metalMushroomCapsuleShopOdds34 = "0", metalMushroomCapsuleSpaceOdds1 = "0", metalMushroomCapsuleSpaceOdds2 = "0", metalMushroomCapsuleSpaceOdds34 = "0", flutterCapsulePrice1 = "0", flutterCapsulePrice2 = "0", flutterCapsulePrice34 = "0", flutterCapsuleShopOdds12 = "0", flutterCapsuleShopOdds34 = "0", flutterCapsuleSpaceOdds1 = "0", flutterCapsuleSpaceOdds2 = "0", flutterCapsuleSpaceOdds34 = "0", cannonCapsulePrice1 = "0", cannonCapsulePrice2 = "0", cannonCapsulePrice34 = "0", cannonCapsuleShopOdds12 = "0", cannonCapsuleShopOdds34 = "0", cannonCapsuleSpaceOdds1 = "0", cannonCapsuleSpaceOdds2 = "0", cannonCapsuleSpaceOdds34 = "0", snackCapsulePrice1 = "0", snackCapsulePrice2 = "0", snackCapsulePrice34 = "0", snackCapsuleShopOdds12 = "0", snackCapsuleShopOdds34 = "0", snackCapsuleSpaceOdds1 = "0", snackCapsuleSpaceOdds2 = "0", snackCapsuleSpaceOdds34 = "0", goombaCapsulePrice1 = "0", goombaCapsulePrice2 = "0", goombaCapsulePrice34 = "0", goombaCapsuleShopOdds12 = "0", goombaCapsuleShopOdds34 = "0", goombaCapsuleSpaceOdds1 = "0", goombaCapsuleSpaceOdds2 = "0", goombaCapsuleSpaceOdds34 = "0", hammerBroCapsulePrice1 = "0", hammerBroCapsulePrice2 = "0", hammerBroCapsulePrice34 = "0", hammerBroCapsuleShopOdds12 = "0", hammerBroCapsuleShopOdds34 = "0", hammerBroCapsuleSpaceOdds1 = "0", hammerBroCapsuleSpaceOdds2 = "0", hammerBroCapsuleSpaceOdds34 = "0", piranhaPlantCapsulePrice1 = "0", piranhaPlantCapsulePrice2 = "0", piranhaPlantCapsulePrice34 = "0", piranhaPlantCapsuleShopOdds12 = "0", piranhaPlantCapsuleShopOdds34 = "0", piranhaPlantCapsuleSpaceOdds1 = "0", piranhaPlantCapsuleSpaceOdds2 = "0", piranhaPlantCapsuleSpaceOdds34 = "0", kleptoCapsulePrice1 = "0", kleptoCapsulePrice2 = "0", kleptoCapsulePrice34 = "0", kleptoCapsuleShopOdds12 = "0", kleptoCapsuleShopOdds34 = "0", kleptoCapsuleSpaceOdds1 = "0", kleptoCapsuleSpaceOdds2 = "0", kleptoCapsuleSpaceOdds34 = "0", kamekCapsulePrice1 = "0", kamekCapsulePrice2 = "0", kamekCapsulePrice34 = "0", kamekCapsuleShopOdds12 = "0", kamekCapsuleShopOdds34 = "0", kamekCapsuleSpaceOdds1 = "0", kamekCapsuleSpaceOdds2 = "0", kamekCapsuleSpaceOdds34 = "0", toadyCapsulePrice1 = "0", toadyCapsulePrice2 = "0", toadyCapsulePrice34 = "0", toadyCapsuleShopOdds12 = "0", toadyCapsuleShopOdds34 = "0", toadyCapsuleSpaceOdds1 = "0", toadyCapsuleSpaceOdds2 = "0", toadyCapsuleSpaceOdds34 = "0", mrBlizzardCapsulePrice1 = "0", mrBlizzardCapsulePrice2 = "0", mrBlizzardCapsulePrice34 = "0", mrBlizzardCapsuleShopOdds12 = "0", mrBlizzardCapsuleShopOdds34 = "0", mrBlizzardCapsuleSpaceOdds1 = "0", mrBlizzardCapsuleSpaceOdds2 = "0", mrBlizzardCapsuleSpaceOdds34 = "0", banditCapsulePrice1 = "0", banditCapsulePrice2 = "0", banditCapsulePrice34 = "0", banditCapsuleShopOdds12 = "0", banditCapsuleShopOdds34 = "0", banditCapsuleSpaceOdds1 = "0", banditCapsuleSpaceOdds2 = "0", banditCapsuleSpaceOdds34 = "0", pinkBooCapsulePrice1 = "0", pinkBooCapsulePrice2 = "0", pinkBooCapsulePrice34 = "0", pinkBooCapsuleShopOdds12 = "0", pinkBooCapsuleShopOdds34 = "0", pinkBooCapsuleSpaceOdds1 = "0", pinkBooCapsuleSpaceOdds2 = "0", pinkBooCapsuleSpaceOdds34 = "0", spinyCapsulePrice1 = "0", spinyCapsulePrice2 = "0", spinyCapsulePrice34 = "0", spinyCapsuleShopOdds12 = "0", spinyCapsuleShopOdds34 = "0", spinyCapsuleSpaceOdds1 = "0", spinyCapsuleSpaceOdds2 = "0", spinyCapsuleSpaceOdds34 = "0", podobooCapsulePrice1 = "0", podobooCapsulePrice2 = "0", podobooCapsulePrice34 = "0", podobooCapsuleShopOdds12 = "0", podobooCapsuleShopOdds34 = "0", podobooCapsuleSpaceOdds1 = "0", podobooCapsuleSpaceOdds2 = "0", podobooCapsuleSpaceOdds34 = "0", tweesterCapsulePrice1 = "0", tweesterCapsulePrice2 = "0", tweesterCapsulePrice34 = "0", tweesterCapsuleShopOdds12 = "0", tweesterCapsuleShopOdds34 = "0", tweesterCapsuleSpaceOdds1 = "0", tweesterCapsuleSpaceOdds2 = "0", tweesterCapsuleSpaceOdds34 = "0", thwompCapsulePrice1 = "0", thwompCapsulePrice2 = "0", thwompCapsulePrice34 = "0", thwompCapsuleShopOdds12 = "0", thwompCapsuleShopOdds34 = "0", thwompCapsuleSpaceOdds1 = "0", thwompCapsuleSpaceOdds2 = "0", thwompCapsuleSpaceOdds34 = "0", warpCapsulePrice1 = "0", warpCapsulePrice2 = "0", warpCapsulePrice34 = "0", warpCapsuleShopOdds12 = "0", warpCapsuleShopOdds34 = "0", warpCapsuleSpaceOdds1 = "0", warpCapsuleSpaceOdds2 = "0", warpCapsuleSpaceOdds34 = "0", bombCapsulePrice1 = "0", bombCapsulePrice2 = "0", bombCapsulePrice34 = "0", bombCapsuleShopOdds12 = "0", bombCapsuleShopOdds34 = "0", bombCapsuleSpaceOdds1 = "0", bombCapsuleSpaceOdds2 = "0", bombCapsuleSpaceOdds34 = "0", fireballCapsulePrice1 = "0", fireballCapsulePrice2 = "0", fireballCapsulePrice34 = "0", fireballCapsuleShopOdds12 = "0", fireballCapsuleShopOdds34 = "0", fireballCapsuleSpaceOdds1 = "0", fireballCapsuleSpaceOdds2 = "0", fireballCapsuleSpaceOdds34 = "0", paraTroopaCapsulePrice1 = "0", paraTroopaCapsulePrice2 = "0", paraTroopaCapsulePrice34 = "0", paraTroopaCapsuleShopOdds12 = "0", paraTroopaCapsuleShopOdds34 = "0", paraTroopaCapsuleSpaceOdds1 = "0", paraTroopaCapsuleSpaceOdds2 = "0", paraTroopaCapsuleSpaceOdds34 = "0", eggCapsulePrice1 = "0", eggCapsulePrice2 = "0", eggCapsulePrice34 = "0", eggCapsuleShopOdds12 = "0", eggCapsuleShopOdds34 = "0", eggCapsuleSpaceOdds1 = "0", eggCapsuleSpaceOdds2 = "0", eggCapsuleSpaceOdds34 = "0", vacuumCapsulePrice1 = "0", vacuumCapsulePrice2 = "0", vacuumCapsulePrice34 = "0", vacuumCapsuleShopOdds12 = "0", vacuumCapsuleShopOdds34 = "0", vacuumCapsuleSpaceOdds1 = "0", vacuumCapsuleSpaceOdds2 = "0", vacuumCapsuleSpaceOdds34 = "0", magicCapsulePrice1 = "0", magicCapsulePrice2 = "0", magicCapsulePrice34 = "0", magicCapsuleShopOdds12 = "0", magicCapsuleShopOdds34 = "0", magicCapsuleSpaceOdds1 = "0", magicCapsuleSpaceOdds2 = "0", magicCapsuleSpaceOdds34 = "0", tripleCapsulePrice1 = "0", tripleCapsulePrice2 = "0", tripleCapsulePrice34 = "0", tripleCapsuleShopOdds12 = "0", tripleCapsuleShopOdds34 = "0", tripleCapsuleSpaceOdds1 = "0", tripleCapsuleSpaceOdds2 = "0", tripleCapsuleSpaceOdds34 = "0", koopaCapsulePrice1 = "0", koopaCapsulePrice2 = "0", koopaCapsulePrice34 = "0", koopaCapsuleShopOdds12 = "0", koopaCapsuleShopOdds34 = "0", koopaCapsuleSpaceOdds1 = "0", koopaCapsuleSpaceOdds2 = "0", koopaCapsuleSpaceOdds34 = "0", cursedMushroomPrice1 = "0", cursedMushroomPrice2 = "0", cursedMushroomPrice34 = "0", cursedMushroomShopOdds12 = "0", cursedMushroomShopOdds34 = "0", cursedMushroomSpaceOdds1 = "0", cursedMushroomSpaceOdds2 = "0", cursedMushroomSpaceOdds34 = "0", orbBagCapsulePrice1 = "0", orbBagCapsulePrice2 = "0", orbBagCapsulePrice34 = "0", orbBagCapsuleShopOdds12 = "0", orbBagCapsuleShopOdds34 = "0", orbBagCapsuleSpaceOdds1 = "0", orbBagCapsuleSpaceOdds2 = "0", orbBagCapsuleSpaceOdds34 = "0", mysteryCapsulePrice1 = "0", mysteryCapsulePrice2 = "0", mysteryCapsulePrice34 = "0", mysteryCapsuleShopOdds12 = "0", mysteryCapsuleShopOdds34 = "0", mysteryCapsuleSpaceOdds1 = "0", mysteryCapsuleSpaceOdds2 = "0", mysteryCapsuleSpaceOdds34 = "0", dkCapsulePrice1 = "0", dkCapsulePrice2 = "0", dkCapsulePrice34 = "0", dkCapsuleShopOdds12 = "0", dkCapsuleShopOdds34 = "0", dkCapsuleSpaceOdds1 = "0", dkCapsuleSpaceOdds2 = "0", dkCapsuleSpaceOdds34 = "0", duelCapsulePrice1 = "0", duelCapsulePrice2 = "0", duelCapsulePrice34 = "0", duelCapsuleShopOdds12 = "0", duelCapsuleShopOdds34 = "0", duelCapsuleSpaceOdds1 = "0", duelCapsuleSpaceOdds2 = "0", duelCapsuleSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            # Handle string values from UI
            if isinstance(capsule, str):
                return int(capsule) if capsule else 0
            # Handle Tkinter widget values
            return capsule.get()
        except:
            return 0

    mushroomCapsuleShopOdds12 = get_capsule_value(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = get_capsule_value(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = get_capsule_value(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = get_capsule_value(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = get_capsule_value(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsulePrice1 = get_capsule_value(goldenMushroomCapsulePrice1)
    goldenMushroomCapsulePrice2 = get_capsule_value(goldenMushroomCapsulePrice2)
    goldenMushroomCapsulePrice34 = get_capsule_value(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = get_capsule_value(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = get_capsule_value(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = get_capsule_value(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = get_capsule_value(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = get_capsule_value(goldenMushroomCapsuleSpaceOdds34)


    slowMushroomCapsulePrice1 = get_capsule_value(slowMushroomCapsulePrice1)
    slowMushroomCapsulePrice2 = get_capsule_value(slowMushroomCapsulePrice2)
    slowMushroomCapsulePrice34 = get_capsule_value(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = get_capsule_value(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = get_capsule_value(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = get_capsule_value(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = get_capsule_value(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = get_capsule_value(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsulePrice1 = get_capsule_value(metalMushroomCapsulePrice1)
    metalMushroomCapsulePrice2 = get_capsule_value(metalMushroomCapsulePrice2)
    metalMushroomCapsulePrice34 = get_capsule_value(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = get_capsule_value(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = get_capsule_value(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = get_capsule_value(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = get_capsule_value(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = get_capsule_value(metalMushroomCapsuleSpaceOdds34)

    flutterCapsulePrice1 = get_capsule_value(flutterCapsulePrice1)
    flutterCapsulePrice2 = get_capsule_value(flutterCapsulePrice2)
    flutterCapsulePrice34 = get_capsule_value(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = get_capsule_value(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = get_capsule_value(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = get_capsule_value(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = get_capsule_value(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = get_capsule_value(flutterCapsuleSpaceOdds34)

    cannonCapsulePrice1 = get_capsule_value(cannonCapsulePrice1)
    cannonCapsulePrice2 = get_capsule_value(cannonCapsulePrice2)
    cannonCapsulePrice34 = get_capsule_value(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = get_capsule_value(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = get_capsule_value(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = get_capsule_value(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = get_capsule_value(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = get_capsule_value(cannonCapsuleSpaceOdds34)

    snackCapsulePrice1 = get_capsule_value(snackCapsulePrice1)
    snackCapsulePrice2 = get_capsule_value(snackCapsulePrice2)
    snackCapsulePrice34 = get_capsule_value(snackCapsulePrice34)
    snackCapsuleShopOdds12 = get_capsule_value(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = get_capsule_value(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = get_capsule_value(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = get_capsule_value(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = get_capsule_value(snackCapsuleSpaceOdds34)

    goombaCapsulePrice1 = get_capsule_value(goombaCapsulePrice1)
    goombaCapsulePrice2 = get_capsule_value(goombaCapsulePrice2)
    goombaCapsulePrice34 = get_capsule_value(goombaCapsulePrice34)
    goombaCapsuleShopOdds12 = get_capsule_value(goombaCapsuleShopOdds12)
    goombaCapsuleShopOdds34 = get_capsule_value(goombaCapsuleShopOdds34)
    goombaCapsuleSpaceOdds1 = get_capsule_value(goombaCapsuleSpaceOdds1)
    goombaCapsuleSpaceOdds2 = get_capsule_value(goombaCapsuleSpaceOdds2)
    goombaCapsuleSpaceOdds34 = get_capsule_value(goombaCapsuleSpaceOdds34)

    hammerBroCapsulePrice1 = get_capsule_value(hammerBroCapsulePrice1)
    hammerBroCapsulePrice2 = get_capsule_value(hammerBroCapsulePrice2)
    hammerBroCapsulePrice34 = get_capsule_value(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = get_capsule_value(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = get_capsule_value(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = get_capsule_value(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = get_capsule_value(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = get_capsule_value(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsulePrice1 = get_capsule_value(piranhaPlantCapsulePrice1)
    piranhaPlantCapsulePrice2 = get_capsule_value(piranhaPlantCapsulePrice2)
    piranhaPlantCapsulePrice34 = get_capsule_value(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = get_capsule_value(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = get_capsule_value(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = get_capsule_value(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = get_capsule_value(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = get_capsule_value(piranhaPlantCapsuleSpaceOdds34)

    kleptoCapsulePrice1 = get_capsule_value(kleptoCapsulePrice1)
    kleptoCapsulePrice2 = get_capsule_value(kleptoCapsulePrice2)
    kleptoCapsulePrice34 = get_capsule_value(kleptoCapsulePrice34)
    kleptoCapsuleShopOdds12 = get_capsule_value(kleptoCapsuleShopOdds12)
    kleptoCapsuleShopOdds34 = get_capsule_value(kleptoCapsuleShopOdds34)
    kleptoCapsuleSpaceOdds1 = get_capsule_value(kleptoCapsuleSpaceOdds1)
    kleptoCapsuleSpaceOdds2 = get_capsule_value(kleptoCapsuleSpaceOdds2)
    kleptoCapsuleSpaceOdds34 = get_capsule_value(kleptoCapsuleSpaceOdds34)

    kamekCapsulePrice1 = get_capsule_value(kamekCapsulePrice1)
    kamekCapsulePrice2 = get_capsule_value(kamekCapsulePrice2)
    kamekCapsulePrice34 = get_capsule_value(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = get_capsule_value(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = get_capsule_value(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = get_capsule_value(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = get_capsule_value(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = get_capsule_value(kamekCapsuleSpaceOdds34)

    toadyCapsulePrice1 = get_capsule_value(toadyCapsulePrice1)
    toadyCapsulePrice2 = get_capsule_value(toadyCapsulePrice2)
    toadyCapsulePrice34 = get_capsule_value(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = get_capsule_value(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = get_capsule_value(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = get_capsule_value(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = get_capsule_value(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = get_capsule_value(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsulePrice1 = get_capsule_value(mrBlizzardCapsulePrice1)
    mrBlizzardCapsulePrice2 = get_capsule_value(mrBlizzardCapsulePrice2)
    mrBlizzardCapsulePrice34 = get_capsule_value(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = get_capsule_value(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = get_capsule_value(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = get_capsule_value(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = get_capsule_value(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = get_capsule_value(mrBlizzardCapsuleSpaceOdds34)

    banditCapsulePrice1 = get_capsule_value(banditCapsulePrice1)
    banditCapsulePrice2 = get_capsule_value(banditCapsulePrice2)
    banditCapsulePrice34 = get_capsule_value(banditCapsulePrice34)
    banditCapsuleShopOdds12 = get_capsule_value(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = get_capsule_value(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = get_capsule_value(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = get_capsule_value(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = get_capsule_value(banditCapsuleSpaceOdds34)

    pinkBooCapsulePrice1 = get_capsule_value(pinkBooCapsulePrice1)
    pinkBooCapsulePrice2 = get_capsule_value(pinkBooCapsulePrice2)
    pinkBooCapsulePrice34 = get_capsule_value(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = get_capsule_value(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = get_capsule_value(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = get_capsule_value(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = get_capsule_value(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = get_capsule_value(pinkBooCapsuleSpaceOdds34)

    spinyCapsulePrice1 = get_capsule_value(spinyCapsulePrice1)
    spinyCapsulePrice2 = get_capsule_value(spinyCapsulePrice2)
    spinyCapsulePrice34 = get_capsule_value(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = get_capsule_value(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = get_capsule_value(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = get_capsule_value(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = get_capsule_value(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = get_capsule_value(spinyCapsuleSpaceOdds34)

    podobooCapsulePrice1 = get_capsule_value(podobooCapsulePrice1)
    podobooCapsulePrice2 = get_capsule_value(podobooCapsulePrice2)
    podobooCapsulePrice34 = get_capsule_value(podobooCapsulePrice34)
    podobooCapsuleShopOdds12 = get_capsule_value(podobooCapsuleShopOdds12)
    podobooCapsuleShopOdds34 = get_capsule_value(podobooCapsuleShopOdds34)
    podobooCapsuleSpaceOdds1 = get_capsule_value(podobooCapsuleSpaceOdds1)
    podobooCapsuleSpaceOdds2 = get_capsule_value(podobooCapsuleSpaceOdds2)
    podobooCapsuleSpaceOdds34 = get_capsule_value(podobooCapsuleSpaceOdds34)

    tweesterCapsulePrice1 = get_capsule_value(tweesterCapsulePrice1)
    tweesterCapsulePrice2 = get_capsule_value(tweesterCapsulePrice2)
    tweesterCapsulePrice34 = get_capsule_value(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = get_capsule_value(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = get_capsule_value(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = get_capsule_value(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = get_capsule_value(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = get_capsule_value(tweesterCapsuleSpaceOdds34)

    thwompCapsulePrice1 = get_capsule_value(thwompCapsulePrice1)
    thwompCapsulePrice2 = get_capsule_value(thwompCapsulePrice2)
    thwompCapsulePrice34 = get_capsule_value(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = get_capsule_value(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = get_capsule_value(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = get_capsule_value(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = get_capsule_value(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = get_capsule_value(thwompCapsuleSpaceOdds34)

    warpCapsulePrice1 = get_capsule_value(warpCapsulePrice1)
    warpCapsulePrice2 = get_capsule_value(warpCapsulePrice2)
    warpCapsulePrice34 = get_capsule_value(warpCapsulePrice34)
    warpCapsuleShopOdds12 = get_capsule_value(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = get_capsule_value(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = get_capsule_value(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = get_capsule_value(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = get_capsule_value(warpCapsuleSpaceOdds34)

    bombCapsulePrice1 = get_capsule_value(bombCapsulePrice1)
    bombCapsulePrice2 = get_capsule_value(bombCapsulePrice2)
    bombCapsulePrice34 = get_capsule_value(bombCapsulePrice34)
    bombCapsuleShopOdds12 = get_capsule_value(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = get_capsule_value(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = get_capsule_value(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = get_capsule_value(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = get_capsule_value(bombCapsuleSpaceOdds34)

    fireballCapsulePrice1 = get_capsule_value(fireballCapsulePrice1)
    fireballCapsulePrice2 = get_capsule_value(fireballCapsulePrice2)
    fireballCapsulePrice34 = get_capsule_value(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = get_capsule_value(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = get_capsule_value(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = get_capsule_value(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = get_capsule_value(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = get_capsule_value(fireballCapsuleSpaceOdds34)

    paraTroopaCapsulePrice1 = get_capsule_value(paraTroopaCapsulePrice1)
    paraTroopaCapsulePrice2 = get_capsule_value(paraTroopaCapsulePrice2)
    paraTroopaCapsulePrice34 = get_capsule_value(paraTroopaCapsulePrice34)
    paraTroopaCapsuleShopOdds12 = get_capsule_value(paraTroopaCapsuleShopOdds12)
    paraTroopaCapsuleShopOdds34 = get_capsule_value(paraTroopaCapsuleShopOdds34)
    paraTroopaCapsuleSpaceOdds1 = get_capsule_value(paraTroopaCapsuleSpaceOdds1)
    paraTroopaCapsuleSpaceOdds2 = get_capsule_value(paraTroopaCapsuleSpaceOdds2)
    paraTroopaCapsuleSpaceOdds34 = get_capsule_value(paraTroopaCapsuleSpaceOdds34)

    eggCapsulePrice1 = get_capsule_value(eggCapsulePrice1)
    eggCapsulePrice2 = get_capsule_value(eggCapsulePrice2)
    eggCapsulePrice34 = get_capsule_value(eggCapsulePrice34)
    eggCapsuleShopOdds12 = get_capsule_value(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = get_capsule_value(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = get_capsule_value(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = get_capsule_value(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = get_capsule_value(eggCapsuleSpaceOdds34)

    vacuumCapsulePrice1 = get_capsule_value(vacuumCapsulePrice1)
    vacuumCapsulePrice2 = get_capsule_value(vacuumCapsulePrice2)
    vacuumCapsulePrice34 = get_capsule_value(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = get_capsule_value(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = get_capsule_value(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = get_capsule_value(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = get_capsule_value(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = get_capsule_value(vacuumCapsuleSpaceOdds34)

    magicCapsulePrice1 = get_capsule_value(magicCapsulePrice1)
    magicCapsulePrice2 = get_capsule_value(magicCapsulePrice2)
    magicCapsulePrice34 = get_capsule_value(magicCapsulePrice34)
    magicCapsuleShopOdds12 = get_capsule_value(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = get_capsule_value(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = get_capsule_value(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = get_capsule_value(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = get_capsule_value(magicCapsuleSpaceOdds34)

    tripleCapsulePrice1 = get_capsule_value(tripleCapsulePrice1)
    tripleCapsulePrice2 = get_capsule_value(tripleCapsulePrice2)
    tripleCapsulePrice34 = get_capsule_value(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = get_capsule_value(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = get_capsule_value(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = get_capsule_value(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = get_capsule_value(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = get_capsule_value(tripleCapsuleSpaceOdds34)

    koopaCapsulePrice1 = get_capsule_value(koopaCapsulePrice1)
    koopaCapsulePrice2 = get_capsule_value(koopaCapsulePrice2)
    koopaCapsulePrice34 = get_capsule_value(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = get_capsule_value(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = get_capsule_value(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = get_capsule_value(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = get_capsule_value(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = get_capsule_value(koopaCapsuleSpaceOdds34)

    cursedMushroomPrice1 = get_capsule_value(cursedMushroomPrice1)
    cursedMushroomPrice2 = get_capsule_value(cursedMushroomPrice2)
    cursedMushroomPrice34 = get_capsule_value(cursedMushroomPrice34)
    cursedMushroomShopOdds12 = get_capsule_value(cursedMushroomShopOdds12)
    cursedMushroomShopOdds34 = get_capsule_value(cursedMushroomShopOdds34)
    cursedMushroomSpaceOdds1 = get_capsule_value(cursedMushroomSpaceOdds1)
    cursedMushroomSpaceOdds2 = get_capsule_value(cursedMushroomSpaceOdds2)
    cursedMushroomSpaceOdds34 = get_capsule_value(cursedMushroomSpaceOdds34)

    orbBagCapsulePrice1 = get_capsule_value(orbBagCapsulePrice1)
    orbBagCapsulePrice2 = get_capsule_value(orbBagCapsulePrice2)
    orbBagCapsulePrice34 = get_capsule_value(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = get_capsule_value(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = get_capsule_value(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = get_capsule_value(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = get_capsule_value(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = get_capsule_value(orbBagCapsuleSpaceOdds34)

    mysteryCapsulePrice1 = get_capsule_value(mysteryCapsulePrice1)
    mysteryCapsulePrice2 = get_capsule_value(mysteryCapsulePrice2)
    mysteryCapsulePrice34 = get_capsule_value(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = get_capsule_value(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = get_capsule_value(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = get_capsule_value(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = get_capsule_value(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = get_capsule_value(mysteryCapsuleSpaceOdds34)

    dkCapsulePrice1 = get_capsule_value(dkCapsulePrice1)
    dkCapsulePrice2 = get_capsule_value(dkCapsulePrice2)
    dkCapsulePrice34 = get_capsule_value(dkCapsulePrice34)
    dkCapsuleShopOdds12 = get_capsule_value(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = get_capsule_value(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = get_capsule_value(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = get_capsule_value(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = get_capsule_value(dkCapsuleSpaceOdds34)

    duelCapsulePrice1 = get_capsule_value(duelCapsulePrice1)
    duelCapsulePrice2 = get_capsule_value(duelCapsulePrice2)
    duelCapsulePrice34 = get_capsule_value(duelCapsulePrice34)
    duelCapsuleShopOdds12 = get_capsule_value(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = get_capsule_value(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = get_capsule_value(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = get_capsule_value(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = get_capsule_value(duelCapsuleSpaceOdds34)

    # Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, goombaCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, kleptoCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, podobooCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, paraTroopaCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, goombaCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, kleptoCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, podobooCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, paraTroopaCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds1 = [
        mushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds1,
        slowMushroomCapsuleSpaceOdds1, flutterCapsuleSpaceOdds1, cannonCapsuleSpaceOdds1,
        snackCapsuleSpaceOdds1, goombaCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds1,
        piranhaPlantCapsuleSpaceOdds1, kleptoCapsuleSpaceOdds1, kamekCapsuleSpaceOdds1,
        toadyCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds1, banditCapsuleSpaceOdds1,
        pinkBooCapsuleSpaceOdds1, spinyCapsuleSpaceOdds1, podobooCapsuleSpaceOdds1,
        tweesterCapsuleSpaceOdds1, thwompCapsuleSpaceOdds1, warpCapsuleSpaceOdds1,
        bombCapsuleSpaceOdds1, fireballCapsuleSpaceOdds1, paraTroopaCapsuleSpaceOdds1,
        eggCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds1, magicCapsuleSpaceOdds1,
        tripleCapsuleSpaceOdds1, koopaCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds1,
        duelCapsuleSpaceOdds1, dkCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds1
    ]

    spaceOdds2 = [
        mushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds2,
        slowMushroomCapsuleSpaceOdds2, flutterCapsuleSpaceOdds2, cannonCapsuleSpaceOdds2,
        snackCapsuleSpaceOdds2, goombaCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds2,
        piranhaPlantCapsuleSpaceOdds2, kleptoCapsuleSpaceOdds2, kamekCapsuleSpaceOdds2,
        toadyCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds2, banditCapsuleSpaceOdds2,
        pinkBooCapsuleSpaceOdds2, spinyCapsuleSpaceOdds2, podobooCapsuleSpaceOdds2,
        tweesterCapsuleSpaceOdds2, thwompCapsuleSpaceOdds2, warpCapsuleSpaceOdds2,
        bombCapsuleSpaceOdds2, fireballCapsuleSpaceOdds2, paraTroopaCapsuleSpaceOdds2,
        eggCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds2, magicCapsuleSpaceOdds2,
        tripleCapsuleSpaceOdds2, koopaCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds2,
        duelCapsuleSpaceOdds2, dkCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds2
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, goombaCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, kleptoCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, podobooCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, paraTroopaCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]

    def safe_int(val):
        try:
            return int(val) if val else 0
        except (ValueError, TypeError):
            return 0
    
    shopOdds12Weights = sum(safe_int(weight) for weight in shopOdds12)
    shopOdds34Weights = sum(safe_int(weight) for weight in shopOdds34)
    spaceOdds1Weights = sum(safe_int(weight) for weight in spaceOdds1)
    spaceOdds2Weights = sum(safe_int(weight) for weight in spaceOdds2)
    spaceOdds34Weights = sum(safe_int(weight) for weight in spaceOdds34)

    def calculateWeight(weight, total):
        # Convert weight to int, default to 0 if empty or None
        weight = int(weight) if weight else 0
        # Check for total being zero to avoid division by zero
        if total <= 0:
            return 0  # Return 0 if total is zero or negative
        if total < 100:
            return weight  # Return the weight directly if total is less than 100
        else:
            percentage = (weight / total) * 100
            if 0 < percentage < 1:
                return math.ceil(percentage)
            return round(percentage)

    # Calculate weights for shop odds 12
    mushroomCapsuleShopOdds12 = calculateWeight(mushroomCapsuleShopOdds12, shopOdds12Weights)
    goldenMushroomCapsuleShopOdds12 = calculateWeight(goldenMushroomCapsuleShopOdds12, shopOdds12Weights)
    metalMushroomCapsuleShopOdds12 = calculateWeight(metalMushroomCapsuleShopOdds12, shopOdds12Weights)
    slowMushroomCapsuleShopOdds12 = calculateWeight(slowMushroomCapsuleShopOdds12, shopOdds12Weights)
    flutterCapsuleShopOdds12 = calculateWeight(flutterCapsuleShopOdds12, shopOdds12Weights)
    cannonCapsuleShopOdds12 = calculateWeight(cannonCapsuleShopOdds12, shopOdds12Weights)
    snackCapsuleShopOdds12 = calculateWeight(snackCapsuleShopOdds12, shopOdds12Weights)
    goombaCapsuleShopOdds12 = calculateWeight(goombaCapsuleShopOdds12, shopOdds12Weights)
    hammerBroCapsuleShopOdds12 = calculateWeight(hammerBroCapsuleShopOdds12, shopOdds12Weights)
    piranhaPlantCapsuleShopOdds12 = calculateWeight(piranhaPlantCapsuleShopOdds12, shopOdds12Weights)
    kleptoCapsuleShopOdds12 = calculateWeight(kleptoCapsuleShopOdds12, shopOdds12Weights)
    kamekCapsuleShopOdds12 = calculateWeight(kamekCapsuleShopOdds12, shopOdds12Weights)
    toadyCapsuleShopOdds12 = calculateWeight(toadyCapsuleShopOdds12, shopOdds12Weights)
    mrBlizzardCapsuleShopOdds12 = calculateWeight(mrBlizzardCapsuleShopOdds12, shopOdds12Weights)
    banditCapsuleShopOdds12 = calculateWeight(banditCapsuleShopOdds12, shopOdds12Weights)
    pinkBooCapsuleShopOdds12 = calculateWeight(pinkBooCapsuleShopOdds12, shopOdds12Weights)
    spinyCapsuleShopOdds12 = calculateWeight(spinyCapsuleShopOdds12, shopOdds12Weights)
    podobooCapsuleShopOdds12 = calculateWeight(podobooCapsuleShopOdds12, shopOdds12Weights)
    tweesterCapsuleShopOdds12 = calculateWeight(tweesterCapsuleShopOdds12, shopOdds12Weights)
    thwompCapsuleShopOdds12 = calculateWeight(thwompCapsuleShopOdds12, shopOdds12Weights)
    warpCapsuleShopOdds12 = calculateWeight(warpCapsuleShopOdds12, shopOdds12Weights)
    bombCapsuleShopOdds12 = calculateWeight(bombCapsuleShopOdds12, shopOdds12Weights)
    fireballCapsuleShopOdds12 = calculateWeight(fireballCapsuleShopOdds12, shopOdds12Weights)
    paraTroopaCapsuleShopOdds12 = calculateWeight(paraTroopaCapsuleShopOdds12, shopOdds12Weights)
    eggCapsuleShopOdds12 = calculateWeight(eggCapsuleShopOdds12, shopOdds12Weights)
    vacuumCapsuleShopOdds12 = calculateWeight(vacuumCapsuleShopOdds12, shopOdds12Weights)
    magicCapsuleShopOdds12 = calculateWeight(magicCapsuleShopOdds12, shopOdds12Weights)
    tripleCapsuleShopOdds12 = calculateWeight(tripleCapsuleShopOdds12, shopOdds12Weights)
    koopaCapsuleShopOdds12 = calculateWeight(koopaCapsuleShopOdds12, shopOdds12Weights)
    mysteryCapsuleShopOdds12 = calculateWeight(mysteryCapsuleShopOdds12, shopOdds12Weights)
    duelCapsuleShopOdds12 = calculateWeight(duelCapsuleShopOdds12, shopOdds12Weights)
    dkCapsuleShopOdds12 = calculateWeight(dkCapsuleShopOdds12, shopOdds12Weights)
    orbBagCapsuleShopOdds12 = calculateWeight(orbBagCapsuleShopOdds12, shopOdds12Weights)

    # Calculate weights for shop odds 34
    mushroomCapsuleShopOdds34 = calculateWeight(mushroomCapsuleShopOdds34, shopOdds34Weights)
    goldenMushroomCapsuleShopOdds34 = calculateWeight(goldenMushroomCapsuleShopOdds34, shopOdds34Weights)
    metalMushroomCapsuleShopOdds34 = calculateWeight(metalMushroomCapsuleShopOdds34, shopOdds34Weights)
    slowMushroomCapsuleShopOdds34 = calculateWeight(slowMushroomCapsuleShopOdds34, shopOdds34Weights)
    flutterCapsuleShopOdds34 = calculateWeight(flutterCapsuleShopOdds34, shopOdds34Weights)
    cannonCapsuleShopOdds34 = calculateWeight(cannonCapsuleShopOdds34, shopOdds34Weights)
    snackCapsuleShopOdds34 = calculateWeight(snackCapsuleShopOdds34, shopOdds34Weights)
    goombaCapsuleShopOdds34 = calculateWeight(goombaCapsuleShopOdds34, shopOdds34Weights)
    hammerBroCapsuleShopOdds34 = calculateWeight(hammerBroCapsuleShopOdds34, shopOdds34Weights)
    piranhaPlantCapsuleShopOdds34 = calculateWeight(piranhaPlantCapsuleShopOdds34, shopOdds34Weights)
    kleptoCapsuleShopOdds34 = calculateWeight(kleptoCapsuleShopOdds34, shopOdds34Weights)
    kamekCapsuleShopOdds34 = calculateWeight(kamekCapsuleShopOdds34, shopOdds34Weights)
    toadyCapsuleShopOdds34 = calculateWeight(toadyCapsuleShopOdds34, shopOdds34Weights)
    mrBlizzardCapsuleShopOdds34 = calculateWeight(mrBlizzardCapsuleShopOdds34, shopOdds34Weights)
    banditCapsuleShopOdds34 = calculateWeight(banditCapsuleShopOdds34, shopOdds34Weights)
    pinkBooCapsuleShopOdds34 = calculateWeight(pinkBooCapsuleShopOdds34, shopOdds34Weights)
    spinyCapsuleShopOdds34 = calculateWeight(spinyCapsuleShopOdds34, shopOdds34Weights)
    podobooCapsuleShopOdds34 = calculateWeight(podobooCapsuleShopOdds34, shopOdds34Weights)
    tweesterCapsuleShopOdds34 = calculateWeight(tweesterCapsuleShopOdds34, shopOdds34Weights)
    thwompCapsuleShopOdds34 = calculateWeight(thwompCapsuleShopOdds34, shopOdds34Weights)
    warpCapsuleShopOdds34 = calculateWeight(warpCapsuleShopOdds34, shopOdds34Weights)
    bombCapsuleShopOdds34 = calculateWeight(bombCapsuleShopOdds34, shopOdds34Weights)
    fireballCapsuleShopOdds34 = calculateWeight(fireballCapsuleShopOdds34, shopOdds34Weights)
    paraTroopaCapsuleShopOdds34 = calculateWeight(paraTroopaCapsuleShopOdds34, shopOdds34Weights)
    eggCapsuleShopOdds34 = calculateWeight(eggCapsuleShopOdds34, shopOdds34Weights)
    vacuumCapsuleShopOdds34 = calculateWeight(vacuumCapsuleShopOdds34, shopOdds34Weights)
    magicCapsuleShopOdds34 = calculateWeight(magicCapsuleShopOdds34, shopOdds34Weights)
    tripleCapsuleShopOdds34 = calculateWeight(tripleCapsuleShopOdds34, shopOdds34Weights)
    koopaCapsuleShopOdds34 = calculateWeight(koopaCapsuleShopOdds34, shopOdds34Weights)
    mysteryCapsuleShopOdds34 = calculateWeight(mysteryCapsuleShopOdds34, shopOdds34Weights)
    duelCapsuleShopOdds34 = calculateWeight(duelCapsuleShopOdds34, shopOdds34Weights)
    dkCapsuleShopOdds34 = calculateWeight(dkCapsuleShopOdds34, shopOdds34Weights)
    orbBagCapsuleShopOdds34 = calculateWeight(orbBagCapsuleShopOdds34, shopOdds34Weights)

    # Calculate weights for space odds 1
    mushroomCapsuleSpaceOdds1 = calculateWeight(mushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    goldenMushroomCapsuleSpaceOdds1 = calculateWeight(goldenMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    metalMushroomCapsuleSpaceOdds1 = calculateWeight(metalMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    slowMushroomCapsuleSpaceOdds1 = calculateWeight(slowMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    flutterCapsuleSpaceOdds1 = calculateWeight(flutterCapsuleSpaceOdds1, spaceOdds1Weights)
    cannonCapsuleSpaceOdds1 = calculateWeight(cannonCapsuleSpaceOdds1, spaceOdds1Weights)
    snackCapsuleSpaceOdds1 = calculateWeight(snackCapsuleSpaceOdds1, spaceOdds1Weights)
    goombaCapsuleSpaceOdds1 = calculateWeight(goombaCapsuleSpaceOdds1, spaceOdds1Weights)
    hammerBroCapsuleSpaceOdds1 = calculateWeight(hammerBroCapsuleSpaceOdds1, spaceOdds1Weights)
    piranhaPlantCapsuleSpaceOdds1 = calculateWeight(piranhaPlantCapsuleSpaceOdds1, spaceOdds1Weights)
    kleptoCapsuleSpaceOdds1 = calculateWeight(kleptoCapsuleSpaceOdds1, spaceOdds1Weights)
    kamekCapsuleSpaceOdds1 = calculateWeight(kamekCapsuleSpaceOdds1, spaceOdds1Weights)
    toadyCapsuleSpaceOdds1 = calculateWeight(toadyCapsuleSpaceOdds1, spaceOdds1Weights)
    mrBlizzardCapsuleSpaceOdds1 = calculateWeight(mrBlizzardCapsuleSpaceOdds1, spaceOdds1Weights)
    banditCapsuleSpaceOdds1 = calculateWeight(banditCapsuleSpaceOdds1, spaceOdds1Weights)
    pinkBooCapsuleSpaceOdds1 = calculateWeight(pinkBooCapsuleSpaceOdds1, spaceOdds1Weights)
    spinyCapsuleSpaceOdds1 = calculateWeight(spinyCapsuleSpaceOdds1, spaceOdds1Weights)
    podobooCapsuleSpaceOdds1 = calculateWeight(podobooCapsuleSpaceOdds1, spaceOdds1Weights)
    tweesterCapsuleSpaceOdds1 = calculateWeight(tweesterCapsuleSpaceOdds1, spaceOdds1Weights)
    thwompCapsuleSpaceOdds1 = calculateWeight(thwompCapsuleSpaceOdds1, spaceOdds1Weights)
    warpCapsuleSpaceOdds1 = calculateWeight(warpCapsuleSpaceOdds1, spaceOdds1Weights)
    bombCapsuleSpaceOdds1 = calculateWeight(bombCapsuleSpaceOdds1, spaceOdds1Weights)
    fireballCapsuleSpaceOdds1 = calculateWeight(fireballCapsuleSpaceOdds1, spaceOdds1Weights)
    paraTroopaCapsuleSpaceOdds1 = calculateWeight(paraTroopaCapsuleSpaceOdds1, spaceOdds1Weights)
    eggCapsuleSpaceOdds1 = calculateWeight(eggCapsuleSpaceOdds1, spaceOdds1Weights)
    vacuumCapsuleSpaceOdds1 = calculateWeight(vacuumCapsuleSpaceOdds1, spaceOdds1Weights)
    magicCapsuleSpaceOdds1 = calculateWeight(magicCapsuleSpaceOdds1, spaceOdds1Weights)
    tripleCapsuleSpaceOdds1 = calculateWeight(tripleCapsuleSpaceOdds1, spaceOdds1Weights)
    koopaCapsuleSpaceOdds1 = calculateWeight(koopaCapsuleSpaceOdds1, spaceOdds1Weights)
    mysteryCapsuleSpaceOdds1 = calculateWeight(mysteryCapsuleSpaceOdds1, spaceOdds1Weights)
    duelCapsuleSpaceOdds1 = calculateWeight(duelCapsuleSpaceOdds1, spaceOdds1Weights)
    dkCapsuleSpaceOdds1 = calculateWeight(dkCapsuleSpaceOdds1, spaceOdds1Weights)
    orbBagCapsuleSpaceOdds1 = calculateWeight(orbBagCapsuleSpaceOdds1, spaceOdds1Weights)

    # Calculate weights for space odds 2
    mushroomCapsuleSpaceOdds2 = calculateWeight(mushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    goldenMushroomCapsuleSpaceOdds2 = calculateWeight(goldenMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    metalMushroomCapsuleSpaceOdds2 = calculateWeight(metalMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    slowMushroomCapsuleSpaceOdds2 = calculateWeight(slowMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    flutterCapsuleSpaceOdds2 = calculateWeight(flutterCapsuleSpaceOdds2, spaceOdds2Weights)
    cannonCapsuleSpaceOdds2 = calculateWeight(cannonCapsuleSpaceOdds2, spaceOdds2Weights)
    snackCapsuleSpaceOdds2 = calculateWeight(snackCapsuleSpaceOdds2, spaceOdds2Weights)
    goombaCapsuleSpaceOdds2 = calculateWeight(goombaCapsuleSpaceOdds2, spaceOdds2Weights)
    hammerBroCapsuleSpaceOdds2 = calculateWeight(hammerBroCapsuleSpaceOdds2, spaceOdds2Weights)
    piranhaPlantCapsuleSpaceOdds2 = calculateWeight(piranhaPlantCapsuleSpaceOdds2, spaceOdds2Weights)
    kleptoCapsuleSpaceOdds2 = calculateWeight(kleptoCapsuleSpaceOdds2, spaceOdds2Weights)
    kamekCapsuleSpaceOdds2 = calculateWeight(kamekCapsuleSpaceOdds2, spaceOdds2Weights)
    toadyCapsuleSpaceOdds2 = calculateWeight(toadyCapsuleSpaceOdds2, spaceOdds2Weights)
    mrBlizzardCapsuleSpaceOdds2 = calculateWeight(mrBlizzardCapsuleSpaceOdds2, spaceOdds2Weights)
    banditCapsuleSpaceOdds2 = calculateWeight(banditCapsuleSpaceOdds2, spaceOdds2Weights)
    pinkBooCapsuleSpaceOdds2 = calculateWeight(pinkBooCapsuleSpaceOdds2, spaceOdds2Weights)
    spinyCapsuleSpaceOdds2 = calculateWeight(spinyCapsuleSpaceOdds2, spaceOdds2Weights)
    podobooCapsuleSpaceOdds2 = calculateWeight(podobooCapsuleSpaceOdds2, spaceOdds2Weights)
    tweesterCapsuleSpaceOdds2 = calculateWeight(tweesterCapsuleSpaceOdds2, spaceOdds2Weights)
    thwompCapsuleSpaceOdds2 = calculateWeight(thwompCapsuleSpaceOdds2, spaceOdds2Weights)
    warpCapsuleSpaceOdds2 = calculateWeight(warpCapsuleSpaceOdds2, spaceOdds2Weights)
    bombCapsuleSpaceOdds2 = calculateWeight(bombCapsuleSpaceOdds2, spaceOdds2Weights)
    fireballCapsuleSpaceOdds2 = calculateWeight(fireballCapsuleSpaceOdds2, spaceOdds2Weights)
    paraTroopaCapsuleSpaceOdds2 = calculateWeight(paraTroopaCapsuleSpaceOdds2, spaceOdds2Weights)
    eggCapsuleSpaceOdds2 = calculateWeight(eggCapsuleSpaceOdds2, spaceOdds2Weights)
    vacuumCapsuleSpaceOdds2 = calculateWeight(vacuumCapsuleSpaceOdds2, spaceOdds2Weights)
    magicCapsuleSpaceOdds2 = calculateWeight(magicCapsuleSpaceOdds2, spaceOdds2Weights)
    tripleCapsuleSpaceOdds2 = calculateWeight(tripleCapsuleSpaceOdds2, spaceOdds2Weights)
    koopaCapsuleSpaceOdds2 = calculateWeight(koopaCapsuleSpaceOdds2, spaceOdds2Weights)
    mysteryCapsuleSpaceOdds2 = calculateWeight(mysteryCapsuleSpaceOdds2, spaceOdds2Weights)
    duelCapsuleSpaceOdds2 = calculateWeight(duelCapsuleSpaceOdds2, spaceOdds2Weights)
    dkCapsuleSpaceOdds2 = calculateWeight(dkCapsuleSpaceOdds2, spaceOdds2Weights)
    orbBagCapsuleSpaceOdds2 = calculateWeight(orbBagCapsuleSpaceOdds2, spaceOdds2Weights)

    # Calculate weights for space odds 34
    mushroomCapsuleSpaceOdds34 = calculateWeight(mushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    goldenMushroomCapsuleSpaceOdds34 = calculateWeight(goldenMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    metalMushroomCapsuleSpaceOdds34 = calculateWeight(metalMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    slowMushroomCapsuleSpaceOdds34 = calculateWeight(slowMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    flutterCapsuleSpaceOdds34 = calculateWeight(flutterCapsuleSpaceOdds34, spaceOdds34Weights)
    cannonCapsuleSpaceOdds34 = calculateWeight(cannonCapsuleSpaceOdds34, spaceOdds34Weights)
    snackCapsuleSpaceOdds34 = calculateWeight(snackCapsuleSpaceOdds34, spaceOdds34Weights)
    goombaCapsuleSpaceOdds34 = calculateWeight(goombaCapsuleSpaceOdds34, spaceOdds34Weights)
    hammerBroCapsuleSpaceOdds34 = calculateWeight(hammerBroCapsuleSpaceOdds34, spaceOdds34Weights)
    piranhaPlantCapsuleSpaceOdds34 = calculateWeight(piranhaPlantCapsuleSpaceOdds34, spaceOdds34Weights)
    kleptoCapsuleSpaceOdds34 = calculateWeight(kleptoCapsuleSpaceOdds34, spaceOdds34Weights)
    kamekCapsuleSpaceOdds34 = calculateWeight(kamekCapsuleSpaceOdds34, spaceOdds34Weights)
    toadyCapsuleSpaceOdds34 = calculateWeight(toadyCapsuleSpaceOdds34, spaceOdds34Weights)
    mrBlizzardCapsuleSpaceOdds34 = calculateWeight(mrBlizzardCapsuleSpaceOdds34, spaceOdds34Weights)
    banditCapsuleSpaceOdds34 = calculateWeight(banditCapsuleSpaceOdds34, spaceOdds34Weights)
    pinkBooCapsuleSpaceOdds34 = calculateWeight(pinkBooCapsuleSpaceOdds34, spaceOdds34Weights)
    spinyCapsuleSpaceOdds34 = calculateWeight(spinyCapsuleSpaceOdds34, spaceOdds34Weights)
    podobooCapsuleSpaceOdds34 = calculateWeight(podobooCapsuleSpaceOdds34, spaceOdds34Weights)
    tweesterCapsuleSpaceOdds34 = calculateWeight(tweesterCapsuleSpaceOdds34, spaceOdds34Weights)
    thwompCapsuleSpaceOdds34 = calculateWeight(thwompCapsuleSpaceOdds34, spaceOdds34Weights)
    warpCapsuleSpaceOdds34 = calculateWeight(warpCapsuleSpaceOdds34, spaceOdds34Weights)
    bombCapsuleSpaceOdds34 = calculateWeight(bombCapsuleSpaceOdds34, spaceOdds34Weights)
    fireballCapsuleSpaceOdds34 = calculateWeight(fireballCapsuleSpaceOdds34, spaceOdds34Weights)
    paraTroopaCapsuleSpaceOdds34 = calculateWeight(paraTroopaCapsuleSpaceOdds34, spaceOdds34Weights)
    eggCapsuleSpaceOdds34 = calculateWeight(eggCapsuleSpaceOdds34, spaceOdds34Weights)
    vacuumCapsuleSpaceOdds34 = calculateWeight(vacuumCapsuleSpaceOdds34, spaceOdds34Weights)
    magicCapsuleSpaceOdds34 = calculateWeight(magicCapsuleSpaceOdds34, spaceOdds34Weights)
    tripleCapsuleSpaceOdds34 = calculateWeight(tripleCapsuleSpaceOdds34, spaceOdds34Weights)
    koopaCapsuleSpaceOdds34 = calculateWeight(koopaCapsuleSpaceOdds34, spaceOdds34Weights)
    mysteryCapsuleSpaceOdds34 = calculateWeight(mysteryCapsuleSpaceOdds34, spaceOdds34Weights)
    duelCapsuleSpaceOdds34 = calculateWeight(duelCapsuleSpaceOdds34, spaceOdds34Weights)
    dkCapsuleSpaceOdds34 = calculateWeight(dkCapsuleSpaceOdds34, spaceOdds34Weights)
    orbBagCapsuleSpaceOdds34 = calculateWeight(orbBagCapsuleSpaceOdds34, spaceOdds34Weights)


    # Redefine Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, goombaCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, kleptoCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, podobooCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, paraTroopaCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, goombaCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, kleptoCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, podobooCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, paraTroopaCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds1 = [
        mushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds1,
        slowMushroomCapsuleSpaceOdds1, flutterCapsuleSpaceOdds1, cannonCapsuleSpaceOdds1,
        snackCapsuleSpaceOdds1, goombaCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds1,
        piranhaPlantCapsuleSpaceOdds1, kleptoCapsuleSpaceOdds1, kamekCapsuleSpaceOdds1,
        toadyCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds1, banditCapsuleSpaceOdds1,
        pinkBooCapsuleSpaceOdds1, spinyCapsuleSpaceOdds1, podobooCapsuleSpaceOdds1,
        tweesterCapsuleSpaceOdds1, thwompCapsuleSpaceOdds1, warpCapsuleSpaceOdds1,
        bombCapsuleSpaceOdds1, fireballCapsuleSpaceOdds1, paraTroopaCapsuleSpaceOdds1,
        eggCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds1, magicCapsuleSpaceOdds1,
        tripleCapsuleSpaceOdds1, koopaCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds1,
        duelCapsuleSpaceOdds1, dkCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds1
    ]

    spaceOdds2 = [
        mushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds2,
        slowMushroomCapsuleSpaceOdds2, flutterCapsuleSpaceOdds2, cannonCapsuleSpaceOdds2,
        snackCapsuleSpaceOdds2, goombaCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds2,
        piranhaPlantCapsuleSpaceOdds2, kleptoCapsuleSpaceOdds2, kamekCapsuleSpaceOdds2,
        toadyCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds2, banditCapsuleSpaceOdds2,
        pinkBooCapsuleSpaceOdds2, spinyCapsuleSpaceOdds2, podobooCapsuleSpaceOdds2,
        tweesterCapsuleSpaceOdds2, thwompCapsuleSpaceOdds2, warpCapsuleSpaceOdds2,
        bombCapsuleSpaceOdds2, fireballCapsuleSpaceOdds2, paraTroopaCapsuleSpaceOdds2,
        eggCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds2, magicCapsuleSpaceOdds2,
        tripleCapsuleSpaceOdds2, koopaCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds2,
        duelCapsuleSpaceOdds2, dkCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds2
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, goombaCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, kleptoCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, podobooCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, paraTroopaCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]

    shopOdds12Weights = sum(weight for weight in shopOdds12)
    shopOdds34Weights = sum(weight for weight in shopOdds34)
    spaceOdds1Weights = sum(weight for weight in spaceOdds1)
    spaceOdds2Weights = sum(weight for weight in spaceOdds2)
    spaceOdds34Weights = sum(weight for weight in shopOdds34)

    if spaceOdds1Weights < 101:
        spaceOdds1Max = max(zip(spaceOdds1, spaceOdds1), key=lambda tuple: tuple[1])[0]

    if spaceOdds34Weights < 101:
        spaceOdds34Max = max(zip(spaceOdds34, spaceOdds34), key=lambda tuple: tuple[1])[0]

    if shopOdds12Weights < 101:
        shopOdds12Max = max(zip(shopOdds12, shopOdds12), key=lambda tuple: tuple[1])[0]

    if spaceOdds2Weights < 101:
        spaceOdds2Max = max(zip(spaceOdds2, spaceOdds2), key=lambda tuple: tuple[1])[0]

    if shopOdds34Weights < 101:
        shopOdds34Max = max(zip(shopOdds34, shopOdds34), key=lambda tuple: tuple[1])[0]

    if shopOdds12Max == 'mushroomCapsuleShopOdds12':
        mushroomCapsuleShopOdds12 += (100 - mushroomCapsuleShopOdds12)

    if shopOdds12Max == 'goldenMushroomCapsuleShopOdds12':
        goldenMushroomCapsuleShopOdds12 += (100 - goldenMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'metalMushroomCapsuleShopOdds12':
        metalMushroomCapsuleShopOdds12 += (100 - metalMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'slowMushroomCapsuleShopOdds12':
        slowMushroomCapsuleShopOdds12 += (100 - slowMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'flutterCapsuleShopOdds12':
        flutterCapsuleShopOdds12 += (100 - flutterCapsuleShopOdds12)

    if shopOdds12Max == 'cannonCapsuleShopOdds12':
        cannonCapsuleShopOdds12 += (100 - cannonCapsuleShopOdds12)

    if shopOdds12Max == 'snackCapsuleShopOdds12':
        snackCapsuleShopOdds12 += (100 - snackCapsuleShopOdds12)

    if shopOdds12Max == 'goombaCapsuleShopOdds12':
        goombaCapsuleShopOdds12 += (100 - goombaCapsuleShopOdds12)

    if shopOdds12Max == 'hammerBroCapsuleShopOdds12':
        hammerBroCapsuleShopOdds12 += (100 - hammerBroCapsuleShopOdds12)

    if shopOdds12Max == 'piranhaPlantCapsuleShopOdds12':
        piranhaPlantCapsuleShopOdds12 += (100 - piranhaPlantCapsuleShopOdds12)

    if shopOdds12Max == 'kleptoCapsuleShopOdds12':
        kleptoCapsuleShopOdds12 += (100 - kleptoCapsuleShopOdds12)

    if shopOdds12Max == 'kamekCapsuleShopOdds12':
        kamekCapsuleShopOdds12 += (100 - kamekCapsuleShopOdds12)

    if shopOdds12Max == 'toadyCapsuleShopOdds12':
        toadyCapsuleShopOdds12 += (100 - toadyCapsuleShopOdds12)

    if shopOdds12Max == 'mrBlizzardCapsuleShopOdds12':
        mrBlizzardCapsuleShopOdds12 += (100 - mrBlizzardCapsuleShopOdds12)

    if shopOdds12Max == 'banditCapsuleShopOdds12':
        banditCapsuleShopOdds12 += (100 - banditCapsuleShopOdds12)

    if shopOdds12Max == 'pinkBooCapsuleShopOdds12':
        pinkBooCapsuleShopOdds12 += (100 - pinkBooCapsuleShopOdds12)

    if shopOdds12Max == 'spinyCapsuleShopOdds12':
        spinyCapsuleShopOdds12 += (100 - spinyCapsuleShopOdds12)

    if shopOdds12Max == 'podobooCapsuleShopOdds12':
        podobooCapsuleShopOdds12 += (100 - podobooCapsuleShopOdds12)

    if shopOdds12Max == 'tweesterCapsuleShopOdds12':
        tweesterCapsuleShopOdds12 += (100 - tweesterCapsuleShopOdds12)

    if shopOdds12Max == 'thwompCapsuleShopOdds12':
        thwompCapsuleShopOdds12 += (100 - thwompCapsuleShopOdds12)

    if shopOdds12Max == 'warpCapsuleShopOdds12':
        warpCapsuleShopOdds12 += (100 - warpCapsuleShopOdds12)

    if shopOdds12Max == 'bombCapsuleShopOdds12':
        bombCapsuleShopOdds12 += (100 - bombCapsuleShopOdds12)

    if shopOdds12Max == 'fireballCapsuleShopOdds12':
        fireballCapsuleShopOdds12 += (100 - fireballCapsuleShopOdds12)

    if shopOdds12Max == 'paraTroopaCapsuleShopOdds12':
        paraTroopaCapsuleShopOdds12 += (100 - paraTroopaCapsuleShopOdds12)

    if shopOdds12Max == 'eggCapsuleShopOdds12':
        eggCapsuleShopOdds12 += (100 - eggCapsuleShopOdds12)

    if shopOdds12Max == 'vacuumCapsuleShopOdds12':
        vacuumCapsuleShopOdds12 += (100 - vacuumCapsuleShopOdds12)

    if shopOdds12Max == 'magicCapsuleShopOdds12':
        magicCapsuleShopOdds12 += (100 - magicCapsuleShopOdds12)

    if shopOdds12Max == 'tripleCapsuleShopOdds12':
        tripleCapsuleShopOdds12 += (100 - tripleCapsuleShopOdds12)

    if shopOdds12Max == 'koopaCapsuleShopOdds12':
        koopaCapsuleShopOdds12 += (100 - koopaCapsuleShopOdds12)

    if shopOdds12Max == 'mysteryCapsuleShopOdds12':
        mysteryCapsuleShopOdds12 += (100 - mysteryCapsuleShopOdds12)

    if shopOdds12Max == 'duelCapsuleShopOdds12':
        duelCapsuleShopOdds12 += (100 - duelCapsuleShopOdds12)

    if shopOdds12Max == 'dkCapsuleShopOdds12':
        dkCapsuleShopOdds12 += (100 - dkCapsuleShopOdds12)

    if shopOdds12Max == 'orbBagCapsuleShopOdds12':
        orbBagCapsuleShopOdds12 += (100 - orbBagCapsuleShopOdds12)

    if shopOdds34Max == 'mushroomCapsuleShopOdds34':
        mushroomCapsuleShopOdds34 += (100 - mushroomCapsuleShopOdds34)

    if shopOdds34Max == 'goldenMushroomCapsuleShopOdds34':
        goldenMushroomCapsuleShopOdds34 += (100 - goldenMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'metalMushroomCapsuleShopOdds34':
        metalMushroomCapsuleShopOdds34 += (100 - metalMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'slowMushroomCapsuleShopOdds34':
        slowMushroomCapsuleShopOdds34 += (100 - slowMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'flutterCapsuleShopOdds34':
        flutterCapsuleShopOdds34 += (100 - flutterCapsuleShopOdds34)

    if shopOdds34Max == 'cannonCapsuleShopOdds34':
        cannonCapsuleShopOdds34 += (100 - cannonCapsuleShopOdds34)

    if shopOdds34Max == 'snackCapsuleShopOdds34':
        snackCapsuleShopOdds34 += (100 - snackCapsuleShopOdds34)

    if shopOdds34Max == 'goombaCapsuleShopOdds34':
        goombaCapsuleShopOdds34 += (100 - goombaCapsuleShopOdds34)

    if shopOdds34Max == 'hammerBroCapsuleShopOdds34':
        hammerBroCapsuleShopOdds34 += (100 - hammerBroCapsuleShopOdds34)

    if shopOdds34Max == 'piranhaPlantCapsuleShopOdds34':
        piranhaPlantCapsuleShopOdds34 += (100 - piranhaPlantCapsuleShopOdds34)

    if shopOdds34Max == 'kleptoCapsuleShopOdds34':
        kleptoCapsuleShopOdds34 += (100 - kleptoCapsuleShopOdds34)

    if shopOdds34Max == 'kamekCapsuleShopOdds34':
        kamekCapsuleShopOdds34 += (100 - kamekCapsuleShopOdds34)

    if shopOdds34Max == 'toadyCapsuleShopOdds34':
        toadyCapsuleShopOdds34 += (100 - toadyCapsuleShopOdds34)

    if shopOdds34Max == 'mrBlizzardCapsuleShopOdds34':
        mrBlizzardCapsuleShopOdds34 += (100 - mrBlizzardCapsuleShopOdds34)

    if shopOdds34Max == 'banditCapsuleShopOdds34':
        banditCapsuleShopOdds34 += (100 - banditCapsuleShopOdds34)

    if shopOdds34Max == 'pinkBooCapsuleShopOdds34':
        pinkBooCapsuleShopOdds34 += (100 - pinkBooCapsuleShopOdds34)

    if shopOdds34Max == 'spinyCapsuleShopOdds34':
        spinyCapsuleShopOdds34 += (100 - spinyCapsuleShopOdds34)

    if shopOdds34Max == 'podobooCapsuleShopOdds34':
        podobooCapsuleShopOdds34 += (100 - podobooCapsuleShopOdds34)

    if shopOdds34Max == 'tweesterCapsuleShopOdds34':
        tweesterCapsuleShopOdds34 += (100 - tweesterCapsuleShopOdds34)

    if shopOdds34Max == 'thwompCapsuleShopOdds34':
        thwompCapsuleShopOdds34 += (100 - thwompCapsuleShopOdds34)

    if shopOdds34Max == 'warpCapsuleShopOdds34':
        warpCapsuleShopOdds34 += (100 - warpCapsuleShopOdds34)

    if shopOdds34Max == 'bombCapsuleShopOdds34':
        bombCapsuleShopOdds34 += (100 - bombCapsuleShopOdds34)

    if shopOdds34Max == 'fireballCapsuleShopOdds34':
        fireballCapsuleShopOdds34 += (100 - fireballCapsuleShopOdds34)

    if shopOdds34Max == 'paraTroopaCapsuleShopOdds34':
        paraTroopaCapsuleShopOdds34 += (100 - paraTroopaCapsuleShopOdds34)

    if shopOdds34Max == 'eggCapsuleShopOdds34':
        eggCapsuleShopOdds34 += (100 - eggCapsuleShopOdds34)

    if shopOdds34Max == 'vacuumCapsuleShopOdds34':
        vacuumCapsuleShopOdds34 += (100 - vacuumCapsuleShopOdds34)

    if shopOdds34Max == 'magicCapsuleShopOdds34':
        magicCapsuleShopOdds34 += (100 - magicCapsuleShopOdds34)

    if shopOdds34Max == 'tripleCapsuleShopOdds34':
        tripleCapsuleShopOdds34 += (100 - tripleCapsuleShopOdds34)

    if shopOdds34Max == 'koopaCapsuleShopOdds34':
        koopaCapsuleShopOdds34 += (100 - koopaCapsuleShopOdds34)

    if shopOdds34Max == 'mysteryCapsuleShopOdds34':
        mysteryCapsuleShopOdds34 += (100 - mysteryCapsuleShopOdds34)

    if shopOdds34Max == 'duelCapsuleShopOdds34':
        duelCapsuleShopOdds34 += (100 - duelCapsuleShopOdds34)

    if shopOdds34Max == 'dkCapsuleShopOdds34':
        dkCapsuleShopOdds34 += (100 - dkCapsuleShopOdds34)

    if shopOdds34Max == 'orbBagCapsuleShopOdds34':
        orbBagCapsuleShopOdds34 += (100 - orbBagCapsuleShopOdds34)

    if spaceOdds1Max == 'mushroomCapsuleSpaceOdds1':
        mushroomCapsuleSpaceOdds1 += (100 - mushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'goldenMushroomCapsuleSpaceOdds1':
        goldenMushroomCapsuleSpaceOdds1 += (100 - goldenMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'metalMushroomCapsuleSpaceOdds1':
        metalMushroomCapsuleSpaceOdds1 += (100 - metalMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'slowMushroomCapsuleSpaceOdds1':
        slowMushroomCapsuleSpaceOdds1 += (100 - slowMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'flutterCapsuleSpaceOdds1':
        flutterCapsuleSpaceOdds1 += (100 - flutterCapsuleSpaceOdds1)

    if spaceOdds1Max == 'cannonCapsuleSpaceOdds1':
        cannonCapsuleSpaceOdds1 += (100 - cannonCapsuleSpaceOdds1)

    if spaceOdds1Max == 'snackCapsuleSpaceOdds1':
        snackCapsuleSpaceOdds1 += (100 - snackCapsuleSpaceOdds1)

    if spaceOdds1Max == 'goombaCapsuleSpaceOdds1':
        goombaCapsuleSpaceOdds1 += (100 - goombaCapsuleSpaceOdds1)

    if spaceOdds1Max == 'hammerBroCapsuleSpaceOdds1':
        hammerBroCapsuleSpaceOdds1 += (100 - hammerBroCapsuleSpaceOdds1)

    if spaceOdds1Max == 'piranhaPlantCapsuleSpaceOdds1':
        piranhaPlantCapsuleSpaceOdds1 += (100 - piranhaPlantCapsuleSpaceOdds1)

    if spaceOdds1Max == 'kleptoCapsuleSpaceOdds1':
        kleptoCapsuleSpaceOdds1 += (100 - kleptoCapsuleSpaceOdds1)

    if spaceOdds1Max == 'kamekCapsuleSpaceOdds1':
        kamekCapsuleSpaceOdds1 += (100 - kamekCapsuleSpaceOdds1)

    if spaceOdds1Max == 'toadyCapsuleSpaceOdds1':
        toadyCapsuleSpaceOdds1 += (100 - toadyCapsuleSpaceOdds1)

    if spaceOdds1Max == 'mrBlizzardCapsuleSpaceOdds1':
        mrBlizzardCapsuleSpaceOdds1 += (100 - mrBlizzardCapsuleSpaceOdds1)

    if spaceOdds1Max == 'banditCapsuleSpaceOdds1':
        banditCapsuleSpaceOdds1 += (100 - banditCapsuleSpaceOdds1)

    if spaceOdds1Max == 'pinkBooCapsuleSpaceOdds1':
        pinkBooCapsuleSpaceOdds1 += (100 - pinkBooCapsuleSpaceOdds1)

    if spaceOdds1Max == 'spinyCapsuleSpaceOdds1':
        spinyCapsuleSpaceOdds1 += (100 - spinyCapsuleSpaceOdds1)

    if spaceOdds1Max == 'podobooCapsuleSpaceOdds1':
        podobooCapsuleSpaceOdds1 += (100 - podobooCapsuleSpaceOdds1)

    if spaceOdds1Max == 'tweesterCapsuleSpaceOdds1':
        tweesterCapsuleSpaceOdds1 += (100 - tweesterCapsuleSpaceOdds1)

    if spaceOdds1Max == 'thwompCapsuleSpaceOdds1':
        thwompCapsuleSpaceOdds1 += (100 - thwompCapsuleSpaceOdds1)

    if spaceOdds1Max == 'warpCapsuleSpaceOdds1':
        warpCapsuleSpaceOdds1 += (100 - warpCapsuleSpaceOdds1)

    if spaceOdds1Max == 'bombCapsuleSpaceOdds1':
        bombCapsuleSpaceOdds1 += (100 - bombCapsuleSpaceOdds1)

    if spaceOdds1Max == 'fireballCapsuleSpaceOdds1':
        fireballCapsuleSpaceOdds1 += (100 - fireballCapsuleSpaceOdds1)

    if spaceOdds1Max == 'paraTroopaCapsuleSpaceOdds1':
        paraTroopaCapsuleSpaceOdds1 += (100 - paraTroopaCapsuleSpaceOdds1)

    if spaceOdds1Max == 'eggCapsuleSpaceOdds1':
        eggCapsuleSpaceOdds1 += (100 - eggCapsuleSpaceOdds1)

    if spaceOdds1Max == 'vacuumCapsuleSpaceOdds1':
        vacuumCapsuleSpaceOdds1 += (100 - vacuumCapsuleSpaceOdds1)

    if spaceOdds1Max == 'magicCapsuleSpaceOdds1':
        magicCapsuleSpaceOdds1 += (100 - magicCapsuleSpaceOdds1)

    if spaceOdds1Max == 'tripleCapsuleSpaceOdds1':
        tripleCapsuleSpaceOdds1 += (100 - tripleCapsuleSpaceOdds1)

    if spaceOdds1Max == 'koopaCapsuleSpaceOdds1':
        koopaCapsuleSpaceOdds1 += (100 - koopaCapsuleSpaceOdds1)

    if spaceOdds1Max == 'mysteryCapsuleSpaceOdds1':
        mysteryCapsuleSpaceOdds1 += (100 - mysteryCapsuleSpaceOdds1)

    if spaceOdds1Max == 'duelCapsuleSpaceOdds1':
        duelCapsuleSpaceOdds1 += (100 - duelCapsuleSpaceOdds1)

    if spaceOdds1Max == 'dkCapsuleSpaceOdds1':
        dkCapsuleSpaceOdds1 += (100 - dkCapsuleSpaceOdds1)

    if spaceOdds1Max == 'orbBagCapsuleSpaceOdds1':
        orbBagCapsuleSpaceOdds1 += (100 - orbBagCapsuleSpaceOdds1)

    if spaceOdds2Max == 'mushroomCapsuleSpaceOdds2':
        mushroomCapsuleSpaceOdds2 += (100 - mushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'goldenMushroomCapsuleSpaceOdds2':
        goldenMushroomCapsuleSpaceOdds2 += (100 - goldenMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'metalMushroomCapsuleSpaceOdds2':
        metalMushroomCapsuleSpaceOdds2 += (100 - metalMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'slowMushroomCapsuleSpaceOdds2':
        slowMushroomCapsuleSpaceOdds2 += (100 - slowMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'flutterCapsuleSpaceOdds2':
        flutterCapsuleSpaceOdds2 += (100 - flutterCapsuleSpaceOdds2)

    if spaceOdds2Max == 'cannonCapsuleSpaceOdds2':
        cannonCapsuleSpaceOdds2 += (100 - cannonCapsuleSpaceOdds2)

    if spaceOdds2Max == 'snackCapsuleSpaceOdds2':
        snackCapsuleSpaceOdds2 += (100 - snackCapsuleSpaceOdds2)

    if spaceOdds2Max == 'goombaCapsuleSpaceOdds2':
        goombaCapsuleSpaceOdds2 += (100 - goombaCapsuleSpaceOdds2)

    if spaceOdds2Max == 'hammerBroCapsuleSpaceOdds2':
        hammerBroCapsuleSpaceOdds2 += (100 - hammerBroCapsuleSpaceOdds2)

    if spaceOdds2Max == 'piranhaPlantCapsuleSpaceOdds2':
        piranhaPlantCapsuleSpaceOdds2 += (100 - piranhaPlantCapsuleSpaceOdds2)

    if spaceOdds2Max == 'kleptoCapsuleSpaceOdds2':
        kleptoCapsuleSpaceOdds2 += (100 - kleptoCapsuleSpaceOdds2)

    if spaceOdds2Max == 'kamekCapsuleSpaceOdds2':
        kamekCapsuleSpaceOdds2 += (100 - kamekCapsuleSpaceOdds2)

    if spaceOdds2Max == 'toadyCapsuleSpaceOdds2':
        toadyCapsuleSpaceOdds2 += (100 - toadyCapsuleSpaceOdds2)

    if spaceOdds2Max == 'mrBlizzardCapsuleSpaceOdds2':
        mrBlizzardCapsuleSpaceOdds2 += (100 - mrBlizzardCapsuleSpaceOdds2)

    if spaceOdds2Max == 'banditCapsuleSpaceOdds2':
        banditCapsuleSpaceOdds2 += (100 - banditCapsuleSpaceOdds2)

    if spaceOdds2Max == 'pinkBooCapsuleSpaceOdds2':
        pinkBooCapsuleSpaceOdds2 += (100 - pinkBooCapsuleSpaceOdds2)

    if spaceOdds2Max == 'spinyCapsuleSpaceOdds2':
        spinyCapsuleSpaceOdds2 += (100 - spinyCapsuleSpaceOdds2)

    if spaceOdds2Max == 'podobooCapsuleSpaceOdds2':
        podobooCapsuleSpaceOdds2 += (100 - podobooCapsuleSpaceOdds2)

    if spaceOdds2Max == 'tweesterCapsuleSpaceOdds2':
        tweesterCapsuleSpaceOdds2 += (100 - tweesterCapsuleSpaceOdds2)

    if spaceOdds2Max == 'thwompCapsuleSpaceOdds2':
        thwompCapsuleSpaceOdds2 += (100 - thwompCapsuleSpaceOdds2)

    if spaceOdds2Max == 'warpCapsuleSpaceOdds2':
        warpCapsuleSpaceOdds2 += (100 - warpCapsuleSpaceOdds2)

    if spaceOdds2Max == 'bombCapsuleSpaceOdds2':
        bombCapsuleSpaceOdds2 += (100 - bombCapsuleSpaceOdds2)

    if spaceOdds2Max == 'fireballCapsuleSpaceOdds2':
        fireballCapsuleSpaceOdds2 += (100 - fireballCapsuleSpaceOdds2)

    if spaceOdds2Max == 'paraTroopaCapsuleSpaceOdds2':
        paraTroopaCapsuleSpaceOdds2 += (100 - paraTroopaCapsuleSpaceOdds2)

    if spaceOdds2Max == 'eggCapsuleSpaceOdds2':
        eggCapsuleSpaceOdds2 += (100 - eggCapsuleSpaceOdds2)

    if spaceOdds2Max == 'vacuumCapsuleSpaceOdds2':
        vacuumCapsuleSpaceOdds2 += (100 - vacuumCapsuleSpaceOdds2)

    if spaceOdds2Max == 'magicCapsuleSpaceOdds2':
        magicCapsuleSpaceOdds2 += (100 - magicCapsuleSpaceOdds2)

    if spaceOdds2Max == 'tripleCapsuleSpaceOdds2':
        tripleCapsuleSpaceOdds2 += (100 - tripleCapsuleSpaceOdds2)

    if spaceOdds2Max == 'koopaCapsuleSpaceOdds2':
        koopaCapsuleSpaceOdds2 += (100 - koopaCapsuleSpaceOdds2)

    if spaceOdds2Max == 'mysteryCapsuleSpaceOdds2':
        mysteryCapsuleSpaceOdds2 += (100 - mysteryCapsuleSpaceOdds2)

    if spaceOdds2Max == 'duelCapsuleSpaceOdds2':
        duelCapsuleSpaceOdds2 += (100 - duelCapsuleSpaceOdds2)

    if spaceOdds2Max == 'dkCapsuleSpaceOdds2':
        dkCapsuleSpaceOdds2 += (100 - dkCapsuleSpaceOdds2)

    if spaceOdds2Max == 'orbBagCapsuleSpaceOdds2':
        orbBagCapsuleSpaceOdds2 += (100 - orbBagCapsuleSpaceOdds2)

    if spaceOdds34Max == 'mushroomCapsuleSpaceOdds34':
        mushroomCapsuleSpaceOdds34 += (100 - mushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'goldenMushroomCapsuleSpaceOdds34':
        goldenMushroomCapsuleSpaceOdds34 += (100 - goldenMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'metalMushroomCapsuleSpaceOdds34':
        metalMushroomCapsuleSpaceOdds34 += (100 - metalMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'slowMushroomCapsuleSpaceOdds34':
        slowMushroomCapsuleSpaceOdds34 += (100 - slowMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'flutterCapsuleSpaceOdds34':
        flutterCapsuleSpaceOdds34 += (100 - flutterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'cannonCapsuleSpaceOdds34':
        cannonCapsuleSpaceOdds34 += (100 - cannonCapsuleSpaceOdds34)

    if spaceOdds34Max == 'snackCapsuleSpaceOdds34':
        snackCapsuleSpaceOdds34 += (100 - snackCapsuleSpaceOdds34)

    if spaceOdds34Max == 'goombaCapsuleSpaceOdds34':
        goombaCapsuleSpaceOdds34 += (100 - goombaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'hammerBroCapsuleSpaceOdds34':
        hammerBroCapsuleSpaceOdds34 += (100 - hammerBroCapsuleSpaceOdds34)

    if spaceOdds34Max == 'piranhaPlantCapsuleSpaceOdds34':
        piranhaPlantCapsuleSpaceOdds34 += (100 - piranhaPlantCapsuleSpaceOdds34)

    if spaceOdds34Max == 'kleptoCapsuleSpaceOdds34':
        kleptoCapsuleSpaceOdds34 += (100 - kleptoCapsuleSpaceOdds34)

    if spaceOdds34Max == 'kamekCapsuleSpaceOdds34':
        kamekCapsuleSpaceOdds34 += (100 - kamekCapsuleSpaceOdds34)

    if spaceOdds34Max == 'toadyCapsuleSpaceOdds34':
        toadyCapsuleSpaceOdds34 += (100 - toadyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mrBlizzardCapsuleSpaceOdds34':
        mrBlizzardCapsuleSpaceOdds34 += (100 - mrBlizzardCapsuleSpaceOdds34)

    if spaceOdds34Max == 'banditCapsuleSpaceOdds34':
        banditCapsuleSpaceOdds34 += (100 - banditCapsuleSpaceOdds34)

    if spaceOdds34Max == 'pinkBooCapsuleSpaceOdds34':
        pinkBooCapsuleSpaceOdds34 += (100 - pinkBooCapsuleSpaceOdds34)

    if spaceOdds34Max == 'spinyCapsuleSpaceOdds34':
        spinyCapsuleSpaceOdds34 += (100 - spinyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'podobooCapsuleSpaceOdds34':
        podobooCapsuleSpaceOdds34 += (100 - podobooCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tweesterCapsuleSpaceOdds34':
        tweesterCapsuleSpaceOdds34 += (100 - tweesterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'thwompCapsuleSpaceOdds34':
        thwompCapsuleSpaceOdds34 += (100 - thwompCapsuleSpaceOdds34)

    if spaceOdds34Max == 'warpCapsuleSpaceOdds34':
        warpCapsuleSpaceOdds34 += (100 - warpCapsuleSpaceOdds34)

    if spaceOdds34Max == 'bombCapsuleSpaceOdds34':
        bombCapsuleSpaceOdds34 += (100 - bombCapsuleSpaceOdds34)

    if spaceOdds34Max == 'fireballCapsuleSpaceOdds34':
        fireballCapsuleSpaceOdds34 += (100 - fireballCapsuleSpaceOdds34)

    if spaceOdds34Max == 'paraTroopaCapsuleSpaceOdds34':
        paraTroopaCapsuleSpaceOdds34 += (100 - paraTroopaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'eggCapsuleSpaceOdds34':
        eggCapsuleSpaceOdds34 += (100 - eggCapsuleSpaceOdds34)

    if spaceOdds34Max == 'vacuumCapsuleSpaceOdds34':
        vacuumCapsuleSpaceOdds34 += (100 - vacuumCapsuleSpaceOdds34)

    if spaceOdds34Max == 'magicCapsuleSpaceOdds34':
        magicCapsuleSpaceOdds34 += (100 - magicCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tripleCapsuleSpaceOdds34':
        tripleCapsuleSpaceOdds34 += (100 - tripleCapsuleSpaceOdds34)

    if spaceOdds34Max == 'koopaCapsuleSpaceOdds34':
        koopaCapsuleSpaceOdds34 += (100 - koopaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mysteryCapsuleSpaceOdds34':
        mysteryCapsuleSpaceOdds34 += (100 - mysteryCapsuleSpaceOdds34)

    if spaceOdds34Max == 'duelCapsuleSpaceOdds34':
        duelCapsuleSpaceOdds34 += (100 - duelCapsuleSpaceOdds34)

    if spaceOdds34Max == 'dkCapsuleSpaceOdds34':
        dkCapsuleSpaceOdds34 += (100 - dkCapsuleSpaceOdds34)

    if spaceOdds34Max == 'orbBagCapsuleSpaceOdds34':
        orbBagCapsuleSpaceOdds34 += (100 - orbBagCapsuleSpaceOdds34)

    mushroomCapsuleShopOdds12 = str(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = str(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = str(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = str(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = str(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsuleShopOdds12 = str(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = str(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = str(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = str(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = str(goldenMushroomCapsuleSpaceOdds34)

    slowMushroomCapsuleShopOdds12 = str(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = str(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = str(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = str(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = str(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsuleShopOdds12 = str(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = str(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = str(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = str(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = str(metalMushroomCapsuleSpaceOdds34)

    flutterCapsuleShopOdds12 = str(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = str(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = str(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = str(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = str(flutterCapsuleSpaceOdds34)

    cannonCapsuleShopOdds12 = str(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = str(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = str(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = str(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = str(cannonCapsuleSpaceOdds34)

    snackCapsuleShopOdds12 = str(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = str(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = str(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = str(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = str(snackCapsuleSpaceOdds34)

    goombaCapsuleShopOdds12 = str(goombaCapsuleShopOdds12)
    goombaCapsuleShopOdds34 = str(goombaCapsuleShopOdds34)
    goombaCapsuleSpaceOdds1 = str(goombaCapsuleSpaceOdds1)
    goombaCapsuleSpaceOdds2 = str(goombaCapsuleSpaceOdds2)
    goombaCapsuleSpaceOdds34 = str(goombaCapsuleSpaceOdds34)

    hammerBroCapsuleShopOdds12 = str(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = str(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = str(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = str(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = str(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsuleShopOdds12 = str(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = str(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = str(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = str(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = str(piranhaPlantCapsuleSpaceOdds34)

    kleptoCapsuleShopOdds12 = str(kleptoCapsuleShopOdds12)
    kleptoCapsuleShopOdds34 = str(kleptoCapsuleShopOdds34)
    kleptoCapsuleSpaceOdds1 = str(kleptoCapsuleSpaceOdds1)
    kleptoCapsuleSpaceOdds2 = str(kleptoCapsuleSpaceOdds2)
    kleptoCapsuleSpaceOdds34 = str(kleptoCapsuleSpaceOdds34)

    kamekCapsuleShopOdds12 = str(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = str(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = str(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = str(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = str(kamekCapsuleSpaceOdds34)

    toadyCapsuleShopOdds12 = str(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = str(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = str(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = str(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = str(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsuleShopOdds12 = str(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = str(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = str(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = str(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = str(mrBlizzardCapsuleSpaceOdds34)

    banditCapsuleShopOdds12 = str(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = str(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = str(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = str(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = str(banditCapsuleSpaceOdds34)

    pinkBooCapsuleShopOdds12 = str(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = str(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = str(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = str(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = str(pinkBooCapsuleSpaceOdds34)

    spinyCapsuleShopOdds12 = str(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = str(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = str(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = str(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = str(spinyCapsuleSpaceOdds34)

    podobooCapsuleShopOdds12 = str(podobooCapsuleShopOdds12)
    podobooCapsuleShopOdds34 = str(podobooCapsuleShopOdds34)
    podobooCapsuleSpaceOdds1 = str(podobooCapsuleSpaceOdds1)
    podobooCapsuleSpaceOdds2 = str(podobooCapsuleSpaceOdds2)
    podobooCapsuleSpaceOdds34 = str(podobooCapsuleSpaceOdds34)

    tweesterCapsuleShopOdds12 = str(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = str(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = str(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = str(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = str(tweesterCapsuleSpaceOdds34)

    thwompCapsuleShopOdds12 = str(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = str(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = str(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = str(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = str(thwompCapsuleSpaceOdds34)

    warpCapsuleShopOdds12 = str(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = str(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = str(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = str(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = str(warpCapsuleSpaceOdds34)

    bombCapsuleShopOdds12 = str(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = str(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = str(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = str(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = str(bombCapsuleSpaceOdds34)

    fireballCapsuleShopOdds12 = str(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = str(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = str(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = str(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = str(fireballCapsuleSpaceOdds34)

    paraTroopaCapsuleShopOdds12 = str(paraTroopaCapsuleShopOdds12)
    paraTroopaCapsuleShopOdds34 = str(paraTroopaCapsuleShopOdds34)
    paraTroopaCapsuleSpaceOdds1 = str(paraTroopaCapsuleSpaceOdds1)
    paraTroopaCapsuleSpaceOdds2 = str(paraTroopaCapsuleSpaceOdds2)
    paraTroopaCapsuleSpaceOdds34 = str(paraTroopaCapsuleSpaceOdds34)

    eggCapsuleShopOdds12 = str(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = str(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = str(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = str(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = str(eggCapsuleSpaceOdds34)

    vacuumCapsuleShopOdds12 = str(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = str(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = str(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = str(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = str(vacuumCapsuleSpaceOdds34)

    magicCapsuleShopOdds12 = str(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = str(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = str(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = str(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = str(magicCapsuleSpaceOdds34)

    tripleCapsuleShopOdds12 = str(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = str(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = str(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = str(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = str(tripleCapsuleSpaceOdds34)

    koopaCapsuleShopOdds12 = str(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = str(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = str(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = str(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = str(koopaCapsuleSpaceOdds34)

    cursedMushroomShopOdds12 = str(cursedMushroomShopOdds12)
    cursedMushroomShopOdds34 = str(cursedMushroomShopOdds34)
    cursedMushroomSpaceOdds1 = str(cursedMushroomSpaceOdds1)
    cursedMushroomSpaceOdds2 = str(cursedMushroomSpaceOdds2)
    cursedMushroomSpaceOdds34 = str(cursedMushroomSpaceOdds34)

    orbBagCapsuleShopOdds12 = str(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = str(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = str(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = str(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = str(orbBagCapsuleSpaceOdds34)

    mysteryCapsuleShopOdds12 = str(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = str(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = str(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = str(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = str(mysteryCapsuleSpaceOdds34)

    dkCapsuleShopOdds12 = str(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = str(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = str(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = str(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = str(dkCapsuleSpaceOdds34)

    duelCapsuleShopOdds12 = str(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = str(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = str(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = str(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = str(duelCapsuleSpaceOdds34)

    def convert_to_hex_weight(weight):
        try:
            weight_hex = hex(int(weight))
            if len(weight_hex) == 4:
                return weight_hex[2:]  # Remove '0x' prefix
            elif len(weight_hex) == 3:
                return "0" + weight_hex[2:]  # Add leading zero
            return weight_hex[2:]  # Return as is for other lengths
        except:
            return "00"  # Return default value on error

    # Usage
    mushroomCapsuleShopOdds12 = convert_to_hex_weight(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = convert_to_hex_weight(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = convert_to_hex_weight(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = convert_to_hex_weight(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = convert_to_hex_weight(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsulePrice1 = convert_to_hex_weight(goldenMushroomCapsulePrice1)
    goldenMushroomCapsulePrice2 = convert_to_hex_weight(goldenMushroomCapsulePrice2)
    goldenMushroomCapsulePrice34 = convert_to_hex_weight(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds34)

    slowMushroomCapsulePrice1 = convert_to_hex_weight(slowMushroomCapsulePrice1)
    slowMushroomCapsulePrice2 = convert_to_hex_weight(slowMushroomCapsulePrice2)
    slowMushroomCapsulePrice34 = convert_to_hex_weight(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = convert_to_hex_weight(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = convert_to_hex_weight(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsulePrice1 = convert_to_hex_weight(metalMushroomCapsulePrice1)
    metalMushroomCapsulePrice2 = convert_to_hex_weight(metalMushroomCapsulePrice2)
    metalMushroomCapsulePrice34 = convert_to_hex_weight(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = convert_to_hex_weight(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = convert_to_hex_weight(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds34)

    flutterCapsulePrice1 = convert_to_hex_weight(flutterCapsulePrice1)
    flutterCapsulePrice2 = convert_to_hex_weight(flutterCapsulePrice2)
    flutterCapsulePrice34 = convert_to_hex_weight(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = convert_to_hex_weight(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = convert_to_hex_weight(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = convert_to_hex_weight(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = convert_to_hex_weight(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = convert_to_hex_weight(flutterCapsuleSpaceOdds34)

    cannonCapsulePrice1 = convert_to_hex_weight(cannonCapsulePrice1)
    cannonCapsulePrice2 = convert_to_hex_weight(cannonCapsulePrice2)
    cannonCapsulePrice34 = convert_to_hex_weight(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = convert_to_hex_weight(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = convert_to_hex_weight(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = convert_to_hex_weight(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = convert_to_hex_weight(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = convert_to_hex_weight(cannonCapsuleSpaceOdds34)

    snackCapsulePrice1 = convert_to_hex_weight(snackCapsulePrice1)
    snackCapsulePrice2 = convert_to_hex_weight(snackCapsulePrice2)
    snackCapsulePrice34 = convert_to_hex_weight(snackCapsulePrice34)
    snackCapsuleShopOdds12 = convert_to_hex_weight(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = convert_to_hex_weight(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = convert_to_hex_weight(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = convert_to_hex_weight(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = convert_to_hex_weight(snackCapsuleSpaceOdds34)

    goombaCapsulePrice1 = convert_to_hex_weight(goombaCapsulePrice1)
    goombaCapsulePrice2 = convert_to_hex_weight(goombaCapsulePrice2)
    goombaCapsulePrice34 = convert_to_hex_weight(goombaCapsulePrice34)
    goombaCapsuleShopOdds12 = convert_to_hex_weight(goombaCapsuleShopOdds12)
    goombaCapsuleShopOdds34 = convert_to_hex_weight(goombaCapsuleShopOdds34)
    goombaCapsuleSpaceOdds1 = convert_to_hex_weight(goombaCapsuleSpaceOdds1)
    goombaCapsuleSpaceOdds2 = convert_to_hex_weight(goombaCapsuleSpaceOdds2)
    goombaCapsuleSpaceOdds34 = convert_to_hex_weight(goombaCapsuleSpaceOdds34)

    hammerBroCapsulePrice1 = convert_to_hex_weight(hammerBroCapsulePrice1)
    hammerBroCapsulePrice2 = convert_to_hex_weight(hammerBroCapsulePrice2)
    hammerBroCapsulePrice34 = convert_to_hex_weight(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = convert_to_hex_weight(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = convert_to_hex_weight(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsulePrice1 = convert_to_hex_weight(piranhaPlantCapsulePrice1)
    piranhaPlantCapsulePrice2 = convert_to_hex_weight(piranhaPlantCapsulePrice2)
    piranhaPlantCapsulePrice34 = convert_to_hex_weight(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds34)

    kleptoCapsulePrice1 = convert_to_hex_weight(kleptoCapsulePrice1)
    kleptoCapsulePrice2 = convert_to_hex_weight(kleptoCapsulePrice2)
    kleptoCapsulePrice34 = convert_to_hex_weight(kleptoCapsulePrice34)
    kleptoCapsuleShopOdds12 = convert_to_hex_weight(kleptoCapsuleShopOdds12)
    kleptoCapsuleShopOdds34 = convert_to_hex_weight(kleptoCapsuleShopOdds34)
    kleptoCapsuleSpaceOdds1 = convert_to_hex_weight(kleptoCapsuleSpaceOdds1)
    kleptoCapsuleSpaceOdds2 = convert_to_hex_weight(kleptoCapsuleSpaceOdds2)
    kleptoCapsuleSpaceOdds34 = convert_to_hex_weight(kleptoCapsuleSpaceOdds34)

    kamekCapsulePrice1 = convert_to_hex_weight(kamekCapsulePrice1)
    kamekCapsulePrice2 = convert_to_hex_weight(kamekCapsulePrice2)
    kamekCapsulePrice34 = convert_to_hex_weight(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = convert_to_hex_weight(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = convert_to_hex_weight(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = convert_to_hex_weight(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = convert_to_hex_weight(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = convert_to_hex_weight(kamekCapsuleSpaceOdds34)

    toadyCapsulePrice1 = convert_to_hex_weight(toadyCapsulePrice1)
    toadyCapsulePrice2 = convert_to_hex_weight(toadyCapsulePrice2)
    toadyCapsulePrice34 = convert_to_hex_weight(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = convert_to_hex_weight(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = convert_to_hex_weight(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = convert_to_hex_weight(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = convert_to_hex_weight(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = convert_to_hex_weight(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsulePrice1 = convert_to_hex_weight(mrBlizzardCapsulePrice1)
    mrBlizzardCapsulePrice2 = convert_to_hex_weight(mrBlizzardCapsulePrice2)
    mrBlizzardCapsulePrice34 = convert_to_hex_weight(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds34)

    banditCapsulePrice1 = convert_to_hex_weight(banditCapsulePrice1)
    banditCapsulePrice2 = convert_to_hex_weight(banditCapsulePrice2)
    banditCapsulePrice34 = convert_to_hex_weight(banditCapsulePrice34)
    banditCapsuleShopOdds12 = convert_to_hex_weight(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = convert_to_hex_weight(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = convert_to_hex_weight(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = convert_to_hex_weight(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = convert_to_hex_weight(banditCapsuleSpaceOdds34)

    pinkBooCapsulePrice1 = convert_to_hex_weight(pinkBooCapsulePrice1)
    pinkBooCapsulePrice2 = convert_to_hex_weight(pinkBooCapsulePrice2)
    pinkBooCapsulePrice34 = convert_to_hex_weight(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = convert_to_hex_weight(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = convert_to_hex_weight(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds34)

    spinyCapsulePrice1 = convert_to_hex_weight(spinyCapsulePrice1)
    spinyCapsulePrice2 = convert_to_hex_weight(spinyCapsulePrice2)
    spinyCapsulePrice34 = convert_to_hex_weight(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = convert_to_hex_weight(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = convert_to_hex_weight(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = convert_to_hex_weight(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = convert_to_hex_weight(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = convert_to_hex_weight(spinyCapsuleSpaceOdds34)

    podobooCapsulePrice1 = convert_to_hex_weight(podobooCapsulePrice1)
    podobooCapsulePrice2 = convert_to_hex_weight(podobooCapsulePrice2)
    podobooCapsulePrice34 = convert_to_hex_weight(podobooCapsulePrice34)
    podobooCapsuleShopOdds12 = convert_to_hex_weight(podobooCapsuleShopOdds12)
    podobooCapsuleShopOdds34 = convert_to_hex_weight(podobooCapsuleShopOdds34)
    podobooCapsuleSpaceOdds1 = convert_to_hex_weight(podobooCapsuleSpaceOdds1)
    podobooCapsuleSpaceOdds2 = convert_to_hex_weight(podobooCapsuleSpaceOdds2)
    podobooCapsuleSpaceOdds34 = convert_to_hex_weight(podobooCapsuleSpaceOdds34)

    tweesterCapsulePrice1 = convert_to_hex_weight(tweesterCapsulePrice1)
    tweesterCapsulePrice2 = convert_to_hex_weight(tweesterCapsulePrice2)
    tweesterCapsulePrice34 = convert_to_hex_weight(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = convert_to_hex_weight(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = convert_to_hex_weight(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = convert_to_hex_weight(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = convert_to_hex_weight(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = convert_to_hex_weight(tweesterCapsuleSpaceOdds34)

    thwompCapsulePrice1 = convert_to_hex_weight(thwompCapsulePrice1)
    thwompCapsulePrice2 = convert_to_hex_weight(thwompCapsulePrice2)
    thwompCapsulePrice34 = convert_to_hex_weight(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = convert_to_hex_weight(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = convert_to_hex_weight(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = convert_to_hex_weight(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = convert_to_hex_weight(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = convert_to_hex_weight(thwompCapsuleSpaceOdds34)

    warpCapsulePrice1 = convert_to_hex_weight(warpCapsulePrice1)
    warpCapsulePrice2 = convert_to_hex_weight(warpCapsulePrice2)
    warpCapsulePrice34 = convert_to_hex_weight(warpCapsulePrice34)
    warpCapsuleShopOdds12 = convert_to_hex_weight(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = convert_to_hex_weight(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = convert_to_hex_weight(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = convert_to_hex_weight(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = convert_to_hex_weight(warpCapsuleSpaceOdds34)

    bombCapsulePrice1 = convert_to_hex_weight(bombCapsulePrice1)
    bombCapsulePrice2 = convert_to_hex_weight(bombCapsulePrice2)
    bombCapsulePrice34 = convert_to_hex_weight(bombCapsulePrice34)
    bombCapsuleShopOdds12 = convert_to_hex_weight(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = convert_to_hex_weight(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = convert_to_hex_weight(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = convert_to_hex_weight(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = convert_to_hex_weight(bombCapsuleSpaceOdds34)

    fireballCapsulePrice1 = convert_to_hex_weight(fireballCapsulePrice1)
    fireballCapsulePrice2 = convert_to_hex_weight(fireballCapsulePrice2)
    fireballCapsulePrice34 = convert_to_hex_weight(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = convert_to_hex_weight(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = convert_to_hex_weight(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = convert_to_hex_weight(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = convert_to_hex_weight(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = convert_to_hex_weight(fireballCapsuleSpaceOdds34)

    paraTroopaCapsulePrice1 = convert_to_hex_weight(paraTroopaCapsulePrice1)
    paraTroopaCapsulePrice2 = convert_to_hex_weight(paraTroopaCapsulePrice2)
    paraTroopaCapsulePrice34 = convert_to_hex_weight(paraTroopaCapsulePrice34)
    paraTroopaCapsuleShopOdds12 = convert_to_hex_weight(paraTroopaCapsuleShopOdds12)
    paraTroopaCapsuleShopOdds34 = convert_to_hex_weight(paraTroopaCapsuleShopOdds34)
    paraTroopaCapsuleSpaceOdds1 = convert_to_hex_weight(paraTroopaCapsuleSpaceOdds1)
    paraTroopaCapsuleSpaceOdds2 = convert_to_hex_weight(paraTroopaCapsuleSpaceOdds2)
    paraTroopaCapsuleSpaceOdds34 = convert_to_hex_weight(paraTroopaCapsuleSpaceOdds34)

    eggCapsulePrice1 = convert_to_hex_weight(eggCapsulePrice1)
    eggCapsulePrice2 = convert_to_hex_weight(eggCapsulePrice2)
    eggCapsulePrice34 = convert_to_hex_weight(eggCapsulePrice34)
    eggCapsuleShopOdds12 = convert_to_hex_weight(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = convert_to_hex_weight(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = convert_to_hex_weight(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = convert_to_hex_weight(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = convert_to_hex_weight(eggCapsuleSpaceOdds34)

    vacuumCapsulePrice1 = convert_to_hex_weight(vacuumCapsulePrice1)
    vacuumCapsulePrice2 = convert_to_hex_weight(vacuumCapsulePrice2)
    vacuumCapsulePrice34 = convert_to_hex_weight(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = convert_to_hex_weight(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = convert_to_hex_weight(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = convert_to_hex_weight(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = convert_to_hex_weight(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = convert_to_hex_weight(vacuumCapsuleSpaceOdds34)

    magicCapsulePrice1 = convert_to_hex_weight(magicCapsulePrice1)
    magicCapsulePrice2 = convert_to_hex_weight(magicCapsulePrice2)
    magicCapsulePrice34 = convert_to_hex_weight(magicCapsulePrice34)
    magicCapsuleShopOdds12 = convert_to_hex_weight(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = convert_to_hex_weight(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = convert_to_hex_weight(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = convert_to_hex_weight(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = convert_to_hex_weight(magicCapsuleSpaceOdds34)

    tripleCapsulePrice1 = convert_to_hex_weight(tripleCapsulePrice1)
    tripleCapsulePrice2 = convert_to_hex_weight(tripleCapsulePrice2)
    tripleCapsulePrice34 = convert_to_hex_weight(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = convert_to_hex_weight(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = convert_to_hex_weight(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = convert_to_hex_weight(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = convert_to_hex_weight(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = convert_to_hex_weight(tripleCapsuleSpaceOdds34)

    koopaCapsulePrice1 = convert_to_hex_weight(koopaCapsulePrice1)
    koopaCapsulePrice2 = convert_to_hex_weight(koopaCapsulePrice2)
    koopaCapsulePrice34 = convert_to_hex_weight(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = convert_to_hex_weight(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = convert_to_hex_weight(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = convert_to_hex_weight(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = convert_to_hex_weight(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = convert_to_hex_weight(koopaCapsuleSpaceOdds34)

    cursedMushroomPrice1 = convert_to_hex_weight(cursedMushroomPrice1)
    cursedMushroomPrice2 = convert_to_hex_weight(cursedMushroomPrice2)
    cursedMushroomPrice34 = convert_to_hex_weight(cursedMushroomPrice34)
    cursedMushroomShopOdds12 = convert_to_hex_weight(cursedMushroomShopOdds12)
    cursedMushroomShopOdds34 = convert_to_hex_weight(cursedMushroomShopOdds34)
    cursedMushroomSpaceOdds1 = convert_to_hex_weight(cursedMushroomSpaceOdds1)
    cursedMushroomSpaceOdds2 = convert_to_hex_weight(cursedMushroomSpaceOdds2)
    cursedMushroomSpaceOdds34 = convert_to_hex_weight(cursedMushroomSpaceOdds34)

    orbBagCapsulePrice1 = convert_to_hex_weight(orbBagCapsulePrice1)
    orbBagCapsulePrice2 = convert_to_hex_weight(orbBagCapsulePrice2)
    orbBagCapsulePrice34 = convert_to_hex_weight(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = convert_to_hex_weight(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = convert_to_hex_weight(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = convert_to_hex_weight(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = convert_to_hex_weight(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = convert_to_hex_weight(orbBagCapsuleSpaceOdds34)

    mysteryCapsulePrice1 = convert_to_hex_weight(mysteryCapsulePrice1)
    mysteryCapsulePrice2 = convert_to_hex_weight(mysteryCapsulePrice2)
    mysteryCapsulePrice34 = convert_to_hex_weight(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = convert_to_hex_weight(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = convert_to_hex_weight(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = convert_to_hex_weight(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = convert_to_hex_weight(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = convert_to_hex_weight(mysteryCapsuleSpaceOdds34)

    dkCapsulePrice1 = convert_to_hex_weight(dkCapsulePrice1)
    dkCapsulePrice2 = convert_to_hex_weight(dkCapsulePrice2)
    dkCapsulePrice34 = convert_to_hex_weight(dkCapsulePrice34)
    dkCapsuleShopOdds12 = convert_to_hex_weight(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = convert_to_hex_weight(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = convert_to_hex_weight(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = convert_to_hex_weight(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = convert_to_hex_weight(dkCapsuleSpaceOdds34)

    duelCapsulePrice1 = convert_to_hex_weight(duelCapsulePrice1)
    duelCapsulePrice2 = convert_to_hex_weight(duelCapsulePrice2)
    duelCapsulePrice34 = convert_to_hex_weight(duelCapsulePrice34)
    duelCapsuleShopOdds12 = convert_to_hex_weight(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = convert_to_hex_weight(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = convert_to_hex_weight(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = convert_to_hex_weight(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = convert_to_hex_weight(duelCapsuleSpaceOdds34)

    # Map MP7 style parameters to MP6 style
    mushroomSpaceOdds1 = mushroomCapsuleSpaceOdds1
    mushroomSpaceOdds2 = mushroomCapsuleSpaceOdds2
    mushroomSpaceOdds3 = mushroomCapsuleSpaceOdds34
    mushroomSpaceOdds4 = mushroomCapsuleSpaceOdds34
    mushroomShopOdds123 = mushroomCapsuleShopOdds12
    mushroomShopOdds4 = mushroomCapsuleShopOdds34

    goldenMushroomPrice1 = goldenMushroomCapsulePrice1
    goldenMushroomPrice2 = goldenMushroomCapsulePrice2
    goldenMushroomPrice34 = goldenMushroomCapsulePrice34
    goldenMushroomSpaceOdds1 = goldenMushroomCapsuleSpaceOdds1
    goldenMushroomSpaceOdds2 = goldenMushroomCapsuleSpaceOdds2
    goldenMushroomSpaceOdds3 = goldenMushroomCapsuleSpaceOdds34
    goldenMushroomSpaceOdds4 = goldenMushroomCapsuleSpaceOdds34
    goldenMushroomShopOdds123 = goldenMushroomCapsuleShopOdds12
    goldenMushroomShopOdds4 = goldenMushroomCapsuleShopOdds34

    slowMushroomPrice1 = slowMushroomCapsulePrice1
    slowMushroomPrice2 = slowMushroomCapsulePrice2
    slowMushroomPrice34 = slowMushroomCapsulePrice34
    slowMushroomSpaceOdds1 = slowMushroomCapsuleSpaceOdds1
    slowMushroomSpaceOdds2 = slowMushroomCapsuleSpaceOdds2
    slowMushroomSpaceOdds3 = slowMushroomCapsuleSpaceOdds34
    slowMushroomSpaceOdds4 = slowMushroomCapsuleSpaceOdds34
    slowMushroomShopOdds123 = slowMushroomCapsuleShopOdds12
    slowMushroomShopOdds4 = slowMushroomCapsuleShopOdds34

    metalMushroomPrice1 = metalMushroomCapsulePrice1
    metalMushroomPrice2 = metalMushroomCapsulePrice2
    metalMushroomPrice34 = metalMushroomCapsulePrice34
    metalMushroomSpaceOdds1 = metalMushroomCapsuleSpaceOdds1
    metalMushroomSpaceOdds2 = metalMushroomCapsuleSpaceOdds2
    metalMushroomSpaceOdds3 = metalMushroomCapsuleSpaceOdds34
    metalMushroomSpaceOdds4 = metalMushroomCapsuleSpaceOdds34
    metalMushroomShopOdds123 = metalMushroomCapsuleShopOdds12
    metalMushroomShopOdds4 = metalMushroomCapsuleShopOdds34

    bulletBillPrice1 = cannonCapsulePrice1
    bulletBillPrice2 = cannonCapsulePrice2
    bulletBillPrice34 = cannonCapsulePrice34
    bulletBillSpaceOdds1 = cannonCapsuleSpaceOdds1
    bulletBillSpaceOdds2 = cannonCapsuleSpaceOdds2
    bulletBillSpaceOdds3 = cannonCapsuleSpaceOdds34
    bulletBillSpaceOdds4 = cannonCapsuleSpaceOdds34
    bulletBillShopOdds123 = cannonCapsuleShopOdds12
    bulletBillShopOdds4 = cannonCapsuleShopOdds34

    flutterPrice1 = flutterCapsulePrice1
    flutterPrice2 = flutterCapsulePrice2
    flutterPrice34 = flutterCapsulePrice34
    flutterSpaceOdds1 = flutterCapsuleSpaceOdds1
    flutterSpaceOdds2 = flutterCapsuleSpaceOdds2
    flutterSpaceOdds3 = flutterCapsuleSpaceOdds34
    flutterSpaceOdds4 = flutterCapsuleSpaceOdds34
    flutterShopOdds123 = flutterCapsuleShopOdds12
    flutterShopOdds4 = flutterCapsuleShopOdds34

    cursedMushroomPrice1 = cursedMushroomPrice1
    cursedMushroomPrice2 = cursedMushroomPrice2
    cursedMushroomPrice34 = cursedMushroomPrice34
    cursedMushroomSpaceOdds1 = cursedMushroomSpaceOdds1
    cursedMushroomSpaceOdds2 = cursedMushroomSpaceOdds2
    cursedMushroomSpaceOdds3 = cursedMushroomSpaceOdds34
    cursedMushroomSpaceOdds4 = cursedMushroomSpaceOdds34
    cursedMushroomShopOdds123 = cursedMushroomShopOdds12
    cursedMushroomShopOdds4 = cursedMushroomShopOdds34

    spinyPrice1 = spinyCapsulePrice1
    spinyPrice2 = spinyCapsulePrice2
    spinyPrice34 = spinyCapsulePrice34
    spinySpaceOdds1 = spinyCapsuleSpaceOdds1
    spinySpaceOdds2 = spinyCapsuleSpaceOdds2
    spinySpaceOdds3 = spinyCapsuleSpaceOdds34
    spinySpaceOdds4 = spinyCapsuleSpaceOdds34
    spinyShopOdds123 = spinyCapsuleShopOdds12
    spinyShopOdds4 = spinyCapsuleShopOdds34

    goombaCapsulePrice1 = goombaCapsulePrice1
    goombaCapsulePrice2 = goombaCapsulePrice2
    goombaCapsulePrice34 = goombaCapsulePrice34
    goombaCapsuleSpaceOdds1 = goombaCapsuleSpaceOdds1
    goombaCapsuleSpaceOdds2 = goombaCapsuleSpaceOdds2
    goombaCapsuleSpaceOdds3 = goombaCapsuleSpaceOdds34
    goombaCapsuleSpaceOdds4 = goombaCapsuleSpaceOdds34
    goombaCapsuleShopOdds123 = goombaCapsuleShopOdds12
    goombaCapsuleShopOdds4 = goombaCapsuleShopOdds34

    plantPrice1 = piranhaPlantCapsulePrice1
    plantPrice2 = piranhaPlantCapsulePrice2
    plantPrice34 = piranhaPlantCapsulePrice34
    plantSpaceOdds1 = piranhaPlantCapsuleSpaceOdds1
    plantSpaceOdds2 = piranhaPlantCapsuleSpaceOdds2
    plantSpaceOdds3 = piranhaPlantCapsuleSpaceOdds34
    plantSpaceOdds4 = piranhaPlantCapsuleSpaceOdds34
    plantShopOdds123 = piranhaPlantCapsuleShopOdds12
    plantShopOdds4 = piranhaPlantCapsuleShopOdds34

    kleptoCapsulePrice1 = kleptoCapsulePrice1
    kleptoCapsulePrice2 = kleptoCapsulePrice2
    kleptoCapsulePrice34 = kleptoCapsulePrice34
    kleptoCapsuleSpaceOdds1 = kleptoCapsuleSpaceOdds1
    kleptoCapsuleSpaceOdds2 = kleptoCapsuleSpaceOdds2
    kleptoCapsuleSpaceOdds3 = kleptoCapsuleSpaceOdds34
    kleptoCapsuleSpaceOdds4 = kleptoCapsuleSpaceOdds34
    kleptoCapsuleShopOdds123 = kleptoCapsuleShopOdds12
    kleptoCapsuleShopOdds4 = kleptoCapsuleShopOdds34

    toadyPrice1 = toadyCapsulePrice1
    toadyPrice2 = toadyCapsulePrice2
    toadyPrice34 = toadyCapsulePrice34
    toadySpaceOdds1 = toadyCapsuleSpaceOdds1
    toadySpaceOdds2 = toadyCapsuleSpaceOdds2
    toadySpaceOdds3 = toadyCapsuleSpaceOdds34
    toadySpaceOdds4 = toadyCapsuleSpaceOdds34
    toadyShopOdds123 = toadyCapsuleShopOdds12
    toadyShopOdds4 = toadyCapsuleShopOdds34

    kamekPrice1 = kamekCapsulePrice1
    kamekPrice2 = kamekCapsulePrice2
    kamekPrice34 = kamekCapsulePrice34
    kamekSpaceOdds1 = kamekCapsuleSpaceOdds1
    kamekSpaceOdds2 = kamekCapsuleSpaceOdds2
    kamekSpaceOdds3 = kamekCapsuleSpaceOdds34
    kamekSpaceOdds4 = kamekCapsuleSpaceOdds34
    kamekShopOdds123 = kamekCapsuleShopOdds12
    kamekShopOdds4 = kamekCapsuleShopOdds34

    blizzardPrice1 = mrBlizzardCapsulePrice1
    blizzardPrice2 = mrBlizzardCapsulePrice2
    blizzardPrice34 = mrBlizzardCapsulePrice34
    blizzardSpaceOdds1 = mrBlizzardCapsuleSpaceOdds1
    blizzardSpaceOdds2 = mrBlizzardCapsuleSpaceOdds2
    blizzardSpaceOdds3 = mrBlizzardCapsuleSpaceOdds34
    blizzardSpaceOdds4 = mrBlizzardCapsuleSpaceOdds34
    blizzardShopOdds123 = mrBlizzardCapsuleShopOdds12
    blizzardShopOdds4 = mrBlizzardCapsuleShopOdds34

    podobooCapsulePrice1 = podobooCapsulePrice1
    podobooCapsulePrice2 = podobooCapsulePrice2
    podobooCapsulePrice34 = podobooCapsulePrice34
    podobooCapsuleSpaceOdds1 = podobooCapsuleSpaceOdds1
    podobooCapsuleSpaceOdds2 = podobooCapsuleSpaceOdds2
    podobooCapsuleSpaceOdds3 = podobooCapsuleSpaceOdds34
    podobooCapsuleSpaceOdds4 = podobooCapsuleSpaceOdds34
    podobooCapsuleShopOdds123 = podobooCapsuleShopOdds12
    podobooCapsuleShopOdds4 = podobooCapsuleShopOdds34

    zapPrice1 = banditCapsulePrice1
    zapPrice2 = banditCapsulePrice2
    zapPrice34 = banditCapsulePrice34
    zapSpaceOdds1 = banditCapsuleSpaceOdds1
    zapSpaceOdds2 = banditCapsuleSpaceOdds2
    zapSpaceOdds3 = banditCapsuleSpaceOdds34
    zapSpaceOdds4 = banditCapsuleSpaceOdds34
    zapShopOdds123 = banditCapsuleShopOdds12
    zapShopOdds4 = banditCapsuleShopOdds34

    tweesterPrice1 = thwompCapsulePrice1
    tweesterPrice2 = thwompCapsulePrice2
    tweesterPrice34 = thwompCapsulePrice34
    tweesterSpaceOdds1 = thwompCapsuleSpaceOdds1
    tweesterSpaceOdds2 = thwompCapsuleSpaceOdds2
    tweesterSpaceOdds3 = thwompCapsuleSpaceOdds34
    tweesterSpaceOdds4 = thwompCapsuleSpaceOdds34
    tweesterShopOdds123 = thwompCapsuleShopOdds12
    tweesterShopOdds4 = thwompCapsuleShopOdds34

    thwompPrice1 = warpCapsulePrice1
    thwompPrice2 = warpCapsulePrice2
    thwompPrice34 = warpCapsulePrice34
    thwompSpaceOdds1 = warpCapsuleSpaceOdds1
    thwompSpaceOdds2 = warpCapsuleSpaceOdds2
    thwompSpaceOdds3 = warpCapsuleSpaceOdds34
    thwompSpaceOdds4 = warpCapsuleSpaceOdds34
    thwompShopOdds123 = warpCapsuleShopOdds12
    thwompShopOdds4 = warpCapsuleShopOdds34

    warpPipePrice1 = bombCapsulePrice1
    warpPipePrice2 = bombCapsulePrice2
    warpPipePrice34 = bombCapsulePrice34
    warpPipeSpaceOdds1 = bombCapsuleSpaceOdds1
    warpPipeSpaceOdds2 = bombCapsuleSpaceOdds2
    warpPipeSpaceOdds3 = bombCapsuleSpaceOdds34
    warpPipeSpaceOdds4 = bombCapsuleSpaceOdds34
    warpPipeShopOdds123 = bombCapsuleShopOdds12
    warpPipeShopOdds4 = bombCapsuleShopOdds34

    bombPrice1 = fireballCapsulePrice1
    bombPrice2 = fireballCapsulePrice2
    bombPrice34 = fireballCapsulePrice34
    bombSpaceOdds1 = fireballCapsuleSpaceOdds1
    bombSpaceOdds2 = fireballCapsuleSpaceOdds2
    bombSpaceOdds3 = fireballCapsuleSpaceOdds34
    bombSpaceOdds4 = fireballCapsuleSpaceOdds34
    bombShopOdds123 = fireballCapsuleShopOdds12
    bombShopOdds4 = fireballCapsuleShopOdds34

    paraTroopaCapsulePrice1 = paraTroopaCapsulePrice1
    paraTroopaCapsulePrice2 = paraTroopaCapsulePrice2
    paraTroopaCapsulePrice34 = paraTroopaCapsulePrice34
    paraTroopaCapsuleSpaceOdds1 = paraTroopaCapsuleSpaceOdds1
    paraTroopaCapsuleSpaceOdds2 = paraTroopaCapsuleSpaceOdds2
    paraTroopaCapsuleSpaceOdds3 = paraTroopaCapsuleSpaceOdds34
    paraTroopaCapsuleSpaceOdds4 = paraTroopaCapsuleSpaceOdds34
    paraTroopaCapsuleShopOdds123 = paraTroopaCapsuleShopOdds12
    paraTroopaCapsuleShopOdds4 = paraTroopaCapsuleShopOdds34

    snackPrice1 = eggCapsulePrice1
    snackPrice2 = eggCapsulePrice2
    snackPrice34 = eggCapsulePrice34
    snackSpaceOdds1 = eggCapsuleSpaceOdds1
    snackSpaceOdds2 = eggCapsuleSpaceOdds2
    snackSpaceOdds3 = eggCapsuleSpaceOdds34
    snackSpaceOdds4 = eggCapsuleSpaceOdds34
    snackShopOdds123 = eggCapsuleShopOdds12
    snackShopOdds4 = eggCapsuleShopOdds34

    gaddLightPrice1 = vacuumCapsulePrice1
    gaddLightPrice2 = vacuumCapsulePrice2
    gaddLightPrice34 = vacuumCapsulePrice34
    gaddLightSpaceOdds1 = vacuumCapsuleSpaceOdds1
    gaddLightSpaceOdds2 = vacuumCapsuleSpaceOdds2
    gaddLightSpaceOdds3 = vacuumCapsuleSpaceOdds34
    gaddLightSpaceOdds4 = vacuumCapsuleSpaceOdds34
    gaddLightShopOdds123 = vacuumCapsuleShopOdds12
    gaddLightShopOdds4 = vacuumCapsuleShopOdds34

    generatedCode = getOrbModsSix(mushroomSpaceOdds1, mushroomSpaceOdds2, mushroomSpaceOdds3, mushroomSpaceOdds4, mushroomShopOdds123, mushroomShopOdds4, goldenMushroomPrice1, goldenMushroomPrice2, goldenMushroomPrice34, goldenMushroomSpaceOdds1, goldenMushroomSpaceOdds2, goldenMushroomSpaceOdds3, goldenMushroomSpaceOdds4, goldenMushroomShopOdds123, goldenMushroomShopOdds4, slowMushroomPrice1, slowMushroomPrice2, slowMushroomPrice34, slowMushroomSpaceOdds1, slowMushroomSpaceOdds2, slowMushroomSpaceOdds3, slowMushroomSpaceOdds4, slowMushroomShopOdds123, slowMushroomShopOdds4, metalMushroomPrice1, metalMushroomPrice2, metalMushroomPrice34, metalMushroomSpaceOdds1, metalMushroomSpaceOdds2, metalMushroomSpaceOdds3, metalMushroomSpaceOdds4, metalMushroomShopOdds123, metalMushroomShopOdds4, bulletBillPrice1, bulletBillPrice2, bulletBillPrice34, bulletBillSpaceOdds1, bulletBillSpaceOdds2, bulletBillSpaceOdds3, bulletBillSpaceOdds4, bulletBillShopOdds123, bulletBillShopOdds4, flutterPrice1, flutterPrice2, flutterPrice34, flutterSpaceOdds1, flutterSpaceOdds2, flutterSpaceOdds3, flutterSpaceOdds4, flutterShopOdds123, flutterShopOdds4, cursedMushroomPrice1, cursedMushroomPrice2, cursedMushroomPrice34, cursedMushroomSpaceOdds1, cursedMushroomSpaceOdds2, cursedMushroomSpaceOdds3, cursedMushroomSpaceOdds4, cursedMushroomShopOdds123, cursedMushroomShopOdds4, spinyPrice1, spinyPrice2, spinyPrice34, spinySpaceOdds1, spinySpaceOdds2, spinySpaceOdds3, spinySpaceOdds4, spinyShopOdds123, spinyShopOdds4, goombaCapsulePrice1, goombaCapsulePrice2, goombaCapsulePrice34, goombaCapsuleSpaceOdds1, goombaCapsuleSpaceOdds2, goombaCapsuleSpaceOdds3, goombaCapsuleSpaceOdds4, goombaCapsuleShopOdds123, goombaCapsuleShopOdds4, plantPrice1, plantPrice2, plantPrice34, plantSpaceOdds1, plantSpaceOdds2, plantSpaceOdds3, plantSpaceOdds4, plantShopOdds123, plantShopOdds4, kleptoCapsulePrice1, kleptoCapsulePrice2, kleptoCapsulePrice34, kleptoCapsuleSpaceOdds1, kleptoCapsuleSpaceOdds2, kleptoCapsuleSpaceOdds3, kleptoCapsuleSpaceOdds4, kleptoCapsuleShopOdds123, kleptoCapsuleShopOdds4, toadyPrice1, toadyPrice2, toadyPrice34, toadySpaceOdds1, toadySpaceOdds2, toadySpaceOdds3, toadySpaceOdds4, toadyShopOdds123, toadyShopOdds4, kamekPrice1, kamekPrice2, kamekPrice34, kamekSpaceOdds1, kamekSpaceOdds2, kamekSpaceOdds3, kamekSpaceOdds4, kamekShopOdds123, kamekShopOdds4, blizzardPrice1, blizzardPrice2, blizzardPrice34, blizzardSpaceOdds1, blizzardSpaceOdds2, blizzardSpaceOdds3, blizzardSpaceOdds4, blizzardShopOdds123, blizzardShopOdds4, podobooCapsulePrice1, podobooCapsulePrice2, podobooCapsulePrice34, podobooCapsuleSpaceOdds1, podobooCapsuleSpaceOdds2, podobooCapsuleSpaceOdds3, podobooCapsuleSpaceOdds4, podobooCapsuleShopOdds123, podobooCapsuleShopOdds4, zapPrice1, zapPrice2, zapPrice34, zapSpaceOdds1, zapSpaceOdds2, zapSpaceOdds3, zapSpaceOdds4, zapShopOdds123, zapShopOdds4, tweesterPrice1, tweesterPrice2, tweesterPrice34, tweesterSpaceOdds1, tweesterSpaceOdds2, tweesterSpaceOdds3, tweesterSpaceOdds4, tweesterShopOdds123, tweesterShopOdds4, thwompPrice1, thwompPrice2, thwompPrice34, thwompSpaceOdds1, thwompSpaceOdds2, thwompSpaceOdds3, thwompSpaceOdds4, thwompShopOdds123, thwompShopOdds4, warpPipePrice1, warpPipePrice2, warpPipePrice34, warpPipeSpaceOdds1, warpPipeSpaceOdds2, warpPipeSpaceOdds3, warpPipeSpaceOdds4, warpPipeShopOdds123, warpPipeShopOdds4, bombPrice1, bombPrice2, bombPrice34, bombSpaceOdds1, bombSpaceOdds2, bombSpaceOdds3, bombSpaceOdds4, bombShopOdds123, bombShopOdds4, paraTroopaCapsulePrice1, paraTroopaCapsulePrice2, paraTroopaCapsulePrice34, paraTroopaCapsuleSpaceOdds1, paraTroopaCapsuleSpaceOdds2, paraTroopaCapsuleSpaceOdds3, paraTroopaCapsuleSpaceOdds4, paraTroopaCapsuleShopOdds123, paraTroopaCapsuleShopOdds4, snackPrice1, snackPrice2, snackPrice34, snackSpaceOdds1, snackSpaceOdds2, snackSpaceOdds3, snackSpaceOdds4, snackShopOdds123, snackShopOdds4, gaddLightPrice1, gaddLightPrice2, gaddLightPrice34, gaddLightSpaceOdds1, gaddLightSpaceOdds2, gaddLightSpaceOdds3, gaddLightSpaceOdds4, gaddLightShopOdds123, gaddLightShopOdds4)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)