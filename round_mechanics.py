
def check_rounds():
    while True:
        print()
        round_heading = "Rounds"
        print(round_heading)
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
        print(heading)

    else:
        heading = "Rounds {} of " \
                  "{}".format(rounds_played + 1, rounds)

        print()
        print(heading)
