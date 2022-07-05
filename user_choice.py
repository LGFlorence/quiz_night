
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


# Ask user for choice and check if valid
print()
genre_heading = "Quiz Genre"
print(genre_heading)
print()
user_choice = choice_checker("Choose quiz genre, pop, geography or history : ")

# print out choices for comparison purposes
print("You chose the {} quiz genre.".format(user_choice))
print()
print()
