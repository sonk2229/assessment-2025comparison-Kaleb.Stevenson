# Functions go here

def num_check(question):
    """Checks Users enter a number"""

    error = "Oops - Please enter an number that is more than 9.99"

    while True:

        try:
            # Return the response if it's an integer
            response = float(input(question))
            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")


# pay_method = string_check("Payment method: ", payment_ans, 2)
# print(f"You chose {pay_method}")

# currency formatting function


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# main routine starts here
while True:
    ask_budget = num_check("How Much is the Budget ")
    if ask_budget < 10:
        print("Your Budget is to little you have to have a number that is 10 or greater for you budget")
        continue
    if ask_budget == "xxx":
        break

    print(f"Your Budget is  {ask_budget}")
    print()
