

user_choice = ""
pop_answers = ""
geo_answers = ""
history_answers = ""
incorrect = 0
correct = 0
choose = ""

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



