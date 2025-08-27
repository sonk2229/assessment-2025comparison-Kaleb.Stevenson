# Functions go here

def string_check(question, valid_ans_list, num_letters):
    """Checks that response is a float / integer than zero"""

    if string_check == "valid_ans_list":
        error = "please enter a metric system unit ."
    else:
        error = "Please enter an integer more than 0"

    while True:
        response = input(question).lower()

        for item in valid_ans_list:
            # check if the response is the entire word
            if response == item:
                return item
            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}")
    while True:
        response = string_check(question, valid_ans_list, num_letters, )


def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")


def num_check(question, ):
    """Checks Users enter a number"""

    error = "Oops - Please enter an number that is more than 9.99 for budget or enter a number for metric unit mass"

    while True:

        try:
            # Return the response if it's an integer
            response = float(input(question))
            return response

        except ValueError:
            print(error)


# Main Routine goes here
amount_of_ml_l_g_kg_list = ['millilitres', 'litre', 'grams', 'kilograms', ]
# Loop for testing purposes
while True:
    item_name = not_blank("Item Name: ")
    if item_name == "xxx":
        break
    amount_of_ml_l_g_kg = string_check("what type it is of the metric system ",
                                       amount_of_ml_l_g_kg_list, 1)
    ask_metric_weight = num_check(f"how much mass is there of the metric unit ")
    if ask_metric_weight <= 0:
        print("Please enter a number that is more than or 0")
        continue
    ask_budget = num_check("How Much is the Budget ")
    if ask_budget < 10:
        print("Your Budget is to little you have to have a number that is 10 or greater for you budget")
        continue

    print(f"you chose {amount_of_ml_l_g_kg}")
    print(f"You bought {ask_metric_weight} {amount_of_ml_l_g_kg} of {item_name}")
    print(f"Your Budget is {ask_budget}")
    print()
