def num_check(question):
    """Checks Users enter a number"""

    error = ("Oops - Please enter an number"
             "")

    while True:

        try:
            # Return the response if it's an integer
            response = float(input(question))
            return response

        except ValueError:
            print(error)


# Main Routine goes here

while True:
    ask_metric_weight = num_check(f"how much mass is there of the metric unit ")
    if ask_metric_weight <= 0:
        print("Please enter a number that is more than or 0")
        continue
    print(f"you have {ask_metric_weight} of mass ")
