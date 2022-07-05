

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

