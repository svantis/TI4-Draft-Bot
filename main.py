import PreparationPhase
import PickingPhase
import BanningPhase
import NominationPhase

# Prompt the user to select a program
print("Which program would you like to run?")
print("1. PreparationPhase")
print("2. PickingPhase")
print("3. BanningPhase")
print("4. NominationPhase")
choice = input("Enter the number of the program you want to run: ")

# Run the selected program
if choice == "1":
    PreparationPhase.main()
elif choice == "2":
    PickingPhase.main()
elif choice == "3":
    BanningPhase.main()
elif choice == "4":
    NominationPhase.main()
else:
    print("Invalid choice. Please enter a number between 1 and 4.")