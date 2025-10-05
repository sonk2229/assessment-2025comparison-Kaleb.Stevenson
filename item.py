# Asks a question and if it is blank it returns the response
def not_blank(question):
    """Checks user response is not blank"""
    while True:
        response = input(question)
        if response != "":
            return response
        else:
            print("Sorry, this can't be blank.")


# Main Routine goes here

# Loop for testing purposes
while True:
    # Asking for the name of the item
    item_name = not_blank("Item Name: ")
    if item_name == "xxx":
        break

    print(f"{item_name}")

