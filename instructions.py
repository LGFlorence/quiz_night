
def instructions():
    print()
    instruction_heading = "Instructions"
    print(instruction_heading)

    print()
    print("First, choose your quiz genre . \n"
          "Enter how many rounds you would like to play (up to 10), if you press <enter> the amount of rounds " 
          "that will be played will be automatically set to 10. \n"
          "Each round you will be asked to answer a quiz question relevant to the genre you picked \n"
          "Then the answer to the question will be uncovered \n"
          "You can quit anytime by entering 'xxx'. \n"
          "If you have selected a certain number of rounds, the game will automatically finish once all "
          "rounds have been played. \n"
          "The objective is to win as many rounds as possible by getting all the questions correct. \n"
          "Game statistics are shown at the end which inform you if you have one or lost the game. \n"
          "Game history can be shown at the end if you answer yes when asked if you want to see it. \n"
          "Enjoy and good luck!")

    print()
    return ""


display_instructions = ""

while display_instructions != "yes" or "no":
    print()
    print()
    display_instructions = input("Would you like for instructions to be displayed? \n"
                                 "Please enter either yes or no : ").lower()

    # if yes, display instructions
    if display_instructions == "yes":
        # print instructions
        print()
        print(instructions())
        break

    elif display_instructions == "no":
        break
