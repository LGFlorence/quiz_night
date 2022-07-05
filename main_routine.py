def choice_checker(question):
    error = "Choose quiz genre, pop, geography or history."

    valid = False
    while not valid:

        # Ask user for choice
        response = input(question).lower()

        if response == "p" or response == "pop":
            return "pop"
        elif response == "g" or response == "geography":
            return "geography"
        elif response == "h" or response == "history":
            return "history"


def check_rounds():
    while True:
        print()
        round_heading = "Rounds"
        decorations = "+"
        statement_generator(round_heading, decorations)
        print()
        response = input("How many rounds would you like to play? (1 - 10 available to choose from):   ")

        round_error = "Please type either <enter>" \
                      " or an integer that is more than 0 and less or equal to 10."

        if response != "":
            try:
                response = int(response)

                if response < 1 or response > 10:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def statement_generator(statement, decorations) -> object:
    sides = decorations * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decorations * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


def instructions():
    print()
    instruction_heading = "Instructions"
    decorations = "+"
    statement_generator(instruction_heading, decorations)

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


# Main Routine

# Relevant lists
yes_no_list = ["yes", "no"]

pop_questions = ["Where is Billie Eilish from?",
                 "What city do The Beatles come from?",
                 "What is the all-time most-streamed song on Spotify to date?",
                 "What is the most-streamed album on Spotify in 2019?",
                 "How many keys does a classic piano have?",
                 "Which famous American pop band was originally called ‘Kara’s Flowers’?",
                 "When was Netflix founded: 1997, 2001, 2009, 2015?",
                 "Name Pixar’s first feature-length movie?",
                 "What is the name of the coffee shop in the sitcom Friends?",
                 "Name Disney’s first film?"]
geo_questions = ["What is the only country that borders the United Kingdom?",
                 "Ninety percent of the Earth’s population lives in which hemisphere?",
                 "In which country would you find the city of Dresden?",
                 "What would you call someone from Sudan?",
                 "What are the names of South Africa’s three capital cities?",
                 "How many time zones does Australia have?",
                 "Which continent is in all four hemispheres?",
                 "What is The Netherlands also called?",
                 "What is the official currency of India?",
                 "What ocean is New Zealand situate in?"]
history_questions = ["When did the construction of the Great Wall of China begin?",
                     "Who sent Christopher Columbus to explore the New World?",
                     "What is considered the largest empire in history?",
                     "What year did the French Revolution start?",
                     "What event is commonly believed to have sparked World War I?",
                     "Who was the last Tsar of Russia?",
                     "How many Celtic languages are still spoken today?",
                     "In what year did Libya gain independence from Italy?",
                     "Where did Albert Einstein live before moving to the United States?",
                     "Who is commonly referred to as the person who created the first printing press?"]

pop_answers = ["los angeles",
               "liverpool",
               "the shape of you",
               "when we fall asleep, where do we go?",
               "88",
               "maroon 5",
               "1997",
               "toy story",
               "central perk",
               "snow white"]
geo_answers = ["ireland",
               "the northern hemisphere",
               "germany",
               "sudanese",
               "cape town, pretoria, and bloemfontein",
               "three",
               "africa",
               "holland",
               "indian rupee",
               "south pacific ocean"]
history_answers = ["7th century ",
                   "king ferdinand of spain",
                   "the mongol empire",
                   "1789",
                   "the assassination of archduke franz ferdinand",
                   "nicholas II",
                   "6",
                   "1951",
                   "germany",
                   "johannes gutenberg"]

game_summary = []

# Welcome message
welcome = "Welcome to Quiz Night"
decorations = "|"
statement_generator(welcome, decorations)

# Ask user if they would like to see instructions
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

# Ask user for choice and check if valid
print()
genre_heading = "Quiz Genre"
decorations = "+"
statement_generator(genre_heading, decorations)
print()
user_choice = choice_checker("Choose quiz genre, pop, geography or history : ")

# print out choices for comparison purposes
print("You chose the {} quiz genre.".format(user_choice))
print()
print()

question_input = "Please place your answer to the previous question"

rounds_played = 0
correct = 0
incorrect = 0

# Ask user for # of rounds, <enter> for continuous mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

    # Break loop if round exceed ten
    if rounds_played >= 10:
        break

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode:  " \
                  "Round {}".format(rounds_played + 1)

        print()
        decorations = "X"
        statement_generator(heading, decorations)

    else:
        heading = "Rounds {} of " \
                  "{}".format(rounds_played + 1, rounds)

        print()
        decorations = "~"
        statement_generator(heading, decorations)

    print()
    print("Question:")

    # Print questions relevant to genre choice
    if user_choice == "pop":
        print(pop_questions[0])
        pop_questions.pop(0)

    elif user_choice == "geography":
        print(geo_questions[0])
        geo_questions.pop(0)

    elif user_choice == "history":
        print(history_questions[0])
        history_questions.pop(0)

    print()

    # Ask for user input (users answer to question)

    choose = input("{} or 'xxx' to "
                   "end : ".format(question_input)).lower()

    # Print answer to question and compare 'choose' (user answer) with actual answer
    # output if correct or no
    # add to correct of incorrect score

    # End game if exit code is typed
    if choose == "xxx":
        break

    if user_choice == "pop":
        print()
        print("The answer to this question is :")
        print(pop_answers[0])

        if choose == pop_answers[0]:
            result = "You answered correctly"
            print(result)
            correct += 1

        else:
            result = "You answered incorrectly"
            print(result)
            incorrect += 1

    pop_answers.pop(0)

    if user_choice == "geography":
        print()
        print("The answer to this question is :")
        print(geo_answers[0])

        if choose == geo_answers[0]:
            result = "You answered correctly"
            print(result)
            correct += 1

        else:
            result = "You answered incorrectly"
            print(result)
            incorrect += 1

    geo_answers.pop(0)

    if user_choice == "history":
        print()
        print("The answer to this question is :")
        print(history_answers[0])

        if choose == history_answers[0]:
            result = "You answered correctly"
            print(result)
            correct += 1

        else:
            result = "You answered incorrectly"
            print(result)
            incorrect += 1

    history_answers.pop(0)

    game_summary.append(result)

    rounds_played += 1

    # End game if requested # of rounds has been played or all questions answered
    if rounds_played == rounds:
        break

# End of game summaries 

print()
print()
end_game_heading = "End Game Summary"
decorations = "+"
statement_generator(end_game_heading, decorations)
print()
print("Correct: {} \t|\t Incorrect: {}".format(correct, incorrect))
print()

# Quick Calculations (winner, percentage results)

if correct > incorrect:
    print("You got more answers correct than incorrect! You won at Quiz Night!")
elif correct < incorrect:
    print("You got more answers incorrect than correct. You lost at Quiz Night!")
else:
    print("You got the same amount of answers correct as incorrect. You tied at Quiz Night! ")

# Game Statistics
if correct or incorrect > 0:
    percent_win = correct / rounds_played * 100
    percent_lose = incorrect / rounds_played * 100

else:
    percent_win = 0
    percent_lose = 0

# displays game stats with : values to the nearest whole number
print()
print("Game Statistics")
print("Won: {} - ({:.0f}%)\nLost: {} -"
      "({:.0f}%)".format(correct,
                         percent_win,
                         incorrect,
                         percent_lose))

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

# End game statements
print()
print()
print()
print("Thanks for playing")
print()
print()
ending_statement = " | The End | " * 20
decorations = "|"
statement_generator(ending_statement, decorations)
print()
