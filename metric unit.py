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


# Main Routine goes here
amount_of_ml_l_g_kg_list = ['millilitres', 'litre', 'grams', 'kilograms', 'xxx', ]
# Loop for testing purposes
while True:
    amount_of_ml_l_g_kg = string_check("what type it is of the metric system ",
                                       amount_of_ml_l_g_kg_list, 1)
    if amount_of_ml_l_g_kg == "xxx":
        print("You chose to break the code")
        break

    print(f"you chose {amount_of_ml_l_g_kg}")
