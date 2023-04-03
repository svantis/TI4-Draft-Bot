from datetime import datetime
import os

# get the game date
while True:
    game_date = input("Game day (YYYY-MM-DD): ")
    try:
        # try to parse the date to ensure it is valid
        game_date = datetime.strptime(game_date, "%Y-%m-%d")
        break
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

# format the file name
file_name = f"TI Draft {game_date.strftime('%Y-%m-%d')}.txt"

# check if the file exists, if not, prompt user to select an existing file
if not os.path.exists(f"./Drafts/{file_name}"):
    while True:
        file_name = input("The specified draft document does not exist. Please select an existing draft document: ")
        if os.path.exists(f"./Drafts/{file_name}"):
            break
        else:
            print("The selected file does not exist. Please try again.")

# get the player name
with open(f"./Drafts/{file_name}", "r+") as f:
    draft_text = f.read()
    draft_lines = draft_text.split("\n")
    while True:
        player_name = input("Player: ")
        players = []
        for line in draft_text.split("\n"):
            if "Factions for player" in line:
                player = line.split("Factions for player ")[1].split(":")[0]
                players.append(player)
        if player_name in players:
            break
        else:
            print("Invalid player name. Please enter a valid player name.")

    # get all factions and number of players
    all_factions = []
    for line in draft_text.split("\n"):
        if "Factions for player" in line:
            faction_list = [faction.strip("[]\"' ").replace("'", "") for faction in line.split(": ")[1].split(", ")]
            all_factions.extend(faction_list)
    all_factions = list(set(all_factions))

    # get the factions that were not picked or banned in the previous phases
    banned_factions = []
    picked_factions = []
    for line in draft_text.split("\n"):
        if "Faction banned by player" in line:
            banned_factions.append(line.split(": ")[1])
        elif "Faction added by player" in line:
            picked_factions.append(line.split(": ")[1])
        elif "Faction seconded by player" in line:
            picked_factions.append(line.split(": ")[1])
    remaining_factions = [f for f in all_factions if f not in banned_factions and f not in picked_factions]

    # get the chosen faction
    chosen_faction = ""
    while chosen_faction not in remaining_factions:
        chosen_faction = input(f"Remaining Faction Pool ({', '.join(remaining_factions)}): ")
        if chosen_faction not in remaining_factions:
            print("Invalid faction selected. Please select a faction from the remaining faction pool.")

# start the nomination phase
    
    phase_header = "Nomination Phase"
    if phase_header not in draft_text:
        draft_lines.append(f"\n{phase_header}\n")

    nominated_factions = []
    for i in range(len(draft_lines)):
        if "Faction nominated by player" in draft_lines[i]:
            nomination_faction = draft_lines[i].split(": ")[1]
            nominated_factions.append(nomination_faction)

    for i in range(len(draft_lines)):
        if "Faction nominated by player" in draft_lines[i]:
            nomination_player = draft_lines[i].split("Faction nominated by player ")[1].split(":")[0]
            nomination_faction = draft_lines[i].split(": ")[1]
            
            if nomination_player == player_name:
                if nomination_faction == chosen_faction:
                    break # Same player and faction, no change
                else:
                    if chosen_faction in nominated_factions:
                        draft_lines.append(f"Faction seconded by player {player_name}: {chosen_faction}")
                        picked_factions.append(chosen_faction)
                        draft_lines.pop(i)
                        nominated_factions.remove(chosen_faction)
                    else:
                        draft_lines[i] = f"Faction nominated by player {player_name}: {chosen_faction}"
                        break
            else:
                if nomination_faction == chosen_faction:
                    nominated_factions.remove(nomination_faction)
                    picked_factions.append(nomination_faction)
                    draft_lines.append(f"Faction seconded by player {player_name}: {chosen_faction} ")
                    break
        
        elif "Faction seconded by player" in draft_lines[i]:
            nomination_player = draft_lines[i].split("Faction seconded by player ")[1].split(":")[0]
            nomination_faction = draft_lines[i].split(": ")[1]
            picked_factions.append(nomination_faction)

            if nomination_player == player_name:
                if nomination_faction == chosen_faction:
                    break # Same player and faction, no change
                else:
                    if chosen_faction in nominated_factions:
                        draft_lines.append(f"Faction seconded by player {player_name}: {chosen_faction}")
                        picked_factions.append(chosen_faction)
                        draft_lines.pop(i)
                        nominated_factions.remove(chosen_faction)
                        break
                    else:
                        draft_lines[i] = f"Faction nominated by player {player_name}: {chosen_faction}"
                        picked_factions.remove(nomination_faction)
                        break

    else:
        draft_lines.append(f"Faction nominated by player {player_name}: {chosen_faction}")
        nominated_factions.append(chosen_faction)

    f.seek(0)
    f.write("\n".join(draft_lines))
    f.truncate()