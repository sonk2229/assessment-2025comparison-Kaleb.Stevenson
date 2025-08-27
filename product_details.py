import pandas

# dictionaries to hold the details of the product
all_names_of_products = ["a", "b", "c", "d", "e"]
all_of_the_budgets = [20, 40, 60, 80, 100]

assessment_dict = {
    'Names': all_names_of_products,
    'Budgets': all_of_the_budgets
}

# create dataframe / table from dictionary
assessment_frame = pandas.DataFrame(assessment_dict)

# Calculate the total budget for each product
assessment_frame['Total'] = assessment_frame['Budgets'] - assessment_frame['Names']
assessment_frame['Left over Budgets'] = assessment_frame['Budgets']

# work out total paid and total left over budget...
total_paid = assessment_frame['Total'].sum()
total_left_over_budget = assessment_frame['Left over Budgets'].sum()

print(assessment_frame)
print()
print(f"Total Paid ${total_paid:.2f}")
print(f"Total Left over Budgets ${total_left_over_budget:.2f}")
