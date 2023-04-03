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

# check if the draft has not progressed to the banning phase
with open(f"./Drafts/{file_name}", "r") as f:
    draft_text = f.read()
    if "Banning Phase" in draft_text:
        print("The draft has progressed to the Banning Phase. Picking is not allowed anymore.")
        exit()

# get the player name
while True:
    player_name = input("Player: ")
    with open(f"./Drafts/{file_name}", "r") as f:
        draft_text = f.read()
        players = []
        for line in draft_text.split("\n"):
            if "Factions for player" in line:
                player = line.split("Factions for player ")[1].split(":")[0]
                players.append(player)
        if player_name in players:
            break
        else:
            print("Invalid player name. Please enter a valid player name.")

# get the chosen faction
with open(f"./Drafts/{file_name}", "r+") as f:
    draft_text = f.read()
    valid_factions = [f.strip("[]\"' ").replace("'", "").replace("\"", "") for f in draft_text.split(f"Factions for player {player_name}: ")[1].split("\n")[0].split(",")]
    while True:
        chosen_faction = input(f"Faction Pool ({', '.join(valid_factions)}): ")
        if chosen_faction in valid_factions:
            break
        else:
            print("Invalid faction choice. Please enter a valid faction.")

# write the result
    phase_header = "Picking Phase"
    if phase_header not in draft_text:
        f.seek(0, os.SEEK_END)
        f.write(f"\n{phase_header}\n\n")
    f.seek(0)
    draft_lines = f.readlines()
    for i in range(len(draft_lines)):
        if f"Faction added by player {player_name}: " in draft_lines[i]:
            if chosen_faction in draft_lines[i]:
                break  # existing choice found, no need to overwrite
            else:
                draft_lines[i] = f"Faction added by player {player_name}: {chosen_faction}\n"
                break  # overwrite the existing line and exit the loop
    else:
        draft_lines.append(f"Faction added by player {player_name}: {chosen_faction}\n")
        # add new line at the end of the document
    f.seek(0)
    f.writelines(draft_lines)
    f.truncate()