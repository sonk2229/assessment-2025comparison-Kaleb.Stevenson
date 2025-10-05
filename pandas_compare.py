import pandas


# lists to hold details
name = ["A", "B", "C", "D", "E"]
metric_mass = [2000, 3000, 1000, 2500, 5000]
budget = [150, 300, 450, 600, 750]
price = [80, 124, 202, 256, 425]

compare_assessment_dict = {
    'Item': name,
    'Mass': metric_mass,
    'Budget': budget,
    'Item Price': price
}

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
