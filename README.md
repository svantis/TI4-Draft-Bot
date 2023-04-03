# TI4 Draft Bot

This is a tool for assisting in creating a faction pool for TI4 in a multi-step process where the players are able to affect what factions are available.

## Programs

There are four different programs, correlating to the different phases of the process. The Preparation phase needs to be run once, first. Then the other programs should be run once for each player.

1. `PreparationPhase`

   In this phase, the user lists the player who will partake in the draft and the program removes factions to make the amount of factions evenly divisible by the number of players and generates faction pools for each player. Expected input will be a list of all players.

2. `PickingPhase`

   In this phase, the players pick 1 of their available factions to include it in the faction pool. Players are able to change their choice until the BanningPhase has started. Expected input will be the date of the game in question, the name of the player making his choice, and the choice in question.

3. `BanningPhase`

   In this phase, the players ban one of their remaining factions so that it is unable to be nominated. Players are able to change their choice until the Nomination phase has started. Expected input will be the date of the game in question, the name of the player making their choice, and the choice in question.

4. `NominationPhase`

   Here, the users, in order, nominate a faction not picked or banned to be potentially added to the picking pool. If two players choose the same faction, it gets added to the pool. Expected input will be the date of the game in question, the name of the player making their choice, and the choice in question.

## Usage

I plan to add a `main.py` so that users only have to run that and choose what part of the draft they want to do, but for now, the different parts must be run separately. The instructions are decently clear in the programs. To run them, write `./{name_of_program}.py` in your terminal of choice, for example, `./PreparationPhase.py`. No command line arguments are required, but it is important that you are in the same folder as the programs to properly access the created drafts in the `Drafts` folder.
I have also not added functionality to select the game_date in the preparation phase, it currently just selects the current date.

## License

This project is licensed under the MIT License.