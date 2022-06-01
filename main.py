# Ask the user for their current age (in years)
age = input("What is your current age? \n")

# Need to calculate how many years left until 90
years_left = 90 - int(age)

# Calculate the number of remainding days, weeks and months
remainding_months = years_left * 12
remainding_weeks = years_left * 52
remainding_days = years_left * 365

# Print out the result for the end user

print(f"You have {remainding_days} days, {remainding_weeks} weeks, and {remainding_months} months left")

# Execution end.