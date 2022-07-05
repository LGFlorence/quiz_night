

user_choice = ""
pop_answers = ""
geo_answers = ""
history_answers = ""
incorrect = 0
correct = 0
choose = ""
question_input = ""


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


end_game = "no"
while end_game == "no":

    # Start of Game Play Loop

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
