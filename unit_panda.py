# Functions go here


def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")


def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""

    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:

        response = input(question)

        # check for exit code and return it if entered
        if response == exit_code:
            return response

        # check datatype is correct and that number
        # is more than zero
        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


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

def units_moneys(unit_amount, unit_dollar, unit_comp, unit_type):
    """Gets the dollar and gets the unit amount so you can / the unit for price for unit """


def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))
    print('''You first enter the item name then the item metric unit, then how much it is in ml,kg,L,g 
     if it is ml,g it will be / by 1000 so it can be l,kg after that you enter the budget.
     After it gets / it will change in to Unit so we can compare the weight/mass of the amount of unit.
     When done the code will print columns of the unit weight/mass, budget, unit price, price total,
     the unit p/w (price per 1kg/l == 1000g/ml weight of the unit divided), item names(the name of the item),
     item(price) and 
     ''')


# Main Routine goes here
print(make_statement("", ""))
want_instructions = yes_no_check("Do you want to see the instructions ")
if want_instructions == "yes":
    instructions()
print("program continues...")
# This is the list for the metric system
amount_of_ml_l_g_kg_unit = ['ml', 'l', 'g', 'kg', ]
# Loop for testing purposes
while True:
    # This is the name for the items
    item_name = not_blank("Item Name: ")
    if item_name == "xxx":
        break
    item_price = num_check(f"What is the price of the item ")
    item_amount = num_check(f"how many items are there ")
    # This is asking for the type of metric system ranging from ml, L, g and Kg
    amount_of_ml_l_g_kg = string_check("what type it is of the metric system ",
                                       amount_of_ml_l_g_kg_unit, 1)
    unit_type = amount_of_ml_l_g_kg
    # if the answer to the metric system is ml, g it will /1000 and the unit will change to l, kg if not nothing changes
    if amount_of_ml_l_g_kg == 'kg':
        ask_metric_weight = num_check(f"how much mass is there of the Items ")
    elif amount_of_ml_l_g_kg == 'l':
        ask_metric_weight = num_check(f"how much mass is there of the Items ")
    elif amount_of_ml_l_g_kg == 'g':
        amount_of_ml_l_g_kg = 'kg'
        ask_metric_weight = num_check(f"how much mass is there of the Items ") / 1000
    elif amount_of_ml_l_g_kg == 'ml':
        amount_of_ml_l_g_kg = 'l'
        ask_metric_weight = num_check(f"how much mass is there of the Items ") / 1000
    # this is asking for the budget it has to be 10 or more
    ask_budget = num_check("How Much is the Budget ")
    if ask_budget < 10:
        print("Your Budget is to little you have to have a number that is 10 or greater for you budget")

    unit_type = 'unit'

    # Shows the results of the code working
    print(f"You bought {ask_metric_weight}{amount_of_ml_l_g_kg} of {item_name}")
    print(f"The cost of the {item_name} being ${item_price} per  and the amount {item_amount}")
    print(f"The budget to spend ${ask_budget}")
    print()
