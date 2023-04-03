import sys
import random
from typing import Tuple
from datetime import datetime

factions = ["The Arborec", "The Barony of Letnev", "The Clan of Saar", "The Embers of Muaat", "The Emirates of Hacan", "The Federation of Sol", "The Ghosts of Creuss", "The L1Z1X Mindnet", "The Mentak Coalition", "The Naalu Collective", "The Nekro Virus", 
"Sardakk N'orr", "The Universities of Jol-Nar", "The Winnu", "The Xxcha Kingdom", "The Yin Brotherhood", "The Yssaril Tribes", "The Argent Flight", "The Empyrean", "The Mahact Gene-Sorcerers", "The Naaz-Rokha Alliance", "The Nomad", "The Titans of Ul", 
"The Vuil'Raith Cabal", "The Council Keleres", ]



def get_players() -> list[str]:
    print("Please write the names of the players one by one and press enter. When you're done, press enter on an empty line.")
    players = []
    while True:
        name = input("The name for the next player: ")
        if name == "":
            break
        players.append(name)
    return players

def remove_random_faction(factions: list[str], player_count: int) -> Tuple[list[str], list[str]]:
    removed_factions = []
    for x in range(len(factions) - player_count*4):
        r = random.randint(0, len(factions)-1)
        removed_factions.append(factions.pop(r))
    return factions, removed_factions

def create_player_pools(factions: list[str], playerCount: int) -> list[list[str]]:
    playerPools = []
    for player in range(playerCount):
        playerPools.append([])
        for x in range(4):
            r = random.randint(0, len(factions)-1) if len(factions) > 1 else 0
            playerPools[player].append(factions.pop(r))
    return playerPools

def printOut():
    original_stdout = sys.stdout
    faction_amount_text = "Factions" if len(removed_factions) > 1 else "Faction"
    document_name = 'TI Draft ' + datetime.now().strftime("%Y-%m-%d" + ".txt")
    with open("Drafts/" + document_name, 'w+') as f:
        sys.stdout = f
        print("Preparation Phase\n")
        print(f"{faction_amount_text} removed from pool: {removed_factions}")
        i = 0
        for player in players:
            print(f"Factions for player {player}: {player_pools[i]}")
            i+=1
    sys.stdout = original_stdout
    with open("Drafts/"+document_name, 'r') as f:
        print(f.read())


players = get_players()
factions, removed_factions = remove_random_faction(factions, len(players))
player_pools = create_player_pools(factions, len(players))
printOut()