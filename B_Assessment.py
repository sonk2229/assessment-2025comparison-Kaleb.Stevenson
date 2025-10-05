import pandas


# Functions go here

# Asks a question and if it is blank it returns the response
def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")

# Is a number checker for the mass of the item and the budget
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

# Makes a statement ment for decorations and the instructions
def make_statement(statement, decoration):
    """Emphasises heading by adding decoration
     at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}\n"

# Asking Yes no with Y and n and returns response if it is not y/n
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

# String checker asking a question and having a list for the metric units
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

def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - Please enter an number more than zero."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)

# Makes the instructions using make statement
def instructions():
    """Displays instructions"""
    print(make_statement("Instructions", "ℹ️"))
    print('''You first enter the item name then the item metric unit, then how much it is in ml,kg,L,g 
     if it is ml,g it will be / by 1000 so it can be l,kg after that you enter the budget.
     After it gets / it will change in to Unit so we can compare the weight/mass of the amount of unit.
     When done the code will print columns of the unit weight/mass, budget, unit price(per kg/l aka 1000g/ml),
     item names(the name of the item).''')

# currency formatting function
def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Main routine starts here
print(make_statement("", ""))
want_instructions = yes_no_check("Do you want to see the instructions ")
if want_instructions == "yes":
    instructions()
print("program continues...")

# This is the list for the metric system
amount_of_ml_l_g_kg_unit = ['ml', 'l', 'g', 'kg', ]

# Initialise items
MAX_ITEMS = 5
items_bought = 0


# Loop to get item name, price,mass, and metric unit
while items_bought < MAX_ITEMS:

    # This is the name for the items
    item_name = not_blank("Item Name: ")
    if item_name == "xxx":
        break
    item_price = num_check("Price of the Item: ")
    # This is asking for the type of metric system ranging from ml, L, g and Kg
    amount_of_ml_l_g_kg = string_check("what type it is of the metric system ",
                                       amount_of_ml_l_g_kg_unit, 1)
    unit_type = amount_of_ml_l_g_kg

    # if the answer to the metric system is ml, g it will /1000 and the unit will change to l, kg if not nothing changes
    if amount_of_ml_l_g_kg == 'kg':
        ask_metric_weight = num_check(f"how much mass is there in Total for the Item ")

    elif amount_of_ml_l_g_kg == 'l':
        ask_metric_weight = num_check(f"how much mass is there in Total for the Item ")

    elif amount_of_ml_l_g_kg == 'g':
        amount_of_ml_l_g_kg = 'kg'
        ask_metric_weight = num_check(f"how much mass is there in Total for the Item ") / 1000

    elif amount_of_ml_l_g_kg == 'ml':
        amount_of_ml_l_g_kg = 'l'
        ask_metric_weight = num_check(f"how much mass is there in Total for the Item ") / 1000

    # this is asking for the budget it has to be 10 or more
    ask_budget = num_check("How Much is the Budget ")
    if ask_budget < 10:
        print("Your Budget is to little you have to have a number that is 10 or greater for you budget")

    unit_type = 'unit'

    break_idk = yes_no_check("Do you want to break ")
    if break_idk == "yes":
        break

# lists to hold details
name = []
metric_mass = []
budget = []
price = []

compare_assessment_dict = {
    'Item': name,
    'Mass': metric_mass,
    'Budget': budget,
    'Item Price': price
}

name.append(item_name)
metric_mass.append(ask_metric_weight)
budget.append(ask_budget)
price.append(item_price)



items_bought += 1

# End of loop

# create dataframe / table from dictionary
compare_assessment_frame = pandas.DataFrame(compare_assessment_dict)

# Calculate the mass / budget for each item
compare_assessment_frame['Total'] = compare_assessment_frame['Budget'] - compare_assessment_frame['Item Price']
compare_assessment_frame['Spent'] = compare_assessment_frame['Item Price'] - 1 + 1
compare_assessment_frame['Price Mass'] = compare_assessment_frame['Mass'] / compare_assessment_frame['Item Price']

# Work out the total paid and total left over...
total_paid = compare_assessment_frame['Total'].sum()
total_price = compare_assessment_frame['Spent'].sum()
total_price_mass = compare_assessment_frame['Price Mass'].sum()

print(compare_assessment_frame)
print()
print(f"Total Paid ${total_paid:.2f}")
print(f"Total Price ${total_price:.2f}")
print(f"Total Price Mass ${total_price_mass:.2f}")

# Shows the results of the code after doing all the questions
print(f"You bought {ask_metric_weight}{amount_of_ml_l_g_kg} of {item_name}")
print(f"The price is ${item_price}")
print(f"The budget ${ask_budget}")
print()
