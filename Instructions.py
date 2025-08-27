# functions go here
def make_statement(statement, decoration):
    """Emphasises heading by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"


def yes_no_check(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:

        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (no).\n")


def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))
    print('''You first enter the item name then the item metric unit, then how much it is in ml,kg,L,g 
    after that you enter the budget.''')


# Main routine goes here
print(make_statement("", ""))
want_instructions = yes_no_check("Do you want to see the instructions ")
print()

if want_instructions == "yes":
    instructions()

print()
print("program continues...")
