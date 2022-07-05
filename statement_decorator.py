
def statement_generator(statement, decorations) -> object:
    sides = decorations * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decorations * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""
