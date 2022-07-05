
# Game History

history = "Would you like to see your game history? (yes/no)"

# Checks if user wants game history to be displayed
while history != "yes" or "no":
    print()
    history = input("Would you like for game history to be displayed? \n"
                    "Please enter either yes or no : ").lower()
    print()

    if history == "yes":
        print("Game History:")
        print()

        # Print game history then break

        while range != rounds_played + 1:
            for item in range(1, (rounds_played + 1)):
                print("Round {}".format(item))
                print(game_summary[0])
                print()
                game_summary.pop(0)

            break
        break

    elif history == "no":
        break
